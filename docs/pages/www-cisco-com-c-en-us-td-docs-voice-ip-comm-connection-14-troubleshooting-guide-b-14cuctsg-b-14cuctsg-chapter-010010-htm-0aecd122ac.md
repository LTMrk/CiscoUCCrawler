---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-connection-14-troubleshooting-guide-b-14cuctsg-b-14cuctsg-chapter-010010-htm-0aecd122ac
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/14/troubleshooting/guide/b_14cuctsg/b_14cuctsg_chapter_010010.html
retrieved_at: 2026-08-17T02:17:41.570681+00:00
---

Troubleshooting Guide for Cisco Unity Connection Release 14

# Troubleshooting Guide for Cisco Unity Connection Release 14

Updated: August 14, 2024

Chapter: Troubleshooting a Cisco Unity Connection Cluster Configuration

## Chapter: Troubleshooting a Cisco Unity Connection Cluster Configuration

# Troubleshooting a Cisco Unity Connection Cluster Configuration

### Troubleshooting a Cisco Unity Connection Cluster Configuration

## One Server Stops
                        	 Functioning and the Other Server is Not Handling Calls

When one
                           		Unity Connection server in a Unity Connection cluster is not functioning (for
                           		example, when the subscriber server is undergoing maintenance) and the
                           		remaining server does not answer calls or send MWI requests, use the following
                           		task list to determine the cause and to resolve the problem.

Following are the tasks to troubleshoot when one server stops
                           		functioning and the other server is not handling calls:

Verify the status of the voice messaging ports in Cisco Unity
                                 			 Connection Serviceability. See the “Verifying
                                    				the Status of the Voice Messaging Ports” section on page 19-1 .

Verify the voice messaging port assignments for the phone system
                                 			 integration. See the “Verifying
                                    				the Voice Messaging Ports Assignments for Phone System Integration” section on
                                    				page 19-2 .

For SCCP integrations, confirm that the voice messaging ports
                                 			 are registered with the Cisco Unified CM server. See the “Confirming
                                    				that Voice Messaging Ports are Registered (SCCP Integrations Only)” section on
                                    				page 19-2 .

Enable the SRM micro trace (all levels) in Cisco Unity
                                 			 Connection Serviceability. For detailed instructions on enabling the micro
                                 			 trace and viewing the trace logs, see the Using Diagnostic Traces for Troubleshooting section.

The Cisco Unity Connection cluster feature is not supported for use with Cisco Business Edition. Requirements for the Unity
                                             Connection cluster feature are available in the “ Requirements for a Unity Connection Cluster ” section in the System Requirements Guide for Cisco Unity Connection Release 14 , available at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/14/requirements/b_14cucsysreqs.html .

### Verifying the
                           	 Status of the Voice Messaging Ports

Step 1

In Cisco Unity Connection Serviceability, on the Tools menu,
                                          			 select Cluster Management .

Step 2

On the Cluster Management page under Port Manager, verify the
                                          			 following for the server that should be handling calls:

In the Total Ports column, the number of ports that is listed is
                                                   					 correct.

In the Change Port Status column, the Stop Taking Calls button
                                                   					 appears. If the Take Calls button appears, select Take Calls .

### Verifying the
                           	 Voice Messaging Ports Assignments for Phone System Integration

Step 1

In Cisco Unity Connection Administration, expand Telephony Integrations , then select Phone System .

Step 2

In the Related Links list, select Check Telephony Integration and select Go .

The Task Execution Results displays one or more messages with
                                             				troubleshooting steps.

Step 3

Follow the steps for correcting the problems.

Step 4

Repeat Step 2 through Step 3 until the Task
                                          			 Execution Results displays no problems.

### Confirming that
                           	 Voice Messaging Ports are Registered (SCCP Integrations Only)

Step 1

In Cisco Unified CM Administration, on the Voice Mail menu,
                                          			 select Voice Mail Port .

Step 2

On the Find and List Voice Mail Ports page, select Find .

Step 3

In the Status column, confirm that all ports show the status of
                                          			 “ Registered with <server
                                             				name .”

## Both Servers Attain Primary Server Status

Use the troubleshooting information in this section if both servers in the Unity Connection cluster have Primary server status
                           (a “split brain” condition). See the following possible causes:

The network is not functioning or is preventing the publisher and subscriber servers from communicating with each other.

The solution is to restore the network Unity Connection so that the publisher and subscriber servers can communicate.

The host name for the subscriber server was changed and is not entered correctly on the System Settings > Cluster page of
                                 the publisher server.

The solution is to enter the correct host name of the subscriber server on the System Settings > Cluster page of the publisher
                           server.

## Unity Connection
                        	 Cluster Not Functioning Correctly

When
                           		a Unity Connection cluster is not functioning correctly (for example, server
                           		status does not change when expected), use the following task list to determine
                           		the cause and to resolve the problem. Do the tasks in the order presented until
                           		the problem is resolved:

Confirm that the applicable services are running on the server
                                 			 with primary server status. See the “Confirming
                                    				that Applicable Services are Running on the Server with Primary Server Status”
                                    				section on page 19-3 .

Confirm that the applicable services are running on both
                                 			 servers. See the “Confirming
                                    				that Applicable Services are Running on Both Servers” section on
                                    				page 19-3 .

Use traces to troubleshoot the Unity Connection cluster. For
                                 			 detailed instructions on enabling the applicable traces and viewing the trace
                                 			 logs, see the Traces in Cisco Unity Connection Serviceability .

### Confirming that
                           	 Applicable Services are Running on the Server with Primary Server
                           	 Status

Step 1

In Cisco Unity Connection Serviceability, on the Tools menu,
                                          			 select Service Management .

Step 2

On the Control Center - Feature Services page, under Critical
                                          			 Services, confirm that the following services have the Started service status:

Connection Message Transfer Agent

Connection Notifier

Step 3

If the services have the Stopped service status, select Start .

### Confirming that
                           	 Applicable Services are Running on Both Servers

Step 1

In Cisco Unity Connection Serviceability, on the Tools menu,
                                          			 select Service Management .

Step 2

On the Control Center - Feature Services page, under Status Only
                                          			 Services, confirm that the Unity Connection Server Role Manager service has the Started service status.

The services in the Status Only Services section cannot be started in Cisco Unity Connection Serviceability. You must use
                                             the command line interface (CLI) to start or stop these services. For information on the CLI, see the Command Line Interface Reference Guide for Cisco Unified Communications Solutions at https://www.cisco.com/c/en/us/support/unified-communications/unity-connection/products-maintenance-guides-list.html .

Step 3

Under Critical Services, check the service status for the
                                          			 following services:

Connection Conversation Manager

Connection Mixer

If the services have the Started service status, skip to Step 4 .
                                             				If the services have the Stopped service status, select Start .

Step 4

Under Base Services, check the service status for the Unity
                                          			 Connection DB Event Publisher service.

If the service has the Started service status, skip to Step 5 .
                                             				If the service has the Stopped service status, select Start .

Step 5

Under Optional Services, check the service status for the
                                          			 following services:

Connection File Syncer

Connection IMAP Server

Connection SMTP Server

If the service has the Stopped service status, select Start .

## Server Cannot be
                        	 Added to the Unity Connection Cluster

Use the
                           		troubleshooting information in this section if the Add New button is disabled
                           		on the System Settings > Cluster page so that you cannot add a server to the
                           		Unity Connection cluster. See the following possible reasons why the Unity
                           		Connection cluster feature is not available:

Unity Connection is installed as Cisco Business Edition, which does not support the Unity Connection cluster feature. See
                                 the “ Requirements for a Unity Connection Cluster ” section in the System Requirements for Cisco Unity Connection Guide Release 14 , available at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/14/requirements/b_14cucsysreqs.html .

The size of the hard disc on the publisher server is inadequate for supporting the Unity Connection cluster feature. Both
                                 servers in a Unity Connection cluster must meet the specifications in the Cisco Unity Connection Supported Platforms List Release 14, available at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/14/supported_platforms/b_14cucspl.html .

The number of servers in the Unity Connection cluster is the maximum that is supported. No more servers can be added to the
                                 Unity Connection cluster. For information on replacing Unity Connection servers in a Unity Connection cluster, see the “ Replacing the Non Functional Server ” section of “Maintaining Cisco Unity Connection Server” chapter of the Install, Upgrade, and Maintenance Guide for Cisco Unity Connection Release 14 , available at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/14/install_upgrade/guide/b_14cuciumg.html .

## Cannot Access Alert Logs When the Publisher Server Stops Functioning

When the publisher server is not functioning and you cannot access the alert logs from the subscriber server, you must specify
                           the subscriber server as the failover collector.

### Enabling the
                           	 Subscriber Server to Access the Alert Logs When the Publisher Server Stops
                           	 Functioning

Step 1

On the publisher server, in Cisco Unity Connection
                                          			 Administration, expand System Settings , then select Service Parameters .

Step 2

On the Service Parameters page, in the Server field, select the
                                          			 publisher server.

Step 3

In the Service field, select Cisco AMC Service .

Step 4

In the Failover Collector field, select the subscriber server.

Step 5

Select Save .

Step 6

In Cisco Unified Serviceability, in the Tools menu, select Control Center - Network Services .

Step 7

In the Server field, select the subscriber server and select Go .

Step 8

Under Performance and Monitoring, select Cisco AMC Service and select Restart .

Step 9

When prompted to confirm that you want to restart the service,
                                          			 select OK .

| Note | The Cisco Unity Connection cluster feature is not supported for use with Cisco Business Edition. Requirements for the Unity
                                             Connection cluster feature are available in the “ Requirements for a Unity Connection Cluster ” section in the System Requirements Guide for Cisco Unity Connection Release 14 , available at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/14/requirements/b_14cucsysreqs.html . |
|---|---|

| Step 1 | In Cisco Unity Connection Serviceability, on the Tools menu,
                                          			 select Cluster Management . |
|---|---|
| Step 2 | On the Cluster Management page under Port Manager, verify the
                                          			 following for the server that should be handling calls: In the Total Ports column, the number of ports that is listed is
                                                   					 correct. In the Change Port Status column, the Stop Taking Calls button
                                                   					 appears. If the Take Calls button appears, select Take Calls . |

| Step 1 | In Cisco Unity Connection Administration, expand Telephony Integrations , then select Phone System . |
|---|---|
| Step 2 | In the Related Links list, select Check Telephony Integration and select Go . The Task Execution Results displays one or more messages with
                                             				troubleshooting steps. |
| Step 3 | Follow the steps for correcting the problems. |
| Step 4 | Repeat Step 2 through Step 3 until the Task
                                          			 Execution Results displays no problems. |

| Step 1 | In Cisco Unified CM Administration, on the Voice Mail menu,
                                          			 select Voice Mail Port . |
|---|---|
| Step 2 | On the Find and List Voice Mail Ports page, select Find . |
| Step 3 | In the Status column, confirm that all ports show the status of
                                          			 “ Registered with <server
                                             				name .” |

| Step 1 | In Cisco Unity Connection Serviceability, on the Tools menu,
                                          			 select Service Management . |
|---|---|
| Step 2 | On the Control Center - Feature Services page, under Critical
                                          			 Services, confirm that the following services have the Started service status: Connection Message Transfer Agent Connection Notifier |
| Step 3 | If the services have the Stopped service status, select Start . |

| Step 1 | In Cisco Unity Connection Serviceability, on the Tools menu,
                                          			 select Service Management . |
|---|---|
| Step 2 | On the Control Center - Feature Services page, under Status Only
                                          			 Services, confirm that the Unity Connection Server Role Manager service has the Started service status. The services in the Status Only Services section cannot be started in Cisco Unity Connection Serviceability. You must use
                                             the command line interface (CLI) to start or stop these services. For information on the CLI, see the Command Line Interface Reference Guide for Cisco Unified Communications Solutions at https://www.cisco.com/c/en/us/support/unified-communications/unity-connection/products-maintenance-guides-list.html . |
| Step 3 | Under Critical Services, check the service status for the
                                          			 following services: Connection Conversation Manager Connection Mixer If the services have the Started service status, skip to Step 4 .
                                             				If the services have the Stopped service status, select Start . |
| Step 4 | Under Base Services, check the service status for the Unity
                                          			 Connection DB Event Publisher service. If the service has the Started service status, skip to Step 5 .
                                             				If the service has the Stopped service status, select Start . |
| Step 5 | Under Optional Services, check the service status for the
                                          			 following services: Connection File Syncer Connection IMAP Server Connection SMTP Server If the service has the Stopped service status, select Start . |

| Step 1 | On the publisher server, in Cisco Unity Connection
                                          			 Administration, expand System Settings , then select Service Parameters . |
|---|---|
| Step 2 | On the Service Parameters page, in the Server field, select the
                                          			 publisher server. |
| Step 3 | In the Service field, select Cisco AMC Service . |
| Step 4 | In the Failover Collector field, select the subscriber server. |
| Step 5 | Select Save . |
| Step 6 | In Cisco Unified Serviceability, in the Tools menu, select Control Center - Network Services . |
| Step 7 | In the Server field, select the subscriber server and select Go . |
| Step 8 | Under Performance and Monitoring, select Cisco AMC Service and select Restart . |
| Step 9 | When prompted to confirm that you want to restart the service,
                                          			 select OK . |