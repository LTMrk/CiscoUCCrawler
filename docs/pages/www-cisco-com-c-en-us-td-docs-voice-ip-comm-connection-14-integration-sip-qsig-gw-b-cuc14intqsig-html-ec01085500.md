---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-connection-14-integration-sip-qsig-gw-b-cuc14intqsig-html-ec01085500
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/14/integration/sip-qsig_gw/b_cuc14intqsig.html
retrieved_at: 2026-08-17T02:14:48.804799+00:00
---

QSIG-Enabled Phone System with Cisco ISR Voice Gateway Integration Guide for Cisco Unity Connection Release 14

# QSIG-Enabled Phone System with Cisco ISR Voice Gateway Integration Guide for Cisco Unity Connection Release 14

### Download Options

Updated: March 25, 2021

# QSIG-Enabled Phone System with Cisco ISR Voice Gateway Integration Guide for Cisco Unity Connection Release 15

This document
               		provides instructions for integrating a QSIG-enabled phone system with Cisco
               		Unity Connection through a Cisco ISR voice gateway.

## Integration
               	 Tasks

Confirm that Unity Connection is installed as per the steps mentioned in the “ Installing Cisco Unity Connection ” chapter of the Install, Upgrade, and Maintenance Guide for Cisco Unity Connection Release 15, available at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/15/install_upgrade/guide/b_15cuciumg.html .

After completing the installation of Unity Connection, follow
                  		the tasks in the “ Task
                     		  List to Create the Integration section ” to complete the integration of
                  		Unity Connection with a QSIG-enabled phone system through a Cisco ISR voice
                  		gateway.

### Task List to
                  	 Create the Integration

Do the following steps in the given task list to integrate Unity
                     		Connection with a QSIG-enabled phone system through a Cisco ISR voice gateway.

Review the system and equipment requirements to confirm that all
                           			 phone system and Unity Connection requirements have been met. See the “Prerequisites”
                              				section .

Plan how the voice messaging ports are used by Unity Connection.
                           			 See the “Planning
                              				the Usage of Voice Messaging Ports” section .

Program the QSIG-enabled phone system. See the “Programming
                              				the QSIG-Enabled Phone Systems” section .

Configure the Cisco ISR voice gateway. See the “Configuring
                              				the Cisco ISR Voice Gateway” section .

Create the integration. See the “Creating
                              				a New Integration with QSIG-enabled Phone System” section .

Test the integration. See the “Testing
                              				the Integration” section .

If this integration is a second or subsequent integration, add
                           			 the applicable new user templates for the new phone system. See the “Adding
                              				New User Templates for Multiple Integrations” section .

While integrating the Cisco Unity Connection with Cisco Unified
                                    			 Call Manager through a QSIG- Enabled Phone system with Cisco ISR Voice gateway
                                    			 uncheck the Synchronize guest time to host option for Unified Communications
                                    			 product line in Virtualized environment. This enables the Unified
                                    			 Communications to synchronize with their clock to external NTP servers.

## Prerequisites

The QSIG-enabled integration supports configurations of the
                  		following components:

### Phone
                  	 System

A QSIG-enabled phone system.

The phone system is ready for the integration.

### Cisco ISR Voice
                  	 Gateway

Cisco IOS version 12.4(11)T or later.

The QSIG-enabled phone system connected to the
                           			 Cisco ISR voice gateway.

### Unity Connection
                  	 Server

Unity Connection installed and ready for the integration, as described in the “ Installing Cisco Unity Connection ” chapter of the Install, Upgrade, and Maintenance Guide for Cisco Unity Connection Release 15, available at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/15/install_upgrade/guide/b_15cuciumg.html .

A license that enables the applicable number of voice messaging
                           			 ports.

### Centralized Voice
                  	 Messaging

Unity Connection supports centralized voice messaging through the phone system, which supports various inter-phone system
                     networking protocols including proprietary protocols such as Avaya DCS, Nortel MCDN, or Siemens CorNet, and standards-based
                     protocols such as QSIG or DPNSS. Note that centralized voice messaging is a function of the phone system and its inter-phone
                     system networking, not voice mail. Unity Connection supports centralized voice messaging as long as the phone system and its
                     inter-phone system networking are properly configured. For details, see the “ Centralized Voice Messaging ” section in the “Integrating Cisco Unity Connection with the Phone System” chapter of the Design Guide for Cisco Unity Connection, Release 15 at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/15/design/guide/b_15cucdg.html .

## Integration
               	 Description

This integration uses a Cisco ISR voice gateway and a LAN or WAN
                  		to connect Unity Connection and a QSIG-enabled phone system. The Cisco ISR
                  		voice gateway converts the QSIG communications to SIP. Figure 1 shows the required connections.

### Call Information

The QSIG-enabled phone system integration sends the following information with forwarded calls:

The extension of the called party

The extension of the calling party (for internal calls) or the phone number of the calling party (if it is an external call
                           and the system uses caller ID)

The reason for the forward (the extension is busy, does not answer, or is set to forward all calls)

Unity Connection uses this information to answer the call appropriately. For example, a call forwarded to Unity Connection
                     is answered with the personal greeting of the user. If the phone system routes the call to Unity Connection without this information,
                     Unity Connection answers with the opening greeting.

### Integration Functionality

The QSIG-enabled phone system integration with Unity Connection provides the following features:

Call forward to personal greeting

Call forward to busy greeting

Caller ID

Easy message access (a user can retrieve messages without entering an ID; Unity Connection identifies a user based on the
                           extension from which the call originated; a password may be required)

Identified user messaging (Unity Connection identifies the user who leaves a message during a forwarded internal call, based
                           on the extension from which the call originated)

Message waiting indication (MWI)

### Integrations with
                  	 Multiple Phone Systems

When Unity Connection is installed as Cisco Business Edition—on
                     		the same server with Cisco Unified Communications Manager—Unity Connection
                     		cannot be integrated with multiple phone systems at one time.

When Unity Connection is not installed as Cisco Business Edition, Unity Connection can be integrated with multiple phone systems
                     at one time. For information on and instructions for integrating Unity Connection with multiple phone systems, see the Multiple Phone System Integration Guide for Cisco Unity Connection, Release 15 at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/15/integration/multiple/b_cuc15intmultiple.html .

In
                              		Unity Connection integration with multiple phone systems is not supported for
                              		use with Cisco Business Edition 5000 and is supported only with Cisco Business
                              		Edition 6000/7000.

## Planning the Usage of Voice Messaging Ports

Before programming the phone system, you need to
                  		plan how the voice messaging ports are used by Unity Connection. The following
                  		considerations affect the programming for the phone system (for example,
                  		setting up the hunt group or call forwarding for the voice messaging ports):

The number of voice messaging ports installed.

For a Unity Connection cluster, each server must
                  		have enough ports to handle all voice messaging traffic in case the other
                  		server stops functioning.

The number of voice messaging ports that
                        			 answer calls.

The number of voice messaging ports that only
                        			 dial out, for example, to send message notification, to set message waiting
                        			 indicators (MWIs), and to make telephone record and playback (TRAP)
                        			 connections.

Release (blind) transfers that are forwarded back
                                    				to Unity Connection uses three b-channels for the remainder of the call.
                                    				However, supervised transfers pull back the consulting call when the target is
                                    				unavailable so that only one b-channel is used for the remainder of the call.

The following table describes the voice messaging
                  		port settings in Unity Connection that can be set on Telephony
                  		Integrations > Port of Cisco Unity Connection Administration.

Field

Considerations

Enabled

Check this check box to enable the port.
                              				  The port is enabled during normal operation.

Uncheck this check box to disable the
                              				  port. When the port is disabled, calls to the port get a ringing tone but are
                              				  not answered. Typically, the port is disabled only by the installer during
                              				  testing.

Server

(When a Unity
                                 					 Connection cluster is configured) Select the name of the Unity Connection
                              				  server that you want to handle this port.

Assign an equal number of answering and
                              				  dial-out voice messaging ports to the Unity Connection servers so that they
                              				  equally share the voice messaging traffic.

Answer Calls

Check this check box to designate the port
                              				  for answering calls. These calls can be incoming calls from unidentified
                              				  callers or from users.

All voice messaging ports connecting to
                              				  the Cisco ISR voice gateway must have the Answer Calls check box checked.
                              				  Otherwise, calls to Unity Connection may not be answered.

Perform Message Notification

Check this check box to designate the port
                              				  for notifying users of messages. Assign Perform Message Notification to the
                              				  least busy ports.

Send MWI Requests

Check this check box to designate the port
                              				  for turning MWIs on and off. Assign Send MWI Requests to the least busy ports.

Allow TRAP Connections

Check this check box so that users can use
                              				  the port for recording and playback through the phone in Unity Connection web
                              				  applications. Assign Allow TRAP Connections to the least busy ports.

## Determining the
               	 Number of Voice Messaging Ports

The following tasks describe the process for determining the
                  		number of voice messaging ports for Cisco Unity Connection to install, answer
                  		call and dial out calls:

For determining the number of voice messaging ports to Install,
                        			 see “Voice
                           				Messaging Ports to Install” section .

For determining the number of voice messaging ports to Answer
                        			 Calls, see “Voice
                           				Messaging Ports to Answer Calls” section .

For determining the number of voice messaging ports to Dial Out,
                        			 see “Voice
                           				Messaging Ports to Dial Out” section .

### Voice Messaging
                  	 Ports to Install

The number of voice messaging ports to install depends on
                     		numerous factors, including:

The number of calls Unity Connection answer when call traffic is
                           			 at its peak.

The expected length of each message that callers record and that
                           			 users listen to.

The number of users.

The number of calls made for message notification.

The number of MWIs that are activated when call traffic is at
                           			 its peak.

The number of TRAP connections needed when call traffic is at
                           			 its peak. (TRAP connections are used by Unity Connection web applications to
                           			 play back and record over the phone.)

The number of calls that use the automated attendant and call
                           			 handlers when call traffic is at its peak.

Whether a Unity Connection cluster is configured. For
                           			 considerations, see the “Considerations
                              				for a Unity Connection Cluster” section .

It is best to install only the number of voice messaging ports
                     		that are needed so that system resources are not allocated to unused ports.

### Voice Messaging
                  	 Ports to Answer Calls

The calls that the voice messaging ports answer can be incoming
                     		calls from unidentified callers or from users. Assign all of the voice
                     		messaging ports to answer calls.

You can set voice messaging ports to both answer calls and to
                     		dial out (for example, to send message notifications).

The
                              		Cisco ISR voice gateway performs transfers by hairpinning two independent calls
                              		across two b-channels on the QSIG trunk. Hairpinned calls use more QSIG
                              		channels in comparison to the number of Unity Connection voice messaging ports
                              		that are available to answer calls. If your system uses Unity Connection
                              		auto-attendant transfers, you must provision a larger number of QSIG b-channels
                              		than the number of Unity Connection voice messaging ports that answer calls.

If your system is configured for a Unity Connection cluster, see
                     		the “Considerations
                        		  for a Unity Connection Cluster” section .

### Voice Messaging
                  	 Ports to Dial Out

Ports that only dial out can do one or more of the following:

Notify users by phone, pager, or e-mail of messages that have
                           			 arrived.

Turn MWIs on and off for user extensions.

Make a TRAP Unity Connection so that users can use the phone as
                           			 a recording and playback device in Unity Connection web applications.

If your system is configured for a Unity Connection cluster, see
                     		the “Considerations
                        		  for a Unity Connection Cluster” section .

### Considerations for a Unity Connection Cluster

If your system is configured for a Unity Connection cluster, consider how the voice messaging ports are used in different
                     scenarios.

#### When Both Unity Connection Servers are Functioning Normally

A hunt group is configured on the phone system to distribute calls equally to both Unity Connection servers.

The network is configured to send incoming calls first to the subscriber server, then to the publisher server if no answering
                              ports are available on the subscriber server.

Both Unity Connection servers are active and handle voice messaging traffic for the system.

In Cisco Unity Connection Administration, the voice messaging ports are configured so that an equal number of voice messaging
                              ports are assigned to each Unity Connection server. This guide directs you to assign the voice messaging ports to their specific
                              server at the applicable time.

The number of voice messaging ports that are assigned to one Unity Connection server must be sufficient to handle all of the
                              voice messaging traffic for the system (answering calls and dialing out) when the other Unity Connection server stops functioning.

If both Unity Connection servers must be functioning to handle the voice messaging traffic, the system do not have sufficient
                        capacity when one of the servers stops functioning.

Each Unity Connection server is assigned half the total number of voice messaging ports.

If all the voice messaging ports are assigned to one Unity Connection server, the other Unity Connection server do not be
                        able to answer calls or to dial out.

Each Unity Connection server must have voice messaging ports that answer calls and that can dial out (for example, to set
                              MWIs).

#### When Only One Unity Connection Server is Functioning

The hunt group on the phone system sends all calls to the functioning Unity Connection server.

The functioning Unity Connection server receives all voice messaging traffic for the system.

The number of voice messaging ports that are assigned to the functioning Unity Connection server must be sufficient to handle
                              all of the voice messaging traffic for the system (answering calls and dialing out).

The functioning Unity Connection server must have voice messaging ports that answer calls and that can dial out (for example,
                              to set MWIs).

If the functioning Unity Connection server does not have voice messaging ports for answering calls, the system is not able
                        to answer incoming calls. Similarly, if the functioning Unity Connection server does not have voice messaging ports for dialing
                        out, the system is not able to dial out (for example, to set MWIs).

## Programming the
               	 QSIG-Enabled Phone Systems

Note that you must program each extension to forward calls to
                     		  the pilot number assigned to the voice messaging ports, based on one of the
                     		  call transfer types shown in Table 2 .

Transfer Types

Usage

Release transfer (blind transfer)

Program the phone to forward calls to the pilot number when:

The extension is busy

The call is not answered

Supervised transfer

Program the phone to forward calls to the pilot number only when
                                 					 the call is not answered (on the phone system, the number of rings before
                                 					 forwarding must be more than the number of rings to supervise the call).
                                 					 Confirm that call forwarding is disabled when the extension is busy.

## Configuring the Cisco ISR Voice Gateway

For a Unity Connection cluster, identify the Unity Connection servers
                              		  with a fully qualified domain name (FQDN), and configure a DNS server to
                              		  resolve the FQDN to the IP addresses and SIP ports of the Unity Connection
                              		  server.

### Creating an
                  	 Integration

### SUMMARY STEPS

- In Cisco Unity Connection Administration, expand Telephony Integrations > and select Phone System .

- On the Search Phone Systems page, under Display Name, select the
                        			 name of the default phone system.

- On the Phone System Basics page, in the Phone System Name field,
                        			 enter the descriptive name that you want for the phone system.

- If you want to use this phone system as the default for TRaP
                        			 connections so that administrators and users without voicemail boxes can record
                        			 and playback through the phone in Unity Connection web applications, check the Default TRAP Switch check box. If you want to use
                        			 another phone system as the default for TRaP connections, uncheck this check
                        			 box.

- Select Save .

- On the Phone System Basics page, in the Related Links drop-down
                        			 box, select Add Port Group and select Go .

- On the New Port Group page, enter the applicable settings and
                        			 select Save .

- On the Port Group Basics page, in the Related Links drop-down
                        			 box, select Add Ports and select Go .

- On the New Port page, enter the following settings and select Save .

- On the Search Ports page, select the display name of the first
                        			 voice messaging port that you created for this phone system integration.

- On the Port Basics page, enter the following settings. The
                        			 fields in the following table are the ones that you can change.

- Select Save .

- Select Next .

- Repeat Step 11 through Step
                           				13 for all remaining voice messaging ports for the phone system.

- If another phone system integration exists, in Cisco Unity
                        			 Connection Administration, expand Telephony
                           				Integrations , then select Trunk .
                        			 Otherwise, skip to Step 19 .

- On the Search Phone System Trunks page, on the Phone System
                        			 Trunk menu, select New Phone System
                           				Trunk .

- On the New Phone System Trunk page, enter the following settings
                        			 for the phone system trunk and select Save .

- Repeat Step
                           				16 and Step 17 for all remaining phone system trunks that you want to create.

- In the Related Links drop-down list, select Check Telephony
                           				Configuration and select Go to confirm
                        			 the phone system integration settings.

- In the Task Execution Results window, select Close .

### DETAILED STEPS

Step 1

In Cisco Unity Connection Administration, expand Telephony Integrations > and select Phone System .

Step 2

On the Search Phone Systems page, under Display Name, select the
                                 			 name of the default phone system.

Step 3

On the Phone System Basics page, in the Phone System Name field,
                                 			 enter the descriptive name that you want for the phone system.

Step 4

If you want to use this phone system as the default for TRaP
                                 			 connections so that administrators and users without voicemail boxes can record
                                 			 and playback through the phone in Unity Connection web applications, check the Default TRAP Switch check box. If you want to use
                                 			 another phone system as the default for TRaP connections, uncheck this check
                                 			 box.

Step 5

Select Save .

Step 6

On the Phone System Basics page, in the Related Links drop-down
                                 			 box, select Add Port Group and select Go .

Step 7

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

Confirm that this check box is unchecked.

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

Select the SIP transport protocol that Unity Connection uses.

IPv4 Address or Host Name

Enter the IP address (or host name) of the primary gateway that
                                                						  you are connecting to Unity Connection.

IPv6 Address or Host Name

Do not enter a value in this field. IPv6 is not supported for
                                                						  this type of integration.

IP Address or Host Name

Enter the IP address (or host name) of the primary gateway that
                                                						  you are connecting to Unity Connection.

Port

Enter the IP port of the primary gateway that you are connecting
                                                						  to Unity Connection. We recommend that you use the default setting.

This setting must match the port setting of the gateway.
                                                						  Otherwise the integration does not function correctly.

Step 8

On the Port Group Basics page, in the Related Links drop-down
                                 			 box, select Add Ports and select Go .

Step 9

On the New Port page, enter the following settings and select Save .

Field

Considerations

Enabled

Check this check box.

Number of Ports

Enter the number of voice
                                                						  messaging ports that you want to create in this port group.

For a Unity Connection cluster, you must enter the total number
                                                         						  of voice messaging ports that are used by all Unity Connection servers. Each
                                                         						  port is later assigned to a specific Unity Connection server.

Phone System

Select the name of the
                                                						  phone system that you entered in Step 3 .

Port Group

Select the name of the
                                                						  port group that you added in Step
                                                   							 7 .

Server

Select the name of the
                                                						  Unity Connection server.

Step 10

On the Search Ports page, select the display name of the first
                                 			 voice messaging port that you created for this phone system integration.

By default, the display names for the voice messaging ports are
                                             				composed of the port group display name followed by incrementing numbers.

Step 11

On the Port Basics page, enter the following settings. The
                                 			 fields in the following table are the ones that you can change.

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

Step 12

Select Save .

Step 13

Select Next .

Step 14

Repeat Step 11 through Step
                                    				13 for all remaining voice messaging ports for the phone system.

Step 15

If another phone system integration exists, in Cisco Unity
                                 			 Connection Administration, expand Telephony
                                    				Integrations , then select Trunk .
                                 			 Otherwise, skip to Step 19 .

Step 16

On the Search Phone System Trunks page, on the Phone System
                                 			 Trunk menu, select New Phone System
                                    				Trunk .

Step 17

On the New Phone System Trunk page, enter the following settings
                                 			 for the phone system trunk and select Save .

Field

Setting

From Phone System

Select the display name
                                                						  of the phone system that you are creating a trunk for.

To Phone System

Select the display name
                                                						  of the previously existing phone system that the trunk connects to.

Trunk Access Code

Enter the extra digits
                                                						  that Unity Connection must dial to transfer calls through the gateway to
                                                						  extensions on the previously existing phone system.

Step 18

Repeat Step
                                    				16 and Step 17 for all remaining phone system trunks that you want to create.

Step 19

In the Related Links drop-down list, select Check Telephony
                                    				Configuration and select Go to confirm
                                 			 the phone system integration settings.

If the test is not successful, the Task Execution Results
                                    				displays one or more messages with troubleshooting steps. After correcting the
                                    				problems, test the Unity Connection again.

Step 20

In the Task Execution Results window, select Close .

## Testing the
               	 Integration

To test whether Unity Connection and the phone system are
                  		integrated correctly, do the following procedures in the order listed.

If any of the steps indicate a failure, see the following
                  		documentation as applicable:

The installation guide for the phone system.

Troubleshooting Guide for Cisco Unity Connection Release 15 , available at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/15/troubleshooting/guide/b_15cuctsg.html .

The setup information earlier in this guide.

### Setting Up the Test Configuration

### SUMMARY STEPS

- Set up two test extensions (Phone 1 and
                        			 Phone 2) on the same phone system that Unity Connection is connected to.

- Set Phone 1 to forward calls to the Unity
                        			 Connection pilot number when calls are not answered.

- In Cisco Unity Connection Administration,
                        			 expand Users > and select Users .

- On the Search Users page, select the display
                        			 name of a user to use for testing. The extension for this user must be the
                        			 extension for Phone 1.

- On the Edit User Basics page, uncheck the Set for Self-enrollment at Next
                           				Login check box.

- In the Voice Name field, record a voice name
                        			 for the test user and select Save .

- On the Edit menu, select Message Waiting
                           				Indicators .

- On the Message Waiting Indicators page,
                        			 select the message waiting indicator. If no message waiting indication is in
                        			 the table, select Add New .

- On the Edit Message Waiting Indicator page,
                        			 enter the following settings.

- Select Save .

- On the Edit menu, select Transfer Rules .

- On the Transfer Rules page, select the
                        			 active option.

- On the Edit Transfer Rule page, under
                        			 Transfer Action, select the Extension option and
                        			 enter the extension of Phone 1.

- In the Transfer Type field, select Release to Switch .

- Select Save .

- Minimize the Cisco Unity Connection
                        			 Administration window. Do not close the Cisco Unity Connection Administration
                        			 window because you use it again in a later procedure.

- Sign in to the Real-Time Monitoring Tool
                        			 (RTMT).

- On the Unity Connection menu, select Port Monitor . The Port
                        			 Monitor tool appears in the right pane.

- In the right pane, select Start Polling . The Port
                        			 Monitor displays which port is handling the calls that you make.

### DETAILED STEPS

Step 1

Set up two test extensions (Phone 1 and
                                 			 Phone 2) on the same phone system that Unity Connection is connected to.

Step 2

Set Phone 1 to forward calls to the Unity
                                 			 Connection pilot number when calls are not answered.

Caution

The phone system must forward calls to the Unity
                                             				Connection pilot number in no fewer than four rings. Otherwise, the test may
                                             				fail.

Step 3

In Cisco Unity Connection Administration,
                                 			 expand Users > and select Users .

Step 4

On the Search Users page, select the display
                                 			 name of a user to use for testing. The extension for this user must be the
                                 			 extension for Phone 1.

Step 5

On the Edit User Basics page, uncheck the Set for Self-enrollment at Next
                                    				Login check box.

Step 6

In the Voice Name field, record a voice name
                                 			 for the test user and select Save .

Step 7

On the Edit menu, select Message Waiting
                                    				Indicators .

Step 8

On the Message Waiting Indicators page,
                                 			 select the message waiting indicator. If no message waiting indication is in
                                 			 the table, select Add New .

Step 9

On the Edit Message Waiting Indicator page,
                                 			 enter the following settings.

Field

Setting

Enabled

Check this check box to enable MWIs
                                                						  for the test user.

Display Name

Accept the default or enter a
                                                						  different name.

Inherit User’s Extension

Check this check box to enable MWIs
                                                						  on Phone 1.

Step 10

Select Save .

Step 11

On the Edit menu, select Transfer Rules .

Step 12

On the Transfer Rules page, select the
                                 			 active option.

Step 13

On the Edit Transfer Rule page, under
                                 			 Transfer Action, select the Extension option and
                                 			 enter the extension of Phone 1.

Step 14

In the Transfer Type field, select Release to Switch .

Step 15

Select Save .

Step 16

Minimize the Cisco Unity Connection
                                 			 Administration window. Do not close the Cisco Unity Connection Administration
                                 			 window because you use it again in a later procedure.

Step 17

Sign in to the Real-Time Monitoring Tool
                                 			 (RTMT).

Step 18

On the Unity Connection menu, select Port Monitor . The Port
                                 			 Monitor tool appears in the right pane.

Step 19

In the right pane, select Start Polling . The Port
                                 			 Monitor displays which port is handling the calls that you make.

### Testing an External Call with Release Transfer

### SUMMARY STEPS

- From Phone 2, enter the access code necessary to get an outside line, then enter the number outside callers use to dial directly
                        to Unity Connection.

- In the Port Monitor, note which port handles this call.

- When you hear the opening greeting, enter the extension for Phone 1. Hearing the opening greeting means that the port is configured
                        correctly.

- Confirm that Phone 1 rings and that you hear a ringback tone on Phone 2. Hearing a ringback tone means that Unity Connection
                        correctly released the call and transferred it to Phone 1.

- Leaving Phone 1 unanswered, confirm that the state of the port handling the call changes to “Idle.” This state means that
                        release transfer is successful.

- Confirm that, after the number of rings that the phone system is set to wait, the call is forwarded to Cisco Unity Connection
                        and that you hear the greeting for the test user. Hearing the greeting means that the phone system forwarded the unanswered
                        call and the call-forward information to Unity Connection, which correctly interpreted the information.

- On the Port Monitor, note which port handles this call.

- Leave a message for the test user and hang up Phone 2.

- In the Port Monitor, confirm that the state of the port handling the call changes to “Idle.” This state means that the port
                        was successfully released when the call ended.

- Confirm that the MWI on Phone 1 is activated. The activated MWI means that the phone system and Unity Connection are successfully
                        integrated for turning on MWIs.

### DETAILED STEPS

Step 1

From Phone 2, enter the access code necessary to get an outside line, then enter the number outside callers use to dial directly
                                 to Unity Connection.

Step 2

In the Port Monitor, note which port handles this call.

Step 3

When you hear the opening greeting, enter the extension for Phone 1. Hearing the opening greeting means that the port is configured
                                 correctly.

Step 4

Confirm that Phone 1 rings and that you hear a ringback tone on Phone 2. Hearing a ringback tone means that Unity Connection
                                 correctly released the call and transferred it to Phone 1.

Step 5

Leaving Phone 1 unanswered, confirm that the state of the port handling the call changes to “Idle.” This state means that
                                 release transfer is successful.

Step 6

Confirm that, after the number of rings that the phone system is set to wait, the call is forwarded to Cisco Unity Connection
                                 and that you hear the greeting for the test user. Hearing the greeting means that the phone system forwarded the unanswered
                                 call and the call-forward information to Unity Connection, which correctly interpreted the information.

Step 7

On the Port Monitor, note which port handles this call.

Step 8

Leave a message for the test user and hang up Phone 2.

Step 9

In the Port Monitor, confirm that the state of the port handling the call changes to “Idle.” This state means that the port
                                 was successfully released when the call ended.

Step 10

Confirm that the MWI on Phone 1 is activated. The activated MWI means that the phone system and Unity Connection are successfully
                                 integrated for turning on MWIs.

### Testing the Listening to Messages

### SUMMARY STEPS

- From Phone 1, enter the internal pilot number for Unity Connection.

- When asked for your password, enter the password for the test user. Hearing the request for your password means that the phone
                        system sent the necessary call information to Unity Connection, which correctly interpreted the information.

- Confirm that you hear the recorded voice name for the test user (if you did not record a voice name for the test user, you
                        hear the extension number for Phone 1). Hearing the voice name means that Unity Connection correctly identified the user by
                        the extension.

- Listen to the message.

- After listening to the message, delete the message.

- Confirm that the MWI on Phone 1 is deactivated. The deactivated MWI means that the phone system and Unity Connection are successfully
                        integrated for turning off MWIs.

- Hang up Phone 1.

- On the Port Monitor, confirm that the state of the port handling the call changes to “Idle.” This state means that the port
                        was successfully released when the call ended.

### DETAILED STEPS

Step 1

From Phone 1, enter the internal pilot number for Unity Connection.

Step 2

When asked for your password, enter the password for the test user. Hearing the request for your password means that the phone
                                 system sent the necessary call information to Unity Connection, which correctly interpreted the information.

Step 3

Confirm that you hear the recorded voice name for the test user (if you did not record a voice name for the test user, you
                                 hear the extension number for Phone 1). Hearing the voice name means that Unity Connection correctly identified the user by
                                 the extension.

Step 4

Listen to the message.

Step 5

After listening to the message, delete the message.

Step 6

Confirm that the MWI on Phone 1 is deactivated. The deactivated MWI means that the phone system and Unity Connection are successfully
                                 integrated for turning off MWIs.

Step 7

Hang up Phone 1.

Step 8

On the Port Monitor, confirm that the state of the port handling the call changes to “Idle.” This state means that the port
                                 was successfully released when the call ended.

### Setting Up Supervised Transfer on Cisco Unity Connection

### SUMMARY STEPS

- In Cisco Unity Connection Administration, on the Edit Transfer Rule page for the test user, in the Transfer Type field, select Supervise Transfer .

- In the Rings to Wait For field, enter 3 .

- Select Save .

- Minimize the Cisco Unity Connection Administration window. Do not close the Cisco Unity Connection Administration window because
                        you use it again in a later procedure.

### DETAILED STEPS

Step 1

In Cisco Unity Connection Administration, on the Edit Transfer Rule page for the test user, in the Transfer Type field, select Supervise Transfer .

Step 2

In the Rings to Wait For field, enter 3 .

Step 3

Select Save .

Step 4

Minimize the Cisco Unity Connection Administration window. Do not close the Cisco Unity Connection Administration window because
                                 you use it again in a later procedure.

### Testing Supervised Transfer

### SUMMARY STEPS

- From Phone 2, enter the access code necessary to get an outside line, then enter the number outside callers use to dial directly
                        to Unity Connection.

- On the Port Monitor, note which port handles this call.

- When you hear the opening greeting, enter the extension for Phone 1. Hearing the opening greeting means that the port is configured
                        correctly.

- Confirm that Phone 1 rings and that you do not hear a ringback tone on Phone 2. Instead, you should hear the indication your
                        phone system uses to mean that the call is on hold (for example, music).

- Leaving Phone 1 unanswered, confirm that the state of the port handling the call remains “Busy.” This state and hearing an
                        indication that you are on hold mean that Unity Connection is supervising the transfer.

- Confirm that, after three rings, you hear the greeting for the test user. Hearing the greeting means that Unity Connection
                        successfully recalled the supervised-transfer call.

- During the greeting, hang up Phone 2.

- On the Port Monitor, confirm that the state of the port handling the call changes to “Idle.” This state means that the port
                        was successfully released when the call ended.

- Select Stop Polling .

- Sign out of RTMT.

### DETAILED STEPS

Step 1

From Phone 2, enter the access code necessary to get an outside line, then enter the number outside callers use to dial directly
                                 to Unity Connection.

Step 2

On the Port Monitor, note which port handles this call.

Step 3

When you hear the opening greeting, enter the extension for Phone 1. Hearing the opening greeting means that the port is configured
                                 correctly.

Step 4

Confirm that Phone 1 rings and that you do not hear a ringback tone on Phone 2. Instead, you should hear the indication your
                                 phone system uses to mean that the call is on hold (for example, music).

Step 5

Leaving Phone 1 unanswered, confirm that the state of the port handling the call remains “Busy.” This state and hearing an
                                 indication that you are on hold mean that Unity Connection is supervising the transfer.

Step 6

Confirm that, after three rings, you hear the greeting for the test user. Hearing the greeting means that Unity Connection
                                 successfully recalled the supervised-transfer call.

Step 7

During the greeting, hang up Phone 2.

Step 8

On the Port Monitor, confirm that the state of the port handling the call changes to “Idle.” This state means that the port
                                 was successfully released when the call ended.

Step 9

Select Stop Polling .

Step 10

Sign out of RTMT.

## Adding New User
               	 Templates for Multiple Integrations

When you create the first phone system integration, this phone
                  		system is automatically selected in the default user template. The users that
                  		you add after creating this phone system integration are assigned to this phone
                  		system by default.

However, for each additional phone system integration that you
                  		create, you must add the applicable new user templates that assign users to the
                  		new phone system. You must add the new templates before you add new users who
                  		are assigned to the new phone system.

For details on adding new user templates, or on selecting a user template when adding a new user, see the “User Templates” section in “User Attributes” chapter of the System Administration Guide for Cisco Unity Connection Release 15 . The guide is available at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/15/administration/guide/b_15cucsag.html .

Cisco and the Cisco Logo are trademarks of Cisco Systems, Inc.
                  		and/or its affiliates in the U.S. and other countries. A listing of Cisco's
                  		trademarks can be found at www.cisco.com/go/trademarks .
                  		Third party trademarks mentioned are the property of their respective owners.
                  		The use of the word partner does not imply a partnership relationship between
                  		Cisco and any other company. (1005R)

Any Internet Protocol (IP) addresses used in this document are
                  		not intended to be actual addresses. Any examples, command display output, and
                  		figures included in the document are shown for illustrative purposes only. Any
                  		use of actual IP addresses in illustrative content is unintentional and
                  		coincidental.

© 2015 Cisco Systems, Inc. All rights reserved.

### This Document Applies to These Products

- Unity Connection Version 14

| Note | While integrating the Cisco Unity Connection with Cisco Unified
                                    			 Call Manager through a QSIG- Enabled Phone system with Cisco ISR Voice gateway
                                    			 uncheck the Synchronize guest time to host option for Unified Communications
                                    			 product line in Virtualized environment. This enables the Unified
                                    			 Communications to synchronize with their clock to external NTP servers. |
|---|---|

| Note | In
                              		Unity Connection integration with multiple phone systems is not supported for
                              		use with Cisco Business Edition 5000 and is supported only with Cisco Business
                              		Edition 6000/7000. |
|---|---|

| Note | The Cisco ISR voice gateway performs transfers by
                                 			 hairpinning two independent calls across two b-channels on the QSIG trunk.
                                 			 Hairpinned calls use more QSIG channels in comparison to the number of
                                 			 Cisco Unity Connection voice messaging ports that are available to answer
                                 			 calls. Release (blind) transfers that are forwarded back
                                    				to Unity Connection uses three b-channels for the remainder of the call.
                                    				However, supervised transfers pull back the consulting call when the target is
                                    				unavailable so that only one b-channel is used for the remainder of the call. |
|---|---|

| Field | Considerations |
|---|---|
| Enabled | Check this check box to enable the port.
                              				  The port is enabled during normal operation. Uncheck this check box to disable the
                              				  port. When the port is disabled, calls to the port get a ringing tone but are
                              				  not answered. Typically, the port is disabled only by the installer during
                              				  testing. |
| Server | (When a Unity
                                 					 Connection cluster is configured) Select the name of the Unity Connection
                              				  server that you want to handle this port. Assign an equal number of answering and
                              				  dial-out voice messaging ports to the Unity Connection servers so that they
                              				  equally share the voice messaging traffic. |
| Answer Calls | Check this check box to designate the port
                              				  for answering calls. These calls can be incoming calls from unidentified
                              				  callers or from users. All voice messaging ports connecting to
                              				  the Cisco ISR voice gateway must have the Answer Calls check box checked.
                              				  Otherwise, calls to Unity Connection may not be answered. |
| Perform Message Notification | Check this check box to designate the port
                              				  for notifying users of messages. Assign Perform Message Notification to the
                              				  least busy ports. |
| Send MWI Requests | Check this check box to designate the port
                              				  for turning MWIs on and off. Assign Send MWI Requests to the least busy ports. |
| Allow TRAP Connections | Check this check box so that users can use
                              				  the port for recording and playback through the phone in Unity Connection web
                              				  applications. Assign Allow TRAP Connections to the least busy ports. |

| Note | The
                              		Cisco ISR voice gateway performs transfers by hairpinning two independent calls
                              		across two b-channels on the QSIG trunk. Hairpinned calls use more QSIG
                              		channels in comparison to the number of Unity Connection voice messaging ports
                              		that are available to answer calls. If your system uses Unity Connection
                              		auto-attendant transfers, you must provision a larger number of QSIG b-channels
                              		than the number of Unity Connection voice messaging ports that answer calls. |
|---|---|

| Transfer Types | Usage |
|---|---|
| Release transfer (blind transfer) | Program the phone to forward calls to the pilot number when: The extension is busy The call is not answered |
| Supervised transfer | Program the phone to forward calls to the pilot number only when
                                 					 the call is not answered (on the phone system, the number of rings before
                                 					 forwarding must be more than the number of rings to supervise the call).
                                 					 Confirm that call forwarding is disabled when the extension is busy. |

| Note | If the Unity Connection SIP Port setting cannot be 5060
                           		(for example, it is set to 5061), you must change the SIP port that the Cisco
                           		ISR voice gateway uses. You can use a command similar to the following: dial-peer voice 1 voip  session protocol sipv2  session
                              		  target ipv4:10.00.00.00:5061 For a Unity Connection cluster, identify the Unity Connection servers
                              		  with a fully qualified domain name (FQDN), and configure a DNS server to
                              		  resolve the FQDN to the IP addresses and SIP ports of the Unity Connection
                              		  server. |
|---|---|

| Step 1 | In Cisco Unity Connection Administration, expand Telephony Integrations > and select Phone System . |
|---|---|
| Step 2 | On the Search Phone Systems page, under Display Name, select the
                                 			 name of the default phone system. |
| Step 3 | On the Phone System Basics page, in the Phone System Name field,
                                 			 enter the descriptive name that you want for the phone system. |
| Step 4 | If you want to use this phone system as the default for TRaP
                                 			 connections so that administrators and users without voicemail boxes can record
                                 			 and playback through the phone in Unity Connection web applications, check the Default TRAP Switch check box. If you want to use
                                 			 another phone system as the default for TRaP connections, uncheck this check
                                 			 box. |
| Step 5 | Select Save . |
| Step 6 | On the Phone System Basics page, in the Related Links drop-down
                                 			 box, select Add Port Group and select Go . |
| Step 7 | On the New Port Group page, enter the applicable settings and
                                 			 select Save . Table 3. Settings for the New Port Group Page Field Setting Phone System Select the name of the phone system that you entered in Step 3 . Create From Select Port Group Template and
                                                						  select SIP in the drop-down
                                                						  box. Display Name Enter a descriptive name for the port group. You can accept the
                                                						  default name or enter the name that you want. Authenticate with SIP Server Confirm that this check box is unchecked. Authentication User Name Leave this field blank. Authentication Password Leave this field blank. Contact Line Name Enter the voice messaging pilot number that matches the dial
                                                						  plan configuration of the gateway. SIP Security Profile Select 5060 . SIP Transport Protocol Select the SIP transport protocol that Unity Connection uses. IPv4 Address or Host Name Enter the IP address (or host name) of the primary gateway that
                                                						  you are connecting to Unity Connection. IPv6 Address or Host Name Do not enter a value in this field. IPv6 is not supported for
                                                						  this type of integration. IP Address or Host Name Enter the IP address (or host name) of the primary gateway that
                                                						  you are connecting to Unity Connection. Port Enter the IP port of the primary gateway that you are connecting
                                                						  to Unity Connection. We recommend that you use the default setting. This setting must match the port setting of the gateway.
                                                						  Otherwise the integration does not function correctly. | Field | Setting | Phone System | Select the name of the phone system that you entered in Step 3 . | Create From | Select Port Group Template and
                                                						  select SIP in the drop-down
                                                						  box. | Display Name | Enter a descriptive name for the port group. You can accept the
                                                						  default name or enter the name that you want. | Authenticate with SIP Server | Confirm that this check box is unchecked. | Authentication User Name | Leave this field blank. | Authentication Password | Leave this field blank. | Contact Line Name | Enter the voice messaging pilot number that matches the dial
                                                						  plan configuration of the gateway. | SIP Security Profile | Select 5060 . | SIP Transport Protocol | Select the SIP transport protocol that Unity Connection uses. | IPv4 Address or Host Name | Enter the IP address (or host name) of the primary gateway that
                                                						  you are connecting to Unity Connection. | IPv6 Address or Host Name | Do not enter a value in this field. IPv6 is not supported for
                                                						  this type of integration. | IP Address or Host Name | Enter the IP address (or host name) of the primary gateway that
                                                						  you are connecting to Unity Connection. | Port | Enter the IP port of the primary gateway that you are connecting
                                                						  to Unity Connection. We recommend that you use the default setting. This setting must match the port setting of the gateway.
                                                						  Otherwise the integration does not function correctly. |
| Field | Setting |
| Phone System | Select the name of the phone system that you entered in Step 3 . |
| Create From | Select Port Group Template and
                                                						  select SIP in the drop-down
                                                						  box. |
| Display Name | Enter a descriptive name for the port group. You can accept the
                                                						  default name or enter the name that you want. |
| Authenticate with SIP Server | Confirm that this check box is unchecked. |
| Authentication User Name | Leave this field blank. |
| Authentication Password | Leave this field blank. |
| Contact Line Name | Enter the voice messaging pilot number that matches the dial
                                                						  plan configuration of the gateway. |
| SIP Security Profile | Select 5060 . |
| SIP Transport Protocol | Select the SIP transport protocol that Unity Connection uses. |
| IPv4 Address or Host Name | Enter the IP address (or host name) of the primary gateway that
                                                						  you are connecting to Unity Connection. |
| IPv6 Address or Host Name | Do not enter a value in this field. IPv6 is not supported for
                                                						  this type of integration. |
| IP Address or Host Name | Enter the IP address (or host name) of the primary gateway that
                                                						  you are connecting to Unity Connection. |
| Port | Enter the IP port of the primary gateway that you are connecting
                                                						  to Unity Connection. We recommend that you use the default setting. This setting must match the port setting of the gateway.
                                                						  Otherwise the integration does not function correctly. |
| Step 8 | On the Port Group Basics page, in the Related Links drop-down
                                 			 box, select Add Ports and select Go . |
| Step 9 | On the New Port page, enter the following settings and select Save . Table 4. Settings for the New Ports Page Field Considerations Enabled Check this check box. Number of Ports Enter the number of voice
                                                						  messaging ports that you want to create in this port group. Note For a Unity Connection cluster, you must enter the total number
                                                         						  of voice messaging ports that are used by all Unity Connection servers. Each
                                                         						  port is later assigned to a specific Unity Connection server. Phone System Select the name of the
                                                						  phone system that you entered in Step 3 . Port Group Select the name of the
                                                						  port group that you added in Step
                                                   							 7 . Server Select the name of the
                                                						  Unity Connection server. | Field | Considerations | Enabled | Check this check box. | Number of Ports | Enter the number of voice
                                                						  messaging ports that you want to create in this port group. Note For a Unity Connection cluster, you must enter the total number
                                                         						  of voice messaging ports that are used by all Unity Connection servers. Each
                                                         						  port is later assigned to a specific Unity Connection server. | Note | For a Unity Connection cluster, you must enter the total number
                                                         						  of voice messaging ports that are used by all Unity Connection servers. Each
                                                         						  port is later assigned to a specific Unity Connection server. | Phone System | Select the name of the
                                                						  phone system that you entered in Step 3 . | Port Group | Select the name of the
                                                						  port group that you added in Step
                                                   							 7 . | Server | Select the name of the
                                                						  Unity Connection server. |
| Field | Considerations |
| Enabled | Check this check box. |
| Number of Ports | Enter the number of voice
                                                						  messaging ports that you want to create in this port group. Note For a Unity Connection cluster, you must enter the total number
                                                         						  of voice messaging ports that are used by all Unity Connection servers. Each
                                                         						  port is later assigned to a specific Unity Connection server. | Note | For a Unity Connection cluster, you must enter the total number
                                                         						  of voice messaging ports that are used by all Unity Connection servers. Each
                                                         						  port is later assigned to a specific Unity Connection server. |
| Note | For a Unity Connection cluster, you must enter the total number
                                                         						  of voice messaging ports that are used by all Unity Connection servers. Each
                                                         						  port is later assigned to a specific Unity Connection server. |
| Phone System | Select the name of the
                                                						  phone system that you entered in Step 3 . |
| Port Group | Select the name of the
                                                						  port group that you added in Step
                                                   							 7 . |
| Server | Select the name of the
                                                						  Unity Connection server. |
| Step 10 | On the Search Ports page, select the display name of the first
                                 			 voice messaging port that you created for this phone system integration. Note By default, the display names for the voice messaging ports are
                                             				composed of the port group display name followed by incrementing numbers. | Note | By default, the display names for the voice messaging ports are
                                             				composed of the port group display name followed by incrementing numbers. |
| Note | By default, the display names for the voice messaging ports are
                                             				composed of the port group display name followed by incrementing numbers. |
| Step 11 | On the Port Basics page, enter the following settings. The
                                 			 fields in the following table are the ones that you can change. Table 5. Settings for the Voice Messaging Ports Field Considerations Enabled Check this check box to
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
| Step 12 | Select Save . |
| Step 13 | Select Next . |
| Step 14 | Repeat Step 11 through Step
                                    				13 for all remaining voice messaging ports for the phone system. |
| Step 15 | If another phone system integration exists, in Cisco Unity
                                 			 Connection Administration, expand Telephony
                                    				Integrations , then select Trunk .
                                 			 Otherwise, skip to Step 19 . |
| Step 16 | On the Search Phone System Trunks page, on the Phone System
                                 			 Trunk menu, select New Phone System
                                    				Trunk . |
| Step 17 | On the New Phone System Trunk page, enter the following settings
                                 			 for the phone system trunk and select Save . Table 6. Settings for the Phone System Trunk Field Setting From Phone System Select the display name
                                                						  of the phone system that you are creating a trunk for. To Phone System Select the display name
                                                						  of the previously existing phone system that the trunk connects to. Trunk Access Code Enter the extra digits
                                                						  that Unity Connection must dial to transfer calls through the gateway to
                                                						  extensions on the previously existing phone system. | Field | Setting | From Phone System | Select the display name
                                                						  of the phone system that you are creating a trunk for. | To Phone System | Select the display name
                                                						  of the previously existing phone system that the trunk connects to. | Trunk Access Code | Enter the extra digits
                                                						  that Unity Connection must dial to transfer calls through the gateway to
                                                						  extensions on the previously existing phone system. |
| Field | Setting |
| From Phone System | Select the display name
                                                						  of the phone system that you are creating a trunk for. |
| To Phone System | Select the display name
                                                						  of the previously existing phone system that the trunk connects to. |
| Trunk Access Code | Enter the extra digits
                                                						  that Unity Connection must dial to transfer calls through the gateway to
                                                						  extensions on the previously existing phone system. |
| Step 18 | Repeat Step
                                    				16 and Step 17 for all remaining phone system trunks that you want to create. |
| Step 19 | In the Related Links drop-down list, select Check Telephony
                                    				Configuration and select Go to confirm
                                 			 the phone system integration settings. If the test is not successful, the Task Execution Results
                                    				displays one or more messages with troubleshooting steps. After correcting the
                                    				problems, test the Unity Connection again. |
| Step 20 | In the Task Execution Results window, select Close . |

| Field | Setting |
|---|---|
| Phone System | Select the name of the phone system that you entered in Step 3 . |
| Create From | Select Port Group Template and
                                                						  select SIP in the drop-down
                                                						  box. |
| Display Name | Enter a descriptive name for the port group. You can accept the
                                                						  default name or enter the name that you want. |
| Authenticate with SIP Server | Confirm that this check box is unchecked. |
| Authentication User Name | Leave this field blank. |
| Authentication Password | Leave this field blank. |
| Contact Line Name | Enter the voice messaging pilot number that matches the dial
                                                						  plan configuration of the gateway. |
| SIP Security Profile | Select 5060 . |
| SIP Transport Protocol | Select the SIP transport protocol that Unity Connection uses. |
| IPv4 Address or Host Name | Enter the IP address (or host name) of the primary gateway that
                                                						  you are connecting to Unity Connection. |
| IPv6 Address or Host Name | Do not enter a value in this field. IPv6 is not supported for
                                                						  this type of integration. |
| IP Address or Host Name | Enter the IP address (or host name) of the primary gateway that
                                                						  you are connecting to Unity Connection. |
| Port | Enter the IP port of the primary gateway that you are connecting
                                                						  to Unity Connection. We recommend that you use the default setting. This setting must match the port setting of the gateway.
                                                						  Otherwise the integration does not function correctly. |

| Field | Considerations |
|---|---|
| Enabled | Check this check box. |
| Number of Ports | Enter the number of voice
                                                						  messaging ports that you want to create in this port group. Note For a Unity Connection cluster, you must enter the total number
                                                         						  of voice messaging ports that are used by all Unity Connection servers. Each
                                                         						  port is later assigned to a specific Unity Connection server. | Note | For a Unity Connection cluster, you must enter the total number
                                                         						  of voice messaging ports that are used by all Unity Connection servers. Each
                                                         						  port is later assigned to a specific Unity Connection server. |
| Note | For a Unity Connection cluster, you must enter the total number
                                                         						  of voice messaging ports that are used by all Unity Connection servers. Each
                                                         						  port is later assigned to a specific Unity Connection server. |
| Phone System | Select the name of the
                                                						  phone system that you entered in Step 3 . |
| Port Group | Select the name of the
                                                						  port group that you added in Step
                                                   							 7 . |
| Server | Select the name of the
                                                						  Unity Connection server. |

| Note | For a Unity Connection cluster, you must enter the total number
                                                         						  of voice messaging ports that are used by all Unity Connection servers. Each
                                                         						  port is later assigned to a specific Unity Connection server. |
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
                                                						  of the previously existing phone system that the trunk connects to. |
| Trunk Access Code | Enter the extra digits
                                                						  that Unity Connection must dial to transfer calls through the gateway to
                                                						  extensions on the previously existing phone system. |

| Step 1 | Set up two test extensions (Phone 1 and
                                 			 Phone 2) on the same phone system that Unity Connection is connected to. |
|---|---|
| Step 2 | Set Phone 1 to forward calls to the Unity
                                 			 Connection pilot number when calls are not answered. Caution The phone system must forward calls to the Unity
                                             				Connection pilot number in no fewer than four rings. Otherwise, the test may
                                             				fail. | Caution | The phone system must forward calls to the Unity
                                             				Connection pilot number in no fewer than four rings. Otherwise, the test may
                                             				fail. |
| Caution | The phone system must forward calls to the Unity
                                             				Connection pilot number in no fewer than four rings. Otherwise, the test may
                                             				fail. |
| Step 3 | In Cisco Unity Connection Administration,
                                 			 expand Users > and select Users . |
| Step 4 | On the Search Users page, select the display
                                 			 name of a user to use for testing. The extension for this user must be the
                                 			 extension for Phone 1. |
| Step 5 | On the Edit User Basics page, uncheck the Set for Self-enrollment at Next
                                    				Login check box. |
| Step 6 | In the Voice Name field, record a voice name
                                 			 for the test user and select Save . |
| Step 7 | On the Edit menu, select Message Waiting
                                    				Indicators . |
| Step 8 | On the Message Waiting Indicators page,
                                 			 select the message waiting indicator. If no message waiting indication is in
                                 			 the table, select Add New . |
| Step 9 | On the Edit Message Waiting Indicator page,
                                 			 enter the following settings. Table 7. Settings for the Edit MWI Page Field Setting Enabled Check this check box to enable MWIs
                                                						  for the test user. Display Name Accept the default or enter a
                                                						  different name. Inherit User’s Extension Check this check box to enable MWIs
                                                						  on Phone 1. | Field | Setting | Enabled | Check this check box to enable MWIs
                                                						  for the test user. | Display Name | Accept the default or enter a
                                                						  different name. | Inherit User’s Extension | Check this check box to enable MWIs
                                                						  on Phone 1. |
| Field | Setting |
| Enabled | Check this check box to enable MWIs
                                                						  for the test user. |
| Display Name | Accept the default or enter a
                                                						  different name. |
| Inherit User’s Extension | Check this check box to enable MWIs
                                                						  on Phone 1. |
| Step 10 | Select Save . |
| Step 11 | On the Edit menu, select Transfer Rules . |
| Step 12 | On the Transfer Rules page, select the
                                 			 active option. |
| Step 13 | On the Edit Transfer Rule page, under
                                 			 Transfer Action, select the Extension option and
                                 			 enter the extension of Phone 1. |
| Step 14 | In the Transfer Type field, select Release to Switch . |
| Step 15 | Select Save . |
| Step 16 | Minimize the Cisco Unity Connection
                                 			 Administration window. Do not close the Cisco Unity Connection Administration
                                 			 window because you use it again in a later procedure. |
| Step 17 | Sign in to the Real-Time Monitoring Tool
                                 			 (RTMT). |
| Step 18 | On the Unity Connection menu, select Port Monitor . The Port
                                 			 Monitor tool appears in the right pane. |
| Step 19 | In the right pane, select Start Polling . The Port
                                 			 Monitor displays which port is handling the calls that you make. |

| Caution | The phone system must forward calls to the Unity
                                             				Connection pilot number in no fewer than four rings. Otherwise, the test may
                                             				fail. |
|---|---|

| Field | Setting |
|---|---|
| Enabled | Check this check box to enable MWIs
                                                						  for the test user. |
| Display Name | Accept the default or enter a
                                                						  different name. |
| Inherit User’s Extension | Check this check box to enable MWIs
                                                						  on Phone 1. |

| Step 1 | From Phone 2, enter the access code necessary to get an outside line, then enter the number outside callers use to dial directly
                                 to Unity Connection. |
|---|---|
| Step 2 | In the Port Monitor, note which port handles this call. |
| Step 3 | When you hear the opening greeting, enter the extension for Phone 1. Hearing the opening greeting means that the port is configured
                                 correctly. |
| Step 4 | Confirm that Phone 1 rings and that you hear a ringback tone on Phone 2. Hearing a ringback tone means that Unity Connection
                                 correctly released the call and transferred it to Phone 1. |
| Step 5 | Leaving Phone 1 unanswered, confirm that the state of the port handling the call changes to “Idle.” This state means that
                                 release transfer is successful. |
| Step 6 | Confirm that, after the number of rings that the phone system is set to wait, the call is forwarded to Cisco Unity Connection
                                 and that you hear the greeting for the test user. Hearing the greeting means that the phone system forwarded the unanswered
                                 call and the call-forward information to Unity Connection, which correctly interpreted the information. |
| Step 7 | On the Port Monitor, note which port handles this call. |
| Step 8 | Leave a message for the test user and hang up Phone 2. |
| Step 9 | In the Port Monitor, confirm that the state of the port handling the call changes to “Idle.” This state means that the port
                                 was successfully released when the call ended. |
| Step 10 | Confirm that the MWI on Phone 1 is activated. The activated MWI means that the phone system and Unity Connection are successfully
                                 integrated for turning on MWIs. |

| Step 1 | From Phone 1, enter the internal pilot number for Unity Connection. |
|---|---|
| Step 2 | When asked for your password, enter the password for the test user. Hearing the request for your password means that the phone
                                 system sent the necessary call information to Unity Connection, which correctly interpreted the information. |
| Step 3 | Confirm that you hear the recorded voice name for the test user (if you did not record a voice name for the test user, you
                                 hear the extension number for Phone 1). Hearing the voice name means that Unity Connection correctly identified the user by
                                 the extension. |
| Step 4 | Listen to the message. |
| Step 5 | After listening to the message, delete the message. |
| Step 6 | Confirm that the MWI on Phone 1 is deactivated. The deactivated MWI means that the phone system and Unity Connection are successfully
                                 integrated for turning off MWIs. |
| Step 7 | Hang up Phone 1. |
| Step 8 | On the Port Monitor, confirm that the state of the port handling the call changes to “Idle.” This state means that the port
                                 was successfully released when the call ended. |

| Step 1 | In Cisco Unity Connection Administration, on the Edit Transfer Rule page for the test user, in the Transfer Type field, select Supervise Transfer . |
|---|---|
| Step 2 | In the Rings to Wait For field, enter 3 . |
| Step 3 | Select Save . |
| Step 4 | Minimize the Cisco Unity Connection Administration window. Do not close the Cisco Unity Connection Administration window because
                                 you use it again in a later procedure. |

| Step 1 | From Phone 2, enter the access code necessary to get an outside line, then enter the number outside callers use to dial directly
                                 to Unity Connection. |
|---|---|
| Step 2 | On the Port Monitor, note which port handles this call. |
| Step 3 | When you hear the opening greeting, enter the extension for Phone 1. Hearing the opening greeting means that the port is configured
                                 correctly. |
| Step 4 | Confirm that Phone 1 rings and that you do not hear a ringback tone on Phone 2. Instead, you should hear the indication your
                                 phone system uses to mean that the call is on hold (for example, music). |
| Step 5 | Leaving Phone 1 unanswered, confirm that the state of the port handling the call remains “Busy.” This state and hearing an
                                 indication that you are on hold mean that Unity Connection is supervising the transfer. |
| Step 6 | Confirm that, after three rings, you hear the greeting for the test user. Hearing the greeting means that Unity Connection
                                 successfully recalled the supervised-transfer call. |
| Step 7 | During the greeting, hang up Phone 2. |
| Step 8 | On the Port Monitor, confirm that the state of the port handling the call changes to “Idle.” This state means that the port
                                 was successfully released when the call ended. |
| Step 9 | Select Stop Polling . |
| Step 10 | Sign out of RTMT. |