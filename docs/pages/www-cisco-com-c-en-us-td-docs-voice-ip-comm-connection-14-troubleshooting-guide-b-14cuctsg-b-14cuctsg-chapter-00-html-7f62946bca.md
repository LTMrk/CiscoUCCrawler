---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-connection-14-troubleshooting-guide-b-14cuctsg-b-14cuctsg-chapter-00-html-7f62946bca
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/14/troubleshooting/guide/b_14cuctsg/b_14cuctsg_chapter_00.html
retrieved_at: 2026-08-17T02:16:22.338310+00:00
---

Troubleshooting Guide for Cisco Unity Connection Release 14

# Troubleshooting Guide for Cisco Unity Connection Release 14

Updated: August 14, 2024

Chapter: Troubleshooting
	 Cisco Unity Connection

## Chapter: Troubleshooting
	 Cisco Unity Connection

# Troubleshooting
                     	 Cisco Unity Connection

The Troubleshooting Guide for Cisco Unity Connection helps resolve
                        		problems that you might encounter with Cisco Unity Connection. If your Unity
                        		Connection system is exhibiting a symptom that is documented in this
                        		troubleshooting guide, perform the recommended troubleshooting procedures.
                        		However, if the symptom is not documented in this troubleshooting guide, or if
                        		the recommended troubleshooting does not resolve the problem, do the procedure
                        		mentioned in this chapter to determine whether the problem is caused by SELinux
                        		Security policies. (SELinux replaced Cisco Security Agent(CSA) on Unity
                        		Connection servers.) You can also use traces to troubleshoot various problems
                        		associated with Unity Connection.

For more information on the CLI commands, see the applicable Command
                        		Line Interface Reference Guide for Cisco Unified Communications Solutions at .

### Troubleshooting Cisco Unity Connection

## Using Diagnostic Traces for Troubleshooting

Diagnostic traces can be used as a tool to assist you in troubleshooting problems. In Cisco Unity Connection Serviceability,
                           you enable traces to troubleshoot Cisco Unity Connection components. In Cisco Unified Serviceability, you enable traces to
                           troubleshoot services that are supported in Cisco Unified Serviceability. After the traces are enabled, you can access the
                           trace log files using Real-Time Monitoring Tool (RTMT) or the command line interface (CLI).

## Traces in Cisco Unity Connection Serviceability

Cisco Unity Connection Serviceability provides both micro traces and macro traces that you can enable individually or in any
                              combination.

Cisco Unity Connection Serviceability micro traces

Used to troubleshoot problems with specific Unity Connection components.

Cisco Unity Connection Serviceability macro traces

Used to troubleshoot general areas of Unity Connection functionality.

After the traces are enabled, you can access the trace log files using the Real-Time Monitoring Tool (RTMT) or the command
                              line interface (CLI).

### Micro Traces for
                           	 Selected Problems

You can use Cisco Unity Connection Serviceability micro traces to troubleshoot problems with specific Unity Connection components. Table 1 provides information on different Cisco Unity Connection Serviceability micro traces that you need for troubleshooting selected
                                 problems and for viewing the trace logs. (For instructions on using Cisco Unity Connection Serviceability micro traces, see
                                 the “ Using Traces ” chapter of the Administration Guide for Cisco Unity Connection Serviceability Release 14 , available at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/14/serv_administration/guide/b_14cucservag.html ).

Enabling Cisco Unity Connection Serviceability micro traces
                                             			 decreases system performance. Enable traces only for troubleshooting purposes.

Problem Area

Traces to Set

RTMT Service to Select

Trace Log Filename

Playing an attachment via the TUI

CML (all levels)

Connection Conversation Manager

diag_CuCsMgr_*.uc

Connection Notifier

diag_CuNotifier_*.uc

Connection Tomcat Application

diag_Tomcat_*.uc

ConvSub (all levels)

Connection Conversation Manager

diag_CuCsMgr_*.uc

Calendar integration

CCL (levels 10, 11, 12, 13)

Connection Conversation Manager.

diag_CuCsMgr_*.uc

Connection Tomcat Application

diag_Tomcat_*.uc

CsWebDav (levels 10, 11, 12, 13)

Connection Conversation Manager

diag_CuCsMgr_*.uc

Connection Tomcat Application

diag_Tomcat_*.uc

Calendar integration (event notifications)

CsWebDav (levels 10 through 13)

Connection IMAP Server

diag_CuImapSvr_*.uc

Routing rules

Arbiter (levels 14, 15, 16)

Connection Conversation Manager

diag_CuCsMgr_*.uc

RoutingRules (level 11)

Connection Conversation Manager

diag_CuCsMgr_*.uc

Cisco Unified Personal Communicator client (IMAP-related issues)

(see also “ Cisco
                                                						Unified Personal Communicator client (IMAP-related issues) ” in Table 1-2 )

CML (all levels)

Connection Conversation Manager

diag_CuCsMgr_*.uc

Connection Notifier

diag_CuNotifier_*.uc

Connection Tomcat Application

diag_Tomcat_*.uc

CsMalUmss (all levels)

Connection Conversation Manager

diag_CuCsMgr_*.uc

Connection Tomcat Application

diag_Tomcat_*.uc

CuImapSvr (all levels)

Connection IMAP Server

diag_CuImapSvr_*.uc

MTA (all levels)

Connection Message Transfer Agent

diag_MTA_*.uc

ViewMail for Outlook (sending and receiving messages)

(see also “ ViewMail
                                                						for Outlook (sending and receiving messages) ” in Table 1-2 )

CML (all levels)

Connection Conversation Manager

diag_CuCsMgr_*.uc

Connection Notifier

diag_CuNotifier_*.uc

Connection Tomcat Application

diag_Tomcat_*.uc

CsMalUmss (all levels)

Connection Conversation Manager

diag_CuCsMgr_*.uc

Connection Tomcat Application

diag_Tomcat_*.uc

CuImapSvr (all levels)

Connection IMAP Server

diag_CuImapSvr_*.uc

MTA (all levels)

Connection Message Transfer Agent

diag_MTA_*.uc

SMTP (all levels)

Connection SMTP Server

diag_SMTP_*.uc

Unity Connection clusters (except file replication)

SRM (all levels)

Connection Server Role Manager

diag_CuSrm_*.uc

Unity Connection cluster file replication

CuFileSync (all levels)

Connection File Syncer

diag_CuFileSync_*.uc

Accessing emails in an external message store

CML (all levels)

Connection Conversation Manager

diag_CuCsMgr_*.uc

Connection Tomcat Application

diag_Tomcat_*.uc

File rendering

MTA (all levels)

Connection Message Transfer Agent

diag_MTA_*.uc

SMTP messages are not sent

MTA (all levels)

Connection Message Transfer Agent

diag_MTA_*.uc

SMTP server mishandles faxes

SMTP (all levels)

Connection SMTP Server

diag_SMTP_*.uc

LDAP synchronization

(see also “ LDAP
                                                						synchronization ” in Table 1-3 )

CuCmDbEventListener

Connection CM Database Event Listener

diag_CuCmDbEventListener_*.uc

Dispatch messages

(see also “ Dispatch
                                                						messages ” in Table 1-2 )

MTA (all levels)

Connection Message Transfer Agent

diag_MTA_*.uc

IMAP messages

(see also “ IMAP
                                                						messages ”in Table 1-2 )

CML (all levels)

Connection Conversation Manager

diag_CuCsMgr_*.uc

Connection Notifier

diag_CuNotifier_*.uc

Connection Tomcat Application

diag_Tomcat_*.uc

CsMalUmss (all levels)

Connection Conversation Manager

diag_CuCsMgr_*.uc

Connection Tomcat Application

diag_Tomcat_*.uc

CuImapSvr (all levels)

Connection IMAP Server

diag_CuImapSvr_*.uc

MTA (all levels)

Unity Connection Message Transfer Agent

diag_MTA_*.uc

SMTP (all levels)

Connection SMTP Server

diag_SMTP_*.uc

Message delivery and retrieval

(see also “ Message
                                                						delivery and retrieval ” in Table 1-2 )

CML (all levels)

Connection Conversation Manager

diag_CuCsMgr_*.uc

Connection Notifier

diag_CuNotifier_*.uc

Connection Tomcat Application

diag_Tomcat_*.uc

CsMalUmss (levels 10, 14, 18, 22, 23, 26)

Connection Conversation Manager

diag_CuCsMgr_*.uc

Connection Tomcat Application

diag_Tomcat_*.uc

MTA (all levels)

Connection Message Transfer Agent

diag_MTA_*.uc

Notifier (all levels except 6 and 7)

Connection Conversation Manager

diag_CuCsMgr_*.uc

Connection Notifier

diag_CuNotifier_*.uc

SMTP (all levels)

Connection SMTP Server

diag_SMTP_*.uc

UmssSysAgentTasks (all levels)

Connection System Agent

diag_CuSysAgent_*.uc

Message Relay Issues

MTA (all levels)

Connection Message Transfer Agent

diag_MTA_*.uc

SMTP (all levels)

Connection SMTP Server

diag_SMTP_*.uc

NDRs

(see also “ NDRs ”
                                             					 in Table 1-2 )

CML (all levels)

Connection Conversation Manager

diag_CuCsMgr_*.uc

Connection Notifier

diag_CuNotifier_*.uc

Connection Tomcat Application

diag_Tomcat_*.uc

CuCsMgr (all levels)

Connection Conversation Manager

diag_CuCsMgr_*.uc

Notifications not sent

(see also “ Notifications
                                                						not sent ” in Table 1-2 )

CuCsMgr (all levels)

Connection Conversation Manager

diag_CuCsMgr_*.uc

Notifier (all levels except 6 and 7)

Connection Conversation Manager

diag_CuCsMgr_*.uc

Connection Notifier

diag_CuNotifier_*.uc

SMTP/HTML notification/Intelligent Notification

Notifier (all levels except 6 and 7)

Connection Notifier

diag_CuNotifier_*.uc

SMTP (all levels)

Connection SMTP Server

diag_SMTP_*.uc

Secure message aging

UmssSysAgentTasks (all levels)

Connection System Agent

diag_CuSysAgent_*.uc

SMS notifications

Notifier (all levels except 6 and 7)

Connection Conversation Manager

diag_CuCsMgr_*.uc

Connection Notifier

diag_CuNotifier_*.uc

Intrasite Networking replication

(see also “ Intrasite
                                                						Networking replication ” in Table 1-2 )

CuReplicator

Connection Digital Networking Replication Agent

diag_CuReplicator_*.uc

Intersite Networking replication

Feeder (levels 00, 01, 02, 03)

Connection Tomcat Application

diag_Tomcat_*.uc

FeedReader (levels 00, 01, 02, 03, 10, 14)

Connection System Agent

diag_CuSysAgent_*.uc

HTTP(S) Networking

FeedReader (levels 00, 01, 02, 03, 10, 14)

Connection System Agent

diag_CuSysAgent_*.uc

Feeder (levels 00, 01, 02, 03)

Connection Tomcat Application

diag_Tomcat_*.uc

VPIM message delivery

(see also “ VPIM
                                                						message delivery ” in Table 1-2 )

MTA (all levels)

Connection Message Transfer Agent

diag_MTA_*.uc

SMTP (all levels)

Connection SMTP Server

diag_SMTP_*.uc

Accessing calendar information

CCL (levels 10, 11, 12, 13)

Connection Conversation Manager

diag_CuCsMgr_*.uc

Connection Tomcat Application

diag_Tomcat_*.uc

CsWebDav (levels 10, 11, 12, 13)

Connection Conversation Manager

diag_CuCsMgr_*.uc

Connection Tomcat Application

diag_Tomcat_*.uc

Configuring personal call transfer rule settings by phone

ConvSub (all levels)

Connection Conversation Manager

diag_CuCsMgr_*.uc

Rule processing during calls to a rules-enabled user

ConvRoutingRules (all levels)

Connection Conversation Manager

diag_CuCsMgr_*.uc

RulesEngine (all levels)

Connection Tomcat Application

diag_Tomcat_*.uc

Connection Conversation Manager

diag_CuCsMgr_*.uc

Rules-related conversations

CDE (all levels)

Connection Conversation Manager

diag_CuCsMgr_*.uc

Phone View

PhoneManager (all levels)

Connection Conversation Manager

diag_CuCsMgr_*.uc

Data collection in reports

ReportDataHarvester (all levels)

Connection Report Data Harvester

diag_CuReportDataHarvester_*.uc

Display of reports

CuService (all levels)

Connection Tomcat Application

diag_Tomcat_*.uc

Access to RSS feeds of voice messages

RSS (all levels)

Connection Tomcat Application

diag_Tomcat_*.uc

SNMP

CuSnmpAgt (all levels)

Connection SNMP Agent

diag_CuSnmpAgt_*.uc

SpeechView transcriptions

SttClient (all levels)

Connection Message Transfer Agent

diag_MTA_*.uc

SttService (all levels)

Connection SpeechView Processor

diag_SttService_*.uc

SMTP (all levels)

Connection SMTP Server

diag_SMTP_*.uc

MTA (level 10, 11, 12, 13)

Connection Message Transfer Agent

diag_MTA_*.uc

SysAgent (level 10, 11, 12, 16)

Connection System Agent

diag_CuSysAgent_*.uc

Sending transcriptions to notification devices

Notifier (level 16, 21, 25, 30)

Connection Notifier

diag_CuNotifier_*.uc

Test button (external service diagnostic tool)

CuESD (all levels)

Connection Tomcat Application

diag_Tomcat_*.uc

Interactions with Representational State Transfer (REST) API

VMREST (all levels)

Connection Tomcat Application

diag_Tomcat_*.uc

Jabber VoiceMail Issues

Jabber VoiceMail

Not Applicable as it is enabled by default

Cisco Tomcat

localhost_access_log.txt

Not Applicable as it is enabled by default

Connection Jetty

request.log

Notifier (level 18 and 21)

Connection Notifier

diag_CuNotifier_*.uc

Connection Tomcat Application

diag_Tomcat_*.uc

Connection Tomcat Application

diag_Tomcat_*.uc

Visual VoiceMail Issues

TRAP - (all levels)

Connection Conversation Manager

diag_CuCsMgr_*.uc

VMREST (all levels)

Connection Tomcat Application

diag_Tomcat_*.uc

Arbiter - (level 12 to17)

Connection Conversation Manager

diag_CuCsMgr_*.uc

CDE-04 - <13-17>

Connection Conversation Manager

diag_CuCsMgr_*.uc

MiuCall - (all levels)

Connection Conversation Manager

diag_CuCsMgr_*.ucCu

MiuGeneral - (all levels)

Connection Conversation Manager

diag_CuCsMgr_*.uc

MiuIO - <11-15>

Connection Conversation Manager

diag_CuCsMgr_*.uc

MiuMethod - (all levels)

Connection Conversation Manager

diag_CuCsMgr_*.uc

MiuSIP - (all levels)

Connection Conversation Manager

diag_CuCsMgr_*.uc

MiuSIPStack - (all levels)

Connection Conversation Manager

diag_CuCsMgr_*.uc

Mixer - (all levels)

Connection Mixer

diag_CuMixer_*.uc

CuSlmSvr (all levels)

Connection Smart License Manager Server

diag_CuSlmSvr_*.uc

Cuca

Connection Tomcat Application

diag_Tomcat_*.uc

VMREST (all levels)

Connection Tomcat Application

diag_Tomcat_*.uc

CDE (level 1, 10 to 17, 20, 21)

Connection Conversation Manager

diag_CuCsMgr_*.uc

ConvSub (level 01 to 05)

Connection Conversation Manager

diag_CuCsMgr_*.uc

MiuIO (level 11 to 13, 25, 27)

Connection Conversation Manager

diag_CuCsMgr_*.uc

Miu Sip/Miu Sip Stack (all levels)

Connection Conversation Manager

diag_CuCsMgr_*.uc

MiuMethods/MiuCall (all levels)

Connection Conversation Manager

diag_CuCsMgr_*.uc

Mixer (levels 01 to 04)

Connection Mixer

diag_CuMixer_*.uc

Video (level 10 and 11)

Connection Conversation Manager

diag_CuCsMgr_*.uc

CLI Command to activate SAML SSO logs:

admin: set samltrace level <trace-level>

where

trace-level can be BEBUG, INFO, WARNING, ERROR, or FATAL

CLI Command to check trace level:

admin: show samltrace level

Cisco Tomcat

Cisco Tomcat Security

Cisco SSO

ssosp*.log

ssoApp.log

Synchronization traces between Unity Connection and Exchange

CsMbxSync

Connection Mailbox Sync

diag_CuMbxSync_*.uc

Synchronization traces between Unity Connection and Gmail Server

CuGSuiteSyncSrv

Connection GSuite Sync Service

diag_CuGSuiteSyncSrv_*.uc

Exchange EWS calls in MbxSync diag

CsEws

Connection Mailbox Sync

diag_CuMbxSync_*.uc

EWS notification in Jetty web service diags

EWSNotify

Connection Jetty

Exchange 2003 webdav protocol diags

CsWebDav

Connection Mailbox Sync

diag_CuMbxSync)_*.uc

Activities of Connection external service

CuEsd

Connection Tomcat Application

diag_Tomcat_*.uc

Message deposition on Connection

MTA

Connection Message Transfer Agent

diag_CuMta_*.uc

CUCA test buttons for UM service and UM user pages

Cuca

Connection Tomcat Application

diag_Tomcat_*.uc

Autodiscovery feature diags

MbxLocator

Connection Mailbox Sync

diag_CuMbxSync_*.uc

MbxSyncQ and EWSNotiftQ events

DBEvent

Connection DB Event Publisher

diag_DbEventPublisher_*.uc

PIN
                                             					 Synchronization Issues

PIN
                                             					 Synchronization Issues

AxlAccess (level 00,01)

Connection Conversation Manager

diag_CuCsMgr_*.uc

Bulk
                                             					 Administration Tool (all levels)

Tomcat
                                             					 Logs

diag_Tomcat_*.uc

CiscoPCA
                                             					 (level 00,01,02,13)

Tomcat
                                             					 Logs

diag_Tomcat_*.uc

Cuca
                                             					 (all levels)

Tomcat
                                             					 Logs

diag_Tomcat_*.uc

CuCsMgr
                                             					 (level 10)

Connection Conversation Manager

diag_CuCsMgr_*.uc

VMREST
                                             					 (all levels)

Tomcat
                                             					 Logs

diag_Tomcat_*.uc

CDL
                                             					 (level 10 and 11)

Connection Conversation Manager

diag_CuCsMgr_*.uc

ConvSub
                                             					 (level 01,03,04,05)

Connection Conversation Manager

diag_CuCsMgr_*.uc

### Macro Traces for
                           	 Selected Problems

Cisco Unity Connection Serviceability macro
                                 		  traces enable a preselected set of micro traces with which you can troubleshoot
                                 		  general areas of Unity Connection functionality.

Table 1-2 lists the information for Cisco Unity Connection Serviceability macro traces that you need for troubleshooting selected problems
                                 and for viewing the trace logs. (For instructions on using Cisco Unity Connection Serviceability macro traces, see the“ Using Traces ” chapter of the Administration Guide for Cisco Unity Connection Serviceability Release 14 , available at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/14/serv_administration/guide/b_14cucservag.html ).

Problem Area

Traces to Set

RTMT Service to Select

Trace Log Filename

Audio quality

Media (Wave) Traces

Connection Conversation Manager

diag_CuCsMgr_*.uc

Connection Mixer

diag_CuMixer_*.uc

Call control

Call Control (Miu) Traces (expand the macro trace to select SIP
                                             					 or SCCP)

Connection Conversation Manager

diag_CuCsMgr_*.uc

Call flow

Call Flow Diagnostics

Connection Conversation Manager

diag_CuCsMgr_*.uc

ViewMail for Outlook (recording or playback by phone)

Call Control (Miu) Traces (expand the macro trace to select SIP
                                             					 or SCCP)

Connection Conversation Manager

diag_CuCsMgr_*.uc

Cisco Unified Personal Communicator client (IMAP-related issues)

(see also “ Cisco
                                                						Unified Personal Communicator client (IMAP-related issues) ” in Table 1-1 )

Call Flow Diagnostics

Connection Conversation Manager

diag_CuCsMgr_*.uc

ViewMail for Outlook (sending and receiving messages)

(see also “ ViewMail
                                                						for Outlook (sending and receiving messages) ” in Table 1-1 )

Call Flow Diagnostics

Connection Conversation Manager

diag_CuCsMgr_*.uc

ViewMail for Outlook

Connection Conversation Manager

diag_CuCsMgr_*.uc

Connection IMAP Server

diag_CuImapSvr_*.uc

Connection Message Transfer Agent

diag_MTA_*.uc

Connection Tomcat Application

diag_Tomcat_*.uc

Connection REST Service

diag_Tomcat_*.uc

Connection Mailbox Sync

diag_CuMbxSync_*.uc

Cisco Unity Connection Serviceability

Connection Serviceability Web Service

Connection Tomcat Application

diag_Tomcat_*.uc

Conversations

Conversation Traces

Connection Conversation Manager

diag_CuCsMgr_*.uc

Dispatch messages

(see also “ Dispatch
                                                						messages ” in Table 1-1 )

Call Flow Diagnostics

Connection Conversation Manager

diag_CuCsMgr_*.uc

IMAP messages

(see also “ IMAP
                                                						messages ” in Table 1-1 )

Call Flow Diagnostics

Connection Conversation Manager

diag_CuCsMgr_*.uc

Message delivery and retrieval

(see also “ Message
                                                						delivery and retrieval ” in Table 1-1 )

Message Tracking Traces

Connection Message Transfer Agent

diag_MTA_*.uc

Connection System Agent

diag_CuSysAgent_*.uc

Connection Conversation Manager

diag_CuCsMgr_*.uc

Connection Tomcat Application

diag_Tomcat_*.uc

Connection IMAP Server

diag_CuImapSvr_*.uc

NDRs

(see also “ NDRs ”
                                             					 in Table 1-1 )

Call Flow Diagnostics

Connection Conversation Manager

diag_CuCsMgr_*.uc

Notifications not sent

(see also “ Notifications
                                                						not sent ” in Table 1-1 )

Traces for Other Notification Problems (expand the macro trace
                                             					 to select SIP or SCCP)

Connection Conversation Manager

diag_CuCsMgr_*.uc

Connection Notifier

diag_CuNotifier_*.uc

Message not synchronized in Unified Messaging

Single Inbox Traces

Connection Mailbox Sync

diag_CuMbxSync_*.uc

MWIs

Traces for MWI problems (expand the macro trace to select SIP or
                                             					 SCCP)

Connection Conversation Manager

diag_CuCsMgr_*.uc

Connection Notifier

diag_CuNotifier_*.uc

Intrasite Networking replication

(see also “ Intrasite
                                                						Networking replication ” in Table 1-1 )

Digital Networking

Connection Digital Networking Replication Agent

diag_CuReplicator_*.uc

VPIM message delivery

(see also “ VPIM
                                                						message delivery ” in Table 1-1 )

Call Flow Diagnostics

Connection Conversation Manager

diag_CuCsMgr_*.uc

Unity Connection startup fails

Unity Startup

Connection Conversation Manager

diag_CuCsMgr_*.uc

Connection Notifier

diag_CuNotifier_*.uc

Text to Speech

Call Control (Miu) Traces (expand the macro trace to select SIP
                                             					 or SCCP)

Connection Conversation Manager

diag_CuCsMgr_*.uc

Media (Wave) Traces

Connection Conversation Manager

diag_CuCsMgr_*.uc

Connection Mixer

diag_CuMixer_*.uc

Text to Speech (TTS) Traces

Connection Conversation Manager

diag_CuCsMgr_*.uc

### Using Micro or Macro Traces

When you use Cisco Unity Connection Serviceability micro traces or macro traces to troubleshoot problems in Unity Connection,
                              you must first enable the applicable traces in Cisco Unity Connection Serviceability. Then you can use the Real-Time Monitoring
                              Tool (RTMT) or the command line interface (CLI) to collect and view the logs that are generated by the traces.

#### Enabling Micro or Macro Traces and View Trace Logs

Step 1

In Cisco Unity Connection Serviceability, on
                                             			 the Trace menu, do either of the following:

select Micro Traces to enable micro
                                                      					 traces.

Select Macro Traces to enable macro
                                                      					 traces.

Step 2

On the Micro Traces or Macro Traces page, in the Server field,
                                             			 select the name of the Unity Connection server and select Go .

Step 3

Do either of the following:

In the Micro Trace field, select the
                                                      					 micro trace that you want to set and select Go .

Check the check box of the macro trace
                                                      					 that you want to enable.

Step 4

Under Micro Traces or Macro Traces, check the check boxes for the
                                             			 micro-trace or macro-trace levels that you want to set and select Save .

Step 5

Reproduce the problem.

Step 6

To collect the trace log files, launch the Real-Time Monitoring
                                             			 Tool (RTMT). For detailed instructions, see the “Working with Trace and Log
                                             			 Central” chapter of the applicable Cisco Unified Real-Time Monitoring Tool
                                                				Administration Guide , available at http://www.cisco.com/en/US/products/ps6509/prod_maintenance_guides_list.html .

You can access the trace log files using the
                                                				command line interface (CLI). For information, see the applicable Command Line Interface Reference Guide for
                                                   				  Cisco Unified Solutions at http://www.cisco.com/en/US/products/ps6509/prod_maintenance_guides_list.html .

Step 7

In RTMT, on the System menu, select Tools > Trace > Trace & Log
                                                   				  Central .

Step 8

In the Trace & Log Central tree hierarchy, double-click Collect Files .

Step 9

In the Select CUC Services/Application tab, check the check boxes
                                             			 for the applicable services and select Next .

Step 10

In the Select System Services/Applications tab, select Next .

Step 11

In the Collection Time group box, specify the time range for which
                                             			 you want to collect traces.

Step 12

In the Download File option group box, specify the options you
                                             			 want for downloading traces.

Step 13

Select Finish .

Step 14

To view the trace files that you collected, you can use the Local
                                             			 Browse option of the trace collection feature.

Step 15

In Cisco Unity Connection Serviceability, disable the traces that
                                             			 you enabled in Step 3 and Step 4 , then select Save .

### Traces in Cisco Unified Serviceability

## Traces for Selected Problems

You can use Cisco Unified Serviceability traces to troubleshoot certain problems. After the traces are enabled, you can access
                           the trace log files using the Real-Time Monitoring Tool (RTMT) or the command line interface (CLI).

Table 1-3 lists the information for Cisco Unified Serviceability traces that you need for troubleshooting selected problems and for
                           viewing the trace logs. (For detailed information on using Cisco Unified Serviceability traces, see the “Trace” chapter of
                           the applicable Cisco Unified Serviceability Administration Guide at http://www.cisco.com/en/US/products/ps6509/prod_maintenance_guides_list.html .)

Enabling Cisco Unified Serviceability traces decreases system performance. Enable traces only for troubleshooting purposes.

Problem Area

Traces to Set

RTMT Service to Select

Backing up and restoring

Cisco DRF Local Cisco DRF Master

Cisco DRF Local Cisco DRF Master

LDAP synchronization

Cisco DirSync

Cisco DirSync

Web application sign-in

Cisco CCMRealm Web Service

Cisco CallManager Realm

## Using Traces to Troubleshoot Problems

When you use Cisco Unified Serviceability traces to troubleshoot problems in Cisco Unity Connection, you must first enable
                           the applicable traces in Cisco Unified Serviceability. Then you can use the Real-Time Monitoring Tool (RTMT) or the command
                           line interface (CLI) to collect and view the logs that are generated by the traces.

### Enabling Cisco Unified Serviceability Traces and View Trace
                           	 Logs

Step 1

In Cisco Unified Serviceability, on the
                                          			 Trace menu, select Troubleshooting Trace
                                             				Settings .

Step 2

On the Troubleshooting Trace Settings page,
                                          			 under Directory Services, check the check box for the trace that you want to
                                          			 enable and select Save .

Step 3

Reproduce the problem.

Step 4

To collect the trace log files, launch the
                                          			 Real-Time Monitoring Tool (RTMT). For detailed instructions, see the “Working
                                          			 with Trace and Log Central” chapter of the applicable Cisco Unified Real-Time Monitoring Tool
                                             				Administration Guide , available at http://www.cisco.com/en/US/products/ps6509/prod_maintenance_guides_list.html .

You can access the trace log files using the
                                             				command line interface (CLI). For information, see the applicable Command Line Interface Reference Guide for
                                                				  Cisco Unified Communications Solutions at http://www.cisco.com/en/US/products/ps6509/prod_maintenance_guides_list.html .

Step 5

In RTMT, on the System menu, select Tools > Trace > Trace & Log
                                                				  Central .

Step 6

In the Trace & Log Central tree
                                          			 hierarchy, double-click Collect Files .

Step 7

In the Select CUC Services/Application tab,
                                          			 select Next .

Step 8

In the Select System Services/Applications
                                          			 tab, check the check boxes for the applicable service and select Next .

Step 9

In the Collection Time group box, specify
                                          			 the time range for which you want to collect traces.

Step 10

In the Download File option group box,
                                          			 specify the options you want for downloading traces.

Step 11

Select Finish .

Step 12

To view the trace files that you collected,
                                          			 you can use the Local Browse option of the trace collection feature.

Step 13

In Cisco Unity Connection Serviceability,
                                          			 disable the traces that you enabled in Step 2 , and select Save .

| Cisco Unity Connection Serviceability micro traces | Used to troubleshoot problems with specific Unity Connection components. |
|---|---|
| Cisco Unity Connection Serviceability macro traces | Used to troubleshoot general areas of Unity Connection functionality. |

| Note | Enabling Cisco Unity Connection Serviceability micro traces
                                             			 decreases system performance. Enable traces only for troubleshooting purposes. |
|---|---|

| Problem Area | Traces to Set | RTMT Service to Select | Trace Log Filename |
|---|---|---|---|
| Audio Issues |
| Playing an attachment via the TUI | CML (all levels) | Connection Conversation Manager | diag_CuCsMgr_*.uc |
| Connection Notifier | diag_CuNotifier_*.uc |
| Connection Tomcat Application | diag_Tomcat_*.uc |
| ConvSub (all levels) | Connection Conversation Manager | diag_CuCsMgr_*.uc |
| Calendar Integration
                                          				  Issues |
| Calendar integration | CCL (levels 10, 11, 12, 13) | Connection Conversation Manager. | diag_CuCsMgr_*.uc |
| Connection Tomcat Application | diag_Tomcat_*.uc |
| CsWebDav (levels 10, 11, 12, 13) | Connection Conversation Manager | diag_CuCsMgr_*.uc |
| Connection Tomcat Application | diag_Tomcat_*.uc |
| Calendar integration (event notifications) | CsWebDav (levels 10 through 13) | Connection IMAP Server | diag_CuImapSvr_*.uc |
| Call Issues |
| Routing rules | Arbiter (levels 14, 15, 16) | Connection Conversation Manager | diag_CuCsMgr_*.uc |
| RoutingRules (level 11) | Connection Conversation Manager | diag_CuCsMgr_*.uc |
| Client Issues |
| Cisco Unified Personal Communicator client (IMAP-related issues) (see also “ Cisco
                                                						Unified Personal Communicator client (IMAP-related issues) ” in Table 1-2 ) | CML (all levels) | Connection Conversation Manager | diag_CuCsMgr_*.uc |
| Connection Notifier | diag_CuNotifier_*.uc |
| Connection Tomcat Application | diag_Tomcat_*.uc |
| CsMalUmss (all levels) | Connection Conversation Manager | diag_CuCsMgr_*.uc |
| Connection Tomcat Application | diag_Tomcat_*.uc |
| CuImapSvr (all levels) | Connection IMAP Server | diag_CuImapSvr_*.uc |
| MTA (all levels) | Connection Message Transfer Agent | diag_MTA_*.uc |
| ViewMail for Outlook (sending and receiving messages) (see also “ ViewMail
                                                						for Outlook (sending and receiving messages) ” in Table 1-2 ) | CML (all levels) | Connection Conversation Manager | diag_CuCsMgr_*.uc |
| Connection Notifier | diag_CuNotifier_*.uc |
| Connection Tomcat Application | diag_Tomcat_*.uc |
| CsMalUmss (all levels) | Connection Conversation Manager | diag_CuCsMgr_*.uc |
| Connection Tomcat Application | diag_Tomcat_*.uc |
| CuImapSvr (all levels) | Connection IMAP Server | diag_CuImapSvr_*.uc |
| MTA (all levels) | Connection Message Transfer Agent | diag_MTA_*.uc |
| SMTP (all levels) | Connection SMTP Server | diag_SMTP_*.uc |
| Unity Connection Cluster
                                          				  Issues |
| Unity Connection clusters (except file replication) | SRM (all levels) | Connection Server Role Manager | diag_CuSrm_*.uc |
| Unity Connection cluster file replication | CuFileSync (all levels) | Connection File Syncer | diag_CuFileSync_*.uc |
| External Message Store
                                          				  Issues |
| Accessing emails in an external message store | CML (all levels) | Connection Conversation Manager | diag_CuCsMgr_*.uc |
| Connection Tomcat Application | diag_Tomcat_*.uc |
| Fax Issues |
| File rendering | MTA (all levels) | Connection Message Transfer Agent | diag_MTA_*.uc |
| SMTP messages are not sent | MTA (all levels) | Connection Message Transfer Agent | diag_MTA_*.uc |
| SMTP server mishandles faxes | SMTP (all levels) | Connection SMTP Server | diag_SMTP_*.uc |
| LDAP Issues |  |
| LDAP synchronization (see also “ LDAP
                                                						synchronization ” in Table 1-3 ) | CuCmDbEventListener | Connection CM Database Event Listener | diag_CuCmDbEventListener_*.uc |
| Message Issues |
| Dispatch messages (see also “ Dispatch
                                                						messages ” in Table 1-2 ) | MTA (all levels) | Connection Message Transfer Agent | diag_MTA_*.uc |
| IMAP messages (see also “ IMAP
                                                						messages ”in Table 1-2 ) | CML (all levels) | Connection Conversation Manager | diag_CuCsMgr_*.uc |
| Connection Notifier | diag_CuNotifier_*.uc |
| Connection Tomcat Application | diag_Tomcat_*.uc |
| CsMalUmss (all levels) | Connection Conversation Manager | diag_CuCsMgr_*.uc |
| Connection Tomcat Application | diag_Tomcat_*.uc |
| CuImapSvr (all levels) | Connection IMAP Server | diag_CuImapSvr_*.uc |
| MTA (all levels) | Unity Connection Message Transfer Agent | diag_MTA_*.uc |
| SMTP (all levels) | Connection SMTP Server | diag_SMTP_*.uc |
| Message delivery and retrieval (see also “ Message
                                                						delivery and retrieval ” in Table 1-2 ) | CML (all levels) | Connection Conversation Manager | diag_CuCsMgr_*.uc |
| Connection Notifier | diag_CuNotifier_*.uc |
| Connection Tomcat Application | diag_Tomcat_*.uc |
| CsMalUmss (levels 10, 14, 18, 22, 23, 26) | Connection Conversation Manager | diag_CuCsMgr_*.uc |
| Connection Tomcat Application | diag_Tomcat_*.uc |
| MTA (all levels) | Connection Message Transfer Agent | diag_MTA_*.uc |
| Notifier (all levels except 6 and 7) | Connection Conversation Manager | diag_CuCsMgr_*.uc |
| Connection Notifier | diag_CuNotifier_*.uc |
| SMTP (all levels) | Connection SMTP Server | diag_SMTP_*.uc |
| UmssSysAgentTasks (all levels) | Connection System Agent | diag_CuSysAgent_*.uc |
| Message Relay Issues | MTA (all levels) | Connection Message Transfer Agent | diag_MTA_*.uc |
| SMTP (all levels) | Connection SMTP Server | diag_SMTP_*.uc |
| NDRs (see also “ NDRs ”
                                             					 in Table 1-2 ) | CML (all levels) | Connection Conversation Manager | diag_CuCsMgr_*.uc |
| Connection Notifier | diag_CuNotifier_*.uc |
| Connection Tomcat Application | diag_Tomcat_*.uc |
| CuCsMgr (all levels) | Connection Conversation Manager | diag_CuCsMgr_*.uc |
| Notifications not sent (see also “ Notifications
                                                						not sent ” in Table 1-2 ) | CuCsMgr (all levels) | Connection Conversation Manager | diag_CuCsMgr_*.uc |
| Notifier (all levels except 6 and 7) | Connection Conversation Manager | diag_CuCsMgr_*.uc |
| Connection Notifier | diag_CuNotifier_*.uc |
| SMTP/HTML notification/Intelligent Notification | Notifier (all levels except 6 and 7) | Connection Notifier | diag_CuNotifier_*.uc |
| SMTP (all levels) | Connection SMTP Server | diag_SMTP_*.uc |
| Secure message aging | UmssSysAgentTasks (all levels) | Connection System Agent | diag_CuSysAgent_*.uc |
| SMS notifications | Notifier (all levels except 6 and 7) | Connection Conversation Manager | diag_CuCsMgr_*.uc |
| Connection Notifier | diag_CuNotifier_*.uc |
| Networking
                                          				  Issues |
| Intrasite Networking replication (see also “ Intrasite
                                                						Networking replication ” in Table 1-2 ) | CuReplicator | Connection Digital Networking Replication Agent | diag_CuReplicator_*.uc |
| Intersite Networking replication | Feeder (levels 00, 01, 02, 03) | Connection Tomcat Application | diag_Tomcat_*.uc |
| FeedReader (levels 00, 01, 02, 03, 10, 14) | Connection System Agent | diag_CuSysAgent_*.uc |
| HTTP(S) Networking | FeedReader (levels 00, 01, 02, 03, 10, 14) | Connection System Agent | diag_CuSysAgent_*.uc |
| Feeder (levels 00, 01, 02, 03) | Connection Tomcat Application | diag_Tomcat_*.uc |
| VPIM message delivery (see also “ VPIM
                                                						message delivery ” in Table 1-2 ) | MTA (all levels) | Connection Message Transfer Agent | diag_MTA_*.uc |
| SMTP (all levels) | Connection SMTP Server | diag_SMTP_*.uc |
| Personal Call Transfer
                                          				  Rule Issues |
| Accessing calendar information | CCL (levels 10, 11, 12, 13) | Connection Conversation Manager | diag_CuCsMgr_*.uc |
| Connection Tomcat Application | diag_Tomcat_*.uc |
| CsWebDav (levels 10, 11, 12, 13) | Connection Conversation Manager | diag_CuCsMgr_*.uc |
| Connection Tomcat Application | diag_Tomcat_*.uc |
| Configuring personal call transfer rule settings by phone | ConvSub (all levels) | Connection Conversation Manager | diag_CuCsMgr_*.uc |
| Rule processing during calls to a rules-enabled user | ConvRoutingRules (all levels) | Connection Conversation Manager | diag_CuCsMgr_*.uc |
| RulesEngine (all levels) | Connection Tomcat Application | diag_Tomcat_*.uc |
| Connection Conversation Manager | diag_CuCsMgr_*.uc |
| Rules-related conversations | CDE (all levels) | Connection Conversation Manager | diag_CuCsMgr_*.uc |
| Phone View
                                          				  Issues |
| Phone View | PhoneManager (all levels) | Connection Conversation Manager | diag_CuCsMgr_*.uc |
| Report Issues |
| Data collection in reports | ReportDataHarvester (all levels) | Connection Report Data Harvester | diag_CuReportDataHarvester_*.uc |
| Display of reports | CuService (all levels) | Connection Tomcat Application | diag_Tomcat_*.uc |
| RSS Feed Issues |
| Access to RSS feeds of voice messages | RSS (all levels) | Connection Tomcat Application | diag_Tomcat_*.uc |
| SNMP Issues |
| SNMP | CuSnmpAgt (all levels) | Connection SNMP Agent | diag_CuSnmpAgt_*.uc |
| SpeechView Transcription
                                          				  Issues |
| SpeechView transcriptions | SttClient (all levels) | Connection Message Transfer Agent | diag_MTA_*.uc |
| SttService (all levels) | Connection SpeechView Processor | diag_SttService_*.uc |
| SMTP (all levels) | Connection SMTP Server | diag_SMTP_*.uc |
| MTA (level 10, 11, 12, 13) | Connection Message Transfer Agent | diag_MTA_*.uc |
| SysAgent (level 10, 11, 12, 16) | Connection System Agent | diag_CuSysAgent_*.uc |
| Sending transcriptions to notification devices | Notifier (level 16, 21, 25, 30) | Connection Notifier | diag_CuNotifier_*.uc |
| Test Button (External
                                          				  Service and External Service Account) Issues |
| Test button (external service diagnostic tool) | CuESD (all levels) | Connection Tomcat Application | diag_Tomcat_*.uc |
| Web Inbox
                                          				  Issues |
| Interactions with Representational State Transfer (REST) API | VMREST (all levels) | Connection Tomcat Application | diag_Tomcat_*.uc |
| Jabber VoiceMail Issues |
| Jabber VoiceMail | Not Applicable as it is enabled by default | Cisco Tomcat | localhost_access_log.txt |
| Not Applicable as it is enabled by default | Connection Jetty | request.log |
| Notifier (level 18 and 21) | Connection Notifier | diag_CuNotifier_*.uc |
| Cuca | Connection Tomcat Application | diag_Tomcat_*.uc |
| VMREST | Connection Tomcat Application | diag_Tomcat_*.uc |
| Visual VoiceMail Issues | TRAP - (all levels) | Connection Conversation Manager | diag_CuCsMgr_*.uc |
| VMREST (all levels) | Connection Tomcat Application | diag_Tomcat_*.uc |
| Arbiter - (level 12 to17) | Connection Conversation Manager | diag_CuCsMgr_*.uc |
| CDE-04 - <13-17> | Connection Conversation Manager | diag_CuCsMgr_*.uc |
| MiuCall - (all levels) | Connection Conversation Manager | diag_CuCsMgr_*.ucCu |
| MiuGeneral - (all levels) | Connection Conversation Manager | diag_CuCsMgr_*.uc |
| MiuIO - <11-15> | Connection Conversation Manager | diag_CuCsMgr_*.uc |
| MiuMethod - (all levels) | Connection Conversation Manager | diag_CuCsMgr_*.uc |
| MiuSIP - (all levels) | Connection Conversation Manager | diag_CuCsMgr_*.uc |
| MiuSIPStack - (all levels) | Connection Conversation Manager | diag_CuCsMgr_*.uc |
| Mixer - (all levels) | Connection Mixer | diag_CuMixer_*.uc |
| Cisco Smart Software
                                          				  Licensing Issues |
| Licensing | CuSlmSvr (all levels) | Connection Smart License Manager Server | diag_CuSlmSvr_*.uc |
| Tenant Partitioning
                                          				  Issues |
| Tenant Partitioning | Cuca | Connection Tomcat Application | diag_Tomcat_*.uc |
| VMREST (all levels) | Connection Tomcat Application | diag_Tomcat_*.uc |
| Video Greetings Issues |
| Video Greetings | CDE (level 1, 10 to 17, 20, 21) | Connection Conversation Manager | diag_CuCsMgr_*.uc |
| ConvSub (level 01 to 05) | Connection Conversation Manager | diag_CuCsMgr_*.uc |
| MiuIO (level 11 to 13, 25, 27) | Connection Conversation Manager | diag_CuCsMgr_*.uc |
| Miu Sip/Miu Sip Stack (all levels) | Connection Conversation Manager | diag_CuCsMgr_*.uc |
| MiuMethods/MiuCall (all levels) | Connection Conversation Manager | diag_CuCsMgr_*.uc |
| Mixer (levels 01 to 04) | Connection Mixer | diag_CuMixer_*.uc |
| Video (level 10 and 11) | Connection Conversation Manager | diag_CuCsMgr_*.uc |
| SAML SSO Issues |
| SAML SSO | CLI Command to activate SAML SSO logs: admin: set samltrace level <trace-level> where trace-level can be BEBUG, INFO, WARNING, ERROR, or FATAL CLI Command to check trace level: admin: show samltrace level | Cisco Tomcat Cisco Tomcat Security Cisco SSO | ssosp*.log ssoApp.log |
|  |  |  |  |
| Miscellaneous
                                          				  Issues |
| Synchronization traces between Unity Connection and Exchange | CsMbxSync | Connection Mailbox Sync | diag_CuMbxSync_*.uc |
| Synchronization traces between Unity Connection and Gmail Server | CuGSuiteSyncSrv | Connection GSuite Sync Service | diag_CuGSuiteSyncSrv_*.uc |
| Exchange EWS calls in MbxSync diag | CsEws | Connection Mailbox Sync | diag_CuMbxSync_*.uc |
| EWS notification in Jetty web service diags | EWSNotify | Connection Jetty |  |
| Exchange 2003 webdav protocol diags | CsWebDav | Connection Mailbox Sync | diag_CuMbxSync)_*.uc |
| Activities of Connection external service | CuEsd | Connection Tomcat Application | diag_Tomcat_*.uc |
| Message deposition on Connection | MTA | Connection Message Transfer Agent | diag_CuMta_*.uc |
| CUCA test buttons for UM service and UM user pages | Cuca | Connection Tomcat Application | diag_Tomcat_*.uc |
| Autodiscovery feature diags | MbxLocator | Connection Mailbox Sync | diag_CuMbxSync_*.uc |
| MbxSyncQ and EWSNotiftQ events | DBEvent | Connection DB Event Publisher | diag_DbEventPublisher_*.uc |
| PIN
                                             					 Synchronization Issues |
| PIN
                                             					 Synchronization Issues | AxlAccess (level 00,01) | Connection Conversation Manager | diag_CuCsMgr_*.uc |
| Bulk
                                             					 Administration Tool (all levels) | Tomcat
                                             					 Logs | diag_Tomcat_*.uc |
| CiscoPCA
                                             					 (level 00,01,02,13) | Tomcat
                                             					 Logs | diag_Tomcat_*.uc |
| Cuca
                                             					 (all levels) | Tomcat
                                             					 Logs | diag_Tomcat_*.uc |
| CuCsMgr
                                             					 (level 10) | Connection Conversation Manager | diag_CuCsMgr_*.uc |
| VMREST
                                             					 (all levels) | Tomcat
                                             					 Logs | diag_Tomcat_*.uc |
| CDL
                                             					 (level 10 and 11) | Connection Conversation Manager | diag_CuCsMgr_*.uc |
| ConvSub
                                             					 (level 01,03,04,05) | Connection Conversation Manager | diag_CuCsMgr_*.uc |

| Note | Enabling Cisco Unity Connection Serviceability macro traces
                                          		  decreases system performance. Enable traces only for troubleshooting purposes. |
|---|---|

| Problem Area | Traces to Set | RTMT Service to Select | Trace Log Filename |
|---|---|---|---|
| Audio Issues |
| Audio quality | Media (Wave) Traces | Connection Conversation Manager | diag_CuCsMgr_*.uc |
| Connection Mixer | diag_CuMixer_*.uc |
| Call Issues |
| Call control | Call Control (Miu) Traces (expand the macro trace to select SIP
                                             					 or SCCP) | Connection Conversation Manager | diag_CuCsMgr_*.uc |
| Call flow | Call Flow Diagnostics | Connection Conversation Manager | diag_CuCsMgr_*.uc |
| ViewMail for Outlook (recording or playback by phone) | Call Control (Miu) Traces (expand the macro trace to select SIP
                                             					 or SCCP) | Connection Conversation Manager | diag_CuCsMgr_*.uc |
| Client Issues |
| Cisco Unified Personal Communicator client (IMAP-related issues) (see also “ Cisco
                                                						Unified Personal Communicator client (IMAP-related issues) ” in Table 1-1 ) | Call Flow Diagnostics | Connection Conversation Manager | diag_CuCsMgr_*.uc |
| ViewMail for Outlook (sending and receiving messages) (see also “ ViewMail
                                                						for Outlook (sending and receiving messages) ” in Table 1-1 ) | Call Flow Diagnostics | Connection Conversation Manager | diag_CuCsMgr_*.uc |
| ViewMail for Outlook | Connection Conversation Manager | diag_CuCsMgr_*.uc |
| Connection IMAP Server | diag_CuImapSvr_*.uc |
| Connection Message Transfer Agent | diag_MTA_*.uc |
| Connection Tomcat Application | diag_Tomcat_*.uc |
| Connection REST Service | diag_Tomcat_*.uc |
| Connection Mailbox Sync | diag_CuMbxSync_*.uc |
| Cisco Unity Connection
                                          				  Serviceability Issues |
| Cisco Unity Connection Serviceability | Connection Serviceability Web Service | Connection Tomcat Application | diag_Tomcat_*.uc |
| Conversation
                                          				  Issues |
| Conversations | Conversation Traces | Connection Conversation Manager | diag_CuCsMgr_*.uc |
| Message Issues |
| Dispatch messages (see also “ Dispatch
                                                						messages ” in Table 1-1 ) | Call Flow Diagnostics | Connection Conversation Manager | diag_CuCsMgr_*.uc |
| IMAP messages (see also “ IMAP
                                                						messages ” in Table 1-1 ) | Call Flow Diagnostics | Connection Conversation Manager | diag_CuCsMgr_*.uc |
| Message delivery and retrieval (see also “ Message
                                                						delivery and retrieval ” in Table 1-1 ) | Message Tracking Traces | Connection Message Transfer Agent | diag_MTA_*.uc |
| Connection System Agent | diag_CuSysAgent_*.uc |
| Connection Conversation Manager | diag_CuCsMgr_*.uc |
| Connection Tomcat Application | diag_Tomcat_*.uc |
| Connection IMAP Server | diag_CuImapSvr_*.uc |
| NDRs (see also “ NDRs ”
                                             					 in Table 1-1 ) | Call Flow Diagnostics | Connection Conversation Manager | diag_CuCsMgr_*.uc |
| Notifications not sent (see also “ Notifications
                                                						not sent ” in Table 1-1 ) | Traces for Other Notification Problems (expand the macro trace
                                             					 to select SIP or SCCP) | Connection Conversation Manager | diag_CuCsMgr_*.uc |
| Connection Notifier | diag_CuNotifier_*.uc |
| Message not synchronized in Unified Messaging | Single Inbox Traces | Connection Mailbox Sync | diag_CuMbxSync_*.uc |
| MWI Issues |
| MWIs | Traces for MWI problems (expand the macro trace to select SIP or
                                             					 SCCP) | Connection Conversation Manager | diag_CuCsMgr_*.uc |
| Connection Notifier | diag_CuNotifier_*.uc |
| Networking
                                          				  Issues |
| Intrasite Networking replication (see also “ Intrasite
                                                						Networking replication ” in Table 1-1 ) | Digital Networking | Connection Digital Networking Replication Agent | diag_CuReplicator_*.uc |
| VPIM message delivery (see also “ VPIM
                                                						message delivery ” in Table 1-1 ) | Call Flow Diagnostics | Connection Conversation Manager | diag_CuCsMgr_*.uc |
| Startup Issues |
| Unity Connection startup fails | Unity Startup | Connection Conversation Manager | diag_CuCsMgr_*.uc |
| Connection Notifier | diag_CuNotifier_*.uc |
| Text to Speech
                                          				  Issues |
| Text to Speech | Call Control (Miu) Traces (expand the macro trace to select SIP
                                             					 or SCCP) | Connection Conversation Manager | diag_CuCsMgr_*.uc |
| Media (Wave) Traces | Connection Conversation Manager | diag_CuCsMgr_*.uc |
| Connection Mixer | diag_CuMixer_*.uc |
| Text to Speech (TTS) Traces | Connection Conversation Manager | diag_CuCsMgr_*.uc |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | In Cisco Unity Connection Serviceability, on
                                             			 the Trace menu, do either of the following: | select Micro Traces to enable micro
                                                      					 traces. Select Macro Traces to enable macro
                                                      					 traces. |
| Step 2 | On the Micro Traces or Macro Traces page, in the Server field,
                                             			 select the name of the Unity Connection server and select Go . |  |
| Step 3 | Do either of the following: | In the Micro Trace field, select the
                                                      					 micro trace that you want to set and select Go . Check the check box of the macro trace
                                                      					 that you want to enable. |
| Step 4 | Under Micro Traces or Macro Traces, check the check boxes for the
                                             			 micro-trace or macro-trace levels that you want to set and select Save . |  |
| Step 5 | Reproduce the problem. |  |
| Step 6 | To collect the trace log files, launch the Real-Time Monitoring
                                             			 Tool (RTMT). For detailed instructions, see the “Working with Trace and Log
                                             			 Central” chapter of the applicable Cisco Unified Real-Time Monitoring Tool
                                                				Administration Guide , available at http://www.cisco.com/en/US/products/ps6509/prod_maintenance_guides_list.html . | You can access the trace log files using the
                                                				command line interface (CLI). For information, see the applicable Command Line Interface Reference Guide for
                                                   				  Cisco Unified Solutions at http://www.cisco.com/en/US/products/ps6509/prod_maintenance_guides_list.html . |
| Step 7 | In RTMT, on the System menu, select Tools > Trace > Trace & Log
                                                   				  Central . |  |
| Step 8 | In the Trace & Log Central tree hierarchy, double-click Collect Files . |  |
| Step 9 | In the Select CUC Services/Application tab, check the check boxes
                                             			 for the applicable services and select Next . |  |
| Step 10 | In the Select System Services/Applications tab, select Next . |  |
| Step 11 | In the Collection Time group box, specify the time range for which
                                             			 you want to collect traces. |  |
| Step 12 | In the Download File option group box, specify the options you
                                             			 want for downloading traces. |  |
| Step 13 | Select Finish . |  |
| Step 14 | To view the trace files that you collected, you can use the Local
                                             			 Browse option of the trace collection feature. |  |
| Step 15 | In Cisco Unity Connection Serviceability, disable the traces that
                                             			 you enabled in Step 3 and Step 4 , then select Save . |  |

| Note | Enabling Cisco Unified Serviceability traces decreases system performance. Enable traces only for troubleshooting purposes. |
|---|---|

| Problem Area | Traces to Set | RTMT Service to Select |
|---|---|---|
| Backing up and restoring | Cisco DRF Local Cisco DRF Master | Cisco DRF Local Cisco DRF Master |
| LDAP synchronization | Cisco DirSync | Cisco DirSync |
| Web application sign-in | Cisco CCMRealm Web Service | Cisco CallManager Realm |

| Step 1 | In Cisco Unified Serviceability, on the
                                          			 Trace menu, select Troubleshooting Trace
                                             				Settings . |
|---|---|
| Step 2 | On the Troubleshooting Trace Settings page,
                                          			 under Directory Services, check the check box for the trace that you want to
                                          			 enable and select Save . |
| Step 3 | Reproduce the problem. |
| Step 4 | To collect the trace log files, launch the
                                          			 Real-Time Monitoring Tool (RTMT). For detailed instructions, see the “Working
                                          			 with Trace and Log Central” chapter of the applicable Cisco Unified Real-Time Monitoring Tool
                                             				Administration Guide , available at http://www.cisco.com/en/US/products/ps6509/prod_maintenance_guides_list.html . You can access the trace log files using the
                                             				command line interface (CLI). For information, see the applicable Command Line Interface Reference Guide for
                                                				  Cisco Unified Communications Solutions at http://www.cisco.com/en/US/products/ps6509/prod_maintenance_guides_list.html . |
| Step 5 | In RTMT, on the System menu, select Tools > Trace > Trace & Log
                                                				  Central . |
| Step 6 | In the Trace & Log Central tree
                                          			 hierarchy, double-click Collect Files . |
| Step 7 | In the Select CUC Services/Application tab,
                                          			 select Next . |
| Step 8 | In the Select System Services/Applications
                                          			 tab, check the check boxes for the applicable service and select Next . |
| Step 9 | In the Collection Time group box, specify
                                          			 the time range for which you want to collect traces. |
| Step 10 | In the Download File option group box,
                                          			 specify the options you want for downloading traces. |
| Step 11 | Select Finish . |
| Step 12 | To view the trace files that you collected,
                                          			 you can use the Local Browse option of the trace collection feature. |
| Step 13 | In Cisco Unity Connection Serviceability,
                                          			 disable the traces that you enabled in Step 2 , and select Save . |