---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-icm-enterprise-icm-enterprise-12-5-1-installatio-9f275e4288
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/icm_enterprise/icm_enterprise_12_5_1/installation/guide/ucce_b_pre-installation-planning-guide-for-cisco/ucce_b_pre-installation-planning-guide-for-cisco_chapter_0101.html
retrieved_at: 2026-08-22T00:11:06.499610+00:00
---

Pre-installation Planning Guide for Cisco Unified Intelligent Contact Management, Release 12.5(1)

# Pre-installation Planning Guide for Cisco Unified Intelligent Contact Management, Release 12.5(1)

Updated: February 4, 2020

Chapter: Peripheral Gateway
	 Configurations

## Chapter: Peripheral Gateway
	 Configurations

# Peripheral Gateway
                     	 Configurations

As part of planning
                        		for ACDs and PGs, you need to decide whether your Peripheral Gateways will be
                        		simplexed or duplexed. Simplexed means that one PG is used. Duplexed means that
                        		two identical PGs are used, one as a backup system. (Both PGs run
                        		simultaneously, with some processes active on both PGs. See the discussion in Peripheral Gateway Fault Tolerance .)

The following figure
                        		shows examples of simplexed and duplexed contact center configurations.
                        		Typically, duplexed PGs are installed for fault tolerance.

The Peripheral Gateway
                        		reads information from one or more peripherals at a contact center and sends
                        		status information back to the Unified ICM CallRouter. A peripheral can be an
                        		ACD, VRU, PBX, or other device that distributes calls within the contact
                        		center. If the Unified ICM system is performing post-routing, the PG also sends
                        		route requests to the CallRouter and receives routing instructions in response.

## Peripheral Gateway Fault Tolerance

Duplexed PGs are implemented to provide fault tolerance in
                              		  Unified ICM software communication with peripherals. The duplexed PGs use a
                              		  private network. The PG private network synchronizes certain processes within a
                              		  duplexed PG pair. It also conducts "heartbeat detection" , a process by which each PG sends a
                              		  heartbeat packet every 100ms to keep track of the "health" of the other PG.

PGs use a combination of the hot standby and synchronization
                              		  approaches to fault tolerance. In the hot standby approach, one set of
                              		  processes is called the primary, and the other is called the backup. In this
                              		  model, the primary process performs the work at hand while the backup process
                              		  is idle. In the event of a primary process failure, the backup process is
                              		  activated and takes over. In a duplexed PG system, the Peripheral Interface
                              		  Manager (PIM) processes use the hot standby approach to fault tolerance.

In the synchronization approach, the critical process is duplicated on
                              		  separate computers. There is no primary and backup. Both process sets run in a
                              		  synchronized fashion, processing duplicate input and producing duplicate
                              		  output. Each synchronized process is an equal peer. Cisco refers to these equal
                              		  peers as a synchronized process pair. In a duplexed PG system, the Open
                              		  Peripheral Controller (OPC) process operates as a synchronized process pair.

The following figure shows how to use hot standby and synchronization in a duplexed Peripheral Gateway.

The OPC processes communicate with each other through a private
                              		  network connection and the Cisco Message Delivery Service (MDS). The MDS
                              		  provides a synchronizer service which combines the input streams from the PIMs
                              		  and PG Agents on both sides of the PG to ensure that both OPC processes see
                              		  exactly the same input.

The OPC process activates PIMs and PG Agents on each side of the
                              		  duplexed PG. The OPC process also supplies uniform message sets from various PG
                              		  types to the Unified ICM central controller.

The PIMs manage the interface between different types of ACDs and the
                              		  OPC. PIMs are duplicated on each side of the system and operate in hot standby
                              		  mode. A PIM can be active on either side of the duplexed PG, but not on both
                              		  sides at the same time. For example, in the preceding figure PIMs 1 and 2 are
                              		  active on Side A; PIM 3 is active on Side B. The duplexed OPCs communicate with
                              		  each other through the MDS to ensure that a PIM is active only on one side at a
                              		  time.

The duplexed PG architecture protects against a failure on one side of
                              		  the PG. For example, if an adapter card controlling access to an ACD fails, a
                              		  hot standby PIM can use the alternate PIM activation path. As shown in the
                              		  preceding figure, PIM3 was activated from Side B of the PG. This might be in
                              		  response to an adapter failure between the Side A PIM3 and ACD3. In this type
                              		  of failure scenario, the PG can maintain communication with the attached ACD.

Only one PG Agent actively communicates with a side of the central
                              		  controller. When messages arrive at the central controller, they are delivered
                              		  to both sides by the central controller Synchronizer process. The PG maintains
                              		  idle communication paths to both sides of the central controller in case a
                              		  switch-over to the other side of the central controller or PG is necessary.

## PG Platform Options

A maximum of two PGs can run on a single hardware platform. A single
                              		  PG can serve only one type of ACD, but can also contain one or more VRU PIMs
                              		  and/or Media Routing PIMs provided that the server hardware has the capacity to
                              		  support the aggregate processing load. For a single hardware platform to serve
                              		  two different types of ACDs, you need two PGs—one for each peripheral type. The
                              		  following figure shows some possible PG options.

As shown in the preceding figure, you can have an Aspect PG on PGA and
                              		  an Aspect PG on PGB. This duplexed PG pair can serve multiple Aspect ACDs. One
                              		  Aspect Peripheral Interface Manager (PIM) is added through Peripheral Gateway
                              		  Setup to connect each Aspect ACD to this PG. In this example, three Aspect PIMs
                              		  are installed on each PG. The PIM is the Unified ICM software interface between
                              		  the PG and different types of contact center peripherals. One PIM is required
                              		  for each peripheral connected to a PG.

In a mixed contact center environment, you may want to run two
                              		  different types of PGs on a single hardware platform. For example, you may want
                              		  to put an Aspect PG and a DEFINITY ECS PG on the same computer. In this way,
                              		  one hardware platform can serve two types of ACDs provided that the hardware
                              		  platform has the necessary memory and CPU capacity to support the aggregate
                              		  processing load.

### Considerations for
                           	 PGs and PIMs

Consider the
                                 		  following points when you plan for PGs and PIMs:

Maximum PGs on a
                                       				platform. A maximum of two PGs can run on a single server platform. These PGs
                                       				can be the same or different types. For example, on a single machine you can
                                       				have an Aspect PG and an Avaya PG, or you can have two Avaya PGs.

PIMs and
                                       				peripherals. You need one PIM for each peripheral connected to the PG. The PIMs
                                       				are installed with the PG software using the Peripheral Gateway Setup tool.

A single PG
                                       				serves peripherals of the same type. A single PG (and its associated PIMs) can
                                       				serve only ACDs of the same type. For example, an Aspect PG with four PIMs can
                                       				serve only four Aspect ACDs. It cannot serve three Aspect ACDs and an Avaya
                                       				DEFINITY ACD. You can put VRU and Media Routing PIMs on the same PG as an ACD,
                                       				but all VRU PIMs must service VRUs of the same type.

Using two PGs on
                                       				a platform. Before you commit to installing two PGs on a single VM, consider
                                       				the expected call load for the ACDs connected to the PGs.

Be sure that the
                                       				VM has enough memory and processing power to handle the expected call load. In
                                       				addition, ensure that the bandwidth in the network between the PG and the
                                       				Unified ICM central controller can handle the route request and event traffic
                                       				generated by the PGs. (These same considerations apply when using multiple PIMs
                                       				on a PG, but to a lesser extent.)

Properly sizing the PG server
                                          				  platform. See the Design Guide to properly size the PG server platform and to determine which PG
                                       				configuration is appropriate for your application.

CTI Server and an ACD PG on
                                          				  the same platform. Install CTI Server and an IVR or ACD PG on the same
                                       				server platform. The PG can run multiple PIMs. (The same considerations
                                       				described earlier in "Using two PGs
                                          				  on a platform," also apply to the CTI Server-PG configuration.)

UCCE Gateway. In Unified ICM Enterprise, the UCCE Gateway PG allows the
                                       				Unified ICM to pre-route calls to Unified CCE call centers and can also
                                       				post-route Unified CCE calls. The UCCE Gateway feature allows Unified CCE or
                                       				Unified CCX to act as enhanced ACDs connected to the Unified ICM. Refer to the for more information.

## Standard PG Configuration

In most PG configurations, the PG is located with the ACD at a contact
                              		  center site. The PG communicates with the central controller via the Unified
                              		  ICM visible network WAN links. These WAN links can be a dedicated circuit,
                              		  or—if Quality of Service (QoS) is implemented—the corporate WAN. When
                              		  Administration & Data Servers are located with PGs and ACDs at the contact
                              		  center site, both PGs and Administration & Data Servers can share the WAN
                              		  links to the central controller. If the PG is collocated with the Unified ICM
                              		  central controller, the PGs connect directly to the Unified ICM visible LAN.
                              		  The following figure shows an example of a standard PG configuration.

## Remote ACD and VRU
                        	 Connection to PGs

Some ACDs allow a
                              		  remote connection to the Unified ICM Peripheral Gateway. In a remote ACD
                              		  configuration, the PGs are located at the central site along with the
                              		  CallRouter, Logger, and NIC. The ACD is located at a remote contact center
                              		  site.

For information on
                              		  remote PG support, see the ACD Supplement for the particular ACD. Usually
                              		  Alcatel, Aspect, Avaya, Avaya ACC ACDs are supported over the WAN. However, in
                              		  all cases, you must check with the ACD manufacturer for any WAN limitations.

The VRU PG can
                              		  communicate remotely with VRU's via a TCP/IP network. However, you must ensure
                              		  that the network link between the PG and VRU system provides enough bandwidth
                              		  to support the call load for the VRU.

## Multiple PGs
                        	 Connecting to Single ACD

Connecting multiple
                              		  PGs to the same ACD is required when multiple Unified ICM customers need to
                              		  share the same service bureau ACD. For this configuration to be possible, the
                              		  ACD must allow multiple CTI applications to share its CTI link(s). Support for
                              		  multiple PG connections varies depending on the ACD platform. See the
                              		  appropriate Cisco Unified ICM software ACD Supplement and contact
                              		  your ACD vendor to determine the availability of this functionality.

| Note | Some ACDs can
                                 		connect directly to the Unified ICM visible LAN. Others connect to the PG via
                                 		serial or other types of communication links. |
|---|---|

| Note | Also consider
                                                				the number of CTIOS agents and number of VRU ports as factors in determining
                                                				server capacity. |
|---|---|