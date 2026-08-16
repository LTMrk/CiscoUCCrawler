---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-crs-express-12-5-maintain-and-operate-guide-uccx-80830e2369
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/crs/express_12_5/maintain_and_operate/guide/uccx_b_uccx-125admin-and-operations-guide/uccx_b_uccx-125admin-and-operations-guide_chapter_011000.html
retrieved_at: 2026-08-16T21:46:23.012370+00:00
---

Cisco Unified Contact Center Express Administration and Operations Guide, Release 12.5(1)

# Cisco Unified Contact Center Express Administration and Operations Guide, Release 12.5(1)

Updated: January 31, 2020

Chapter: Real-Time Monitoring

## Chapter: Real-Time Monitoring

# Real-Time Monitoring

The Cisco Unified Real-Time Monitoring Tool (RTMT), which runs
                           		  as a client-side application, uses HTTPS and TCP to monitor system performance.
                           		  Unified RTMT can connect directly to devices through HTTPS to troubleshoot system problems.

Unified RTMT allows you to perform the following tasks:

Monitor a set of predefined management objects that monitor the
                                 				health of the system.

Generate alerts in the form of email messages, for objects when
                                 				values go above or below user-configured thresholds.

Collect and view traces in default viewers that exist in
                                 				RTMT.

View syslog messages in SysLog Viewer.

Work with performance-monitoring counters.

Even when Unified RTMT is not running as an application on your desktop,
                                       			 tasks such as alarm and performance monitoring updates continue to take place
                                       			 on the server in the background.

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

#### Unified CCX Alerts

The
                                    		  following list contains preconfigured Unified CCX alerts:

Alert Name

Syslog Alarm Name

Description

DB CRA %
                                                						Space Used

DB CRA %
                                                						Space Used

The
                                                						percentage of used space in the Unified CCX database, db_cra. The database,
                                                						db_cra, contains the Unified CCX historical and configuration data.

DBReplicationStopped

DB_REPLICATION_STOPPED

Unified
                                                						CCX Database Replication has been removed. This typically happens when the
                                                						replication queues become full due to the inability to contact the other node.

HistoricalDataWrittenToFiles

UCCX_HISTORICAL_DATA_WRITTEN_TO_FILES

Historical data is not written to the Unified CCX database and
                                                						has been written to the file system. Please verify the state of the Unified CCX
                                                						database.

Intelligence Center CUIC_DATABASE_UNAVAILABLE

CUIC_DATABASE_UNAVAILABLE

This
                                                						alert occurs when the Intelligence Center CUIC_DATABASE_UNAVAILABLE event gets
                                                						generated. This indicates the system detected critical error with database.

Intelligence Center CUIC_DB_REPLICATION_FAILED

CUIC_DB_REPLICATION_FAILED

This
                                                						alert occurs when the Intelligence Center CUIC_DB_REPLICATION_FAILED event gets
                                                						generated. This indicates the Database replication failed.

Intelligence Center CUIC_REPORT_EXECUTION_FAILED

CUIC_REPORT_EXECUTION_FAILED

This
                                                						alert occurs when the Intelligence Center CUIC_DB_REPLICATION_FAILED event gets
                                                						generated. This indicates that the reporting server could not run a report.
                                                						This could be because the associated datasource is offline.

Intelligence Center CUIC_UNRECOVERABLE_ERROR

CUIC_UNRECOVERABLE_ERROR

This
                                                						alert occurs when the Intelligence Center CUIC_UNRECOVERABLE_ERROR event gets
                                                						generated. This indicates that the system has detected an internal error within
                                                						Reporting Server which may prevent it from functioning correctly. Restart may
                                                						be required.

CCXToCUICAdminSyncFailed

UCCX_TO_CUIC_SYNC_FAILED

This
                                                						alert occurs when the Unified CCX has failed to notify CUIC on any resource
                                                						change.

CCXToCUICCVDSyncFailed

UCCX_TO_CUIC_SYNC_FAILED

This
                                                						alert occurs when the Unified CCX has failed to notify CUIC on any resource
                                                						change.

CCXToCUICEngineSyncFailed

UCCX_TO_CUIC_SYNC_FAILED

This
                                                						alert occurs when the Unified CCX has failed to notify CUIC on any resource
                                                						change.

PurgeInvoked

AUTO_PURGE_COMPLETE

This
                                                						alert occurs when the Unified CCX Auto Purging has completed.

UnifiedCCXEngineMemoryUsageHigh

UnifiedCCXEngineMemoryUsageHigh

This
                                                						alert occurs when the percentage of JVM heap memory used by Cisco Unified CCX
                                                						Engine process is greater than the configured threshold value.

EMAIL_SERVER_DOWN

EMAIL_SERVER_DOWN

This
                                                						alert occurs when the email server is not reachable.

CCP TomcatServiceDown

SS_PARTIAL_SERVICE_ CCP _TOMCAT_DOWN

This alert occurs when CCP Tomcat is not reachable.

CCP XMPPServiceDown

CCP _XMPP_SERVICE_DOWN

This alert occurs when the Unified CCX has failed to contact CCP runtime server (XMPP).

OutboundScheduledContactImportFailed

OB_SCHEDULED_CONTACT_IMPORT_FAILED

Scheduled import of outbound contacts failed.

OutboundContactImportSchedulingFailed

OB_CONTACT_IMPORT_SCHEDULING_FAILED

Scheduling of outbound import contact failed.

UserPasswordMismatchAcrossNodes

UserPasswordMismatchAcrossNodes

One
                                                						or more user passwords are not same across both the nodes.

ReasonCodesSyncRetryFailure

REASONCODE_SYNC_RETRY_ERROR

Reason Codes Sync from Finesse failed and reached to Maximum
                                                						number of retries.

Ensure that Finesse service and Unified CCX database are
                                                						active.

CCP CacheStatusFull

CCP _CACHE_STATUS_FULL

Unable to cache emails as disk space is low. No new emails will be fetched.

CCP CacheStatusReachedLowThreshold

CCP _CACHE_STATUS_REACHED_LOW_THRESHOLD

Existing emails have consumed a considerable amount of disk space.

CacheStatusOnline

CCP _CACHE_STATUS_ONLINE

Considerable amount of disk space is now available. New emails would now be fetched.

CCP SSLError

SS_PARTIAL_SERVICE_ CCP _SSL_ERROR

This alert occurs when SSL Connectivity with Customer Collaboration Platform fails.

To view or edit values for any alert, right click on the alert and select Set Alert/Properties... .

#### Cisco Identity
                              	 Service Alerts

You can view the Cisco Identity Service alerts from the Unified CCX pane.

The following list contains preconfigured Cisco Identity
                                    		  Service alerts:

Alert Name

Syslog Alarm Name

Description

IdSInitializationFailure

IDS_INIT_ERROR

This alert occurs when an error is encountered during IdS
                                                						initialization.

IDPMetaDataLoadError

IDP_META_DATA_LOAD_ERROR

This alert occurs when the trust could not be established
                                                						between IdS and IdP during initialization.

SPMetaDataLoadError

SP_META_DATA_LOAD_ERROR

This alert occurs when SAML SP metadata Initialization
                                                						fails.

IDPMetaDataUpdateError

IDP_META_DATA_UPDATE_ERROR

This alert occurs when there is an error updating IdP
                                                						metadata and propagating across the cluster.

SPMetaDataUpdateError

SP_META_DATA_UPDATE_ERROR

This alert occurs when SAML SP certificate regeneration
                                                						fails.

TokenMetaDataUpdateError

TOKEN_META_DATA_UPDATE_ERROR

This alert occurs when TOKEN Keystore regeneration or update
                                                						fails.

IdSSecurityConfigNotPresent

IDS_SECURITY_CONFIG_NOT_PRESENT

This alert occurs when some IdS security configuration files
                                                						are not present on the secondary node.

IdSSecurityConfigPullFailure

IDS_SECURITY_CONFIG_PULL_FAILURE

This alert occurs when the security config could not be
                                                						pulled from the primary IdS node.

SAMLCertificateLoadFailed

SAML_CERTIFICATE_LOAD_FAILED

This alert occurs when the system is unable to read the SAML
                                                						SP certificate.

IdSStateNotConfigured

STATE_NOT_CONFIGURED

This alert occurs when the trust between IdS node and IdP is
                                                						yet to be established or when the IdS configuration could not be synchronized
                                                						from the master node.

IdSStateOutOfService

STATE_OUT_OF_SERVICE

This alert occurs whenever a system error results in the IdS
                                                						Application failing to start.

To view or edit values for any alert, right-click the alert and
                                                   				select Set Alert/Properties .

### Syslog and Alert

Below are the set of syslog messages and alert which can be viewed from RTMT.

Syslog Alarm Name

Description

CONTM_INIT_FAILURE

Container Manager initialisation failed

CONTM_INIT_HTTP_FAILURE

Container Manager HTTP Server initialisation failed

CONTM_INIT_PROVISIONING_FAILURE

Container Manager fails to initialise the provisioning

CONTAINER_AUTO_UPDATE_FAILURE

Container Manager fails to update containers based on the provisioning

CONTAINER_AUTO_UPDATE

_RECOVERY_FAILURE

Container Manager failed to update containers based on new provisioning, and failed to revert back containers based on existing
                                          provisioning

CONTAINER_AUTO_UPDATE_PERSIST

_PROVISIONING_FAILURE

Container Manager failed to persist the new provisioning after container auto update

### Traces and
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

### Cloud Connect Serviceability

Use the Cisco Unified Real-Time Monitoring Tool (RTMT) to collect Cloud Connect logs.

You can use the Cloud Connect CLIs to:

List all the containers in your deployment.

View details of the specified container in JSON format.

Start the specified container.

Stop the specified container.

Generate the heap dump for the specified container that is running JVM.

Generate the thread dump for the specified container that is running JVM.

Set log level for the specified service.

Update the Cloud Connect Cherry point connector configuration details.

Download and install RTMT on a client computer.

For more information on Cloud Connect CLIs, see Cloud Connect .

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

| Note | Even when Unified RTMT is not running as an application on your desktop,
                                       			 tasks such as alarm and performance monitoring updates continue to take place
                                       			 on the server in the background. |
|---|---|

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

| Alert Name | Syslog Alarm Name | Description |
|---|---|---|
| DB CRA %
                                                						Space Used | DB CRA %
                                                						Space Used | The
                                                						percentage of used space in the Unified CCX database, db_cra. The database,
                                                						db_cra, contains the Unified CCX historical and configuration data. |
| DBReplicationStopped | DB_REPLICATION_STOPPED | Unified
                                                						CCX Database Replication has been removed. This typically happens when the
                                                						replication queues become full due to the inability to contact the other node. |
| HistoricalDataWrittenToFiles | UCCX_HISTORICAL_DATA_WRITTEN_TO_FILES | Historical data is not written to the Unified CCX database and
                                                						has been written to the file system. Please verify the state of the Unified CCX
                                                						database. |
| Intelligence Center CUIC_DATABASE_UNAVAILABLE | CUIC_DATABASE_UNAVAILABLE | This
                                                						alert occurs when the Intelligence Center CUIC_DATABASE_UNAVAILABLE event gets
                                                						generated. This indicates the system detected critical error with database. |
| Intelligence Center CUIC_DB_REPLICATION_FAILED | CUIC_DB_REPLICATION_FAILED | This
                                                						alert occurs when the Intelligence Center CUIC_DB_REPLICATION_FAILED event gets
                                                						generated. This indicates the Database replication failed. |
| Intelligence Center CUIC_REPORT_EXECUTION_FAILED | CUIC_REPORT_EXECUTION_FAILED | This
                                                						alert occurs when the Intelligence Center CUIC_DB_REPLICATION_FAILED event gets
                                                						generated. This indicates that the reporting server could not run a report.
                                                						This could be because the associated datasource is offline. |
| Intelligence Center CUIC_UNRECOVERABLE_ERROR | CUIC_UNRECOVERABLE_ERROR | This
                                                						alert occurs when the Intelligence Center CUIC_UNRECOVERABLE_ERROR event gets
                                                						generated. This indicates that the system has detected an internal error within
                                                						Reporting Server which may prevent it from functioning correctly. Restart may
                                                						be required. |
| CCXToCUICAdminSyncFailed | UCCX_TO_CUIC_SYNC_FAILED | This
                                                						alert occurs when the Unified CCX has failed to notify CUIC on any resource
                                                						change. |
| CCXToCUICCVDSyncFailed | UCCX_TO_CUIC_SYNC_FAILED | This
                                                						alert occurs when the Unified CCX has failed to notify CUIC on any resource
                                                						change. |
| CCXToCUICEngineSyncFailed | UCCX_TO_CUIC_SYNC_FAILED | This
                                                						alert occurs when the Unified CCX has failed to notify CUIC on any resource
                                                						change. |
| PurgeInvoked | AUTO_PURGE_COMPLETE | This
                                                						alert occurs when the Unified CCX Auto Purging has completed. |
| UnifiedCCXEngineMemoryUsageHigh | UnifiedCCXEngineMemoryUsageHigh | This
                                                						alert occurs when the percentage of JVM heap memory used by Cisco Unified CCX
                                                						Engine process is greater than the configured threshold value. |
| EMAIL_SERVER_DOWN | EMAIL_SERVER_DOWN | This
                                                						alert occurs when the email server is not reachable. |
| CCP TomcatServiceDown | SS_PARTIAL_SERVICE_ CCP _TOMCAT_DOWN | This alert occurs when CCP Tomcat is not reachable. |
| CCP XMPPServiceDown | CCP _XMPP_SERVICE_DOWN | This alert occurs when the Unified CCX has failed to contact CCP runtime server (XMPP). |
| OutboundScheduledContactImportFailed | OB_SCHEDULED_CONTACT_IMPORT_FAILED | Scheduled import of outbound contacts failed. |
| OutboundContactImportSchedulingFailed | OB_CONTACT_IMPORT_SCHEDULING_FAILED | Scheduling of outbound import contact failed. |
| UserPasswordMismatchAcrossNodes | UserPasswordMismatchAcrossNodes | One
                                                						or more user passwords are not same across both the nodes. |
| ReasonCodesSyncRetryFailure | REASONCODE_SYNC_RETRY_ERROR | Reason Codes Sync from Finesse failed and reached to Maximum
                                                						number of retries. Ensure that Finesse service and Unified CCX database are
                                                						active. |
| CCP CacheStatusFull | CCP _CACHE_STATUS_FULL | Unable to cache emails as disk space is low. No new emails will be fetched. |
| CCP CacheStatusReachedLowThreshold | CCP _CACHE_STATUS_REACHED_LOW_THRESHOLD | Existing emails have consumed a considerable amount of disk space. |
| CacheStatusOnline | CCP _CACHE_STATUS_ONLINE | Considerable amount of disk space is now available. New emails would now be fetched. |
| CCP SSLError | SS_PARTIAL_SERVICE_ CCP _SSL_ERROR | This alert occurs when SSL Connectivity with Customer Collaboration Platform fails. |

| Note | To view or edit values for any alert, right click on the alert and select Set Alert/Properties... . |
|---|---|

| Alert Name | Syslog Alarm Name | Description |
|---|---|---|
| IdSInitializationFailure | IDS_INIT_ERROR | This alert occurs when an error is encountered during IdS
                                                						initialization. |
| IDPMetaDataLoadError | IDP_META_DATA_LOAD_ERROR | This alert occurs when the trust could not be established
                                                						between IdS and IdP during initialization. |
| SPMetaDataLoadError | SP_META_DATA_LOAD_ERROR | This alert occurs when SAML SP metadata Initialization
                                                						fails. |
| IDPMetaDataUpdateError | IDP_META_DATA_UPDATE_ERROR | This alert occurs when there is an error updating IdP
                                                						metadata and propagating across the cluster. |
| SPMetaDataUpdateError | SP_META_DATA_UPDATE_ERROR | This alert occurs when SAML SP certificate regeneration
                                                						fails. |
| TokenMetaDataUpdateError | TOKEN_META_DATA_UPDATE_ERROR | This alert occurs when TOKEN Keystore regeneration or update
                                                						fails. |
| IdSSecurityConfigNotPresent | IDS_SECURITY_CONFIG_NOT_PRESENT | This alert occurs when some IdS security configuration files
                                                						are not present on the secondary node. |
| IdSSecurityConfigPullFailure | IDS_SECURITY_CONFIG_PULL_FAILURE | This alert occurs when the security config could not be
                                                						pulled from the primary IdS node. |
| SAMLCertificateLoadFailed | SAML_CERTIFICATE_LOAD_FAILED | This alert occurs when the system is unable to read the SAML
                                                						SP certificate. |
| IdSStateNotConfigured | STATE_NOT_CONFIGURED | This alert occurs when the trust between IdS node and IdP is
                                                						yet to be established or when the IdS configuration could not be synchronized
                                                						from the master node. |
| IdSStateOutOfService | STATE_OUT_OF_SERVICE | This alert occurs whenever a system error results in the IdS
                                                						Application failing to start. |

| Note | To view or edit values for any alert, right-click the alert and
                                                   				select Set Alert/Properties . |
|---|---|

| Syslog Alarm Name | Description |
|---|---|
| CONTM_INIT_FAILURE | Container Manager initialisation failed |
| CONTM_INIT_HTTP_FAILURE | Container Manager HTTP Server initialisation failed |
| CONTM_INIT_PROVISIONING_FAILURE | Container Manager fails to initialise the provisioning |
| CONTAINER_AUTO_UPDATE_FAILURE | Container Manager fails to update containers based on the provisioning |
| CONTAINER_AUTO_UPDATE _RECOVERY_FAILURE | Container Manager failed to update containers based on new provisioning, and failed to revert back containers based on existing
                                          provisioning |
| CONTAINER_AUTO_UPDATE_PERSIST _PROVISIONING_FAILURE | Container Manager failed to persist the new provisioning after container auto update |

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