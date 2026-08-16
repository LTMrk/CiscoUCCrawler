---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-connection-15-integration-timg-b-15cucinttimg-b-14cucinttimg-chapter-01-html-1a4cb80e08
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/15/integration/timg/b_15cucinttimg/b_14cucinttimg_chapter_01.html
retrieved_at: 2026-08-16T18:47:26.150426+00:00
---

TIMG Integration Guide for Cisco Unity Connection Release 15

# TIMG Integration Guide for Cisco Unity Connection Release 15

Updated: December 18, 2023

Chapter: Planning the Usage of Voice Messaging Ports in Cisco Unity
	 Connection

## Chapter: Planning the Usage of Voice Messaging Ports in Cisco Unity
	 Connection

# Planning the Usage of Voice Messaging Ports in Cisco Unity
                     	 Connection

## Planning the Usage of Voice Messaging Ports in Cisco Unity
                        	 Connection

### Planning the Port Setup

Before programming the phone system, you need to plan how the voice messaging ports used by Cisco Unity Connection. The following
                                 considerations affect the programming for the phone system (for example, setting up the hunt group or call forwarding for
                                 the voice messaging ports):

The number of voice messaging ports installed.

For a Unity Connection cluster, each server must have enough ports to handle all voice messaging traffic in case the other
                                 server stops functioning.

The number of voice messaging ports that answer calls.

The number of voice messaging ports that only dial out, for example, to send message notification, to set message waiting
                                       indicators (MWIs), and to make telephone record and playback (TRAP) connections.

The following table describes the voice messaging port settings in Unity Connection that can be set on Telephony Integrations >
                                 Port of Cisco Unity Connection Administration.

Field

Considerations

Enabled

Check this check box to enable the port. The port is enabled during normal operation.

Uncheck this check box to disable the port. When the port is disabled, calls to the port get a ringing tone but are not answered.
                                             Typically, the port is disabled only by the installer during testing.

Extension

Enter the extension for the port as assigned on the phone system.

Answer Calls

Check this check box to designate the port for answering calls. These calls can be incoming calls from unidentified callers
                                             or from users.

Perform Message Notification

Check this check box to designate the port for notifying users of messages. Assign Perform Message Notification to the least
                                             busy ports.

Send MWI Requests

(not used by serial integrations)

For serial integrations, uncheck this check box. Otherwise, the integration may not function correctly.

For in-band integrations, check this check box to designate the port for turning MWIs on and off. Assign Send MWI Requests
                                             to the least busy ports.

Allow TRAP Connections

Check this check box so that users can use the phone as a recording and playback device in Unity Connection web applications.
                                             Assign Allow TRAP Connections to the least busy ports.

Outgoing Hunt Order

Enter the priority order in which Unity Connection use the ports when dialing out (for example, if the Perform Message Notification,
                                             Send MWI Requests, or Allow TRAP Connections check box is checked). The highest numbers are used first. However, when multiple
                                             ports have the same Outgoing Hunt Order number, Unity Connection use the port that has been idle the longest.

### Determining the Number of Voice Messaging Ports

The following tasks describe the process for determining the number of voice messaging ports for Cisco Unity Connection to
                              install, answer call and dial out calls:

For determining the number of voice messaging ports to Install, see “Voice Messaging Ports to Install” section on page 2-2 .

For determining the number of voice messaging ports to Answer Calls, see “Voice Messaging Ports to Answer Calls” section on page 2-3 .

For determining the number of voice messaging ports to Dial Out, see “Voice Messaging Ports that Dial Out” section on page 2-3 .

#### Voice Messaging
                              	 Ports to Install

The number of
                                 		voice messaging ports to install depends on numerous factors, including:

The number of calls Unity Connection answer when call traffic is
                                       			 at its peak.

The expected length of each message that callers record and that
                                       			 users listen.

The number of users.

The number of ports that be set to dial out only.

The number of calls made for message notification.

The number of MWIs activated when call traffic is at its peak.

The number of TRAP connections needed when call traffic is at
                                       			 its peak. (TRAP connections are used by Unity Connection web applications to
                                       			 play back and record over the phone).

The number of calls use the automated attendant and call
                                       			 handlers when call traffic is at its peak.

Whether a Unity Connection cluster is configured. For
                                       			 considerations, see the " Considerations
                                          				for a Unity Connection Cluster " section.

It is best to install only the number of voice messaging ports
                                 		that are needed so that system resources are not allocated to unused ports.

#### Voice Messaging
                              	 Ports to Answer Calls

The
                                 		calls that the voice messaging ports answer can be incoming calls from
                                 		unidentified callers or from users. Typically, the voice messaging ports that
                                 		answer calls are the busiest.

You can set voice messaging ports to both answer calls and to
                                 		dial out (for example, to send message notifications). However, when the voice
                                 		messaging ports perform more than one function and are very active (for
                                 		example, answering many calls), the other functions may be delayed until the
                                 		voice messaging port is free (for example, message notifications cannot be sent
                                 		until there are fewer calls to answer). For best performance, dedicate certain
                                 		voice messaging ports for only answering incoming calls, and dedicate other
                                 		ports for only dialing out. Separating these port functions eliminates the
                                 		possibility of a collision, in which an incoming call arrives on a port at the
                                 		same time that Unity Connection takes the port off-hook to dial out.

If your system is configured for a Unity Connection cluster, see
                                 		the " Considerations
                                    		  for a Unity Connection Cluster " section..

#### Voice Messaging
                              	 Ports that Dial Out

Ports
                                 		that only dial out and do not answer calls can do one or more of the following:

Notify users by phone, pager, or email of messages that have
                                       			 arrived.

Turn MWIs on and off for user extensions.

Make a TRAP connection so that users can use the phone as a
                                       			 recording and playback device in Cisco Unity Connection web applications.

Typically, these voice messaging ports are the least busy ports.

If your system is configured for a Unity Connection cluster, see
                                 		the " Considerations
                                    		  for a Unity Connection Cluster " section.

Caution

### Considerations for a Unity Connection Cluster

If your system is configured for a Unity Connection cluster, consider how the voice messaging ports used in different scenarios.

#### When Both Unity Connection Servers are Functioning

The number of ports provisioned on the phone system is the same as the number of voice messaging ports on each Unity Connection
                                       server.

The TIMG units are configured to send incoming calls first to the subscriber server, then to the publisher server if no answering
                                       ports are available on the subscriber server.

Both Unity Connection servers are active and handle voice messaging traffic for the system.

The number of voice messaging ports on each Unity Connection server must be sufficient to handle all of the voice messaging
                                       traffic for the system (answering calls and dialing out) when the other Unity Connection server stops functioning.

If both Unity Connection servers must be functioning to handle the voice messaging traffic, the system do not have sufficient
                                 capacity when one of the servers stops functioning.

Each Unity Connection server must have voice messaging ports that answer calls and that can dial out (for example, to set
                                       MWIs).

#### When Only One Unity Connection Server is Functioning

TIMG units send all calls to the functioning Unity Connection server.

The functioning Unity Connection server receives all voice messaging traffic for the system.

The number of voice messaging ports that are assigned to the functioning Unity Connection server must be sufficient to handle
                                       all of the voice messaging traffic for the system (answering calls and dialing out).

The functioning Unity Connection server must have voice messaging ports that answer calls and that can dial out (for example,
                                       to set MWIs).

If the functioning Unity Connection server does not have voice messaging ports for answering calls, the system is not able
                                 to answer incoming calls. Similarly, if the functioning Unity Connection server does not have voice messaging ports for dialing
                                 out, the system is not able to dial out (for example, to set MWIs).

| Field | Considerations |
|---|---|
| Enabled | Check this check box to enable the port. The port is enabled during normal operation. Uncheck this check box to disable the port. When the port is disabled, calls to the port get a ringing tone but are not answered.
                                             Typically, the port is disabled only by the installer during testing. |
| Extension | Enter the extension for the port as assigned on the phone system. |
| Answer Calls | Check this check box to designate the port for answering calls. These calls can be incoming calls from unidentified callers
                                             or from users. |
| Perform Message Notification | Check this check box to designate the port for notifying users of messages. Assign Perform Message Notification to the least
                                             busy ports. |
| Send MWI Requests (not used by serial integrations) | For serial integrations, uncheck this check box. Otherwise, the integration may not function correctly. For in-band integrations, check this check box to designate the port for turning MWIs on and off. Assign Send MWI Requests
                                             to the least busy ports. |
| Allow TRAP Connections | Check this check box so that users can use the phone as a recording and playback device in Unity Connection web applications.
                                             Assign Allow TRAP Connections to the least busy ports. |
| Outgoing Hunt Order | Enter the priority order in which Unity Connection use the ports when dialing out (for example, if the Perform Message Notification,
                                             Send MWI Requests, or Allow TRAP Connections check box is checked). The highest numbers are used first. However, when multiple
                                             ports have the same Outgoing Hunt Order number, Unity Connection use the port that has been idle the longest. |

| Caution | In
                                          		programming the phone system, do not send calls to voice messaging ports in
                                          		Cisco Unity Connection that cannot answer calls (voice messaging ports that are
                                          		not set to Answer Calls). For example, if a voice messaging port is set only to
                                          		Perform Message Notification, do not send calls to it. |
|---|---|