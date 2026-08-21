---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-connection-12x-serv-administration-b-12xcucservag-b-12xcucservag-chapter-010-f82c5d3690
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/12x/serv_administration/b_12xcucservag/b_12xcucservag_chapter_0100.html
retrieved_at: 2026-08-21T00:24:36.596679+00:00
---

Administration Guide for Cisco Unity Connection Serviceability Release 12.x

# Administration Guide for Cisco Unity Connection Serviceability Release 12.x

Updated: August 4, 2017

Chapter: Managing Cisco Unity Connection Services

## Chapter: Managing Cisco Unity Connection Services

# Managing Cisco Unity Connection Services

## Cisco Unity
                        	 Connection Services

Cisco Unity Connection has the
                              		  services described in Table 5-1 .

Service

Description

Status Only Services

Connection DB

This service enables the Unity Connection database and can be
                                          					 deactivated only using the command-line interface (CLI).

Connection Server Role Manager

This service enables the server status when a Unity Connection
                                          					 cluster is configured and can be deactivated only using the command-line
                                          					 interface (CLI).

Connection Serviceability

This service enables the Cisco Unity Connection Serviceability
                                          					 Administration interface and can be deactivated only using the command-line
                                          					 interface (CLI).

Critical Services

Connection Conversation Manager

This service enables Unity Connection to handle calls. Disabling
                                          					 this service degrades the ability of Unity Connection to function.

Connection Mailbox Sync

This service synchronizes messages between Unity Connection and
                                          					 Exchange.

Connection Message Transfer Agent

This service enables the delivery of messages to the message
                                          					 store. Disabling this service degrades the ability of Unity Connection to
                                          					 function.

Connection Mixer

This service enables the audio (media stream) for calls,
                                          					 recorded messages, and Text-to-Speech (TTS). Disabling this service degrades
                                          					 the ability of Unity Connection to function.

Connection Notifier

This service enables notification of messages, such as turning
                                          					 message waiting indicators (MWIs) on and off. Disabling this service degrades
                                          					 the ability of Unity Connection to function.

This
                                          					 service manages all the Cisco Smart Software Licensing operations on Cisco
                                          					 Unity Connection.

Base Services

Connection Administration

This service enables Cisco Unity Connection Administration and
                                          					 the settings that are saved in the interface.

Connection DB Event Publisher

This service enables notifying Unity Connection components of
                                          					 changes to the Unity Connection database.

Connection SNMP Agent

This service enables the Simple Network Management Protocol
                                          					 (SNMP) that uses the Cisco-Unity-MIB.

For more
                                          					 information on SNMP, see the " Simple Network Management
                                             						Protocol " chapter of the Cisco
                                             						Unified Serviceability Administration Guide available at http://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-callmanager/products-maintenance-guides-list.html

Optional Services

Connection Access Layer

This service enables the sharing of user data between
                                          					 Unity Connection and other servers using Cisco Unity Access Layer (CUAL), a
                                          					 HTTP/SOAP web service. For example, this service can be used by Cisco Business
                                          					 Edition or by Digital Networking with Cisco Unity.

Connection Branch Sync Service

This service enables Survivable Remote Site Voicemail (SRSV)
                                          					 feature.

Connection CM Database Event Listener

This service enables the detection of changes in the Cisco
                                          					 Unified Communications Manager database.

Connection Database Proxy

This service allows tools that are not installed on the
                                          					 Unity Connection server (COBRAS, User Data Dump, Distribution List Builder, and
                                          					 so on) to gain direct access to the Unity Connection database via ODBC from a
                                          					 Windows client on the network.

The service is disabled by default. To use any of these tools,
                                          					 you must enable the service, configure the time out for the service, and create
                                          					 a user that has the remote admin role. For more information, see the help file
                                          					 for the applicable tool.

Connection Diagnostic Portal Service

This service enables access to data on Unity Connection by the
                                          					 Diagnostic Portal in the Real-Time Monitoring Tool (RTMT).

Connection Digital Networking Replication Agent

This service enables the replication of data between
                                          					 Unity Connection servers for Digital Networking.

Connection Directory Feeder

For Intersite Networking, this service checks the local site
                                          					 change-tracking database for directory changes and responds to poll requests
                                          					 from the remote site gateway Reader task.

Connection File Syncer

This service enables the replication of files for
                                          					 Unity Connection clusters.

Connection Groupware Caching Service

This service enables Unity Connection to cache calendar data
                                          					 (from Exchange, MeetingPlace, or MeetingPlace Express servers) and to cache
                                          					 Exchange contacts.

Connection HTTPS Directory Feeder

This service checks the change-tracking database of its own and
                                          					 the associated local subtree locations for directory changes and responds to
                                          					 poll requests from the remote location Reader task.

Connection IMAP Server

This service enables access to data on Unity Connection by IMAP
                                          					 clients.

Connection Inbox RSS Feed

This service enables RSS feeds for checking voicemail from RSS
                                          					 clients.

Connection Integrated Mailbox Configuration

This service enables sharing of user data between Unity
                                          					 Connection and Cisco Unified Communications Manager.

Connection Jetty

This service enables Java web clients.

Connection Message Event Service

This service enables access to voice message data on
                                          					 Unity Connection by Cisco Unified Mobility Advantage.

Connection Personal Communication Assistant

This service enables access to data on Unity Connection by the
                                          					 Cisco Personal Communications Assistant (Cisco PCA).

Connection Realtime Monitoring APIs

This service enables access to data on Unity Connection by
                                          					 Real-Time Monitoring Tool (RTMT).

Connection Reports Data Harvester

This service enables conversion of data in log files to entries
                                          					 in the reports database, which is used to generate reports.

Connection REST Service

This service enables Representational State Transfer (REST) API
                                          					 clients.

Connection SMTP Server

This service enables access to data on Unity Connection by an
                                          					 SMTP server.

Connection SpeechView

This service enables the SpeechView feature and communicates
                                          					 with the third-party external transcription service.

Connection System Agent

This service enables schedules system tasks (such as
                                          					 re-synchronizing MWIs) that the administrator can enter in Cisco Unity
                                          					 Connection Administration.

Connection Voicemail Web Service

This service enables access to data on Unity Connection through
                                          					 Voicemail Web Service (VMWS) by Cisco Unified Communications Widgets such as
                                          					 Visual Voicemail.

Connection Voice Recognition Transport

This service enables generation and placement of dynamic
                                          					 grammars that are used by the speech-recognition engine for the voice user
                                          					 interface (VUI).

Connection Voice Recognizer

This service is the speech-recognition engine that enables voice
                                          					 recognition for the voice user interface (VUI).

## Managing Services in Control Center

Control Center in Cisco Unity Connection Serviceability lets you do the following tasks:

Activate and deactivate Unity Connection services in the Optional Services section.

Start and stop all Unity Connection services except the services in the Status Only Services section.

Stopping Unity Connection services in the Critical Services section may cause calls in progress to be dropped and degrades
                           the normal function of the Unity Connection or Cisco Business Edition server.

When a Cisco Unity Connection cluster is configured, stopping a service in the Critical Services section for the server with
                           Primary status causes the status for the servers in the cluster to change.

View the status the status of Unity Connection services.

Refresh the status of Unity Connection services.

You may need to manage services in both Cisco Unity Connection Serviceability and Cisco Unified Serviceability to troubleshoot
                                             a problem.

The Cisco Unified Serviceability services are described in the Cisco Unified Serviceability Administration Guide.

This section contains five procedures; do the applicable procedure to activate, deactivate, start, or stop Unity Connection
                           services, or to refresh the status of services. You can activate, deactivate, start, and stop only one service at a time.

### Activating a Service in Control Center

In Cisco Unity Connection Serviceability,
                                          			 select Tools > Service Management .

From the Server drop-down box, select the
                                          			 applicable Unity Connection or Cisco Business Edition server, and select Go .

Under Optional Services, locate the service
                                          			 that you want to activate.

In the Change Activate Status column, select Activate .

### Deactivating a Service in Control Center

In Cisco Unity Connection Serviceability,
                                          			 select Tools > Service Management .

From the Server drop-down box, select the
                                          			 applicable Unity Connection or Cisco Business Edition server, and select Go .

Under Optional Services, locate the service
                                          			 that you want to deactivate.

In the Change Activate Status column, select Deactivate .

### Starting a Service in Control Center

In Cisco Unity Connection Serviceability,
                                          			 select Tools > Service Management .

From the Server drop-down box, select the
                                          			 applicable Unity Connection or Cisco Business Edition server, and select Go .

Locate the service that you want to start.

Services that are deactivated must be
                                                         				  activated before they can be started.

In the Change Service Status column, select Start .

### Stopping a Service in Control Center

In Cisco Unity Connection Serviceability,
                                          			 select Tools > Service Management .

From the Server drop-down box, select the
                                          			 applicable Unity Connection or Cisco Business Edition server, and select Go .

Locate the service that you want to stop.

Services in the Status Only Services
                                                         				  section cannot be started or stopped in Cisco Unity Connection Serviceability.
                                                         				  You must use the command-line interface (CLI) to start or stop these services.

When a Unity Connection cluster is configured,
                                                         				  stopping a service in the Critical Services section for the server with Primary
                                                         				  status causes the status for the servers in the cluster to change. To prevent
                                                         				  the status change when the service is stopped, in Cisco Unity Connection
                                                         				  Administration, you must uncheck the Automatically Change Server Status When
                                                         				  the Publisher Server Fails check box on the System Settings > Advanced >
                                                         				  Cluster Configuration page.

In the Change Service Status column, select Stop .

Stopping Unity Connection services in the
                                                         				  Critical Services section may cause calls in progress to be dropped and
                                                         				  degrades the normal function of the Unity Connection or Cisco Business Edition
                                                         				  server.

A service that is not activated cannot be
                                                         				  started or stopped.

If you are prompted that the cluster server
                                          			 status changes, select OK .

### Refreshing Service Status in Control Center

In Cisco Unity Connection Serviceability,
                                          			 select Tools > Service Management .

From the Server drop-down box, select the
                                          			 applicable Unity Connection or Cisco Business Edition server, and select Go .

Select Refresh .

The status information is updated to reflect
                                             				the current status.

| Service | Description |
|---|---|
| Status Only Services |
| Connection DB | This service enables the Unity Connection database and can be
                                          					 deactivated only using the command-line interface (CLI). |
| Connection Server Role Manager | This service enables the server status when a Unity Connection
                                          					 cluster is configured and can be deactivated only using the command-line
                                          					 interface (CLI). |
| Connection Serviceability | This service enables the Cisco Unity Connection Serviceability
                                          					 Administration interface and can be deactivated only using the command-line
                                          					 interface (CLI). |
| Critical Services |
| Connection Conversation Manager | This service enables Unity Connection to handle calls. Disabling
                                          					 this service degrades the ability of Unity Connection to function. |
| Connection Mailbox Sync | This service synchronizes messages between Unity Connection and
                                          					 Exchange. |
| Connection Message Transfer Agent | This service enables the delivery of messages to the message
                                          					 store. Disabling this service degrades the ability of Unity Connection to
                                          					 function. |
| Connection Mixer | This service enables the audio (media stream) for calls,
                                          					 recorded messages, and Text-to-Speech (TTS). Disabling this service degrades
                                          					 the ability of Unity Connection to function. |
| Connection Notifier | This service enables notification of messages, such as turning
                                          					 message waiting indicators (MWIs) on and off. Disabling this service degrades
                                          					 the ability of Unity Connection to function. |
| Connection Smart License
                                       				  Manager Server | This
                                          					 service manages all the Cisco Smart Software Licensing operations on Cisco
                                          					 Unity Connection. |
| Base Services |
| Connection Administration | This service enables Cisco Unity Connection Administration and
                                          					 the settings that are saved in the interface. |
| Connection DB Event Publisher | This service enables notifying Unity Connection components of
                                          					 changes to the Unity Connection database. |
| Connection SNMP Agent | This service enables the Simple Network Management Protocol
                                          					 (SNMP) that uses the Cisco-Unity-MIB. For more
                                          					 information on SNMP, see the " Simple Network Management
                                             						Protocol " chapter of the Cisco
                                             						Unified Serviceability Administration Guide available at http://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-callmanager/products-maintenance-guides-list.html |
| Optional Services |
| Connection Access Layer | This service enables the sharing of user data between
                                          					 Unity Connection and other servers using Cisco Unity Access Layer (CUAL), a
                                          					 HTTP/SOAP web service. For example, this service can be used by Cisco Business
                                          					 Edition or by Digital Networking with Cisco Unity. |
| Connection Branch Sync Service | This service enables Survivable Remote Site Voicemail (SRSV)
                                          					 feature. |
| Connection CM Database Event Listener | This service enables the detection of changes in the Cisco
                                          					 Unified Communications Manager database. |
| Connection Database Proxy | This service allows tools that are not installed on the
                                          					 Unity Connection server (COBRAS, User Data Dump, Distribution List Builder, and
                                          					 so on) to gain direct access to the Unity Connection database via ODBC from a
                                          					 Windows client on the network. The service is disabled by default. To use any of these tools,
                                          					 you must enable the service, configure the time out for the service, and create
                                          					 a user that has the remote admin role. For more information, see the help file
                                          					 for the applicable tool. |
| Connection Diagnostic Portal Service | This service enables access to data on Unity Connection by the
                                          					 Diagnostic Portal in the Real-Time Monitoring Tool (RTMT). |
| Connection Digital Networking Replication Agent | This service enables the replication of data between
                                          					 Unity Connection servers for Digital Networking. |
| Connection Directory Feeder | For Intersite Networking, this service checks the local site
                                          					 change-tracking database for directory changes and responds to poll requests
                                          					 from the remote site gateway Reader task. |
| Connection File Syncer | This service enables the replication of files for
                                          					 Unity Connection clusters. |
| Connection Groupware Caching Service | This service enables Unity Connection to cache calendar data
                                          					 (from Exchange, MeetingPlace, or MeetingPlace Express servers) and to cache
                                          					 Exchange contacts. |
| Connection HTTPS Directory Feeder | This service checks the change-tracking database of its own and
                                          					 the associated local subtree locations for directory changes and responds to
                                          					 poll requests from the remote location Reader task. |
| Connection IMAP Server | This service enables access to data on Unity Connection by IMAP
                                          					 clients. |
| Connection Inbox RSS Feed | This service enables RSS feeds for checking voicemail from RSS
                                          					 clients. |
| Connection Integrated Mailbox Configuration | This service enables sharing of user data between Unity
                                          					 Connection and Cisco Unified Communications Manager. |
| Connection Jetty | This service enables Java web clients. |
| Connection Message Event Service | This service enables access to voice message data on
                                          					 Unity Connection by Cisco Unified Mobility Advantage. |
| Connection Personal Communication Assistant | This service enables access to data on Unity Connection by the
                                          					 Cisco Personal Communications Assistant (Cisco PCA). |
| Connection Realtime Monitoring APIs | This service enables access to data on Unity Connection by
                                          					 Real-Time Monitoring Tool (RTMT). |
| Connection Reports Data Harvester | This service enables conversion of data in log files to entries
                                          					 in the reports database, which is used to generate reports. |
| Connection REST Service | This service enables Representational State Transfer (REST) API
                                          					 clients. |
| Connection SMTP Server | This service enables access to data on Unity Connection by an
                                          					 SMTP server. |
| Connection SpeechView | This service enables the SpeechView feature and communicates
                                          					 with the third-party external transcription service. |
| Connection System Agent | This service enables schedules system tasks (such as
                                          					 re-synchronizing MWIs) that the administrator can enter in Cisco Unity
                                          					 Connection Administration. |
| Connection Voicemail Web Service | This service enables access to data on Unity Connection through
                                          					 Voicemail Web Service (VMWS) by Cisco Unified Communications Widgets such as
                                          					 Visual Voicemail. |
| Connection Voice Recognition Transport | This service enables generation and placement of dynamic
                                          					 grammars that are used by the speech-recognition engine for the voice user
                                          					 interface (VUI). |
| Connection Voice Recognizer | This service is the speech-recognition engine that enables voice
                                          					 recognition for the voice user interface (VUI). |

| Tip | You may need to manage services in both Cisco Unity Connection Serviceability and Cisco Unified Serviceability to troubleshoot
                                             a problem. |
|---|---|

| Tip | The Cisco Unified Serviceability services are described in the Cisco Unified Serviceability Administration Guide. |
|---|---|

| Step 1 | In Cisco Unity Connection Serviceability,
                                          			 select Tools > Service Management . |
|---|---|
| Step 2 | From the Server drop-down box, select the
                                          			 applicable Unity Connection or Cisco Business Edition server, and select Go . |
| Step 3 | Under Optional Services, locate the service
                                          			 that you want to activate. |
| Step 4 | In the Change Activate Status column, select Activate . |

| Step 1 | In Cisco Unity Connection Serviceability,
                                          			 select Tools > Service Management . |
|---|---|
| Step 2 | From the Server drop-down box, select the
                                          			 applicable Unity Connection or Cisco Business Edition server, and select Go . |
| Step 3 | Under Optional Services, locate the service
                                          			 that you want to deactivate. |
| Step 4 | In the Change Activate Status column, select Deactivate . |

| Step 1 | In Cisco Unity Connection Serviceability,
                                          			 select Tools > Service Management . |
|---|---|
| Step 2 | From the Server drop-down box, select the
                                          			 applicable Unity Connection or Cisco Business Edition server, and select Go . |
| Step 3 | Locate the service that you want to start. Note Services that are deactivated must be
                                                         				  activated before they can be started. | Note | Services that are deactivated must be
                                                         				  activated before they can be started. |
| Note | Services that are deactivated must be
                                                         				  activated before they can be started. |
| Step 4 | In the Change Service Status column, select Start . |

| Note | Services that are deactivated must be
                                                         				  activated before they can be started. |
|---|---|

| Step 1 | In Cisco Unity Connection Serviceability,
                                          			 select Tools > Service Management . |
|---|---|
| Step 2 | From the Server drop-down box, select the
                                          			 applicable Unity Connection or Cisco Business Edition server, and select Go . |
| Step 3 | Locate the service that you want to stop. Note Services in the Status Only Services
                                                         				  section cannot be started or stopped in Cisco Unity Connection Serviceability.
                                                         				  You must use the command-line interface (CLI) to start or stop these services. When a Unity Connection cluster is configured,
                                                         				  stopping a service in the Critical Services section for the server with Primary
                                                         				  status causes the status for the servers in the cluster to change. To prevent
                                                         				  the status change when the service is stopped, in Cisco Unity Connection
                                                         				  Administration, you must uncheck the Automatically Change Server Status When
                                                         				  the Publisher Server Fails check box on the System Settings > Advanced >
                                                         				  Cluster Configuration page. | Note | Services in the Status Only Services
                                                         				  section cannot be started or stopped in Cisco Unity Connection Serviceability.
                                                         				  You must use the command-line interface (CLI) to start or stop these services. When a Unity Connection cluster is configured,
                                                         				  stopping a service in the Critical Services section for the server with Primary
                                                         				  status causes the status for the servers in the cluster to change. To prevent
                                                         				  the status change when the service is stopped, in Cisco Unity Connection
                                                         				  Administration, you must uncheck the Automatically Change Server Status When
                                                         				  the Publisher Server Fails check box on the System Settings > Advanced >
                                                         				  Cluster Configuration page. |
| Note | Services in the Status Only Services
                                                         				  section cannot be started or stopped in Cisco Unity Connection Serviceability.
                                                         				  You must use the command-line interface (CLI) to start or stop these services. When a Unity Connection cluster is configured,
                                                         				  stopping a service in the Critical Services section for the server with Primary
                                                         				  status causes the status for the servers in the cluster to change. To prevent
                                                         				  the status change when the service is stopped, in Cisco Unity Connection
                                                         				  Administration, you must uncheck the Automatically Change Server Status When
                                                         				  the Publisher Server Fails check box on the System Settings > Advanced >
                                                         				  Cluster Configuration page. |
| Step 4 | In the Change Service Status column, select Stop . Note Stopping Unity Connection services in the
                                                         				  Critical Services section may cause calls in progress to be dropped and
                                                         				  degrades the normal function of the Unity Connection or Cisco Business Edition
                                                         				  server. A service that is not activated cannot be
                                                         				  started or stopped. | Note | Stopping Unity Connection services in the
                                                         				  Critical Services section may cause calls in progress to be dropped and
                                                         				  degrades the normal function of the Unity Connection or Cisco Business Edition
                                                         				  server. A service that is not activated cannot be
                                                         				  started or stopped. |
| Note | Stopping Unity Connection services in the
                                                         				  Critical Services section may cause calls in progress to be dropped and
                                                         				  degrades the normal function of the Unity Connection or Cisco Business Edition
                                                         				  server. A service that is not activated cannot be
                                                         				  started or stopped. |
| Step 5 | If you are prompted that the cluster server
                                          			 status changes, select OK . |

| Note | Services in the Status Only Services
                                                         				  section cannot be started or stopped in Cisco Unity Connection Serviceability.
                                                         				  You must use the command-line interface (CLI) to start or stop these services. When a Unity Connection cluster is configured,
                                                         				  stopping a service in the Critical Services section for the server with Primary
                                                         				  status causes the status for the servers in the cluster to change. To prevent
                                                         				  the status change when the service is stopped, in Cisco Unity Connection
                                                         				  Administration, you must uncheck the Automatically Change Server Status When
                                                         				  the Publisher Server Fails check box on the System Settings > Advanced >
                                                         				  Cluster Configuration page. |
|---|---|

| Note | Stopping Unity Connection services in the
                                                         				  Critical Services section may cause calls in progress to be dropped and
                                                         				  degrades the normal function of the Unity Connection or Cisco Business Edition
                                                         				  server. A service that is not activated cannot be
                                                         				  started or stopped. |
|---|---|

| Step 1 | In Cisco Unity Connection Serviceability,
                                          			 select Tools > Service Management . |
|---|---|
| Step 2 | From the Server drop-down box, select the
                                          			 applicable Unity Connection or Cisco Business Edition server, and select Go . |
| Step 3 | Select Refresh . The status information is updated to reflect
                                             				the current status. |