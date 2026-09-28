---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-connection-12x-integration-guide-cucme-sip-b-12xcucmesip-html-b24c37524c
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/12x/integration/guide/cucme_sip/b_12xcucmesip.html
retrieved_at: 2026-08-19T00:45:37.933352+00:00
---

Cisco Unified Communications Manager Express SIP Trunk Integration Guide for Cisco Unity Connection Release 12.x

# Cisco Unified Communications Manager Express SIP Trunk Integration Guide for Cisco Unity Connection Release 12.x

### Download Options

Updated: January 24, 2019

# Cisco Unified
            	 Communications Manager Express SIP Trunk Integration Guide for Cisco Unity
            	 Connection Release 12.x

## Integration
               	 Tasks

Before doing the
                  		following tasks to integrate Unity Connection with Cisco Unified Communications
                  		Manager Express through a SIP trunk, confirm that the Unity Connection server
                  		is ready for the integration by completing the applicable tasks in the “ Installing Cisco Unity
                     		  Connection ” chapter of the Install, Upgrade,
                     		  and Maintenance Guide for Cisco Unity Connection , Release 12.x, available
                  		at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/12x/install_upgrade/guide/b_12xcuciumg.html .

The following task
                  		list describes the process for creating the integration.

### Task List to
                  	 Create the Integration

Use the following task list to set
                     		up a Cisco Unified CM Express SIP trunk integration.

Review the system and equipment requirements to confirm that all
                           			 phone system and Unity Connection server requirements have been met. See the
                           			 “Requirements” section on page 2.

Plan how the voice messaging ports are used by Unity Connection. See
                           			 the “Planning the Usage of Voice Messaging in Unity Connection” section on page
                           			 4.

Program Cisco Unified Communications Manager Express. See the
                           			 “Programming the Cisco Unified Communications Manager Express Phone System”
                           			 section on page 7.

Create the integration. See the “Creating a New Integration with
                           			 Cisco Unified CM Express” section on page 10.

- Test the integration. See
                        		  the “Testing the Integration” section on page 13.

If this integration is a second or subsequent integration, add the
                           			 applicable new user templates for the new phone system. See the “Adding New
                           			 User Templates for Multiple Integrations” section on page 16.

While integrating the Cisco Unity Connection with Cisco Unified Call
                              		Manager through a SIP trunk uncheck the Synchronize guest time to host option
                              		for Unified Communications product line in Virtualized environment. This
                              		enables the Unified Communications to synchronize with their clock to external
                              		NTP servers.

## Requirements

The Cisco Unified CM Express SIP trunk integration supports
                  		configurations of the following components:

### Phone
                  	 System

A compatible
                           			 version of Cisco Unified CM Express.

For details on
                           			 compatible versions of Cisco Unified CM Express, see the Compatibility Matrix for
                              				Cisco Unity Connection at http://www.cisco.com/c/en/us/support/unified-communications/unity-connection/products-device-support-tables-list.html .

A compatible
                           			 Cisco IOS software version. See the Cisco Unified CME and Cisco IOS Software
                           			 Version Compatibility Matrix at http://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-express/products-device-support-tables-list.html .

- Cisco Unified CM Express
                        		  feature license.

Cisco IP phone
                           			 feature licenses, and Cisco licenses for other H.323-compliant devices or
                           			 software (such as Cisco VirtualPhone and Microsoft NetMeeting clients)
                           			 connected to the network, as well as one license for each Unity Connection
                           			 port.

For the Cisco
                           			 Unified CM Express extensions, SIP phones that support DTMF relay as described
                           			 in RFC-2833. For a list of supported Cisco IP phone models, see the applicable
                           			 compatibility information document at http://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-express/products-device-support-tables-list.html .

- Only SIP phones.

- Both SCCP phones and SIP
                              				phones.

Note that
                                 				  older SCCP phone models may require a Media Termination Point (MTP) to function
                                 				  correctly.

- A LAN Unity Connection in
                              				each location where you plug the applicable phone into the network.

### Unity Connection
                  	 Server

The applicable
                           			 version of Unity Connection. For details on compatible versions of Cisco Unity
                           			 Connection, see the Compatibility
                              				Matrix for Cisco Unity Connection , at http://www.cisco.com/c/en/us/support/unified-communications/unity-connection/products-device-support-tables-list.html .

Unity Connection
                           			 installed and ready for the integration, as described in the “Installing Cisco
                           			 Unity Connection” chapter of the Install, Upgrade, and Maintenance Guide for Cisco Unity
                              				Connection , Release 12.x, available at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/12x/install_upgrade/guide/b_12xcuciumg.html .

- A license that enables the
                        		  applicable number of voice messaging ports.

### Centralized Voice
                  	 Messaging

Unity Connection
                     		supports centralized voice messaging through the phone system, which supports
                     		various inter-phone system networking protocols including proprietary protocols
                     		such as Avaya DCS, Nortel MCDN, or Siemens CorNet, and standards-based
                     		protocols such as QSIG or DPNSS. Note that centralized voice messaging is a
                     		function of the phone system and its inter-phone system networking, not
                     		voicemail. Unity Connection supports centralized voice messaging as long as the
                     		phone system and its inter-phone system networking are properly configured. For
                     		details, see the “ Centralized Voice
                        		  Messaging ” section in the “Integrating Cisco Unity Connection with the
                     		Phone System” chapter of the Design Guide for
                        		  Cisco Unity Connection , Release 12.x at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/12x/design/guide/b_12xcucdg.html .

## Integration
               	 Description

The Cisco Unified
                  		Communications Manager (CM) Express SIP trunk integration uses a LAN to connect
                  		Unity Connection and the phone system. The Cisco Unified Communications Manager
                  		Express router also provides connections to the PSTN.

For a list of
                  		  supported versions of Cisco Unified CM Express that are qualified to integrate
                  		  with Unity Connection through a SIP trunk, see the Compatibility Matrix for
                  		  Cisco Unity Connection at http://www.cisco.com/c/en/us/support/unified-communications/unity-connection/products-device-support-tables-list.html .

### Call Information

The phone system sends the following information with forwarded calls:

The extension of the called party

The extension of the calling party (for internal calls) or the phone
                           			 number of the calling party (if it is an external call and the system uses
                           			 caller ID)

- The reason for the forward
                        		  (the extension is busy, does not answer, or is set to forward all calls)

Unity Connection uses this information to answer the call appropriately.
                     		For example, a call forwarded to Unity Connection is answered with the personal
                     		greeting of the user. If the phone system routes the

call to Unity Connection without this information, Unity Connection
                     		answers with the opening greeting.

### Integration
                  	 Functionality

The Cisco Unified CM Express SIP trunk integration with Unity Connection
                     		provides the following features:

Call forward to personal
                           			 greeting

- Call forward to busy
                        		  greeting

- Caller ID

Easy message access (a user can retrieve messages without entering
                           			 an ID; Unity Connection identifies a user based on the extension from which the
                           			 call originated; a password may be required)

Identified user messaging (Unity Connection automatically identifies
                           			 a user who leaves a message during a forwarded internal call, based on the
                           			 extension from which the call originated)

- Message waiting indication
                        		  (MWI)

### Integrations with
                  	 Multiple Phone Systems

When Unity
                     		Connection is installed as Cisco Business Edition—on the same server with Cisco
                     		Unified Communications Manager—Unity Connection cannot be integrated with
                     		multiple phone systems at one time.

When Unity
                     		Connection is not installed as Cisco Business Edition, Unity Connection can be
                     		integrated with two or more phone systems at one time. For information on and
                     		instructions for integrating Unity Connection with multiple phone systems, see
                     		the Multiple Phone
                        		  System Integration Guide for Cisco Unity Connection , Release 12.x at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/12x/integration/guide/multiple_integration/b_cuc12xintmultiple.html .

## Planning the Usage
               	 of Voice Messaging in Unity Connection

Before programming the phone system, you need to plan how the voice
                  		messaging ports are used by Unity Connection. The following considerations
                  		affect the programming for the phone system (for example, setting up the hunt
                  		group or call forwarding for the voice messaging ports):

For a Unity Connection cluster, each Unity Connection server must
                        			 have enough ports to handle all voice messaging traffic in case the other
                        			 server stops functioning.

- The number of voice
                     		  messaging ports that answer calls.

The number of voice messaging ports that only dial out, for example,
                        			 to send message notification, to set message waiting indicators (MWIs), and to
                        			 make telephone record and playback (TRAP) connections.

The following table describes the voice messaging port settings in Unity
                  		Connection that can be set on Telephony Integrations > Port of Cisco Unity
                  		Connection Administration.

(When a Unity Connection cluster is configured)

Select the name of the Unity Connection server that you want to
                              				  handle this port.

Assign an equal number of answering and dial-out voice messaging
                              				  ports to the Unity Connection servers so that they equally share the voice
                              				  messaging traffic.

answered.

Check this check box to designate the port for notifying users
                              				  of messages.

Check this check box to designate the port for turning MWIs on
                              				  and off.

Check this check box so that users can use the phone as a
                              				  recording and playback device in Unity Connection web applications.

### Determining the
                  	 Number Voice of Messaging Ports to Install

The number of voice
                     		messaging ports to install depends on numerous factors, including:

The number of
                           			 calls Unity Connection answers when call traffic is at its peak.

- The expected length of each
                        		  message that callers record and that users listen to.

- The number of users.

- The number of calls made
                        		  for message notification.

- The number of MWIs
                        		  activated when call traffic is at its peak.

The number of
                           			 TRAP connections needed when call traffic is at its peak. (TRAP connections are
                           			 used by Unity Connection web applications to play back and record over the
                           			 phone.)

- The number of calls that
                        		  use the automated attendant and call handlers when call traffic is at its peak.

- Whether a Unity Connection
                        		  cluster is configured. For considerations, see the Considerations for a Unity Connection Cluster section.

It is best to
                     		install only the number of voice messaging ports that are needed so that system
                     		resources are not allocated to unused ports.

### Determining the
                  	 Number of Voice Messaging Ports to Answers Calls

The calls that the
                     		voice messaging ports answer can be incoming calls from unidentified callers or
                     		from users. Typically, the voice messaging ports that answer calls are the
                     		busiest.

You can set voice
                     		messaging ports to both answer calls and to dial out (for example, to send
                     		message notifications). However, when the voice messaging ports perform more
                     		than one function and are very active (for example, answering many calls), the
                     		other functions may be delayed until the voice messaging port is free (for
                     		example, message notifications cannot be sent until there are fewer calls to
                     		answer). For best performance, dedicate certain voice messaging ports for only
                     		answering incoming calls, and dedicate other ports for only dialing out.

If your system is
                     		configured for a Unity Connection cluster, see the Considerations for a Unity Connection Cluster section.

### Determining the
                  	 Number of Voice Messaging Ports to Dials Out

Ports that only dial
                     		out can do one or more of the following:

Notify users by
                           			 phone, pager, or email of messages that have arrived.

- Turn MWIs on and off for
                        		  user extensions.

Make a TRAP
                           			 connection so that users can use the phone as a recording and playback device
                           			 in Unity Connection web applications.

If your system is
                     		configured for a Unity Connection cluster, see the Considerations for a Unity Connection Cluster section.

In
                              		programming the phone system, do not send calls to voice messaging ports in
                              		Unity Connection that cannot answer calls (voice messaging ports that are not
                              		set to Answer Calls). For example, if a voice messaging port is set only to
                              		Send MWI Requests, do not send calls to it.

### Considerations for
                  	 a Unity Connection Cluster

If your system is configured for a Unity Connection cluster, consider
                     		how the voice messaging ports are used in different scenarios.

## When Both Unity
               	 Connection Servers are Functioning

A hunt group is configured to send incoming calls first to the
                        			 subscriber server, then to the publisher server if no answering ports are
                        			 available on the subscriber server.

In Cisco Unity Connection Administration, the voice messaging ports
                        			 are configured so that an equal number of voice messaging ports are assigned to
                        			 each Unity Connection server. This guide directs you to assign the voice
                        			 messaging ports to their specific server at the applicable time.

The number of voice messaging ports that are assigned to one Unity
                        			 Connection server must be sufficient to handle all of the voice messaging
                        			 traffic for the system (answering calls and dialing out) when the other Unity
                        			 Connection server stops functioning.

If both Unity Connection servers must be functioning to handle the
                        			 voice messaging traffic, the system do not have sufficient capacity when one of
                        			 the servers stops functioning.

If all the voice messaging ports are assigned to one Unity
                        			 Connection server, the other Unity Connection server cannot answer calls or to
                        			 dial out.

Each Unity Connection server must have voice messaging ports that
                        			 answer calls and can dial out (for example, to set MWIs).

## When Only One
               	 Unity Connection Server is Functioning

The hunt group on the phone
                        			 system sends all calls to the functioning Unity Connection server.

- The functioning Unity
                     		  Connection server receives all voice messaging traffic for the system.

The number of voice messaging ports that are assigned to the
                        			 functioning Unity Connection server must be sufficient to handle all of the
                        			 voice messaging traffic for the system (answering calls and dialing out).

The functioning Unity Connection server must have voice messaging
                        			 ports that answer calls and can dial out (for example, to set MWIs).

If the functioning Unity Connection server does not have voice
                        			 messaging ports for answering calls, the system cannot answer incoming calls.
                        			 Similarly, if the functioning Unity Connection server does not have voice
                        			 messaging ports for dialing out, the system cannot dial out (for example, to
                        			 set MWIs).

## Programming the
               	 Cisco Unified Communications Manager Express Phone System

For details on
                  		programming the Cisco Unified Communications Manager Express router for the
                  		integration with Unity Connection, see the “Integrating Voice Mail” chapter of
                  		the Cisco Unified Communications Manager Express System Administrator Guide at http://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-express/products-installation-and-configuration-guides-list.html .

After you have
                  		configured the Cisco Unified CM Express router for the integration, do the
                  		applicable following procedures:

For Cisco
                        			 Unified CM Express 4.1 or later, if calls can be received from a Cisco Unified
                        			 Communications Manager SIP trunk, do the To Configure the Cisco Unified Communications Manager Express Router 4.1 and Later

- For a Unity Connection
                     		  cluster, do the To Configure the Cisco Unified Communications Manager Express Router for a Unity Connection Cluster

### To Configure the
                  	 Cisco Unified Communications Manager Express Router 4.1 and Later

On the Cisco Unified CM
                                 			 Express router connected to a Cisco Unified Communications Manager SIP trunk,
                                 			 go into the global configuration mode by entering the following command:

configure
                                       				  terminal

To enter the voice service
                                 			 configuration mode, enter the following command:

voice service
                                       				  voip

To disable the 302 “Moved
                                 			 Temporarily” SIP message, enter the following command:

no supplementary-service sip moved-temporarily

To exit the global configuration mode, enter the following
                                 			 command:

exit

### To Configure the
                  	 Cisco Unified Communications Manager Express Router for a Unity Connection
                  	 Cluster

On the Cisco
                                 			 Unified CM Express router, go into the global configuration mode by entering
                                 			 the following command:

configure
                                       				  terminal

To enter
                                 			 dial-peer configuration mode for port group for the publisher server, enter the
                                 			 following command:

dial-peer voice
                                       				  <number> voip

To set the
                                 			 description for the dial-peer, enter the following command:

description <name of
                                    				publisher server>

To set the
                                 			 Unity Connection pilot number for the dial-peer, enter the following command:

destination-pattern
                                    				<pilot number>

To configure
                                 			 the dial-peer to use Session Initiation Protocol (SIP) for calls, enter the
                                 			 following command:

session protocol
                                    				sipv2

To specify the
                                 			 IP address (or DNS name) of the publisher server, enter the following command:

session target {ipv4:<IP
                                    				address>|dns:<host name>}

To enable DTMF
                                 			 relay, enter the following command:

dtmf-relay
                                 			 rtp-nte

To set the
                                 			 codec for calls, enter the following command:

codec
                                 			 <codec used for calls>

To equalize
                                 			 the number of calls sent to each Unity Connection server in the cluster, enter
                                 			 the following command:

max-conn <number of
                                    				ports handled by publisher server>

To set the
                                 			 dial-peer preference for port group so that the calls are routed first to the
                                 			 subscriber server, then to the publisher server if no ports are available on
                                 			 the subscriber server, enter the following command:

preference 2

To enable
                                 			 huntstop, enter the following command:

huntstop

To exit the
                                 			 global configuration mode, enter the following command:

exit

To set a
                                 			 dial-peer that prevents Cisco Unified CM Express from hunting beyond the
                                 			 dial-peers for the Unity Connection port groups, entering the following
                                 			 command:

configure
                                    				terminal

To enter
                                 			 dial-peer configuration mode, enter the following command:

dial-peer voice
                                    				<number> voip

To set the
                                 			 description for the dial-peer, enter the following command:

description <name of
                                    				subscriber server>

To set the
                                 			 Unity Connection pilot number for the dial-peer, enter the following command:

destination-pattern
                                    				<pilot number>

To configure
                                 			 the dial-peer to use Session Initiation Protocol (SIP) for calls, enter the
                                 			 following command:

session protocol
                                    				sipv2

To specify the
                                 			 IP address (or DNS name) of the subscriber server, enter the following command:

session target {ipv4:<IP
                                    				address>|dns:<host name>}

To enable DTMF
                                 			 relay, enter the following command:

dtmf-relay
                                    				rtp-nte

To set the
                                 			 codec for calls, enter the following command:

codec <codec used for
                                    				calls>

To equalize
                                 			 the number of calls sent to each Unity Connection server in the cluster, enter
                                 			 the following command:

max-conn <number of
                                    				ports handled by subscriber server>

To set the
                                 			 dial-peer preference so that the calls are routed first to the subscriber
                                 			 server, then to the publisher server if no ports are available on the
                                 			 subscriber server, enter the following command:

preference 1

To disable
                                 			 huntstop so that the calls use the next available voice messaging port on the
                                 			 subscriber server, then use voice messaging ports on the publisher server if no
                                 			 ports are available on the subscriber server, enter the following command:

no huntstop

To exit the
                                 			 global configuration mode, enter the following command:

exit

Example

#### Example

```
!
dial-peer voice 2 voip
description CUC1
destination-pattern 8000
session protocol sipv2
session target ipv4:<IP address>
dtmf-relay rtp-nte
codec g711ulaw
max-conn 4
preference 1
huntstop
!
```

The following is
                        		  an example of the configuration with a Unity Connection cluster configured:

```
!
dial-peer voice 2 voip
description CUC1
destination-pattern <pilot number>
session protocol sipv2
session target ipv4:<IP address of publisher server>
dtmf-relay rtp-nte
codec g711ulaw
max-conn 4
preference 2
huntstop
!
dial-peer voice 4 voip
description CUC2
destination-pattern <pilot number>
session protocol sipv2
session target ipv4:<IP address of subscriber server>
dtmf-relay rtp-nte
codec g711ulaw
max-conn 4
preference 1
no huntstop
!
```

## Creating a New
               	 Integration with Cisco Unified CM Express

After ensuring that Cisco Unified Communications Manager Express and
                     		  Unity Connection are ready for the integration, do the following procedure to
                     		  set up the integration and to enter the port settings.

In Cisco Unity Connection
                              			 Administration, expand Telephony Integrations , then select Phone System .

On the Search Phone Systems
                              			 page, under Display Name , select the name of the default phone system.

On the Phone System Basics
                              			 page, in the Phone System Name field, enter the descriptive name that you
                              			 want for the phone system.

If you want to use this phone system as the default for TRaP
                              			 connections so that administrators and users without voicemail boxes can record
                              			 and playback through the phone in the Unity Connection web applications, check
                              			 the Default TRAP Switch check box . If you want to use another phone
                              			 system as the default for TRaP connections, uncheck this check box.

Select Save .

On the Phone System Basics page, in the Related Links drop-down
                              			 box, select Add Port Group and select Go .

On the New Port Group page, enter the applicable settings and
                              			 select Save.

Enter a descriptive name for the port group. You can
                                             						  accept the default name or enter the name that you want.

Authenticate with SIP Server

Check this check box if you want Unity Connection to
                                             						  authenticate with the Cisco Unified CM Express router.

Authentication User Name

Enter the name that Unity Connection uses to authenticate
                                             						  with the Cisco Unified CM Express router.

Enter the password that Unity Connection uses to
                                             						  authenticate with the Cisco Unified CM Express router.

Enter the voice messaging line name (or pilot number) that
                                             						  users use to contact Unity Connection and registers with the Cisco Unified CM
                                             						  Express router.

Cisco Unified CM Express does not support Cisco Unified
                                                      						  CM authentication and encryption.

IPv4 Address or Host Name

Enter the IP address (or host name) of the Cisco Unified
                                             						  CM Express router that you are integrating with Unity Connection.

IPv6 Address or Host Name

Do not enter a value in this field. IPv6 is not supported
                                             						  for Cisco Unified CM Express integrations.

Enter the IP address (or host name) of the Cisco Unified
                                             						  CM Express router that you are integrating with Unity Connection.

Enter the IP port of the Cisco Unified CM Express router
                                             						  that you are integrating with Unity Connection. We recommend that you use the
                                             						  default setting.

On the Port Group Basics page, in the Related Links drop-down box,
                              			 select Add Ports and select Go .

On the New Port page, enter the following settings and select Save .

Enter the number of voice messaging ports that you want to
                                             						  create in this port group.

For a Unity Connection cluster, you must enter the
                                                      						  total number of voice messaging ports that are used by all Unity Connection
                                                      						  servers. Each port is later assigned to a specific Unity Connection server.

On the Search Ports page, select the display name of the first
                              			 voice messaging port that you created for this phone integration.

By default, the display names for the voice messaging ports are
                                          				composed of the port group display name followed by incrementing numbers.

On the Port Basics page, set the voice messaging port settings as
                              			 applicable. The fields in the following table are the ones that you can change.

Uncheck this check box to disable the port. When the port
                                             						  is disabled, calls to the port get a ringing tone but are not answered.
                                             						  Typically, the port is disabled only by the installer during testing.

(For Unity Connection clusters only) Select the
                                             						  name of the Unity Connection server that you want to handle this port.

Assign an equal number of answering and dial-out voice
                                             						  messaging ports to the Unity Connection servers so that they equally share the
                                             						  voice messaging traffic.

Check this check box to designate the port for answering
                                             						  calls. These calls can be incoming calls from unidentified callers or from
                                             						  users.

Check this check box to designate the port for notifying
                                             						  users of messages. Assign Perform Message Notification to the least busy
                                             						  ports.

Check this check box to designate the port for turning
                                             						  MWIs on and off. Assign Send MWI Requests to the least busy ports.

Check this check box so that users can use the port for
                                             						  recording and playback through the phone in Unity Connection web applications.
                                             						  Assign Allow TRAP Connections to the least busy ports.

Select Save .

Select Next .

Repeat Step 11 through Step 13 for all remaining voice messaging
                              			 ports for the phone system.

If another phone system integration exists, in Cisco Unity
                              			 Connection Administration, expand Telephony Integrations , then select Trunk . Otherwise, skip to Step 19.

On the Search Phone System Trunks page, on the Phone System Trunk
                              			 menu, select New Phone System Trunk .

On the New Phone System Trunk page, enter the following settings for
                              			 the phone system trunk and select Save .

Select the display name of the previously existing phone
                                             						  system that the trunk connects to.

Enter the extra digits that Unity Connection must dial to
                                             						  transfer calls through the gateway to extensions on the previously existing
                                             						  phone system.

Repeat Step 16 and Step 17 for all remaining phone system trunks
                              			 that you want to create.

In the Related Links drop-down list, select Check Telephony
                                 				Configuration and select Go to confirm the phone system integration settings.

If the test is not successful, the Task Execution Results displays
                                 				one or more messages with troubleshooting steps. After correcting the problems,
                                 				test the Unity Connection again.

In the Task Execution Results window, select Close .

## Testing the
               	 Integration

To test whether
                  		Unity Connection and the phone system are integrated correctly, do the
                  		following procedures in the order listed.

If any of the steps
                  		indicate a failure, see the following documentation as applicable:

The “ Installing Cisco Unity
                           				Connection ” chapter of the Install,
                           				Upgrade, and Maintenance Guide for Cisco Unity Connection , Release 12.x,
                        			 available at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/12x/install_upgrade/guide/b_12xcuciumg.html .

- Troubleshooting Guide for
                        			 Cisco Unity Connection , Release 12.x at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/12x/troubleshooting/guide/b_12xcuctsg.html .

### Setting Up the Test Configuration

Set up two test extensions (Phone 1 and Phone 2) on the same
                                 			 phone system that Unity Connection is connected to.

Set Phone 1 to forward calls to the Unity Connection pilot number
                                 			 when calls are not answered.

The phone system must forward calls to the Unity
                                             				Connection pilot number in no fewer than four rings. Otherwise, the test may
                                             				fail.

In Cisco Unity Connection Administration, expand Users , then select Users .

On the Search Users page, select the display name of a user to use
                                 			 for testing. The extension for this user must be the extension for Phone 1.

On the Edit User Basics page, uncheck the Set for Self-enrollment at Next Login check box.

In the Voice Name field, record a recorded name for the test user.

Select Save .

On the Edit menu, select Message Waiting Indicators .

On the Message Waiting Indicators page, select the message waiting
                                 			 indicator. If no message waiting indication is in the table, select Add New .

On the Edit Message Waiting Indicator page, enter the following
                                 			 settings.

Field

Setting

Enabled

Check this check box to enable MWIs for the test user.

Display Name

Accept the default or enter a different name.

Inherit User’s Extension

Check this check box to enable MWIs on Phone 1.

Select Save .

On the Edit menu, select Transfer Rules .

On the Transfer Rules page, select the active transfer rule.

On the Edit Transfer Rule page, under Transfer Action , select Extension and enter the extension of Phone 1.

In the Transfer Type field, select Release to Switch .

Select Save.

Minimize the Cisco Unity Connection Administration window.

Do not close the Cisco Unity Connection Administration window
                                    				because you use it again in a later procedure.

Sign in to the Real-Time Monitoring Tool (RTMT).

On the Unity Connection menu, select Port Monitor . The Port Monitor tool appears in the right pane.

In the right pane, select Start Polling . The Port Monitor displays which port is
                                 			 handling the calls that you make.

### Testing an External Call with Release Transfer

From Phone 2, enter the access code necessary to get an outside
                                 			 line, then enter the number outside callers use to dial directly to Unity
                                 			 Connection.

In the Port Monitor, note which port handles this call.

When you hear the opening greeting, enter the extension for Phone
                                 			 1. Hearing the opening greeting means that the port is configured correctly.

Confirm that Phone 1 rings and that you hear a ringback tone on
                                 			 Phone 2. Hearing a ring back tone means that Unity Connection correctly
                                 			 released the call and transferred it to Phone 1.

Leaving Phone 1 unanswered, confirm that the state of the port
                                 			 handling the call changes to “Idle.” This state means that release transfer is
                                 			 successful.

Confirm that, after the number of rings that the phone system is
                                 			 set to wait, the call is forwarded to Unity Connection and that you hear the
                                 			 greeting for the test user. Hearing the greeting means that the phone system
                                 			 forwarded the unanswered call and the call-forward information to Unity
                                 			 Connection, which correctly interpreted the information.

On the Port Monitor, note which port handles this call.

Leave a message for the test user and hang up Phone 2.

In the Port Monitor, confirm that the state of the port handling
                                 			 the call changes to “Idle.” This state means that the port was successfully
                                 			 released when the call ended.

Confirm that the MWI on Phone 1 is activated. The activated MWI
                                 			 means that the phone system and Unity Connection are successfully integrated
                                 			 for turning on MWIs.

### Testing Listening to Messages

From Phone 1, enter the internal pilot number for Unity
                                 			 Connection.

When asked for your password, enter the password for the test
                                 			 user. Hearing the request for your password means that the phone system sent
                                 			 the necessary call information to Unity Connection, which correctly interpreted
                                 			 the information.

Confirm that you hear the recorded name for the test user (if you
                                 			 did not record a name for the test user, you hear the extension number for
                                 			 Phone 1). Hearing the recorded name means that Unity Connection correctly
                                 			 identified the user by the extension.

Listen to the message.

After listening to the message, delete the message.

Confirm that the MWI on Phone 1 is deactivated. The deactivated
                                 			 MWI means that the phone system and Unity Connection are successfully
                                 			 integrated for turning off MWIs.

Hang up Phone 1.

On the Port Monitor, confirm that the state of the port handling
                                 			 the call changes to “Idle.” This state means that the port was successfully
                                 			 released when the call ended.

### Setting Up Supervised Transfer on Cisco Unity Connection

In Cisco Unity Connection Administration, on the Edit Transfer
                                 			 Rule page for the test user, in the Transfer Type field, select Supervise Transfer .

In the Rings to Wait For field, enter 3 .

Select Save .

Minimize the Cisco Unity Connection Administration window.

Do not close the Cisco Unity Connection Administration window
                                    				because you use it again in a later procedure.

## Adding New User
               	 Templates for Multiple Integrations

When you create the
                  		first phone system integration, this first phone system is automatically
                  		selected in the default user template. The users that you add after creating
                  		this phone system integration is assigned to this phone system by default.

However, for each
                  		additional phone system integration that you create, you must add the
                  		applicable new user templates that assign users to the new phone system. You
                  		must add the new templates before you add new users who are assigned to the new
                  		phone system. For details on adding new user templates, or on selecting a user
                  		template when adding a new user, see the User Templates section of the “ User Attributes ”
                  		chapter of the System
                     		  Administration Guide for Cisco Unity Connection, Release 12.x , available at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/12x/administration/guide/b_12xcucsag.html .

### This Document Applies to These Products

- Unity Connection Version 12.x

| Note | While integrating the Cisco Unity Connection with Cisco Unified Call
                              		Manager through a SIP trunk uncheck the Synchronize guest time to host option
                              		for Unified Communications product line in Virtualized environment. This
                              		enables the Unified Communications to synchronize with their clock to external
                              		NTP servers. |
|---|---|

| Field | Considerations |
|---|---|
| Enabled | Check this check box. |
| Server | (When a Unity Connection cluster is configured) Select the name of the Unity Connection server that you want to
                              				  handle this port. Assign an equal number of answering and dial-out voice messaging
                              				  ports to the Unity Connection servers so that they equally share the voice
                              				  messaging traffic. |
| Answer Calls | Check this check box. Caution All voice messaging ports connecting to the
                                       				  Cisco Unified CM server must have the Answer Calls check box checked.
                                       				  Otherwise, calls to Unity Connection may not be answered. | Caution | All voice messaging ports connecting to the
                                       				  Cisco Unified CM server must have the Answer Calls check box checked.
                                       				  Otherwise, calls to Unity Connection may not be answered. |
| Caution | All voice messaging ports connecting to the
                                       				  Cisco Unified CM server must have the Answer Calls check box checked.
                                       				  Otherwise, calls to Unity Connection may not be answered. |
| Perform Message Notification | Check this check box to designate the port for notifying users
                              				  of messages. |
| Send MWI Requests | Check this check box to designate the port for turning MWIs on
                              				  and off. |
| Allow TRAP Connections | Check this check box so that users can use the phone as a
                              				  recording and playback device in Unity Connection web applications. |

| Caution | All voice messaging ports connecting to the
                                       				  Cisco Unified CM server must have the Answer Calls check box checked.
                                       				  Otherwise, calls to Unity Connection may not be answered. |
|---|---|

| Caution | In
                              		programming the phone system, do not send calls to voice messaging ports in
                              		Unity Connection that cannot answer calls (voice messaging ports that are not
                              		set to Answer Calls). For example, if a voice messaging port is set only to
                              		Send MWI Requests, do not send calls to it. |
|---|---|

| Step 1 | On the Cisco Unified CM
                                 			 Express router connected to a Cisco Unified Communications Manager SIP trunk,
                                 			 go into the global configuration mode by entering the following command: configure
                                       				  terminal |
|---|---|
| Step 2 | To enter the voice service
                                 			 configuration mode, enter the following command: voice service
                                       				  voip |
| Step 3 | To disable the 302 “Moved
                                 			 Temporarily” SIP message, enter the following command: no supplementary-service sip moved-temporarily |
| Step 4 | To exit the global configuration mode, enter the following
                                 			 command: exit |

| Step 1 | On the Cisco
                                 			 Unified CM Express router, go into the global configuration mode by entering
                                 			 the following command: configure
                                       				  terminal |
|---|---|
| Step 2 | To enter
                                 			 dial-peer configuration mode for port group for the publisher server, enter the
                                 			 following command: dial-peer voice
                                       				  <number> voip |
| Step 3 | To set the
                                 			 description for the dial-peer, enter the following command: description <name of
                                    				publisher server> |
| Step 4 | To set the
                                 			 Unity Connection pilot number for the dial-peer, enter the following command: destination-pattern
                                    				<pilot number> |
| Step 5 | To configure
                                 			 the dial-peer to use Session Initiation Protocol (SIP) for calls, enter the
                                 			 following command: session protocol
                                    				sipv2 |
| Step 6 | To specify the
                                 			 IP address (or DNS name) of the publisher server, enter the following command: session target {ipv4:<IP
                                    				address>\|dns:<host name>} |
| Step 7 | To enable DTMF
                                 			 relay, enter the following command: dtmf-relay
                                 			 rtp-nte |
| Step 8 | To set the
                                 			 codec for calls, enter the following command: codec
                                 			 <codec used for calls> |
| Step 9 | To equalize
                                 			 the number of calls sent to each Unity Connection server in the cluster, enter
                                 			 the following command: max-conn <number of
                                    				ports handled by publisher server> |
| Step 10 | To set the
                                 			 dial-peer preference for port group so that the calls are routed first to the
                                 			 subscriber server, then to the publisher server if no ports are available on
                                 			 the subscriber server, enter the following command: preference 2 |
| Step 11 | To enable
                                 			 huntstop, enter the following command: huntstop |
| Step 12 | To exit the
                                 			 global configuration mode, enter the following command: exit |
| Step 13 | To set a
                                 			 dial-peer that prevents Cisco Unified CM Express from hunting beyond the
                                 			 dial-peers for the Unity Connection port groups, entering the following
                                 			 command: configure
                                    				terminal |
| Step 14 | To enter
                                 			 dial-peer configuration mode, enter the following command: dial-peer voice
                                    				<number> voip |
| Step 15 | To set the
                                 			 description for the dial-peer, enter the following command: description <name of
                                    				subscriber server> |
| Step 16 | To set the
                                 			 Unity Connection pilot number for the dial-peer, enter the following command: destination-pattern
                                    				<pilot number> |
| Step 17 | To configure
                                 			 the dial-peer to use Session Initiation Protocol (SIP) for calls, enter the
                                 			 following command: session protocol
                                    				sipv2 |
| Step 18 | To specify the
                                 			 IP address (or DNS name) of the subscriber server, enter the following command: session target {ipv4:<IP
                                    				address>\|dns:<host name>} |
| Step 19 | To enable DTMF
                                 			 relay, enter the following command: dtmf-relay
                                    				rtp-nte |
| Step 20 | To set the
                                 			 codec for calls, enter the following command: codec <codec used for
                                    				calls> |
| Step 21 | To equalize
                                 			 the number of calls sent to each Unity Connection server in the cluster, enter
                                 			 the following command: max-conn <number of
                                    				ports handled by subscriber server> |
| Step 22 | To set the
                                 			 dial-peer preference so that the calls are routed first to the subscriber
                                 			 server, then to the publisher server if no ports are available on the
                                 			 subscriber server, enter the following command: preference 1 |
| Step 23 | To disable
                                 			 huntstop so that the calls use the next available voice messaging port on the
                                 			 subscriber server, then use voice messaging ports on the publisher server if no
                                 			 ports are available on the subscriber server, enter the following command: no huntstop |
| Step 24 | To exit the
                                 			 global configuration mode, enter the following command: exit |

| Step 1 | In Cisco Unity Connection
                              			 Administration, expand Telephony Integrations , then select Phone System . |
|---|---|
| Step 2 | On the Search Phone Systems
                              			 page, under Display Name , select the name of the default phone system. |
| Step 3 | On the Phone System Basics
                              			 page, in the Phone System Name field, enter the descriptive name that you
                              			 want for the phone system. |
| Step 4 | If you want to use this phone system as the default for TRaP
                              			 connections so that administrators and users without voicemail boxes can record
                              			 and playback through the phone in the Unity Connection web applications, check
                              			 the Default TRAP Switch check box . If you want to use another phone
                              			 system as the default for TRaP connections, uncheck this check box. |
| Step 5 | Select Save . |
| Step 6 | On the Phone System Basics page, in the Related Links drop-down
                              			 box, select Add Port Group and select Go . |
| Step 7 | On the New Port Group page, enter the applicable settings and
                              			 select Save. Table 2. Settings for the New Port Group Page Field Value Phone System Select the name of the phone system that
                                          						you entered in Step 3. Create From Select Port Group Template and select SIP in the drop-down box. Display Name Enter a descriptive name for the port group. You can
                                             						  accept the default name or enter the name that you want. Authenticate with SIP Server Check this check box if you want Unity Connection to
                                             						  authenticate with the Cisco Unified CM Express router. Authentication User Name Enter the name that Unity Connection uses to authenticate
                                             						  with the Cisco Unified CM Express router. Authentication Password Enter the password that Unity Connection uses to
                                             						  authenticate with the Cisco Unified CM Express router. Contact Line Name Enter the voice messaging line name (or pilot number) that
                                             						  users use to contact Unity Connection and registers with the Cisco Unified CM
                                             						  Express router. SIP Security Profile Select the SIP security profile that
                                          						Unity Connection uses. Note Cisco Unified CM Express does not support Cisco Unified
                                                      						  CM authentication and encryption. SIP Transport Protocol Select the SIP transport protocol that
                                          						Unity Connection uses. IPv4 Address or Host Name Enter the IP address (or host name) of the Cisco Unified
                                             						  CM Express router that you are integrating with Unity Connection. IPv6 Address or Host Name Do not enter a value in this field. IPv6 is not supported
                                             						  for Cisco Unified CM Express integrations. IP Address or Host Name Enter the IP address (or host name) of the Cisco Unified
                                             						  CM Express router that you are integrating with Unity Connection. Port Enter the IP port of the Cisco Unified CM Express router
                                             						  that you are integrating with Unity Connection. We recommend that you use the
                                             						  default setting. | Field | Value | Phone System | Select the name of the phone system that
                                          						you entered in Step 3. | Create From | Select Port Group Template and select SIP in the drop-down box. | Display Name | Enter a descriptive name for the port group. You can
                                             						  accept the default name or enter the name that you want. | Authenticate with SIP Server | Check this check box if you want Unity Connection to
                                             						  authenticate with the Cisco Unified CM Express router. | Authentication User Name | Enter the name that Unity Connection uses to authenticate
                                             						  with the Cisco Unified CM Express router. | Authentication Password | Enter the password that Unity Connection uses to
                                             						  authenticate with the Cisco Unified CM Express router. | Contact Line Name | Enter the voice messaging line name (or pilot number) that
                                             						  users use to contact Unity Connection and registers with the Cisco Unified CM
                                             						  Express router. | SIP Security Profile | Select the SIP security profile that
                                          						Unity Connection uses. Note Cisco Unified CM Express does not support Cisco Unified
                                                      						  CM authentication and encryption. | Note | Cisco Unified CM Express does not support Cisco Unified
                                                      						  CM authentication and encryption. | SIP Transport Protocol | Select the SIP transport protocol that
                                          						Unity Connection uses. | IPv4 Address or Host Name | Enter the IP address (or host name) of the Cisco Unified
                                             						  CM Express router that you are integrating with Unity Connection. | IPv6 Address or Host Name | Do not enter a value in this field. IPv6 is not supported
                                             						  for Cisco Unified CM Express integrations. | IP Address or Host Name | Enter the IP address (or host name) of the Cisco Unified
                                             						  CM Express router that you are integrating with Unity Connection. | Port | Enter the IP port of the Cisco Unified CM Express router
                                             						  that you are integrating with Unity Connection. We recommend that you use the
                                             						  default setting. |
| Field | Value |
| Phone System | Select the name of the phone system that
                                          						you entered in Step 3. |
| Create From | Select Port Group Template and select SIP in the drop-down box. |
| Display Name | Enter a descriptive name for the port group. You can
                                             						  accept the default name or enter the name that you want. |
| Authenticate with SIP Server | Check this check box if you want Unity Connection to
                                             						  authenticate with the Cisco Unified CM Express router. |
| Authentication User Name | Enter the name that Unity Connection uses to authenticate
                                             						  with the Cisco Unified CM Express router. |
| Authentication Password | Enter the password that Unity Connection uses to
                                             						  authenticate with the Cisco Unified CM Express router. |
| Contact Line Name | Enter the voice messaging line name (or pilot number) that
                                             						  users use to contact Unity Connection and registers with the Cisco Unified CM
                                             						  Express router. |
| SIP Security Profile | Select the SIP security profile that
                                          						Unity Connection uses. Note Cisco Unified CM Express does not support Cisco Unified
                                                      						  CM authentication and encryption. | Note | Cisco Unified CM Express does not support Cisco Unified
                                                      						  CM authentication and encryption. |
| Note | Cisco Unified CM Express does not support Cisco Unified
                                                      						  CM authentication and encryption. |
| SIP Transport Protocol | Select the SIP transport protocol that
                                          						Unity Connection uses. |
| IPv4 Address or Host Name | Enter the IP address (or host name) of the Cisco Unified
                                             						  CM Express router that you are integrating with Unity Connection. |
| IPv6 Address or Host Name | Do not enter a value in this field. IPv6 is not supported
                                             						  for Cisco Unified CM Express integrations. |
| IP Address or Host Name | Enter the IP address (or host name) of the Cisco Unified
                                             						  CM Express router that you are integrating with Unity Connection. |
| Port | Enter the IP port of the Cisco Unified CM Express router
                                             						  that you are integrating with Unity Connection. We recommend that you use the
                                             						  default setting. |
| Step 8 | On the Port Group Basics page, in the Related Links drop-down box,
                              			 select Add Ports and select Go . |
| Step 9 | On the New Port page, enter the following settings and select Save . Table 3. Settings for the New Port Page Field Setting Enabled Check this check box. Number of Ports Enter the number of voice messaging ports that you want to
                                             						  create in this port group. Note For a Unity Connection cluster, you must enter the
                                                      						  total number of voice messaging ports that are used by all Unity Connection
                                                      						  servers. Each port is later assigned to a specific Unity Connection server. Phone System Select the name of the phone system that
                                          						you entered in Step 3. Port Group Select the name of the port group that
                                          						you added in Step 7. Server Select the name Unity Connection server. | Field | Setting | Enabled | Check this check box. | Number of Ports | Enter the number of voice messaging ports that you want to
                                             						  create in this port group. Note For a Unity Connection cluster, you must enter the
                                                      						  total number of voice messaging ports that are used by all Unity Connection
                                                      						  servers. Each port is later assigned to a specific Unity Connection server. | Note | For a Unity Connection cluster, you must enter the
                                                      						  total number of voice messaging ports that are used by all Unity Connection
                                                      						  servers. Each port is later assigned to a specific Unity Connection server. | Phone System | Select the name of the phone system that
                                          						you entered in Step 3. | Port Group | Select the name of the port group that
                                          						you added in Step 7. | Server | Select the name Unity Connection server. |
| Field | Setting |
| Enabled | Check this check box. |
| Number of Ports | Enter the number of voice messaging ports that you want to
                                             						  create in this port group. Note For a Unity Connection cluster, you must enter the
                                                      						  total number of voice messaging ports that are used by all Unity Connection
                                                      						  servers. Each port is later assigned to a specific Unity Connection server. | Note | For a Unity Connection cluster, you must enter the
                                                      						  total number of voice messaging ports that are used by all Unity Connection
                                                      						  servers. Each port is later assigned to a specific Unity Connection server. |
| Note | For a Unity Connection cluster, you must enter the
                                                      						  total number of voice messaging ports that are used by all Unity Connection
                                                      						  servers. Each port is later assigned to a specific Unity Connection server. |
| Phone System | Select the name of the phone system that
                                          						you entered in Step 3. |
| Port Group | Select the name of the port group that
                                          						you added in Step 7. |
| Server | Select the name Unity Connection server. |
| Step 10 | On the Search Ports page, select the display name of the first
                              			 voice messaging port that you created for this phone integration. Note By default, the display names for the voice messaging ports are
                                          				composed of the port group display name followed by incrementing numbers. | Note | By default, the display names for the voice messaging ports are
                                          				composed of the port group display name followed by incrementing numbers. |
| Note | By default, the display names for the voice messaging ports are
                                          				composed of the port group display name followed by incrementing numbers. |
| Step 11 | On the Port Basics page, set the voice messaging port settings as
                              			 applicable. The fields in the following table are the ones that you can change. Table 4. Settings for the Voice Messaging Ports Field Setting Enabled Check this check box to enable the port.
                                          						The port is enabled during normal operation. Uncheck this check box to disable the port. When the port
                                             						  is disabled, calls to the port get a ringing tone but are not answered.
                                             						  Typically, the port is disabled only by the installer during testing. Server (For Unity Connection clusters only) Select the
                                             						  name of the Unity Connection server that you want to handle this port. Assign an equal number of answering and dial-out voice
                                             						  messaging ports to the Unity Connection servers so that they equally share the
                                             						  voice messaging traffic. Answer Calls Check this check box to designate the port for answering
                                             						  calls. These calls can be incoming calls from unidentified callers or from
                                             						  users. Perform Message Notification Check this check box to designate the port for notifying
                                             						  users of messages. Assign Perform Message Notification to the least busy
                                             						  ports. Send MWI Requests Check this check box to designate the port for turning
                                             						  MWIs on and off. Assign Send MWI Requests to the least busy ports. Allow TRAP Connections Check this check box so that users can use the port for
                                             						  recording and playback through the phone in Unity Connection web applications.
                                             						  Assign Allow TRAP Connections to the least busy ports. | Field | Setting | Enabled | Check this check box to enable the port.
                                          						The port is enabled during normal operation. Uncheck this check box to disable the port. When the port
                                             						  is disabled, calls to the port get a ringing tone but are not answered.
                                             						  Typically, the port is disabled only by the installer during testing. | Server | (For Unity Connection clusters only) Select the
                                             						  name of the Unity Connection server that you want to handle this port. Assign an equal number of answering and dial-out voice
                                             						  messaging ports to the Unity Connection servers so that they equally share the
                                             						  voice messaging traffic. | Answer Calls | Check this check box to designate the port for answering
                                             						  calls. These calls can be incoming calls from unidentified callers or from
                                             						  users. | Perform Message Notification | Check this check box to designate the port for notifying
                                             						  users of messages. Assign Perform Message Notification to the least busy
                                             						  ports. | Send MWI Requests | Check this check box to designate the port for turning
                                             						  MWIs on and off. Assign Send MWI Requests to the least busy ports. | Allow TRAP Connections | Check this check box so that users can use the port for
                                             						  recording and playback through the phone in Unity Connection web applications.
                                             						  Assign Allow TRAP Connections to the least busy ports. |
| Field | Setting |
| Enabled | Check this check box to enable the port.
                                          						The port is enabled during normal operation. Uncheck this check box to disable the port. When the port
                                             						  is disabled, calls to the port get a ringing tone but are not answered.
                                             						  Typically, the port is disabled only by the installer during testing. |
| Server | (For Unity Connection clusters only) Select the
                                             						  name of the Unity Connection server that you want to handle this port. Assign an equal number of answering and dial-out voice
                                             						  messaging ports to the Unity Connection servers so that they equally share the
                                             						  voice messaging traffic. |
| Answer Calls | Check this check box to designate the port for answering
                                             						  calls. These calls can be incoming calls from unidentified callers or from
                                             						  users. |
| Perform Message Notification | Check this check box to designate the port for notifying
                                             						  users of messages. Assign Perform Message Notification to the least busy
                                             						  ports. |
| Send MWI Requests | Check this check box to designate the port for turning
                                             						  MWIs on and off. Assign Send MWI Requests to the least busy ports. |
| Allow TRAP Connections | Check this check box so that users can use the port for
                                             						  recording and playback through the phone in Unity Connection web applications.
                                             						  Assign Allow TRAP Connections to the least busy ports. |
| Step 12 | Select Save . |
| Step 13 | Select Next . |
| Step 14 | Repeat Step 11 through Step 13 for all remaining voice messaging
                              			 ports for the phone system. |
| Step 15 | If another phone system integration exists, in Cisco Unity
                              			 Connection Administration, expand Telephony Integrations , then select Trunk . Otherwise, skip to Step 19. |
| Step 16 | On the Search Phone System Trunks page, on the Phone System Trunk
                              			 menu, select New Phone System Trunk . |
| Step 17 | On the New Phone System Trunk page, enter the following settings for
                              			 the phone system trunk and select Save . Table 5. Settings for the Phone System Trunk Field Setting From Phone System Select the display name of the phone
                                          						system that you are creating a trunk for. To Phone System Select the display name of the previously existing phone
                                             						  system that the trunk connects to. Trunk Access Code Enter the extra digits that Unity Connection must dial to
                                             						  transfer calls through the gateway to extensions on the previously existing
                                             						  phone system. | Field | Setting | From Phone System | Select the display name of the phone
                                          						system that you are creating a trunk for. | To Phone System | Select the display name of the previously existing phone
                                             						  system that the trunk connects to. | Trunk Access Code | Enter the extra digits that Unity Connection must dial to
                                             						  transfer calls through the gateway to extensions on the previously existing
                                             						  phone system. |
| Field | Setting |
| From Phone System | Select the display name of the phone
                                          						system that you are creating a trunk for. |
| To Phone System | Select the display name of the previously existing phone
                                             						  system that the trunk connects to. |
| Trunk Access Code | Enter the extra digits that Unity Connection must dial to
                                             						  transfer calls through the gateway to extensions on the previously existing
                                             						  phone system. |
| Step 18 | Repeat Step 16 and Step 17 for all remaining phone system trunks
                              			 that you want to create. |
| Step 19 | In the Related Links drop-down list, select Check Telephony
                                 				Configuration and select Go to confirm the phone system integration settings. If the test is not successful, the Task Execution Results displays
                                 				one or more messages with troubleshooting steps. After correcting the problems,
                                 				test the Unity Connection again. |
| Step 20 | In the Task Execution Results window, select Close . |

| Field | Value |
|---|---|
| Phone System | Select the name of the phone system that
                                          						you entered in Step 3. |
| Create From | Select Port Group Template and select SIP in the drop-down box. |
| Display Name | Enter a descriptive name for the port group. You can
                                             						  accept the default name or enter the name that you want. |
| Authenticate with SIP Server | Check this check box if you want Unity Connection to
                                             						  authenticate with the Cisco Unified CM Express router. |
| Authentication User Name | Enter the name that Unity Connection uses to authenticate
                                             						  with the Cisco Unified CM Express router. |
| Authentication Password | Enter the password that Unity Connection uses to
                                             						  authenticate with the Cisco Unified CM Express router. |
| Contact Line Name | Enter the voice messaging line name (or pilot number) that
                                             						  users use to contact Unity Connection and registers with the Cisco Unified CM
                                             						  Express router. |
| SIP Security Profile | Select the SIP security profile that
                                          						Unity Connection uses. Note Cisco Unified CM Express does not support Cisco Unified
                                                      						  CM authentication and encryption. | Note | Cisco Unified CM Express does not support Cisco Unified
                                                      						  CM authentication and encryption. |
| Note | Cisco Unified CM Express does not support Cisco Unified
                                                      						  CM authentication and encryption. |
| SIP Transport Protocol | Select the SIP transport protocol that
                                          						Unity Connection uses. |
| IPv4 Address or Host Name | Enter the IP address (or host name) of the Cisco Unified
                                             						  CM Express router that you are integrating with Unity Connection. |
| IPv6 Address or Host Name | Do not enter a value in this field. IPv6 is not supported
                                             						  for Cisco Unified CM Express integrations. |
| IP Address or Host Name | Enter the IP address (or host name) of the Cisco Unified
                                             						  CM Express router that you are integrating with Unity Connection. |
| Port | Enter the IP port of the Cisco Unified CM Express router
                                             						  that you are integrating with Unity Connection. We recommend that you use the
                                             						  default setting. |

| Note | Cisco Unified CM Express does not support Cisco Unified
                                                      						  CM authentication and encryption. |
|---|---|

| Field | Setting |
|---|---|
| Enabled | Check this check box. |
| Number of Ports | Enter the number of voice messaging ports that you want to
                                             						  create in this port group. Note For a Unity Connection cluster, you must enter the
                                                      						  total number of voice messaging ports that are used by all Unity Connection
                                                      						  servers. Each port is later assigned to a specific Unity Connection server. | Note | For a Unity Connection cluster, you must enter the
                                                      						  total number of voice messaging ports that are used by all Unity Connection
                                                      						  servers. Each port is later assigned to a specific Unity Connection server. |
| Note | For a Unity Connection cluster, you must enter the
                                                      						  total number of voice messaging ports that are used by all Unity Connection
                                                      						  servers. Each port is later assigned to a specific Unity Connection server. |
| Phone System | Select the name of the phone system that
                                          						you entered in Step 3. |
| Port Group | Select the name of the port group that
                                          						you added in Step 7. |
| Server | Select the name Unity Connection server. |

| Note | For a Unity Connection cluster, you must enter the
                                                      						  total number of voice messaging ports that are used by all Unity Connection
                                                      						  servers. Each port is later assigned to a specific Unity Connection server. |
|---|---|

| Note | By default, the display names for the voice messaging ports are
                                          				composed of the port group display name followed by incrementing numbers. |
|---|---|

| Field | Setting |
|---|---|
| Enabled | Check this check box to enable the port.
                                          						The port is enabled during normal operation. Uncheck this check box to disable the port. When the port
                                             						  is disabled, calls to the port get a ringing tone but are not answered.
                                             						  Typically, the port is disabled only by the installer during testing. |
| Server | (For Unity Connection clusters only) Select the
                                             						  name of the Unity Connection server that you want to handle this port. Assign an equal number of answering and dial-out voice
                                             						  messaging ports to the Unity Connection servers so that they equally share the
                                             						  voice messaging traffic. |
| Answer Calls | Check this check box to designate the port for answering
                                             						  calls. These calls can be incoming calls from unidentified callers or from
                                             						  users. |
| Perform Message Notification | Check this check box to designate the port for notifying
                                             						  users of messages. Assign Perform Message Notification to the least busy
                                             						  ports. |
| Send MWI Requests | Check this check box to designate the port for turning
                                             						  MWIs on and off. Assign Send MWI Requests to the least busy ports. |
| Allow TRAP Connections | Check this check box so that users can use the port for
                                             						  recording and playback through the phone in Unity Connection web applications.
                                             						  Assign Allow TRAP Connections to the least busy ports. |

| Field | Setting |
|---|---|
| From Phone System | Select the display name of the phone
                                          						system that you are creating a trunk for. |
| To Phone System | Select the display name of the previously existing phone
                                             						  system that the trunk connects to. |
| Trunk Access Code | Enter the extra digits that Unity Connection must dial to
                                             						  transfer calls through the gateway to extensions on the previously existing
                                             						  phone system. |

| Step 1 | Set up two test extensions (Phone 1 and Phone 2) on the same
                                 			 phone system that Unity Connection is connected to. |
|---|---|
| Step 2 | Set Phone 1 to forward calls to the Unity Connection pilot number
                                 			 when calls are not answered. Caution The phone system must forward calls to the Unity
                                             				Connection pilot number in no fewer than four rings. Otherwise, the test may
                                             				fail. | Caution | The phone system must forward calls to the Unity
                                             				Connection pilot number in no fewer than four rings. Otherwise, the test may
                                             				fail. |
| Caution | The phone system must forward calls to the Unity
                                             				Connection pilot number in no fewer than four rings. Otherwise, the test may
                                             				fail. |
| Step 3 | In Cisco Unity Connection Administration, expand Users , then select Users . |
| Step 4 | On the Search Users page, select the display name of a user to use
                                 			 for testing. The extension for this user must be the extension for Phone 1. |
| Step 5 | On the Edit User Basics page, uncheck the Set for Self-enrollment at Next Login check box. |
| Step 6 | In the Voice Name field, record a recorded name for the test user. |
| Step 7 | Select Save . |
| Step 8 | On the Edit menu, select Message Waiting Indicators . |
| Step 9 | On the Message Waiting Indicators page, select the message waiting
                                 			 indicator. If no message waiting indication is in the table, select Add New . |
| Step 10 | On the Edit Message Waiting Indicator page, enter the following
                                 			 settings. Table 6. Table 15 Settings for the Edit MWI Page Field Setting Enabled Check this check box to enable MWIs for the test user. Display Name Accept the default or enter a different name. Inherit User’s Extension Check this check box to enable MWIs on Phone 1. | Field | Setting | Enabled | Check this check box to enable MWIs for the test user. | Display Name | Accept the default or enter a different name. | Inherit User’s Extension | Check this check box to enable MWIs on Phone 1. |
| Field | Setting |
| Enabled | Check this check box to enable MWIs for the test user. |
| Display Name | Accept the default or enter a different name. |
| Inherit User’s Extension | Check this check box to enable MWIs on Phone 1. |
| Step 11 | Select Save . |
| Step 12 | On the Edit menu, select Transfer Rules . |
| Step 13 | On the Transfer Rules page, select the active transfer rule. |
| Step 14 | On the Edit Transfer Rule page, under Transfer Action , select Extension and enter the extension of Phone 1. |
| Step 15 | In the Transfer Type field, select Release to Switch . |
| Step 16 | Select Save. |
| Step 17 | Minimize the Cisco Unity Connection Administration window. Do not close the Cisco Unity Connection Administration window
                                    				because you use it again in a later procedure. |
| Step 18 | Sign in to the Real-Time Monitoring Tool (RTMT). |
| Step 19 | On the Unity Connection menu, select Port Monitor . The Port Monitor tool appears in the right pane. |
| Step 20 | In the right pane, select Start Polling . The Port Monitor displays which port is
                                 			 handling the calls that you make. |

| Caution | The phone system must forward calls to the Unity
                                             				Connection pilot number in no fewer than four rings. Otherwise, the test may
                                             				fail. |
|---|---|

| Field | Setting |
|---|---|
| Enabled | Check this check box to enable MWIs for the test user. |
| Display Name | Accept the default or enter a different name. |
| Inherit User’s Extension | Check this check box to enable MWIs on Phone 1. |

| Step 1 | From Phone 2, enter the access code necessary to get an outside
                                 			 line, then enter the number outside callers use to dial directly to Unity
                                 			 Connection. |
|---|---|
| Step 2 | In the Port Monitor, note which port handles this call. |
| Step 3 | When you hear the opening greeting, enter the extension for Phone
                                 			 1. Hearing the opening greeting means that the port is configured correctly. |
| Step 4 | Confirm that Phone 1 rings and that you hear a ringback tone on
                                 			 Phone 2. Hearing a ring back tone means that Unity Connection correctly
                                 			 released the call and transferred it to Phone 1. |
| Step 5 | Leaving Phone 1 unanswered, confirm that the state of the port
                                 			 handling the call changes to “Idle.” This state means that release transfer is
                                 			 successful. |
| Step 6 | Confirm that, after the number of rings that the phone system is
                                 			 set to wait, the call is forwarded to Unity Connection and that you hear the
                                 			 greeting for the test user. Hearing the greeting means that the phone system
                                 			 forwarded the unanswered call and the call-forward information to Unity
                                 			 Connection, which correctly interpreted the information. |
| Step 7 | On the Port Monitor, note which port handles this call. |
| Step 8 | Leave a message for the test user and hang up Phone 2. |
| Step 9 | In the Port Monitor, confirm that the state of the port handling
                                 			 the call changes to “Idle.” This state means that the port was successfully
                                 			 released when the call ended. |
| Step 10 | Confirm that the MWI on Phone 1 is activated. The activated MWI
                                 			 means that the phone system and Unity Connection are successfully integrated
                                 			 for turning on MWIs. |

| Step 1 | From Phone 1, enter the internal pilot number for Unity
                                 			 Connection. |
|---|---|
| Step 2 | When asked for your password, enter the password for the test
                                 			 user. Hearing the request for your password means that the phone system sent
                                 			 the necessary call information to Unity Connection, which correctly interpreted
                                 			 the information. |
| Step 3 | Confirm that you hear the recorded name for the test user (if you
                                 			 did not record a name for the test user, you hear the extension number for
                                 			 Phone 1). Hearing the recorded name means that Unity Connection correctly
                                 			 identified the user by the extension. |
| Step 4 | Listen to the message. |
| Step 5 | After listening to the message, delete the message. |
| Step 6 | Confirm that the MWI on Phone 1 is deactivated. The deactivated
                                 			 MWI means that the phone system and Unity Connection are successfully
                                 			 integrated for turning off MWIs. |
| Step 7 | Hang up Phone 1. |
| Step 8 | On the Port Monitor, confirm that the state of the port handling
                                 			 the call changes to “Idle.” This state means that the port was successfully
                                 			 released when the call ended. |

| Step 1 | In Cisco Unity Connection Administration, on the Edit Transfer
                                 			 Rule page for the test user, in the Transfer Type field, select Supervise Transfer . |
|---|---|
| Step 2 | In the Rings to Wait For field, enter 3 . |
| Step 3 | Select Save . |
| Step 4 | Minimize the Cisco Unity Connection Administration window. Do not close the Cisco Unity Connection Administration window
                                    				because you use it again in a later procedure. |