---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-cisco-vvb-vvb-12-5-operations-guide-ccvp-b-1251--e7d26f72f2
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/cisco_vvb/VVB_12_5/operations/guide/ccvp_b_1251-cisco-virtualized-voice-browser-serviceability-administration-guide/ccvp_b_1251-cisco-virtualized-voice-browser-serviceability-administration-guide_chapter_0100.html
retrieved_at: 2026-08-21T16:34:46.109794+00:00
---

Cisco Virtualized Voice Browser Serviceability Administration Guide, Release 12.5(1)

# Cisco Virtualized Voice Browser Serviceability Administration Guide, Release 12.5(1)

Updated: February 2, 2020

Chapter: Serviceability
	 Tools

## Chapter: Serviceability
	 Tools

# Serviceability
                     	 Tools

## Access Control
                        	 Center — Network Services Menu

Control Center in Cisco VVB Serviceability lets you do the following tasks:

Start, stop, and restart Cisco VVB services

View the status the status of Cisco VVB services

Refresh the status of Cisco VVB services

Cisco VVB Serviceability provides Control Center - Network
                              		  Services menu option, which is essential for your system to function.

Choose Tools > Control Center - Network
                                             				  Services from the Cisco
                                          				VVB Serviceability menu bar to perform the above-mentioned actions.

## Network
                        	 Services

Installed
                              		  automatically, network services include services that the system requires to
                              		  function; for example, database and system services. Because these services are
                              		  required for basic functionality, you cannot activate them in the Service
                              		  Activation window.

After the installation of
                              		  your application, network services start automatically. The list of services
                              		  displayed in the Control Center—Network Services web page depends on the
                              		  license package of your Cisco VVB. The Serviceability categorizes the network
                              		  services into the following categories, which are explained in the subsequent
                              		  sections:

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

Only System and Admin Services Information will be visible in Cisco VVB Node Services Information.

### System
                           	 Services

The Cisco VVB Serviceability service supports starting and
                                 		  stopping of the following System Services:

Perfmon Counter
                                          				Service

Cluster View
                                          				Daemon—List of Managers

Engine—List of
                                          				Subsystems and Managers

Voice Subagent

SNMP Java
                                          				Adapter

Speech Server

### Admin
                           	 Services

The Cisco VVB Serviceability service supports starting and stopping of the
                                 		  following Admin Services:

Cisco VVB
                                          				Configuration API

Cisco VVB
                                          				Administration

Cisco VVB
                                          				Serviceability - List of Managers

You can start or stop this service only by using CLI. Cisco VVB Serviceability web interface does not provide the functionality
                                                      to start or stop this service.

### DB Services

You can
                                 		  start and stop Cisco VVB Database
                                 		  service.

## Manage Network
                        	 Services

Control
                              		  Center in Cisco VVB Serviceability allows you to view status, refresh the status, and to start,
                              		  stop, and restart network services.

Perform the following procedure to start, stop, restart, or view the status of services for a server. You can start, stop,
                              or refresh only one service at a time. Be aware that when a service is stopping, you cannot start it until the service is
                              stopped. Likewise, when a service is starting, you cannot stop it until the service starts.

Choose Tools > Control Center—Network
                                             				  Services from the Cisco
                                          				VVB Serviceability menu bar.

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

## Simple Network
                        	 Management Protocol

Simple
                              		  Network Management Protocol (SNMP) is an industry-standard interface for
                              		  exchanging management information between network devices. SNMP enables you to
                              		  monitor and manage the Cisco VVB system. You
                              		  also can set up SNMP traps to automatically notify any high-severity messages
                              		  and errors that are generated by the Cisco VVB system.

You can configure
                              		  the SNMP settings using the Cisco
                                 			 Unified Serviceability web interface.

### SNMP Management
                           	 Information Base (MIB)

A
                                 		  Management Information Base (MIB) designates a collection of information that
                                 		  is organized hierarchically. MIBs are made up of managed objects, which are
                                 		  referenced by object identifiers. Managed objects are made up of one or more
                                 		  object instances, which are essentially variables. MIBs provide status
                                 		  monitoring, provisioning, and notification.

MIB

Agent
                                             					 Service

CISCO-VOICE-APPS-MIB

Cisco VVB Voice
                                             					 Subagent

CISCO-CDP-MIB

Cisco CDP Agent

CISCO-SYSLOG-MIB

Cisco
                                             					 Syslog Agent

SYSAPPL-MIB

System
                                             					 Application Agent

MIB-II

MIB2
                                             					 Agent

HOST-RESOURCES-MIB

Host
                                             					 Resources Agent

In Cisco VVB , the
                                                      					 SysAppl MIB will not provide the Cisco VVB subsystem
                                                      					 information and their status information. You can view the subsystem and their
                                                      					 status information through Cisco VVB Serviceability web interface.

Syslog
                                                      					 messages can also be sent as SNMP traps using the CISCO-SYSLOG-MIB. Refer to
                                                      					 the section on CISCO-SYSLOG-MIB for details. They can be correlated to the
                                                      					 failure of important features of Cisco VVB .

The following section describes CISCO-VOICE-APPS-MIB. For more information about other Cisco VVB supported MIBs, see Cisco Unified CM SNMP chapter in the Cisco Unified Serviceability Administration Guide available at https://www.cisco.com/en/US/partner/products/sw/voicesw/ps556/prod_maintenance_guides_list.html

#### CISCO-VOICE-APPS-MIB

The CISCO-VOICE-APPS-MIB
                                 		  provides information associated with the installed workflow applications
                                 		  provisioned on the Cisco VVB Server. It also provides information on the
                                 		  supported SNMP Traps on Cisco VVB. You can manage CISCO-VOICE-APPS-MIB through Cisco
                                    			 VVB Serviceability web interface.

Cisco VVB Voice
                                       				Subagent

Cisco VVB Voice Subagent
                                 		  service implements the CISCO-VOICE-APPS-MIB. Cisco VVB Voice Subagent
                                 		  Service communicates with the SNMP Master Agent through Cisco VVB SNMP Java
                                 		  Adaptor. The Cisco VVB SNMP Java
                                 		  Adaptor service should be up and running for the Cisco VVB Voice
                                 		  Subagent to work properly.

For more
                                 		  information about the CISCO-VOICE-APPS-MIB, see this URL: ftp://ftp.cisco.com/pub/mibs/v2/CISCO-VOICE-APPS-MIB.my.

In Cisco VVB , while
                                                   				  exposing the Cisco VVB workflow
                                                   				  information through CISCO-VOICE-APPS-MIB, only one trigger per application row
                                                   				  will be returned when doing a walk on the workflow table
                                                   				  (cvaWorkflowInstallTable object). If there are multiple triggers associated
                                                   				  with a Workflow application, these are shown as separate entries (rows).

#### SNMP
                                 		  Traps

Subsystems, which are the functional blocks of Cisco VVB , sends out
                                 		  alarms that are routed to the Syslog or as SNMP Traps. SNMP Traps are generated
                                 		  when any Cisco VVB Subsystem
                                 		  or module or processes start or stop or runtime failure occurs for a module.
                                 		  These failures can be tracked for each major component to track the health of
                                 		  the Cisco VVB system.

The following
                                 		  Traps are supported as part of the CISCO-VOICE-APPS-MIB:

Trap
                                             						Name

Description

cvaModuleStart

A
                                             						cvaModuleStart notification signifies that an application module or subsystem
                                             						has successfully started and transitioned into in-service state.

cvaModuleStop

A
                                             						cvaModuleStop notification signifies that an application module or subsystem
                                             						has stopped. If cause of the failure is known then, it will be specified as
                                             						part of the Trap message.

cvaModuleRunTimeFailure

cvaModuleRunTimeFailure notification signifies that a run time failure has
                                             						occurred. If cause of the failure is known then it will be specified as part of
                                             						the Trap message.

cvaProcessStart

A
                                             						cvaProcessStart notification signifies that a process has just started.

cvaProcessStop

A
                                             						cvaProcessStop notification signifies that a process has just stopped.

The ModuleStart and ModuleStop traps are generated when the key Cisco VVB services including Cisco VVB Engine and Cisco VVB Administration and their modules/subsystems are started and stopped respectively.

The ProcessStart and ProcessStop traps are generated when the key Cisco VVB services including Cisco VVB Engine,  and Cisco VVB Administration are started and stopped.

You can
                                 		  configure the notification destinations by using the SNMP
                                    			 Notification Destination Configuration page in Cisco Unified
                                    			 Serviceability .

SNMP Traps are not generated for events when the Cisco VVB services and/or their subsystems go Out of Service or are In Service. These events are sent as Remote Syslog messages and
                                             can be viewed through any third-party Syslog Viewers. You can refer to the list of Cisco VVB services and their subsystems/modules from the Cisco VVB Serviceability under Tools > Control Center - Network Services .

Cisco VVB does not
                                                   				  support SNMP trap V3 notifications.

CISCO-VOICE-APPS-MIB does not support INFORM notifications.

For
                                 		  all notifications, the system sends traps immediately if the corresponding trap
                                 		  flags are enabled. Before you configure notification destination, verify that
                                 		  the required SNMP services are activated and running. Also, make sure that you
                                 		  configured the privileges for the community string or user correctly.

### More Info on
                           	 SNMP

For more information related to SNMP such as SNMP Version 1, Version 2C, Version 3, SNMP system group configuration, SNMP
                                 informs and SNMP trap parameters, see Cisco Unified Serviceability Administration Guide available at https://www.cisco.com/en/US/partner/products/sw/voicesw/ps556/prod_maintenance_guides_list.html

## Configure
                        	 Performance Monitoring of Cisco VVB Servers

- Cluster View Daemon

- Engine

- Serviceability

Use the
                              		  following procedure to configure JVM parameters for a particular service on a
                              		  particular server.

From the Cisco VVB Serviceability
                                       			 menu bar, choose Tools > Performance Configuration and
                                             				  Logging .

Choose a server
                                       			 from the Server drop-down list box and click Go .

The first node
                                          				is selected by default and JVM options for the VVB Engine service in
                                          				the first node is displayed.

Choose a service
                                       			 for which you want to see the JVM options from the Service drop-down list box.
                                       			 You should be able to select any one of the following services from this list
                                       			 box:

- Cluster View Daemon

- Engine

- Serviceability

PrintClassHistogram

PrintGCDetails

PrintGC

PrintGCTimeStamps

Click the Dump
                                          				Thread Trace icon or button to dump the thread traces for the
                                       			 selected service in the selected server. You can collect the corresponding
                                       			 jvm.log from the log folder for that facility using Real-Time Monitoring Tool
                                       			 (RTMT).

Click the Dump
                                          				Memory Trace icon or button to dump the memory traces. This creates
                                       			 the following two logs in the log folder for that facility.

Memory-<facility name>-<time stamp>.hprof (for heap
                                             				  dump)

histo-<facility name> <time stamp>.log (for
                                             				  histogram)

You can change
                                       			 the JVM options by clicking Enable or Disable radio buttons in this page.

Click the Update
                                             				  JVM Options icon or button to update the new settings for selected
                                          				service on selected node.

| Choose Tools > Control Center - Network
                                             				  Services from the Cisco
                                          				VVB Serviceability menu bar to perform the above-mentioned actions. Tip You may need to manage services in both Cisco VVB Serviceability and Cisco Unified Serviceability to troubleshoot a problem. For information on Unified Serviceability services,
                                                   see the Cisco Unified Contact
                                                            				  Center Express Serviceability Administration Guide available at: https://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-callmanager/tsd-products-support-series-home.html . | Tip | You may need to manage services in both Cisco VVB Serviceability and Cisco Unified Serviceability to troubleshoot a problem. For information on Unified Serviceability services,
                                                   see the Cisco Unified Contact
                                                            				  Center Express Serviceability Administration Guide available at: https://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-callmanager/tsd-products-support-series-home.html . |
|---|---|---|
| Tip | You may need to manage services in both Cisco VVB Serviceability and Cisco Unified Serviceability to troubleshoot a problem. For information on Unified Serviceability services,
                                                   see the Cisco Unified Contact
                                                            				  Center Express Serviceability Administration Guide available at: https://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-callmanager/tsd-products-support-series-home.html . |

| Tip | You may need to manage services in both Cisco VVB Serviceability and Cisco Unified Serviceability to troubleshoot a problem. For information on Unified Serviceability services,
                                                   see the Cisco Unified Contact
                                                            				  Center Express Serviceability Administration Guide available at: https://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-callmanager/tsd-products-support-series-home.html . |
|---|---|

| Note | Only System and Admin Services Information will be visible in Cisco VVB Node Services Information. |
|---|---|

| Note | You can start or stop this service only by using CLI. Cisco VVB Serviceability web interface does not provide the functionality
                                                      to start or stop this service. |
|---|---|

| Step 1 | Choose Tools > Control Center—Network
                                             				  Services from the Cisco
                                          				VVB Serviceability menu bar. |
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

| MIB | Agent
                                             					 Service |
|---|---|
| CISCO-VOICE-APPS-MIB | Cisco VVB Voice
                                             					 Subagent |
| CISCO-CDP-MIB | Cisco CDP Agent |
| CISCO-SYSLOG-MIB | Cisco
                                             					 Syslog Agent |
| SYSAPPL-MIB | System
                                             					 Application Agent |
| MIB-II | MIB2
                                             					 Agent |
| HOST-RESOURCES-MIB | Host
                                             					 Resources Agent |

| Note | In Cisco VVB , the
                                                      					 SysAppl MIB will not provide the Cisco VVB subsystem
                                                      					 information and their status information. You can view the subsystem and their
                                                      					 status information through Cisco VVB Serviceability web interface. Syslog
                                                      					 messages can also be sent as SNMP traps using the CISCO-SYSLOG-MIB. Refer to
                                                      					 the section on CISCO-SYSLOG-MIB for details. They can be correlated to the
                                                      					 failure of important features of Cisco VVB . |
|---|---|

| Note | In Cisco VVB , while
                                                   				  exposing the Cisco VVB workflow
                                                   				  information through CISCO-VOICE-APPS-MIB, only one trigger per application row
                                                   				  will be returned when doing a walk on the workflow table
                                                   				  (cvaWorkflowInstallTable object). If there are multiple triggers associated
                                                   				  with a Workflow application, these are shown as separate entries (rows). |
|---|---|

| Trap
                                             						Name | Description |
|---|---|
| cvaModuleStart | A
                                             						cvaModuleStart notification signifies that an application module or subsystem
                                             						has successfully started and transitioned into in-service state. |
| cvaModuleStop | A
                                             						cvaModuleStop notification signifies that an application module or subsystem
                                             						has stopped. If cause of the failure is known then, it will be specified as
                                             						part of the Trap message. |
| cvaModuleRunTimeFailure | cvaModuleRunTimeFailure notification signifies that a run time failure has
                                             						occurred. If cause of the failure is known then it will be specified as part of
                                             						the Trap message. |
| cvaProcessStart | A
                                             						cvaProcessStart notification signifies that a process has just started. |
| cvaProcessStop | A
                                             						cvaProcessStop notification signifies that a process has just stopped. |

| Note | SNMP Traps are not generated for events when the Cisco VVB services and/or their subsystems go Out of Service or are In Service. These events are sent as Remote Syslog messages and
                                             can be viewed through any third-party Syslog Viewers. You can refer to the list of Cisco VVB services and their subsystems/modules from the Cisco VVB Serviceability under Tools > Control Center - Network Services . |
|---|---|

| Note | Cisco VVB does not
                                                   				  support SNMP trap V3 notifications. CISCO-VOICE-APPS-MIB does not support INFORM notifications. |
|---|---|

| Step 1 | From the Cisco VVB Serviceability
                                       			 menu bar, choose Tools > Performance Configuration and
                                             				  Logging . |
|---|---|
| Step 2 | Choose a server
                                       			 from the Server drop-down list box and click Go . The first node
                                          				is selected by default and JVM options for the VVB Engine service in
                                          				the first node is displayed. |
| Step 3 | Choose a service
                                       			 for which you want to see the JVM options from the Service drop-down list box.
                                       			 You should be able to select any one of the following services from this list
                                       			 box: Cluster View Daemon Engine Serviceability The following
                                          				JVM options are displayed for each service: PrintClassHistogram PrintGCDetails PrintGC PrintGCTimeStamps |
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