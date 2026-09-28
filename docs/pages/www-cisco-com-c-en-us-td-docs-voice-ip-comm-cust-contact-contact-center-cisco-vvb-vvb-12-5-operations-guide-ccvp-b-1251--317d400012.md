---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-cisco-vvb-vvb-12-5-operations-guide-ccvp-b-1251--317d400012
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/cisco_vvb/VVB_12_5/operations/guide/ccvp_b_1251-cisco-virtualized-voice-browser-serviceability-administration-guide/ccvp_b_1251-cisco-virtualized-voice-browser-serviceability-administration-guide_chapter_011.html
retrieved_at: 2026-08-21T16:34:41.377543+00:00
---

Cisco Virtualized Voice Browser Serviceability Administration Guide, Release 12.5(1)

# Cisco Virtualized Voice Browser Serviceability Administration Guide, Release 12.5(1)

Updated: February 2, 2020

Chapter: Traces

## Chapter: Traces

# Traces

A trace
                           		  file is a log file that records activity from the Cisco VVB components. Trace files let you obtain specific, detailed information about the
                           		  system that can help you troubleshoot problems.

The Cisco VVB system
                           		  can generate trace information for different services. This information is
                           		  stored in a trace file. To help you control the size of a trace file, you can
                           		  specify the services for which you want to collect information and the level of
                           		  information that you want to collect.

The Cisco VVB system
                           		  also generates information about all threads that are running on the system.
                           		  This information is stored in the thread dump file and is useful for
                           		  troubleshooting.

## Component Trace
                        	 Files

The component trace file
                              		  contains information about each component. You can create a trace file for any
                              		  of the following Cisco VVB components:

Administration

Engine

Speech Server

The component
                              		  trace file contains information about each component. To set up the trace file,
                              		  follow the procedure mentioned in Configure Trace Parameters section.

After configuring the
                              		  information that you want to include in the trace files for the various
                              		  services, you can collect and view trace files by using the trace and log
                              		  central option in the Cisco Unified Real-Time Monitoring Tool.

## Configure Trace
                        	 Parameters

To update
                              		  trace file information and to activate and deactivate logging, follow the
                              		  procedure mentioned below:

From the Cisco VVB
                                          				Serviceability menu bar, choose Trace > Configuration .

The Trace Configuration web
                                          				page opens displaying the default trace configuration for Cisco VVB Engine.

From the Select Service drop-down list box, choose a service or component for which you want to configure trace. Then, click Go .

You should be able to view the existing Trace configurations and debug levels for the selected Cisco VVB service with check boxes for the various Debugging and XDebugging levels for each sub facility.

Cisco VVB Components

Subfacilities or Services

Cisco VVB Administration

Libraries

Managers

Miscellaneous

Cisco VVB Engine

Libraries

Managers

Miscellaneous

Steps

Subsystems

Cisco VVB Speech Server

Subsystems

Update the debug
                                       			 level for one or more of the libraries or sub facilities for the selected
                                       			 service by doing the following:

To activate
                                             				  traces for a specific component or logging for a server, check the check box
                                             				  for the service that you chose.

To
                                             				  deactivate logging for a server, uncheck the specific check box.

To limit the
                                       			 number and size of the trace files, you can specify the trace output setting
                                       			 using the following two fields. See the following table for description and
                                       			 default values for these two fields.

Field

Description

Maximum No. of Files

The
                                                      							 maximum number of trace files to be retained by the system.

This
                                                      							 field specifies the total number of trace files for a given service. Cisco VVB Serviceability automatically appends a sequence number to the file name to
                                                      							 indicate which file it is; for example, Cisco001MADM14.log. When the last file
                                                      							 in the sequence is full, the trace data begins writing over the first file. The
                                                      							 default value varies by service.

Maximum File Size

This field specifies the maximum size of the trace file in kilobytes or megabytes depending on the selected service. The default
                                                      value varies by service.

Click Save icon in the tool bar in the upper, left corner of the window or the Save button at the bottom of the window to save your trace parameter configuration. The settings are updated in the system and
                                       the trace files will be generated as per the saved settings. Click Restore Defaults icon to revert to the default settings for the selected service.

You should activate additional logging only for the purpose of debugging and remember to deactivate logging once the debugging
                                                      session is complete.

## Trace Level
                        	 Options

A trace
                              		  file is a log file that records activity from the Cisco VVB component
                              		  subsystems and steps. Trace files let you obtain specific, detailed information
                              		  about the system that can help you troubleshoot problems.

The Cisco VVB system can
                              		  generate trace information for every component. This information is stored in
                              		  an trace file. To help you control the size of an trace file, you specify the
                              		  components for which you want to collect information and the level of
                              		  information that you want to collect.

A trace
                              		  file that records all information for a component, such as 
                              		  
                              		  Engine, can become large and difficult to read. To help you manage the trace
                              		  file, the Cisco VVB system lets
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

## Trace file
                        	 location

You can collect and view
                              		  trace information using the Real-Time Monitoring Tool (RTMT).

### Trace File Information

The trace files contain information in standard Syslog format. The file includes some or all of the following information
                                 for each event that it records:

Line number

Date and time the event occurred

Facility and subfacility (component) name

Severity level

Message name

Explanation

Parameters and values

## Log Profiles
                        	 Management

Log
                              		  Profile is an aggregated entity that preserves trace settings of the following Cisco VVB services:

Cisco VVB
                                       				Engine (Traces termed as MIVR)

Cisco VVB
                                       				Administration (Traces termed as MADM)

Choose Trace > Profile from the Cisco
                                 			 VVB Serviceability menu bar to access the Log Profiles Management web
                              		  page. The Log Profiles Management web page opens displaying the available log
                              		  profiles each with a radio button. You can perform different operations on the
                              		  listed log profiles, which are explained in detail in the following
                              		  sub-sections.

Log
                              		  profiles in Cisco VVB can be one
                              		  of the following two types:

System Log
                                       				Profiles: These log profiles are pre-installed with Cisco VVB and you
                                       				cannot modify these profiles.

The following
                                       				table provides information on the log profiles that are factory shipped with Cisco VVB :

Name

Scenario
                                                      					 in which this profile must be activated

DefaultVVB

Generic
                                                      					 logs are enabled.

AppAdminVVB

For issues
                                                      					 with web administration through AppAdmin, Cisco VVB Serviceability, and other
                                                      					 web pages.

MediaVVB

For issues
                                                      					 with media setup or media transmission.

VoiceBrowserVVB

For issues
                                                      					 with handling calls.

MRCPVVB

For issues
                                                      					 with ASR/TTS with Cisco VVB interaction.

CallControlVVB

For issues
                                                      					 with SIP signaling related are published in the log.

### Enable
                           	 Profile

To enable
                                 		  or activate a log profile, perform the following steps:

From the Cisco
                                             				VVB Serviceability menu bar, choose Trace > Profile . The Log Profiles Management
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

The trace
                                          			 setting for the selected profile is transferred to system's trace settings and
                                          			 on successful activation, a message will be displayed in the status bar.

| Step 1 | From the Cisco VVB
                                          				Serviceability menu bar, choose Trace > Configuration . The Trace Configuration web
                                          				page opens displaying the default trace configuration for Cisco VVB Engine. |
|---|---|
| Step 2 | From the Select Service drop-down list box, choose a service or component for which you want to configure trace. Then, click Go . You should be able to view the existing Trace configurations and debug levels for the selected Cisco VVB service with check boxes for the various Debugging and XDebugging levels for each sub facility. The debug levels for different Cisco VVB subfacilities or services might vary depending on the selected service and are listed
                                          in the following table: Table 1. Debug Levels for Different Cisco VVB Subfacilities Cisco VVB Components Subfacilities or Services Cisco VVB Administration Libraries Managers Miscellaneous Cisco VVB Engine Libraries Managers Miscellaneous Steps Subsystems Cisco VVB Speech Server Subsystems | Cisco VVB Components | Subfacilities or Services | Cisco VVB Administration | Libraries Managers Miscellaneous | Cisco VVB Engine | Libraries Managers Miscellaneous Steps Subsystems | Cisco VVB Speech Server | Subsystems |
| Cisco VVB Components | Subfacilities or Services |
| Cisco VVB Administration | Libraries Managers Miscellaneous |
| Cisco VVB Engine | Libraries Managers Miscellaneous Steps Subsystems |
| Cisco VVB Speech Server | Subsystems |
| Step 3 | Update the debug
                                       			 level for one or more of the libraries or sub facilities for the selected
                                       			 service by doing the following: To activate
                                             				  traces for a specific component or logging for a server, check the check box
                                             				  for the service that you chose. To
                                             				  deactivate logging for a server, uncheck the specific check box. |
| Step 4 | To limit the
                                       			 number and size of the trace files, you can specify the trace output setting
                                       			 using the following two fields. See the following table for description and
                                       			 default values for these two fields. Field Description Maximum No. of Files The
                                                      							 maximum number of trace files to be retained by the system. This
                                                      							 field specifies the total number of trace files for a given service. Cisco VVB Serviceability automatically appends a sequence number to the file name to
                                                      							 indicate which file it is; for example, Cisco001MADM14.log. When the last file
                                                      							 in the sequence is full, the trace data begins writing over the first file. The
                                                      							 default value varies by service. Maximum File Size This field specifies the maximum size of the trace file in kilobytes or megabytes depending on the selected service. The default
                                                      value varies by service. | Field | Description | Maximum No. of Files | The
                                                      							 maximum number of trace files to be retained by the system. This
                                                      							 field specifies the total number of trace files for a given service. Cisco VVB Serviceability automatically appends a sequence number to the file name to
                                                      							 indicate which file it is; for example, Cisco001MADM14.log. When the last file
                                                      							 in the sequence is full, the trace data begins writing over the first file. The
                                                      							 default value varies by service. | Maximum File Size | This field specifies the maximum size of the trace file in kilobytes or megabytes depending on the selected service. The default
                                                      value varies by service. |
| Field | Description |
| Maximum No. of Files | The
                                                      							 maximum number of trace files to be retained by the system. This
                                                      							 field specifies the total number of trace files for a given service. Cisco VVB Serviceability automatically appends a sequence number to the file name to
                                                      							 indicate which file it is; for example, Cisco001MADM14.log. When the last file
                                                      							 in the sequence is full, the trace data begins writing over the first file. The
                                                      							 default value varies by service. |
| Maximum File Size | This field specifies the maximum size of the trace file in kilobytes or megabytes depending on the selected service. The default
                                                      value varies by service. |
| Step 5 | Click Save icon in the tool bar in the upper, left corner of the window or the Save button at the bottom of the window to save your trace parameter configuration. The settings are updated in the system and
                                       the trace files will be generated as per the saved settings. Click Restore Defaults icon to revert to the default settings for the selected service. Caution You should activate additional logging only for the purpose of debugging and remember to deactivate logging once the debugging
                                                      session is complete. | Caution | You should activate additional logging only for the purpose of debugging and remember to deactivate logging once the debugging
                                                      session is complete. |
| Caution | You should activate additional logging only for the purpose of debugging and remember to deactivate logging once the debugging
                                                      session is complete. |

| Cisco VVB Components | Subfacilities or Services |
|---|---|
| Cisco VVB Administration | Libraries Managers Miscellaneous |
| Cisco VVB Engine | Libraries Managers Miscellaneous Steps Subsystems |
| Cisco VVB Speech Server | Subsystems |

| Field | Description |
|---|---|
| Maximum No. of Files | The
                                                      							 maximum number of trace files to be retained by the system. This
                                                      							 field specifies the total number of trace files for a given service. Cisco VVB Serviceability automatically appends a sequence number to the file name to
                                                      							 indicate which file it is; for example, Cisco001MADM14.log. When the last file
                                                      							 in the sequence is full, the trace data begins writing over the first file. The
                                                      							 default value varies by service. |
| Maximum File Size | This field specifies the maximum size of the trace file in kilobytes or megabytes depending on the selected service. The default
                                                      value varies by service. |

| Caution | You should activate additional logging only for the purpose of debugging and remember to deactivate logging once the debugging
                                                      session is complete. |
|---|---|

| Component Code | Description |
|---|---|
| APP_MGR | Applications Manager |
| ARCHIVE_MGR | Archive Manager |
| BOOTSTRAP_MGR | Cisco VVB Bootstrap
                                       				  Manager |
| CFG_MGR | Configuration Manager |
| CHANNEL_MGR | Channel Manager |
| CLUSTER_MGR | Cluster Manager |
| CONTACT_MGR | Contact Manager |
| DOC_MGR | Document Manager |
| ENG | Engine |
| EXECUTOR_MGR | Executor Manager |
| GENERIC | Generic catalog for a
                                       				  facility |
| JASMIN | Java Signaling and
                                       				  Monitoring Interface |
| LIB_CFG | Configuration Library |
| LIB_EVENT | Event Message Library |
| LIB_JDBC | JDBC Library |
| LIB_JINI | JINI Services |
| LIB_LICENSE | License Library |
| LIB_MEDIA | Media Library |
| LIB_RMI | Java Remote Method
                                       				  Invocation Library |
| LIB_SERVLET | Servlet Library |
| LIB_TC | Tomcat Library |
| LOG_MGR | Log Manager |
| MGR_MGR | Manager Manager |
| NODE_MGR | Node Manager |
| PROMPT_MGR | Prompt Manager |
| RTPPORT_MGR | RTP Manager |
| SCRIPT_MGR | Script Manager |
| SESSION_MGR | Session Manager |
| SIP_STACK | SIP Stack logging |
| SOCKET_MGR | Socket Manager |
| SS_CMT | Cisco Media Termination
                                       				  Subsystem |
| SS_DB | Database Subsystem |
| SS_HTTP | HTTP Subsystem |
| SS_MRCP_ASR | MRCP ASR Subsystem |
| SS_MRCP_TTS | MRCP TTS Subsystem |
| SS_RM | Resource Manager Subsystem |
| SS_RMCM | Resource Manager Contact
                                       				  Manager Subsystem |
| SS_ROUTEANDQUEUE | Route and Queue Subsystem |
| SS_RTR | Real-Time Reporting
                                       				  Subsystem |
| SS_SIP | SIP Subsystem |
| SS_VB | Voice Browser Subsystem |
| STEP_CALL_CONTROL | Call Control Steps |
| STEP_MEDIA_CONTROL | Media Control Steps |
| STEP_SESSION_MGMT | Session Management Steps |
| STEP_CALL_CONTACT | Call Contact Steps |
| STEPS_CONTACT | Contact Steps |
| STEPS_DB | Database Steps |
| STEPS_DOCUMENT | Document Steps |
| STEPS_GRAMMAR | Grammar Steps |
| STEPS_ICM | Cisco Unified ICME Steps |
| STEPS_JAVA | Java Steps |
| STEPS_PROMPT | Prompt Steps |
| STEPS_SESSION | Session Steps |
| STEPS_USER | User Steps |

| Name | Scenario
                                                      					 in which this profile must be activated |
|---|---|
| DefaultVVB | Generic
                                                      					 logs are enabled. |
| AppAdminVVB | For issues
                                                      					 with web administration through AppAdmin, Cisco VVB Serviceability, and other
                                                      					 web pages. |
| MediaVVB | For issues
                                                      					 with media setup or media transmission. |
| VoiceBrowserVVB | For issues
                                                      					 with handling calls. |
| MRCPVVB | For issues
                                                      					 with ASR/TTS with Cisco VVB interaction. |
| CallControlVVB | For issues
                                                      					 with SIP signaling related are published in the log. |

| Step 1 | From the Cisco
                                             				VVB Serviceability menu bar, choose Trace > Profile . The Log Profiles Management
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