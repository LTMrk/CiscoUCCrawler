---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-connection-12x-serv-administration-b-12xcucservag-b-12xcucservag-chapter-010-14460fa2c5
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/12x/serv_administration/b_12xcucservag/b_12xcucservag_chapter_010.html
retrieved_at: 2026-08-21T00:22:09.353072+00:00
---

Administration Guide for Cisco Unity Connection Serviceability Release 12.x

# Administration Guide for Cisco Unity Connection Serviceability Release 12.x

Updated: August 4, 2017

Chapter: Using Traces

## Chapter: Using Traces

# Using Traces

Using Traces

## Understanding
                        	 Traces

Cisco Unity Connection Serviceability
                           		traces help troubleshoot problems in the following ways:

You can specify the log file parameters for each Unity
                                 			 Connection component, including the maximum number of log files and the maximum
                                 			 file size that can be created when you run traces for a component.

You can enable micro traces and the level of micro-trace
                                 			 information that you want.

You can enable macro traces (preselected groups of micro traces)
                                 			 and the level of macro-trace information that you want.

After you have configured the log files and enabled the traces,
                           		you collect trace log files in one of the following ways:

Using the trace and log central option in the Real-Time
                                 			 Monitoring Tool (RTMT). For information, see the “Working with Trace and Log
                                 			 Central” chapter (in the “Tools for Traces, Logs, and Plug-Ins” part) of the
                                 			 Cisco Unified Real-Time Monitoring Tool Administration Guide at http://www.cisco.com/en/US/products/ps6509/prod_maintenance_guides_list.html .

Using the command line interface (CLI). For information, see the Command Line Interface Reference Guide for Cisco Unified
                                    				Communications Solutions at http://www.cisco.com/en/US/products/ps6509/prod_maintenance_guides_list.html .

Enabling macro or micro traces decreases system performance.
                                             				Enable traces only for troubleshooting purposes.

## Configuring Trace
                        	 Log Files

In Cisco Unity Connection Serviceability, select Trace > Configuration . The Trace Configuration page appears.

In the Server drop-down box, select the applicable Unity
                                 			 Connection or Cisco Business Edition server, and select Go .

From the Component drop-down box, select the component for which
                                 			 you want to configure trace log files, and select Go .

The drop-down box displays all components (active and inactive).

In the Maximum No. of Files field, enter the maximum number of
                                 			 trace log files that is created for this component.

In the Maximum File Size field, enter the size limit (in
                                 			 megabytes) for the trace log files that is created for this component.

If you want to return to the default settlings, select Set Default . Otherwise, skip to the next step.

Select Save .

If you want the new trace log files to replace the old trace log
                                 			 files for this component, select Restart Log Files .

## Enabling Micro Traces

Enable
                              		  micro traces when you are troubleshooting problems with specific Cisco Unity
                              		  Connection components. For example, if the Alert Central tool in Real-Time
                              		  Monitoring Tool (RTMT) has notification errors, enable the Notifier trace.
                              		  However, keep in mind that running traces can affect system performance and
                              		  hard-disk space.

Enabling micro traces decreases system
                                          			 performance. Enable traces only for troubleshooting purposes.

In Cisco Unity Connection Serviceability,
                                       			 select Trace > Micro Traces .

The Micro Traces page appears.

In the Server drop-down box, select the
                                       			 applicable Unity Connection or Cisco Business Edition server, and select Go .

From the Micro Trace drop-down box, select
                                       			 the micro trace that you want to enable, and select Go .

Under Micro-Trace Levels, check the check
                                       			 boxes for the micro-trace levels that you want to enable.

Select Save .

You may need to enable traces in
                                                      				  Cisco Unity Connection Serviceability and Cisco Unified Serviceability to
                                                      				  troubleshoot Unity Connection issues. To troubleshoot Unity Connection
                                                      				  components, enable traces in Cisco Unity Connection Serviceability. Similarly,
                                                      				  to troubleshoot services that are supported in Cisco Unified Serviceability,
                                                      				  enable traces in Cisco Unified Serviceability. For information on how to enable
                                                      				  traces in Cisco Unified Serviceability, see the Cisco Unified Serviceability
                                                      				  Administration Guide at http://www.cisco.com/en/US/products/ps6509/prod_maintenance_guides_list.html .

## Available Micro
                        	 Traces

The Table 3-1 lists each
                              		  micro trace that is available, a description of what it analyzes, and the
                              		  filename of the trace log that it generates.

Micro Trace Name

What the Trace Analyzes

Filename of Trace Log

Arbiter

Conversations, ports, and call routing rules that are used for
                                          					 calls

diag_CuCsMgr_*.uc

AudioStore

The audio recording service used by web-based applications that
                                          					 use Media Player to playback or record audio streams

diag_Tomcat_*.uc

AxlAccess

Interaction with the AXL server to get and set phone-related
                                          					 properties

diag_Tomcat_*.uc

BulkAdministrationTool

Bulk Administration Tool that is used for creating, updating,
                                          					 and deleting multiple users or system contacts

diag_Tomcat_*.uc

CCL

The retrieval of meeting information for the calendaring feature

diag_CuCsMgr_*.uc

diag_CuGalSvc_*.uc

diag_Tomcat_*.uc

CDE

Conversation engine and conversation events

diag_CuCsMgr_*.uc

CDL

Information retrieval from the database

diag_CuCsMgr_*.uc

diag_Tomcat_*.uc

CiscoPCA

The Cisco Personal Communications Assistant (Cisco PCA)

diag_Tomcat_*.uc

CML

The retrieval of messages from the Cisco Unity Connection
                                          					 message store; the retrieval of messages from an Exchange server (using IMAP)
                                          					 for using Text-to-Speech feature to read email messages

diag_CuCsMgr_*.uc

diag_CuNotifier_*.uc

diag_Tomcat_*.uc

Common

Low-level activities for components that are shared by
                                          					 Cisco Unity Connection services

<any>

ConfigData

Detection that configuration data has been updated in the
                                          					 database

<any>

ConvRoutingRules

The conversation to which the Arbiter routes calls

diag_CuCsMgr_*.uc

ConvSub

User activities and usage

diag_CuCsMgr_*.uc

CsEws

Exchange Web Services calls from Unity Connection to Exchange
                                          					 for single inbox, calendaring, and text-to-speech

diag_CuCsMgr_*.uc

diag_CuMbxSync_*.uc

CsExchangeMbxLocator

Autodiscovery of Exchange mailboxes for single inbox,
                                          					 calendaring, and text-to-speech

diag_CuCsMgr_*.uc

diag_CuMbxSync_*.uc

CsMalUmss

Access to the message store by the CML, Notifier, and IMAP
                                          					 server

diag_CuCsMgr_*.uc

diag_Tomcat_*.uc

CsMbxSync

Single inbox synchronization

diag_CuMbxSync_*.uc

CsWebDav

Calendar activities in connection with Exchange

diag_CuCsMgr_*.uc

diag_CuGalSvc_*.uc

diag_Tomcat_*.uc

Cuals

The activities of the web services to add users

diag_Tomcat_*.uc

Cuca

The activities of Cisco Unity Connection Administration

diag_Tomcat_*.uc

CuCESync

Activity related with Survival Remote Site Voicemail (SRSV)
                                          					 processing.

diag_CUCESync_*.uc

CuCcmSynchronizationTasks

Synchronization of the user data from Cisco Unified CM

diag_Tomcat_*.uc

CuCmDbEventListener

Detection of changes in the Cisco Unified CM database

diag_CuCmDbEventListener_*.uc

CuCsMgr

Main Cisco Unity Connection process; starting and stopping Unity
                                          					 Connection

diag_CuCsMgr_*.uc

CuDbProxy

Database replication for Cisco Unity Connection clusters

diag_CuDbProxy_*.uc

CuEncrypt

Encryption (except for messaging) and the encryption audit logs

<any>

CuESD

The activities of Unity Connection external service diagnostic
                                          					 tools

diag_Tomcat_*.uc

CuFileSync

File replication for Unity Connection clusters

diag_CuFileSync_*.uc

CuGal

The retrieval of calendar and contact information from Exchange

diag_CuGalSvc_*.uc

CuImapSvr

Access to voice messages by IMAP clients

diag_CuImapSvr_*.uc

CuReplicator

Replication for digital networking

We recommend that the Debug Traces and Debug Statistics
                                                      						micro-trace levels be enabled for no more than one hour because they can
                                                      						produce a large number of log entries.

diag_CuReplicator_*.uc

CuService

The activities of Cisco Unity Connection Serviceability

diag_Tomcat_*.uc

CuSnmpAgt

The activities of the Connection SNMP subagent

diag_CuSnmpAgt_*.uc

DataSysAgentTasks

Data SysAgent tasks

diag_CuSysAgent_*.uc

DbEvent

Component notification of database changes

<any>

DPAPI

The activities of the diagnostic portal application programming
                                          					 interface web service

diag_Tomcat_*.uc

EWSNotify

Exchange EWS mailbox synchronization notifications

<date in the format yyyy_mm_dd>.stderrout.log.*

FailureConv

Activation of the Failure Conversation when a system error
                                          					 occurs

diag_CuCsMgr_*.uc

Feeder

In Intersite Networking, this micro trace checks the local site
                                          					 change-tracking database for directory changes and responds to poll requests
                                          					 from the remote site gateway Reader task

In HTTPS Networking, this micro trace checks the change-tracking
                                          					 database of local subtree in Feeder for directory changes and responds to poll
                                          					 requests from the remote location Reader task.

diag_Tomcat_*.uc

FeedReader

In Intersite Networking, this microtrace periodically polls the
                                          					 remote site gateway for any directory changes since the last poll interval.

In HTTPS Networking, this microtrace periodically polls the
                                          					 remote location for any directory changes since the last poll interval.

diag_Tomcat_*.uc

LicenseClient

Functions related to license management

diag_CuCsMgr_*.uc

Logger

Writing traces logs and events

<any>

MessageEventService

Detection of arrival or deletion of messages

diag_Tomcat_*.uc

MiuAdm

Functions in Cisco Unity Connection Administration relating to
                                          					 testing voice messaging ports and generating certificates

diag_Tomcat_*.uc

MiuCall

The process between the Miu and conversations

diag_CuCsMgr_*.uc

MiuDatatbase

Media activities relating to accessing the database

diag_CuCsMgr_*.uc

MiuGeneral

Tracking calls through the phone user interface (TUI); call
                                          					 control functions; turning message waiting indicators (MWIs) on and off;
                                          					 notification and outdial functions; basic media or WAV file usage

diag_CuCsMgr_*.uc

MiuIO

Media or WAV file usage with TAPI (circuit-switched or Cisco
                                          					 Unified CallManager) integrations

diag_CuCsMgr_*.uc

MiuMethods

Handing of incoming calls; call control; turning messaging
                                          					 waiting indicators (MWIs) on and off; notification and outdial functions; media
                                          					 or WAV file usage

diag_CuCsMgr_*.uc

MiuSIP

SIP call control

diag_CuCsMgr_*.uc

MiuSIPStack

Low-level SIP interactions for call control

diag_CuCsMgr_*.uc

MiuSkinny

SCCP call control

diag_CuCsMgr_*.uc

MiuTranscode

Low-level media functions relating to transcoding

diag_CuCsMgr_*.uc

Mixer

Low-level activities relating to media and the Text-to-Speech
                                          					 feature

diag_CuMixer_*.uc

Monitor

Monitoring the status of voice messaging ports and call
                                          					 processing during a call; the server-side functions for displaying port status
                                          					 in Real-Time Monitoring Tool

diag_CuCsMgr_*.uc

MTA

Delivery of voice messages to the message store

diag_MTA_*.uc

Notifier

Notification of messages and selected events; turning message
                                          					 waiting indicators (MWIs) on and off

diag_CuCsMgr_*.uc

diag_CuNotifier_*.uc

PCAMeetingPlace

Activities of the Cisco Personal Communications Assistant
                                          					 relating to MeetingPlace for the calendar feature

diag_Tomcat_*.u

PCAUnifiedCM

Activities of the Cisco Personal Communications Assistant
                                          					 relating to the Cisco Unified Communications Manager integration

diag_Tomcat_*.uc

PhoneManager

The management of IP phone applications

diag_CuCsMgr_*.uc

PhraseServer

The prompts that play and the user DTMF input; the logs are
                                          					 written to a file

diag_CuCsMgr_*.uc

PhraseServerToMonitor

The prompts that play and the user DTMF input; the logs are
                                          					 written to the monitor

diag_CuCsMgr_*.uc

ReportDataHarvester

Conversion of the content in the data log files to entries in
                                          					 the reports database

diag_CuReportDataHarvester_*.uc

ResourceLoader

Using the selected language in the GUI; filling strings with
                                          					 product or message information

<any>

ResourceManager

Monitoring and providing available resources to the Arbiter as
                                          					 needed

diag_CuCsMgr_*.uc

RoutingRules

Call routing decisions

diag_CuCsMgr_*.uc

RSS

RSS feeds that are used for checking voicemail from an RSS
                                          					 client

diag_Tomcat_*.uc

RulesEngine

Evaluation of personal call transfer rules for a user during a
                                          					 call

diag_CuCsMgr_*.uc

diag_Tomcat_*.uc

SMTP

SMTP functions

diag_SMTP_*.uc

SocketPoolHelper

Socket connections to the IMAP server

<any>

SRM

Functions related to cluster management

diag_CuSrm_*.uc

SslInit

Initialization procedures for components that use OpenSSL

<any>

SttClient

Detects messages that need to be transcribed; attaches completed
                                          					 transcriptions to original messages

diag_MTA_*.uc

SttService

Communication between Cisco Unity Connection and the third-party
                                          					 external transcription service

diag_SttService_*.uc

SysAgent

System Agent component, which schedules system tasks that the
                                          					 administrator enters (such as resynchronizing MWIs)

diag_CuSysAgent_*.uc

TaskRequest

Functions related to the Task Management tool

diag_CuSysAgent_*.uc

TextToSpeech

The activities of the Text to Speech feature

diag_CuCsMgr_*.uc

ThreadPool

The use of threads by the processor

<any>

TimerHelper

The timer used by the Conversation Manager component

<any>

TranscodeWeb

The web server audio format transcoding utilities that transcode
                                          					 the incoming audio streams into the audio format that Cisco Unity Connection
                                          					 uses

diag_Tomcat_*.uc

TRaP

Phone Record and Playback (TRaP), which lets clients use the
                                          					 phone as a recording and playback device

diag_CuCsMgr_*.uc

diag_Tomcat_*.uc

UmssSysAgentTasks

Messaging tasks for the System Agent component

diag_CuSysAgent_*.uc

UnityAssistant

The activities of the Messaging Assistant web tool in the
                                          					 Cisco Personal Communications Assistant

diag_Tomcat_*.uc

UnityInbox

The activities of the Messaging Inbox web tool in the
                                          					 Cisco Personal Communications Assistant

diag_Tomcat_*.uc

UnityPCTR

The activities of the Cisco Unity Connection Personal Call
                                          					 Transfer Rules web tool in the Cisco Personal Communications Assistant

diag_CuCsMgr_*.uc

Video

The activities of Video call between Unity Connection and Cisco
                                          					 MediaSense through APIs.

diag_CuCsMgr_*.uc

VirtualQueue

Call queuing

diag_CuCsMgr_*.uc

VMREST

Interactions with Representational State Transfer (REST) API
                                          					 clients

diag_Tomcat_*.uc

VMWS

Interactions with voice messaging web services

diag_Tomcat_*.uc

VUI

The voice user interface

diag_CuCsMgr_*.uc

## Enabling Macro
                        	 Traces

Enable macro traces, which are
                              		  preselected sets of micro traces, when you are troubleshooting general areas of
                              		  Unity Connection functionality. For example, if there are MWI problems, enable
                              		  the Traces for MWI Problems macro trace. However, keep in mind that running
                              		  traces can affect system performance and hard-disk space.

Enabling macro traces decreases system performance. Enable
                                          			 traces only for troubleshooting purposes.

In Cisco Unity Connection Serviceability, select Trace > Macro
                                             				  Traces .

The Macro Traces page appears.

In the Server drop-down box, select the applicable Unity
                                       			 Connection or Cisco Business Edition server, and select Go .

Check the check box of the macro trace that you want to enable.

Expand the macro trace, and check the check boxes for the levels
                                       			 that you want to enable.

Select Save .

You may need to enable traces in Cisco Unity Connection
                                                      				  Serviceability and Cisco Unified Serviceability to troubleshoot Unity
                                                      				  Connection issues. To troubleshoot Unity Connection components, enable traces
                                                      				  in Cisco Unity Connection Serviceability. Similarly, to troubleshoot services
                                                      				  that are supported in Cisco Unified Serviceability, enable traces in Cisco
                                                      				  Unified Serviceability. For information on how to enable traces in Cisco
                                                      				  Unified Serviceability, see the Cisco Unified Serviceability Administration
                                                      				  Guide at http://www.cisco.com/en/US/products/ps6509/prod_maintenance_guides_list.html .

## Available Macro
                        	 Traces

Table 2 lists each macro trace that is available, a description of what it analyzes,
                           		and the filename of the trace log that it generates.

Macro Trace Name

What the Trace Analyzes

Filename of Trace Log

Call Flow Diagnostics

The flow of a call through Unity Connection

diag_CuCsMgr_*.uc

Message Tracking Traces

Message handing; the objects that handle messages from delivery
                                       				  to deletion

diag_CuSysAgent_*.uc

diag_MTA_*.uc

diag_CuCsMgr_*.uc

diag_CuImapSvr_*.uc

diag_Tomcat_*.uc

Call Control (Miu) Traces

Call control functions

diag_CuCsMgr_*.uc

Traces for MWI Problems

Turning message waiting indicators (MWIs) on and off

diag_CuCsMgr_*.uc

diag_CuNotifier_*.uc

Traces for Other Notification Problems

Notification and outdial functions

diag_CuCsMgr_*.uc

diag_CuNotifier_*.uc

Unity Startup

Unity Connection startup functions

diag_CuCsMgr_*.uc

diag_CuNotifier_*.uc

Conversation Traces

Conversation usage

diag_CuCsMgr_*.uc

Voice User Interface/Speech Recognition Traces

Voice user interface (VUI)

diag_CuCsMgr_*.uc

Media (Wave) Traces

Media and WAV file usage

diag_CuCsMgr_*.uc

diag_CuMixer_*.uc

Text to Speech (TTS) Traces

The Text to Speech (TTS) feature; also can log traces on other
                                       				  Cisco Unity Connection components that interact with TTS

diag_CuCsMgr_*.uc

Unity Connection Serviceability Web Service

The activity of Cisco Unified Serviceability

diag_Tomcat_*.uc

ViewMail for Outlook

The activity of Cisco Unity Connection ViewMail for Microsoft
                                       				  Outlook clients

diag_CuCsMgr_*.uc

diag_CuImapSvr_*.uc

diag_MTA_*.uc

diag_Tomcat_*.uc

Digital Networking

Digital networking functions

diag_CuReplicator_*.uc

Single Inbox

Single inbox message synchronization

<date in the format
                                       				  yyyy_mm_dd>.stderrout. log.* diag_CuMbxSync_*.uc

| Note | Enabling macro or micro traces decreases system performance.
                                             				Enable traces only for troubleshooting purposes. |
|---|---|

| Note | Before trace
                                    		information can be written to the log files, you must enable micro traces or
                                    		macro traces that provide the troubleshooting information in the areas that you
                                    		select. |
|---|---|

| Note | Enabling micro traces decreases system
                                          			 performance. Enable traces only for troubleshooting purposes. |
|---|---|

| Step 1 | In Cisco Unity Connection Serviceability,
                                       			 select Trace > Micro Traces . The Micro Traces page appears. |
|---|---|
| Step 2 | In the Server drop-down box, select the
                                       			 applicable Unity Connection or Cisco Business Edition server, and select Go . |
| Step 3 | From the Micro Trace drop-down box, select
                                       			 the micro trace that you want to enable, and select Go . |
| Step 4 | Under Micro-Trace Levels, check the check
                                       			 boxes for the micro-trace levels that you want to enable. |
| Step 5 | Select Save . Tip You may need to enable traces in
                                                      				  Cisco Unity Connection Serviceability and Cisco Unified Serviceability to
                                                      				  troubleshoot Unity Connection issues. To troubleshoot Unity Connection
                                                      				  components, enable traces in Cisco Unity Connection Serviceability. Similarly,
                                                      				  to troubleshoot services that are supported in Cisco Unified Serviceability,
                                                      				  enable traces in Cisco Unified Serviceability. For information on how to enable
                                                      				  traces in Cisco Unified Serviceability, see the Cisco Unified Serviceability
                                                      				  Administration Guide at http://www.cisco.com/en/US/products/ps6509/prod_maintenance_guides_list.html . | Tip | You may need to enable traces in
                                                      				  Cisco Unity Connection Serviceability and Cisco Unified Serviceability to
                                                      				  troubleshoot Unity Connection issues. To troubleshoot Unity Connection
                                                      				  components, enable traces in Cisco Unity Connection Serviceability. Similarly,
                                                      				  to troubleshoot services that are supported in Cisco Unified Serviceability,
                                                      				  enable traces in Cisco Unified Serviceability. For information on how to enable
                                                      				  traces in Cisco Unified Serviceability, see the Cisco Unified Serviceability
                                                      				  Administration Guide at http://www.cisco.com/en/US/products/ps6509/prod_maintenance_guides_list.html . |
| Tip | You may need to enable traces in
                                                      				  Cisco Unity Connection Serviceability and Cisco Unified Serviceability to
                                                      				  troubleshoot Unity Connection issues. To troubleshoot Unity Connection
                                                      				  components, enable traces in Cisco Unity Connection Serviceability. Similarly,
                                                      				  to troubleshoot services that are supported in Cisco Unified Serviceability,
                                                      				  enable traces in Cisco Unified Serviceability. For information on how to enable
                                                      				  traces in Cisco Unified Serviceability, see the Cisco Unified Serviceability
                                                      				  Administration Guide at http://www.cisco.com/en/US/products/ps6509/prod_maintenance_guides_list.html . |

| Tip | You may need to enable traces in
                                                      				  Cisco Unity Connection Serviceability and Cisco Unified Serviceability to
                                                      				  troubleshoot Unity Connection issues. To troubleshoot Unity Connection
                                                      				  components, enable traces in Cisco Unity Connection Serviceability. Similarly,
                                                      				  to troubleshoot services that are supported in Cisco Unified Serviceability,
                                                      				  enable traces in Cisco Unified Serviceability. For information on how to enable
                                                      				  traces in Cisco Unified Serviceability, see the Cisco Unified Serviceability
                                                      				  Administration Guide at http://www.cisco.com/en/US/products/ps6509/prod_maintenance_guides_list.html . |
|---|---|

| Micro Trace Name | What the Trace Analyzes | Filename of Trace Log |
|---|---|---|
| Arbiter | Conversations, ports, and call routing rules that are used for
                                          					 calls | diag_CuCsMgr_*.uc |
| AudioStore | The audio recording service used by web-based applications that
                                          					 use Media Player to playback or record audio streams | diag_Tomcat_*.uc |
| AxlAccess | Interaction with the AXL server to get and set phone-related
                                          					 properties | diag_Tomcat_*.uc |
| BulkAdministrationTool | Bulk Administration Tool that is used for creating, updating,
                                          					 and deleting multiple users or system contacts | diag_Tomcat_*.uc |
| CCL | The retrieval of meeting information for the calendaring feature | diag_CuCsMgr_*.uc diag_CuGalSvc_*.uc diag_Tomcat_*.uc |
| CDE | Conversation engine and conversation events | diag_CuCsMgr_*.uc |
| CDL | Information retrieval from the database | diag_CuCsMgr_*.uc diag_Tomcat_*.uc |
| CiscoPCA | The Cisco Personal Communications Assistant (Cisco PCA) | diag_Tomcat_*.uc |
| CML | The retrieval of messages from the Cisco Unity Connection
                                          					 message store; the retrieval of messages from an Exchange server (using IMAP)
                                          					 for using Text-to-Speech feature to read email messages | diag_CuCsMgr_*.uc diag_CuNotifier_*.uc diag_Tomcat_*.uc |
| Common | Low-level activities for components that are shared by
                                          					 Cisco Unity Connection services | <any> |
| ConfigData | Detection that configuration data has been updated in the
                                          					 database | <any> |
| ConvRoutingRules | The conversation to which the Arbiter routes calls | diag_CuCsMgr_*.uc |
| ConvSub | User activities and usage | diag_CuCsMgr_*.uc |
| CsEws | Exchange Web Services calls from Unity Connection to Exchange
                                          					 for single inbox, calendaring, and text-to-speech | diag_CuCsMgr_*.uc diag_CuMbxSync_*.uc |
| CsExchangeMbxLocator | Autodiscovery of Exchange mailboxes for single inbox,
                                          					 calendaring, and text-to-speech | diag_CuCsMgr_*.uc diag_CuMbxSync_*.uc |
| CsMalUmss | Access to the message store by the CML, Notifier, and IMAP
                                          					 server | diag_CuCsMgr_*.uc diag_Tomcat_*.uc |
| CsMbxSync | Single inbox synchronization | diag_CuMbxSync_*.uc |
| CsWebDav | Calendar activities in connection with Exchange | diag_CuCsMgr_*.uc diag_CuGalSvc_*.uc diag_Tomcat_*.uc |
| Cuals | The activities of the web services to add users | diag_Tomcat_*.uc |
| Cuca | The activities of Cisco Unity Connection Administration | diag_Tomcat_*.uc |
| CuCESync | Activity related with Survival Remote Site Voicemail (SRSV)
                                          					 processing. | diag_CUCESync_*.uc |
| CuCcmSynchronizationTasks | Synchronization of the user data from Cisco Unified CM | diag_Tomcat_*.uc |
| CuCmDbEventListener | Detection of changes in the Cisco Unified CM database | diag_CuCmDbEventListener_*.uc |
| CuCsMgr | Main Cisco Unity Connection process; starting and stopping Unity
                                          					 Connection | diag_CuCsMgr_*.uc |
| CuDbProxy | Database replication for Cisco Unity Connection clusters | diag_CuDbProxy_*.uc |
| CuEncrypt | Encryption (except for messaging) and the encryption audit logs | <any> |
| CuESD | The activities of Unity Connection external service diagnostic
                                          					 tools | diag_Tomcat_*.uc |
| CuFileSync | File replication for Unity Connection clusters | diag_CuFileSync_*.uc |
| CuGal | The retrieval of calendar and contact information from Exchange | diag_CuGalSvc_*.uc |
| CuImapSvr | Access to voice messages by IMAP clients | diag_CuImapSvr_*.uc |
| CuReplicator | Replication for digital networking Note We recommend that the Debug Traces and Debug Statistics
                                                      						micro-trace levels be enabled for no more than one hour because they can
                                                      						produce a large number of log entries. | Note | We recommend that the Debug Traces and Debug Statistics
                                                      						micro-trace levels be enabled for no more than one hour because they can
                                                      						produce a large number of log entries. | diag_CuReplicator_*.uc |
| Note | We recommend that the Debug Traces and Debug Statistics
                                                      						micro-trace levels be enabled for no more than one hour because they can
                                                      						produce a large number of log entries. |
| CuService | The activities of Cisco Unity Connection Serviceability | diag_Tomcat_*.uc |
| CuSlmSvr | The activities of Cisco
                                       				  Smart Software Licensing Services in Cisco Unity Connection | diag_CuSlmSvr_*.uc |
| CuSnmpAgt | The activities of the Connection SNMP subagent | diag_CuSnmpAgt_*.uc |
| DataSysAgentTasks | Data SysAgent tasks | diag_CuSysAgent_*.uc |
| DbEvent | Component notification of database changes | <any> |
| DPAPI | The activities of the diagnostic portal application programming
                                          					 interface web service | diag_Tomcat_*.uc |
| EWSNotify | Exchange EWS mailbox synchronization notifications | <date in the format yyyy_mm_dd>.stderrout.log.* |
| FailureConv | Activation of the Failure Conversation when a system error
                                          					 occurs | diag_CuCsMgr_*.uc |
| Feeder | In Intersite Networking, this micro trace checks the local site
                                          					 change-tracking database for directory changes and responds to poll requests
                                          					 from the remote site gateway Reader task In HTTPS Networking, this micro trace checks the change-tracking
                                          					 database of local subtree in Feeder for directory changes and responds to poll
                                          					 requests from the remote location Reader task. | diag_Tomcat_*.uc |
| FeedReader | In Intersite Networking, this microtrace periodically polls the
                                          					 remote site gateway for any directory changes since the last poll interval. In HTTPS Networking, this microtrace periodically polls the
                                          					 remote location for any directory changes since the last poll interval. | diag_Tomcat_*.uc |
| LicenseClient | Functions related to license management | diag_CuCsMgr_*.uc |
| Logger | Writing traces logs and events | <any> |
| MessageEventService | Detection of arrival or deletion of messages | diag_Tomcat_*.uc |
| MiuAdm | Functions in Cisco Unity Connection Administration relating to
                                          					 testing voice messaging ports and generating certificates | diag_Tomcat_*.uc |
| MiuCall | The process between the Miu and conversations | diag_CuCsMgr_*.uc |
| MiuDatatbase | Media activities relating to accessing the database | diag_CuCsMgr_*.uc |
| MiuGeneral | Tracking calls through the phone user interface (TUI); call
                                          					 control functions; turning message waiting indicators (MWIs) on and off;
                                          					 notification and outdial functions; basic media or WAV file usage | diag_CuCsMgr_*.uc |
| MiuIO | Media or WAV file usage with TAPI (circuit-switched or Cisco
                                          					 Unified CallManager) integrations | diag_CuCsMgr_*.uc |
| MiuMethods | Handing of incoming calls; call control; turning messaging
                                          					 waiting indicators (MWIs) on and off; notification and outdial functions; media
                                          					 or WAV file usage | diag_CuCsMgr_*.uc |
| MiuSIP | SIP call control | diag_CuCsMgr_*.uc |
| MiuSIPStack | Low-level SIP interactions for call control | diag_CuCsMgr_*.uc |
| MiuSkinny | SCCP call control | diag_CuCsMgr_*.uc |
| MiuTranscode | Low-level media functions relating to transcoding | diag_CuCsMgr_*.uc |
| Mixer | Low-level activities relating to media and the Text-to-Speech
                                          					 feature | diag_CuMixer_*.uc |
| Monitor | Monitoring the status of voice messaging ports and call
                                          					 processing during a call; the server-side functions for displaying port status
                                          					 in Real-Time Monitoring Tool | diag_CuCsMgr_*.uc |
| MTA | Delivery of voice messages to the message store | diag_MTA_*.uc |
| Notifier | Notification of messages and selected events; turning message
                                          					 waiting indicators (MWIs) on and off | diag_CuCsMgr_*.uc diag_CuNotifier_*.uc |
| PCAMeetingPlace | Activities of the Cisco Personal Communications Assistant
                                          					 relating to MeetingPlace for the calendar feature | diag_Tomcat_*.u |
| PCAUnifiedCM | Activities of the Cisco Personal Communications Assistant
                                          					 relating to the Cisco Unified Communications Manager integration | diag_Tomcat_*.uc |
| PhoneManager | The management of IP phone applications | diag_CuCsMgr_*.uc |
| PhraseServer | The prompts that play and the user DTMF input; the logs are
                                          					 written to a file | diag_CuCsMgr_*.uc |
| PhraseServerToMonitor | The prompts that play and the user DTMF input; the logs are
                                          					 written to the monitor | diag_CuCsMgr_*.uc |
| ReportDataHarvester | Conversion of the content in the data log files to entries in
                                          					 the reports database | diag_CuReportDataHarvester_*.uc |
| ResourceLoader | Using the selected language in the GUI; filling strings with
                                          					 product or message information | <any> |
| ResourceManager | Monitoring and providing available resources to the Arbiter as
                                          					 needed | diag_CuCsMgr_*.uc |
| RoutingRules | Call routing decisions | diag_CuCsMgr_*.uc |
| RSS | RSS feeds that are used for checking voicemail from an RSS
                                          					 client | diag_Tomcat_*.uc |
| RulesEngine | Evaluation of personal call transfer rules for a user during a
                                          					 call | diag_CuCsMgr_*.uc diag_Tomcat_*.uc |
| SMTP | SMTP functions | diag_SMTP_*.uc |
| SocketPoolHelper | Socket connections to the IMAP server | <any> |
| SRM | Functions related to cluster management | diag_CuSrm_*.uc |
| SslInit | Initialization procedures for components that use OpenSSL | <any> |
| SttClient | Detects messages that need to be transcribed; attaches completed
                                          					 transcriptions to original messages | diag_MTA_*.uc |
| SttService | Communication between Cisco Unity Connection and the third-party
                                          					 external transcription service | diag_SttService_*.uc |
| SysAgent | System Agent component, which schedules system tasks that the
                                          					 administrator enters (such as resynchronizing MWIs) | diag_CuSysAgent_*.uc |
| TaskRequest | Functions related to the Task Management tool | diag_CuSysAgent_*.uc |
| TextToSpeech | The activities of the Text to Speech feature | diag_CuCsMgr_*.uc |
| ThreadPool | The use of threads by the processor | <any> |
| TimerHelper | The timer used by the Conversation Manager component | <any> |
| TranscodeWeb | The web server audio format transcoding utilities that transcode
                                          					 the incoming audio streams into the audio format that Cisco Unity Connection
                                          					 uses | diag_Tomcat_*.uc |
| TRaP | Phone Record and Playback (TRaP), which lets clients use the
                                          					 phone as a recording and playback device | diag_CuCsMgr_*.uc diag_Tomcat_*.uc |
| UmssSysAgentTasks | Messaging tasks for the System Agent component | diag_CuSysAgent_*.uc |
| UnityAssistant | The activities of the Messaging Assistant web tool in the
                                          					 Cisco Personal Communications Assistant | diag_Tomcat_*.uc |
| UnityInbox | The activities of the Messaging Inbox web tool in the
                                          					 Cisco Personal Communications Assistant | diag_Tomcat_*.uc |
| UnityPCTR | The activities of the Cisco Unity Connection Personal Call
                                          					 Transfer Rules web tool in the Cisco Personal Communications Assistant | diag_CuCsMgr_*.uc |
| Video | The activities of Video call between Unity Connection and Cisco
                                          					 MediaSense through APIs. | diag_CuCsMgr_*.uc |
| VirtualQueue | Call queuing | diag_CuCsMgr_*.uc |
| VMREST | Interactions with Representational State Transfer (REST) API
                                          					 clients | diag_Tomcat_*.uc |
| VMWS | Interactions with voice messaging web services | diag_Tomcat_*.uc |
| VUI | The voice user interface | diag_CuCsMgr_*.uc |

| Note | We recommend that the Debug Traces and Debug Statistics
                                                      						micro-trace levels be enabled for no more than one hour because they can
                                                      						produce a large number of log entries. |
|---|---|

| Caution | Enabling macro traces decreases system performance. Enable
                                          			 traces only for troubleshooting purposes. |
|---|---|

| Step 1 | In Cisco Unity Connection Serviceability, select Trace > Macro
                                             				  Traces . The Macro Traces page appears. |
|---|---|
| Step 2 | In the Server drop-down box, select the applicable Unity
                                       			 Connection or Cisco Business Edition server, and select Go . |
| Step 3 | Check the check box of the macro trace that you want to enable. |
| Step 4 | Expand the macro trace, and check the check boxes for the levels
                                       			 that you want to enable. |
| Step 5 | Select Save . Tip You may need to enable traces in Cisco Unity Connection
                                                      				  Serviceability and Cisco Unified Serviceability to troubleshoot Unity
                                                      				  Connection issues. To troubleshoot Unity Connection components, enable traces
                                                      				  in Cisco Unity Connection Serviceability. Similarly, to troubleshoot services
                                                      				  that are supported in Cisco Unified Serviceability, enable traces in Cisco
                                                      				  Unified Serviceability. For information on how to enable traces in Cisco
                                                      				  Unified Serviceability, see the Cisco Unified Serviceability Administration
                                                      				  Guide at http://www.cisco.com/en/US/products/ps6509/prod_maintenance_guides_list.html . | Tip | You may need to enable traces in Cisco Unity Connection
                                                      				  Serviceability and Cisco Unified Serviceability to troubleshoot Unity
                                                      				  Connection issues. To troubleshoot Unity Connection components, enable traces
                                                      				  in Cisco Unity Connection Serviceability. Similarly, to troubleshoot services
                                                      				  that are supported in Cisco Unified Serviceability, enable traces in Cisco
                                                      				  Unified Serviceability. For information on how to enable traces in Cisco
                                                      				  Unified Serviceability, see the Cisco Unified Serviceability Administration
                                                      				  Guide at http://www.cisco.com/en/US/products/ps6509/prod_maintenance_guides_list.html . |
| Tip | You may need to enable traces in Cisco Unity Connection
                                                      				  Serviceability and Cisco Unified Serviceability to troubleshoot Unity
                                                      				  Connection issues. To troubleshoot Unity Connection components, enable traces
                                                      				  in Cisco Unity Connection Serviceability. Similarly, to troubleshoot services
                                                      				  that are supported in Cisco Unified Serviceability, enable traces in Cisco
                                                      				  Unified Serviceability. For information on how to enable traces in Cisco
                                                      				  Unified Serviceability, see the Cisco Unified Serviceability Administration
                                                      				  Guide at http://www.cisco.com/en/US/products/ps6509/prod_maintenance_guides_list.html . |

| Tip | You may need to enable traces in Cisco Unity Connection
                                                      				  Serviceability and Cisco Unified Serviceability to troubleshoot Unity
                                                      				  Connection issues. To troubleshoot Unity Connection components, enable traces
                                                      				  in Cisco Unity Connection Serviceability. Similarly, to troubleshoot services
                                                      				  that are supported in Cisco Unified Serviceability, enable traces in Cisco
                                                      				  Unified Serviceability. For information on how to enable traces in Cisco
                                                      				  Unified Serviceability, see the Cisco Unified Serviceability Administration
                                                      				  Guide at http://www.cisco.com/en/US/products/ps6509/prod_maintenance_guides_list.html . |
|---|---|

| Macro Trace Name | What the Trace Analyzes | Filename of Trace Log |
|---|---|---|
| Call Flow Diagnostics | The flow of a call through Unity Connection | diag_CuCsMgr_*.uc |
| Message Tracking Traces | Message handing; the objects that handle messages from delivery
                                       				  to deletion | diag_CuSysAgent_*.uc diag_MTA_*.uc diag_CuCsMgr_*.uc diag_CuImapSvr_*.uc diag_Tomcat_*.uc |
| Call Control (Miu) Traces | Call control functions | diag_CuCsMgr_*.uc |
| Traces for MWI Problems | Turning message waiting indicators (MWIs) on and off | diag_CuCsMgr_*.uc diag_CuNotifier_*.uc |
| Traces for Other Notification Problems | Notification and outdial functions | diag_CuCsMgr_*.uc diag_CuNotifier_*.uc |
| Unity Startup | Unity Connection startup functions | diag_CuCsMgr_*.uc diag_CuNotifier_*.uc |
| Conversation Traces | Conversation usage | diag_CuCsMgr_*.uc |
| Voice User Interface/Speech Recognition Traces | Voice user interface (VUI) | diag_CuCsMgr_*.uc |
| Media (Wave) Traces | Media and WAV file usage | diag_CuCsMgr_*.uc diag_CuMixer_*.uc |
| Text to Speech (TTS) Traces | The Text to Speech (TTS) feature; also can log traces on other
                                       				  Cisco Unity Connection components that interact with TTS | diag_CuCsMgr_*.uc |
| Unity Connection Serviceability Web Service | The activity of Cisco Unified Serviceability | diag_Tomcat_*.uc |
| ViewMail for Outlook | The activity of Cisco Unity Connection ViewMail for Microsoft
                                       				  Outlook clients | diag_CuCsMgr_*.uc diag_CuImapSvr_*.uc diag_MTA_*.uc diag_Tomcat_*.uc |
| Digital Networking | Digital networking functions | diag_CuReplicator_*.uc |
| Single Inbox | Single inbox message synchronization | <date in the format
                                       				  yyyy_mm_dd>.stderrout. log.* diag_CuMbxSync_*.uc |