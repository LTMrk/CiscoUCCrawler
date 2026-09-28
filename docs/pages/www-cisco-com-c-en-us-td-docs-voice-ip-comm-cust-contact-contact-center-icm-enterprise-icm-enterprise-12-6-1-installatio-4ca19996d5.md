---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-icm-enterprise-icm-enterprise-12-6-1-installatio-4ca19996d5
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/icm_enterprise/icm_enterprise_12_6_1/installation/guide/ucce_b_cti-os-system-manager-guide12-6-1/ucce_b_cti-os-system-manager-guide12-5_chapter_01001.html
retrieved_at: 2026-08-16T20:04:32.923378+00:00
---

CTI OS System Manager Guide for Cisco Unified ICM, Release 12.6(1)

# CTI OS System Manager Guide for Cisco Unified ICM, Release 12.6(1)

Updated: May 12, 2021

Chapter: Startup, Shutdown, and Failover

## Chapter: Startup, Shutdown, and Failover

# Startup, Shutdown, and Failover

## Unified CCE Service
                        	 Control

The Unified
                              		  CCE Service Control application is an interface into the Windows platform's
                              		  service control manager, which starts and stops services.

CTI OS is not
                                             				displayed in the Service Manager in the ICM Websetup page.

When the
                              		  CTI OS service starts, it launches processes listed in the following table.

Process Name

Process
                                          					 Description

Runs In
                                          					 Console Window

CtiosServerNode

The main CTI
                                          					 OS Server process. This process manages all CTI OS objects and listens for and
                                          					 manages client connections.

Yes

CTIOSTrace

The CTI OS
                                          					 tracing utility. This process uses the Unified ICM Event Management System
                                          					 (EMS) to trace server messages to local log files in EMS format.

No

NM

The Unified ICM NodeManager (fault tolerance manager). Each Unified ICM service is started by NodeManager, and NodeManager
                                          restarts any processes that were terminated unusually.

No

NMM

The Unified
                                          					 ICM NodeManagerManager (system fault tolerance). Each Unified ICM Node (e.g.
                                          					 CTI OS) starts up a NMM process to handle system-level faults. In the event of
                                          					 a unrecoverable system fault, NMM restarts the host computer.

No

## CTI OS Failover

The server processes are managed by a fault tolerance/recovery platform called NodeManager. NodeManager creates and monitors
                           each process running as part of the CTI OS service, and automatically restarts processes that were terminated unusually.

### Failover of CTI OS Related Components

CTI OS handles failover of related components as described in the following sections.

Caution

The CTI OS desktop can buffer actions if an agent clicks buttons during a failover. Those actions can then take effect when
                                          the failover completes. You should warn agents not to click desktop buttons during a failover.

#### IP Phones

If an IP phone goes out of service, CTI OS sends an event to all soft phones associated with the IP phone that their IP phone
                                    is out of service. In addition, the affected softphones display the message "Offline." When the IP phone is back in service, agents must manually log in.

#### Switches

If a switch goes out of service, CTI OS sends an event to all softphones associated with the switch that the switch is offline.
                                    In addition, the affected softphones display the message "Offline." When the switch is back in service, agents must manually sign in.

#### Peripheral Gateway

Because the Peripheral Gateway (PG) is a fault-tolerant process pair, CTI OS is not affected if the PG merely switches active
                                    sides. If the PG goes offline, CTI OS sends an "Offline" message to each softphone client.

#### CTI Server Failure

On a CTI Server failure, the CTI OS Server usually reconnects almost immediately to the redundant CTI Server. If reconnection
                                    to the redundant CTI Server is not possible, the CTI OS Server sends a failure response to any requests made to the CTI Server.

In addition, CTI OS sends an event message to all softphone clients. On receipt of this message, the softphone clients display
                                    an "Offline" message.

When the CTI Server comes back online, CTI OS performs a snapshot of all agents, devices, and calls to reestablish state information.

#### CTI OS Server Failure

On a CTI OS Server failure, CTI OS disconnects all softphones from the failed CTI OS Server. These softphones attempt to reconnect
                                    automatically to another CTI OS Server; if reconnection is not possible, CTI OS sends an event message to all softphone clients.
                                    On receipt of this message, the softphone clients display an "Offline" message.

NodeManager restarts the CTI OS Server. When the CTI OS Server process comes back online, CTI OS performs a snapshot of all
                                    agents, devices, and calls to reestablish state information.

| Note | CTI OS is not
                                             				displayed in the Service Manager in the ICM Websetup page. |
|---|---|

| Process Name | Process
                                          					 Description | Runs In
                                          					 Console Window |
|---|---|---|
| CtiosServerNode | The main CTI
                                          					 OS Server process. This process manages all CTI OS objects and listens for and
                                          					 manages client connections. | Yes |
| CTIOSTrace | The CTI OS
                                          					 tracing utility. This process uses the Unified ICM Event Management System
                                          					 (EMS) to trace server messages to local log files in EMS format. | No |
| NM | The Unified ICM NodeManager (fault tolerance manager). Each Unified ICM service is started by NodeManager, and NodeManager
                                          restarts any processes that were terminated unusually. | No |
| NMM | The Unified
                                          					 ICM NodeManagerManager (system fault tolerance). Each Unified ICM Node (e.g.
                                          					 CTI OS) starts up a NMM process to handle system-level faults. In the event of
                                          					 a unrecoverable system fault, NMM restarts the host computer. | No |

| Caution | The CTI OS desktop can buffer actions if an agent clicks buttons during a failover. Those actions can then take effect when
                                          the failover completes. You should warn agents not to click desktop buttons during a failover. |
|---|---|