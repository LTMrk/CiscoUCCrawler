---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-connection-15-integration-cucm-sccp-b-15cucintcucmskinny-b-14cucintcucmskinn-df17664362
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/15/integration/cucm_sccp/b_15cucintcucmskinny/b_14cucintcucmskinny_chapter_01.html
retrieved_at: 2026-08-16T18:28:54.334528+00:00
---

Cisco Unified Communications Manager SCCP Integration Guide for Cisco Unity Connection Release 15

# Cisco Unified Communications Manager SCCP Integration Guide for Cisco Unity Connection Release 15

Updated: December 18, 2023

Chapter: Planning the Voice Messaging
	 Ports

## Chapter: Planning the Voice Messaging
	 Ports

# Planning the Voice Messaging
                     	 Ports

## Planning the Voice Messaging
                        	 Ports

### Planning the Port Setup

Before programming the phone system, you need to plan how the voice messaging ports are going to be used by Cisco Unity Connection.
                              The following considerations affect the programming for the phone system (for example, setting up the hunt group or call forwarding
                              for the voice messaging ports):

The number of voice messaging ports installed.

For a Unity Connection cluster, each Unity Connection server must have enough ports to handle all voice messaging traffic
                              in case the other server stops functioning. The Cisco Unified CM server must have enough ports installed for all Unity Connection
                              servers.

The number of voice messaging ports that answer calls.

The number of voice messaging ports that only dial out, for example, to send message notification, to set message waiting
                                    indicators (MWIs), and to make telephone record and playback (TRAP) connections.

### Determining the
                           	 Number of Voice Messaging Ports

The following
                              		tasks describe the process for determining the number of voice messaging ports
                              		for Cisco Unity Connection to install, answer call and dial out calls:

For determining the number of voice messaging ports to Install,
                                    			 see “ Voice Messaging Ports to Install ” section.

For determining the number of voice messaging ports to Answer
                                    			 Calls, see “ Voice Messaging Ports to Answer Calls ”
                                    			 section.

For determining the number of voice messaging ports to Dial Out,
                                    			 see “ Voice Messaging Ports to Dial Out ” section.

#### Voice Messaging
                              	 Ports to Install

The number of voice messaging ports to install depends on
                                 		numerous factors, including:

The number of calls Unity Connection answers when call traffic
                                       			 is at its peak.

The expected length of each message that callers record and that
                                       			 users listen to.

The number of users.

The number of ports that are set to dial out only.

The number of calls made for message notification.

The number of MWIs activated when call traffic is at its peak.

The number of TRAP connections needed when call traffic is at
                                       			 its peak. (TRAP connections are used by Unity Connection web applications to
                                       			 play back and record over the phone.)

The number of calls that use the automated attendant and call
                                       			 handlers when call traffic is at its peak.

It is best to install only the number of voice messaging ports
                                 		that are needed so that system resources are not allocated to unused ports.

If your system is configured for a Cisco Unity Connection
                                 		cluster, see the Considerations for Unity Connection Cluster .

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
                                 		same time that Unity Connection takes the port off-hook to dial out.

If your system is configured for a Cisco Unity Connection
                                 		cluster, see the Considerations for Unity Connection Cluster .

#### Voice Messaging
                              	 Ports to Dial Out

Ports
                                 		that only dial out and do not answer calls can do one or more of the following:

Notify users by phone, pager, or email of messages that have
                                       			 arrived.

Turn MWIs on and off for user extensions.

Make a TRAP Unity Connection so that users can use the phone as
                                       			 a recording and playback device in Unity Connection web applications.

Typically, these voice messaging ports are the least busy ports.

If your system is configured for a Cisco Unity Connection
                                 		cluster, see the Considerations for Unity Connection Cluster .

Caution

In programming the phone system, do not send calls to voice
                                             		  messaging ports in Unity Connection that cannot answer calls (voice messaging
                                             		  ports that are not set to Answer Calls). For example, if a voice messaging port
                                             		  is set only to Send MWI Requests, do not send calls to it.

### Considerations for a Unity Connection Cluster

If your system is configured for a Unity Connection cluster, consider how the voice messaging ports are used in different
                              scenarios.

#### When Both Unity Connection Servers are Functioning

The phone system is provisioned with twice the number SCCP voice mail port devices needed to handle the voice messaging traffic.

A hunt group is configured to send incoming calls first to the subscriber server, then to the publisher server if no answering
                                       ports are available on the subscriber server.

Both Unity Connection servers are active and handle voice messaging traffic for the system.

In Cisco Unity Connection Administration, the voice messaging ports are assigned in the following manner:

The subscriber server answers most incoming calls for the system.

The publisher server handles most dial-out calls (MWI requests and notifications).

This guide directs you to assign the voice messaging ports to their specific Unity Connection server at the applicable time.

The voice messaging ports on both the servers are registered with the phone system.

The number of voice messaging ports that are assigned to one Unity Connection server must be sufficient to handle all of the
                                       voice messaging traffic for the system (answering calls and dialing out) when the other Unity Connection server stops functioning.

If both the Unity Connection servers are functioning to handle the voice messaging traffic, the system does not have sufficient
                                 capacity when one of the servers stops functioning.

Each Unity Connection server is assigned half the total number of voice messaging ports.

If all the voice messaging ports are assigned to one Unity Connection server, the other Unity Connection server is not able
                                 to answer calls or to dial out.

Each Unity Connection server must be assigned voice messaging ports that answer calls and that can dial out (for example,
                                       to set MWIs).

#### When Only One
                              	 Unity Connection Server is Functioning

The SCCP voice mail port devices that have stopped functioning
                                       			 on the phone system are unregistered from the voice messaging ports of Unity
                                       			 Connection server.

The hunt group on the phone system sends all calls to the
                                       			 functioning Unity Connection server.

The functioning Unity Connection server receives all voice
                                       			 messaging traffic for the system.

The number of voice messaging ports that are assigned to the
                                       			 functioning Unity Connection server must be sufficient to handle all of the
                                       			 voice messaging traffic for the system (answering calls and dialing out).

The functioning Unity Connection server must have voice
                                       			 messaging ports that answer calls and that can dial out (for example, to set
                                       			 MWIs).

If the functioning Unity Connection server does not have voice
                                 		messaging ports for answering calls, the system is not able to answer incoming
                                 		calls. Similarly, if the functioning Unity Connection server does not have
                                 		voice messaging ports for dialing out, the system is not able to dial out (for
                                 		example, to set MWIs).

All the ports for all
                                 		Unity Connection servers must appear on the Search Ports page. Otherwise, the
                                 		Unity Connection cluster has not been correctly configured and does not
                                 		function correctly.

| Caution | In programming the phone system, do not send calls to voice
                                             		  messaging ports in Unity Connection that cannot answer calls (voice messaging
                                             		  ports that are not set to Answer Calls). For example, if a voice messaging port
                                             		  is set only to Send MWI Requests, do not send calls to it. |
|---|---|