---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-crs-express-12-5-1-su1-maintain-and-operate-guid-3ba9f9e596
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/crs/express_12_5_1_su1/maintain_and_operate/guide/uccx_b_1251su1admin-and-operations-guide/uccx_b_12_5_2admin-and-operations-guide_chapter_011001.html
retrieved_at: 2026-08-16T21:40:01.801097+00:00
---

Cisco Unified Contact Center Express Administration and Operations Guide, Release 12.5(1)SU1

# Cisco Unified Contact Center Express Administration and Operations Guide, Release 12.5(1)SU1

Updated: January 31, 2021

Chapter: Cisco Unified CCX Serviceability

## Chapter: Cisco Unified CCX Serviceability

# Cisco Unified CCX Serviceability

## Cisco Unified CCX Serviceability

### Access Cisco Unified CCX Serviceability

When you
                                 		  complete the AppAdmin inital setup, the end user with administrator capability
                                 		  as configured in AppAdmin web interface can login to Cisco Unified CCX Serviceability. You can also log in as an
                                 		  Application user with default administrator capability configured during the
                                 		  installation of Unified CCX . See the Cisco Unified Contact
                                          				  Center Express Install and Upgrade Guide and Cisco Unified Contact Center Express Administration Guide for detailed instructions on initial AppAdmin setup and how to
                                 		  assign administrator capability to end users.

To access Cisco Unified CCX Serviceability:

Step 1

By using a
                                          			 supported web browser, open a browser session.

Step 2

Go to https://<server name or IP
                                                				  address>/uccxservice/.

Step 3

Enter an
                                          			 applicable username and password, and click Login .

If you log in as an end user,
                                                         				  you can access Cisco Unified CCX Administration 
                                                         				   from the Navigation drop-down list box without logging in
                                                         				  again. If you log in as an Application user, you can access Cisco Unified
                                                         				  Serviceability in addition to these web applications.

## Alarms

Cisco Unified CCX Serviceability alarms provide information on runtime status and
                              		  the state of the system so that you can monitor the status and troubleshoot
                              		  problems that are associated with the system. Alarm information includes the
                              		  catalog, name, severity, explanation, recommended action, routing list, and
                              		  parameters.

You can
                              		  view alarm information by using the SysLog Viewer in Cisco Unified Real-Time
                              		  Monitoring Tool (RTMT). See Cisco Unified Real-Time
                                          				  Monitoring Tool Administration Guide for Cisco Unified Contact Center Express
                                          				  and Cisco Unified IP IVR for detailed information on how to view alarm information.

Use the Alarm
                                          			 Definitions web page in Cisco Unified Serviceability to find information about
                                          			 an alarm message.

For information on alarm definitions, see the Cisco Unified Serviceability Administration Guide available at: https://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-callmanager/products-maintenance-guides-list.html .

### Alarm
                           	 Configuration

Use the Alarm Configuration
                                 		  web page in Unified CCX Serviceability to view and configure alarm server
                                 		  settings for different Unified CCX components.

Alarm Server Configuration is
                                             			 applicable for the following Unified CCX components: Unified CCX
                                             			 Administration, Unified CCX Engine, and Unified CCX Cluster View Daemon .

The alarm
                                 		  configuration submenu allows you to:

Enable or
                                       				disable sending of alarms to local or remote syslog server.

Configure alarm
                                       				event level for local or remote syslog server

Select Alarm > Configuration from the Cisco Unified CCX Serviceability menu bar to access the Alarm Configuration web
                                 		  page.

### Configure Alarm
                           	 Settings

The Alarm
                                 		  Configuration page is used to view and update Cisco Unified
                                    			 CCX Alarm
                                 		  Configuration for local and remote syslogs.

Step 1

From the Unified
                                             				CCX Serviceability menu bar, choose Alarm and click Configuration .

The Alarm
                                             				Configuration web page opens and the following fields are displayed on the
                                             				Alarm Configuration web page, if configured on your Unified
                                                				  CCX server:

Field

Description

Local Syslogs

Enable
                                                         							 Alarm

Use
                                                         							 the check box next to Enable Alarm field to enable or disable the alarms for
                                                         							 local syslog.

Alarm
                                                         							 Event Level

Lists
                                                         							 the alarm severity level.

Remote Syslogs

Enable
                                                         							 Alarm

Use
                                                         							 the check box next to Enable Alarm field to enable or disable the alarms for
                                                         							 remote syslog.

Alarm
                                                         							 Event Level

Lists
                                                         							 the alarm severity level.

Server
                                                         							 Name

IP address or hostname of the Syslog server to which system should send the alarm messages. If you are using CiscoWorks, enter
                                                         the IP address or the hostname of the CiscoWorks server.

Step 2

To update the
                                          			 Alarm Event Level for local or remote syslogs, check the check box before
                                          			 Enable Alarm field.

Step 3

Modify Alarm
                                          			 Event Level for the local or remote syslogs by selecting from the Alarm Event
                                          			 Level drop-down list. Modify the syslog server name in case of remote syslog.

Step 4

Click Update icon that displays in the tool bar in the
                                          			 upper, left corner of the window or the Update button that displays at the bottom of the
                                          			 window to save your configuration. Click Clear to reset data to the previous values.

In case of a High
                                             				Availability deployment, the alarm configuration changes are automatically
                                             				propagated to the second node. If the second node cannot be contacted, an alert
                                             				message indicating that the update has failed on the remote node is displayed.

Caution

You should
                                                         				  activate logging only for
                                                         				  the purpose of debugging and remember to deactivate logging once the debugging session is complete.

### Alarm Configuration
                           	 Settings

Use the Alarm Configuration page to modify alarm
                                 		  settings.

In the case of a High Availability deployment, the alarm configuration
                                 		  changes are automatically propagated to the second node. If the second node
                                 		  cannot be contacted, an alert message indicating that the update has failed on
                                 		  the remote node is displayed.

Following table defines the options available on this page:

Setting

Description

Enable Alarm
                                          					 for Local Syslogs

The SysLog
                                          					 viewer serves as the alarm destination. The program logs errors in the
                                          					 Application Logs within SysLog Viewer and provides a description of the alarm
                                          					 and a recommended action. You can access the SysLog Viewer from the Cisco
                                          					 Unified Real-Time Monitoring Tool.

For information on viewing
                                          					 logs with the SysLog Viewer, see Cisco Unified Real-Time
                                                   				  Monitoring Tool Administration Guide for Cisco Unified Contact Center Express
                                                   				  and Cisco Unified IP IVR .

Enable Alarm
                                          					 for Remote Syslogs

The Syslog
                                          					 file serves as the alarm destination. Check this check box to enable the Syslog
                                          					 messages to be stored on a Syslog server and to specify the Syslog server name.

Alarm Event
                                          					 Level

Alarm event
                                          					 level messages range from severity 0 (most severe) to severity 7 (least severe)
                                          					 description of which is mentioned below. When you choose a severity level, all
                                          					 messages of that severity level and higher are sent.

For example,
                                          					 if you choose ERROR_ALARM (Severity 3), all messages of severity 3, severity 2,
                                          					 severity 1, and severity 0 are sent. The default is "INFORMATIONAL_ALARM (Severity 6)" , which will send messages
                                          					 of all severity levels starting from 6 to severity level 0.

## Traces

A trace
                              		  file is a log file that records activity from the Cisco Unified
                                 			 CCX components. Trace files let you obtain specific, detailed information about the
                              		  system that can help you troubleshoot problems.

The Cisco Unified
                                 			 CCX system
                              		  can generate trace information for different services. This information is
                              		  stored in a trace file. To help you control the size of a trace file, you can
                              		  specify the services for which you want to collect information and the level of
                              		  information that you want to collect.

The Cisco Unified
                                 			 CCX system
                              		  also generates information about all threads that are running on the system.
                              		  This information is stored in the thread dump file and is useful for
                              		  troubleshooting.

### Component Trace
                           	 Files

The component trace file
                                 		  contains information about each component. You can create a trace file for any
                                 		  of the following Unified CCX components:

Cisco Unified CCX Administration

Cisco Unified CCX Cluster View Daemon

Cisco Unified CCX Editor

Cisco Unified CCX Engine

Cisco Unified CM Telephony Client

Cisco Unified CCX Recording and Monitoring Services

Cisco Unified CCX Socket.IO Service

Administration

Engine

You must use Cisco Unified Intelligence Center CLIs for Log Trace Settings. For more
                                             					information see Cisco Unified Intelligence Center
                                                						Commands .

The component
                                 		  trace file contains information about each component. To set up the trace file,
                                 		  follow the procedure mentioned in Configure Trace Parameters section.

After configuring the
                                 		  information that you want to include in the trace files for the various
                                 		  services, you can collect and view trace files by using the trace and log
                                 		  central option in the Cisco Unified Real-Time Monitoring Tool. See Cisco Unified Real-Time
                                          				  Monitoring Tool Administration Guide for Cisco Unified Contact Center Express
                                          				  and Cisco Unified IP IVR for detailed information.

### Configure Trace
                           	 Parameters

To
                                 		  update trace file information and to activate and deactivate logging, follow
                                 		  the procedure mentioned below:

Step 1

From the Cisco Unified CCX
                                             				Serviceability menu bar, choose Trace > Configuration .

The Trace Configuration web
                                             				page opens displaying the default trace configuration for Unified CCX Engine.

Step 2

From the Select
                                             				Service drop-down list box, choose a service or component for which
                                          			 you want to configure trace then, click Go .

You should be
                                             				able to view the existing Trace configurations and debug levels for the
                                             				selected Unified CCX service with
                                             				check boxes for the various Debugging and XDebugging levels for each sub
                                             				facility.

The debug levels for different Unified CCX subfacilities or services might vary depending on the selected service and are
                                             listed in the following table:

Cisco Unified CCX Components

Subfacilities or Services

Cisco Unified CCX Administration

Libraries

Managers

Miscellaneous

Cisco Unified CCX Cluster View Daemon

Libraries

Managers

Miscellaneous

Cisco Unified CCX Editor

Libraries

Managers

Miscellaneous

Steps

Cisco Identity Service

Error

Warning

Information

Debugging

Cisco Unified CCX Engine

Libraries

Managers

Miscellaneous

Steps

Subsystems

Cisco Unified CM Telephony Client or JTAPI Debug Levels

Warning

Information

Debugging

Cisco Unified CCX Socket.IO Service

Service

DataProcessing

Communication

Step 3

Update the
                                          			 debug level for one or more of the libraries or sub facilities for the selected
                                          			 service by doing the following:

To
                                                				  activate traces for a specific component or logging for a server, check the
                                                				  check box for the service that you chose.

To
                                                				  deactivate logging for a server, uncheck the specific check box.

Caution

Step 4

To limit the
                                          			 number and size of the trace files, you can specify the trace output setting
                                          			 using the following two fields. See the following table for description and
                                          			 default values for these two fields.

Field

Description

Maximum No. of Files

The maximum number of trace files to be retained by the system.

This field specifies the total number of trace files for a given
                                                         							 service. Cisco Unified CCX Serviceability automatically appends a sequence number to the file name to
                                                         							 indicate which file it is; for example, Cisco001MADM14.log. When the last file
                                                         							 in the sequence is full, the trace data begins writing over the first file. The
                                                         							 default value varies by service.

Maximum File Size

This field specifies the maximum size of the trace file in
                                                         							 kilobytes or megabytes depending on the selected service. The default value
                                                         							 varies by service.

Step 5

Click Save icon that displays in the tool bar in the
                                          			 upper, left corner of the window or the Save button that displays at the bottom of the
                                          			 window to save your trace parameter configuration. The settings are updated in
                                          			 the system and the trace files will be generated as per the saved settings.
                                          			 Click Restore Defaults icon or button to revert to the
                                          			 default settings for the selected service.

In a High
                                             				Availability deployment, the changes are propagated to the second node. If the
                                             				second node cannot be contacted, an alert message indicating that the update
                                             				has failed on the remote node is displayed.

Caution

### Trace Level
                           	 Options

A trace
                                 		  file is a log file that records activity from the Cisco Unified CCX component
                                 		  subsystems and steps. Trace files let you obtain specific, detailed information
                                 		  about the system that can help you troubleshoot problems.

The Cisco Unified CCX system can
                                 		  generate trace information for every component. This information is stored in
                                 		  an trace file. To help you control the size of an trace file, you specify the
                                 		  components for which you want to collect information and the level of
                                 		  information that you want to collect.

A trace
                                 		  file that records all information for a component, such as the Cisco Unified CCX Engine, can become large and difficult to read. To help you manage the trace
                                 		  file, the Cisco Unified CCX system lets
                                 		  you specify the subfacilities for which you want to record information.

For each
                                 		  component, you can select one or more Debugging trace levels. These selections
                                 		  specify the level of details in the debugging messages that the system sends to
                                 		  a trace file. For instance, if you select Debugging, the system sends only the
                                 		  basic error messages while if you select XDebugging5, the system will send
                                 		  errors, warnings, informational, debugging, verbose messages and so on in
                                 		  detail to the trace file.

The table
                                 		  below describes the Trace file subfacilities.

Component
                                             					 Code

Description

AC_CLUSTER

Archive
                                             					 Cluster Component

AC_CONFIG

Archive
                                             					 Configuration Component

AC_DATABASE

Archive
                                             					 Database Component

AC_JTAPI

JTAPI
                                             					 Archive Component

AC_OS

Archive
                                             					 Operating System Component

ADM

Administration Client

ADM_CFG

Administration Configuration

APP_MGR

Applications Manager

ARCHIVE_MGR

Archive
                                             					 Manager

AW_CFG

Restore
                                             					 Administration Configuration

BARBI_CLI

Backup and
                                             					 Restore Client Interface

BOOTSTRAP_MGR

Cisco
                                             					 Unified CCX Bootstrap Manager

CFG_MGR

Configuration Manager

CHANNEL_MGR

Channel
                                             					 Manager

CLUSTER_MGR

Cluster
                                             					 Manager

CONTACT_MGR

Contact
                                             					 Manager

CONTACT_STEPS

Contact
                                             					 Steps

CRA_CMM

Cisco
                                             					 Unified CCX ClusterMsgMgr Component

CRA_HRDM

Cisco
                                             					 Unified CCX Historical Reporting Data Manager

CVD

Cluster
                                             					 View Daemon

DB

Database

DBPURGE_MGR

Database
                                             					 Purge Manager

DESKTOP

Cisco
                                             					 Unified CCX Editor Desktop

DOC_MGR

Document
                                             					 Manager

EDT

Cisco
                                             					 Unified CCX Editor general

ENG

Cisco
                                             					 Unified CCX Engine

EXECUTOR_MGR

Executor
                                             					 Manager

EXPR_MGR

Expression
                                             					 Manager

FILE_MGR

File
                                             					 Manager

GENERIC

Generic
                                             					 catalog for a facility

GRAMMAR_MGR

Grammar
                                             					 Manager

GRP_CFG

Group
                                             					 Configuration

HOLIDAY_MGR

Holiday
                                             					 Manager

HR_MGR

Historical
                                             					 Reports Manager

ICD_CTI

Cisco
                                             					 Unified CCX CTI Server

ICD_HDM

IPCC
                                             					 Express Historical Data Manager

ICD_RTDM

Cisco
                                             					 Unified CCX ICD Real-Time Data Manager

IVR_RTDM

Cisco
                                             					 Unified CCX IP IVR Real-Time Data Manager

IO_ICM

Cisco
                                             					 Unified ICME Input/Output

JASMIN

Java
                                             					 Signaling and Monitoring Interface

LIB_APPADMININTERCEPTOR

Cisco
                                             					 Unified CCX Administration Interceptor Library

LIB_AXL

AXL
                                             					 Library

LIB_CFG

Configuration Library

LIB_CLUSTER_CFG

Configuration Library for the cluster

LIB_CRTP

CRTP
                                             					 Library

LIB_DATABASE

Database
                                             					 Library

LIB_DIRECTORY

Directory
                                             					 Access Library

LIB_EVENT

Event
                                             					 Message Library

LIB_ICM

Cisco
                                             					 Unified ICME Library

LIB_JASPER

Jasper
                                             					 Tomcat Library

LIB_JCUP

JavaCup
                                             					 Library to parse expressions

LIB_JDBC

JDBC
                                             					 Library

LIB_JINI

JINI
                                             					 Services

LIB_JMAIL

Java Mail
                                             					 Library

LIB_JLEX

JLEX
                                             					 Library used to parse expressions

LIB_LICENSE

License
                                             					 Library

LIB_MEDIA

Media
                                             					 Library

LIB_RMI

Java
                                             					 Remote Method Invocation Library

LIB_SERVLET

Servlet
                                             					 Library

LIB_TC

Tomcat
                                             					 Library

LOG_MGR

Log
                                             					 Manager

MRCP_CFG

MRCP
                                             					 Configuration

MGR_MGR

Manager
                                             					 Manager

NODE_MGR

Node
                                             					 Manager

PALETTE

Editor
                                             					 Palette

PROMPT_MGR

Prompt
                                             					 Manager

PURGING

Purging

RPT

Reporting

RTPPORT_MGR

RTP
                                             					 Manager

SCRIPT_MGR

Script
                                             					 Manager

SESSION_MGR

Session
                                             					 Manager

SIP_STACK

SIP Stack
                                             					 logging

SOCKET_MGR

Socket
                                             					 Manager

SS_APP

Application Subsystem

SS_CHAT

Chat
                                             					 Subsystem

SS_CM

Contact
                                             					 Manager Subsystem

SS_CMT

Cisco
                                             					 Media Termination Subsystem

SS_DB

Database
                                             					 Subsystem

SS_EMAIL

Email
                                             					 Subsystem

SS_HTTP

HTTP
                                             					 Subsystem

SS_ICM

Cisco
                                             					 Unified ICME Subsystem

SS_MRCP_ASR

MRCP ASR
                                             					 Subsystem

SS_MRCP_TTS

MRCP TTS
                                             					 Subsystem

SS_OUTBOUND

Outbound
                                             					 Dialer Express Subsystem (uses MIVR log file)

SS_RM

Resource
                                             					 Manager Subsystem

SS_RMCM

Resource
                                             					 Manager Contact Manager Subsystem

SS_ROUTEANDQUEUE

Route and
                                             					 Queue Subsystem

SS_RTR

Real-Time
                                             					 Reporting Subsystem

SS_SIP

SIP
                                             					 Subsystem

SS_TEL

JTAPI
                                             					 Subsystem (Telephony)

STEP_CALL_CONTROL

Call
                                             					 Control Steps

STEP_MEDIA_CONTROL

Media
                                             					 Control Steps

STEP_SESSION

Sessions
                                             					 Steps

STEP_SESSION_MGMT

Session
                                             					 Management Steps

STEP_USER

User Steps

STEP_CALL_CONTACT

Call
                                             					 Contact Steps

STEPS_CONTACT

Contact
                                             					 Steps

STEPS_DB

Database
                                             					 Steps

STEPS_DOCUMENT

Document
                                             					 Steps

STEPS_EMAIL

E-mail
                                             					 Steps

STEPS_GENERAL

General
                                             					 Steps

STEPS_GRAMMAR

Grammar
                                             					 Steps

STEPS_HTTP

HTTP Steps

STEPS_ICM

Cisco
                                             					 Unified ICME Steps

STEPS_IPCC_EXP

Cisco
                                             					 Unified CCX Steps

STEPS_JAVA

Java Steps

STEPS_PROMPT

Prompt
                                             					 Steps

STEPS_SESSION

Session
                                             					 Steps

UCCX_WEBSERVICES

Chat
                                             					 Subsystem

USR_MGR

User
                                             					 Manager

WEB_STEPS

HTTP
                                             					 Contact Steps

When the Cisco Unified CCX
                                 		  product is running on a 7845 machine and tracing is ON (the default), limit the
                                 		  Busy Hour Call Completions (BHCC) to 4500 calls per hour. If you want to run a
                                 		  higher BHCC, turn the debug traces OFF. The trace subfacilities to be turned
                                 		  OFF are ICD_CTI, SS_TEL, SS_RM, SS_CM, and SS_RMCM.

### Trace file
                           	 location

The Unified
                                    			 CCX server stores the trace files in the Log directory under the directory in
                                    			 which you installed the Unified CCX component. You can collect and view
                                 		  trace information using the Real-Time Monitoring Tool (RTMT).

#### Trace File Information

The trace files contain information in standard Syslog format. The file includes some or all of the following information
                                    for each event that it records:

Line number

Date and time the event occurred

Facility and subfacility (component) name

Severity level

Message name

Explanation

Parameters and values

### Log Profiles
                           	 Management

Log
                                 		  Profile is an aggregated entity that preserves trace settings of the following Unified CCX services:

Cisco Unified
                                          				CCX Engine (Traces termed as MIVR)

Cisco Unified
                                          				CCX Administration (Traces termed as MADM)

Cisco Unified
                                          				CCX Cluster View Daemon (Traces termed as MCVD)

Choose Trace > Profile from the Unified CCX Serviceability menu bar to access the Log Profiles Management web
                                 		  page. The Log Profiles Management web page opens displaying the available log
                                 		  profiles each with a radio button. You can perform different operations on the
                                 		  listed log profiles, which are explained in detail in the following
                                 		  sub-sections.

Log
                                 		  profiles in Unified CCX can be one
                                 		  of the following two types:

System Log
                                          				Profiles: These log profiles are pre-installed with Unified CCX and you
                                          				cannot modify these profiles.

The following
                                          				table provides information on the log profiles that are factory shipped with Unified CCX :

Name

Scenario
                                                         					 in which this profile must be activated

Default

Activate
                                                         					 this profile once an issue is resolved.

Outbound

For issues
                                                         					 with Unified CCX Outbound Dialer AppAdmin.

AppAdmin

For issues
                                                         					 with web administration through AppAdmin, Unified CCX Serviceability, and other
                                                         					 web pages.

Media

For issues
                                                         					 with media setup or media transmission.

HRDM
                                                         					 (Historical Reporting Data Manager)

For
                                                         					 issues with historical data that is written to the database.

StuckSession

For
                                                         					 issues with application sessions, sessions that are not being deleted when
                                                         					 appropriate and appearing stuck in AppAdmin Real Time Reports.

Database

For issues
                                                         					 with Unified CCX Informix database.

EDBS
                                                         					 (Enterprise Database Subsystem)

For issues
                                                         					 with external database connectivity and integration.

CallsStuckInQueue

For issues
                                                         					 with calls in queue that are not being allocated to available agents or
                                                         					 appearing stuck in queue in reports.

Serviceability

For issues
                                                         					 with the functionality in Unified CCX Serviceability Administration Interface.

RealTimeDataProblems

For issues
                                                         					 with Real Time Reports in AppAdmin.

Custom Log
                                          			 Profiles: If the trace settings generated by system profiles are not sufficient
                                          			 in a particular scenario, you can create custom log profiles for better
                                          			 troubleshooting. You can upload and activate these custom log profiles, on a
                                          			 need basis.

In a HA
                                                               					 deployment of Unified CCX, all the log profile operations will be reflected on
                                                               					 both the nodes in the cluster.

You cannot
                                                               					 delete the profile if the selected log profile is the last-enabled profile in
                                                               					 the system.

#### Create
                              	 Profile

To create
                                    		  a log profile for a specific trace, perform the following steps:

Step 1

From the Unified CCX Serviceability menu bar, choose Trace > Profile . The Log Profiles Management
                                             			 web page displays.

Step 2

Click Add
                                                				New icon that displays in the tool bar in the upper, left corner of
                                             			 the window or the Add
                                                				New button that displays at the bottom of the window.

The Log Profile
                                                				Configuration web page displays. You can view lists of subfacilities such as
                                                				libraries, managers, steps, subsystems, and so on with check boxes for the
                                                				various Debugging and XDebugging levels for each subfacility for the MIVR tab
                                                				by default.

Step 3

Select desired
                                             			 trace setting for different subfacilities in a service by clicking the
                                             			 corresponding check box.

Step 4

Click MCVD and
                                             			 MADM tabs to navigate to view and enable trace setting for these profiles.

Step 5

On successful
                                             			 configuration of these log profiles, click Save to save the profile or Save and
                                                				Enable to save and enable the profile. The new profile will be
                                             			 displayed in the main profile page.

#### Save as Another
                              	 Profile

To save an
                                    		  existing profile as another profile, perform the following steps:

Step 1

From the Unified
                                                				CCX Serviceability menu bar, choose Trace > Profile . The Log Profiles Management
                                             			 web page displays.

Step 2

Click the radio
                                             			 button to select a log profile.

Step 3

Click Save
                                                				As .

The Log Profile
                                                				Configuration web page for the selected profile is displayed where you can view
                                                				and update the existing profile settings. Click MIVR , MCVD, and MADM tabs to
                                                				view and modify the trace settings.

Step 4

You can save
                                             			 these updated trace settings with a new name. You will see a message confirming
                                             			 successful saving of the new profile.

#### Enable
                              	 Profile

To enable
                                    		  or activate a log profile, perform the following steps:

Step 1

From the Unified
                                                				CCX Serviceability menu bar, choose Trace > Profile . The Log Profiles Management
                                             			 web page displays.

You can enable a
                                                				log profile using any one of the following methods from the Log Profiles
                                                				Management web page:

Select the
                                                   				  radio button for the profile and click Enable icon or button

Click the
                                                   				  hyperlink for the desired profile. Log Profile Configuration web page for the
                                                   				  selected profile is displayed. Click Enable icon or button in the Profile Configuration
                                                   				  web page

Click Add
                                                      					 New . Enter the desired trace settings in the Profile Configuration
                                                   				  web page and click Save
                                                      					 and Enable icon or button in the Profile Configuration web page.

Step 2

The trace
                                             			 setting for the selected profile is transferred to system's trace settings and
                                             			 on successful activation, a message will be displayed in the status bar.

#### Delete
                              	 Profile

To delete
                                    		  an existing log profile, perform the following steps:

Step 1

From the Unified
                                                				CCX Serviceability menu bar, choose Trace > Profile .

Step 2

Select the radio
                                             			 button for an existing profile and click Delete icon or button to delete a log profile.

Alternatively,
                                                				you can click the hyperlink of the profile that you want to delete from the Log
                                                				Profiles Management web page. Log Profile Configuration web page for the
                                                				selected profile is displayed where you can view the existing profile settings.
                                                				Click Delete to delete the selected log profile.

Step 3

The selected log
                                             			 profile is deleted and you will see a confirmation message in the status bar.

You cannot
                                                            				  delete the default and system log profiles. If the selected log profile happens
                                                            				  to be the last-enabled profile in the system, then you cannot delete the
                                                            				  profile. If you try to delete the last-enabled profile, the following alert
                                                            				  message— "This is the last
                                                               					 enabled profile in system and hence not allowed to be deleted." will be
                                                            				  displayed.

#### Save Current Trace
                              	 Settings

The trace
                                    		  settings that are currently enabled in Unified
                                       			 CCX can be
                                    		  saved by clicking Save
                                       			 Current Trace Settings so that it can be enabled at a later date.
                                    		  For example, you might be asked to enable certain trace levels or a log profile
                                    		  during troubleshooting. In such a scenario, before doing the troubleshooting,
                                    		  you can save the current trace settings of your system as a profile so that you
                                    		  can enable the same trace settings after resolving the issue.

Use the
                                    		  procedure mentioned below to save the current trace settings in the system as a
                                    		  profile:

Step 1

From the Unified
                                                				CCX Serviceability menu bar, choose Trace > Profile . The Log Profiles Management
                                             			 web page displays.

Step 2

Click Save
                                                				Current Trace Settings icon in the tool bar or the Save
                                                				Current Trace Settings button at the bottom of the window.

Step 3

The Explorer
                                             			 User Prompt dialog box opens. Enter a name for your log profile.

Step 4

Click OK to save this profile. All the existing trace
                                             			 settings in your system is saved as a profile. Click Cancel to cancel this operation.

You should be
                                                				able to view this new log profile along with the existing profiles in the Log
                                                				Profiles Management web page. You can select and click Enable to enable the same profile at a later date.

#### Upload
                              	 Profile

To upload
                                    		  a log profile, perform the following steps:

Step 1

From th Unified CCX Serviceability menu
                                             			 bar, choose Trace > Profile . The Log Profiles Management
                                             			 web page displays.

Step 2

To locate the
                                             			 log profile, click the Browse button next to Enter a
                                                				Profile File to Upload field, navigate to the directory in which
                                             			 the profile (.xml file) is located, and click Open . The path for the profile appears in this
                                             			 field.

Step 3

Click Upload to upload the profile.

Step 4

You should be
                                             			 able to view the uploaded profile along with the existing profiles in the Log
                                             			 Profiles Management web page.

#### Update
                              	 Profile

You can
                                    		  update only custom log profiles. To view and update an existing log profile,
                                    		  perform the following steps:

Step 1

From the Unified
                                                				CCX Serviceability menu bar, choose Trace > Profile . The Log Profiles Management
                                             			 web page displays.

Step 2

Click the
                                             			 hyperlink of the profile you wish to view or update.

The Log Profile
                                                				Configuration web page for the selected profile is displayed where you can view
                                                				the existing profile settings.

Step 3

Click MIVR , MCVD, and MADM tabs to
                                             			 view and modify the trace settings.

Step 4

Click Save to save the updated profile settings or Save and
                                                				Enable to enable the updated profile. You will see a message
                                             			 confirming successful saving or enabling of the updated profile. Click Cancel to go back to Log Profiles Management web
                                             			 page.

## Serviceability
                        	 Tools

### Access Control
                           	 Center — Network Services Menu

Control Center in Cisco Unified CCX Serviceability lets you do the following tasks:

Start, stop, and restart Unified CCX services

View the status the status of Unified CCX services

Refresh the status of Unified CCX services

Unified CCX Serviceability provides Control Center - Network
                                 		  Services menu option, which is essential for your system to function.

Choose Tools > Control Center - Network
                                                				  Services from the Unified CCX Serviceability menu bar to perform the above-mentioned actions.

Tip

### Network
                           	 Services

Installed
                                 		  automatically, network services include services that the system requires to
                                 		  function; for example, database and system services. Because these services are
                                 		  required for basic functionality, you cannot activate them in the Service
                                 		  Activation window.

After the
                                 		  installation of your application, network services start automatically. The
                                 		  list of services displayed in the Control Center—Network Services web page
                                 		  depends on the license package of your Unified CCX. If you have a Unified CCX
                                 		  Premium license, Unified CCX Serviceability categorizes the network services
                                 		  into the following categories, which are explained in the subsequent sections:

System Services

Admin Services

DB Services

The
                                 		  Control Center—Network Services web page displays the following information for
                                 		  the network services:

Name of the
                                       				network services, their dependant subsystems, managers, or components

Status of the
                                       				service (IN SERVICE, PARTIAL SERVICE, or SHUT DOWN; for individual subsystems,
                                       				the status could be OUT OF SERVICE or NOT CONFIGURED).

Start Time of
                                       				the service

Up Time of the
                                       				service

Unified CCX Engine Services information will be removed from Unified CCX Serviceability page, when an invalid license is uploaded.

Only System and Admin Services Information will be visible in Unified CCX Node Services Information.

#### System
                              	 Services

The Unified CCX Serviceability service supports starting and stopping of the following System
                                 		Services:

Cisco Unified CCX Perfmon Counter Service

Cisco Unified CCX Cluster View Daemon—List of Managers

Cisco Unified CCX Engine—List of Subsystems and Managers

Cisco Unified CCX Voice Subagent

Cisco Unified CCX Notification Service

Cisco Unified CCX SNMP Java Adapter

Cisco Unified Intelligence Center Reporting Service

Cisco Unified Intelligence Center Serviceability Service

Cisco Unified CCX DB Perfmon Counter Service

Cisco Unified CCX Socket IO Service

Cisco Identity Service

Cisco Unified Web Proxy Service

#### Admin
                              	 Services

The Unified CCX Serviceability service supports starting and stopping of the
                                    		  following Admin Services:

Cisco Unified CCX Administration

Cisco Unified CCX Serviceability - List of Managers

You cannot start or stop this service from the Unified CCX Serviceability web interface and you need to use CLI.

Cisco Unified CCX WebServices

#### DB Services

You can
                                    		  start and stop Cisco Unified
                                       			 CCX Database
                                    		  service.

#### Finesse
                              	 Services

The Unified CCX Serviceability service supports starting and stopping of the following Cisco Finesse Services:

Cisco Finesse Tomcat

### Manage Network
                           	 Services

Control
                                 		  Center in Cisco Unified
                                    			 CCX Serviceability allows you to view status, refresh the status, and to start,
                                 		  stop, and restart network services.

Perform the following procedure to start, stop, restart, or view the status of services for a server (or for a server in a cluster in a Unified CCX cluster configuration) . You can start, stop, or refresh only one service at a time. Be aware that when a service is stopping, you cannot start it
                                 until the service is stopped. Likewise, when a service is starting, you cannot stop it until the service starts.

Step 1

Choose Tools > Control Center—Network
                                                				  Services from the Unified
                                             				CCX Serviceability menu bar.

Step 2

From the Server drop-down list box, choose the sever and then
                                          			 click Go .

The window
                                             				displays the following items:

The service
                                                				  names for the server that you chose.

The service
                                                				  status; for example, In Service, Shutdown, Partial Service and so on. (Status
                                                				  column)

The exact
                                                				  time that the service started running. (Start Time column)

The amount
                                                				  of time that the service has been running. (Up Time column)

Step 3

Perform one of
                                          			 the following tasks:

Click the
                                                				  radio button before the service that you want to start and click the Start button.

The Status
                                                   					 changes to reflect the updated status.

Click the
                                                				  radio button before the service that you want to stop and click the Stop button.

The Status
                                                   					 changes to reflect the updated status.

Click the
                                                				  radio button before the service that you want to restart and click the Restart button.

A message
                                                   					 indicates that restarting may take a while. Click OK .

To get the
                                                				  latest status of the services, click the Refresh button. The status information is updated to
                                                				  reflect the current status.

### Command Line
                           	 Interface

You can
                                 		  start and stop some services though the Command Line Interface (CLI). For a
                                 		  list of services that you can start and stop though the CLI and for information
                                 		  on how to perform these tasks, refer to the Cisco Unified Contact
                                          				  Center Express Command Line Interface Reference Guide .

### Unified CCX
                           	 Datastore

Datastores
                                 		  are components that allow you to manage and monitor historical, 
                                 		  repository, and configuration data across all servers in the
                                 		  Unified CCX cluster.

Support for High
                                             			 Availability and remote servers is available only in multiple-server
                                             			 deployments.

The
                                 		  Unified CCX Cluster uses the publisher/subscriber database model for data
                                 		  replication across the system. Under normal circumstances, the database master
                                 		  acts as the source of data and the other node acts as the target for the data.
                                 		  In other words, the database master is the publisher and
                                 		  the other node is the subscriber .

In the Tools > Datastore Control Center > Datastores web page, the first node installed in the cluster is marked as publisher (with an icon marked P). This should not be confused
                                             with the publisher/ subscriber model being discussed here. The term publisher is used to denote only the first node in the
                                             cluster and does not indicate that node to be the source of the data. The publisher/subscriber mentioned in these pages refer
                                             to the source and destination of the data respectively. Typically, the database master node acts as the source and the other
                                             node acts as the destination.

The
                                 		  publisher/subscriber database model enables Unified CCX to provide
                                 		  high-availability and failover support. To support this on the database level,
                                 		  the data must be available on multiple nodes of the cluster. To have such data
                                 		  availability, replication is used for the 
                                 		  Historical, and Repository datastore. The Configuration datastore
                                 		  does not use replication; instead, it uses atomic transactions to commit data
                                 		  changes to all active Configuration datastores in the cluster.

The
                                 		  database master is the main database. All data is written to this database,
                                 		  with the other database synchronizing with it. If the database master fails,
                                 		  then data can be written to the database on the second node. When the database
                                 		  master is back online, it returns to accepting writes. It also synchronizes
                                 		  with the other database to ensure data consistency is maintained in the
                                 		  cluster.

### Network
                           	 Outage

By
                                 		  default, replication between two nodes is removed if they are not able to
                                 		  synchronize with each other due to network outage for a substantial period of
                                 		  time. If the replication is dropped due to network outage, an alert is sent to
                                 		  the administrator so that the administrator can take corrective action.

Even though the
                                             			 replication between the nodes is removed, data could still be written to the
                                             			 database, which is accessible to the Unified
                                                				CCX engine.

If the
                                 		  replication is removed, the administrator can go to Tools > Datastore Control
                                       				Center > Replication Servers submenu from the
                                 		  Cisco Unified
                                    			 CCX Serviceability menu bar and click Reset Replication . This ensures that the
                                 		  replication is established between the nodes and the data synchronization
                                 		  (repair) process is initiated. Click Check
                                    			 Details icon in this web page to monitor the status of the repair.

If the
                                 		  network outage did not result in the replication setup being removed, once the
                                 		  network is up, the synchronization of data between the databases will happen
                                 		  automatically. For outages that last a few seconds, typically the administrator
                                 		  need not take any action and the system will be able to synchronize
                                 		  automatically.

### Datastore
                           	 Replication Status

Unified CCX Cluster configuration is not complete until Historical, and Repository publishers are configured. The Datastore
                                 Control Center in Unified CCX displays the status of datastore replication, allows you to synchronize data, and reset replication
                                 functions.

Support for High
                                             			 Availability is available only in multiple-server deployments.

Obtain an
                                          				overview of the datastores in the cluster and their relationships.

Manage the
                                          				datastore read/write access.

Monitor and
                                          				control the replication state (available only for 
                                          				Historical, and Repository datastores.)

Tip

The Datastore
                                             			 Control Center page is available even in single-node deployments but you can
                                             			 only monitor the read and write access. You cannot synchronize data, reset
                                             			 replication, or control the replication state.

Reset Replication Between Nodes

Datastores

The
                                 		  following table describes the datastores available and what they contain.

Datastore Name

Description

Historical

This
                                          					 datastore contains Historical Report data.

Repository

This
                                          					 datastore contains user prompts tables, grammar tables, and document tables.

Configuration

This
                                          					 datastore contains Unified CCX system configuration
                                          					 information.

#### Reset Replication
                              	 Between Nodes

The Replication Servers
                                    		  menu option in Datastore Control Center allows you to view replication status
                                    		  and reset the replication between two nodes for the above-mentioned three
                                    		  datastores across all servers in the cluster. This menu will be available only
                                    		  in a High Availability deployment.

Follow the procedure
                                    		  below to access the Replication Servers web page:

Step 1

Choose Tools > Datastore Control
                                                   				  Center > Replication Servers from the Unified
                                             			 CCXServiceability menu bar.

Host
                                                               						  name of the server.

Node ID
                                                               						  of the server in the Unified CCX cluster.

The current
                                                               					 state of this database.

The time the
                                                               					 connection state was last changed.

Step 2

Click Reset
                                                				Replication to reset the replication if the replication is not
                                             			 functional between the two nodes.

The Reset
                                                   				  Replication button will be enabled only when the database on both
                                                				the nodes are enabled.

When the
                                                				subscriber goes down and it is required to make configuration updates from the
                                                				publisher, you can disable Config Datastore (CDS) and Historical Datastore
                                                				(HDS) on the subscriber using Disable CDS and HDS icon or button. The database
                                                				information for the cluster is displayed at the bottom of the window. Once the
                                                				subscriber is up, you can enable CDS and HDS on the subscriber using the same
                                                				toggle button.

Caution

Any
                                                            				  configuration in Application Administration and Historical data on the
                                                            				  Subscriber node would get over written, when CDS is enabled again.

#### Datastores

Step 1

Choose Tools > Datastore Control
                                                   				  Center .

Step 2

Click Datastores from the Unified CCXServiceability menu
                                             			 bar to view replication status of all the Unified CCX datastores and to
                                             			 synchronize data.

Step 3

Click Synchronize Data to synchronize data for each
                                             			 datastore except for the Configuration datastore between the two nodes in case
                                             			 of mismatch.

##### Datastore Control
                                 	 Center contents

The
                                       		  following table describes the Datastore Control Center contents common to all
                                       		  the Unified CCX datastores.

Field

Description

Server

Server
                                                					 machine name.

Replication
                                                					 Type

- ER—Publication

- ER—Subscription

Node ID

Node ID of
                                                					 server/node in Unified CCX cluster.

Read Access

Indicates
                                                					 whether data can be read from the datastore. Options: Yes, No.

Write Access

Indicates
                                                					 whether data can be written to the datastore. Options: Yes, No.

Replicate
                                                					 Status

Last Update
                                                					 Time

Indicates
                                                					 the last action the replication agent was performing.

Info

### Update
                           	 Parameters

Use the Service Parameters page to view and update different services in Unified CCX servers. Ensure the following prerequisites are met before configuring the parameters:

The servers are configured.

The service is available on the servers.

Caution

Some changes to
                                             			 service parameters may cause system failure, thus do not make any changes to
                                             			 service parameters unless you fully understand the feature that you are
                                             			 changing or unless the Cisco Technical Assistance Center (TAC) specifies the
                                             			 changes.

Use the
                                 		  following procedure to configure the service parameters for a particular
                                 		  service on a particular Unified CCX server.

Step 1

From the Unified CCX Serviceability menu bar, choose Tools and click Service
                                             				Parameters .

Step 2

Choose a server
                                          			 from the Server drop-down list box. If parameters are available for that
                                          			 server, the service drop down list box appears displaying the following
                                          			 services:

- Cisco AMC Service.

- Cisco Log Partition
                                             				Monitoring Tool.

- Cisco Trace Collection
                                             				Service.

- Cisco RIS Data Collector.

- Cisco Serviceability
                                             				Reporter.

- Cisco DRF local.

- Cisco DRF Master.

Only the
                                                         				  common platform services mentioned above are supported currently for Unified CCX .

Step 3

Choose the
                                          			 service that contains the parameter that you want to update from the Service
                                          			 drop-down list box.

The Service
                                                         				  Parameter Configuration window displays all services (active or not active).

Step 4

The parameters
                                          			 for the selected service are displayed and the suggested values (if available)
                                          			 are listed against each one of them. Update the appropriate parameter value.

Step 5

Click Save .

The modified
                                             				values are saved and the new values are reflected on subsequent access to the
                                             				service's parameters.

Click Set to
                                                				  Default to set all service parameters for this instance of the
                                             				service to the default value. A warning is displayed that this action cannot be
                                             				undone and only on confirmation, the parameter values for the selected service
                                             				is set to the default values.

Currently, you
                                                         				  cannot configure any parameters for the following platform services: Cisco
                                                         				  Trace Collection Service and Cisco Log Partition Monitoring Tool.

### Configure
                           	 Performance Monitoring of Unified CCX Servers

Use the Performance Configuration and Logging page to configure JVM parameters and dump Thread and Memory traces for performance
                                 monitoring of Unified CCX servers. You can configure settings only for the following services of Unified CCX :

Cisco Unified CCX Cluster View Daemon

Cisco Unified CCX Engine

Cisco Unified CCX Serviceability

Use the
                                 		  following procedure to configure JVM parameters for a particular service on a
                                 		  particular server.

Step 1

From the Cisco Unified CCX Serviceability
                                          			 menu bar, choose Tools > Performance Configuration and
                                                				  Logging .

Step 2

Choose a server
                                          			 from the Server drop-down list box and click Go .

The first node
                                             				is selected by default and JVM options for the Unified CCX Engine service in
                                             				the first node is displayed.

Step 3

Choose a service
                                          			 for which you want to see the JVM options from the Service drop-down list box.
                                          			 You should be able to select any one of the following services from this list
                                          			 box:

- Cisco Unified CCX Cluster View Daemon

- Cisco Unified CCX Engine

- Cisco Unified CCX Serviceability

The following JVM options are displayed for each service:

PrintClassHistogram

PrintGCDetails

PrintGC

PrintGCTimeStamps

Step 4

Click the Dump
                                             				Thread Trace icon or button to dump the thread traces for the
                                          			 selected service in the selected server. You can collect the corresponding
                                          			 jvm.log from the log folder for that facility using Real-Time Monitoring Tool
                                          			 (RTMT).

Step 5

Click the Dump
                                             				Memory Trace icon or button to dump the memory traces. This creates
                                          			 the following two logs in the log folder for that facility.

Memory-<facility name>-<time stamp>.hprof (for heap
                                                				  dump)

histo-<facility name> <time stamp>.log (for
                                                				  histogram)

Step 6

You can change
                                          			 the JVM options by clicking Enable or Disable radio buttons in this page.

Click the Update
                                                				  JVM Options icon or button to update the new settings for selected
                                             				service on selected node.

| Step 1 | By using a
                                          			 supported web browser, open a browser session. |
|---|---|
| Step 2 | Go to https://<server name or IP
                                                				  address>/uccxservice/. |
| Step 3 | Enter an
                                          			 applicable username and password, and click Login . Note If you log in as an end user,
                                                         				  you can access Cisco Unified CCX Administration 
                                                         				   from the Navigation drop-down list box without logging in
                                                         				  again. If you log in as an Application user, you can access Cisco Unified
                                                         				  Serviceability in addition to these web applications. | Note | If you log in as an end user,
                                                         				  you can access Cisco Unified CCX Administration 
                                                         				   from the Navigation drop-down list box without logging in
                                                         				  again. If you log in as an Application user, you can access Cisco Unified
                                                         				  Serviceability in addition to these web applications. |
| Note | If you log in as an end user,
                                                         				  you can access Cisco Unified CCX Administration 
                                                         				   from the Navigation drop-down list box without logging in
                                                         				  again. If you log in as an Application user, you can access Cisco Unified
                                                         				  Serviceability in addition to these web applications. |

| Note | If you log in as an end user,
                                                         				  you can access Cisco Unified CCX Administration 
                                                         				   from the Navigation drop-down list box without logging in
                                                         				  again. If you log in as an Application user, you can access Cisco Unified
                                                         				  Serviceability in addition to these web applications. |
|---|---|

| Note | Use the Alarm
                                          			 Definitions web page in Cisco Unified Serviceability to find information about
                                          			 an alarm message. For information on alarm definitions, see the Cisco Unified Serviceability Administration Guide available at: https://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-callmanager/products-maintenance-guides-list.html . |
|---|---|

| Note | Alarm Server Configuration is
                                             			 applicable for the following Unified CCX components: Unified CCX
                                             			 Administration, Unified CCX Engine, and Unified CCX Cluster View Daemon . |
|---|---|

| Step 1 | From the Unified
                                             				CCX Serviceability menu bar, choose Alarm and click Configuration . The Alarm
                                             				Configuration web page opens and the following fields are displayed on the
                                             				Alarm Configuration web page, if configured on your Unified
                                                				  CCX server: Field Description Local Syslogs Enable
                                                         							 Alarm Use
                                                         							 the check box next to Enable Alarm field to enable or disable the alarms for
                                                         							 local syslog. Alarm
                                                         							 Event Level Lists
                                                         							 the alarm severity level. Remote Syslogs Enable
                                                         							 Alarm Use
                                                         							 the check box next to Enable Alarm field to enable or disable the alarms for
                                                         							 remote syslog. Alarm
                                                         							 Event Level Lists
                                                         							 the alarm severity level. Server
                                                         							 Name IP address or hostname of the Syslog server to which system should send the alarm messages. If you are using CiscoWorks, enter
                                                         the IP address or the hostname of the CiscoWorks server. | Field | Description | Local Syslogs | Enable
                                                         							 Alarm | Use
                                                         							 the check box next to Enable Alarm field to enable or disable the alarms for
                                                         							 local syslog. | Alarm
                                                         							 Event Level | Lists
                                                         							 the alarm severity level. | Remote Syslogs | Enable
                                                         							 Alarm | Use
                                                         							 the check box next to Enable Alarm field to enable or disable the alarms for
                                                         							 remote syslog. | Alarm
                                                         							 Event Level | Lists
                                                         							 the alarm severity level. | Server
                                                         							 Name | IP address or hostname of the Syslog server to which system should send the alarm messages. If you are using CiscoWorks, enter
                                                         the IP address or the hostname of the CiscoWorks server. |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Field | Description |
| Local Syslogs |
| Enable
                                                         							 Alarm | Use
                                                         							 the check box next to Enable Alarm field to enable or disable the alarms for
                                                         							 local syslog. |
| Alarm
                                                         							 Event Level | Lists
                                                         							 the alarm severity level. |
| Remote Syslogs |
| Enable
                                                         							 Alarm | Use
                                                         							 the check box next to Enable Alarm field to enable or disable the alarms for
                                                         							 remote syslog. |
| Alarm
                                                         							 Event Level | Lists
                                                         							 the alarm severity level. |
| Server
                                                         							 Name | IP address or hostname of the Syslog server to which system should send the alarm messages. If you are using CiscoWorks, enter
                                                         the IP address or the hostname of the CiscoWorks server. |
| Step 2 | To update the
                                          			 Alarm Event Level for local or remote syslogs, check the check box before
                                          			 Enable Alarm field. |
| Step 3 | Modify Alarm
                                          			 Event Level for the local or remote syslogs by selecting from the Alarm Event
                                          			 Level drop-down list. Modify the syslog server name in case of remote syslog. |
| Step 4 | Click Update icon that displays in the tool bar in the
                                          			 upper, left corner of the window or the Update button that displays at the bottom of the
                                          			 window to save your configuration. Click Clear to reset data to the previous values. In case of a High
                                             				Availability deployment, the alarm configuration changes are automatically
                                             				propagated to the second node. If the second node cannot be contacted, an alert
                                             				message indicating that the update has failed on the remote node is displayed. Caution You should
                                                         				  activate logging only for
                                                         				  the purpose of debugging and remember to deactivate logging once the debugging session is complete. | Caution | You should
                                                         				  activate logging only for
                                                         				  the purpose of debugging and remember to deactivate logging once the debugging session is complete. |
| Caution | You should
                                                         				  activate logging only for
                                                         				  the purpose of debugging and remember to deactivate logging once the debugging session is complete. |

| Field | Description |
|---|---|
| Local Syslogs |
| Enable
                                                         							 Alarm | Use
                                                         							 the check box next to Enable Alarm field to enable or disable the alarms for
                                                         							 local syslog. |
| Alarm
                                                         							 Event Level | Lists
                                                         							 the alarm severity level. |
| Remote Syslogs |
| Enable
                                                         							 Alarm | Use
                                                         							 the check box next to Enable Alarm field to enable or disable the alarms for
                                                         							 remote syslog. |
| Alarm
                                                         							 Event Level | Lists
                                                         							 the alarm severity level. |
| Server
                                                         							 Name | IP address or hostname of the Syslog server to which system should send the alarm messages. If you are using CiscoWorks, enter
                                                         the IP address or the hostname of the CiscoWorks server. |

| Caution | You should
                                                         				  activate logging only for
                                                         				  the purpose of debugging and remember to deactivate logging once the debugging session is complete. |
|---|---|

| Setting | Description |
|---|---|
| Enable Alarm
                                          					 for Local Syslogs | The SysLog
                                          					 viewer serves as the alarm destination. The program logs errors in the
                                          					 Application Logs within SysLog Viewer and provides a description of the alarm
                                          					 and a recommended action. You can access the SysLog Viewer from the Cisco
                                          					 Unified Real-Time Monitoring Tool. For information on viewing
                                          					 logs with the SysLog Viewer, see Cisco Unified Real-Time
                                                   				  Monitoring Tool Administration Guide for Cisco Unified Contact Center Express
                                                   				  and Cisco Unified IP IVR . |
| Enable Alarm
                                          					 for Remote Syslogs | The Syslog
                                          					 file serves as the alarm destination. Check this check box to enable the Syslog
                                          					 messages to be stored on a Syslog server and to specify the Syslog server name. |
| Alarm Event
                                          					 Level | Alarm event
                                          					 level messages range from severity 0 (most severe) to severity 7 (least severe)
                                          					 description of which is mentioned below. When you choose a severity level, all
                                          					 messages of that severity level and higher are sent. For example,
                                          					 if you choose ERROR_ALARM (Severity 3), all messages of severity 3, severity 2,
                                          					 severity 1, and severity 0 are sent. The default is "INFORMATIONAL_ALARM (Severity 6)" , which will send messages
                                          					 of all severity levels starting from 6 to severity level 0. You can
                                          					 choose one of the following alarm event level options from the drop-down list
                                          					 box: Emergency This
                                                						  level designates system as unusable. Alert This
                                                						  level indicates that immediate action is needed. Critical The
                                                						  system detects a critical condition. Error This
                                                						  level signifies an error condition exists. Warning This
                                                						  level indicates that a warning condition is detected. Notice This
                                                						  level designates a normal but significant condition. Informational This
                                                						  level designates information messages only. Debug This
                                                						  level designates detailed event information that Cisco TAC engineers use for
                                                						  debugging. |

| Note | You must use Cisco Unified Intelligence Center CLIs for Log Trace Settings. For more
                                             					information see Cisco Unified Intelligence Center
                                                						Commands . |
|---|---|

| Step 1 | From the Cisco Unified CCX
                                             				Serviceability menu bar, choose Trace > Configuration . The Trace Configuration web
                                             				page opens displaying the default trace configuration for Unified CCX Engine. |
|---|---|
| Step 2 | From the Select
                                             				Service drop-down list box, choose a service or component for which
                                          			 you want to configure trace then, click Go . You should be
                                             				able to view the existing Trace configurations and debug levels for the
                                             				selected Unified CCX service with
                                             				check boxes for the various Debugging and XDebugging levels for each sub
                                             				facility. The debug levels for different Unified CCX subfacilities or services might vary depending on the selected service and are
                                             listed in the following table: Table 1. Debug
                                                   				Levels for Different Unified CCX Subfacilities Cisco Unified CCX Components Subfacilities or Services Cisco Unified CCX Administration Libraries Managers Miscellaneous Cisco Unified CCX Cluster View Daemon Libraries Managers Miscellaneous Cisco Unified CCX Editor Libraries Managers Miscellaneous Steps Cisco Identity Service Error Warning Information Debugging Cisco Unified CCX Engine Libraries Managers Miscellaneous Steps Subsystems Cisco Unified CM Telephony Client or JTAPI Debug Levels Warning Information Debugging Cisco Unified CCX Socket.IO Service Service DataProcessing Communication | Cisco Unified CCX Components | Subfacilities or Services | Cisco Unified CCX Administration |  | Libraries | Managers | Miscellaneous | Cisco Unified CCX Cluster View Daemon |  | Libraries | Managers | Miscellaneous | Cisco Unified CCX Editor |  | Libraries | Managers | Miscellaneous | Steps | Cisco Identity Service |  | Error | Warning | Information | Debugging | Cisco Unified CCX Engine |  | Libraries | Managers | Miscellaneous | Steps | Subsystems | Cisco Unified CM Telephony Client or JTAPI Debug Levels |  | Warning | Information | Debugging | Cisco Unified CCX Socket.IO Service |  | Service | DataProcessing | Communication |
| Cisco Unified CCX Components | Subfacilities or Services |
| Cisco Unified CCX Administration |
|  | Libraries |
| Managers |
| Miscellaneous |
| Cisco Unified CCX Cluster View Daemon |
|  | Libraries |
| Managers |
| Miscellaneous |
| Cisco Unified CCX Editor |
|  | Libraries |
| Managers |
| Miscellaneous |
| Steps |
| Cisco Identity Service |
|  | Error |
| Warning |
| Information |
| Debugging |
| Cisco Unified CCX Engine |
|  | Libraries |
| Managers |
| Miscellaneous |
| Steps |
| Subsystems |
| Cisco Unified CM Telephony Client or JTAPI Debug Levels |
|  | Warning |
| Information |
| Debugging |
| Cisco Unified CCX Socket.IO Service |
|  | Service |
| DataProcessing |
| Communication |
| Step 3 | Update the
                                          			 debug level for one or more of the libraries or sub facilities for the selected
                                          			 service by doing the following: To
                                                				  activate traces for a specific component or logging for a server, check the
                                                				  check box for the service that you chose. To
                                                				  deactivate logging for a server, uncheck the specific check box. Caution If you modify the trace level settings for Cisco Unified CM Telephony Client, you have to restart the Unified CCX Engine for
                                                      the changes to take effect. | Caution | If you modify the trace level settings for Cisco Unified CM Telephony Client, you have to restart the Unified CCX Engine for
                                                      the changes to take effect. |
| Caution | If you modify the trace level settings for Cisco Unified CM Telephony Client, you have to restart the Unified CCX Engine for
                                                      the changes to take effect. |
| Step 4 | To limit the
                                          			 number and size of the trace files, you can specify the trace output setting
                                          			 using the following two fields. See the following table for description and
                                          			 default values for these two fields. Field Description Maximum No. of Files The maximum number of trace files to be retained by the system. This field specifies the total number of trace files for a given
                                                         							 service. Cisco Unified CCX Serviceability automatically appends a sequence number to the file name to
                                                         							 indicate which file it is; for example, Cisco001MADM14.log. When the last file
                                                         							 in the sequence is full, the trace data begins writing over the first file. The
                                                         							 default value varies by service. Maximum File Size This field specifies the maximum size of the trace file in
                                                         							 kilobytes or megabytes depending on the selected service. The default value
                                                         							 varies by service. | Field | Description | Maximum No. of Files | The maximum number of trace files to be retained by the system. This field specifies the total number of trace files for a given
                                                         							 service. Cisco Unified CCX Serviceability automatically appends a sequence number to the file name to
                                                         							 indicate which file it is; for example, Cisco001MADM14.log. When the last file
                                                         							 in the sequence is full, the trace data begins writing over the first file. The
                                                         							 default value varies by service. | Maximum File Size | This field specifies the maximum size of the trace file in
                                                         							 kilobytes or megabytes depending on the selected service. The default value
                                                         							 varies by service. |
| Field | Description |
| Maximum No. of Files | The maximum number of trace files to be retained by the system. This field specifies the total number of trace files for a given
                                                         							 service. Cisco Unified CCX Serviceability automatically appends a sequence number to the file name to
                                                         							 indicate which file it is; for example, Cisco001MADM14.log. When the last file
                                                         							 in the sequence is full, the trace data begins writing over the first file. The
                                                         							 default value varies by service. |
| Maximum File Size | This field specifies the maximum size of the trace file in
                                                         							 kilobytes or megabytes depending on the selected service. The default value
                                                         							 varies by service. |
| Step 5 | Click Save icon that displays in the tool bar in the
                                          			 upper, left corner of the window or the Save button that displays at the bottom of the
                                          			 window to save your trace parameter configuration. The settings are updated in
                                          			 the system and the trace files will be generated as per the saved settings.
                                          			 Click Restore Defaults icon or button to revert to the
                                          			 default settings for the selected service. In a High
                                             				Availability deployment, the changes are propagated to the second node. If the
                                             				second node cannot be contacted, an alert message indicating that the update
                                             				has failed on the remote node is displayed. Caution You should activate logging only for the purpose of debugging and remember to deactivate logging once the debugging session is complete. Note You will not be able to save the trace configuration if the Socket.IO service is down. When the node containing the socket.IO
                                                      service is down then the log levels will not be saved on that particular node. | Caution | You should activate logging only for the purpose of debugging and remember to deactivate logging once the debugging session is complete. | Note | You will not be able to save the trace configuration if the Socket.IO service is down. When the node containing the socket.IO
                                                      service is down then the log levels will not be saved on that particular node. |
| Caution | You should activate logging only for the purpose of debugging and remember to deactivate logging once the debugging session is complete. |
| Note | You will not be able to save the trace configuration if the Socket.IO service is down. When the node containing the socket.IO
                                                      service is down then the log levels will not be saved on that particular node. |

| Cisco Unified CCX Components | Subfacilities or Services |
|---|---|
| Cisco Unified CCX Administration |
|  | Libraries |
| Managers |
| Miscellaneous |
| Cisco Unified CCX Cluster View Daemon |
|  | Libraries |
| Managers |
| Miscellaneous |
| Cisco Unified CCX Editor |
|  | Libraries |
| Managers |
| Miscellaneous |
| Steps |
| Cisco Identity Service |
|  | Error |
| Warning |
| Information |
| Debugging |
| Cisco Unified CCX Engine |
|  | Libraries |
| Managers |
| Miscellaneous |
| Steps |
| Subsystems |
| Cisco Unified CM Telephony Client or JTAPI Debug Levels |
|  | Warning |
| Information |
| Debugging |
| Cisco Unified CCX Socket.IO Service |
|  | Service |
| DataProcessing |
| Communication |

| Caution | If you modify the trace level settings for Cisco Unified CM Telephony Client, you have to restart the Unified CCX Engine for
                                                      the changes to take effect. |
|---|---|

| Field | Description |
|---|---|
| Maximum No. of Files | The maximum number of trace files to be retained by the system. This field specifies the total number of trace files for a given
                                                         							 service. Cisco Unified CCX Serviceability automatically appends a sequence number to the file name to
                                                         							 indicate which file it is; for example, Cisco001MADM14.log. When the last file
                                                         							 in the sequence is full, the trace data begins writing over the first file. The
                                                         							 default value varies by service. |
| Maximum File Size | This field specifies the maximum size of the trace file in
                                                         							 kilobytes or megabytes depending on the selected service. The default value
                                                         							 varies by service. |

| Caution | You should activate logging only for the purpose of debugging and remember to deactivate logging once the debugging session is complete. |
|---|---|

| Note | You will not be able to save the trace configuration if the Socket.IO service is down. When the node containing the socket.IO
                                                      service is down then the log levels will not be saved on that particular node. |
|---|---|

| Component
                                             					 Code | Description |
|---|---|
| AC_CLUSTER | Archive
                                             					 Cluster Component |
| AC_CONFIG | Archive
                                             					 Configuration Component |
| AC_DATABASE | Archive
                                             					 Database Component |
| AC_JTAPI | JTAPI
                                             					 Archive Component |
| AC_OS | Archive
                                             					 Operating System Component |
| ADM | Administration Client |
| ADM_CFG | Administration Configuration |
| APP_MGR | Applications Manager |
| ARCHIVE_MGR | Archive
                                             					 Manager |
| AW_CFG | Restore
                                             					 Administration Configuration |
| BARBI_CLI | Backup and
                                             					 Restore Client Interface |
| BOOTSTRAP_MGR | Cisco
                                             					 Unified CCX Bootstrap Manager |
| CFG_MGR | Configuration Manager |
| CHANNEL_MGR | Channel
                                             					 Manager |
| CLUSTER_MGR | Cluster
                                             					 Manager |
| CONTACT_MGR | Contact
                                             					 Manager |
| CONTACT_STEPS | Contact
                                             					 Steps |
| CRA_CMM | Cisco
                                             					 Unified CCX ClusterMsgMgr Component |
| CRA_HRDM | Cisco
                                             					 Unified CCX Historical Reporting Data Manager |
| CVD | Cluster
                                             					 View Daemon |
| DB | Database |
| DBPURGE_MGR | Database
                                             					 Purge Manager |
| DESKTOP | Cisco
                                             					 Unified CCX Editor Desktop |
| DOC_MGR | Document
                                             					 Manager |
| EDT | Cisco
                                             					 Unified CCX Editor general |
| ENG | Cisco
                                             					 Unified CCX Engine |
| EXECUTOR_MGR | Executor
                                             					 Manager |
| EXPR_MGR | Expression
                                             					 Manager |
| FILE_MGR | File
                                             					 Manager |
| GENERIC | Generic
                                             					 catalog for a facility |
| GRAMMAR_MGR | Grammar
                                             					 Manager |
| GRP_CFG | Group
                                             					 Configuration |
| HOLIDAY_MGR | Holiday
                                             					 Manager |
| HR_MGR | Historical
                                             					 Reports Manager |
| ICD_CTI | Cisco
                                             					 Unified CCX CTI Server |
| ICD_HDM | IPCC
                                             					 Express Historical Data Manager |
| ICD_RTDM | Cisco
                                             					 Unified CCX ICD Real-Time Data Manager |
| IVR_RTDM | Cisco
                                             					 Unified CCX IP IVR Real-Time Data Manager |
| IO_ICM | Cisco
                                             					 Unified ICME Input/Output |
| JASMIN | Java
                                             					 Signaling and Monitoring Interface |
| LIB_APPADMININTERCEPTOR | Cisco
                                             					 Unified CCX Administration Interceptor Library |
| LIB_AXL | AXL
                                             					 Library |
| LIB_CFG | Configuration Library |
| LIB_CLUSTER_CFG | Configuration Library for the cluster |
| LIB_CRTP | CRTP
                                             					 Library |
| LIB_DATABASE | Database
                                             					 Library |
| LIB_DIRECTORY | Directory
                                             					 Access Library |
| LIB_EVENT | Event
                                             					 Message Library |
| LIB_ICM | Cisco
                                             					 Unified ICME Library |
| LIB_JASPER | Jasper
                                             					 Tomcat Library |
| LIB_JCUP | JavaCup
                                             					 Library to parse expressions |
| LIB_JDBC | JDBC
                                             					 Library |
| LIB_JINI | JINI
                                             					 Services |
| LIB_JMAIL | Java Mail
                                             					 Library |
| LIB_JLEX | JLEX
                                             					 Library used to parse expressions |
| LIB_LICENSE | License
                                             					 Library |
| LIB_MEDIA | Media
                                             					 Library |
| LIB_RMI | Java
                                             					 Remote Method Invocation Library |
| LIB_SERVLET | Servlet
                                             					 Library |
| LIB_TC | Tomcat
                                             					 Library |
| LOG_MGR | Log
                                             					 Manager |
| MRCP_CFG | MRCP
                                             					 Configuration |
| MGR_MGR | Manager
                                             					 Manager |
| NODE_MGR | Node
                                             					 Manager |
| PALETTE | Editor
                                             					 Palette |
| PROMPT_MGR | Prompt
                                             					 Manager |
| PURGING | Purging |
| RPT | Reporting |
| RTPPORT_MGR | RTP
                                             					 Manager |
| SCRIPT_MGR | Script
                                             					 Manager |
| SESSION_MGR | Session
                                             					 Manager |
| SIP_STACK | SIP Stack
                                             					 logging |
| SOCKET_MGR | Socket
                                             					 Manager |
| SS_APP | Application Subsystem |
| SS_CHAT | Chat
                                             					 Subsystem |
| SS_CM | Contact
                                             					 Manager Subsystem |
| SS_CMT | Cisco
                                             					 Media Termination Subsystem |
| SS_DB | Database
                                             					 Subsystem |
| SS_EMAIL | Email
                                             					 Subsystem |
| SS_HTTP | HTTP
                                             					 Subsystem |
| SS_ICM | Cisco
                                             					 Unified ICME Subsystem |
| SS_MRCP_ASR | MRCP ASR
                                             					 Subsystem |
| SS_MRCP_TTS | MRCP TTS
                                             					 Subsystem |
| SS_OUTBOUND | Outbound
                                             					 Dialer Express Subsystem (uses MIVR log file) |
| SS_RM | Resource
                                             					 Manager Subsystem |
| SS_RMCM | Resource
                                             					 Manager Contact Manager Subsystem |
| SS_ROUTEANDQUEUE | Route and
                                             					 Queue Subsystem |
| SS_RTR | Real-Time
                                             					 Reporting Subsystem |
| SS_SIP | SIP
                                             					 Subsystem |
| SS_TEL | JTAPI
                                             					 Subsystem (Telephony) |
| STEP_CALL_CONTROL | Call
                                             					 Control Steps |
| STEP_MEDIA_CONTROL | Media
                                             					 Control Steps |
| STEP_SESSION | Sessions
                                             					 Steps |
| STEP_SESSION_MGMT | Session
                                             					 Management Steps |
| STEP_USER | User Steps |
| STEP_CALL_CONTACT | Call
                                             					 Contact Steps |
| STEPS_CONTACT | Contact
                                             					 Steps |
| STEPS_DB | Database
                                             					 Steps |
| STEPS_DOCUMENT | Document
                                             					 Steps |
| STEPS_EMAIL | E-mail
                                             					 Steps |
| STEPS_GENERAL | General
                                             					 Steps |
| STEPS_GRAMMAR | Grammar
                                             					 Steps |
| STEPS_HTTP | HTTP Steps |
| STEPS_ICM | Cisco
                                             					 Unified ICME Steps |
| STEPS_IPCC_EXP | Cisco
                                             					 Unified CCX Steps |
| STEPS_JAVA | Java Steps |
| STEPS_PROMPT | Prompt
                                             					 Steps |
| STEPS_SESSION | Session
                                             					 Steps |
| UCCX_WEBSERVICES | Chat
                                             					 Subsystem |
| USR_MGR | User
                                             					 Manager |
| WEB_STEPS | HTTP
                                             					 Contact Steps |

| Note | Log Profiles
                                             			 Management does not support Socket.IO service. |
|---|---|

| Name | Scenario
                                                         					 in which this profile must be activated |
|---|---|
| Default | Activate
                                                         					 this profile once an issue is resolved. |
| Outbound | For issues
                                                         					 with Unified CCX Outbound Dialer AppAdmin. |
| AppAdmin | For issues
                                                         					 with web administration through AppAdmin, Unified CCX Serviceability, and other
                                                         					 web pages. |
| Media | For issues
                                                         					 with media setup or media transmission. |
| HRDM
                                                         					 (Historical Reporting Data Manager) | For
                                                         					 issues with historical data that is written to the database. |
| StuckSession | For
                                                         					 issues with application sessions, sessions that are not being deleted when
                                                         					 appropriate and appearing stuck in AppAdmin Real Time Reports. |
| Database | For issues
                                                         					 with Unified CCX Informix database. |
| EDBS
                                                         					 (Enterprise Database Subsystem) | For issues
                                                         					 with external database connectivity and integration. |
| CallsStuckInQueue | For issues
                                                         					 with calls in queue that are not being allocated to available agents or
                                                         					 appearing stuck in queue in reports. |
| Serviceability | For issues
                                                         					 with the functionality in Unified CCX Serviceability Administration Interface. |
| RealTimeDataProblems | For issues
                                                         					 with Real Time Reports in AppAdmin. |

| Note | In a HA
                                                               					 deployment of Unified CCX, all the log profile operations will be reflected on
                                                               					 both the nodes in the cluster. You cannot
                                                               					 delete the profile if the selected log profile is the last-enabled profile in
                                                               					 the system. |
|---|---|

| Step 1 | From the Unified CCX Serviceability menu bar, choose Trace > Profile . The Log Profiles Management
                                             			 web page displays. |
|---|---|
| Step 2 | Click Add
                                                				New icon that displays in the tool bar in the upper, left corner of
                                             			 the window or the Add
                                                				New button that displays at the bottom of the window. The Log Profile
                                                				Configuration web page displays. You can view lists of subfacilities such as
                                                				libraries, managers, steps, subsystems, and so on with check boxes for the
                                                				various Debugging and XDebugging levels for each subfacility for the MIVR tab
                                                				by default. |
| Step 3 | Select desired
                                             			 trace setting for different subfacilities in a service by clicking the
                                             			 corresponding check box. |
| Step 4 | Click MCVD and
                                             			 MADM tabs to navigate to view and enable trace setting for these profiles. |
| Step 5 | On successful
                                             			 configuration of these log profiles, click Save to save the profile or Save and
                                                				Enable to save and enable the profile. The new profile will be
                                             			 displayed in the main profile page. |

| Step 1 | From the Unified
                                                				CCX Serviceability menu bar, choose Trace > Profile . The Log Profiles Management
                                             			 web page displays. |
|---|---|
| Step 2 | Click the radio
                                             			 button to select a log profile. |
| Step 3 | Click Save
                                                				As . The Log Profile
                                                				Configuration web page for the selected profile is displayed where you can view
                                                				and update the existing profile settings. Click MIVR , MCVD, and MADM tabs to
                                                				view and modify the trace settings. |
| Step 4 | You can save
                                             			 these updated trace settings with a new name. You will see a message confirming
                                             			 successful saving of the new profile. |

| Step 1 | From the Unified
                                                				CCX Serviceability menu bar, choose Trace > Profile . The Log Profiles Management
                                             			 web page displays. You can enable a
                                                				log profile using any one of the following methods from the Log Profiles
                                                				Management web page: Select the
                                                   				  radio button for the profile and click Enable icon or button Click the
                                                   				  hyperlink for the desired profile. Log Profile Configuration web page for the
                                                   				  selected profile is displayed. Click Enable icon or button in the Profile Configuration
                                                   				  web page Click Add
                                                      					 New . Enter the desired trace settings in the Profile Configuration
                                                   				  web page and click Save
                                                      					 and Enable icon or button in the Profile Configuration web page. |
|---|---|
| Step 2 | The trace
                                             			 setting for the selected profile is transferred to system's trace settings and
                                             			 on successful activation, a message will be displayed in the status bar. |

| Step 1 | From the Unified
                                                				CCX Serviceability menu bar, choose Trace > Profile . The Log
                                             			 Profiles Management web page displays. |
|---|---|
| Step 2 | Select the radio
                                             			 button for an existing profile and click Delete icon or button to delete a log profile. Alternatively,
                                                				you can click the hyperlink of the profile that you want to delete from the Log
                                                				Profiles Management web page. Log Profile Configuration web page for the
                                                				selected profile is displayed where you can view the existing profile settings.
                                                				Click Delete to delete the selected log profile. |
| Step 3 | The selected log
                                             			 profile is deleted and you will see a confirmation message in the status bar. Note You cannot
                                                            				  delete the default and system log profiles. If the selected log profile happens
                                                            				  to be the last-enabled profile in the system, then you cannot delete the
                                                            				  profile. If you try to delete the last-enabled profile, the following alert
                                                            				  message— "This is the last
                                                               					 enabled profile in system and hence not allowed to be deleted." will be
                                                            				  displayed. | Note | You cannot
                                                            				  delete the default and system log profiles. If the selected log profile happens
                                                            				  to be the last-enabled profile in the system, then you cannot delete the
                                                            				  profile. If you try to delete the last-enabled profile, the following alert
                                                            				  message— "This is the last
                                                               					 enabled profile in system and hence not allowed to be deleted." will be
                                                            				  displayed. |
| Note | You cannot
                                                            				  delete the default and system log profiles. If the selected log profile happens
                                                            				  to be the last-enabled profile in the system, then you cannot delete the
                                                            				  profile. If you try to delete the last-enabled profile, the following alert
                                                            				  message— "This is the last
                                                               					 enabled profile in system and hence not allowed to be deleted." will be
                                                            				  displayed. |

| Note | You cannot
                                                            				  delete the default and system log profiles. If the selected log profile happens
                                                            				  to be the last-enabled profile in the system, then you cannot delete the
                                                            				  profile. If you try to delete the last-enabled profile, the following alert
                                                            				  message— "This is the last
                                                               					 enabled profile in system and hence not allowed to be deleted." will be
                                                            				  displayed. |
|---|---|

| Step 1 | From the Unified
                                                				CCX Serviceability menu bar, choose Trace > Profile . The Log Profiles Management
                                             			 web page displays. |
|---|---|
| Step 2 | Click Save
                                                				Current Trace Settings icon in the tool bar or the Save
                                                				Current Trace Settings button at the bottom of the window. |
| Step 3 | The Explorer
                                             			 User Prompt dialog box opens. Enter a name for your log profile. |
| Step 4 | Click OK to save this profile. All the existing trace
                                             			 settings in your system is saved as a profile. Click Cancel to cancel this operation. You should be
                                                				able to view this new log profile along with the existing profiles in the Log
                                                				Profiles Management web page. You can select and click Enable to enable the same profile at a later date. |

| Step 1 | From th Unified CCX Serviceability menu
                                             			 bar, choose Trace > Profile . The Log Profiles Management
                                             			 web page displays. |
|---|---|
| Step 2 | To locate the
                                             			 log profile, click the Browse button next to Enter a
                                                				Profile File to Upload field, navigate to the directory in which
                                             			 the profile (.xml file) is located, and click Open . The path for the profile appears in this
                                             			 field. |
| Step 3 | Click Upload to upload the profile. |
| Step 4 | You should be
                                             			 able to view the uploaded profile along with the existing profiles in the Log
                                             			 Profiles Management web page. |

| Step 1 | From the Unified
                                                				CCX Serviceability menu bar, choose Trace > Profile . The Log Profiles Management
                                             			 web page displays. |
|---|---|
| Step 2 | Click the
                                             			 hyperlink of the profile you wish to view or update. The Log Profile
                                                				Configuration web page for the selected profile is displayed where you can view
                                                				the existing profile settings. |
| Step 3 | Click MIVR , MCVD, and MADM tabs to
                                             			 view and modify the trace settings. |
| Step 4 | Click Save to save the updated profile settings or Save and
                                                				Enable to enable the updated profile. You will see a message
                                             			 confirming successful saving or enabling of the updated profile. Click Cancel to go back to Log Profiles Management web
                                             			 page. |

| Choose Tools > Control Center - Network
                                                				  Services from the Unified CCX Serviceability menu bar to perform the above-mentioned actions. Tip You may need to manage services in both Unified CCX Serviceability and Cisco Unified Serviceability to troubleshoot a problem. For information on Unified Serviceability services,
                                                      see the Cisco Unified Serviceability Administration Guide available at: https://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-callmanager/products-maintenance-guides-list.html . | Tip | You may need to manage services in both Unified CCX Serviceability and Cisco Unified Serviceability to troubleshoot a problem. For information on Unified Serviceability services,
                                                      see the Cisco Unified Serviceability Administration Guide available at: https://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-callmanager/products-maintenance-guides-list.html . |
|---|---|---|
| Tip | You may need to manage services in both Unified CCX Serviceability and Cisco Unified Serviceability to troubleshoot a problem. For information on Unified Serviceability services,
                                                      see the Cisco Unified Serviceability Administration Guide available at: https://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-callmanager/products-maintenance-guides-list.html . |

| Tip | You may need to manage services in both Unified CCX Serviceability and Cisco Unified Serviceability to troubleshoot a problem. For information on Unified Serviceability services,
                                                      see the Cisco Unified Serviceability Administration Guide available at: https://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-callmanager/products-maintenance-guides-list.html . |
|---|---|

| Note | Unified CCX Engine Services information will be removed from Unified CCX Serviceability page, when an invalid license is uploaded. Only System and Admin Services Information will be visible in Unified CCX Node Services Information. |
|---|---|

| Note | You cannot start or stop this service from the Unified CCX Serviceability web interface and you need to use CLI. |
|---|---|

| Step 1 | Choose Tools > Control Center—Network
                                                				  Services from the Unified
                                             				CCX Serviceability menu bar. |
|---|---|
| Step 2 | From the Server drop-down list box, choose the sever and then
                                          			 click Go . The window
                                             				displays the following items: The service
                                                				  names for the server that you chose. The service
                                                				  status; for example, In Service, Shutdown, Partial Service and so on. (Status
                                                				  column) The exact
                                                				  time that the service started running. (Start Time column) The amount
                                                				  of time that the service has been running. (Up Time column) |
| Step 3 | Perform one of
                                          			 the following tasks: Click the
                                                				  radio button before the service that you want to start and click the Start button. The Status
                                                   					 changes to reflect the updated status. Click the
                                                				  radio button before the service that you want to stop and click the Stop button. The Status
                                                   					 changes to reflect the updated status. Click the
                                                				  radio button before the service that you want to restart and click the Restart button. A message
                                                   					 indicates that restarting may take a while. Click OK . To get the
                                                				  latest status of the services, click the Refresh button. The status information is updated to
                                                				  reflect the current status. |

| Note | Support for High
                                             			 Availability and remote servers is available only in multiple-server
                                             			 deployments. |
|---|---|

| Note | In the Tools > Datastore Control Center > Datastores web page, the first node installed in the cluster is marked as publisher (with an icon marked P). This should not be confused
                                             with the publisher/ subscriber model being discussed here. The term publisher is used to denote only the first node in the
                                             cluster and does not indicate that node to be the source of the data. The publisher/subscriber mentioned in these pages refer
                                             to the source and destination of the data respectively. Typically, the database master node acts as the source and the other
                                             node acts as the destination. |
|---|---|

| Note | Even though the
                                             			 replication between the nodes is removed, data could still be written to the
                                             			 database, which is accessible to the Unified
                                                				CCX engine. |
|---|---|

| Note | Support for High
                                             			 Availability is available only in multiple-server deployments. |
|---|---|

| Tip | The Datastore
                                             			 Control Center page is available even in single-node deployments but you can
                                             			 only monitor the read and write access. You cannot synchronize data, reset
                                             			 replication, or control the replication state. |
|---|---|

| Datastore Name | Description |
|---|---|
| Historical | This
                                          					 datastore contains Historical Report data. |
| Repository | This
                                          					 datastore contains user prompts tables, grammar tables, and document tables. |
| Configuration | This
                                          					 datastore contains Unified CCX system configuration
                                          					 information. |

| Step 1 | Choose Tools > Datastore Control
                                                   				  Center > Replication Servers from the Unified
                                             			 CCXServiceability menu bar. The Replication
                                                				Servers web page opens displaying the list of servers and the following fields
                                                				in a High Availability deployment. Datastore
                                                            						Name Description Server Host
                                                               						  name of the server. Node ID Node ID
                                                               						  of the server in the Unified CCX cluster. State The
                                                               						  current connectivity status of the node in the replication network, which can
                                                               						  be one of the following values: DROPPED/ TIMED OUT The
                                                                     								server cannot be reached and is not available in the replicated network. ACTIVE/ CONNECTED The
                                                                     								server is connected in the replication network and sends or receives updates. Job Status The current
                                                               					 state of this database. Last
                                                            				  Changed The time the
                                                               					 connection state was last changed. | Datastore
                                                            						Name | Description | Server | Host
                                                               						  name of the server. | Node ID | Node ID
                                                               						  of the server in the Unified CCX cluster. | State | The
                                                               						  current connectivity status of the node in the replication network, which can
                                                               						  be one of the following values: DROPPED/ TIMED OUT The
                                                                     								server cannot be reached and is not available in the replicated network. ACTIVE/ CONNECTED The
                                                                     								server is connected in the replication network and sends or receives updates. | Job Status | The current
                                                               					 state of this database. | Last
                                                            				  Changed | The time the
                                                               					 connection state was last changed. |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Datastore
                                                            						Name | Description |
| Server | Host
                                                               						  name of the server. |
| Node ID | Node ID
                                                               						  of the server in the Unified CCX cluster. |
| State | The
                                                               						  current connectivity status of the node in the replication network, which can
                                                               						  be one of the following values: DROPPED/ TIMED OUT The
                                                                     								server cannot be reached and is not available in the replicated network. ACTIVE/ CONNECTED The
                                                                     								server is connected in the replication network and sends or receives updates. |
| Job Status | The current
                                                               					 state of this database. |
| Last
                                                            				  Changed | The time the
                                                               					 connection state was last changed. |
| Step 2 | Click Reset
                                                				Replication to reset the replication if the replication is not
                                             			 functional between the two nodes. The Reset
                                                   				  Replication button will be enabled only when the database on both
                                                				the nodes are enabled. When the
                                                				subscriber goes down and it is required to make configuration updates from the
                                                				publisher, you can disable Config Datastore (CDS) and Historical Datastore
                                                				(HDS) on the subscriber using Disable CDS and HDS icon or button. The database
                                                				information for the cluster is displayed at the bottom of the window. Once the
                                                				subscriber is up, you can enable CDS and HDS on the subscriber using the same
                                                				toggle button. Caution Any
                                                            				  configuration in Application Administration and Historical data on the
                                                            				  Subscriber node would get over written, when CDS is enabled again. | Caution | Any
                                                            				  configuration in Application Administration and Historical data on the
                                                            				  Subscriber node would get over written, when CDS is enabled again. |
| Caution | Any
                                                            				  configuration in Application Administration and Historical data on the
                                                            				  Subscriber node would get over written, when CDS is enabled again. |

| Datastore
                                                            						Name | Description |
|---|---|
| Server | Host
                                                               						  name of the server. |
| Node ID | Node ID
                                                               						  of the server in the Unified CCX cluster. |
| State | The
                                                               						  current connectivity status of the node in the replication network, which can
                                                               						  be one of the following values: DROPPED/ TIMED OUT The
                                                                     								server cannot be reached and is not available in the replicated network. ACTIVE/ CONNECTED The
                                                                     								server is connected in the replication network and sends or receives updates. |
| Job Status | The current
                                                               					 state of this database. |
| Last
                                                            				  Changed | The time the
                                                               					 connection state was last changed. |

| Caution | Any
                                                            				  configuration in Application Administration and Historical data on the
                                                            				  Subscriber node would get over written, when CDS is enabled again. |
|---|---|

| Step 1 | Choose Tools > Datastore Control
                                                   				  Center . |
|---|---|
| Step 2 | Click Datastores from the Unified CCXServiceability menu
                                             			 bar to view replication status of all the Unified CCX datastores and to
                                             			 synchronize data. |
| Step 3 | Click Synchronize Data to synchronize data for each
                                             			 datastore except for the Configuration datastore between the two nodes in case
                                             			 of mismatch. |

| Field | Description |
|---|---|
| Server | Server
                                                					 machine name. |
| Replication
                                                					 Type | One of the
                                                					 following Enterprise Replication (ER) values in a High Availability deployment: ER—Publication ER—Subscription |
| Node ID | Node ID of
                                                					 server/node in Unified CCX cluster. |
| Read Access | Indicates
                                                					 whether data can be read from the datastore. Options: Yes, No. |
| Write Access | Indicates
                                                					 whether data can be written to the datastore. Options: Yes, No. |
| Replicate
                                                					 Status | Can be one
                                                					 of the following values: RUNNING All the
                                                      						  necessary database services are up and the datastore is functioning as
                                                      						  expected. RETRYING The
                                                      						  datastore is in partial service and might be in the state of restart. SHUTDOWN The
                                                      						  datastore is shutdown. UNKNOWN Unable
                                                      						  to determine the current status of the datastore. This value is shown in a
                                                      						  single-node deployment only. |
| Last Update
                                                					 Time | Indicates
                                                					 the last action the replication agent was performing. |
| Info | Use these
                                                					 icons to view further information in a new window: Check
                                                      						  Details Click
                                                      						  this icon to view information about data synchronization or repair jobs that
                                                      						  might have been initiated. History Click
                                                      						  this icon to view information about the replication latency (the time it takes
                                                      						  to replicate transactions). |

| Caution | Some changes to
                                             			 service parameters may cause system failure, thus do not make any changes to
                                             			 service parameters unless you fully understand the feature that you are
                                             			 changing or unless the Cisco Technical Assistance Center (TAC) specifies the
                                             			 changes. |
|---|---|

| Step 1 | From the Unified CCX Serviceability menu bar, choose Tools and click Service
                                             				Parameters . |
|---|---|
| Step 2 | Choose a server
                                          			 from the Server drop-down list box. If parameters are available for that
                                          			 server, the service drop down list box appears displaying the following
                                          			 services: Cisco AMC Service. Cisco Log Partition
                                             				Monitoring Tool. Cisco Trace Collection
                                             				Service. Cisco RIS Data Collector. Cisco Serviceability
                                             				Reporter. Cisco DRF local. Cisco DRF Master. Note Only the
                                                         				  common platform services mentioned above are supported currently for Unified CCX . | Note | Only the
                                                         				  common platform services mentioned above are supported currently for Unified CCX . |
| Note | Only the
                                                         				  common platform services mentioned above are supported currently for Unified CCX . |
| Step 3 | Choose the
                                          			 service that contains the parameter that you want to update from the Service
                                          			 drop-down list box. Note The Service
                                                         				  Parameter Configuration window displays all services (active or not active). | Note | The Service
                                                         				  Parameter Configuration window displays all services (active or not active). |
| Note | The Service
                                                         				  Parameter Configuration window displays all services (active or not active). |
| Step 4 | The parameters
                                          			 for the selected service are displayed and the suggested values (if available)
                                          			 are listed against each one of them. Update the appropriate parameter value. |
| Step 5 | Click Save . The modified
                                             				values are saved and the new values are reflected on subsequent access to the
                                             				service's parameters. Click Set to
                                                				  Default to set all service parameters for this instance of the
                                             				service to the default value. A warning is displayed that this action cannot be
                                             				undone and only on confirmation, the parameter values for the selected service
                                             				is set to the default values. Note Currently, you
                                                         				  cannot configure any parameters for the following platform services: Cisco
                                                         				  Trace Collection Service and Cisco Log Partition Monitoring Tool. | Note | Currently, you
                                                         				  cannot configure any parameters for the following platform services: Cisco
                                                         				  Trace Collection Service and Cisco Log Partition Monitoring Tool. |
| Note | Currently, you
                                                         				  cannot configure any parameters for the following platform services: Cisco
                                                         				  Trace Collection Service and Cisco Log Partition Monitoring Tool. |

| Note | Only the
                                                         				  common platform services mentioned above are supported currently for Unified CCX . |
|---|---|

| Note | The Service
                                                         				  Parameter Configuration window displays all services (active or not active). |
|---|---|

| Note | Currently, you
                                                         				  cannot configure any parameters for the following platform services: Cisco
                                                         				  Trace Collection Service and Cisco Log Partition Monitoring Tool. |
|---|---|

| Step 1 | From the Cisco Unified CCX Serviceability
                                          			 menu bar, choose Tools > Performance Configuration and
                                                				  Logging . |
|---|---|
| Step 2 | Choose a server
                                          			 from the Server drop-down list box and click Go . The first node
                                             				is selected by default and JVM options for the Unified CCX Engine service in
                                             				the first node is displayed. |
| Step 3 | Choose a service
                                          			 for which you want to see the JVM options from the Service drop-down list box.
                                          			 You should be able to select any one of the following services from this list
                                          			 box: Cisco Unified CCX Cluster View Daemon Cisco Unified CCX Engine Cisco Unified CCX Serviceability The following JVM options are displayed for each service: PrintClassHistogram PrintGCDetails PrintGC PrintGCTimeStamps |
| Step 4 | Click the Dump
                                             				Thread Trace icon or button to dump the thread traces for the
                                          			 selected service in the selected server. You can collect the corresponding
                                          			 jvm.log from the log folder for that facility using Real-Time Monitoring Tool
                                          			 (RTMT). |
| Step 5 | Click the Dump
                                             				Memory Trace icon or button to dump the memory traces. This creates
                                          			 the following two logs in the log folder for that facility. Memory-<facility name>-<time stamp>.hprof (for heap
                                                				  dump) histo-<facility name> <time stamp>.log (for
                                                				  histogram) |
| Step 6 | You can change
                                          			 the JVM options by clicking Enable or Disable radio buttons in this page. Click the Update
                                                				  JVM Options icon or button to update the new settings for selected
                                             				service on selected node. |