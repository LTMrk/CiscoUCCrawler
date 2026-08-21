---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-customer-voice-portal-cvp-12-5-user-guide-ccvp-b-89a0176b13
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/customer_voice_portal/cvp_12_5/user/guide/ccvp_b_1251-operations-guide-for-cisco-unified-customer-voice-portal/ccvp_b_1251-operations-guide-for-cisco-unified-customer-voice-portal_chapter_010.html
retrieved_at: 2026-08-21T03:08:14.490601+00:00
---

Operations Guide for Cisco Unified Customer Voice Portal, Release 12.5(1)

# Operations Guide for Cisco Unified Customer Voice Portal, Release 12.5(1)

Updated: February 2, 2020

Chapter: Configure Unified CVP Logging and Event Notifications

## Chapter: Configure Unified CVP Logging and Event Notifications

# Configure Unified CVP Logging and Event Notifications

Unified CVP provides information about component device
                        status and interaction through

Logs, which are
                              presented in text format and can be viewed using Cisco serviceability
                              tools

Statistics, which can be viewed using the Unified
                              CVP Operations Console

This chapter also provides
                        information about CVP SNMP-Raise/Clear Mappings , and contains the following topics:

## Using Syslog

Unified CVP allows you
                           to configure the  primary and backup syslog servers with the forked primary and forked backup servers. Failover from primary
                           to backup server is not guaranteed. When the
                           primary syslog server goes down (the entire machine, not just the
                           syslog receiver application), Unified CVP relies on the host operating system
                           and the Java Runtime Environment for notification that the destination is not
                           reachable. Because the semantics of this notification do not guarantee
                           delivery, Unified CVP cannot guarantee failover.

## Using Logs to Interpret Events

You can use
                           the CVPLogMessages.xml file to help interpret events.
                           This file contains all messages (or notifications) on SNMP events and/or
                           through Syslog.

Each event in the CVPLogMessages.xml field containing information that
                           must be useful for correcting any problems indicated by the event.

The sections that
                           follow provide information about editing, uploading, and downloading the
                           CVPLogMessages.xml file from the Operations
                           Console.

### Editing the Log Messages XML File

The log messages XML file, CVPLogMessages.xml , defines the severity,
                              destination (SNMP management station or Syslog server) and possible resolution
                              for Unified CVP
                              log messages. This file also identifies an event type identifier and message
                              text identifier for each event. The text for these identifiers is stored in the
                              resource properties file, CVPLogMessagesRes.properties .

Each
                              Unified CVP Call Server, VXML Server, and Reporting Server has a log messages
                              XML file and log message file. You can edit the CVPLogMessages.xml file on a particular Unified CVP
                              server to customize the severity, destination and possible resolution for each
                              event that the server generates. You can also edit the CVPLogMessagesRes.properties file to change the text
                              of the message that is generated when an event occurs on that server.

Use any plain-text editor (one that does not create any markup) or XML
                              editor to edit the CVPLogMessages.xml file. Use a
                              resource file editor to edit the CVPLogMessagesRes.properties file. If a resource
                              file editor is not available, use a text editor.

Message
                                          Element

Possible
                                          Values

What it
                                          Means

Name

Resource="identifier"

Identifies the event type described in
                                          the CVPLogMessagesRes.properties file.

Body

Resource="identifier"

Identifies the message text described in the CVPLogMessagesRes.properties file.

Severity

0 to
                                          6

Identifies the severity level of the event.

SendToSNMP

True or false

Set to true, to send this message,
                                          when logged, to an SNMP manager, if one is configured.

SendToSyslog

True or false

Set to true to send this message, when
                                          logged, to a Syslog server, if one is configured.

SNMPRaise

True or false

Set to true to identify this message,
                                          when logged, as an SNMP raise event, which the SNMP management station  uses
                                          to initiate a task or automatically take an action.

Set to false to
                                          identify this message as an SNMP clear when sent to an SNMP management station.
                                          An SNMP clear event usually corresponds to an SNMP raise event, indicating that
                                          the problem causing the raise has been corrected. An administrator on an SNMP
                                          management station can correlate SNMP raise events with SNMP clear
                                          events.

Save the file and restart the CVP server to implement the changes.

### Unified CVP Event Severity Levels

The following table describes the
                              available severity levels for
                              Unified CVP events. You can set
                              the severity level for an event by editing the log messages XML file,
                              CVPLogMessages.xml, on the server that generates events. For instructions on
                              editing this file, see Editing the Log Messages XML File .

Level

Severity

Purpose

EMERGENCY

0

System or service is unusable

ALERT

1

Action must be taken
                                          immediately

CRITICAL

2

Critical condition, similar to ALERT, but not
                                          necessarily requiring an immediate action

ERROR

3

An error condition that does
                                          not necessarily impact the ability of the service to continue to
                                          function

WARN

4

A warning about a bad condition, which is not
                                          necessarily an error

NOTICE

5

Notification about interesting system-level
                                          conditions, which are not errors

INFO

6

Information about internal
                                          flows or application or per-request information, not system-wide
                                          information

## VoiceXML Logs

### About VoiceXML Logs

VoiceXML logs record Unified CVP
                              system-specific information, such as heartbeat status. By default, VoiceXML
                              logs are stored in the \Cisco\CVP\logs\VXML folder.

The table that
                              follows describes the logs that VoiceXML creates.

Log
                                          Type

Log Name

Description

Infrastructure

CVP.<timestamp>.log

Unified CVP logs for the VoiceXML Service: This
                                          includes Notice, Info, and Debug logs. With Debug turned on, you can also see
                                          Call, Message, and Method trace types of logs.

Error messages

Error.<timestamp>.log

Unified CVP error log: This contains any error that
                                          Unified CVP Services and message layer has generated.

### Correlate Unified
                           	 CVP/Unified ICME Logs with VXML Server Logs

When using the VXML
                                 		  Server option in the Unified CVP solution, you can correlate Unified
                                 		  CVP/ Unified ICME logs
                                 		  with VoiceXML logs. Pass the Call ID to the VXML Server by URL. Building upon
                                 		  the URL used in the previous example, the URL is as follows: http://VXML Server
                                    			 IPAddress:7000/CVP/Server?application=Chapter1_HelloWorld&callid=XXXXX-XXXXX-XXXXXX-XXXXXX

The following
                                 		  procedure describes how to configure logging.

In the Unified ICME script, use the formula editor to set ToExtVXML[1]. Set the value of
                                          			 ToExtVXML[1] variable to concatenate("callid=",Call.user.media.id)

Always
                                                               						include Call ID when sending the call to the Unified CVP VXML Server using the
                                                               						Comprehensive call flow model. The Call ID can also be used in Unified CVP VXML
                                                               						Server (standalone) solutions.

When you
                                                               						concatenate multiple values, use a comma for the delimiter.

The value
                                                               						of ICMInfoKeys must contain RouterCallKey, RouterCallDay, and
                                                               						RouterCallKeySequenceNumber separated by a “-“.

For
                                                               						example,
                                                               						concatenate("ICMInfoKeys=",Call.RouterCallKey,"-",Call.RouterCallDay,"-",Call.RouterCallKeySequenceNumber).

### About Unified CVP VXML Server Logs

Unified CVP VXML Server logs record interactions between the Unified CVP VXML Server and the
                              server that hosts the VoiceXML applications. By default, Unified CVP VXML Server logs are
                              stored in the /Cisco/CVP/VXMLServer/logs folder.

The following table describes the logs that Unified CVP VXML Server creates:

Log
                                          Type

Log Name

Description

Unified CVP VXML Server Call Log

call_log<timestamp>.txt

Records a single line for every application visit
                                          handled by the  Unified CVP VXML Server.

Unified CVP VXML Server Call Error Log

error_log<timestamp>.txt

Records errors that occur outside the realm of a
                                          particular application.

Unified CVP VXML Server Administration History Log

admin_history<timestamp>.txt

Records information from Unified CVP VXML Server
                                          administration scripts.

The Unified CVP VXML Server Call Error Log contains the following error
                              codes:

Error Code 40 -- System Unavailable

This is returned if the application server is unavailable (shutdown,
                                    network connection disabled, and so forth)

Error Code 41
                                    -- App Error

This is returned if some Unified CVP VXML Server-specific error
                                    occurs (For example, java exception).

Error Code 42 -- App
                                    Hangup

This is returned to Unified CVP if the Hang Up element is
                                    used without being preceded by a Subdialog_Return element.

Error Code 43 -- Suspended

This is returned if the Unified CVP VXML Server application is suspended.

Error Code 44 -- No
                                    Session Error

This is returned when an emergency error occurs
                                    (for example, an application is called that has not been loaded in the Unified CVP VXML Server application).

Error Code 45 -- Bad Fetch

This is returned when the Unified CVP VXML Server encounters a bad fetch situation.
                                    This code is returned when a .wav file or an external grammar file is
                                    not found.

### About VoiceXML
                           	 Application Logging

The Unified CVP VXML
                              		Server creates several logs for each individual VoiceXML application. By
                              		default, these application logs - with the exception of CVPDatafeedLog and
                              		CVPSNMPLog - are stored in the /Cisco/CVP/VXMLServer/applications/<NAME of
                              		APPLICATION>/logs folder.

Application developers have to use the above folder for application
                                          		  and custom logs.

Configure these logs
                              		using Call Studio:

The following table
                              		  describes the logs that are created for each application:

Application Logger Type

Log Name

Description

ActivityLog

activity_log<timestamp>.txt

Records
                                          						all application activity, showing which elements are entered and exited during
                                          						a call.

Default
                                          						setting: on

ErrorLog

error_log<timestamp>.txt

Records
                                          						all error messages for the application.

Default
                                          						setting: on

AdminLog

admin_history<timestamp>.txt

Records
                                          						information from application-specific administration scripts.

Default
                                          						setting: on

CVPDatafeedLog

CVPDatafeed.log.

Listens
                                          						for logging events and provides Unified CVP VXML Server and VoiceXML Service
                                          						data to the Unified CVP Reporting Server. The Unified CVP Reporting Server
                                          						stores this information in a reporting database so that it is available for
                                          						later review.

One
                                          						CVPDatafeedLog is created per application.

Default
                                          						setting: on

CVPSNMPLog

CVPSNMP.log.

Listens
                                          						for a set of events and sends information about these events to the SNMP log,
                                          						Syslog, or Unified CVP log.

Default
                                          						setting: on

DebugLog

debug_log<timestamp>.txt.

Creates a
                                          						single file per call that contains all HTTP requests and responses that
                                          						occurred between a IOS Gateway and Unified CVP VXML Server during the call
                                          						session.

Default
                                          						setting: off

## About Event Statistics

You
                           can monitor the following statistics through the Operations Console Control
                           Center:

Device statistics

Infrastructure statistics

ICM Service call
                                 statistics

IVR Service call statistics

SIP Service call statistics

Gateway statistics

VXML
                                 Server statistics

Reporting Server
                                 statistics

### Infrastructure Statistics

Unified CVP
                              infrastructure statistics include realtime and interval data on the Java
                              Virtual Machine (JVM), threading, and Licensing.

You can access
                              these statistics by choosing Control Center from the System menu and then
                              selecting a device. See the Operations Console topic Viewing
                                 Infrastructure Statistics for more information.

Access infrastructure statistics either by:

Selecting System > Control Center , selecting a device,
                                    clicking the Statistics icon in the toolbar, and then selecting the Infrastructure tab.

Selecting a device
                                    type from the Device Management menu, selecting a device,
                                    clicking the Statistics icon in the toolbar, and then selecting the Infrastructure tab.

The following
                              table describes Licensing statistics.

Statistic

Description

Realtime
                                             Statistics

Port Licenses Available

The number of port licenses available
                                          for the processing of new calls. Exactly one port license is used per call,
                                          independent of the call's traversal through the individual Call Server
                                          services.

Current Port Licenses in Use

The number of port licenses currently
                                          in use on the Call Server. One port license is used per call,
                                          independent of the call's traversal of the individual Call Server services.

Current
                                          Port Licenses State

There are four threshold levels of port license usage: safe, warning,
                                          critical and failure. An administrator may set the required percentage of port
                                          licenses in use needed to reach a given threshold level, with the exception of
                                          the failure level which is reached when the number of ports checked out is
                                          equal to the number of licenses ports.

Interval Statistics

Start Time

The time the system
                                          started collecting statistics for the current interval.

Duration Elapsed

The amount of time that has elapsed since the
                                          start time in the current interval.

Interval Duration

The interval at which statistics are collected. The
                                          default value is 30 minutes.

Total New Port License Requests

The number of port
                                          license checkout requests made in the current interval. For each port license
                                          checkout request, this metric is
                                          increased by one, regardless of whether if checks out a new port license.

Average License Requests/Minute

The average number of port license
                                          checkout requests made per minute in the current interval. This metric is
                                          calculated by dividing the port license requests metric by the number of
                                          minutes elapsed in the current interval.

Maximum Port Licenses Used

The maximum number of port licenses used during
                                          this time interval.

Aggregate
                                             Statistics

Start
                                          Time

The time the service started
                                          collecting statistics.

Duration Elapsed

The amount
                                          of time that has elapsed since the service start time.

Total New Port License Requests

The number of port license checkout
                                          requests made since the system was started. For each port license checkout, this metric is increased by one, regardless of
                                          whether if checks out a new port license.

Average License Requests /Minute

The average number of port license checkout
                                          requests made per minute since the system was started. This metric is
                                          calculated by dividing the aggregate port license requests metric by the number
                                          of minutes elapsed since the system was started.

Peak Port Licenses
                                          Used

The peak number of simultaneous
                                          port licenses used since the start of the system. When a port checkout occurs,
                                          this metric is set to the current port licenses in use metric if that value is
                                          greater than this metric's current peak value.

Total Denied Port License
                                          Requests

The number of  port license
                                          checkout requests that were denied since the start of the system. A port license checkout request is denied if the number
                                          of port
                                          licenses checked out at the time of the request is equal to the total number of
                                          port license available. When a port license checkout is denied, the call does
                                          not receive regular treatment (the caller may hear a busy tone or an error
                                          message).

The following table describes
                              thread pool system statistics. The thread pool is a cache of threads, used by
                              Unified CVP components only, for processing relatively short tasks. Using a
                              thread pool eliminates the waste of resources encountered when rapidly creating
                              and destroying threads for these types of tasks.

Statistic

Description

Realtime
                                             Statistics

Idle Threads

The number of idle threads waiting for
                                          some work

Running Threads

The number of running thread pool threads currently processing some work.

Core
                                          Threads

The number of
                                          thread pool threads that will never be destroyed no matter how long they remain
                                          idle

Maximum Threads

The maximum
                                          number of thread pool threads that will ever exist simultaneously

Peak
                                          Threads Used

The peak
                                          number of thread pool threads ever simultaneously tasked with some work to
                                          process

The following
                              table describes Java Virtual Machine statistics.

Statistic

Description

Realtime
                                             Statistics

Peak Memory Usage

The greatest amount of memory used by the Java
                                          Virtual machine since startup. The number reported is in megabytes and
                                          indicates the peak amount of memory ever used simultaneously by this Java
                                          Virtual Machine.

Current Memory Usage

The
                                          current number of megabytes of memory used by the Java Virtual Machine.

Total
                                          Memory

The amount of memory in
                                          megabytes available to the Java Virtual Machine. The number  indicates how much system memory is available for the Java
                                          Virtual Machine.

Available Memory

The amount
                                          of available memory in the Java Virtual Machine. The number reported is in
                                          megabytes and indicates how much of the current system memory claimed by the
                                          Java Virtual Machine is not currently being used.

Threads in Use

The number of threads currently in use in the Java
                                          Virtual Machine. This number includes all of the Unified CVP standalone and
                                          thread pool threads, and  those threads created by the Web Application
                                          Server running within the same JVM.

Peak Threads in Use

The greatest amount of threads used
                                          simultaneously in the Java Virtual Machine since startup. The peak number of
                                          threads used by thw Java Virtual Machine includes all Unified CVP
                                          standalone and thread pool threads, and threads created by the Web
                                          Application Server running within the same JVM.

Uptime

The time that the Java Virtual Machine
                                          has been running. This time is measured in hh:mm:ss and shows the amount of
                                          elapsed time since the Java Virtual Machine process began.

### ICM Service Call Statistics

The ICM Service call statistics include data on
                              calls currently being processed by the ICM service, new calls received during a
                              specified interval, and total calls processed since start time.

Access ICM Service statistics either by:

Selecting System > Control Center , selecting a CVP
                                    Call Server, clicking the Statistics icon in the toolbar, and
                                    then selecting the ICM tab.

Selecting Device Management > CVP Call Server , selecting a Call
                                    Server, clicking the Statistics icon in the toolbar, and then
                                    selecting the ICM tab.

The following
                              table describes ICM Service call statistics.

Statistic

Description

Realtime
                                             Statistics

Active Calls

The
                                          current number of calls being serviced by the Unified Intelligent Contact Management (Unified ICM) Server for a Unified CVP
                                          Call
                                          Server. This value represents the calls currently being serviced by the
                                          Unified ICM for the Unified CVP Call Server for follow-on routing to a Contact Center
                                          agent.

Active SIP Call Legs

The ICM
                                          Server can accept VoIP calls that originate using either the
                                          Session Initiation Protocol (SIP). Active SIP Call Legs
                                          indicates the number of calls received by the Unified ICM Server from the
                                          Unified CVP Call Server using the SIP protocol.

Active VRU Call Legs

The current number of calls receiving Voice
                                          Response Unit (VRU) treatment from the Unified ICM Server. The VRU treatment includes
                                          playing pre-recorded messages, asking for Caller Entered Digits (CED) or Speech
                                          Recognition Techniques to understand the customer request.

Active ICM
                                          Lookup Requests

Calls originating
                                          from an external Unified CVP VXML Server need call routing instructions from the Unified ICM
                                          Server. Active Lookup Requests indicates the current number of external Unified CVP VXML Server call routing requests sent
                                          to the ICM Server.

Active Basic Service Video Calls
                                          Offered

The current number of
                                          simultaneous basic service video calls being processed by theUnified  ICM service where
                                          video capability was offered.

Active Basic Service Video Calls
                                          Accepted

The current number of
                                          simultaneous calls that were accepted as basic service video calls and are
                                          being processed by the Unified  ICM service.

Interval
                                             Statistics

Start Time

The time at which the current interval began.

Duration
                                          Elapsed

The amount of time that has
                                          elapsed since the current interval began.

Interval Duration

The time interval at which statistics are collected. The
                                          default value is 30 minutes.

New Calls

The number of new calls received by the Unified ICM application for follow-on Voice Response Unit (VRU)
                                          treatment and routing to a Contact Center agent during the current
                                          interval.

SIP Call Legs

The Unified ICM application accepts VoIP calls that originate from the Session Initiation Protocol (SIP) Protocol.
                                          Interval SIP Call Legs is an interval specific snapshot metric indicating the
                                          number of calls received by the ICM application from SIP during the current
                                          interval.

VRU Call Legs

The number of calls
                                          receiving VRU treatment from the Unified  ICM application. The VRU treatment includes playing pre-recorded
                                          messages, asking for Caller Entered Digits (CED) or speech recognition
                                          techniques to understand the customer request during the current interval.

ICM Lookup
                                          Requests

Calls originating in an
                                          external Unified CVP VXML Server need call routing instructions from the Unified ICM application. Interval Lookup Requests
                                          is an interval
                                          specific metric indicating the number of external Unified CVP VXML Server call routing
                                          requests sent to the Unified ICM application during the current interval.

Basic
                                          Service Video Calls Offered

The
                                          number of offered basic service video calls processed by the Unified  ICM service during
                                          the current interval.

Basic Service Video Calls
                                          Accepted

The number of basic service
                                          video calls accepted and processed by the Unified  ICM service during the current
                                          interval.

Aggregate Statistics

Start Time

The time the service started collecting statistics.

Duration Elapsed

The amount of time that has elapsed since the
                                          service start time.

Total Calls

The total number of new calls received by the
                                          Unified ICM application for follow-on VRU treatment and routing to a Contact Center agent since system start
                                          time.

Total
                                          SIP Call Legs

The Unified ICM application can accept VoIP calls that originate from the Session Initiation Protocol (SIP) Protocol.
                                          Total SIP Switch Legs is a metric indicating the number of calls received
                                          by the ICM application by SIP since system start time.

Total VRU Call
                                          Legs

The number of calls that
                                          have received VRU treatment from the Unified ICM application since system start time. The VRU treatment
                                          includes playing pre-recorded messages, asking for Caller Entered Digits (CED)
                                          or Speech Recognition Techniques to understand the customer request.

Total ICM
                                          Lookup Requests

Calls originating
                                          in an external Unified CVP VXML Server need call routing instructions from the Unified ICM application. Total Lookup Requests
                                          is a metric
                                          indicating the total number of external Unified CVP VXML Server call routing requests sent
                                          to the Unified ICM application since system start time.

Total Basic Service Video Calls
                                          Offered

The number of newly
                                          offered basic service video calls processed by the Unified ICM service since system
                                          start time.

Total Basic Service Video Calls Accepted

The number of new basic service video calls
                                          accepted and processed by the Unified ICM service since system start
                                          time.

### IVR Service Call
                           	 Statistics

The IVR service call
                              		statistics include data on calls currently being processed by the IVR service,
                              		new calls received during a specified interval, and total calls processed since
                              		the IVR service started.

Access IVR Service
                              		statistics either by:

Selecting System > Control
                                          				  Center , selecting a Call Server, clicking the Statistics icon in the toolbar, and then selecting
                                    			 the IVR tab.

Selecting Device
                                          				  Management > CVP Call Server , selecting a Call
                                    			 Server, clicking the Statistics icon in the toolbar, and then selecting
                                    			 the IVR tab.

The following table
                              		describes the IVR Service call statistics.

Statistic

Description

Realtime Call Statistics

Active Calls

The number of
                                          				active calls being serviced by the IVR service.

Active HTTP
                                          				Requests

The number of
                                          				active HTTP requests being serviced by the IVR service.

Interval Statistics

Start Time

The time the
                                          				system starts collecting statistics for the current interval.

Duration
                                          				Elapsed

The amount of
                                          				time that has elapsed since the start time in the current interval.

Interval
                                          				Duration

The interval at
                                          				which statistics are collected. The default value is 30 minutes.

Peak Active
                                          				Calls

Maximum number
                                          				of active calls handled by the IVR service simultaneously.

New Calls

Metric that
                                          				counts the number of New Call requests received from the IOS Gateway. A New
                                          				Call includes the Switch leg of the call and the IVR leg of the call. This
                                          				metric counts the number of New Call Requests received by the IVR Service.

Calls Finished

Metric that
                                          				counts the number of Unified CVP Calls that have finished during this interval.
                                          				A Call, for the purpose of the Call Finished metric, includes both the Switch
                                          				leg and the IVR leg of the Unified CVP call. When both legs of the call are
                                          				finished, the Calls
                                             				  Finished metric increases.

Average Call
                                          				Latency

The average
                                          				amount of time in milliseconds that it takes the IVR Service to process a New
                                          				Call or Call Result Request.

Maximum Call
                                          				Latency

The maximum
                                          				amount of time in milliseconds that it has taken for the IVR Service to process
                                          				a New Call Request or a Request Instruction Request.

Minimum Call
                                          				Latency

The minimum
                                          				amount of time in milliseconds it took for the IVR Service to process a New
                                          				Call Request or a Request Instruction Request.

Peak Active
                                          				HTTP Requests

Active HTTP
                                          				Requests is a metric that indicates the current number of simultaneous HTTP
                                          				requests being processed by the IVR Service. Peak Active Requests is a metric
                                          				that represents the maximum simultaneous HTTP requests being processed by the
                                          				IVR Service.

Total HTTP
                                          				Requests

The number of
                                          				HTTP Requests received from a client by the IVR Service.

Average HTTP
                                          				Requests/second

The average
                                          				number of HTTP Requests the IVR Service receives per second.

Peak Active HTTP
                                          				Requests/second

HTTP Requests
                                          				per Second is a metric that represents the number of HTTP Requests the IVR
                                          				Service receives each second from all clients. Peak HTTP Requests per Second is
                                          				the maximum number of HTTP Requests that were processed by the IVR Service in
                                          				any given second. This is also known as high water marking.

Aggregate Statistics

Start Time

The time the
                                          				service started collecting statistics.

Duration Elapsed

The amount of
                                          				time that has elapsed since the service start time.

Total New Calls

Metric that
                                          				counts the number of New Call requests received from the IOS GatewayUsing
                                          				Unified ICME Warm. A New Call includes the Switch leg of the call and the IVR
                                          				leg of the call. Total New Calls is a metric that represents the number of new
                                          				calls received by the IVR Service since system startup.

Peak Active
                                          				Calls

The maximum
                                          				number of simultaneous calls processed by the IVR Service since the service
                                          				started.

Total HTTP
                                          				Requests

Metric that
                                          				represents the number of HTTP Requests received from all clients. This metric
                                          				is the total number of HTTP Requests received by the IVR Service since system
                                          				startup.

Peak Active
                                          				HTTP Requests

Peak Active
                                          				HTTP Requests is a metric that indicates the current number of simultaneous
                                          				HTTP requests processed by the IVR Service. Maximum number of active HTTP
                                          				requests processed at the same time since the IVR service started. This is also
                                          				known as high water marking.

Total Agent
                                          				Video Pushes

The number of
                                          				videos pushed by agents since system start time.

Total Agent
                                          				Initiated Recordings

The number of
                                          				video recordings by agents since system start time.

Total Agent
                                          				VCR Control Invocations

The number of
                                          				video VCR controls invoked by agents since system start time.

### SIP Service Call Statistics

The SIP service call statistics include data on calls currently being
                              processed by the SIP service, new calls received during a specified interval,
                              and total calls processed since the SIP service started.

Access SIP Service statistics either by:

Selecting System > Control Center , selecting a Call
                                    Server, clicking the Statistics icon in the toolbar, and then
                                    selecting the SIP tab.

Selecting Device Management > CVP Call Server , selecting a Call
                                    Server, clicking the Statistics icon in the toolbar, and then
                                    selecting the SIP tab.

The following
                              table describes the SIP Service call statistics.

Statistic

Description

Realtime
                                             Statistics

Total Call Legs

The number of SIP call legs being handled by
                                          the SIP service. A call leg is also known as a SIP dialog. The metric includes
                                          incoming, outgoing and ringtone type call legs. For each active call in the SIP
                                          service, there is an incoming call leg, and an outgoing call leg to the
                                          destination of the transfer label.

Active Basic Service Video Calls
                                          Offered

The number of basic service
                                          video calls in progress where video capability was
                                          offered.

Active Basic Service Video Calls Answered

The number of basic service video calls in progress
                                          where video capability was answered.

Interval
                                             Statistics

Start
                                          Time

The time the system started
                                          collecting statistics.

Duration Elapsed

The amount of time that has elapsed since the
                                          start time.

Interval Duration

The interval at which statistics are collected. The
                                          default value is 30 minutes.

New Calls

The number of SIP Invite messages received by
                                          Unified CVP in the current interval. It includes the failed calls, and calls rejected due to the SIP service being out of
                                          service.

Connects
                                          Received

The number of CONNECT
                                          messages received by SIP service to perform a call Transfer, in the
                                          last statistics aggregation interval. Connects Received includes the regular
                                          Unified CVP transfers, and Refer transfers. Any label coming from the ICM
                                          service is a CONNECT message, whether it is a label to send to the
                                          VRU or a label to transfer to an agent.

Avg Latency Connect to
                                          Answer

The period of time between
                                          the CONNECT from ICM and when the call is answered. The metric includes the
                                          average latency computation for the calls that have been answered in the
                                          last statistics aggregation interval.

Failed SIP Transfers (Pre-Dialog)

The number of failed SIP
                                          transfers since system start time. When Unified CVP attempts to make a transfer
                                          to the first destination of the call, it sends the initial INVITE request to
                                          set up the caller with the ICM routed destination label. The metric does not
                                          include rejections due to the SIP Service not running. The metric includes
                                          failed transfers that were made after a label was returned from the ICM Server
                                          in a CONNECT message.

Failed SIP Transfers (Post-Dialog)

The number of failed re-invite
                                          requests on either the inbound or outbound legs of the call during the
                                          interval. After a SIP dialog is established, re-INVITE messages perform transfers. Re-invite requests can originate from the
                                          endpoints or else
                                          be initiated by a Unified CVP transfer from the Unified ICME script. This
                                          counter includes failures for both kinds of re-invite
                                          requests.

Basic Service Video Calls Offered

The number of basic service video calls offered in the current
                                          interval.

Basic Service Video Calls Answered

The number of basic service video calls answered in the current
                                          interval.

Aggregate Statistics

Start Time

The time the service started collecting statistics.

Duration Elapsed

The amount of time that has elapsed since the
                                          service start time.

Total New Calls

The number of SIP Invite messages received by
                                          Unified CVP since system start time. It includes the failed calls, and calls rejected due to the SIP service being out of
                                          service.

Connects
                                          Received

The number of Connect
                                          messages received by SIP service to perform a Unified CVP Transfer,
                                          since system start time. Connects Received includes the regular Unified CVP
                                          transfers, and Refer transfers. Any label coming from the ICM service is
                                          a Connect message, whether it is a label to send to the VRU or a
                                          label to transfer to an agent.

Avg Latency Connect to Answer

The  time between the
                                          Connect from ICM and when the call is answered. The metric includes the average
                                          latency computation for all the calls that have been answered since system
                                          start up time.

Failed SIP Transfers (Pre-Dialog)

The total number of failed transfers on the first CVP transfer since
                                          system start time. A SIP dialog is established after the first CVP transfer finishes. The metric does not include rejections
                                          due to SIP being out of
                                          service. The metric includes failed transfers that are after a label is
                                          returned from the ICM in a CONNECT message.

Failed SIP Transfers (Post-Dialog)

The number of failed re-invite
                                          requests on the inbound or outbound legs of the call since start time.
                                          After a SIP dialog is established, re-INVITE messages perform
                                          transfers. Re-invite requests can originate from the endpoints or 
                                          initiated by a Unified CVP transfer from the Unified ICME script. This counter
                                          includes failures for re-invite requests.

Total Basic Service Video Calls
                                          Offered

The number of basic
                                          service video calls offered since system start time.

Total Basic Service Video Calls
                                          Answered

The number of basic
                                          service video calls answered since system start time.

### Gateway Statistics

Gateway statistics include the number of active
                              calls, available memory, and CPU utilization.

To obtain gateway
                                    		  statistics:

Choose System > Control
                                                   				  Center .

Select the Device
                                                				Type tab in the left pane, then select Gateways .

Gateways are
                                                				listed in the right pane.

Select the
                                             			 gateway by clicking on its link under the Hostname column.

the Edit
                                                				Gateway Configuration window opens.

Select the
                                             			 Statistics icon in the toolbar.

##### What to do next

See Administration Guide for
                                             				  Cisco Unified Customer Voice Portal for device statistics.

#### Gateway Statistics

The following table describes
                                 gateway statistics.

Statistic

Description

Active Calls

Number of currently active calls handled by the gateway. For example,
                                             Total call-legs: 0

no active calls

Free Memory

Free memory, for example:

Processor memory free: 82%

I/O memory free: 79%

CPU Utilization

CPU utilization, for example:

CPU utilization for five seconds: 3%/3%; one minute: 3%;
                                                five minutes:
                                                4%

### Trunk Utilization Reporting

You can configure IOS gateways to report on truck
                              utilization. The configuration involves two pieces:

Configuring the Call Server using the Operations Console to request
                                    reporting from a given gateway.

Configuring the gateway
                                    to respond to trunk utilization reporting requests.

To configure Unified CVP to provide trunk utilization reporting,
                              complete these steps:

In the Operations Console,
                                    select: Device Management > Call Server > ICM (tab) > Advanced
                                          Configuration ..

Under Trunk Utilization ,
                                    select Enable Gateway Trunk Reporting

In
                                    the same section, associate the gateway(s) that you want to send truck
                                    information to the Call Server.

Add the following
                                    configuration to the gateway configuration:

```
voice class resource-group 1
                            resource cpu 1-min-avg threshold high 80 low 60
                            resource ds0
                            resource dsp
                            resource mem total-mem
                            periodic-report interval 30

                            sip-ua
                            rai target ipv4:10.86.129.11 resource-group 1
                            rai target ipv4:10.86.129.24 resource-group 1
```

### RAI Information on SIP OPTIONS (CVP Server Group Heartbeats)

If a resource availability indicator (RAI) is desired on
                              SIP OPTIONS, the option override host setting can be used with server group
                              heartbeating. When one or more Unified CVPs are sending OPTIONS heartbeats to the
                              gateway, RAI trunk utilization information is not normally sent in the 200 OK
                              response, unless an RAI target is configured.

CLI like the
                              following can be added in IOS to have RAI information sent to CVP in
                              the response:

```
sip-ua
                            rai target dns:cvp.cisco.com resource-group 1
```

### Unified CVP VXML
                           	 Server Statistics

The Operations Console
                              		displays realtime, interval, and aggregate Unified CVP VXML server statistics.

Access Unified CVP
                              		VXML server statistics either by:

Selecting System > Control
                                          				  Center , selecting a Unified CVP VXML server, and then
                                    			 clicking the Statistics icon in the toolbar.

Selecting Device
                                          				  Management > VXML Server (or Unified CVP VXML
                                    			 server (Standalone)), selecting a Unified CVP VXML server, and then clicking
                                    			 the Statistics icon in the toolbar.

The following table
                              		describes the statistics reported by the Unified CVP VXML server.

Statistic

Description

Real Time Statistics

Active Sessions

The number of
                                          				current sessions being handled by the Unified CVP VXML server.

Active ICM
                                          				Lookup Requests

The number of
                                          				current ICM requests being handled by the Unified CVP VXML server.

Interval Statistics

Start Time

The time when
                                          				the current interval began.

Duration
                                          				Elapsed

The time that
                                          				has elapsed since the start time in the current interval.

Interval
                                          				Duration

The interval at
                                          				which statistics are collected. The default is 30 minutes.

Sessions

The number of
                                          				sessions in the Unified CVP VXML server.

Reporting Events

The number of
                                          				events sent to the Reporting Server from the Unified CVP VXML server.

ICM Lookup
                                          				Requests

The number of
                                          				requests from the Unified CVP VXML server to the ICM Service.

ICM Lookup
                                          				Responses

The number of
                                          				responses to failed and successful ICM Lookup Requests that the ICM Service
                                          				sends to the Unified CVP VXML server. In the case that multiple response
                                          				messages are sent back to the Unified CVP VXML server to a single request, this
                                          				metric increases per response message from the ICM Service.

ICM Lookup
                                          				Successes

The number of
                                          				successful requests from the Unified CVP VXML server to the ICM Service in the
                                          				current interval.

ICM Lookup
                                          				Failures

The number of
                                          				requests from the Unified CVP VXML server to the ICM Service in the current
                                          				interval. This metric increases when an ICM failed message is received or when
                                          				the Unified CVP VXML server generates the failed message.

Aggregate Statistics

Start Time

The time when
                                          				the current interval has begins.

Duration Elapsed

The time since
                                          				the current interval began.

Total Sessions

The number of
                                          				sessions in the Unified CVP VXML server since startup.

Total Reporting
                                          				Events

The number of
                                          				reporting events sent from the Unified CVP VXML server since startup.

Total ICM
                                          				Lookup Requests

The number of
                                          				requests from the Unified CVP VXML server to the ICM Service. For each ICM
                                          				lookup request (successful or failed), this metric increases by one.

Total ICM
                                          				Lookup Responses

The number of
                                          				responses the ICM Service has sent to the Unified CVP VXML server since
                                          				startup. For each ICM lookup request (successful or failed), this metric
                                          				increases by one. When multiple response messages are sent back to the Unified
                                          				CVP VXML server to a single request, this metric increases per response message
                                          				from the ICM Service.

Total ICM
                                          				Lookup Success

The number of
                                          				requests from the Unified CVP VXML server to the ICM Service since startup. For
                                          				each ICM lookup request that succeeded, this metric increases one.

Total ICM
                                          				Lookup Failures

The number of
                                          				requests from the Unified CVP VXML server to the ICM Service since startup. For
                                          				each ICM lookup request that failed, this metric increases by one. This metric
                                          				will increase when an ICM failed message was received or in the case the
                                          				Unified CVP VXML server generates a failed message.

See the Administration Guide for
                                       				  Cisco Unified Customer Voice Portal for Infrastructure Statistics and Device Statistics.

### Reporting Server Statistics

Reporting Server statistics include the total number
                              of events received from the IVR, SIP, and VoiceXML services.

Access Reporting Server statistics either by:

Selecting System > Control Center , selecting a
                                    Reporting Server, and then clicking the Statistics icon in the
                                    toolbar.

Selecting Device Management > CVP
                                          Reporting Server , selecting a Reporting Server, and then clicking the
                                    Statistics icon in the toolbar.

The following table
                              describes the Reporting Server statistics.

Statistic

Description

Interval
                                             Statistics

Start Time

The time the system began collecting statistics.

Duration Elapsed

The amount of time that has elapsed since the
                                          start time.

Interval Duration

The interval at which statistics are collected. The
                                          default value is 30 minutes.

VXML Events Received

The number of reporting events received from
                                          the VoiceXML Service. For each reporting event received
                                          from the VoiceXML Service, this metric increases by
                                          one.

SIP
                                          Events Received

The number of
                                          reporting events received from the SIP Service during this interval. For each
                                          reporting event received from the SIP Service, this metric increases by
                                          one.

IVR
                                          Events Received

The number of
                                          reporting events received from the IVR service in the interval. For each
                                          reporting event received from the IVR service, this metric increases by
                                          one.

Database Writes

The number of
                                          writes to the database made by the Reporting server during the interval. For
                                          each write, this metric increases one.

Aggregate Statistics

Start Time

The time the service started collecting
                                          statistics.

Duration Elapsed

The amount
                                          of time that has elapsed since the service start time.

VXML Events
                                          Received

The number of
                                          reporting events received from the VoiceXML Service since the service started.
                                          For each reporting event received from the VoiceXML Service, this metric increases by one.

SIP Events Received

The number of reporting events received from
                                          the SIP Service since the service started. For each reporting event received
                                          from the SIP Service, this metric increases by one.

IVR Events
                                          Received

The number of
                                          reporting events received from the IVR Service since the service started. For
                                          each event received, this metric increases by one.

Database Writes

The number of writes to the database made by the Reporting server during since
                                          startup. For each write, this metric
                                          increases by one.

## Unified CVP SNMP-Raise/Clear Mappings

The following log
                           messages are SNMP-enabled by default. Administrators can
                           define a unique alarm within their SNMP management station for all SNMP Raise
                           events emitted by a system. These alarms are usually cleared automatically
                           using one or more corresponding SNMP Clear events when the condition is
                           resolved. The tables below list a mapping of Unified CVP SNMP Raise events with
                           their corresponding SNMP Clears.

Raise ID

Clear ID

Event
                                       Name

7

ADAPTER_INITIALIZATION_FAILURE

8

ADAPTER_INITIALIZATION_SUCCESS

9

PLUGIN_INITIALIZATION_FAILURE

10

PLUGIN_INITIALIZATION_SUCCESS

15

SEND_QUEUE_THRESHOLD_REACHED

20

SEND_QUEUE_SIZE_CLEAR

Raise ID

Clear ID

Event
                                       Name

9005

LICENSING

1003

[AUDIT] "The system has started up."

9007

PORT_THRESHOLD

9008

PORT_THRESHOLD

9014

SHUTDOWN

1003

[AUDIT] "The system has started up."

1004

[AUDIT] "The system has completely shutdown."

9016

SERVER_SETUP - "CCBUSNMPAgent Server setup failed
                                       because XXX"

9015

SERVER_SETUP - "CCBUSNMPAgent Server setup on port YYY"

1011

HEARTBEATS_STOPPED - "Heartbeats from XXX
                                       stopped..."

1014

RECEIVED_STATE_MSG - "StateManager: Subsystem [XXX] reported change
                                       to..."

1012

STATE_MANAGER_STARTUP_FAILURE

1003

[AUDIT] "The system has started up."

1020

STARTUP

1003

[AUDIT] "The system has started up."

1024

SERVLET_STARTUP

1003

[AUDIT] "The system has started up."

1025

START - "Could not start XXX due to: YYY"

1003

[AUDIT] "The system has started up."

1033

START - "No Subsystems have been started..."

1026

START - "All Subsystems have been started."

1035

LICENSE_EXPIRATION

1003

[AUDIT] "The system has started up."

Raise ID

Clear ID

Event
                                       Name

2001

LOGMSG_ICM_SS_MSGBUS_SHUTDOWN

2003

LOGMSG_ICM_SS_MSGBUS_ACTIVE

2002

LOGMSG_ICM_SS_PIM_SHUTDOWN

2004

LOGMSG_ICM_SS_PIM_ACTIVE

2005

LOGMSG_ICM_SS_HEARTBEAT_FAILURE

2012

LOGMSG_ICM_SS_INSERVICE_STATE

2006

LOGMSG_ICM_SS_STATE

2012

LOGMSG_ICM_SS_INSERVICE_STATE

Raise ID

Clear ID

Event
                                       Name

4005

REPORTING_SS_ERROR_RAISE

1026

START - "All Subsystems have been started."

4006

REPORTING_DB_PURGE_FAILED

4007

REPORTING_DB_PURGE_COMPLETED

4010

REPORTING_DB_BACKUP_FAILED

4011

REPORTING_DB_BACKUP_COMPLETED

4014

REPORTING_DB_ALERT_MSG

N/A

Not
                                       applicable

4017

REPORTING_DB_STARTING_PURGE

4007

REPORTING_DB_PURGE_COMPLETED

4009

REPORTING_DB_EMERGENCY_PURGE_COMPLETED

4018

REPORTING_DB_REMAINDER_DATA

4019

REPORTING_DB_NO_REMAINDER_DATA

Raise ID

Clear ID

Event
                                       Name

3002

STATE_CHANGED

3001

STATE_CHANGED_IN_SERVICE

3000

SHUTDOWN_NOTICE

3001

STATE_CHANGED_IN_SERVICE

Raise ID

Clear ID

Event
                                       Name

5001

SS_STATE; The SIP subsystem changed state to
                                       something other than the in service state.

5002

SS_STATE; The SIP subsystem changed state to the in
                                          service state.

Raise ID

Clear ID

Event
                                       Name

6012

VXML_SERVER_APP_SHUTDOWN_ALERT

6011

VXML_SERVER_APP_STARTUP_CLEAR

6013

VXML_SERVER_APPADMIN_ERROR

1003

[AUDIT] "The system has started up."

1004

[AUDIT] "The system has
                                       completely shutdown."

6014

VXML_SERVER_SYSTEM_ERROR

1003

[AUDIT] "The system has started up."

1004

[AUDIT] "The system has
                                       completely shutdown."

6024

VXML_LICENSE_ALERT

6025

VXML_LICENSE_ALERT_CLEAR

VXML_LICENSE_ALERT is raised when the VXML Port license utilization exceeds 90% of the total deployed license ports and the
                                       VXML_LICENSE_ALERT_CLEAR is raised when the VXML port license utilization drops below 70% of the total deployed license ports.

| Note | The CVPLogMessages.xml file
                                    applies to all Unified CVP Services. |
|---|---|

| Note | Be aware that the <resolution> field might not always
                                    contain as much information as the Troubleshooting Guide for Cisco Unified Customer Voice Portal or other Unified CVP documentation, and should be considered with all
                                    other resources when troubleshooting a problem. |
|---|---|

| Message
                                          Element | Possible
                                          Values | What it
                                          Means |
|---|---|---|
| Name | Resource="identifier" | Identifies the event type described in
                                          the CVPLogMessagesRes.properties file. |
| Body | Resource="identifier" | Identifies the message text described in the CVPLogMessagesRes.properties file. |
| Severity | 0 to
                                          6 | Identifies the severity level of the event. |
| SendToSNMP | True or false | Set to true, to send this message,
                                          when logged, to an SNMP manager, if one is configured. |
| SendToSyslog | True or false | Set to true to send this message, when
                                          logged, to a Syslog server, if one is configured. |
| SNMPRaise | True or false | Set to true to identify this message,
                                          when logged, as an SNMP raise event, which the SNMP management station  uses
                                          to initiate a task or automatically take an action. Set to false to
                                          identify this message as an SNMP clear when sent to an SNMP management station.
                                          An SNMP clear event usually corresponds to an SNMP raise event, indicating that
                                          the problem causing the raise has been corrected. An administrator on an SNMP
                                          management station can correlate SNMP raise events with SNMP clear
                                          events. |

| Level | Severity | Purpose |
|---|---|---|
| EMERGENCY | 0 | System or service is unusable |
| ALERT | 1 | Action must be taken
                                          immediately |
| CRITICAL | 2 | Critical condition, similar to ALERT, but not
                                          necessarily requiring an immediate action |
| ERROR | 3 | An error condition that does
                                          not necessarily impact the ability of the service to continue to
                                          function |
| WARN | 4 | A warning about a bad condition, which is not
                                          necessarily an error |
| NOTICE | 5 | Notification about interesting system-level
                                          conditions, which are not errors |
| INFO | 6 | Information about internal
                                          flows or application or per-request information, not system-wide
                                          information |

| Log
                                          Type | Log Name | Description |
|---|---|---|
| Infrastructure | CVP.<timestamp>.log | Unified CVP logs for the VoiceXML Service: This
                                          includes Notice, Info, and Debug logs. With Debug turned on, you can also see
                                          Call, Message, and Method trace types of logs. |
| Error messages | Error.<timestamp>.log | Unified CVP error log: This contains any error that
                                          Unified CVP Services and message layer has generated. |

| Note | Unified CVP VXML
                                          		  Server (by default) receives callid (which contains the call GUID), _dnis, and
                                          		  _ani as session variables in comprehensive mode even if the variables are not
                                          		  configured as parameters in the ToExtVXML array. If the variables are
                                          		  configured in ToExtVXML then those values are used. These variables are
                                          		  available to VXML applications as session variables, and displayed in the
                                          		  Unified CVP VXML Server log. This change is backwards compatible with the
                                          		  following script. That is, if you have added the following script, you do not
                                          		  change it. However, if you remove this script, you save an estimated 40 bytes
                                          		  of ECC variable space. |
|---|---|

| In the Unified ICME script, use the formula editor to set ToExtVXML[1]. Set the value of
                                          			 ToExtVXML[1] variable to concatenate("callid=",Call.user.media.id) Note Always
                                                               						include Call ID when sending the call to the Unified CVP VXML Server using the
                                                               						Comprehensive call flow model. The Call ID can also be used in Unified CVP VXML
                                                               						Server (standalone) solutions. When you
                                                               						concatenate multiple values, use a comma for the delimiter. The value
                                                               						of ICMInfoKeys must contain RouterCallKey, RouterCallDay, and
                                                               						RouterCallKeySequenceNumber separated by a “-“. For
                                                               						example,
                                                               						concatenate("ICMInfoKeys=",Call.RouterCallKey,"-",Call.RouterCallDay,"-",Call.RouterCallKeySequenceNumber). | Note | Always
                                                               						include Call ID when sending the call to the Unified CVP VXML Server using the
                                                               						Comprehensive call flow model. The Call ID can also be used in Unified CVP VXML
                                                               						Server (standalone) solutions. When you
                                                               						concatenate multiple values, use a comma for the delimiter. The value
                                                               						of ICMInfoKeys must contain RouterCallKey, RouterCallDay, and
                                                               						RouterCallKeySequenceNumber separated by a “-“. For
                                                               						example,
                                                               						concatenate("ICMInfoKeys=",Call.RouterCallKey,"-",Call.RouterCallDay,"-",Call.RouterCallKeySequenceNumber). |
|---|---|---|
| Note | Always
                                                               						include Call ID when sending the call to the Unified CVP VXML Server using the
                                                               						Comprehensive call flow model. The Call ID can also be used in Unified CVP VXML
                                                               						Server (standalone) solutions. When you
                                                               						concatenate multiple values, use a comma for the delimiter. The value
                                                               						of ICMInfoKeys must contain RouterCallKey, RouterCallDay, and
                                                               						RouterCallKeySequenceNumber separated by a “-“. For
                                                               						example,
                                                               						concatenate("ICMInfoKeys=",Call.RouterCallKey,"-",Call.RouterCallDay,"-",Call.RouterCallKeySequenceNumber). |

| Note | Always
                                                               						include Call ID when sending the call to the Unified CVP VXML Server using the
                                                               						Comprehensive call flow model. The Call ID can also be used in Unified CVP VXML
                                                               						Server (standalone) solutions. When you
                                                               						concatenate multiple values, use a comma for the delimiter. The value
                                                               						of ICMInfoKeys must contain RouterCallKey, RouterCallDay, and
                                                               						RouterCallKeySequenceNumber separated by a “-“. For
                                                               						example,
                                                               						concatenate("ICMInfoKeys=",Call.RouterCallKey,"-",Call.RouterCallDay,"-",Call.RouterCallKeySequenceNumber). |
|---|---|

| Log
                                          Type | Log Name | Description |
|---|---|---|
| Unified CVP VXML Server Call Log | call_log<timestamp>.txt | Records a single line for every application visit
                                          handled by the  Unified CVP VXML Server. |
| Unified CVP VXML Server Call Error Log | error_log<timestamp>.txt | Records errors that occur outside the realm of a
                                          particular application. |
| Unified CVP VXML Server Administration History Log | admin_history<timestamp>.txt | Records information from Unified CVP VXML Server
                                          administration scripts. |

| Note | If the
                                             application is configured correctly, this does not occur. |
|---|---|

| Note | Application developers have to use the above folder for application
                                          		  and custom logs. |
|---|---|

| Note | See Element Specifications for
                                          			 Cisco Unified CVP Unified CVP VXML Server and Unified Call Studio for
                                       		  information about configuring loggers. |
|---|---|

| Application Logger Type | Log Name | Description |
|---|---|---|
| ActivityLog | activity_log<timestamp>.txt Note Log
                                                   						files are stored in the ActivityLog directory. | Note | Log
                                                   						files are stored in the ActivityLog directory. | Records
                                          						all application activity, showing which elements are entered and exited during
                                          						a call. Default
                                          						setting: on |
| Note | Log
                                                   						files are stored in the ActivityLog directory. |
| ErrorLog | error_log<timestamp>.txt Note Log
                                                   						files are stored in the ErrorLog directory. | Note | Log
                                                   						files are stored in the ErrorLog directory. | Records
                                          						all error messages for the application. Default
                                          						setting: on |
| Note | Log
                                                   						files are stored in the ErrorLog directory. |
| AdminLog | admin_history<timestamp>.txt Note Log
                                                   						files are stored in the AdminLog directory. | Note | Log
                                                   						files are stored in the AdminLog directory. | Records
                                          						information from application-specific administration scripts. Default
                                          						setting: on |
| Note | Log
                                                   						files are stored in the AdminLog directory. |
| CVPDatafeedLog | CVPDatafeed.log. Note This
                                                   						log is stored in /Cisco/CVP/logs/VXML folder. | Note | This
                                                   						log is stored in /Cisco/CVP/logs/VXML folder. | Listens
                                          						for logging events and provides Unified CVP VXML Server and VoiceXML Service
                                          						data to the Unified CVP Reporting Server. The Unified CVP Reporting Server
                                          						stores this information in a reporting database so that it is available for
                                          						later review. One
                                          						CVPDatafeedLog is created per application. Default
                                          						setting: on Note The
                                                   						VoiceXML Service can be started by adding this logger in the VoiceXML
                                                   						application. | Note | The
                                                   						VoiceXML Service can be started by adding this logger in the VoiceXML
                                                   						application. |
| Note | This
                                                   						log is stored in /Cisco/CVP/logs/VXML folder. |
| Note | The
                                                   						VoiceXML Service can be started by adding this logger in the VoiceXML
                                                   						application. |
| CVPSNMPLog | CVPSNMP.log. Note This
                                                   						log is stored in /Cisco/CVP/logs/VXML folder. | Note | This
                                                   						log is stored in /Cisco/CVP/logs/VXML folder. | Listens
                                          						for a set of events and sends information about these events to the SNMP log,
                                          						Syslog, or Unified CVP log. Default
                                          						setting: on |
| Note | This
                                                   						log is stored in /Cisco/CVP/logs/VXML folder. |
| DebugLog | debug_log<timestamp>.txt. Note Log
                                                   						files are stored in the DebugLog directory. | Note | Log
                                                   						files are stored in the DebugLog directory. | Creates a
                                          						single file per call that contains all HTTP requests and responses that
                                          						occurred between a IOS Gateway and Unified CVP VXML Server during the call
                                          						session. Default
                                          						setting: off |
| Note | Log
                                                   						files are stored in the DebugLog directory. |

| Note | Log
                                                   						files are stored in the ActivityLog directory. |
|---|---|

| Note | Log
                                                   						files are stored in the ErrorLog directory. |
|---|---|

| Note | Log
                                                   						files are stored in the AdminLog directory. |
|---|---|

| Note | This
                                                   						log is stored in /Cisco/CVP/logs/VXML folder. |
|---|---|

| Note | The
                                                   						VoiceXML Service can be started by adding this logger in the VoiceXML
                                                   						application. |
|---|---|

| Note | This
                                                   						log is stored in /Cisco/CVP/logs/VXML folder. |
|---|---|

| Note | Log
                                                   						files are stored in the DebugLog directory. |
|---|---|

| Statistic | Description |
|---|---|
| Realtime
                                             Statistics |
| Port Licenses Available | The number of port licenses available
                                          for the processing of new calls. Exactly one port license is used per call,
                                          independent of the call's traversal through the individual Call Server
                                          services. |
| Current Port Licenses in Use | The number of port licenses currently
                                          in use on the Call Server. One port license is used per call,
                                          independent of the call's traversal of the individual Call Server services. |
| Current
                                          Port Licenses State | There are four threshold levels of port license usage: safe, warning,
                                          critical and failure. An administrator may set the required percentage of port
                                          licenses in use needed to reach a given threshold level, with the exception of
                                          the failure level which is reached when the number of ports checked out is
                                          equal to the number of licenses ports. |
| Interval Statistics |
| Start Time | The time the system
                                          started collecting statistics for the current interval. |
| Duration Elapsed | The amount of time that has elapsed since the
                                          start time in the current interval. |
| Interval Duration | The interval at which statistics are collected. The
                                          default value is 30 minutes. |
| Total New Port License Requests | The number of port
                                          license checkout requests made in the current interval. For each port license
                                          checkout request, this metric is
                                          increased by one, regardless of whether if checks out a new port license. |
| Average License Requests/Minute | The average number of port license
                                          checkout requests made per minute in the current interval. This metric is
                                          calculated by dividing the port license requests metric by the number of
                                          minutes elapsed in the current interval. |
| Maximum Port Licenses Used | The maximum number of port licenses used during
                                          this time interval. |
| Aggregate
                                             Statistics |
| Start
                                          Time | The time the service started
                                          collecting statistics. |
| Duration Elapsed | The amount
                                          of time that has elapsed since the service start time. |
| Total New Port License Requests | The number of port license checkout
                                          requests made since the system was started. For each port license checkout, this metric is increased by one, regardless of
                                          whether if checks out a new port license. |
| Average License Requests /Minute | The average number of port license checkout
                                          requests made per minute since the system was started. This metric is
                                          calculated by dividing the aggregate port license requests metric by the number
                                          of minutes elapsed since the system was started. |
| Peak Port Licenses
                                          Used | The peak number of simultaneous
                                          port licenses used since the start of the system. When a port checkout occurs,
                                          this metric is set to the current port licenses in use metric if that value is
                                          greater than this metric's current peak value. |
| Total Denied Port License
                                          Requests | The number of  port license
                                          checkout requests that were denied since the start of the system. A port license checkout request is denied if the number
                                          of port
                                          licenses checked out at the time of the request is equal to the total number of
                                          port license available. When a port license checkout is denied, the call does
                                          not receive regular treatment (the caller may hear a busy tone or an error
                                          message). |

| Statistic | Description |
|---|---|
| Realtime
                                             Statistics |
| Idle Threads | The number of idle threads waiting for
                                          some work |
| Running Threads | The number of running thread pool threads currently processing some work. |
| Core
                                          Threads | The number of
                                          thread pool threads that will never be destroyed no matter how long they remain
                                          idle |
| Maximum Threads | The maximum
                                          number of thread pool threads that will ever exist simultaneously |
| Peak
                                          Threads Used | The peak
                                          number of thread pool threads ever simultaneously tasked with some work to
                                          process |

| Statistic | Description |
|---|---|
| Realtime
                                             Statistics |
| Peak Memory Usage | The greatest amount of memory used by the Java
                                          Virtual machine since startup. The number reported is in megabytes and
                                          indicates the peak amount of memory ever used simultaneously by this Java
                                          Virtual Machine. |
| Current Memory Usage | The
                                          current number of megabytes of memory used by the Java Virtual Machine. |
| Total
                                          Memory | The amount of memory in
                                          megabytes available to the Java Virtual Machine. The number  indicates how much system memory is available for the Java
                                          Virtual Machine. |
| Available Memory | The amount
                                          of available memory in the Java Virtual Machine. The number reported is in
                                          megabytes and indicates how much of the current system memory claimed by the
                                          Java Virtual Machine is not currently being used. |
| Threads in Use | The number of threads currently in use in the Java
                                          Virtual Machine. This number includes all of the Unified CVP standalone and
                                          thread pool threads, and  those threads created by the Web Application
                                          Server running within the same JVM. |
| Peak Threads in Use | The greatest amount of threads used
                                          simultaneously in the Java Virtual Machine since startup. The peak number of
                                          threads used by thw Java Virtual Machine includes all Unified CVP
                                          standalone and thread pool threads, and threads created by the Web
                                          Application Server running within the same JVM. |
| Uptime | The time that the Java Virtual Machine
                                          has been running. This time is measured in hh:mm:ss and shows the amount of
                                          elapsed time since the Java Virtual Machine process began. |

| Statistic | Description |
|---|---|
| Realtime
                                             Statistics |
| Active Calls | The
                                          current number of calls being serviced by the Unified Intelligent Contact Management (Unified ICM) Server for a Unified CVP
                                          Call
                                          Server. This value represents the calls currently being serviced by the
                                          Unified ICM for the Unified CVP Call Server for follow-on routing to a Contact Center
                                          agent. |
| Active SIP Call Legs | The ICM
                                          Server can accept VoIP calls that originate using either the
                                          Session Initiation Protocol (SIP). Active SIP Call Legs
                                          indicates the number of calls received by the Unified ICM Server from the
                                          Unified CVP Call Server using the SIP protocol. |
| Active VRU Call Legs | The current number of calls receiving Voice
                                          Response Unit (VRU) treatment from the Unified ICM Server. The VRU treatment includes
                                          playing pre-recorded messages, asking for Caller Entered Digits (CED) or Speech
                                          Recognition Techniques to understand the customer request. |
| Active ICM
                                          Lookup Requests | Calls originating
                                          from an external Unified CVP VXML Server need call routing instructions from the Unified ICM
                                          Server. Active Lookup Requests indicates the current number of external Unified CVP VXML Server call routing requests sent
                                          to the ICM Server. |
| Active Basic Service Video Calls
                                          Offered | The current number of
                                          simultaneous basic service video calls being processed by theUnified  ICM service where
                                          video capability was offered. |
| Active Basic Service Video Calls
                                          Accepted | The current number of
                                          simultaneous calls that were accepted as basic service video calls and are
                                          being processed by the Unified  ICM service. |
| Interval
                                             Statistics |
| Start Time | The time at which the current interval began. |
| Duration
                                          Elapsed | The amount of time that has
                                          elapsed since the current interval began. |
| Interval Duration | The time interval at which statistics are collected. The
                                          default value is 30 minutes. |
| New Calls | The number of new calls received by the Unified ICM application for follow-on Voice Response Unit (VRU)
                                          treatment and routing to a Contact Center agent during the current
                                          interval. |
| SIP Call Legs | The Unified ICM application accepts VoIP calls that originate from the Session Initiation Protocol (SIP) Protocol.
                                          Interval SIP Call Legs is an interval specific snapshot metric indicating the
                                          number of calls received by the ICM application from SIP during the current
                                          interval. |
| VRU Call Legs | The number of calls
                                          receiving VRU treatment from the Unified  ICM application. The VRU treatment includes playing pre-recorded
                                          messages, asking for Caller Entered Digits (CED) or speech recognition
                                          techniques to understand the customer request during the current interval. |
| ICM Lookup
                                          Requests | Calls originating in an
                                          external Unified CVP VXML Server need call routing instructions from the Unified ICM application. Interval Lookup Requests
                                          is an interval
                                          specific metric indicating the number of external Unified CVP VXML Server call routing
                                          requests sent to the Unified ICM application during the current interval. |
| Basic
                                          Service Video Calls Offered | The
                                          number of offered basic service video calls processed by the Unified  ICM service during
                                          the current interval. |
| Basic Service Video Calls
                                          Accepted | The number of basic service
                                          video calls accepted and processed by the Unified  ICM service during the current
                                          interval. |
| Aggregate Statistics |
| Start Time | The time the service started collecting statistics. |
| Duration Elapsed | The amount of time that has elapsed since the
                                          service start time. |
| Total Calls | The total number of new calls received by the
                                          Unified ICM application for follow-on VRU treatment and routing to a Contact Center agent since system start
                                          time. |
| Total
                                          SIP Call Legs | The Unified ICM application can accept VoIP calls that originate from the Session Initiation Protocol (SIP) Protocol.
                                          Total SIP Switch Legs is a metric indicating the number of calls received
                                          by the ICM application by SIP since system start time. |
| Total VRU Call
                                          Legs | The number of calls that
                                          have received VRU treatment from the Unified ICM application since system start time. The VRU treatment
                                          includes playing pre-recorded messages, asking for Caller Entered Digits (CED)
                                          or Speech Recognition Techniques to understand the customer request. |
| Total ICM
                                          Lookup Requests | Calls originating
                                          in an external Unified CVP VXML Server need call routing instructions from the Unified ICM application. Total Lookup Requests
                                          is a metric
                                          indicating the total number of external Unified CVP VXML Server call routing requests sent
                                          to the Unified ICM application since system start time. |
| Total Basic Service Video Calls
                                          Offered | The number of newly
                                          offered basic service video calls processed by the Unified ICM service since system
                                          start time. |
| Total Basic Service Video Calls Accepted | The number of new basic service video calls
                                          accepted and processed by the Unified ICM service since system start
                                          time. |

| Statistic | Description |
|---|---|
| Realtime Call Statistics |
| Active Calls | The number of
                                          				active calls being serviced by the IVR service. |
| Active HTTP
                                          				Requests | The number of
                                          				active HTTP requests being serviced by the IVR service. |
| Interval Statistics |
| Start Time | The time the
                                          				system starts collecting statistics for the current interval. |
| Duration
                                          				Elapsed | The amount of
                                          				time that has elapsed since the start time in the current interval. |
| Interval
                                          				Duration | The interval at
                                          				which statistics are collected. The default value is 30 minutes. |
| Peak Active
                                          				Calls | Maximum number
                                          				of active calls handled by the IVR service simultaneously. |
| New Calls | Metric that
                                          				counts the number of New Call requests received from the IOS Gateway. A New
                                          				Call includes the Switch leg of the call and the IVR leg of the call. This
                                          				metric counts the number of New Call Requests received by the IVR Service. |
| Calls Finished | Metric that
                                          				counts the number of Unified CVP Calls that have finished during this interval.
                                          				A Call, for the purpose of the Call Finished metric, includes both the Switch
                                          				leg and the IVR leg of the Unified CVP call. When both legs of the call are
                                          				finished, the Calls
                                             				  Finished metric increases. |
| Average Call
                                          				Latency | The average
                                          				amount of time in milliseconds that it takes the IVR Service to process a New
                                          				Call or Call Result Request. |
| Maximum Call
                                          				Latency | The maximum
                                          				amount of time in milliseconds that it has taken for the IVR Service to process
                                          				a New Call Request or a Request Instruction Request. |
| Minimum Call
                                          				Latency | The minimum
                                          				amount of time in milliseconds it took for the IVR Service to process a New
                                          				Call Request or a Request Instruction Request. |
| Peak Active
                                          				HTTP Requests | Active HTTP
                                          				Requests is a metric that indicates the current number of simultaneous HTTP
                                          				requests being processed by the IVR Service. Peak Active Requests is a metric
                                          				that represents the maximum simultaneous HTTP requests being processed by the
                                          				IVR Service. |
| Total HTTP
                                          				Requests | The number of
                                          				HTTP Requests received from a client by the IVR Service. |
| Average HTTP
                                          				Requests/second | The average
                                          				number of HTTP Requests the IVR Service receives per second. |
| Peak Active HTTP
                                          				Requests/second | HTTP Requests
                                          				per Second is a metric that represents the number of HTTP Requests the IVR
                                          				Service receives each second from all clients. Peak HTTP Requests per Second is
                                          				the maximum number of HTTP Requests that were processed by the IVR Service in
                                          				any given second. This is also known as high water marking. |
| Aggregate Statistics |
| Start Time | The time the
                                          				service started collecting statistics. |
| Duration Elapsed | The amount of
                                          				time that has elapsed since the service start time. |
| Total New Calls | Metric that
                                          				counts the number of New Call requests received from the IOS GatewayUsing
                                          				Unified ICME Warm. A New Call includes the Switch leg of the call and the IVR
                                          				leg of the call. Total New Calls is a metric that represents the number of new
                                          				calls received by the IVR Service since system startup. |
| Peak Active
                                          				Calls | The maximum
                                          				number of simultaneous calls processed by the IVR Service since the service
                                          				started. |
| Total HTTP
                                          				Requests | Metric that
                                          				represents the number of HTTP Requests received from all clients. This metric
                                          				is the total number of HTTP Requests received by the IVR Service since system
                                          				startup. |
| Peak Active
                                          				HTTP Requests | Peak Active
                                          				HTTP Requests is a metric that indicates the current number of simultaneous
                                          				HTTP requests processed by the IVR Service. Maximum number of active HTTP
                                          				requests processed at the same time since the IVR service started. This is also
                                          				known as high water marking. |
| Total Agent
                                          				Video Pushes | The number of
                                          				videos pushed by agents since system start time. |
| Total Agent
                                          				Initiated Recordings | The number of
                                          				video recordings by agents since system start time. |
| Total Agent
                                          				VCR Control Invocations | The number of
                                          				video VCR controls invoked by agents since system start time. |

| Statistic | Description |
|---|---|
| Realtime
                                             Statistics |
| Total Call Legs | The number of SIP call legs being handled by
                                          the SIP service. A call leg is also known as a SIP dialog. The metric includes
                                          incoming, outgoing and ringtone type call legs. For each active call in the SIP
                                          service, there is an incoming call leg, and an outgoing call leg to the
                                          destination of the transfer label. |
| Active Basic Service Video Calls
                                          Offered | The number of basic service
                                          video calls in progress where video capability was
                                          offered. |
| Active Basic Service Video Calls Answered | The number of basic service video calls in progress
                                          where video capability was answered. |
| Interval
                                             Statistics |
| Start
                                          Time | The time the system started
                                          collecting statistics. |
| Duration Elapsed | The amount of time that has elapsed since the
                                          start time. |
| Interval Duration | The interval at which statistics are collected. The
                                          default value is 30 minutes. |
| New Calls | The number of SIP Invite messages received by
                                          Unified CVP in the current interval. It includes the failed calls, and calls rejected due to the SIP service being out of
                                          service. |
| Connects
                                          Received | The number of CONNECT
                                          messages received by SIP service to perform a call Transfer, in the
                                          last statistics aggregation interval. Connects Received includes the regular
                                          Unified CVP transfers, and Refer transfers. Any label coming from the ICM
                                          service is a CONNECT message, whether it is a label to send to the
                                          VRU or a label to transfer to an agent. |
| Avg Latency Connect to
                                          Answer | The period of time between
                                          the CONNECT from ICM and when the call is answered. The metric includes the
                                          average latency computation for the calls that have been answered in the
                                          last statistics aggregation interval. |
| Failed SIP Transfers (Pre-Dialog) | The number of failed SIP
                                          transfers since system start time. When Unified CVP attempts to make a transfer
                                          to the first destination of the call, it sends the initial INVITE request to
                                          set up the caller with the ICM routed destination label. The metric does not
                                          include rejections due to the SIP Service not running. The metric includes
                                          failed transfers that were made after a label was returned from the ICM Server
                                          in a CONNECT message. |
| Failed SIP Transfers (Post-Dialog) | The number of failed re-invite
                                          requests on either the inbound or outbound legs of the call during the
                                          interval. After a SIP dialog is established, re-INVITE messages perform transfers. Re-invite requests can originate from the
                                          endpoints or else
                                          be initiated by a Unified CVP transfer from the Unified ICME script. This
                                          counter includes failures for both kinds of re-invite
                                          requests. |
| Basic Service Video Calls Offered | The number of basic service video calls offered in the current
                                          interval. |
| Basic Service Video Calls Answered | The number of basic service video calls answered in the current
                                          interval. |
| Aggregate Statistics |
| Start Time | The time the service started collecting statistics. |
| Duration Elapsed | The amount of time that has elapsed since the
                                          service start time. |
| Total New Calls | The number of SIP Invite messages received by
                                          Unified CVP since system start time. It includes the failed calls, and calls rejected due to the SIP service being out of
                                          service. |
| Connects
                                          Received | The number of Connect
                                          messages received by SIP service to perform a Unified CVP Transfer,
                                          since system start time. Connects Received includes the regular Unified CVP
                                          transfers, and Refer transfers. Any label coming from the ICM service is
                                          a Connect message, whether it is a label to send to the VRU or a
                                          label to transfer to an agent. |
| Avg Latency Connect to Answer | The  time between the
                                          Connect from ICM and when the call is answered. The metric includes the average
                                          latency computation for all the calls that have been answered since system
                                          start up time. |
| Failed SIP Transfers (Pre-Dialog) | The total number of failed transfers on the first CVP transfer since
                                          system start time. A SIP dialog is established after the first CVP transfer finishes. The metric does not include rejections
                                          due to SIP being out of
                                          service. The metric includes failed transfers that are after a label is
                                          returned from the ICM in a CONNECT message. |
| Failed SIP Transfers (Post-Dialog) | The number of failed re-invite
                                          requests on the inbound or outbound legs of the call since start time.
                                          After a SIP dialog is established, re-INVITE messages perform
                                          transfers. Re-invite requests can originate from the endpoints or 
                                          initiated by a Unified CVP transfer from the Unified ICME script. This counter
                                          includes failures for re-invite requests. |
| Total Basic Service Video Calls
                                          Offered | The number of basic
                                          service video calls offered since system start time. |
| Total Basic Service Video Calls
                                          Answered | The number of basic
                                          service video calls answered since system start time. |

| Step 1 | Choose System > Control
                                                   				  Center . |
|---|---|
| Step 2 | Select the Device
                                                				Type tab in the left pane, then select Gateways . Gateways are
                                                				listed in the right pane. |
| Step 3 | Select the
                                             			 gateway by clicking on its link under the Hostname column. the Edit
                                                				Gateway Configuration window opens. |
| Step 4 | Select the
                                             			 Statistics icon in the toolbar. |

| Statistic | Description |
|---|---|
| Active Calls | Number of currently active calls handled by the gateway. For example,
                                             Total call-legs: 0 no active calls |
| Free Memory | Free memory, for example: Processor memory free: 82% I/O memory free: 79% |
| CPU Utilization | CPU utilization, for example: CPU utilization for five seconds: 3%/3%; one minute: 3%;
                                                five minutes:
                                                4% |

| Note | Trunk Utilization data is only written to the Unified CVP
                                       database when RAI OPTIONS are sent from the gateway to Unified CVP targets. When Unified CVP is using server group heartbeats
                                       to the gateway, the RAI data in the
                                       response is only marks the element as UP or DOWN (overloaded resources)
                                       in the server group. |
|---|---|

| Statistic | Description |
|---|---|
| Real Time Statistics |
| Active Sessions | The number of
                                          				current sessions being handled by the Unified CVP VXML server. |
| Active ICM
                                          				Lookup Requests | The number of
                                          				current ICM requests being handled by the Unified CVP VXML server. |
| Interval Statistics |
| Start Time | The time when
                                          				the current interval began. |
| Duration
                                          				Elapsed | The time that
                                          				has elapsed since the start time in the current interval. |
| Interval
                                          				Duration | The interval at
                                          				which statistics are collected. The default is 30 minutes. |
| Sessions | The number of
                                          				sessions in the Unified CVP VXML server. |
| Reporting Events | The number of
                                          				events sent to the Reporting Server from the Unified CVP VXML server. |
| ICM Lookup
                                          				Requests | The number of
                                          				requests from the Unified CVP VXML server to the ICM Service. |
| ICM Lookup
                                          				Responses | The number of
                                          				responses to failed and successful ICM Lookup Requests that the ICM Service
                                          				sends to the Unified CVP VXML server. In the case that multiple response
                                          				messages are sent back to the Unified CVP VXML server to a single request, this
                                          				metric increases per response message from the ICM Service. |
| ICM Lookup
                                          				Successes | The number of
                                          				successful requests from the Unified CVP VXML server to the ICM Service in the
                                          				current interval. |
| ICM Lookup
                                          				Failures | The number of
                                          				requests from the Unified CVP VXML server to the ICM Service in the current
                                          				interval. This metric increases when an ICM failed message is received or when
                                          				the Unified CVP VXML server generates the failed message. |
| Aggregate Statistics |
| Start Time | The time when
                                          				the current interval has begins. |
| Duration Elapsed | The time since
                                          				the current interval began. |
| Total Sessions | The number of
                                          				sessions in the Unified CVP VXML server since startup. |
| Total Reporting
                                          				Events | The number of
                                          				reporting events sent from the Unified CVP VXML server since startup. |
| Total ICM
                                          				Lookup Requests | The number of
                                          				requests from the Unified CVP VXML server to the ICM Service. For each ICM
                                          				lookup request (successful or failed), this metric increases by one. |
| Total ICM
                                          				Lookup Responses | The number of
                                          				responses the ICM Service has sent to the Unified CVP VXML server since
                                          				startup. For each ICM lookup request (successful or failed), this metric
                                          				increases by one. When multiple response messages are sent back to the Unified
                                          				CVP VXML server to a single request, this metric increases per response message
                                          				from the ICM Service. |
| Total ICM
                                          				Lookup Success | The number of
                                          				requests from the Unified CVP VXML server to the ICM Service since startup. For
                                          				each ICM lookup request that succeeded, this metric increases one. |
| Total ICM
                                          				Lookup Failures | The number of
                                          				requests from the Unified CVP VXML server to the ICM Service since startup. For
                                          				each ICM lookup request that failed, this metric increases by one. This metric
                                          				will increase when an ICM failed message was received or in the case the
                                          				Unified CVP VXML server generates a failed message. |

| Statistic | Description |
|---|---|
| Interval
                                             Statistics |
| Start Time | The time the system began collecting statistics. |
| Duration Elapsed | The amount of time that has elapsed since the
                                          start time. |
| Interval Duration | The interval at which statistics are collected. The
                                          default value is 30 minutes. |
| VXML Events Received | The number of reporting events received from
                                          the VoiceXML Service. For each reporting event received
                                          from the VoiceXML Service, this metric increases by
                                          one. |
| SIP
                                          Events Received | The number of
                                          reporting events received from the SIP Service during this interval. For each
                                          reporting event received from the SIP Service, this metric increases by
                                          one. |
| IVR
                                          Events Received | The number of
                                          reporting events received from the IVR service in the interval. For each
                                          reporting event received from the IVR service, this metric increases by
                                          one. |
| Database Writes | The number of
                                          writes to the database made by the Reporting server during the interval. For
                                          each write, this metric increases one. |
| Aggregate Statistics |
| Start Time | The time the service started collecting
                                          statistics. |
| Duration Elapsed | The amount
                                          of time that has elapsed since the service start time. |
| VXML Events
                                          Received | The number of
                                          reporting events received from the VoiceXML Service since the service started.
                                          For each reporting event received from the VoiceXML Service, this metric increases by one. |
| SIP Events Received | The number of reporting events received from
                                          the SIP Service since the service started. For each reporting event received
                                          from the SIP Service, this metric increases by one. |
| IVR Events
                                          Received | The number of
                                          reporting events received from the IVR Service since the service started. For
                                          each event received, this metric increases by one. |
| Database Writes | The number of writes to the database made by the Reporting server during since
                                          startup. For each write, this metric
                                          increases by one. |

| Note | Raises are listed first, with
                                    their corresponding clears below them. |
|---|---|

| Raise ID | Clear ID | Event
                                       Name |
|---|---|---|
| 7 |  | ADAPTER_INITIALIZATION_FAILURE |
|  | 8 | ADAPTER_INITIALIZATION_SUCCESS |
| 9 |  | PLUGIN_INITIALIZATION_FAILURE |
|  | 10 | PLUGIN_INITIALIZATION_SUCCESS |
| 15 |  | SEND_QUEUE_THRESHOLD_REACHED |
|  | 20 | SEND_QUEUE_SIZE_CLEAR |

| Raise ID | Clear ID | Event
                                       Name |
|---|---|---|
| 9005 |  | LICENSING |
|  | 1003 | [AUDIT] "The system has started up." |
| 9007 |  | PORT_THRESHOLD |
|  | 9008 | PORT_THRESHOLD |
| 9014 |  | SHUTDOWN |
|  | 1003 | [AUDIT] "The system has started up." |
|  | 1004 | [AUDIT] "The system has completely shutdown." |
| 9016 |  | SERVER_SETUP - "CCBUSNMPAgent Server setup failed
                                       because XXX" |
|  | 9015 | SERVER_SETUP - "CCBUSNMPAgent Server setup on port YYY" |
| 1011 |  | HEARTBEATS_STOPPED - "Heartbeats from XXX
                                       stopped..." |
|  | 1014 | RECEIVED_STATE_MSG - "StateManager: Subsystem [XXX] reported change
                                       to..." |
| 1012 |  | STATE_MANAGER_STARTUP_FAILURE |
|  | 1003 | [AUDIT] "The system has started up." |
| 1020 |  | STARTUP |
|  | 1003 | [AUDIT] "The system has started up." |
| 1024 |  | SERVLET_STARTUP |
|  | 1003 | [AUDIT] "The system has started up." |
| 1025 |  | START - "Could not start XXX due to: YYY" |
|  | 1003 | [AUDIT] "The system has started up." |
| 1033 |  | START - "No Subsystems have been started..." |
|  | 1026 | START - "All Subsystems have been started." |
| 1035 |  | LICENSE_EXPIRATION |
|  | 1003 | [AUDIT] "The system has started up." |

| Raise ID | Clear ID | Event
                                       Name |
|---|---|---|
| 2001 |  | LOGMSG_ICM_SS_MSGBUS_SHUTDOWN |
|  | 2003 | LOGMSG_ICM_SS_MSGBUS_ACTIVE |
| 2002 |  | LOGMSG_ICM_SS_PIM_SHUTDOWN |
|  | 2004 | LOGMSG_ICM_SS_PIM_ACTIVE |
| 2005 |  | LOGMSG_ICM_SS_HEARTBEAT_FAILURE |
|  | 2012 | LOGMSG_ICM_SS_INSERVICE_STATE |
| 2006 |  | LOGMSG_ICM_SS_STATE |
|  | 2012 | LOGMSG_ICM_SS_INSERVICE_STATE |

| Raise ID | Clear ID | Event
                                       Name |
|---|---|---|
| 4005 |  | REPORTING_SS_ERROR_RAISE |
|  | 1026 | START - "All Subsystems have been started." |
| 4006 |  | REPORTING_DB_PURGE_FAILED |
|  | 4007 | REPORTING_DB_PURGE_COMPLETED |
| 4010 |  | REPORTING_DB_BACKUP_FAILED |
|  | 4011 | REPORTING_DB_BACKUP_COMPLETED |
| 4014 |  | REPORTING_DB_ALERT_MSG |
|  | N/A | Not
                                       applicable |
| 4017 |  | REPORTING_DB_STARTING_PURGE |
|  | 4007 | REPORTING_DB_PURGE_COMPLETED |
|  | 4009 | REPORTING_DB_EMERGENCY_PURGE_COMPLETED |
| 4018 |  | REPORTING_DB_REMAINDER_DATA |
|  | 4019 | REPORTING_DB_NO_REMAINDER_DATA |

| Raise ID | Clear ID | Event
                                       Name |
|---|---|---|
| 3002 |  | STATE_CHANGED |
|  | 3001 | STATE_CHANGED_IN_SERVICE |
| 3000 |  | SHUTDOWN_NOTICE |
|  | 3001 | STATE_CHANGED_IN_SERVICE |

| Raise ID | Clear ID | Event
                                       Name |
|---|---|---|
| 5001 |  | SS_STATE; The SIP subsystem changed state to
                                       something other than the in service state. |
|  | 5002 | SS_STATE; The SIP subsystem changed state to the in
                                          service state. |

| Raise ID | Clear ID | Event
                                       Name |
|---|---|---|
| 6012 |  | VXML_SERVER_APP_SHUTDOWN_ALERT |
|  | 6011 | VXML_SERVER_APP_STARTUP_CLEAR |
| 6013 |  | VXML_SERVER_APPADMIN_ERROR |
|  | 1003 | [AUDIT] "The system has started up." |
|  | 1004 | [AUDIT] "The system has
                                       completely shutdown." |
| 6014 |  | VXML_SERVER_SYSTEM_ERROR |
|  | 1003 | [AUDIT] "The system has started up." |
|  | 1004 | [AUDIT] "The system has
                                       completely shutdown." |
| 6024 |  | VXML_LICENSE_ALERT |
|  | 6025 | VXML_LICENSE_ALERT_CLEAR |

| Note | VXML_LICENSE_ALERT is raised when the VXML Port license utilization exceeds 90% of the total deployed license ports and the
                                       VXML_LICENSE_ALERT_CLEAR is raised when the VXML port license utilization drops below 70% of the total deployed license ports. |
|---|---|