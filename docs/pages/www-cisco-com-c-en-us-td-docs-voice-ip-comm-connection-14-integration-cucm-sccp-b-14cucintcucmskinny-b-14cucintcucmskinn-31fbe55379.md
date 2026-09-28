---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-connection-14-integration-cucm-sccp-b-14cucintcucmskinny-b-14cucintcucmskinn-31fbe55379
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/14/integration/cucm_sccp/b_14cucintcucmskinny/b_14cucintcucmskinny_chapter_011.html
retrieved_at: 2026-08-16T18:36:09.480925+00:00
---

Cisco Unified Communications Manager SCCP Integration Guide for Cisco Unity Connection Release 14

# Cisco Unified Communications Manager SCCP Integration Guide for Cisco Unity Connection Release 14

Updated: November 25, 2020

Chapter: Configuring Voice
	 Messaging Ports Configuration for a Unity Connection Cluster

## Chapter: Configuring Voice
	 Messaging Ports Configuration for a Unity Connection Cluster

# Configuring Voice
                     	 Messaging Ports Configuration for a Unity Connection Cluster

## Configuring Voice
                        	 Messaging Ports Configuration for a Unity Connection Cluster

### Introduction

This chapter provides information for configuring voice
                              		messaging ports for a Unity Connection cluster.

The Cisco Unity Connection cluster feature provides high
                              		availability Unity Connection voice messaging through two Unity Connection
                              		servers.

For details on the Unity Connection cluster feature, see the Configuring Cisco Unity Connection Cluster chapter of the Install, Upgrade, and Maintenance Guide for Cisco Unity Connection, Release 15 available at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/15/install_upgrade/guide/b_15cuciumg.html .

### Voice Messaging Port for Unity Connection Cluster

For a Unity Connection cluster, you must know how the voice messaging ports function—which ports answer calls and which ports
                                 dial out (for setting MWIs and for sending message notifications). Depending on the function of the ports, you assign them
                                 to the applicable server in the Unity Connection cluster:

Answering ports

Beginning with the answering port that has the lowest number in its display name, assign half the answering ports to the subscriber
                                             server so that the subscriber server answer most incoming calls. Assign the remaining answering ports to the publisher server.

Dial-out ports (for MWIs and notifications)

Beginning with the dial-out port that has the lowest number in its display name, assign half the dial-out ports to the primary
                                             server so that the primary server handle MWIs and notification calls. Assign the remaining dial-out ports to the subscriber
                                             server.

For example, an eight-port system with six answering ports and two dial-out ports can be configured as follows.

Port Function

Port Display Name

Server

Answering

UCM1-001

Subscriber

UCM1-002

Subscriber

UCM1-003

Subscriber

UCM1-004

Publisher

UCM1-005

Publisher

UCM1-006

Publisher

Dialing out

UCM1-007

Publisher

UCM1-008

Subscriber

Under normal conditions, the Unity Connection cluster handles calls in the following manner:

The subscriber server answer most incoming calls. If no answering ports on the subscriber server are available, the publisher
                                       server answer calls.

The publisher server dial out for MWIs and notifications. If no dial-out ports on the publisher server are available, the
                                       subscriber server dial out for MWIs and notifications.

### Voice Messaging
                           	 Ports Configuration for a Unity Connection Cluster

Step 1

In Cisco
                                          			 Unity Connection Administration, expand Telephony
                                             				Integrations and select Port .

Step 2

On the Search
                                          			 Ports page, select the display name of the first voice messaging port in the
                                          			 Unity Connection cluster.

Caution

Step 3

On the Port
                                          			 Basics page, in the Server field, select the name of the applicable Unity
                                          			 Connection server depending on the port function. For details, see the Voice
                                             				Messaging Ports for Unity Connection Cluster .

Step 4

Select Save .

Step 5

Select Next .

Step 6

Repeat Step 3 through Step 5 for all remaining voice messaging ports in the Unity Connection cluster.

| Answering ports | Beginning with the answering port that has the lowest number in its display name, assign half the answering ports to the subscriber
                                             server so that the subscriber server answer most incoming calls. Assign the remaining answering ports to the publisher server. |
|---|---|
| Dial-out ports (for MWIs and notifications) | Beginning with the dial-out port that has the lowest number in its display name, assign half the dial-out ports to the primary
                                             server so that the primary server handle MWIs and notification calls. Assign the remaining dial-out ports to the subscriber
                                             server. |

| Port Function | Port Display Name | Server |
|---|---|---|
| Answering | UCM1-001 | Subscriber |
| UCM1-002 | Subscriber |
| UCM1-003 | Subscriber |
| UCM1-004 | Publisher |
| UCM1-005 | Publisher |
| UCM1-006 | Publisher |
| Dialing out | UCM1-007 | Publisher |
| UCM1-008 | Subscriber |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | In Cisco
                                          			 Unity Connection Administration, expand Telephony
                                             				Integrations and select Port . |  |
| Step 2 | On the Search
                                          			 Ports page, select the display name of the first voice messaging port in the
                                          			 Unity Connection cluster. | Caution All ports for all Unity Connection servers must appear on the
                                                      				Search Ports page. Otherwise, the Unity Connection cluster has not been
                                                      				correctly configured and does not function correctly. | Caution | All ports for all Unity Connection servers must appear on the
                                                      				Search Ports page. Otherwise, the Unity Connection cluster has not been
                                                      				correctly configured and does not function correctly. |
| Caution | All ports for all Unity Connection servers must appear on the
                                                      				Search Ports page. Otherwise, the Unity Connection cluster has not been
                                                      				correctly configured and does not function correctly. |
| Step 3 | On the Port
                                          			 Basics page, in the Server field, select the name of the applicable Unity
                                          			 Connection server depending on the port function. For details, see the Voice
                                             				Messaging Ports for Unity Connection Cluster . |  |
| Step 4 | Select Save . |  |
| Step 5 | Select Next . |  |
| Step 6 | Repeat Step 3 through Step 5 for all remaining voice messaging ports in the Unity Connection cluster. |  |

| Caution | All ports for all Unity Connection servers must appear on the
                                                      				Search Ports page. Otherwise, the Unity Connection cluster has not been
                                                      				correctly configured and does not function correctly. |
|---|---|