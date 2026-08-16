---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-connection-12x-integration-guide-egw-b-cuc12xintegw-html-1f48158393
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/12x/integration/guide/egw/b_cuc12xintegw.html
retrieved_at: 2026-08-16T14:19:35.264361+00:00
---

QSIG/DPNSS Phone System with Cisco EGW 2200 Integration Guide for Cisco Unity Connection Release 12.x

# QSIG/DPNSS Phone System with Cisco EGW 2200 Integration Guide for Cisco Unity Connection Release 12.x

Log in to Save Content

### Download Options

Updated: January 22, 2019

# QSIG/DPNSS Phone
            	 System with Cisco EGW 2200 Integration Guide for Cisco Unity Connection Release
            	 12.x

## Introduction

Published May, 2015

This document provides instructions for integrating a QSIG/DPNSS phone
                  		system with Cisco Unity Connection through a Cisco EGW 2200.

## Prerequisites

The QSIG/DPNSS integration supports configurations of the
                  		following components:

### Phone
                  	 System

A QSIG/DPNSS phone system.

The phone system ready for the integration as
                           			 described in the documentation for the phone system and for the Cisco EGW 2200.

A VoIP gateway configured and connected to the
                           			 QSIG/DPNSS phone system.

### Unity Connection
                  	 Server

Unity Connection installed and ready for the integration, as
                           			 described in the “ Installing Cisco Unity
                              				Connection ” chapter of the Install,
                              				Upgrade, and Maintenance Guide for Cisco Unity Connection, Release 12.x ,
                           			 available at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/12x/install_upgrade/guide/b_12xcuciumg.html .

A license that enables the applicable number of voice messaging
                           			 ports.

A Cisco EGW 2200 ready for the integration as described in the
                           			 Cisco EGW 2200 documentation.

The Cisco EGW 2200 connected to the LAN and configured for a
                           			 QSIG/DPNSS backhaul signaling stream from the VoIP gateway.

### Centralized Voice
                  	 Messaging

Unity Connection supports centralized voice messaging through
                     		the phone system, which supports various inter-phone system networking
                     		protocols including proprietary protocols such as Avaya DCS, Nortel MCDN, or
                     		Siemens CorNet, and standards-based protocols such as QSIG or DPNSS. Note that
                     		centralized voice messaging is a function of the phone system and its
                     		inter-phone system networking, not voicemail. Unity Connection will support
                     		centralized voice messaging as long as the phone system and its inter-phone
                     		system networking are properly configured. For details, see the “ Centralized Voice
                        		  Messaging ” section in the “Integrating Unity Connection with the Phone
                     		System” chapter of the Design Guide for Cisco Unity Connection Release 12.x at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/12x/design/guide/b_12xcucdg.html .

## Integration
               	 Tasks

Before doing the following tasks to integrate Unity Connection
                  		with a QSIG/DPNSS phone system through a Cisco EGW 2200, confirm that Unity
                  		Connection is ready for the integration by completing the applicable tasks in
                  		the “ Installing Cisco Unity
                     		  Connection ” chapter of the Install, Upgrade,
                     		  and Maintenance Guide for Cisco Unity Connection, Release 12.x , available
                  		at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/12x/install_upgrade/guide/b_12xcuciumg.html .

### Task List to
                  	 Create the Integration

Use the following task list to integrate Unity Connection with
                     		the QSIG/DPNSS phone system.

Review the system and equipment requirements to confirm that all
                           			 phone system and Unity Connection server requirements have been met. See the
                           			 “ Prerequisites
                              				section on page 1 ”.

Plan how the voice messaging ports will be used by Unity
                           			 Connection. See the “ Planning
                              				the Usage of Voice Messaging Ports section on page 4 ”.

Program the QSIG/DPNSS phone system. See the “ Programming
                              				the QSIG/DPNSS Phone System" section on page 7 ”.

Set up the Cisco EGW 2200. See the “ Setting
                              				Up the Cisco EGW 2200 section on page 7 ”.

Create the integration. See the “ Creating
                              				a New Integration with the QSIG/DPNSS Phone System section on page 7 ”.

Test the integration. See the “ Testing
                              				the Integration section on page 10 ”.

If this integration is a second or subsequent integration, add
                           			 the applicable new user templates for the new phone system. See the “ Adding
                              				New User Templates for Multiple Integrations section on page 13 ”.

While integrating the Cisco Unity Connection with Cisco Unified
                                    			 Call Manager through a EGW uncheck the Synchronize guest time to host option
                                    			 for Unified Communications product line in Virtualized environment. This
                                    			 enables the Unified Communications to synchronize with their clock to external
                                    			 NTP servers.

## Integration
               	 Description

The QSIG/DPNSS integration uses a Cisco EGW 2200, which
                  		translates QSIG or DPNSS call signaling into SIP, a VoIP gateway, and the LAN
                  		to connect Unity Connection and a QSIG/DPNSS phone system. Figure 1 shows the
                  		required connections.

### Call Information

The QSIG/DPNSS integration sends the following information with forwarded calls:

The extension of the called party

The extension of the calling party (for internal calls) or the phone number of the calling party (if it is an external call
                           and the system uses caller ID)

The reason for the forward (the extension is busy, does not answer, or is set to forward all calls)

Unity Connection uses this information to answer the call appropriately. For example, a call forwarded to Unity Connection
                     is answered with the personal greeting of the user. If the phone system routes the call to Unity Connection without this information,
                     Unity Connection answers with the opening greeting.

### Integration Functionality

The QSIG/DPNSS integration with Unity Connection provides the following features:

Call forward to personal greeting

Call forward to busy greeting

Caller ID

Easy message access (a user can retrieve messages without entering an ID; Unity Connection identifies a user based on the
                           extension from which the call originated; a password may be required)

Identified user messaging (Unity Connection automatically identifies a user who leaves a message during a forwarded internal
                           call, based on the extension from which the call originated)

Message waiting indication (MWI)

### Integrations with
                  	 Multiple Phone Systems

When Unity Connection is installed as Cisco Business Edition—on
                     		the same server with Cisco Unified Communications Manager—Unity Connection
                     		cannot be integrated with multiple phone systems at one time.

When Unity Connection is not installed as Cisco Business
                     		Edition, Unity Connection can be integrated with two or more phone systems at
                     		one time. For information on and instructions for integrating Unity Connection
                     		with multiple phone systems, see the Multiple Phone System Integration Guide for Unity Connection
                        		  Release 12.x at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/12x/integration/guide/multiple_integration/b_cuc12xintmultiple.html .

## Planning the Usage
               	 of Voice Messaging Ports

Before programming the phone system, you need to plan how the
                     		  voice messaging ports will be used by Unity Connection. The following
                     		  considerations will affect the programming for the phone system (for example,
                     		  setting up the hunt group or call forwarding for the voice messaging ports):

The number of voice messaging ports installed.

For a Unity Connection cluster, each Unity Connection server
                     		  must have enough ports to handle all voice messaging traffic in case the other
                     		  server stops functioning.

The number of voice messaging ports that will answer calls.

The number of voice messaging ports that will only dial out, for
                           				example, to send message notification, to set message waiting indicators
                           				(MWIs), and to make telephone record and playback (TRAP) connections.

The following table describes the voice messaging port settings
                     		  in Unity Connection that can be set on Telephony Integrations > Port of
                     		  Cisco Unity Connection Administration.

Field

Considerations

Enabled

Check this check box.

Server

(When a Unity Connection cluster is configured) Select the
                                 					 name of the Unity Connection server that you want to handle this port.

Assign an equal number of answering and dial-out voice messaging
                                 					 ports to the Unity Connection servers so that they equally share the voice
                                 					 messaging traffic.

Answer Calls

Check this check box.

All voice messaging ports connecting to the phone system must
                                          					 have the Answer Calls check box checked. Otherwise, calls to
                                          					 Unity Connection may not be answered.

Perform Message Notification

Check this check box to designate the port for notifying users
                                 					 of messages.

Send MWI Requests

Check this check box to designate the port for turning MWIs on
                                 					 and off.

Allow TRAP Connections

Check this check box so that users can use the phone as a
                                 					 recording and playback device in Unity Connection web applications.

## Determining the
               	 Number of Voice Messaging Ports

The following tasks describe the process for determining the
                  		number of voice messaging ports for Unity Connection to install, answer call
                  		and dial out calls:

For determining the number of voice messaging ports to Install,
                        			 see “ Voice
                           				Messaging Ports to Install section on page 5 ”.

For determining the number of voice messaging ports to Answer
                        			 Calls, see “ Voice
                           				Messaging Ports to Answer Call section on page 5 ”.

For determining the number of voice messaging ports to Dial Out,
                        			 see “ Voice
                           				Messaging Ports to Dial Out section on page 6 ”.

### Voice Messaging
                  	 Ports to Install

The number of voice messaging ports to install depends on
                     		numerous factors, including:

The number of calls Unity Connection will answer when call
                           			 traffic is at its peak.

The expected length of each message that callers will record and
                           			 that users will listen to.

The number of users.

The number of calls made for message notification.

The number of MWIs that will be activated when call traffic is
                           			 at its peak.

The number of TRAP connections needed when call traffic is at
                           			 its peak. (TRAP connections are used by Unity Connection web applications to
                           			 play back and record over the phone.)

The number of calls that will use the automated attendant and
                           			 call handlers when call traffic is at its peak.

It is best to install only the number of voice messaging ports
                     		that are needed so that system resources are not allocated to unused ports.

If your system is configured for a Unity Connection cluster, see
                     		the “ Considerations
                        		  for a Unity Connection Cluster section on page 6 ”.

### Voice Messaging
                  	 Ports to Answer Call

The calls that the voice messaging ports answer can be incoming
                     		calls from unidentified callers or from users. Assign all of the voice
                     		messaging ports to answer calls.

You can set voice messaging ports to both answer calls and to
                     		dial out (for example, to send message notifications).

If your system is configured for a Unity Connection cluster, see
                     		the “ Considerations
                        		  for a Unity Connection Cluster section on page 6 ”.

### Voice Messaging
                  	 Ports to Dial Out

Ports that will dial out can do one or more of the following:

Notify users by phone, pager, or email of messages that have
                           			 arrived.

Turn MWIs on and off for user extensions.

Make a TRAP connection so that users can use the phone as a
                           			 recording and playback device in Unity Connection web applications.

If your system is configured for a Unity Connection cluster, see
                     		the “ Considerations
                        		  for a Unity Connection Cluster section on page 6 ”.

## Considerations for a Unity Connection Cluster

If your system is configured for a Unity Connection cluster, consider how the voice messaging ports will be used in different
                  scenarios.

### When Both Unity Connection Servers are Functioning

A hunt group is configured on the phone system to distribute calls equally to both Unity Connection servers.

The network is configured to send incoming calls first to the subscriber server, then to the publisher server if no answering
                           ports are available on the subscriber server.

Both Unity Connection servers are active and handle voice messaging traffic for the system.

In Cisco Unity Connection Administration, the voice messaging ports are configured so that an equal number of voice messaging
                           ports are assigned to each Unity Connection server. This guide directs you to assign the voice messaging ports to their specific
                           server at the applicable time.

The number of voice messaging ports that are assigned to one Unity Connection server must be sufficient to handle all of the
                           voice messaging traffic for the system (answering calls and dialing out) when the other Unity Connection server stops functioning.

If both Unity Connection servers must be functioning to handle the voice messaging traffic, the system will not have sufficient
                     capacity when one of the servers stops functioning.

Each Unity Connection server is assigned half the total number of voice messaging ports.

If all the voice messaging ports are assigned to one Unity Connection server, the other Unity Connection server will not be
                     able to answer calls or to dial out.

Each Unity Connection server must have voice messaging ports that will answer calls and that can dial out (for example, to
                           set MWIs).

### When Only One Unity Connection Server is Functioning

The hunt group on the phone system sends all calls to the functioning Unity Connection server.

The functioning Unity Connection server receives all voice messaging traffic for the system.

The number of voice messaging ports that are assigned to the functioning Unity Connection server must be sufficient to handle
                           all of the voice messaging traffic for the system (answering calls and dialing out).

The functioning Unity Connection server must have voice messaging ports that will answer calls and that can dial out (for
                           example, to set MWIs).

If the functioning Unity Connection server does not have voice messaging ports for answering calls, the system will not be
                     able to answer incoming calls. Similarly, if the functioning Unity Connection server does not have voice messaging ports for
                     dialing out, the system will not be able to dial out (for example, to set MWIs).

## Programming the QSIG/DPNSS Phone System

For information on provisioning a QSIG or DPNSS
                  		phone system to integrate with Unity Connection, see the Cisco EGW 2200
                  		documentation.

In programming the phone system, do not send calls to
                           		voice messaging ports in Unity Connection that cannot answer calls (voice
                           		messaging ports that are not set to Answer Calls). For example, if a voice
                           		messaging port is set only to Dialout MWI, do not send calls to it.

## Setting Up the Cisco EGW 2200

For information on setting up the Cisco EGW 2200,
                  		see the Cisco EGW 2200 documentation.

For a Unity Connection cluster, identify the Unity
                           		Connection servers with a fully qualified domain name (FQDN), and configure a
                           		DNS server to resolve the FQDN to the IP addresses and SIP ports of the Unity
                           		Connection server.

## Creating a New
               	 Integration with the QSIG/DPNSS Phone System

After ensuring that QSIG/DPNSS phone system and Unity Connection
                     		  are ready for the integration, do the following procedure to set up the
                     		  integration and to enter the port settings.

Procedure

### Procedure

In Cisco Unity Connection Administration, expand Telephony Integrations , then select Phone System .

On the Search Phone Systems page, under Display Name, select the
                              			 name of the default phone system.

On the Phone System Basics page, in the Phone System Name field,
                              			 enter the descriptive name that you want for the phone system.

If you want to use this phone system as the default for TRaP
                              			 connections so that administrators and users without voicemail boxes can record
                              			 and playback through the phone in Cisco Unity Connection web applications,
                              			 check the Default TRAP Switch check box. If you want to use
                              			 another phone system as the default for TRaP connections, uncheck this check
                              			 box.

Select Save .

On the Phone System Basics page, in the Related Links drop-down
                              			 box, select Add Port Group and select Go .

On the New Port Group page, enter the applicable settings and
                              			 select Save .

Field

Setting

Phone System

Select the name of the phone system that you entered in Step 3 .

Create From

Select Port Group Template and
                                             						  select SIP in the drop-down
                                             						  box.

Display Name

Enter a descriptive name for the port group. You can accept the
                                             						  default name or enter the name that you want.

Authenticate with SIP Server

Uncheck this check box.

Authentication User Name

Leave this field blank.

Authentication Password

Leave this field blank.

Contact Line Name

Enter the voice messaging pilot number that matches the dial
                                             						  plan configuration of the gateway.

SIP Security Profile

Select 5060 .

SIP Transport Protocol

Select the SIP transport protocol that Cisco Unity Connection
                                             						  will use.

IPv4 Address or Host Name

Enter the IP address (or host name) of the primary gateway that
                                             						  you are connecting to Unity Connection.

IPv6 Address or Host Name

Do not enter a value in this field. IPv6 is not supported for
                                             						  EGW 2200 integrations.

IP Address or Host Name

Enter the IP address (or host name) of the primary gateway that
                                             						  you are connecting to Unity Connection.

Port

Enter the IP port of the primary gateway that you are connecting
                                             						  to Unity Connection. We recommend that you use the default setting.

This setting must match the port setting of the gateway.
                                                      						  Otherwise the integration will not function correctly.

On the Port Group Basics page, do the following substeps if
                              			 there is a secondary gateway. Otherwise, continue to Step 9 .

On the Edit menu, select Servers .

On the Edit Servers page, under SIP Servers, select Add .

Enter the following settings for the secondary gateway and
                                    				  select Save .

Field

Setting

Order

Enter the order of
                                                   								priority for the gateway. The lowest number is the primary gateway, the higher
                                                   								numbers are the secondary gateways.

IPv4 Address or Host Name

Enter the IP address (or
                                                   								host name) of the secondary gateway.

IPv6 Address or Host Name

Do not enter a value in
                                                   								this field. IPv6 is not supported for EGW 2200 integrations.

IP Address or Host Name

Enter the IP address (or
                                                   								host name) of the secondary gateway.

Port

Enter the IP port of the
                                                   								secondary gateway that you are connecting to Unity Connection. We recommend
                                                   								that you use the default setting.

Repeat Step 8 b. and Step 8 c. for all remaining
                                    				  secondary gateways.

On the Edit menu, select Port Group Basics .

Select Reset .

On the Port Group Basics page, in the Related Links drop-down
                              			 box, select Add Ports and
                              			 select Go .

On the New Port page, enter the following settings and select Save .

Field

Considerations

Enabled

Check this check box.

Number of Ports

Enter the number of voice
                                             						  messaging ports that you want to create in this port group.

For a Unity Connection cluster, you must enter the total number
                                                      						  of voice messaging ports that will be used by all Unity Connection servers.
                                                      						  Each port will later be assigned to a specific Unity Connection server.

Phone System

Select the name of the
                                             						  phone system that you entered in Step 3 .

Port Group

Select the name of the
                                             						  port group that you added in Step 7 .

Server

Select the name of the
                                             						  Unity Connection server.

On the Search Ports page, select the display name of the first
                              			 voice messaging port that you created for this phone system integration.

By default, the display names for the voice messaging ports are
                                             				  composed of the port group display name followed by incrementing numbers.

On the Port Basics page, set the voice messaging port settings
                              			 as applicable. The fields in the following table are the ones that you can
                              			 change.

Field

Considerations

Enabled

Check this check box to
                                             						  enable the port. The port is enabled during normal operation.

Uncheck this check box to
                                             						  disable the port. When the port is disabled, calls to the port get a ringing
                                             						  tone but are not answered. Typically, the port is disabled only by the
                                             						  installer during testing.

Server

(For Unity Connection
                                                							 clusters only) Select the name of the Unity Connection server that you want
                                             						  to handle this port.

Assign an equal number of
                                             						  answering and dial-out voice messaging ports to the Unity Connection servers so
                                             						  that they equally share the voice messaging traffic.

Answer Calls

Check this check box to
                                             						  designate the port for answering calls. These calls can be incoming calls from
                                             						  unidentified callers or from users.

Perform Message
                                             						  Notification

Check this check box to
                                             						  designate the port for notifying users of messages. Assign Perform Message
                                             						  Notification to the least busy ports.

Send MWI Requests

Check this check box to
                                             						  designate the port for turning MWIs on and off. Assign Send MWI Requests to the
                                             						  least busy ports.

Allow TRAP Connections

Check this check box so
                                             						  that users can use the port for recording and playback through the phone in
                                             						  Unity Connection web applications. Assign Allow TRAP Connections to the least
                                             						  busy ports.

Select Save .

Select Next .

Repeat Step 12 through Step 14 for all
                              			 remaining voice messaging ports for the phone system.

If another phone system integration exists, in Cisco Unity
                              			 Connection Administration, expand Telephony
                                 				Integrations , then select Trunk .
                              			 Otherwise, skip to Step 20 .

On the Search Phone System Trunks page, on the Phone System
                              			 Trunk menu, select New Phone System
                                 				Trunk .

On the New Phone System Trunk page, enter the following settings
                              			 for the phone system trunk and select Save .

Field

Setting

From Phone System

Select the display name
                                             						  of the phone system that you are creating a trunk for.

To Phone System

Select the display name
                                             						  of the previously existing phone system that the trunk will connect to.

Trunk Access Code

Enter the extra digits
                                             						  that Unity Connection must dial to transfer calls through the gateway to
                                             						  extensions on the previously existing phone system.

Repeat Step 17 and Step 18 for all
                              			 remaining phone system trunks that you want to create.

In the Related Links drop-down list, select Check Telephony
                                 				Configuration and select Go to confirm
                              			 the phone system integration settings.

If the test is not successful, the Task Execution Results
                                 				displays one or more messages with troubleshooting steps. After correcting the
                                 				problems, test the Unity Connection again.

In the Task Execution Results window, select Close .

## Testing the
               	 Integration

To test whether Unity Connection and the phone system are
                  		integrated correctly, do the following procedures in the order listed.

If any of the steps indicate a failure, see the following
                  		documentation as applicable:

The installation guide for the phone system.

Troubleshooting Guide for Cisco Unity Connection Release
                           				11.x , available at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/12x/troubleshooting/guide/b_12xcuctsg.html .

The setup information earlier in this guide.

### Setting Up Test
                  	 Configuration

Procedure

#### Procedure

Set up two test extensions (Phone 1 and Phone 2) on the same
                                 			 phone system that Unity Connection is connected to.

Set Phone 1 to forward calls to the Unity Connection pilot
                                 			 number when calls are not answered.

The phone system must forward calls to the Unity Connection
                                             				pilot number in no fewer than four rings. Otherwise, the test may fail.

In Cisco Unity Connection Administration, expand Users , then select Users .

On the Search Users page, select the display name of a user to
                                 			 use for testing. The extension for this user must be the extension for Phone 1.

On the Edit User Basics page, uncheck the Set for Self-enrollment at Next Login check box.

In the Voice Name field, record a recorded name for the test
                                 			 user.

Select Save .

On the Edit menu, select Message Waiting Indicators .

On the Message Waiting Indicators page, select the message
                                 			 waiting indicator. If no message waiting indication is in the table, select Add New .

On the Edit Message Waiting Indicator page, enter the following
                                 			 settings.

Field

Setting

Enabled

Check this check box to enable MWIs for the test user.

Display Name

Accept the default or enter a different name.

Inherit User’s Extension

Check this check box to enable MWIs on Phone 1.

Select Save .

On the Edit menu, select Transfer Rules .

On the Transfer Rules page, select the active rule.

On the Edit Transfer Rule page, under Transfer Action, select Extension and enter the extension of Phone 1.

In the Transfer Type field, select Release to Switch .

Select Save .

Minimize the Cisco Unity Connection Administration window.

Do not close
                                    				the Cisco Unity Connection Administration window because you will use it again
                                    				in a later procedure.

Sign in to the
                                 			 Real-Time Monitoring Tool (RTMT).

On the Unity
                                 			 Connection menu, select Port Monitor . The Port Monitor tool appears in the
                                 			 right pane.

In the right
                                 			 pane, select Start Polling . The Port Monitor will display which
                                 			 port is handling the calls that you will make.

### Testing an
                  	 External Call with Release Transfer

Procedure

#### Procedure

From Phone 2, enter the access code necessary to get an outside
                                 			 line, then enter the number outside callers use to dial directly to Unity
                                 			 Connection.

In the Port Monitor, note which port handles this call.

When you hear the opening greeting, enter the extension for
                                 			 Phone 1. Hearing the opening greeting means that the port is configured
                                 			 correctly.

Confirm that Phone 1 rings and that you hear a ringback tone on
                                 			 Phone 2. Hearing a ringback tone means that Unity Connection correctly released
                                 			 the call and transferred it to Phone 1.

Leaving Phone 1 unanswered, confirm that the state of the port
                                 			 handling the call changes to “Idle.” This state means that release transfer is
                                 			 successful.

Confirm that, after the number of rings that the phone system is
                                 			 set to wait, the call is forwarded to Unity Connection and that you hear the
                                 			 greeting for the test user. Hearing the greeting means that the phone system
                                 			 forwarded the unanswered call and the call-forward information to Unity
                                 			 Connection, which correctly interpreted the information.

On the Port Monitor, note which port handles this call.

Leave a message for the test user and hang up Phone 2.

In the Port Monitor, confirm that the state of the port handling
                                 			 the call changes to “Idle.” This state means that the port was successfully
                                 			 released when the call ended.

Confirm that the MWI on Phone 1 is activated. The activated MWI
                                 			 means that the phone system and Unity Connection are successfully integrated
                                 			 for turning on MWIs.

### Testing Listening
                  	 to the Messages

Procedure

#### Procedure

From Phone 1, enter the internal pilot number for Unity
                                 			 Connection.

When asked for your password, enter the password for the test
                                 			 user. Hearing the request for your password means that the phone system sent
                                 			 the necessary call information to Unity Connection, which correctly interpreted
                                 			 the information.

Confirm that you hear the recorded name for the test user (if
                                 			 you did not record a name for the test user, you will hear the extension number
                                 			 for Phone 1). Hearing the recorded name means that Unity Connection correctly
                                 			 identified the user by the extension.

Listen to the message.

After listening to the message, delete the message.

Confirm that the MWI on Phone 1 is deactivated. The deactivated
                                 			 MWI means that the phone system and Unity Connection are successfully
                                 			 integrated for turning off MWIs.

Hang up Phone 1.

On the Port Monitor, confirm that the state of the port handling
                                 			 the call changes to “Idle.” This state means that the port was successfully
                                 			 released when the call ended.

### Setting Up
                  	 Supervised Transfer on Unity Connection

Procedure

#### Procedure

In Cisco Unity Connection Administration, on the Edit Transfer
                                 			 Rule page for the test user, in the Transfer Type field, select Supervise Transfer .

In the Rings to Wait For field, enter 3 .

Select Save .

Minimize the Cisco Unity Connection Administration window.

Do not close
                                 			 the Cisco Unity Connection Administration window because you will use it again
                                 			 in a later procedure.

### Testing Supervised
                  	 Transfer

Procedure

#### Procedure

From Phone 2, enter the access code necessary to get an outside
                                 			 line, then enter the number outside callers use to dial directly to Unity
                                 			 Connection.

On the Port Monitor, note which port handles this call.

When you hear the opening greeting, enter the extension for
                                 			 Phone 1. Hearing the opening greeting means that the port is configured
                                 			 correctly.

Confirm that Phone 1 rings and that you do not hear a ringback
                                 			 tone on Phone 2. Instead, you should hear the indication your phone system uses
                                 			 to mean that the call is on hold (for example, music).

Leaving Phone 1 unanswered, confirm that the state of the port
                                 			 handling the call remains “Busy.” This state and hearing an indication that you
                                 			 are on hold mean that Unity Connection is supervising the transfer.

Confirm that, after three rings, you hear the greeting for the
                                 			 test user. Hearing the greeting means that Unity Connection successfully
                                 			 recalled the supervised-transfer call.

During the greeting, hang up Phone 2.

On the Port Monitor, confirm that the state of the port handling
                                 			 the call changes to “Idle.” This state means that the port was successfully
                                 			 released when the call ended.

Select Stop Polling .

Sign out of RTMT.

## Adding New User
               	 Templates for Multiple Integrations

When you create the first phone system integration, this phone
                  		system is automatically selected in the default user template. The users that
                  		you add after creating this phone system integration will be assigned to this
                  		phone system by default.

However, for each additional phone system integration that you
                  		create, you must add the applicable new user templates that will assign users
                  		to the new phone system. You must add the new templates before you add new
                  		users who will be assigned to the new phone system.

For details on adding new user templates, or on selecting a user
                  		template when adding a new user, see the “ User Attributes ”
                  		chapter of the System Administration Guide for Cisco Unity Connection Release
                     		  12.x . The guide is available at

https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/12x/administration/guide/b_12xcucsag.html .

Cisco and the Cisco Logo
                     		  are trademarks of Cisco Systems, Inc. and/or its affiliates in the U.S. and
                     		  other countries. A listing of Cisco's trademarks can be found at www.cisco.com/go/trademarks .
                     		  Third party trademarks mentioned are the property of their respective owners.
                     		  The use of the word partner does not imply a partnership relationship between
                     		  Cisco and any other company. (1005R)

Any Internet Protocol (IP)
                     		  addresses used in this document are not intended to be actual addresses. Any
                     		  examples, command display output, and figures included in the document are
                     		  shown for illustrative purposes only. Any use of actual IP addresses in
                     		  illustrative content is unintentional and coincidental.

© 2015 Cisco Systems, Inc.
                     		  All rights reserved.

### Contact Cisco

- Open a Support Case

- (Requires a Cisco Service Contract )

### This Document Applies to These Products

- Unity Connection Version 12.x

| Note | While integrating the Cisco Unity Connection with Cisco Unified
                                    			 Call Manager through a EGW uncheck the Synchronize guest time to host option
                                    			 for Unified Communications product line in Virtualized environment. This
                                    			 enables the Unified Communications to synchronize with their clock to external
                                    			 NTP servers. |
|---|---|

| Field | Considerations |
|---|---|
| Enabled | Check this check box. |
| Server | (When a Unity Connection cluster is configured) Select the
                                 					 name of the Unity Connection server that you want to handle this port. Assign an equal number of answering and dial-out voice messaging
                                 					 ports to the Unity Connection servers so that they equally share the voice
                                 					 messaging traffic. |
| Answer Calls | Check this check box. Caution All voice messaging ports connecting to the phone system must
                                          					 have the Answer Calls check box checked. Otherwise, calls to
                                          					 Unity Connection may not be answered. | Caution | All voice messaging ports connecting to the phone system must
                                          					 have the Answer Calls check box checked. Otherwise, calls to
                                          					 Unity Connection may not be answered. |
| Caution | All voice messaging ports connecting to the phone system must
                                          					 have the Answer Calls check box checked. Otherwise, calls to
                                          					 Unity Connection may not be answered. |
| Perform Message Notification | Check this check box to designate the port for notifying users
                                 					 of messages. |
| Send MWI Requests | Check this check box to designate the port for turning MWIs on
                                 					 and off. |
| Allow TRAP Connections | Check this check box so that users can use the phone as a
                                 					 recording and playback device in Unity Connection web applications. |

| Caution | All voice messaging ports connecting to the phone system must
                                          					 have the Answer Calls check box checked. Otherwise, calls to
                                          					 Unity Connection may not be answered. |
|---|---|

| Caution | In programming the phone system, do not send calls to
                           		voice messaging ports in Unity Connection that cannot answer calls (voice
                           		messaging ports that are not set to Answer Calls). For example, if a voice
                           		messaging port is set only to Dialout MWI, do not send calls to it. |
|---|---|

| Note | For a Unity Connection cluster, identify the Unity
                           		Connection servers with a fully qualified domain name (FQDN), and configure a
                           		DNS server to resolve the FQDN to the IP addresses and SIP ports of the Unity
                           		Connection server. |
|---|---|

| Step 1 | In Cisco Unity Connection Administration, expand Telephony Integrations , then select Phone System . |
|---|---|
| Step 2 | On the Search Phone Systems page, under Display Name, select the
                              			 name of the default phone system. |
| Step 3 | On the Phone System Basics page, in the Phone System Name field,
                              			 enter the descriptive name that you want for the phone system. |
| Step 4 | If you want to use this phone system as the default for TRaP
                              			 connections so that administrators and users without voicemail boxes can record
                              			 and playback through the phone in Cisco Unity Connection web applications,
                              			 check the Default TRAP Switch check box. If you want to use
                              			 another phone system as the default for TRaP connections, uncheck this check
                              			 box. |
| Step 5 | Select Save . |
| Step 6 | On the Phone System Basics page, in the Related Links drop-down
                              			 box, select Add Port Group and select Go . |
| Step 7 | On the New Port Group page, enter the applicable settings and
                              			 select Save . Table 2. Settings for the New Port Group Page Field Setting Phone System Select the name of the phone system that you entered in Step 3 . Create From Select Port Group Template and
                                             						  select SIP in the drop-down
                                             						  box. Display Name Enter a descriptive name for the port group. You can accept the
                                             						  default name or enter the name that you want. Authenticate with SIP Server Uncheck this check box. Authentication User Name Leave this field blank. Authentication Password Leave this field blank. Contact Line Name Enter the voice messaging pilot number that matches the dial
                                             						  plan configuration of the gateway. SIP Security Profile Select 5060 . SIP Transport Protocol Select the SIP transport protocol that Cisco Unity Connection
                                             						  will use. IPv4 Address or Host Name Enter the IP address (or host name) of the primary gateway that
                                             						  you are connecting to Unity Connection. IPv6 Address or Host Name Do not enter a value in this field. IPv6 is not supported for
                                             						  EGW 2200 integrations. IP Address or Host Name Enter the IP address (or host name) of the primary gateway that
                                             						  you are connecting to Unity Connection. Port Enter the IP port of the primary gateway that you are connecting
                                             						  to Unity Connection. We recommend that you use the default setting. Caution This setting must match the port setting of the gateway.
                                                      						  Otherwise the integration will not function correctly. | Field | Setting | Phone System | Select the name of the phone system that you entered in Step 3 . | Create From | Select Port Group Template and
                                             						  select SIP in the drop-down
                                             						  box. | Display Name | Enter a descriptive name for the port group. You can accept the
                                             						  default name or enter the name that you want. | Authenticate with SIP Server | Uncheck this check box. | Authentication User Name | Leave this field blank. | Authentication Password | Leave this field blank. | Contact Line Name | Enter the voice messaging pilot number that matches the dial
                                             						  plan configuration of the gateway. | SIP Security Profile | Select 5060 . | SIP Transport Protocol | Select the SIP transport protocol that Cisco Unity Connection
                                             						  will use. | IPv4 Address or Host Name | Enter the IP address (or host name) of the primary gateway that
                                             						  you are connecting to Unity Connection. | IPv6 Address or Host Name | Do not enter a value in this field. IPv6 is not supported for
                                             						  EGW 2200 integrations. | IP Address or Host Name | Enter the IP address (or host name) of the primary gateway that
                                             						  you are connecting to Unity Connection. | Port | Enter the IP port of the primary gateway that you are connecting
                                             						  to Unity Connection. We recommend that you use the default setting. Caution This setting must match the port setting of the gateway.
                                                      						  Otherwise the integration will not function correctly. | Caution | This setting must match the port setting of the gateway.
                                                      						  Otherwise the integration will not function correctly. |
| Field | Setting |
| Phone System | Select the name of the phone system that you entered in Step 3 . |
| Create From | Select Port Group Template and
                                             						  select SIP in the drop-down
                                             						  box. |
| Display Name | Enter a descriptive name for the port group. You can accept the
                                             						  default name or enter the name that you want. |
| Authenticate with SIP Server | Uncheck this check box. |
| Authentication User Name | Leave this field blank. |
| Authentication Password | Leave this field blank. |
| Contact Line Name | Enter the voice messaging pilot number that matches the dial
                                             						  plan configuration of the gateway. |
| SIP Security Profile | Select 5060 . |
| SIP Transport Protocol | Select the SIP transport protocol that Cisco Unity Connection
                                             						  will use. |
| IPv4 Address or Host Name | Enter the IP address (or host name) of the primary gateway that
                                             						  you are connecting to Unity Connection. |
| IPv6 Address or Host Name | Do not enter a value in this field. IPv6 is not supported for
                                             						  EGW 2200 integrations. |
| IP Address or Host Name | Enter the IP address (or host name) of the primary gateway that
                                             						  you are connecting to Unity Connection. |
| Port | Enter the IP port of the primary gateway that you are connecting
                                             						  to Unity Connection. We recommend that you use the default setting. Caution This setting must match the port setting of the gateway.
                                                      						  Otherwise the integration will not function correctly. | Caution | This setting must match the port setting of the gateway.
                                                      						  Otherwise the integration will not function correctly. |
| Caution | This setting must match the port setting of the gateway.
                                                      						  Otherwise the integration will not function correctly. |
| Step 8 | On the Port Group Basics page, do the following substeps if
                              			 there is a secondary gateway. Otherwise, continue to Step 9 . On the Edit menu, select Servers . On the Edit Servers page, under SIP Servers, select Add . Enter the following settings for the secondary gateway and
                                    				  select Save . Table 3. Settings for the
                                             					 Secondary Gateways Field Setting Order Enter the order of
                                                   								priority for the gateway. The lowest number is the primary gateway, the higher
                                                   								numbers are the secondary gateways. IPv4 Address or Host Name Enter the IP address (or
                                                   								host name) of the secondary gateway. IPv6 Address or Host Name Do not enter a value in
                                                   								this field. IPv6 is not supported for EGW 2200 integrations. IP Address or Host Name Enter the IP address (or
                                                   								host name) of the secondary gateway. Port Enter the IP port of the
                                                   								secondary gateway that you are connecting to Unity Connection. We recommend
                                                   								that you use the default setting. Repeat Step 8 b. and Step 8 c. for all remaining
                                    				  secondary gateways. On the Edit menu, select Port Group Basics . Select Reset . | Field | Setting | Order | Enter the order of
                                                   								priority for the gateway. The lowest number is the primary gateway, the higher
                                                   								numbers are the secondary gateways. | IPv4 Address or Host Name | Enter the IP address (or
                                                   								host name) of the secondary gateway. | IPv6 Address or Host Name | Do not enter a value in
                                                   								this field. IPv6 is not supported for EGW 2200 integrations. | IP Address or Host Name | Enter the IP address (or
                                                   								host name) of the secondary gateway. | Port | Enter the IP port of the
                                                   								secondary gateway that you are connecting to Unity Connection. We recommend
                                                   								that you use the default setting. |
| Field | Setting |
| Order | Enter the order of
                                                   								priority for the gateway. The lowest number is the primary gateway, the higher
                                                   								numbers are the secondary gateways. |
| IPv4 Address or Host Name | Enter the IP address (or
                                                   								host name) of the secondary gateway. |
| IPv6 Address or Host Name | Do not enter a value in
                                                   								this field. IPv6 is not supported for EGW 2200 integrations. |
| IP Address or Host Name | Enter the IP address (or
                                                   								host name) of the secondary gateway. |
| Port | Enter the IP port of the
                                                   								secondary gateway that you are connecting to Unity Connection. We recommend
                                                   								that you use the default setting. |
| Step 9 | On the Port Group Basics page, in the Related Links drop-down
                              			 box, select Add Ports and
                              			 select Go . |
| Step 10 | On the New Port page, enter the following settings and select Save . Table 4. Settings for the New Ports Page Field Considerations Enabled Check this check box. Number of Ports Enter the number of voice
                                             						  messaging ports that you want to create in this port group. Note For a Unity Connection cluster, you must enter the total number
                                                      						  of voice messaging ports that will be used by all Unity Connection servers.
                                                      						  Each port will later be assigned to a specific Unity Connection server. Phone System Select the name of the
                                             						  phone system that you entered in Step 3 . Port Group Select the name of the
                                             						  port group that you added in Step 7 . Server Select the name of the
                                             						  Unity Connection server. | Field | Considerations | Enabled | Check this check box. | Number of Ports | Enter the number of voice
                                             						  messaging ports that you want to create in this port group. Note For a Unity Connection cluster, you must enter the total number
                                                      						  of voice messaging ports that will be used by all Unity Connection servers.
                                                      						  Each port will later be assigned to a specific Unity Connection server. | Note | For a Unity Connection cluster, you must enter the total number
                                                      						  of voice messaging ports that will be used by all Unity Connection servers.
                                                      						  Each port will later be assigned to a specific Unity Connection server. | Phone System | Select the name of the
                                             						  phone system that you entered in Step 3 . | Port Group | Select the name of the
                                             						  port group that you added in Step 7 . | Server | Select the name of the
                                             						  Unity Connection server. |
| Field | Considerations |
| Enabled | Check this check box. |
| Number of Ports | Enter the number of voice
                                             						  messaging ports that you want to create in this port group. Note For a Unity Connection cluster, you must enter the total number
                                                      						  of voice messaging ports that will be used by all Unity Connection servers.
                                                      						  Each port will later be assigned to a specific Unity Connection server. | Note | For a Unity Connection cluster, you must enter the total number
                                                      						  of voice messaging ports that will be used by all Unity Connection servers.
                                                      						  Each port will later be assigned to a specific Unity Connection server. |
| Note | For a Unity Connection cluster, you must enter the total number
                                                      						  of voice messaging ports that will be used by all Unity Connection servers.
                                                      						  Each port will later be assigned to a specific Unity Connection server. |
| Phone System | Select the name of the
                                             						  phone system that you entered in Step 3 . |
| Port Group | Select the name of the
                                             						  port group that you added in Step 7 . |
| Server | Select the name of the
                                             						  Unity Connection server. |
| Step 11 | On the Search Ports page, select the display name of the first
                              			 voice messaging port that you created for this phone system integration. Note By default, the display names for the voice messaging ports are
                                             				  composed of the port group display name followed by incrementing numbers. | Note | By default, the display names for the voice messaging ports are
                                             				  composed of the port group display name followed by incrementing numbers. |
| Note | By default, the display names for the voice messaging ports are
                                             				  composed of the port group display name followed by incrementing numbers. |
| Step 12 | On the Port Basics page, set the voice messaging port settings
                              			 as applicable. The fields in the following table are the ones that you can
                              			 change. Table 5. Settings for the Voice Messaging Ports Field Considerations Enabled Check this check box to
                                             						  enable the port. The port is enabled during normal operation. Uncheck this check box to
                                             						  disable the port. When the port is disabled, calls to the port get a ringing
                                             						  tone but are not answered. Typically, the port is disabled only by the
                                             						  installer during testing. Server (For Unity Connection
                                                							 clusters only) Select the name of the Unity Connection server that you want
                                             						  to handle this port. Assign an equal number of
                                             						  answering and dial-out voice messaging ports to the Unity Connection servers so
                                             						  that they equally share the voice messaging traffic. Answer Calls Check this check box to
                                             						  designate the port for answering calls. These calls can be incoming calls from
                                             						  unidentified callers or from users. Perform Message
                                             						  Notification Check this check box to
                                             						  designate the port for notifying users of messages. Assign Perform Message
                                             						  Notification to the least busy ports. Send MWI Requests Check this check box to
                                             						  designate the port for turning MWIs on and off. Assign Send MWI Requests to the
                                             						  least busy ports. Allow TRAP Connections Check this check box so
                                             						  that users can use the port for recording and playback through the phone in
                                             						  Unity Connection web applications. Assign Allow TRAP Connections to the least
                                             						  busy ports. | Field | Considerations | Enabled | Check this check box to
                                             						  enable the port. The port is enabled during normal operation. Uncheck this check box to
                                             						  disable the port. When the port is disabled, calls to the port get a ringing
                                             						  tone but are not answered. Typically, the port is disabled only by the
                                             						  installer during testing. | Server | (For Unity Connection
                                                							 clusters only) Select the name of the Unity Connection server that you want
                                             						  to handle this port. Assign an equal number of
                                             						  answering and dial-out voice messaging ports to the Unity Connection servers so
                                             						  that they equally share the voice messaging traffic. | Answer Calls | Check this check box to
                                             						  designate the port for answering calls. These calls can be incoming calls from
                                             						  unidentified callers or from users. | Perform Message
                                             						  Notification | Check this check box to
                                             						  designate the port for notifying users of messages. Assign Perform Message
                                             						  Notification to the least busy ports. | Send MWI Requests | Check this check box to
                                             						  designate the port for turning MWIs on and off. Assign Send MWI Requests to the
                                             						  least busy ports. | Allow TRAP Connections | Check this check box so
                                             						  that users can use the port for recording and playback through the phone in
                                             						  Unity Connection web applications. Assign Allow TRAP Connections to the least
                                             						  busy ports. |
| Field | Considerations |
| Enabled | Check this check box to
                                             						  enable the port. The port is enabled during normal operation. Uncheck this check box to
                                             						  disable the port. When the port is disabled, calls to the port get a ringing
                                             						  tone but are not answered. Typically, the port is disabled only by the
                                             						  installer during testing. |
| Server | (For Unity Connection
                                                							 clusters only) Select the name of the Unity Connection server that you want
                                             						  to handle this port. Assign an equal number of
                                             						  answering and dial-out voice messaging ports to the Unity Connection servers so
                                             						  that they equally share the voice messaging traffic. |
| Answer Calls | Check this check box to
                                             						  designate the port for answering calls. These calls can be incoming calls from
                                             						  unidentified callers or from users. |
| Perform Message
                                             						  Notification | Check this check box to
                                             						  designate the port for notifying users of messages. Assign Perform Message
                                             						  Notification to the least busy ports. |
| Send MWI Requests | Check this check box to
                                             						  designate the port for turning MWIs on and off. Assign Send MWI Requests to the
                                             						  least busy ports. |
| Allow TRAP Connections | Check this check box so
                                             						  that users can use the port for recording and playback through the phone in
                                             						  Unity Connection web applications. Assign Allow TRAP Connections to the least
                                             						  busy ports. |
| Step 13 | Select Save . |
| Step 14 | Select Next . |
| Step 15 | Repeat Step 12 through Step 14 for all
                              			 remaining voice messaging ports for the phone system. |
| Step 16 | If another phone system integration exists, in Cisco Unity
                              			 Connection Administration, expand Telephony
                                 				Integrations , then select Trunk .
                              			 Otherwise, skip to Step 20 . |
| Step 17 | On the Search Phone System Trunks page, on the Phone System
                              			 Trunk menu, select New Phone System
                                 				Trunk . |
| Step 18 | On the New Phone System Trunk page, enter the following settings
                              			 for the phone system trunk and select Save . Table 6. Settings for the Phone System Trunk Field Setting From Phone System Select the display name
                                             						  of the phone system that you are creating a trunk for. To Phone System Select the display name
                                             						  of the previously existing phone system that the trunk will connect to. Trunk Access Code Enter the extra digits
                                             						  that Unity Connection must dial to transfer calls through the gateway to
                                             						  extensions on the previously existing phone system. | Field | Setting | From Phone System | Select the display name
                                             						  of the phone system that you are creating a trunk for. | To Phone System | Select the display name
                                             						  of the previously existing phone system that the trunk will connect to. | Trunk Access Code | Enter the extra digits
                                             						  that Unity Connection must dial to transfer calls through the gateway to
                                             						  extensions on the previously existing phone system. |
| Field | Setting |
| From Phone System | Select the display name
                                             						  of the phone system that you are creating a trunk for. |
| To Phone System | Select the display name
                                             						  of the previously existing phone system that the trunk will connect to. |
| Trunk Access Code | Enter the extra digits
                                             						  that Unity Connection must dial to transfer calls through the gateway to
                                             						  extensions on the previously existing phone system. |
| Step 19 | Repeat Step 17 and Step 18 for all
                              			 remaining phone system trunks that you want to create. |
| Step 20 | In the Related Links drop-down list, select Check Telephony
                                 				Configuration and select Go to confirm
                              			 the phone system integration settings. If the test is not successful, the Task Execution Results
                                 				displays one or more messages with troubleshooting steps. After correcting the
                                 				problems, test the Unity Connection again. |
| Step 21 | In the Task Execution Results window, select Close . |

| Field | Setting |
|---|---|
| Phone System | Select the name of the phone system that you entered in Step 3 . |
| Create From | Select Port Group Template and
                                             						  select SIP in the drop-down
                                             						  box. |
| Display Name | Enter a descriptive name for the port group. You can accept the
                                             						  default name or enter the name that you want. |
| Authenticate with SIP Server | Uncheck this check box. |
| Authentication User Name | Leave this field blank. |
| Authentication Password | Leave this field blank. |
| Contact Line Name | Enter the voice messaging pilot number that matches the dial
                                             						  plan configuration of the gateway. |
| SIP Security Profile | Select 5060 . |
| SIP Transport Protocol | Select the SIP transport protocol that Cisco Unity Connection
                                             						  will use. |
| IPv4 Address or Host Name | Enter the IP address (or host name) of the primary gateway that
                                             						  you are connecting to Unity Connection. |
| IPv6 Address or Host Name | Do not enter a value in this field. IPv6 is not supported for
                                             						  EGW 2200 integrations. |
| IP Address or Host Name | Enter the IP address (or host name) of the primary gateway that
                                             						  you are connecting to Unity Connection. |
| Port | Enter the IP port of the primary gateway that you are connecting
                                             						  to Unity Connection. We recommend that you use the default setting. Caution This setting must match the port setting of the gateway.
                                                      						  Otherwise the integration will not function correctly. | Caution | This setting must match the port setting of the gateway.
                                                      						  Otherwise the integration will not function correctly. |
| Caution | This setting must match the port setting of the gateway.
                                                      						  Otherwise the integration will not function correctly. |

| Caution | This setting must match the port setting of the gateway.
                                                      						  Otherwise the integration will not function correctly. |
|---|---|

| Field | Setting |
|---|---|
| Order | Enter the order of
                                                   								priority for the gateway. The lowest number is the primary gateway, the higher
                                                   								numbers are the secondary gateways. |
| IPv4 Address or Host Name | Enter the IP address (or
                                                   								host name) of the secondary gateway. |
| IPv6 Address or Host Name | Do not enter a value in
                                                   								this field. IPv6 is not supported for EGW 2200 integrations. |
| IP Address or Host Name | Enter the IP address (or
                                                   								host name) of the secondary gateway. |
| Port | Enter the IP port of the
                                                   								secondary gateway that you are connecting to Unity Connection. We recommend
                                                   								that you use the default setting. |

| Field | Considerations |
|---|---|
| Enabled | Check this check box. |
| Number of Ports | Enter the number of voice
                                             						  messaging ports that you want to create in this port group. Note For a Unity Connection cluster, you must enter the total number
                                                      						  of voice messaging ports that will be used by all Unity Connection servers.
                                                      						  Each port will later be assigned to a specific Unity Connection server. | Note | For a Unity Connection cluster, you must enter the total number
                                                      						  of voice messaging ports that will be used by all Unity Connection servers.
                                                      						  Each port will later be assigned to a specific Unity Connection server. |
| Note | For a Unity Connection cluster, you must enter the total number
                                                      						  of voice messaging ports that will be used by all Unity Connection servers.
                                                      						  Each port will later be assigned to a specific Unity Connection server. |
| Phone System | Select the name of the
                                             						  phone system that you entered in Step 3 . |
| Port Group | Select the name of the
                                             						  port group that you added in Step 7 . |
| Server | Select the name of the
                                             						  Unity Connection server. |

| Note | For a Unity Connection cluster, you must enter the total number
                                                      						  of voice messaging ports that will be used by all Unity Connection servers.
                                                      						  Each port will later be assigned to a specific Unity Connection server. |
|---|---|

| Note | By default, the display names for the voice messaging ports are
                                             				  composed of the port group display name followed by incrementing numbers. |
|---|---|

| Field | Considerations |
|---|---|
| Enabled | Check this check box to
                                             						  enable the port. The port is enabled during normal operation. Uncheck this check box to
                                             						  disable the port. When the port is disabled, calls to the port get a ringing
                                             						  tone but are not answered. Typically, the port is disabled only by the
                                             						  installer during testing. |
| Server | (For Unity Connection
                                                							 clusters only) Select the name of the Unity Connection server that you want
                                             						  to handle this port. Assign an equal number of
                                             						  answering and dial-out voice messaging ports to the Unity Connection servers so
                                             						  that they equally share the voice messaging traffic. |
| Answer Calls | Check this check box to
                                             						  designate the port for answering calls. These calls can be incoming calls from
                                             						  unidentified callers or from users. |
| Perform Message
                                             						  Notification | Check this check box to
                                             						  designate the port for notifying users of messages. Assign Perform Message
                                             						  Notification to the least busy ports. |
| Send MWI Requests | Check this check box to
                                             						  designate the port for turning MWIs on and off. Assign Send MWI Requests to the
                                             						  least busy ports. |
| Allow TRAP Connections | Check this check box so
                                             						  that users can use the port for recording and playback through the phone in
                                             						  Unity Connection web applications. Assign Allow TRAP Connections to the least
                                             						  busy ports. |

| Field | Setting |
|---|---|
| From Phone System | Select the display name
                                             						  of the phone system that you are creating a trunk for. |
| To Phone System | Select the display name
                                             						  of the previously existing phone system that the trunk will connect to. |
| Trunk Access Code | Enter the extra digits
                                             						  that Unity Connection must dial to transfer calls through the gateway to
                                             						  extensions on the previously existing phone system. |

| Step 1 | Set up two test extensions (Phone 1 and Phone 2) on the same
                                 			 phone system that Unity Connection is connected to. |
|---|---|
| Step 2 | Set Phone 1 to forward calls to the Unity Connection pilot
                                 			 number when calls are not answered. Caution The phone system must forward calls to the Unity Connection
                                             				pilot number in no fewer than four rings. Otherwise, the test may fail. | Caution | The phone system must forward calls to the Unity Connection
                                             				pilot number in no fewer than four rings. Otherwise, the test may fail. |
| Caution | The phone system must forward calls to the Unity Connection
                                             				pilot number in no fewer than four rings. Otherwise, the test may fail. |
| Step 3 | In Cisco Unity Connection Administration, expand Users , then select Users . |
| Step 4 | On the Search Users page, select the display name of a user to
                                 			 use for testing. The extension for this user must be the extension for Phone 1. |
| Step 5 | On the Edit User Basics page, uncheck the Set for Self-enrollment at Next Login check box. |
| Step 6 | In the Voice Name field, record a recorded name for the test
                                 			 user. |
| Step 7 | Select Save . |
| Step 8 | On the Edit menu, select Message Waiting Indicators . |
| Step 9 | On the Message Waiting Indicators page, select the message
                                 			 waiting indicator. If no message waiting indication is in the table, select Add New . |
| Step 10 | On the Edit Message Waiting Indicator page, enter the following
                                 			 settings. Table 7. Settings for the Edit MWI Page Field Setting Enabled Check this check box to enable MWIs for the test user. Display Name Accept the default or enter a different name. Inherit User’s Extension Check this check box to enable MWIs on Phone 1. | Field | Setting | Enabled | Check this check box to enable MWIs for the test user. | Display Name | Accept the default or enter a different name. | Inherit User’s Extension | Check this check box to enable MWIs on Phone 1. |
| Field | Setting |
| Enabled | Check this check box to enable MWIs for the test user. |
| Display Name | Accept the default or enter a different name. |
| Inherit User’s Extension | Check this check box to enable MWIs on Phone 1. |
| Step 11 | Select Save . |
| Step 12 | On the Edit menu, select Transfer Rules . |
| Step 13 | On the Transfer Rules page, select the active rule. |
| Step 14 | On the Edit Transfer Rule page, under Transfer Action, select Extension and enter the extension of Phone 1. |
| Step 15 | In the Transfer Type field, select Release to Switch . |
| Step 16 | Select Save . |
| Step 17 | Minimize the Cisco Unity Connection Administration window. Do not close
                                    				the Cisco Unity Connection Administration window because you will use it again
                                    				in a later procedure. |
| Step 18 | Sign in to the
                                 			 Real-Time Monitoring Tool (RTMT). |
| Step 19 | On the Unity
                                 			 Connection menu, select Port Monitor . The Port Monitor tool appears in the
                                 			 right pane. |
| Step 20 | In the right
                                 			 pane, select Start Polling . The Port Monitor will display which
                                 			 port is handling the calls that you will make. |

| Caution | The phone system must forward calls to the Unity Connection
                                             				pilot number in no fewer than four rings. Otherwise, the test may fail. |
|---|---|

| Field | Setting |
|---|---|
| Enabled | Check this check box to enable MWIs for the test user. |
| Display Name | Accept the default or enter a different name. |
| Inherit User’s Extension | Check this check box to enable MWIs on Phone 1. |

| Step 1 | From Phone 2, enter the access code necessary to get an outside
                                 			 line, then enter the number outside callers use to dial directly to Unity
                                 			 Connection. |
|---|---|
| Step 2 | In the Port Monitor, note which port handles this call. |
| Step 3 | When you hear the opening greeting, enter the extension for
                                 			 Phone 1. Hearing the opening greeting means that the port is configured
                                 			 correctly. |
| Step 4 | Confirm that Phone 1 rings and that you hear a ringback tone on
                                 			 Phone 2. Hearing a ringback tone means that Unity Connection correctly released
                                 			 the call and transferred it to Phone 1. |
| Step 5 | Leaving Phone 1 unanswered, confirm that the state of the port
                                 			 handling the call changes to “Idle.” This state means that release transfer is
                                 			 successful. |
| Step 6 | Confirm that, after the number of rings that the phone system is
                                 			 set to wait, the call is forwarded to Unity Connection and that you hear the
                                 			 greeting for the test user. Hearing the greeting means that the phone system
                                 			 forwarded the unanswered call and the call-forward information to Unity
                                 			 Connection, which correctly interpreted the information. |
| Step 7 | On the Port Monitor, note which port handles this call. |
| Step 8 | Leave a message for the test user and hang up Phone 2. |
| Step 9 | In the Port Monitor, confirm that the state of the port handling
                                 			 the call changes to “Idle.” This state means that the port was successfully
                                 			 released when the call ended. |
| Step 10 | Confirm that the MWI on Phone 1 is activated. The activated MWI
                                 			 means that the phone system and Unity Connection are successfully integrated
                                 			 for turning on MWIs. |

| Step 1 | From Phone 1, enter the internal pilot number for Unity
                                 			 Connection. |
|---|---|
| Step 2 | When asked for your password, enter the password for the test
                                 			 user. Hearing the request for your password means that the phone system sent
                                 			 the necessary call information to Unity Connection, which correctly interpreted
                                 			 the information. |
| Step 3 | Confirm that you hear the recorded name for the test user (if
                                 			 you did not record a name for the test user, you will hear the extension number
                                 			 for Phone 1). Hearing the recorded name means that Unity Connection correctly
                                 			 identified the user by the extension. |
| Step 4 | Listen to the message. |
| Step 5 | After listening to the message, delete the message. |
| Step 6 | Confirm that the MWI on Phone 1 is deactivated. The deactivated
                                 			 MWI means that the phone system and Unity Connection are successfully
                                 			 integrated for turning off MWIs. |
| Step 7 | Hang up Phone 1. |
| Step 8 | On the Port Monitor, confirm that the state of the port handling
                                 			 the call changes to “Idle.” This state means that the port was successfully
                                 			 released when the call ended. |

| Step 1 | In Cisco Unity Connection Administration, on the Edit Transfer
                                 			 Rule page for the test user, in the Transfer Type field, select Supervise Transfer . |
|---|---|
| Step 2 | In the Rings to Wait For field, enter 3 . |
| Step 3 | Select Save . |
| Step 4 | Minimize the Cisco Unity Connection Administration window. Do not close
                                 			 the Cisco Unity Connection Administration window because you will use it again
                                 			 in a later procedure. |

| Step 1 | From Phone 2, enter the access code necessary to get an outside
                                 			 line, then enter the number outside callers use to dial directly to Unity
                                 			 Connection. |
|---|---|
| Step 2 | On the Port Monitor, note which port handles this call. |
| Step 3 | When you hear the opening greeting, enter the extension for
                                 			 Phone 1. Hearing the opening greeting means that the port is configured
                                 			 correctly. |
| Step 4 | Confirm that Phone 1 rings and that you do not hear a ringback
                                 			 tone on Phone 2. Instead, you should hear the indication your phone system uses
                                 			 to mean that the call is on hold (for example, music). |
| Step 5 | Leaving Phone 1 unanswered, confirm that the state of the port
                                 			 handling the call remains “Busy.” This state and hearing an indication that you
                                 			 are on hold mean that Unity Connection is supervising the transfer. |
| Step 6 | Confirm that, after three rings, you hear the greeting for the
                                 			 test user. Hearing the greeting means that Unity Connection successfully
                                 			 recalled the supervised-transfer call. |
| Step 7 | During the greeting, hang up Phone 2. |
| Step 8 | On the Port Monitor, confirm that the state of the port handling
                                 			 the call changes to “Idle.” This state means that the port was successfully
                                 			 released when the call ended. |
| Step 9 | Select Stop Polling . |
| Step 10 | Sign out of RTMT. |