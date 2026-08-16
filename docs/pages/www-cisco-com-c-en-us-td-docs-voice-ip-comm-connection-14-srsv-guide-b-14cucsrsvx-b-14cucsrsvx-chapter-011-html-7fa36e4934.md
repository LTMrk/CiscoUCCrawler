---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-connection-14-srsv-guide-b-14cucsrsvx-b-14cucsrsvx-chapter-011-html-7fa36e4934
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/14/srsv/guide/b_14cucsrsvx/b_14cucsrsvx_chapter_011.html
retrieved_at: 2026-08-16T18:35:27.883272+00:00
---

Complete Reference Guide for Cisco Unity Connection Survivable Remote Site Voicemail (SRSV)

# Complete Reference Guide for Cisco Unity Connection Survivable Remote Site Voicemail (SRSV)

Updated: March 31, 2021

Chapter: Services in Cisco Unity Connection SRSV

## Chapter: Services in Cisco Unity Connection SRSV

- Services in Cisco Unity Connection SRSV

- Unity Connection                              	 SRSV Services

- Configuring                              	 Services in Control Center

# Services in Cisco Unity Connection SRSV

Introduction

This chapter provides information on the various critical, base, and optional services in Cisco Unity Connection Survivable
                        Remote Site Voicemail and a way to manage the services.

## Unity Connection
                        	 SRSV Services

The Table
                                 			 -1 describes the services in Unity Connection SRSV:

Service

Description

Status Only Services

Connection DB

This service activates the Cisco Unity Connection database and
                                          					 can be deactivated only using the Command Line Interface (CLI).

This service should always be in the Started state for the Unity
                                                      						Connection SRSV server to be functional. Stopping or restarting this service
                                                      						impacts other critical services.

Connection Server Role Manager

This service enables the server status when a Unity Connection
                                          					 cluster is configured and can be deactivated only using the CLI.

Connection Serviceability

This service enables the Cisco Unity Connection Serviceability
                                          					 Administration interface and can be deactivated only using the command-line
                                          					 interface (CLI).

Critical Services

Connection Conversation Manager

This service enables Unity Connection to handle the calls.
                                          					 Disabling this service degrades the ability of Unity Connection to function.

Connection Message Transfer Agent

This service enables the delivery of messages to the message
                                          					 store. Disabling this service degrades the ability of Unity Connection to
                                          					 function.

Connection Mixer

This service enables the audio (media stream) for calls,
                                          					 recorded messages, and Text-to-Speech (TTS). Disabling this service degrades
                                          					 the ability of Unity Connection to function.

Connection Notifier

This service enables notification of messages, such as turning
                                          					 message waiting indicators (MWIs) on and off. Disabling this service degrades
                                          					 the ability of Unity Connection to function

Base Services

Connection DB Event Publisher

This service enables Unity Connection components to receive
                                          					 notifications for any changes made to the Unity Connection database.

Connection SRSV Administration

This service enables Cisco Unity Connection SRSV Administration
                                          					 and the settings that are saved in the interface.

Optional Services

Connection Branch Sync Service

This service enables the Survivable Remote Site Voicemail (SRSV)
                                          					 feature.

Connection CM Database Event Listener

This service enables the detection of changes in the Cisco
                                          					 Unified Communications Manager database.

Connection Database Proxy

This service allows tools that are not installed on the Unity
                                          					 Connection server (COBRAS, User Data Dump, Distribution List Builder, and so
                                          					 on) to gain direct access to the Unity Connection database via ODBC from a
                                          					 Windows client on the network.

The service is off by default. To use any of these tools, you
                                          					 must enable the service, configure the time out for the service, and create a
                                          					 user that has the remote admin role. For more information, see the help file
                                          					 for the applicable tool.

Connection Diagnostic Portal Service

This service enables access to data on Unity Connection SRSV by
                                          					 the Diagnostic Portal in the Real-Time Monitoring Tool (RTMT).

Connection Realtime Monitoring APIs

This service enables access to data on Unity Connection SRSV by
                                          					 Real-Time Monitoring Tool (RTMT).

Connection Reports Data Harvester

This service enables conversion of data in log files to entries
                                          					 in the reports database used to generate reports.

Connection REST Service

This service enables Representational State Transfer (REST) API
                                          					 clients.

Connection System Agent

This service schedules system tasks, for example,
                                          					 re-synchronizing MWIs that the administrator can enter in Cisco Unity
                                          					 Connection Administration.

## Configuring
                        	 Services in Control Center

The control center in
                              		  Cisco Unity Connection Serviceability allows you to perform the following
                              		  tasks:

Activate and deactivate Unity Connection SRSV services in the
                                    				Optional Services section.

Start and stop all Unity Connection SRSV services except the
                                    				services in the Status Only Services section.

Stopping Unity Connection SRSV services in the Critical Services
                                                				  section may cause calls in progress to be dropped and degrades the normal
                                                				  function of the Unity Connection SRSV.

View the status of Unity Connection SRSV services.

Refresh the status of Unity Connection SRSV services.

You may need to manage services in both Cisco Unity Connection
                                                				  Serviceability and Cisco Unified Serviceability to troubleshoot a problem.

In Cisco Unity Connection Serviceability, expand Tools > and select > Service
                                             				  Management .

From the Server drop-down box, select the applicable Unity
                                       			 Connection SRSV server and select Go .

Configure services in control center (For information on each
                                       			 field, see Help> This Page):

To activate a service in control center:

Under Optional Services, locate the service that you want to
                                                      						  activate.

In the Change Activate Status column, select Activate .

To deactivate a service in control center:

Under Optional Services, locate the service that you want to
                                                      						  deactivate.

In the Change Activate Status column, select Deactivate .

To start a service in control center:

Locate the service that you want to start.

Services that are
                                                                  							 deactivated must be activated before they can be started.

In the Change Service Status column, select Start .

To stop a service in control center:

Locate the service that you want to stop.

Services in the Status Only
                                                                  							 Services section cannot be started or stopped in Cisco Unity Connection
                                                                  							 Serviceability. You must use the command line interface (CLI) to start or stop
                                                                  							 these services.

In the Change Service Status column, select Stop .

Stopping Unity Connection
                                                                  							 SRSV services in the Critical Services section may cause calls in progress to
                                                                  							 be dropped and degrades the normal function of the Unity Connection SRSV.A
                                                                  							 service that is not activated cannot be started or stopped.

To refresh service status in control center:

Select Refresh .

The status information is updated to reflect the current status.

You can activate,
                                                                  							 deactivate, start, and stop only one service at a time.

| Service | Description |
|---|---|
| Status Only Services |
| Connection DB | This service activates the Cisco Unity Connection database and
                                          					 can be deactivated only using the Command Line Interface (CLI). Caution This service should always be in the Started state for the Unity
                                                      						Connection SRSV server to be functional. Stopping or restarting this service
                                                      						impacts other critical services. | Caution | This service should always be in the Started state for the Unity
                                                      						Connection SRSV server to be functional. Stopping or restarting this service
                                                      						impacts other critical services. |
| Caution | This service should always be in the Started state for the Unity
                                                      						Connection SRSV server to be functional. Stopping or restarting this service
                                                      						impacts other critical services. |
| Connection Server Role Manager | This service enables the server status when a Unity Connection
                                          					 cluster is configured and can be deactivated only using the CLI. |
| Connection Serviceability | This service enables the Cisco Unity Connection Serviceability
                                          					 Administration interface and can be deactivated only using the command-line
                                          					 interface (CLI). |
| Critical Services |
| Connection Conversation Manager | This service enables Unity Connection to handle the calls.
                                          					 Disabling this service degrades the ability of Unity Connection to function. |
| Connection Message Transfer Agent | This service enables the delivery of messages to the message
                                          					 store. Disabling this service degrades the ability of Unity Connection to
                                          					 function. |
| Connection Mixer | This service enables the audio (media stream) for calls,
                                          					 recorded messages, and Text-to-Speech (TTS). Disabling this service degrades
                                          					 the ability of Unity Connection to function. |
| Connection Notifier | This service enables notification of messages, such as turning
                                          					 message waiting indicators (MWIs) on and off. Disabling this service degrades
                                          					 the ability of Unity Connection to function |
| Base Services |
| Connection DB Event Publisher | This service enables Unity Connection components to receive
                                          					 notifications for any changes made to the Unity Connection database. |
| Connection SRSV Administration | This service enables Cisco Unity Connection SRSV Administration
                                          					 and the settings that are saved in the interface. |
| Optional Services |
| Connection Branch Sync Service | This service enables the Survivable Remote Site Voicemail (SRSV)
                                          					 feature. |
| Connection CM Database Event Listener | This service enables the detection of changes in the Cisco
                                          					 Unified Communications Manager database. |
| Connection Database Proxy | This service allows tools that are not installed on the Unity
                                          					 Connection server (COBRAS, User Data Dump, Distribution List Builder, and so
                                          					 on) to gain direct access to the Unity Connection database via ODBC from a
                                          					 Windows client on the network. The service is off by default. To use any of these tools, you
                                          					 must enable the service, configure the time out for the service, and create a
                                          					 user that has the remote admin role. For more information, see the help file
                                          					 for the applicable tool. |
| Connection Diagnostic Portal Service | This service enables access to data on Unity Connection SRSV by
                                          					 the Diagnostic Portal in the Real-Time Monitoring Tool (RTMT). |
| Connection Realtime Monitoring APIs | This service enables access to data on Unity Connection SRSV by
                                          					 Real-Time Monitoring Tool (RTMT). |
| Connection Reports Data Harvester | This service enables conversion of data in log files to entries
                                          					 in the reports database used to generate reports. |
| Connection REST Service | This service enables Representational State Transfer (REST) API
                                          					 clients. |
| Connection System Agent | This service schedules system tasks, for example,
                                          					 re-synchronizing MWIs that the administrator can enter in Cisco Unity
                                          					 Connection Administration. |

| Caution | This service should always be in the Started state for the Unity
                                                      						Connection SRSV server to be functional. Stopping or restarting this service
                                                      						impacts other critical services. |
|---|---|

| Note | Stopping Unity Connection SRSV services in the Critical Services
                                                				  section may cause calls in progress to be dropped and degrades the normal
                                                				  function of the Unity Connection SRSV. |
|---|---|

| Tip | You may need to manage services in both Cisco Unity Connection
                                                				  Serviceability and Cisco Unified Serviceability to troubleshoot a problem. |
|---|---|

| Step 1 | In Cisco Unity Connection Serviceability, expand Tools > and select > Service
                                             				  Management . |
|---|---|
| Step 2 | From the Server drop-down box, select the applicable Unity
                                       			 Connection SRSV server and select Go . |
| Step 3 | Configure services in control center (For information on each
                                       			 field, see Help> This Page): To activate a service in control center: Under Optional Services, locate the service that you want to
                                                      						  activate. In the Change Activate Status column, select Activate . To deactivate a service in control center: Under Optional Services, locate the service that you want to
                                                      						  deactivate. In the Change Activate Status column, select Deactivate . To start a service in control center: Locate the service that you want to start. Note Services that are
                                                                  							 deactivated must be activated before they can be started. In the Change Service Status column, select Start . To stop a service in control center: Locate the service that you want to stop. Note Services in the Status Only
                                                                  							 Services section cannot be started or stopped in Cisco Unity Connection
                                                                  							 Serviceability. You must use the command line interface (CLI) to start or stop
                                                                  							 these services. In the Change Service Status column, select Stop . Note Stopping Unity Connection
                                                                  							 SRSV services in the Critical Services section may cause calls in progress to
                                                                  							 be dropped and degrades the normal function of the Unity Connection SRSV.A
                                                                  							 service that is not activated cannot be started or stopped. To refresh service status in control center: Select Refresh . The status information is updated to reflect the current status. Note You can activate,
                                                                  							 deactivate, start, and stop only one service at a time. | Note | Services that are
                                                                  							 deactivated must be activated before they can be started. | Note | Services in the Status Only
                                                                  							 Services section cannot be started or stopped in Cisco Unity Connection
                                                                  							 Serviceability. You must use the command line interface (CLI) to start or stop
                                                                  							 these services. | Note | Stopping Unity Connection
                                                                  							 SRSV services in the Critical Services section may cause calls in progress to
                                                                  							 be dropped and degrades the normal function of the Unity Connection SRSV.A
                                                                  							 service that is not activated cannot be started or stopped. | Note | You can activate,
                                                                  							 deactivate, start, and stop only one service at a time. |
| Note | Services that are
                                                                  							 deactivated must be activated before they can be started. |
| Note | Services in the Status Only
                                                                  							 Services section cannot be started or stopped in Cisco Unity Connection
                                                                  							 Serviceability. You must use the command line interface (CLI) to start or stop
                                                                  							 these services. |
| Note | Stopping Unity Connection
                                                                  							 SRSV services in the Critical Services section may cause calls in progress to
                                                                  							 be dropped and degrades the normal function of the Unity Connection SRSV.A
                                                                  							 service that is not activated cannot be started or stopped. |
| Note | You can activate,
                                                                  							 deactivate, start, and stop only one service at a time. |

| Note | Services that are
                                                                  							 deactivated must be activated before they can be started. |
|---|---|

| Note | Services in the Status Only
                                                                  							 Services section cannot be started or stopped in Cisco Unity Connection
                                                                  							 Serviceability. You must use the command line interface (CLI) to start or stop
                                                                  							 these services. |
|---|---|

| Note | Stopping Unity Connection
                                                                  							 SRSV services in the Critical Services section may cause calls in progress to
                                                                  							 be dropped and degrades the normal function of the Unity Connection SRSV.A
                                                                  							 service that is not activated cannot be started or stopped. |
|---|---|

| Note | You can activate,
                                                                  							 deactivate, start, and stop only one service at a time. |
|---|---|