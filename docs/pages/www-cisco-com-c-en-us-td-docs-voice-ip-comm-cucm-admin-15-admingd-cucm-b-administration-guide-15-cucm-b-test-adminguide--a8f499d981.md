---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-admin-15-admingd-cucm-b-administration-guide-15-cucm-b-test-adminguide--a8f499d981
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/admin/15/adminGd/cucm_b_administration-guide-15/cucm_b_test-adminguide_chapter_011000.html
retrieved_at: 2026-08-17T00:37:20.719202+00:00
---

Administration Guide for Cisco Unified Communications Manager, Release 15 and SUs

# Administration Guide for Cisco Unified Communications Manager, Release 15 and SUs

Updated: October 31, 2025

Chapter: Trace

## Chapter: Trace

# Trace

## Trace

Cisco Unified Serviceability provides trace tools to assist you in troubleshooting issues with your voice application. Cisco Unified Serviceability supports SDI (System Diagnostic Interface) trace, SDL (Signaling Distribution Layer) trace (for Cisco CallManager and Cisco
                              CTIManager services, applicable to Unified Communications Manager only), and Log4J trace (for Java applications).

You use the Trace Configuration window to specify the level of information that you want traced as well the type of information
                              that you want to be included in each trace file.

Unified Communications Manager only: If the service is a call-processing application such as Cisco CallManager or Cisco CTIManager,
                              you can configure a trace on devices such as phones and gateway.

Unified Communications Manager only: In the Alarm Configuration window, you can direct alarms to various locations, including
                              SDL trace log files. If you want to do so, you can configure trace for alerts in the Cisco Unified Real-Time Monitoring Tool (Unified RTMT).

After you have configured information that you want to include in the trace files for the various services, you can collect
                              and view trace files by using the Trace and Log Central option in the Cisco Unified Real-Time Monitoring Tool .

Cisco Unified IM and Presence Serviceability provides trace tools to assist you in troubleshooting issues with your instant messaging and presence application. Cisco Unified IM and Presence Serviceability supports:

SDI trace

Log4J trace (for Java applications)

You can configure the level of information that you want traced (debug level), what information you want to trace (trace fields),
                              and information about the trace files (such as number of files per service, size of file, and time that the data is stored
                              in the trace files).  You can configure trace for a single service or apply the trace settings for that service to all servers
                              in the cluster.

In the Alarm Configuration window, you can direct alarms to various locations. If you want to do so, you can configure trace for alerts in the IM and Presence Unified RTMT.

After you have configured information that you want to include in the trace files for the various services, you can collect
                              and view trace files by using the Trace and Log Central option in the Unified RTMT. You can configure trace parameters for
                              any feature or network service that is available on any IM and Presence node in the cluster. Use the Trace Configuration window to specify the parameters that you want to trace for troubleshooting problems. If you want to use predetermined troubleshooting
                              trace settings rather than choosing your own trace fields, you can use the Troubleshooting Trace Setting window.

Enabling Trace decreases system performance; therefore, enable Trace only for troubleshooting purposes. For assistance in
                                          using Trace, contact Cisco Technical Assistance Center (TAC).

### Trace Configuration

You can configure trace parameters for any feature or network service that displays in the Serviceability interface. If you
                              have clusters, you can configure trace parameters for any feature or network service that is available on any  server in the
                              cluster. Use the Trace Configuration window to specify the parameters that you want to trace for troubleshooting problems.

You can configure the level of information that you want traced (debug level), what information you want to trace (trace fields),
                              and information about the trace files (such as number of files per service, size of file, and time that the data is stored
                              in the trace files). If you have clusters, you can configure trace for a single service or apply the trace settings for that
                              service to all servers in the cluster.

If you want to use predetermined troubleshooting trace settings rather than choosing your own trace fields, you can use the
                              Troubleshooting Trace window. For more information on troubleshooting trace, see Trace settings.

After you have configured information that you want to include in the trace files for the various services, you can collect
                              trace files by using the trace and log central option in Unified RTMT. For more information regarding trace collection, see
                              Trace collection.

### Trace Settings

The Troubleshooting Trace Settings window allows you to choose the services for which you want to set predetermined troubleshooting
                              trace settings. In this window, you can choose a single service or multiple services and change the trace settings for those
                              services to the predetermined trace settings. If you have clusters, you can choose the services on different servers in the
                              cluster, so the trace settings of the chosen services get changed to the predetermined trace settings. You can choose specific
                              activated services for a single server, all activated services for the server, specific activated services for all servers
                              in the cluster, or all activated services for all servers in the cluster. In the window, N/A displays next to inactive services.

The predetermined troubleshooting trace settings for a  feature or network service include SDL, SDI, and Log4j trace settings.
                                          Before the troubleshooting trace settings are applied, the system backs up the original trace settings. When you reset the
                                          troubleshooting trace settings, the original trace settings are restored.

When you open the Troubleshooting Trace Settings window after you apply troubleshooting trace settings to a service, the service
                              that you set for troubleshooting displays as checked. In the Troubleshooting Trace Settings window, you can reset the trace
                              settings to the original settings.

After you apply Troubleshooting Trace Setting to a service, the Trace Configuration window displays a message that troubleshooting
                              trace is set for that service. From the Related Links drop-down list box, you can choose the Troubleshooting Trace Settings
                              option if you want to reset the settings for the service. For the given service, the Trace Configuration window displays all
                              the settings as read-only, except for some parameters of trace output settings, for example, Maximum No. of Files. You can
                              modify these parameters even after you apply troubleshooting trace settings.

### Trace Collection

Use Trace and Log Central , an option in the Cisco Unified Real-Time Monitoring Tool , to collect, view, and zip various service traces or other log files. With the Trace and Log Central option, you can collect SDL/SDI traces, Application Logs, System Logs (such as Event View Application, Security, and System
                              logs), and crash dump files.

Tip

Do not use Windows NotePad to view collected trace files to view collected trace files, because Windows NotePad does not properly
                                          display line
                                          breaks.

Unified Communications Manager only: For devices that support encryption, the Secure Real-time Transport Protocol (SRTP) keying
                                          material does not display in the trace file.

For more information about trace collection, see Cisco Unified Real-Time Monitoring Tool Administration Guide .

### Called Party Tracing

Called Party Tracing allows you to configure a directory number or list of directory numbers that you want to trace. You can
                              request on-demand tracing of calls using the Session Trace Tool.

For more information, see the Cisco Unified Real-Time Monitoring Tool Administration Guide .

### Set Up Trace Configuration

The following procedure provides an overview of the steps to
                                 		  configure and collect trace for feature and network services in 
                                 		  the Serviceability interface.

Step 1

Configure the values of the TLC Throttling CPU Goal and TLC
                                          			 Throttling IOWait Goal service parameters (Cisco RIS Data Collector service) by performing one of these steps:

Cisco Unified Communications Manager Administration and Cisco Unified IM and Presence : Select System > ServiceParameters and configure the values of the TLC Throttling CPU Goal and TLC Throttling IOWait Goal service parameters (Cisco RIS Data
                                                Collector service).

Cisco Unity Connection only: Select System
                                                      						Settings > Service Parameters in Cisco Unity Connection Administration and configure the values of the TLC
                                                				  Throttling CPU Goal and TLC Throttling IOWait Goal service parameters (Cisco
                                                				  RIS Data Collector service).

Step 2

Configure the trace setting for the service for which you want to
                                          			 collect traces. If you have clusters, you can configure trace for the service on one server
                                          			 or on all servers in the cluster.

To configure trace settings, choose what information you
                                             				want to include in the trace log by choosing the debug level and trace fields.

If you want to run predetermined traces on services, set
                                             				troubleshooting trace for those services.

Step 3

Install the Cisco Unified Real-Time Monitoring Tool on a local PC.

Step 4

If you want to generate an alarm when the specified search string
                                          			 exists in a monitored trace file, enable the LogFileSearchStringFound alert in Unified
                                          			 RTMT.

You can find the LogFileSearchStringFound alarm in the
                                             				LpmTctCatalog. (Select Alarms > Definitions .
                                             				In the Find alarms where drop-down list box, choose the System Alarm Catalog ; in the Equals
                                             				drop-down list box, choose LpmTctCatalog ).

Step 5

If you want to automatically capture traces for alerts such as
                                          			 CriticalServiceDownand CodeYellow, check the Enable Trace Download check box in the Set
                                          			 Alert/Properties dialog box for the specific alert in Unified RTMT; configure how often
                                          			 that you want the download to occur.

Step 6

Collect the traces.

Step 7

View the log file in the appropriate viewer.

Step 8

If you enabled troubleshooting trace, reset the trace settings
                                          			 services, so the original settings are restored.

Leaving troubleshooting trace enabled for a long time increases
                                                         				  the size of the trace files and may affect the performance of the services.

## Configure Trace

This section provides information for configuring trace settings.

Enabling trace decreases system performance; therefore, enable trace
                                       		  only for troubleshooting purposes. For assistance in using trace, contact your
                                       		  technical support team.

### Set Up Trace Parameters

This section describes how to configure trace parameters for
                                 		  feature and network services that you manage through 
                                 		  the Serviceability GUI .

Tip

For Cisco Unity Connection , you may need to run trace in Cisco Unified Serviceability and Cisco Unity Connection Serviceability to troubleshoot Cisco Unity Connection issues. For
                                             			 information on how to run trace in Cisco Unity Connection Serviceability , refer to the Cisco Unity Connection Serviceability Administration Guide .

Step 1

Select Trace > Configuration .

The Trace Configuration window displays.

Step 2

From the Server drop-down list box, select the server that is
                                          			 running the service for which you want to configure trace; then, click Go .

Step 3

From the Service Group drop-down list box, select the service
                                          			 group for the service that you want to configure trace; then, click Go .

Tip

The Service Groups in Trace Configuration table
                                                         				  lists the services and trace libraries that correspond to the options that
                                                         				  display in the Service Group drop-down list box.

Step 4

From the Service drop-down list box, select the service for which
                                          			 you want to configure trace and, click Go .

The drop-down list box displays active and inactive services.

Tip

Cisco Unity Connection only: For the Cisco CallManager and
                                                         				  CTIManager services, you can configure SDL trace parameters. To do so, open the
                                                         				  Trace Configuration window for one of those services, and click the Go button that is next to the Related
                                                         				  Links drop-down list box.

If you configured Troubleshooting Trace for the service, a message
                                             				displays at the top of the window that indicates that the Troubleshooting
                                             				Traces feature is set, which means that the system disables all fields in the
                                             				Trace Configuration window except for Trace Output Settings. To configure the
                                             				Trace Output Settings, go to 
                                             				Step 11.
                                             				To reset Troubleshooting Trace, see the 
                                             				Set up troubleshooting trace settings.

The trace parameters display for the service that you chose. In addition, the Apply to All Nodes check box displays (Unified
                                             Communications Manager only).

Step 5

Unified Communications Manager and IM and Presence only: If you want to do so, you can apply the trace
                                          			 settings for the service or trace library to all servers in the cluster by
                                          			 checking the Apply to All Nodes check box; that is, if your
                                          			 configuration supports clusters.

Step 6

Check the Trace On check box.

Step 7

Cisco Unity Connection only: If you are configuring SDL
                                          			 trace parameters, go to 
                                          			 Step 10.

Step 8

Select the level of information that you want traced from the Debug Trace Level list box, as described in 
                                          			 Debug trace level settings.

Step 9

Check the Trace Fields check box for the service that you chose,
                                          			 for example, Cisco Log Partition Monitoring Tool Trace Fields.

Step 10

If the service does not have multiple trace settings where you can
                                          			 specify the traces that you want to activate, check the Enable All Trace check box. If the service
                                          			 that you chose has multiple trace settings, check the check boxes next to the
                                          			 trace check boxes that you want to enable, as described in 
                                          			 Trace field descriptions.

Step 11

To limit the number and size of the trace files, specify the trace
                                          			 output setting. See 
                                          			 Trace Ouput Settings
                                          			 for descriptions.

Step 12

To save your trace parameters configuration, click the Save button.

The changes to trace configuration take effect immediately for all services except Cisco Messaging Interface (Unified Communications
                                             Manager only). The trace configuration changes for Cisco Messaging Interface take effect in 3 to 5 minutes.

To set the default, click the Set Default button.

### Service Groups in Trace Configuration

The following
                              		table lists the services and trace libraries that correspond to the options in
                              		the Service Group drop-down list box in the Trace Configuration window.

Service Group

Services and Trace Libraries

Notes

Unified Communications Manager

CM
                                          				  Services

- Cisco CTIManager

- Cisco CallManager

- Cisco CallManager Cisco IP
                                             					 Phone Service

- Cisco DHCP Monitor Service

- Cisco Dialed Number
                                             					 Analyzer

- Cisco Dialed Number
                                             					 Analyzer Server

- Cisco Extended Functions,
                                             					 Cisco Extension Mobility

- Cisco Extension Mobility
                                             					 Application

- Cisco IP Voice Media
                                             					 Streaming App

- Cisco Messaging Interface

- Cisco TFTP

- Cisco Unified Mobile Voice
                                             					 Access Service

For
                                          				  most services in the CM Services group, you run trace for specific components,
                                          				  instead of enabling all trace for the service. The Trace field descriptions
                                          				  lists the services for which you can run trace for specific components.

Unified Communications Manager

CTI
                                          				  Services

- Cisco IP Manager Assistant

- Cisco Web Dialer Web
                                             					 Service

For
                                          				  these services, you can run trace for specific components, instead of enabling
                                          				  all trace for the service; see the Trace field descriptions.

Unified Communications Manager

CDR
                                          				  Services

- Cisco Unified Communications Manager CDR Analysis and Reporting Scheduler

- Cisco Unified Communications Manager CDR Analysis and Reporting Web Service

- Cisco CDR Agent

- Cisco CDR Repository
                                             					 Manager

You
                                          				  enable all trace for each service, instead of running trace for specific
                                          				  components.

In Cisco Unified Communications Manager CDR Analysis and Reporting, when reports are run that call stored procedures, Cisco
                                          Unified Communications Manager CDR Analysis and Reporting checks the configured debug trace level for the Cisco Unified Communications
                                          Manager CDR Analysis and Reporting Scheduler service and the Cisco Unified Communications Manager CDR Analysis and Reporting
                                          Web Service in the Trace Configuration window before stored procedure logging begins. For pregenerated reports, Cisco Unified
                                          Communications Manager CDR Analysis and Reporting checks the level for the Cisco Unified Communications Manager CDR Analysis
                                          and Reporting Scheduler service; for on-demand reports, Cisco Unified Communications Manager CDR Analysis and Reporting checks
                                          the level for the Cisco Unified Communications Manager CDR Analysis and Reporting Web Service. If you choose Debug from the
                                          Debug Trace Level drop-down list box, stored procedure logging gets enabled and continues until you choose another option
                                          from the drop-down list box. The following Cisco Unified Communications Manager CDR Analysis and Reporting reports use stored
                                          procedure logging: Gateway Utilization report, Route and Line Group Utilization report, Route/Hunt List Utilization report,
                                          Route Pattern/Hunt Pilot Utilization report, Conference Call Details report, Conference Call Summary report, Conference Bridge
                                          Utilization report, Voice Messaging Utilization report, and the CDR Search report.

IM and Presence Services

- Cisco Client Profile Agent

- Cisco Config Agent

- Cisco Intercluster Sync
                                             					 Agent

- Cisco Login Datastore

- Cisco OAM Agent

- Cisco Presence Datastore

- Cisco Presence Engine

- Cisco IM and Presence Data Monitor

- Cisco Route Datastore

- Cisco SIP Proxy

- Cisco SIP Registration
                                             					 Datastore

- Cisco Server Recovery
                                             					 Manager

- Cisco Sync Agent

- Cisco XCP Authentication
                                             					 Service

- Cisco XCP Config Manager

- Cisco XCP Connection
                                             					 Manager

- Cisco XCP Directory Service

- Cisco XCP Message Archiver

- Cisco XCP Router

- Cisco XCP SIP Federation
                                             					 Connection Manager

- Cisco XCP Text Conference
                                             					 Manager

- Cisco XCP Web Connection
                                             					 Manager

- Cisco XCP XMPP Federation
                                             					 Connection Manager

See topics
                                          				  related to feature and network services in Cisco Unified IM and Presence Serviceability for a
                                          				  description of these services.

- For these services, you
                                             					 should enable all trace for the service, instead of running trace for specific
                                             					 components.

Database and Admin Services

Unified Communications Manager and Cisco Unity Connection:

- Cisco AXL Web Service

- Cisco CCM DBL Web Library

- Cisco CCMAdmin Web Service

- Cisco CCMUser Web Service

- Cisco Database Layer
                                             					 Monitor

- Cisco UXL Web Service

Unified Communications Manager

- Cisco Bulk Provisioning
                                             					 Service

- Cisco GRT Communications
                                             					 Web Service

- Cisco Role-based Security

- Cisco TAPS Service

- Cisco Unified Reporting Web
                                             					 Service

IM and
                                          				  Presence Services:

- Cisco AXL Web Service

- Cisco Bulk Provisioning
                                             					 Service

- Cisco CCMUser Web Service

- Cisco Database Layer
                                             					 Monitor

- Cisco GRT Communications
                                             					 Web Service

- Cisco IM and Presence Admin

- Cisco Unified Reporting Web
                                             					 Service

- Platform Administrative
                                             					 Web Service

Choosing the Cisco CCM DBL Web Library option activates the
                                          				  trace for database access for Java applications. For database access for C++
                                          				  applications, activate trace for Cisco Database Layer Monitor, as described in
                                          				  the Cisco Extended Functions trace fields.

Choosing the Cisco Role-based Security option, which supports Unified Communications Manager, activates trace for user-role
                                          authorization.

For most services in the Database and Admin Services group, you
                                          				  enable all trace for the service/library, instead of enabling trace for
                                          				  specific components. For Cisco Database Layer Monitor, you can run trace for
                                          				  specific components.

You can control logging for services in the Cisco Unified IM and Presence Serviceability UI. To change the log level, select the System Services group and Cisco CCMService Web Service.

Performance and Monitoring Services

Unified Communications Manager and Cisco Unity Connection:

- Cisco AMC Service

- Cisco CCM NCS Web Library

- CCM PD Web Service

- Cisco CallManager SNMP
                                             					 Service

- Cisco Log Partition
                                             					 Monitoring Tool

- Cisco RIS Data Collector

- Cisco RTMT Web Service

- Cisco Audit Event Service

- Cisco RisBean Library

Unified Communications Manager:

- Cisco CCM PD Web Service

IM and
                                          				  Presence Services:

- Cisco AMC Service

- Cisco Audit Event Service

- Cisco Log Partition
                                             					 Monitoring Tool

- Cisco RIS Data Collector

- Cisco RTMT Web Service

- Cisco RisBean Library

Choosing the Cisco CCM NCS Web Library option activates trace
                                          				  for database change notification for the Java client.

Choosing the Cisco Unity RTMT Web Service option activates trace
                                          				  for the Unity RTMT servlets; running this trace creates the server-side log for
                                          				  Unity RTMT client queries.

Unified Communications Manager

Security Services

- Cisco CTL Provider

- Cisco Certificate
                                             					 Authority Proxy Function

- Cisco Trust Verification
                                             					 Service

You enable all trace for each service, instead of running trace
                                          				  for specific components.

Unified Communications Manager

Directory Services

Cisco
                                          				  DirSync

You enable all trace for this service, instead of running trace
                                          				  for specific components.

Backup and Restore Services

- Cisco DRF Local

- Unified Communications Manager and Cisco Unity Connection only: Cisco DRF Master

You enable all trace for each service, instead of running trace
                                          				  for specific components.

System Services

Unified Communications Manager:

- Cisco CCMRealm Web
                                             					 Service

- Cisco CCMService Web
                                             					 Service

- Cisco Common User
                                             					 Interface

- Cisco Trace Collection
                                             					 Service

IM and
                                          				  Presence Services:

- Cisco CCMService Web
                                             					 Service

- Cisco Trace Collection
                                             					 Service

Choosing the Cisco CCMRealm Web Service option activates trace
                                          				  for login authentication.

Choosing the Cisco Common User Interface option activates trace
                                          				  for the common code that multiple applications use; for example, Cisco Unified
                                          				  Operating System Administration and Cisco Unified
                                             					 Serviceability .

Choosing the Cisco CCMService Web Service option activates trace
                                          				  for the Cisco Unified
                                             					 Serviceability web application (GUI).

You enable all trace for each option/service, instead of running
                                          				  trace for specific components.

SOAP Services

- CiscoSOAP Web Service

- CiscoSOAPMessage Service

Choosing the Cisco SOAP Web Service option activates the trace
                                          				  for the AXL Serviceability API.

You enable all trace for this service, instead of running trace
                                          				  for specific components.

Platform Services

Cisco Unified OS Admin Web Service

The Cisco Unified OS Admin Web Service supports Cisco Unified
                                          				  Operating System Administration, which is the web application that provides
                                          				  management of platform-related functionality such as certificate management,
                                          				  version settings, and installations and upgrades.

You enable all trace for this service, instead of running trace
                                          				  for specific components.

### Debug Trace Level Settings

The following table describes the debug trace level settings for services.

Level

Description

Error

Traces alarm conditions and events. Used for all traces that are generated in abnormal path. Uses minimum number of CPU cycles.

Special

Traces all Error conditions plus process and device initialization messages.

State Transition

Traces all Special conditions plus subsystem state transitions that occur during normal operation. Traces call-processing
                                             events.

Significant

Traces all State Transition conditions plus media layer events that occur during normal operation.

Entry/Exit

Not all services use this trace level.

Traces all Significant conditions plus entry and exit points of routines.

Arbitrary

Traces all Entry/Exit conditions plus low-level debugging information.

Detailed

Traces all Arbitrary conditions plus detailed debugging information.

The following table describes the debug trace level settings for servlets.

Level

Description

Fatal

Traces very severe error events that may cause the application to abort.

Error

Traces alarm conditions and events. Used for all traces that are generated in abnormal path.

Warn

Traces potentially harmful situations.

Info

Traces the majority of servlet problems and has a minimal effect on system performance.

Debug

Traces all State Transition conditions plus media layer events that occur during normal operation.

Trace level that turns on all logging.

To avoid memory issues, we recommend you NOT to enable Debug Logging for the Cisco XCP Router service. If the load of the
                                                         system allows then in some cases you can turn it ON for very short period of time based on the memory capacity.

### Trace Field Descriptions

For some services, you can activate trace for specific components, instead of enabling all trace for the service. The following
                              list includes the services for which you can activate trace for specific components. Clicking one of the cross-references
                              takes you to the applicable section where a description displays for each trace field for the service. If a service does not
                              exist in the following list, the Enable All Trace check box displays for the service in the Trace Configuration window.

The following services are applicable to Unified Communications Manager and Cisco Unity Connection :

Database layer monitor trace fields

Cisco RIS data collector trace fields

The following services are applicable to Unified Communications Manager:

Cisco CallManager SDI trace fields

- Cisco CallManager SDL trace fields

Cisco CTIManager SDL trace fields

Cisco Extended Functions trace fields

Cisco Extension Mobility trace fields

Cisco IP manager assistant trace fields

Cisco IP voice media streaming app trace fields

Cisco TFTP trace fields

Cisco Web Dialer web service trace fields

#### Database Layer Monitor Trace Fields

The following table describes the Cisco Database Layer Monitor trace fields. The Cisco Database Layer Monitor service supports
                                    Unified Communications Manager and Cisco Unity Connection .

Field Name

Description

Enable DB Library Trace

Activates database library trace for C++ applications.

Enable Service Trace

Activates service trace.

Enable DB Change Notification Trace

Activates the database change notification traces for C++ applications.

Enable Unit Test Trace

Do not check this check box. Cisco engineering uses it for debugging purposes.

#### Cisco RIS Data Collector Trace Fields

The following table describes the Cisco RIS Data Collector trace fields. The Cisco RIS Data Collector service supports Unified
                                    Communications Manager and Cisco Unity Connection .

Field Name

Description

Enable RISDC Trace

Activates trace for the RISDC thread of the RIS data collector service (RIS).

Enable System Access Trace

Activates trace for the system access library in the RIS data collector.

Enable Link Services Trace

Activates trace for the link services library in the RIS data collector.

Enable RISDC Access Trace

Activates trace for the RISDC access library in the RIS data collector.

Enable RISDB Trace

Activates trace for the RISDB library in the RIS data collector.

Enable PI Trace

Activates trace for the PI library in the RIS data collector.

Enable XML Trace

Activates trace for the input/output XML messages of the RIS data collector service.

Enable Perfmon Logger Trace

Activates trace for the troubleshooting perfmon data logging in the RIS data collector. Used to trace the name of the log
                                                file, the total number of counters that are logged, the names of the application and system counters and instances, calculation
                                                of process and thread CPU percentage, and occurrences of log file rollover and deletion.

#### Cisco CallManager SDI Trace Fields

The following table describes the Cisco CallManager SDI trace fields. The Cisco CallManager service supports Unified Communications
                                    Manager.

Field Name

Description

Enable H245 Message Trace

Activates trace of H245 messages.

Enable DT-24+/DE-30+ Trace

Activates the logging of ISDN type of DT-24+/DE-30+
                                                					 device traces.

Enable PRI Trace

Activates trace of primary rate interface (PRI)
                                                					 devices.

Enable ISDN Translation Trace

Activates ISDN message traces. Used for normal
                                                					 debugging.

Enable H225 & Gatekeeper Trace

Activates trace of H.225 devices. Used for normal
                                                					 debugging.

Enable Miscellaneous Trace

Activates trace of miscellaneous devices.

Do not check this check box during normal system operation.

Enable Conference Bridge Trace

Activates trace of conference bridges. Used for
                                                					 normal debugging.

Enable Music on Hold Trace

Activates trace of music on hold (MOH) devices. Used to trace MOH device status such as registered with Unified Communications
                                                Manager, unregistered with Unified Communications Manager, and resource allocation processed successfully or failed.

Enable Unified CM Real-Time Information Server Trace

Activates Unified Communications Manager real-time information traces that the real-time information server uses.

Enable SIP Stack Trace

Activates trace of SIP stack.
                                                				  The default is enabled.

Enable Annunciator Trace

Activates trace for the annunciator, a SCCP device that uses the Cisco IP Voice Media Streaming Application service to enable
                                                Unified Communications Manager to play prerecorded announcements (.wav files) and tones to Cisco Unified IP Phones, gateways,
                                                and other configurable devices.

Enable CDR Trace

Activates traces for CDR.

Enable Analog Trunk Trace

Activates trace of all analog trunk (AT) gateways.

Enable All Phone Device Trace

Activates trace of phone devices. Trace information
                                                					 includes SoftPhone devices. Used for normal debugging.

Enable MTP Trace

Activates trace of media termination point (MTP)
                                                					 devices. Used for normal debugging.

Enable All Gateway Trace

Activates trace of all analog and digital gateways.

Enable Forward and Miscellaneous Trace

Activates trace for call forwarding and all
                                                					 subsystems that are not covered by another check box. Used for normal
                                                					 debugging.

Enable MGCP Trace

Activates trace for media gateway control protocol
                                                					 (MGCP) devices. Used for normal debugging.

Enable Media Resource Manager Trace

Activates trace for media resource manager (MRM)
                                                					 activities.

Enable SIP Call Processing Trace

Activates trace for SIP call processing.

Enable SCCP Keep Alive Trace

Activates trace for SCCP keepalive trace information
                                                					 in the Cisco CallManager traces. Because each SCCP device reports keepalive
                                                					 messages every 30 seconds, and each keepalive message creates 3 lines of trace
                                                					 data, the system generates a large amount of trace data when this check box is
                                                					 checked.

Enable SIP Keep Alive (REGISTER Refresh) Trace

Activates trace for SIP keepalive (REGISTER refresh)
                                                					 trace information in the Cisco CallManager traces. Because each SIP device
                                                					 reports keepalive messages every 2 minutes, and each keepalive message can
                                                					 create multiple lines of trace data, the system generates a large amount of
                                                					 trace data when this check box is checked.

#### Cisco CallManager SDL Trace Fields

The following table describes the Cisco CallManager SDL trace filter settings. The Cisco CallManager service supports Unified
                                    Communications Manager.

Cisco recommends that you use the defaults unless a Cisco engineer instructs you to do otherwise.

Setting Name

Description

Enable all Layer 1 traces.

Activates traces for Layer 1.

Enable detailed Layer 1 traces.

Activates detailed Layer 1 traces.

Enable all Layer 2 traces.

Activates traces for Layer 2.

Enable Layer 2 interface trace.

Activates Layer 2 interface traces.

Enable Layer 2 TCP trace.

Activates Layer 2 Transmission Control Program (TCP) traces.

Enable detailed dump Layer 2 trace.

Activates detailed traces for dump Layer 2.

Enable all Layer 3 traces.

Activates traces for Layer 3.

Enable all call control traces.

Activates traces for call control.

Enable miscellaneous polls trace.

Activates traces for miscellaneous polls.

Enable miscellaneous trace (database signals).

Activates miscellaneous traces such as database signals.

Enable message translation signals trace.

Activates traces for message translation signals.

Enable UUIE output trace.

Activates traces for user-to-user informational element (UUIE) output.

Enable gateway signals trace.

Activates traces for gateway signals.

Enable CTI trace.

Activates CTI trace.

Enable network service data trace

Activates network service data trace.

Enable network service event trace

Activates network service event trace.

Enable ICCP admin trace

Activates ICCP administration trace.

Enable default trace

Activates default trace.

The following table describes the Cisco CallManager SDL configuration characteristics.

Characteristics

Description

Enable SDL link states trace.

Activates trace for intracluster communication protocol (ICCP) link state.

Enable low-level SDL trace.

Activates trace for low-level SDL.

Enable SDL link poll trace.

Activates trace for ICCP link poll.

Enable SDL link messages trace.

Activates trace for ICCP raw messages.

Enable signal data dump trace.

Activates traces for signal data dump.

Enable correlation tag mapping trace.

Activates traces for correlation tag mapping.

Enable SDL process states trace.

Activates traces for SDL process states.

Disable pretty print of SDL trace.

Disables trace for pretty print of SDL. Pretty print adds tabs and spaces in a trace file without performing post processing.

Enable SDL TCP event trace.

Activates SDL TCP event trace.

#### Cisco CTIManager SDL Trace Fields

The following table describes the Cisco CTIManager SDL configuration trace filter settings. The Cisco CTIManager service supports
                                    Unified Communications Manager.

Tip

Cisco recommends that you use the defaults unless a Cisco engineer instructs you to do otherwise.

Tip

When you choose the CTIManager service from the Service Groups drop-down list box, the Trace Configuration window displays
                                                for SDI traces for this service. To activate SDI trace for the Cisco CTI Manager service, check the Enable All Trace check box in the Trace Configuration window for the Cisco CTIManager service. To access the SDL Configuration window, choose SDL Configuration from the Related Links drop-down list box; the settings that are described in Cisco CTIManager SDL Configuration Trace Filter
                                                Settings table and Cisco CTIManager SDL Configuration Trace Characteristics table display.

Setting Name

Description

Enable miscellaneous polls trace.

Activates traces for miscellaneous polls.

Enable miscellaneous trace (database signals).

Activates miscellaneous traces such as database signals.

Enable CTI trace.

Activates CTI trace.

Enable Network Service Data Trace

Activates network service data trace.

Enable Network Service Event Trace

Activates network service event trace.

Enable ICCP Admin Trace

Activates ICCP administration trace.

Enable Default Trace

Activates default trace.

The following table describes the Cisco CTIManager SDL configuration trace characteristics.

Characteristics

Description

Enable SDL link states trace.

Activates trace for ICCP link state.

Enable low-level SDL trace.

Activates trace for low-level SDL.

Enable SDL link poll trace.

Activates trace for ICCP link poll.

Enable SDL link messages trace.

Activates trace for ICCP raw messages.

Enable signal data dump trace.

Activates traces for signal data dump.

Enable correlation tag mapping trace.

Activates traces for correlation tag mapping.

Enable SDL process states trace.

Activates traces for SDL process states.

Disable pretty print of SDL trace.

Disables trace for pretty print of SDL. Pretty print adds tabs and spaces in a trace file without performing post processing.

Enable SDL TCP Event trace

Activates SDL TCP event trace.

#### Cisco Extended Functions Trace Fields

The following table describes the Cisco Extended Functions trace fields. The Cisco Extended Functions service supports Unified
                                    Communications Manager.

Field Name

Description

Enable QBE Helper TSP Trace

Activates telephony service provider trace.

Enable QBE Helper TSPI Trace

Activates QBE helper TSP interface trace.

Enable QRT Dictionary Trace

Activates quality report tool service dictionary trace.

Enable DOM Helper Traces

Activates DOM helper trace.

Enable Redundancy and Change Notification Trace

Activates database change notification trace.

Enable QRT Report Handler Trace

Activates quality report tool report handler trace.

Enable QBE Helper CTI Trace

Activates QBE helper CTI trace.

Enable QRT Service Trace

Activates quality report tool service related trace.

Enable QRT DB Traces

Activates QRT DB access trace.

Enable Template Map Traces

Activates standard template map and multimap trace.

Enable QRT Event Handler Trace

Activates quality report tool event handler trace.

Enable QRT Real-Time Information Server Trace

Activates quality report tool real-time information server trace.

#### Cisco Extension Mobility Trace Fields

The following table describes the Cisco Extension Mobility trace fields. The Cisco Extension Mobility service supports Unified
                                    Communications Manager.

Field Name

Description

Enable EM Service Trace

Activates trace for the extension mobility service.

Tip

When you activate trace for the Cisco Extension Mobility Application service, you check the Enable All Trace check box in the Trace Configuration window for the Cisco Extension Mobility Application service.

#### Cisco IP Manager Assistant Trace Fields

The following table  describes the Cisco IP Manager Assistant trace fields. The Cisco IP Manager Assistant service supports Cisco Unified Communications Manager Assistant .

Field Name

Description

Enable IPMA Service Trace

Activates trace for the Cisco IP Manager Assistant service.

Enable IPMA Manager Configuration Change Log

Activates trace for the changes that you make to the manager and assistant configurations.

Enable IPMA CTI Trace

Activates trace for the CTI Manager connection.

Enable IPMA CTI Security Trace

Activates trace for the secure connection to CTIManager.

#### Cisco IP Voice Media Streaming App Trace Fields

The information in this section does not apply to Cisco Unity Connection .

The following table describes the Cisco IP Voice Media Streaming App trace fields. The Cisco IP Voice Media Streaming App
                                    service supports Unified Communications Manager.

Field Name

Description

Enable Service Initialization Trace

Activates trace for initialization information.

Enable MTP Device Trace

Activates traces to monitor the processed messages for media termination point (MTP).

Enable Device Recovery Trace

Activates traces for device-recovery-related information for MTP, conference bridge, and MOH.

Enable Skinny Station Messages Trace

Activates traces for skinny station protocol.

Enable WinSock Level 2 Trace

Activates trace for high-level, detailed WinSock-related information.

Enable Music On Hold Manager Trace

Activates trace to monitor MOH audio source manager.

Enable Annunciator Trace

Activates trace to monitor annunciator.

Enable DB Setup Manager Trace

Activates trace to monitor database setup and changes for MTP, conference bridge, and MOH.

Enable Conference Bridge Device Trace

Activates traces to monitor the processed messages for conference bridge.

Enable Device Driver Trace

Activates device driver traces.

Enable WinSock Level 1 Trace

Activates trace for low-level, general, WinSock-related information.

Enable Music on Hold Device Trace

Activates traces to monitor the processed messages for MOH.

Enable TFTP Downloads Trace

Activates trace to monitor the download of MOH audio source files.

#### Cisco TFTP Trace Fields

The following table describes the Cisco TFTP trace fields. The Cisco TFTP service supports Unified Communications Manager.

Field Name

Description

Enable Service System Trace

Activates trace for service system.

Enable Build File Trace

Activates trace for build files.

Enable Serve File Trace

Activates trace for serve files.

#### Cisco Web Dialer Web Service Trace Fields

The following table describes the Cisco Web Dialer Web Service trace fields. The Cisco Web Dialer Web Service supports Unified
                                    Communications Manager.

Field Name

Description

Enable Web Dialer Servlet Trace

Activates trace for Cisco Web Dialer servlet.

Enable Redirector Servlet Trace

Activates trace for the Redirector servlet.

### IM and Presence SIP Proxy Service Trace Filter Settings

The following table below describes the service trace filter settings for the IM and Presence SIP Proxy.

Enable Access Log Trace

This parameter enables the proxy access log trace; the first line of each SIP message received by the proxy is logged.

Enable Authentication Trace

This parameter enables tracing for the Authentication module.

Enable CALENDAR Trace

This parameter enables tracing for the Calendar module.

Enable CTI Gateway Trace

This parameter enables tracing for the CTI Gateway.

Enable Enum Trace

This parameter enables tracing for the Enum module.

Enable Method/Event Routing Trace

This parameter enables tracing for the Method/Event routing module.

Enable Number Expansion Trace

This parameter enables tracing for the Number Expansion module.

Enable Parser Trace

This parameter enables tracing of parser information related to the operation of the per-sipd child SIP parser.

Enable Privacy Trace

This parameter enables tracing for information about processing of PAI, RPID, and Diversion headers in relation to privacy
                                             requests.

Enable Registry Trace

This parameter enables tracing for the Registry module.

Enable Routing Trace

This parameter enables tracing for the Routing module.

Enable SIPUA Trace

This parameter enables tracing for the SIP UA application module.

Enable Server Trace

This parameter enables tracing for the Server.

Enable SIP Message and State Machine Trace

This parameter enables tracing for information related to the operation of the per-sipd SIP state machine.

Enable SIP TCP Trace

This parameter enables tracing for information related to the TCP transport of SIP messages by TCP services.

Enable SIP TLS Trace

This parameter enables tracing for information related to the TLS transport of SIP messages by TCP services.

Enable SIP XMPP IM Gateway Trace

This parameter enables trace for the SIP XMPP IM Gateway.

Enable Presence Web Service Trace

This parameter enables tracing for the Presence Web Service.

### IM and Presence Trace Field Descriptions

The following tables provide field descriptions for the services that support trace activation of specific components. For
                                 some services, you can activate trace for specific component instead of enabling all trace for the service. If a service is
                                 not included in this chapter, Enable All Trace displays for the service in the Trace Configuration window.

#### Cisco Access Log Trace Fields

The following table describes the Cisco Access Log trace fields.

Field Name

Description

Enable Access Log Trace

Turns on Access Log trace.

#### Cisco Authentication Trace Fields

The following table describes the Cisco Authentication trace fields.

Field Name

Description

Enable Authentication Trace

Turns on authentication trace.

#### Cisco Calendar Trace Fields

The following table describes the Cisco Calendar trace fields.

Field Name

Description

Enable Calendar Trace

Turns on Calendar trace.

#### Cisco CTI Gateway Trace Fields

The following table describes the Cisco CTI Gateway trace fields.

Field Name

Description

Enable CTI Gateway Trace

Turns on CTI Gateway trace.

#### Cisco Database Layer Monitor Trace Fields

The following table describes the Cisco Database Layer Monitor trace fields.

Field Name

Description

Enable DB Library Trace

Turns on database library trace for C++ applications.

Enable Service Trace

Turns on service trace.

Enable DB Change Notification Trace

Activates the database change notification traces for C++ applications.

Enable Unit Test Trace

Do not check. Cisco engineering uses it for debugging purposes.

#### Cisco Enum Trace Fields

The following table describes the Cisco Enum trace fields.

Field Name

Description

Enable Enum Trace

Turns on Enum trace.

#### Cisco Method/Event Trace Fields

The following table describes the Cisco Method/Event trace fields.

Field Name

Description

Enable Method/Event Trace

Turns on Method/Event trace.

#### Cisco Number Expansion Trace Fields

The following table describes the Cisco Number Expansion trace fields.

Field Name

Description

Enable Number Expansion Trace

Activates number expansion trace.

#### Cisco Parser Trace Fields

The following table describes the Cisco Parser trace fields.

Field Name

Description

Enable Parser Trace

Activates parser trace.

#### Cisco Privacy Trace Fields

The following table describes the Cisco Privacy trace fields.

Field Name

Description

Enable Privacy Trace

Activates Privacy trace.

#### Cisco Proxy Trace Fields

The following table describes the Cisco proxy trace fields.

Field Name

Description

Add Proxy

Turns on Proxy trace.

#### Cisco RIS Data Collector Trace Fields

The following table describes the Cisco RIS Data Collector trace fields.

Field Name

Description

Enable RISDC Trace

Activates trace for the RISDC thread of the RIS data collector service (RIS).

Enable System Access Trace

Activates trace for the system access library in the RIS data collector.

Enable Link Services Trace

Activates trace for the link services library in the RIS data collector.

Enable RISDC Access Trace

Activates trace for the RISDC access library in the RIS data collector.

Enable RISDB Trace

Activates trace for the RISDB library in the RIS data collector.

Enable PI Trace

Activates trace for the PI library in the RIS data collector.

Enable XML Trace

Activates trace for the input/output XML messages of the RIS data collector service.

Enable Perfmon Logger Trace

Activates trace for the troubleshooting perfmon data logging in the RIS data collector. Used to trace the name of the log
                                                file, the total number of counters that are logged, the names of the application and system counters and instances, calculation
                                                of process and thread CPU percentage, and occurrences of log file rollover and deletion.

#### Cisco Registry Trace Fields

The following table describes the Cisco Registry trace fields.

Field Name

Description

Enable Registry Trace

Activates Registry trace.

#### Cisco Routing Trace Fields

The following table describes the Cisco Routing trace fields.

Field Name

Description

Enable Routing Trace

Activates Routing trace.

#### Cisco Server Trace Fields

The following table describes the Cisco Server trace fields.

Field Name

Description

Enable Server Trace

Activates Server trace.

#### Cisco SIP Message and State Machine Trace Fields

The following table describes the Cisco SIP Message and State Machine trace fields.

Field Name

Description

Enable SIP Message and State Machine Trace

Activates SIP Message and State Machine trace.

#### Cisco SIP TCP Trace Fields

The following table describes the Cisco SIP TCP trace fields.

Field Name

Description

Enable SIP TCP Trace

Activates SIP TCP trace.

#### Cisco SIP TLS Trace Fields

The following table describes the Cisco SIP TLS trace fields.

Field Name

Description

Enable SIP TLS Trace

Activates SIP TLS trace.

#### Cisco Web Service Trace Fields

The following table describes the Cisco Web Service trace fields.

Field Name

Description

Enable Presence Web Service Trace

Activates Presence Web Service trace.

### Trace Output Settings

The following table contains the trace log file descriptions.

Caution

When you change either the Maximum No. of Files or the Maximum File Size settings in the Trace Configuration window, the system
                                             deletes all service log files except for the current file, that is, if the service is running; if the service has not been
                                             activated, the system deletes the files immediately after you activate the service. Before you change the Maximum No. of Files
                                             setting or the Maximum File Size setting, download and save the service log files to another server if you want to keep a
                                             record of the log files; to perform this task, use Trace and Log Central in Unity RTMT.

Field

Description

Maximum number of files

This field specifies the total number of trace files for a given service.

Cisco Unified Serviceability automatically appends a sequence number to the filename to indicate which file it is, for example, cus299.txt. When the last
                                             file in the sequence is full, the trace data begins writing over the first file. The default varies by service.

Maximum file size (MB)

This field specifies the maximum size of the trace file in megabytes. The default varies by service.

### Trace Setting Troubleshooting

#### Troubleshoot Trace Settings Window

The Troubleshooting Trace Settings window allows you to select the services in the Serviceability GUI for which you want to set predetermined troubleshooting
                                    trace settings. In this window, you can select the services on different   nodes in the cluster. This populates the trace
                                    settings changes for all the services you choose. You can select specific active services for a single node, all active services
                                    for the node, specific active services for all nodes in the cluster, or all active services for all nodes in the cluster.
                                    In the window, N/A displays next to inactive services.

For IM and Presence the predetermined troubleshooting trace settings for an IM and Presence feature or network service include SDI and Log4j trace settings. Before the troubleshooting trace settings are applied, the
                                                system backs up the original trace settings. When you reset the troubleshooting trace settings, the original trace settings
                                                are restored.

When you open the Troubleshooting Trace Settings window after you apply troubleshooting trace settings to a service, the service that you set for troubleshooting displays
                                    as checked. In the Troubleshooting Trace Settings window, you can reset the trace settings to the original settings.

After you apply Troubleshooting Trace Setting to a service, the Trace Configuration window displays a message that troubleshooting trace is set for that service. From the Related Links list box, you can select the Troubleshooting Trace Settings option if you want to reset the settings for the service. For
                                    the given service, the Trace Configuration window displays all the settings as read-only, except for some parameters of trace output settings, for example, Maximum
                                    No. of Files.

#### Troubleshoot Trace Settings

##### Before you begin

Review the tasks Set up trace configuration and Set up trace parameters.

Step 1

Select Trace > Troubleshooting Trace Settings .

Step 2

Select the server where you want to troubleshoot trace settings from the Server list box.

Step 3

Select Go .

A list of services display. The services that are not active display as N/A.

Step 4

Perform one of the following actions:

To monitor specific services on the node that you selected from the Server list box, check the service in the Services pane.

For example, the Database and Admin Services, Performance and Monitoring Services, or the Backup and Restore Services pane
                                                      (and so on).

This task affects only the node that you selected from the Server list box.

To monitor all services on the node that you selected from the Server list box, check Check All Services .

Cisco Unified Communications Manager and IM and Presence clusters only: To monitor specific services on all nodes in a cluster,
                                                   check Check Selected Services on All Nodes .

This setting applies for all nodes in the cluster where the service is active.

Unified Communications Manager and IM and Presence clusters only: To monitor all services for all nodes in the cluster, check Check All Services on All Nodes .

Step 5

Select Save .

Step 6

Select one of the following buttons to restore the original trace settings:

Reset Troubleshooting Traces —Restores the original trace settings for the services on the node that you chose in the Server list box; also displays as
                                                   an icon that you can select.

Unified Communications Manager and IM and Presence clusters only: Reset Troubleshooting Traces On All Nodes —Restores the original trace settings for the services on all nodes in the cluster.

The Reset Troubleshooting Traces button displays only if you have set troubleshooting trace for one or more services.

Leaving troubleshooting trace enabled for a long time increases the size of the trace files and may affect the performance
                                                                  of the services.

After you select the Reset button, the window refreshes and the service check boxes display as unchecked.

| Note | Enabling Trace decreases system performance; therefore, enable Trace only for troubleshooting purposes. For assistance in
                                          using Trace, contact Cisco Technical Assistance Center (TAC). |
|---|---|

| Note | The predetermined troubleshooting trace settings for a  feature or network service include SDL, SDI, and Log4j trace settings.
                                          Before the troubleshooting trace settings are applied, the system backs up the original trace settings. When you reset the
                                          troubleshooting trace settings, the original trace settings are restored. |
|---|---|

| Tip | Do not use Windows NotePad to view collected trace files to view collected trace files, because Windows NotePad does not properly
                                          display line
                                          breaks. |
|---|---|

| Note | Unified Communications Manager only: For devices that support encryption, the Secure Real-time Transport Protocol (SRTP) keying
                                          material does not display in the trace file. |
|---|---|

| Step 1 | Configure the values of the TLC Throttling CPU Goal and TLC
                                          			 Throttling IOWait Goal service parameters (Cisco RIS Data Collector service) by performing one of these steps: Cisco Unified Communications Manager Administration and Cisco Unified IM and Presence : Select System > ServiceParameters and configure the values of the TLC Throttling CPU Goal and TLC Throttling IOWait Goal service parameters (Cisco RIS Data
                                                Collector service). Cisco Unity Connection only: Select System
                                                      						Settings > Service Parameters in Cisco Unity Connection Administration and configure the values of the TLC
                                                				  Throttling CPU Goal and TLC Throttling IOWait Goal service parameters (Cisco
                                                				  RIS Data Collector service). |
|---|---|
| Step 2 | Configure the trace setting for the service for which you want to
                                          			 collect traces. If you have clusters, you can configure trace for the service on one server
                                          			 or on all servers in the cluster. To configure trace settings, choose what information you
                                             				want to include in the trace log by choosing the debug level and trace fields. If you want to run predetermined traces on services, set
                                             				troubleshooting trace for those services. |
| Step 3 | Install the Cisco Unified Real-Time Monitoring Tool on a local PC. |
| Step 4 | If you want to generate an alarm when the specified search string
                                          			 exists in a monitored trace file, enable the LogFileSearchStringFound alert in Unified
                                          			 RTMT. You can find the LogFileSearchStringFound alarm in the
                                             				LpmTctCatalog. (Select Alarms > Definitions .
                                             				In the Find alarms where drop-down list box, choose the System Alarm Catalog ; in the Equals
                                             				drop-down list box, choose LpmTctCatalog ). |
| Step 5 | If you want to automatically capture traces for alerts such as
                                          			 CriticalServiceDownand CodeYellow, check the Enable Trace Download check box in the Set
                                          			 Alert/Properties dialog box for the specific alert in Unified RTMT; configure how often
                                          			 that you want the download to occur. |
| Step 6 | Collect the traces. |
| Step 7 | View the log file in the appropriate viewer. |
| Step 8 | If you enabled troubleshooting trace, reset the trace settings
                                          			 services, so the original settings are restored. Note Leaving troubleshooting trace enabled for a long time increases
                                                         				  the size of the trace files and may affect the performance of the services. | Note | Leaving troubleshooting trace enabled for a long time increases
                                                         				  the size of the trace files and may affect the performance of the services. |
| Note | Leaving troubleshooting trace enabled for a long time increases
                                                         				  the size of the trace files and may affect the performance of the services. |

| Note | Leaving troubleshooting trace enabled for a long time increases
                                                         				  the size of the trace files and may affect the performance of the services. |
|---|---|

| Note | Enabling trace decreases system performance; therefore, enable trace
                                       		  only for troubleshooting purposes. For assistance in using trace, contact your
                                       		  technical support team. |
|---|---|

| Tip | For Cisco Unity Connection , you may need to run trace in Cisco Unified Serviceability and Cisco Unity Connection Serviceability to troubleshoot Cisco Unity Connection issues. For
                                             			 information on how to run trace in Cisco Unity Connection Serviceability , refer to the Cisco Unity Connection Serviceability Administration Guide . |
|---|---|

| Step 1 | Select Trace > Configuration . The Trace Configuration window displays. |
|---|---|
| Step 2 | From the Server drop-down list box, select the server that is
                                          			 running the service for which you want to configure trace; then, click Go . |
| Step 3 | From the Service Group drop-down list box, select the service
                                          			 group for the service that you want to configure trace; then, click Go . Tip The Service Groups in Trace Configuration table
                                                         				  lists the services and trace libraries that correspond to the options that
                                                         				  display in the Service Group drop-down list box. | Tip | The Service Groups in Trace Configuration table
                                                         				  lists the services and trace libraries that correspond to the options that
                                                         				  display in the Service Group drop-down list box. |
| Tip | The Service Groups in Trace Configuration table
                                                         				  lists the services and trace libraries that correspond to the options that
                                                         				  display in the Service Group drop-down list box. |
| Step 4 | From the Service drop-down list box, select the service for which
                                          			 you want to configure trace and, click Go . The drop-down list box displays active and inactive services. Tip Cisco Unity Connection only: For the Cisco CallManager and
                                                         				  CTIManager services, you can configure SDL trace parameters. To do so, open the
                                                         				  Trace Configuration window for one of those services, and click the Go button that is next to the Related
                                                         				  Links drop-down list box. If you configured Troubleshooting Trace for the service, a message
                                             				displays at the top of the window that indicates that the Troubleshooting
                                             				Traces feature is set, which means that the system disables all fields in the
                                             				Trace Configuration window except for Trace Output Settings. To configure the
                                             				Trace Output Settings, go to 
                                             				Step 11.
                                             				To reset Troubleshooting Trace, see the 
                                             				Set up troubleshooting trace settings. The trace parameters display for the service that you chose. In addition, the Apply to All Nodes check box displays (Unified
                                             Communications Manager only). | Tip | Cisco Unity Connection only: For the Cisco CallManager and
                                                         				  CTIManager services, you can configure SDL trace parameters. To do so, open the
                                                         				  Trace Configuration window for one of those services, and click the Go button that is next to the Related
                                                         				  Links drop-down list box. |
| Tip | Cisco Unity Connection only: For the Cisco CallManager and
                                                         				  CTIManager services, you can configure SDL trace parameters. To do so, open the
                                                         				  Trace Configuration window for one of those services, and click the Go button that is next to the Related
                                                         				  Links drop-down list box. |
| Step 5 | Unified Communications Manager and IM and Presence only: If you want to do so, you can apply the trace
                                          			 settings for the service or trace library to all servers in the cluster by
                                          			 checking the Apply to All Nodes check box; that is, if your
                                          			 configuration supports clusters. |
| Step 6 | Check the Trace On check box. |
| Step 7 | Cisco Unity Connection only: If you are configuring SDL
                                          			 trace parameters, go to 
                                          			 Step 10. |
| Step 8 | Select the level of information that you want traced from the Debug Trace Level list box, as described in 
                                          			 Debug trace level settings. |
| Step 9 | Check the Trace Fields check box for the service that you chose,
                                          			 for example, Cisco Log Partition Monitoring Tool Trace Fields. |
| Step 10 | If the service does not have multiple trace settings where you can
                                          			 specify the traces that you want to activate, check the Enable All Trace check box. If the service
                                          			 that you chose has multiple trace settings, check the check boxes next to the
                                          			 trace check boxes that you want to enable, as described in 
                                          			 Trace field descriptions. |
| Step 11 | To limit the number and size of the trace files, specify the trace
                                          			 output setting. See 
                                          			 Trace Ouput Settings
                                          			 for descriptions. |
| Step 12 | To save your trace parameters configuration, click the Save button. The changes to trace configuration take effect immediately for all services except Cisco Messaging Interface (Unified Communications
                                             Manager only). The trace configuration changes for Cisco Messaging Interface take effect in 3 to 5 minutes. Note To set the default, click the Set Default button. | Note | To set the default, click the Set Default button. |
| Note | To set the default, click the Set Default button. |

| Tip | The Service Groups in Trace Configuration table
                                                         				  lists the services and trace libraries that correspond to the options that
                                                         				  display in the Service Group drop-down list box. |
|---|---|

| Tip | Cisco Unity Connection only: For the Cisco CallManager and
                                                         				  CTIManager services, you can configure SDL trace parameters. To do so, open the
                                                         				  Trace Configuration window for one of those services, and click the Go button that is next to the Related
                                                         				  Links drop-down list box. |
|---|---|

| Note | To set the default, click the Set Default button. |
|---|---|

| Service Group | Services and Trace Libraries | Notes |
|---|---|---|
| Unified Communications Manager CM
                                          				  Services | Cisco CTIManager Cisco CallManager Cisco CallManager Cisco IP
                                             					 Phone Service Cisco DHCP Monitor Service Cisco Dialed Number
                                             					 Analyzer Cisco Dialed Number
                                             					 Analyzer Server Cisco Extended Functions,
                                             					 Cisco Extension Mobility Cisco Extension Mobility
                                             					 Application Cisco IP Voice Media
                                             					 Streaming App Cisco Messaging Interface Cisco TFTP Cisco Unified Mobile Voice
                                             					 Access Service | For
                                          				  most services in the CM Services group, you run trace for specific components,
                                          				  instead of enabling all trace for the service. The Trace field descriptions
                                          				  lists the services for which you can run trace for specific components. |
| Unified Communications Manager CTI
                                          				  Services | Cisco IP Manager Assistant Cisco Web Dialer Web
                                             					 Service | For
                                          				  these services, you can run trace for specific components, instead of enabling
                                          				  all trace for the service; see the Trace field descriptions. |
| Unified Communications Manager CDR
                                          				  Services | Cisco Unified Communications Manager CDR Analysis and Reporting Scheduler Cisco Unified Communications Manager CDR Analysis and Reporting Web Service Cisco CDR Agent Cisco CDR Repository
                                             					 Manager | You
                                          				  enable all trace for each service, instead of running trace for specific
                                          				  components. In Cisco Unified Communications Manager CDR Analysis and Reporting, when reports are run that call stored procedures, Cisco
                                          Unified Communications Manager CDR Analysis and Reporting checks the configured debug trace level for the Cisco Unified Communications
                                          Manager CDR Analysis and Reporting Scheduler service and the Cisco Unified Communications Manager CDR Analysis and Reporting
                                          Web Service in the Trace Configuration window before stored procedure logging begins. For pregenerated reports, Cisco Unified
                                          Communications Manager CDR Analysis and Reporting checks the level for the Cisco Unified Communications Manager CDR Analysis
                                          and Reporting Scheduler service; for on-demand reports, Cisco Unified Communications Manager CDR Analysis and Reporting checks
                                          the level for the Cisco Unified Communications Manager CDR Analysis and Reporting Web Service. If you choose Debug from the
                                          Debug Trace Level drop-down list box, stored procedure logging gets enabled and continues until you choose another option
                                          from the drop-down list box. The following Cisco Unified Communications Manager CDR Analysis and Reporting reports use stored
                                          procedure logging: Gateway Utilization report, Route and Line Group Utilization report, Route/Hunt List Utilization report,
                                          Route Pattern/Hunt Pilot Utilization report, Conference Call Details report, Conference Call Summary report, Conference Bridge
                                          Utilization report, Voice Messaging Utilization report, and the CDR Search report. |
| IM and Presence Services | Cisco Client Profile Agent Cisco Config Agent Cisco Intercluster Sync
                                             					 Agent Cisco Login Datastore Cisco OAM Agent Cisco Presence Datastore Cisco Presence Engine Cisco IM and Presence Data Monitor Cisco Route Datastore Cisco SIP Proxy Cisco SIP Registration
                                             					 Datastore Cisco Server Recovery
                                             					 Manager Cisco Sync Agent Cisco XCP Authentication
                                             					 Service Cisco XCP Config Manager Cisco XCP Connection
                                             					 Manager Cisco XCP Directory Service Cisco XCP Message Archiver Cisco XCP Router Cisco XCP SIP Federation
                                             					 Connection Manager Cisco XCP Text Conference
                                             					 Manager Cisco XCP Web Connection
                                             					 Manager Cisco XCP XMPP Federation
                                             					 Connection Manager | See topics
                                          				  related to feature and network services in Cisco Unified IM and Presence Serviceability for a
                                          				  description of these services. For these services, you
                                             					 should enable all trace for the service, instead of running trace for specific
                                             					 components. |
| Database and Admin Services | Unified Communications Manager and Cisco Unity Connection: Cisco AXL Web Service Cisco CCM DBL Web Library Cisco CCMAdmin Web Service Cisco CCMUser Web Service Cisco Database Layer
                                             					 Monitor Cisco UXL Web Service Unified Communications Manager Cisco Bulk Provisioning
                                             					 Service Cisco GRT Communications
                                             					 Web Service Cisco Role-based Security Cisco TAPS Service Cisco Unified Reporting Web
                                             					 Service IM and
                                          				  Presence Services: Cisco AXL Web Service Cisco Bulk Provisioning
                                             					 Service Cisco CCMUser Web Service Cisco Database Layer
                                             					 Monitor Cisco GRT Communications
                                             					 Web Service Cisco IM and Presence Admin Cisco Unified Reporting Web
                                             					 Service Platform Administrative
                                             					 Web Service | Choosing the Cisco CCM DBL Web Library option activates the
                                          				  trace for database access for Java applications. For database access for C++
                                          				  applications, activate trace for Cisco Database Layer Monitor, as described in
                                          				  the Cisco Extended Functions trace fields. Choosing the Cisco Role-based Security option, which supports Unified Communications Manager, activates trace for user-role
                                          authorization. For most services in the Database and Admin Services group, you
                                          				  enable all trace for the service/library, instead of enabling trace for
                                          				  specific components. For Cisco Database Layer Monitor, you can run trace for
                                          				  specific components. Note You can control logging for services in the Cisco Unified IM and Presence Serviceability UI. To change the log level, select the System Services group and Cisco CCMService Web Service. | Note | You can control logging for services in the Cisco Unified IM and Presence Serviceability UI. To change the log level, select the System Services group and Cisco CCMService Web Service. |
| Note | You can control logging for services in the Cisco Unified IM and Presence Serviceability UI. To change the log level, select the System Services group and Cisco CCMService Web Service. |
| Performance and Monitoring Services | Unified Communications Manager and Cisco Unity Connection: Cisco AMC Service Cisco CCM NCS Web Library CCM PD Web Service Cisco CallManager SNMP
                                             					 Service Cisco Log Partition
                                             					 Monitoring Tool Cisco RIS Data Collector Cisco RTMT Web Service Cisco Audit Event Service Cisco RisBean Library Unified Communications Manager: Cisco CCM PD Web Service IM and
                                          				  Presence Services: Cisco AMC Service Cisco Audit Event Service Cisco Log Partition
                                             					 Monitoring Tool Cisco RIS Data Collector Cisco RTMT Web Service Cisco RisBean Library | Choosing the Cisco CCM NCS Web Library option activates trace
                                          				  for database change notification for the Java client. Choosing the Cisco Unity RTMT Web Service option activates trace
                                          				  for the Unity RTMT servlets; running this trace creates the server-side log for
                                          				  Unity RTMT client queries. |
| Unified Communications Manager Security Services | Cisco CTL Provider Cisco Certificate
                                             					 Authority Proxy Function Cisco Trust Verification
                                             					 Service | You enable all trace for each service, instead of running trace
                                          				  for specific components. |
| Unified Communications Manager Directory Services | Cisco
                                          				  DirSync | You enable all trace for this service, instead of running trace
                                          				  for specific components. |
| Backup and Restore Services | Cisco DRF Local Unified Communications Manager and Cisco Unity Connection only: Cisco DRF Master | You enable all trace for each service, instead of running trace
                                          				  for specific components. |
| System Services | Unified Communications Manager: Cisco CCMRealm Web
                                             					 Service Cisco CCMService Web
                                             					 Service Cisco Common User
                                             					 Interface Cisco Trace Collection
                                             					 Service IM and
                                          				  Presence Services: Cisco CCMService Web
                                             					 Service Cisco Trace Collection
                                             					 Service | Choosing the Cisco CCMRealm Web Service option activates trace
                                          				  for login authentication. Choosing the Cisco Common User Interface option activates trace
                                          				  for the common code that multiple applications use; for example, Cisco Unified
                                          				  Operating System Administration and Cisco Unified
                                             					 Serviceability . Choosing the Cisco CCMService Web Service option activates trace
                                          				  for the Cisco Unified
                                             					 Serviceability web application (GUI). You enable all trace for each option/service, instead of running
                                          				  trace for specific components. |
| SOAP Services | CiscoSOAP Web Service CiscoSOAPMessage Service | Choosing the Cisco SOAP Web Service option activates the trace
                                          				  for the AXL Serviceability API. You enable all trace for this service, instead of running trace
                                          				  for specific components. |
| Platform Services | Cisco Unified OS Admin Web Service | The Cisco Unified OS Admin Web Service supports Cisco Unified
                                          				  Operating System Administration, which is the web application that provides
                                          				  management of platform-related functionality such as certificate management,
                                          				  version settings, and installations and upgrades. You enable all trace for this service, instead of running trace
                                          				  for specific components. |

| Note | You can control logging for services in the Cisco Unified IM and Presence Serviceability UI. To change the log level, select the System Services group and Cisco CCMService Web Service. |
|---|---|

| Level | Description |
|---|---|
| Error | Traces alarm conditions and events. Used for all traces that are generated in abnormal path. Uses minimum number of CPU cycles. |
| Special | Traces all Error conditions plus process and device initialization messages. |
| State Transition | Traces all Special conditions plus subsystem state transitions that occur during normal operation. Traces call-processing
                                             events. |
| Significant | Traces all State Transition conditions plus media layer events that occur during normal operation. |
| Entry/Exit | Note Not all services use this trace level. Traces all Significant conditions plus entry and exit points of routines. | Note | Not all services use this trace level. |
| Note | Not all services use this trace level. |
| Arbitrary | Traces all Entry/Exit conditions plus low-level debugging information. |
| Detailed | Traces all Arbitrary conditions plus detailed debugging information. |

| Note | Not all services use this trace level. |
|---|---|

| Level | Description |
|---|---|
| Fatal | Traces very severe error events that may cause the application to abort. |
| Error | Traces alarm conditions and events. Used for all traces that are generated in abnormal path. |
| Warn | Traces potentially harmful situations. |
| Info | Traces the majority of servlet problems and has a minimal effect on system performance. |
| Debug | Traces all State Transition conditions plus media layer events that occur during normal operation. Trace level that turns on all logging. Note To avoid memory issues, we recommend you NOT to enable Debug Logging for the Cisco XCP Router service. If the load of the
                                                         system allows then in some cases you can turn it ON for very short period of time based on the memory capacity. | Note | To avoid memory issues, we recommend you NOT to enable Debug Logging for the Cisco XCP Router service. If the load of the
                                                         system allows then in some cases you can turn it ON for very short period of time based on the memory capacity. |
| Note | To avoid memory issues, we recommend you NOT to enable Debug Logging for the Cisco XCP Router service. If the load of the
                                                         system allows then in some cases you can turn it ON for very short period of time based on the memory capacity. |

| Note | To avoid memory issues, we recommend you NOT to enable Debug Logging for the Cisco XCP Router service. If the load of the
                                                         system allows then in some cases you can turn it ON for very short period of time based on the memory capacity. |
|---|---|

| Field Name | Description |
|---|---|
| Enable DB Library Trace | Activates database library trace for C++ applications. |
| Enable Service Trace | Activates service trace. |
| Enable DB Change Notification Trace | Activates the database change notification traces for C++ applications. |
| Enable Unit Test Trace | Do not check this check box. Cisco engineering uses it for debugging purposes. |

| Field Name | Description |
|---|---|
| Enable RISDC Trace | Activates trace for the RISDC thread of the RIS data collector service (RIS). |
| Enable System Access Trace | Activates trace for the system access library in the RIS data collector. |
| Enable Link Services Trace | Activates trace for the link services library in the RIS data collector. |
| Enable RISDC Access Trace | Activates trace for the RISDC access library in the RIS data collector. |
| Enable RISDB Trace | Activates trace for the RISDB library in the RIS data collector. |
| Enable PI Trace | Activates trace for the PI library in the RIS data collector. |
| Enable XML Trace | Activates trace for the input/output XML messages of the RIS data collector service. |
| Enable Perfmon Logger Trace | Activates trace for the troubleshooting perfmon data logging in the RIS data collector. Used to trace the name of the log
                                                file, the total number of counters that are logged, the names of the application and system counters and instances, calculation
                                                of process and thread CPU percentage, and occurrences of log file rollover and deletion. |

| Field Name | Description |
|---|---|
| Enable H245 Message Trace | Activates trace of H245 messages. |
| Enable DT-24+/DE-30+ Trace | Activates the logging of ISDN type of DT-24+/DE-30+
                                                					 device traces. |
| Enable PRI Trace | Activates trace of primary rate interface (PRI)
                                                					 devices. |
| Enable ISDN Translation Trace | Activates ISDN message traces. Used for normal
                                                					 debugging. |
| Enable H225 & Gatekeeper Trace | Activates trace of H.225 devices. Used for normal
                                                					 debugging. |
| Enable Miscellaneous Trace | Activates trace of miscellaneous devices. Note Do not check this check box during normal system operation. | Note | Do not check this check box during normal system operation. |
| Note | Do not check this check box during normal system operation. |
| Enable Conference Bridge Trace | Activates trace of conference bridges. Used for
                                                					 normal debugging. |
| Enable Music on Hold Trace | Activates trace of music on hold (MOH) devices. Used to trace MOH device status such as registered with Unified Communications
                                                Manager, unregistered with Unified Communications Manager, and resource allocation processed successfully or failed. |
| Enable Unified CM Real-Time Information Server Trace | Activates Unified Communications Manager real-time information traces that the real-time information server uses. |
| Enable SIP Stack Trace | Activates trace of SIP stack.
                                                				  The default is enabled. |
| Enable Annunciator Trace | Activates trace for the annunciator, a SCCP device that uses the Cisco IP Voice Media Streaming Application service to enable
                                                Unified Communications Manager to play prerecorded announcements (.wav files) and tones to Cisco Unified IP Phones, gateways,
                                                and other configurable devices. |
| Enable CDR Trace | Activates traces for CDR. |
| Enable Analog Trunk Trace | Activates trace of all analog trunk (AT) gateways. |
| Enable All Phone Device Trace | Activates trace of phone devices. Trace information
                                                					 includes SoftPhone devices. Used for normal debugging. |
| Enable MTP Trace | Activates trace of media termination point (MTP)
                                                					 devices. Used for normal debugging. |
| Enable All Gateway Trace | Activates trace of all analog and digital gateways. |
| Enable Forward and Miscellaneous Trace | Activates trace for call forwarding and all
                                                					 subsystems that are not covered by another check box. Used for normal
                                                					 debugging. |
| Enable MGCP Trace | Activates trace for media gateway control protocol
                                                					 (MGCP) devices. Used for normal debugging. |
| Enable Media Resource Manager Trace | Activates trace for media resource manager (MRM)
                                                					 activities. |
| Enable SIP Call Processing Trace | Activates trace for SIP call processing. |
| Enable SCCP Keep Alive Trace | Activates trace for SCCP keepalive trace information
                                                					 in the Cisco CallManager traces. Because each SCCP device reports keepalive
                                                					 messages every 30 seconds, and each keepalive message creates 3 lines of trace
                                                					 data, the system generates a large amount of trace data when this check box is
                                                					 checked. |
| Enable SIP Keep Alive (REGISTER Refresh) Trace | Activates trace for SIP keepalive (REGISTER refresh)
                                                					 trace information in the Cisco CallManager traces. Because each SIP device
                                                					 reports keepalive messages every 2 minutes, and each keepalive message can
                                                					 create multiple lines of trace data, the system generates a large amount of
                                                					 trace data when this check box is checked. |

| Note | Do not check this check box during normal system operation. |
|---|---|

| Note | Cisco recommends that you use the defaults unless a Cisco engineer instructs you to do otherwise. |
|---|---|

| Setting Name | Description |
|---|---|
| Enable all Layer 1 traces. | Activates traces for Layer 1. |
| Enable detailed Layer 1 traces. | Activates detailed Layer 1 traces. |
| Enable all Layer 2 traces. | Activates traces for Layer 2. |
| Enable Layer 2 interface trace. | Activates Layer 2 interface traces. |
| Enable Layer 2 TCP trace. | Activates Layer 2 Transmission Control Program (TCP) traces. |
| Enable detailed dump Layer 2 trace. | Activates detailed traces for dump Layer 2. |
| Enable all Layer 3 traces. | Activates traces for Layer 3. |
| Enable all call control traces. | Activates traces for call control. |
| Enable miscellaneous polls trace. | Activates traces for miscellaneous polls. |
| Enable miscellaneous trace (database signals). | Activates miscellaneous traces such as database signals. |
| Enable message translation signals trace. | Activates traces for message translation signals. |
| Enable UUIE output trace. | Activates traces for user-to-user informational element (UUIE) output. |
| Enable gateway signals trace. | Activates traces for gateway signals. |
| Enable CTI trace. | Activates CTI trace. |
| Enable network service data trace | Activates network service data trace. |
| Enable network service event trace | Activates network service event trace. |
| Enable ICCP admin trace | Activates ICCP administration trace. |
| Enable default trace | Activates default trace. |

| Characteristics | Description |
|---|---|
| Enable SDL link states trace. | Activates trace for intracluster communication protocol (ICCP) link state. |
| Enable low-level SDL trace. | Activates trace for low-level SDL. |
| Enable SDL link poll trace. | Activates trace for ICCP link poll. |
| Enable SDL link messages trace. | Activates trace for ICCP raw messages. |
| Enable signal data dump trace. | Activates traces for signal data dump. |
| Enable correlation tag mapping trace. | Activates traces for correlation tag mapping. |
| Enable SDL process states trace. | Activates traces for SDL process states. |
| Disable pretty print of SDL trace. | Disables trace for pretty print of SDL. Pretty print adds tabs and spaces in a trace file without performing post processing. |
| Enable SDL TCP event trace. | Activates SDL TCP event trace. |

| Tip | Cisco recommends that you use the defaults unless a Cisco engineer instructs you to do otherwise. |
|---|---|

| Tip | When you choose the CTIManager service from the Service Groups drop-down list box, the Trace Configuration window displays
                                                for SDI traces for this service. To activate SDI trace for the Cisco CTI Manager service, check the Enable All Trace check box in the Trace Configuration window for the Cisco CTIManager service. To access the SDL Configuration window, choose SDL Configuration from the Related Links drop-down list box; the settings that are described in Cisco CTIManager SDL Configuration Trace Filter
                                                Settings table and Cisco CTIManager SDL Configuration Trace Characteristics table display. |
|---|---|

| Setting Name | Description |
|---|---|
| Enable miscellaneous polls trace. | Activates traces for miscellaneous polls. |
| Enable miscellaneous trace (database signals). | Activates miscellaneous traces such as database signals. |
| Enable CTI trace. | Activates CTI trace. |
| Enable Network Service Data Trace | Activates network service data trace. |
| Enable Network Service Event Trace | Activates network service event trace. |
| Enable ICCP Admin Trace | Activates ICCP administration trace. |
| Enable Default Trace | Activates default trace. |

| Characteristics | Description |
|---|---|
| Enable SDL link states trace. | Activates trace for ICCP link state. |
| Enable low-level SDL trace. | Activates trace for low-level SDL. |
| Enable SDL link poll trace. | Activates trace for ICCP link poll. |
| Enable SDL link messages trace. | Activates trace for ICCP raw messages. |
| Enable signal data dump trace. | Activates traces for signal data dump. |
| Enable correlation tag mapping trace. | Activates traces for correlation tag mapping. |
| Enable SDL process states trace. | Activates traces for SDL process states. |
| Disable pretty print of SDL trace. | Disables trace for pretty print of SDL. Pretty print adds tabs and spaces in a trace file without performing post processing. |
| Enable SDL TCP Event trace | Activates SDL TCP event trace. |

| Field Name | Description |
|---|---|
| Enable QBE Helper TSP Trace | Activates telephony service provider trace. |
| Enable QBE Helper TSPI Trace | Activates QBE helper TSP interface trace. |
| Enable QRT Dictionary Trace | Activates quality report tool service dictionary trace. |
| Enable DOM Helper Traces | Activates DOM helper trace. |
| Enable Redundancy and Change Notification Trace | Activates database change notification trace. |
| Enable QRT Report Handler Trace | Activates quality report tool report handler trace. |
| Enable QBE Helper CTI Trace | Activates QBE helper CTI trace. |
| Enable QRT Service Trace | Activates quality report tool service related trace. |
| Enable QRT DB Traces | Activates QRT DB access trace. |
| Enable Template Map Traces | Activates standard template map and multimap trace. |
| Enable QRT Event Handler Trace | Activates quality report tool event handler trace. |
| Enable QRT Real-Time Information Server Trace | Activates quality report tool real-time information server trace. |

| Field Name | Description |
|---|---|
| Enable EM Service Trace | Activates trace for the extension mobility service. |

| Tip | When you activate trace for the Cisco Extension Mobility Application service, you check the Enable All Trace check box in the Trace Configuration window for the Cisco Extension Mobility Application service. |
|---|---|

| Field Name | Description |
|---|---|
| Enable IPMA Service Trace | Activates trace for the Cisco IP Manager Assistant service. |
| Enable IPMA Manager Configuration Change Log | Activates trace for the changes that you make to the manager and assistant configurations. |
| Enable IPMA CTI Trace | Activates trace for the CTI Manager connection. |
| Enable IPMA CTI Security Trace | Activates trace for the secure connection to CTIManager. |

| Field Name | Description |
|---|---|
| Enable Service Initialization Trace | Activates trace for initialization information. |
| Enable MTP Device Trace | Activates traces to monitor the processed messages for media termination point (MTP). |
| Enable Device Recovery Trace | Activates traces for device-recovery-related information for MTP, conference bridge, and MOH. |
| Enable Skinny Station Messages Trace | Activates traces for skinny station protocol. |
| Enable WinSock Level 2 Trace | Activates trace for high-level, detailed WinSock-related information. |
| Enable Music On Hold Manager Trace | Activates trace to monitor MOH audio source manager. |
| Enable Annunciator Trace | Activates trace to monitor annunciator. |
| Enable DB Setup Manager Trace | Activates trace to monitor database setup and changes for MTP, conference bridge, and MOH. |
| Enable Conference Bridge Device Trace | Activates traces to monitor the processed messages for conference bridge. |
| Enable Device Driver Trace | Activates device driver traces. |
| Enable WinSock Level 1 Trace | Activates trace for low-level, general, WinSock-related information. |
| Enable Music on Hold Device Trace | Activates traces to monitor the processed messages for MOH. |
| Enable TFTP Downloads Trace | Activates trace to monitor the download of MOH audio source files. |

| Field Name | Description |
|---|---|
| Enable Service System Trace | Activates trace for service system. |
| Enable Build File Trace | Activates trace for build files. |
| Enable Serve File Trace | Activates trace for serve files. |

| Field Name | Description |
|---|---|
| Enable Web Dialer Servlet Trace | Activates trace for Cisco Web Dialer servlet. |
| Enable Redirector Servlet Trace | Activates trace for the Redirector servlet. |

| Parameter | Description |
|---|---|
| Enable Access Log Trace | This parameter enables the proxy access log trace; the first line of each SIP message received by the proxy is logged. |
| Enable Authentication Trace | This parameter enables tracing for the Authentication module. |
| Enable CALENDAR Trace | This parameter enables tracing for the Calendar module. |
| Enable CTI Gateway Trace | This parameter enables tracing for the CTI Gateway. |
| Enable Enum Trace | This parameter enables tracing for the Enum module. |
| Enable Method/Event Routing Trace | This parameter enables tracing for the Method/Event routing module. |
| Enable Number Expansion Trace | This parameter enables tracing for the Number Expansion module. |
| Enable Parser Trace | This parameter enables tracing of parser information related to the operation of the per-sipd child SIP parser. |
| Enable Privacy Trace | This parameter enables tracing for information about processing of PAI, RPID, and Diversion headers in relation to privacy
                                             requests. |
| Enable Registry Trace | This parameter enables tracing for the Registry module. |
| Enable Routing Trace | This parameter enables tracing for the Routing module. |
| Enable SIPUA Trace | This parameter enables tracing for the SIP UA application module. |
| Enable Server Trace | This parameter enables tracing for the Server. |
| Enable SIP Message and State Machine Trace | This parameter enables tracing for information related to the operation of the per-sipd SIP state machine. |
| Enable SIP TCP Trace | This parameter enables tracing for information related to the TCP transport of SIP messages by TCP services. |
| Enable SIP TLS Trace | This parameter enables tracing for information related to the TLS transport of SIP messages by TCP services. |
| Enable SIP XMPP IM Gateway Trace | This parameter enables trace for the SIP XMPP IM Gateway. |
| Enable Presence Web Service Trace | This parameter enables tracing for the Presence Web Service. |

| Field Name | Description |
|---|---|
| Enable Access Log Trace | Turns on Access Log trace. |

| Field Name | Description |
|---|---|
| Enable Authentication Trace | Turns on authentication trace. |

| Field Name | Description |
|---|---|
| Enable Calendar Trace | Turns on Calendar trace. |

| Field Name | Description |
|---|---|
| Enable CTI Gateway Trace | Turns on CTI Gateway trace. |

| Field Name | Description |
|---|---|
| Enable DB Library Trace | Turns on database library trace for C++ applications. |
| Enable Service Trace | Turns on service trace. |
| Enable DB Change Notification Trace | Activates the database change notification traces for C++ applications. |
| Enable Unit Test Trace | Do not check. Cisco engineering uses it for debugging purposes. |

| Field Name | Description |
|---|---|
| Enable Enum Trace | Turns on Enum trace. |

| Field Name | Description |
|---|---|
| Enable Method/Event Trace | Turns on Method/Event trace. |

| Field Name | Description |
|---|---|
| Enable Number Expansion Trace | Activates number expansion trace. |

| Field Name | Description |
|---|---|
| Enable Parser Trace | Activates parser trace. |

| Field Name | Description |
|---|---|
| Enable Privacy Trace | Activates Privacy trace. |

| Field Name | Description |
|---|---|
| Add Proxy | Turns on Proxy trace. |

| Field Name | Description |
|---|---|
| Enable RISDC Trace | Activates trace for the RISDC thread of the RIS data collector service (RIS). |
| Enable System Access Trace | Activates trace for the system access library in the RIS data collector. |
| Enable Link Services Trace | Activates trace for the link services library in the RIS data collector. |
| Enable RISDC Access Trace | Activates trace for the RISDC access library in the RIS data collector. |
| Enable RISDB Trace | Activates trace for the RISDB library in the RIS data collector. |
| Enable PI Trace | Activates trace for the PI library in the RIS data collector. |
| Enable XML Trace | Activates trace for the input/output XML messages of the RIS data collector service. |
| Enable Perfmon Logger Trace | Activates trace for the troubleshooting perfmon data logging in the RIS data collector. Used to trace the name of the log
                                                file, the total number of counters that are logged, the names of the application and system counters and instances, calculation
                                                of process and thread CPU percentage, and occurrences of log file rollover and deletion. |

| Field Name | Description |
|---|---|
| Enable Registry Trace | Activates Registry trace. |

| Field Name | Description |
|---|---|
| Enable Routing Trace | Activates Routing trace. |

| Field Name | Description |
|---|---|
| Enable Server Trace | Activates Server trace. |

| Field Name | Description |
|---|---|
| Enable SIP Message and State Machine Trace | Activates SIP Message and State Machine trace. |

| Field Name | Description |
|---|---|
| Enable SIP TCP Trace | Activates SIP TCP trace. |

| Field Name | Description |
|---|---|
| Enable SIP TLS Trace | Activates SIP TLS trace. |

| Field Name | Description |
|---|---|
| Enable Presence Web Service Trace | Activates Presence Web Service trace. |

| Caution | When you change either the Maximum No. of Files or the Maximum File Size settings in the Trace Configuration window, the system
                                             deletes all service log files except for the current file, that is, if the service is running; if the service has not been
                                             activated, the system deletes the files immediately after you activate the service. Before you change the Maximum No. of Files
                                             setting or the Maximum File Size setting, download and save the service log files to another server if you want to keep a
                                             record of the log files; to perform this task, use Trace and Log Central in Unity RTMT. |
|---|---|

| Field | Description |
|---|---|
| Maximum number of files | This field specifies the total number of trace files for a given service. Cisco Unified Serviceability automatically appends a sequence number to the filename to indicate which file it is, for example, cus299.txt. When the last
                                             file in the sequence is full, the trace data begins writing over the first file. The default varies by service. |
| Maximum file size (MB) | This field specifies the maximum size of the trace file in megabytes. The default varies by service. |

| Note | For IM and Presence the predetermined troubleshooting trace settings for an IM and Presence feature or network service include SDI and Log4j trace settings. Before the troubleshooting trace settings are applied, the
                                                system backs up the original trace settings. When you reset the troubleshooting trace settings, the original trace settings
                                                are restored. |
|---|---|

| Step 1 | Select Trace > Troubleshooting Trace Settings . |
|---|---|
| Step 2 | Select the server where you want to troubleshoot trace settings from the Server list box. |
| Step 3 | Select Go . A list of services display. The services that are not active display as N/A. |
| Step 4 | Perform one of the following actions: To monitor specific services on the node that you selected from the Server list box, check the service in the Services pane. For example, the Database and Admin Services, Performance and Monitoring Services, or the Backup and Restore Services pane
                                                      (and so on). This task affects only the node that you selected from the Server list box. To monitor all services on the node that you selected from the Server list box, check Check All Services . Cisco Unified Communications Manager and IM and Presence clusters only: To monitor specific services on all nodes in a cluster,
                                                   check Check Selected Services on All Nodes . This setting applies for all nodes in the cluster where the service is active. Unified Communications Manager and IM and Presence clusters only: To monitor all services for all nodes in the cluster, check Check All Services on All Nodes . |
| Step 5 | Select Save . |
| Step 6 | Select one of the following buttons to restore the original trace settings: Reset Troubleshooting Traces —Restores the original trace settings for the services on the node that you chose in the Server list box; also displays as
                                                   an icon that you can select. Unified Communications Manager and IM and Presence clusters only: Reset Troubleshooting Traces On All Nodes —Restores the original trace settings for the services on all nodes in the cluster. The Reset Troubleshooting Traces button displays only if you have set troubleshooting trace for one or more services. Note Leaving troubleshooting trace enabled for a long time increases the size of the trace files and may affect the performance
                                                                  of the services. After you select the Reset button, the window refreshes and the service check boxes display as unchecked. | Note | Leaving troubleshooting trace enabled for a long time increases the size of the trace files and may affect the performance
                                                                  of the services. |
| Note | Leaving troubleshooting trace enabled for a long time increases the size of the trace files and may affect the performance
                                                                  of the services. |

| Note | Leaving troubleshooting trace enabled for a long time increases the size of the trace files and may affect the performance
                                                                  of the services. |
|---|---|