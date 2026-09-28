---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-icm-enterprise-icm-enterprise-12-6-1-installatio-ba6b37ac2a
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/icm_enterprise/icm_enterprise_12_6_1/installation/guide/ucce_b_pre-installation-planning-guide-for-cisco/ucce_m_interactive-voice-response-vru-systems126.html
retrieved_at: 2026-08-16T20:03:29.774288+00:00
---

Pre-installation Planning Guide for Cisco Unified Intelligent Contact Management, Release 12.6(1)

# Pre-installation Planning Guide for Cisco Unified Intelligent Contact Management, Release 12.6(1)

Updated: May 12, 2021

Chapter: Interactive Voice
	 Response (VRU) Systems

## Chapter: Interactive Voice
	 Response (VRU) Systems

# Interactive Voice
                     	 Response (VRU) Systems

Cisco provides an
                        		option for running an interface to Interactive Voice Response (VRU) systems.
                        		The VRU interface software allows VRU's to take advantage of Unified ICM call
                        		routing features. For example, an VRU can use post-routing capabilities to
                        		select targets for calls it needs to transfer. The VRU interface software runs
                        		on a standard PG hardware platform. It allows the Unified ICM to route calls to
                        		targets on an VRU and collect data from an VRU for use in call routing,
                        		real-time monitoring, and historical reporting. The VRU interface is not
                        		specific to a particular VRU system or manufacturer. It is based on an open VRU
                        		model. Many VRU systems support Cisco's Open VRU Interface Specification,
                        		including Unified CVP. For a list of VRU's that support this interface, contact
                        		your Cisco representative.

To plan for this VRU
                        		option:

Review the options
                              			 for integrating VRU's into the Unified ICM system.

Determine if any
                              			 VRU programming or application development is necessary.

Review the
                              			 Peripheral Gateway platform requirements.

## VRU Configuration
                        	 Options

VRU's can be located
                              		  at the customer's call center site or in the IXC network. At the call center,
                              		  you can connect the VRU on the network side of the ACD or "behind" the
                              		  ACD. In the IXC network, the network provider can offer the VRU as a service.

In an Unified ICM
                              		  configuration that includes an VRU, you configure the ACD so that it can
                              		  transfer calls to the VRU. The following figure shows some of the capabilities
                              		  of the VRU in an Unified ICM system.

Capabilities of VRU:

In most Unified
                                    				ICM /VRU configurations, calls continue to be Pre-Routed by the Unified ICM
                                    				system.

When a call is
                                    				routed to an VRU, the VRU answers the call and interacts with the caller.

The VRU can
                                    				access a host system (for example, a customer profile database) to retrieve
                                    				more information to help process the call.

Often, the caller can get all the required information through simple interaction with the VRU. In some cases, however, the
                                    VRU needs to transfer the caller to an agent or another call resource.

In some
                                    				configurations, the VRU can invoke post-routing to select an agent from
                                    				anywhere in the call center enterprise. To do this, the VRU sends a route
                                    				request to the PG. The PG forwards the request to the Unified ICM system, which
                                    				responds with a new destination for the call. The PG returns the new
                                    				destination to the VRU. The VRU then signals the ACD or network to transfer the
                                    				call to the specified destination.

The way in which an
                              		  VRU is integrated into the Unified ICM system affects the flow of call
                              		  processing and determines the types of data the Unified ICM can collect from
                              		  the VRU. For example, an VRU that has a direct interface to an VRU PG provides
                              		  the Unified ICM system with data that is used in call routing, monitoring, and
                              		  reporting. A configuration in which the VRU has an interface only to the ACD
                              		  has more limited capabilities.

You can integrate
                              		  VRU's into the Unified ICM system in several different ways. Each integration
                              		  option provides a different set of Unified ICM functionality.

### Configuration with
                           	 ACD PG Only

In this option, the
                                 		  IVR is attached only to the ACD. The ACD, in turn, is attached to a PG. The PG
                                 		  is running the Cisco peripheral interface software (PG software process)
                                 		  required to communicate with the specific type of ACD. There is no direct
                                 		  interface between the IVR and the Unified ICM system (in other words, an IVR
                                 		  process is not implemented).

In this
                                 		  configuration, you must connect the IVR to an ACD that supports post-routing.
                                 		  The IVR and ACD cooperate so that calls are transferred from the IVR
                                 		  to the ACD, and then post-routed by the ACD via the PG. The PG in this
                                 		  configuration has only the ACD peripheral interface software. It does not have
                                 		  the IVR interface software; therefore, it does not provide the IVR with full
                                 		  access to post-routing.

In the preceding
                                 		  figure, the IVR can handle a call in two different ways:

The IVR can
                                       				handle the call to completion (for example, if the caller wanted current
                                       				billing information and needed no further assistance, the IVR can complete the
                                       				call.)

The IVR can
                                       				transfer the call to the ACD. The ACD can then use the PG to post-route the
                                       				call.

### Configuration with
                           	 IVR and ACD PGs

This configuration
                                 		  option is similar to the previous option except that an IVR process
                                 		  and host link to the IVR are implemented. In addition to monitoring
                                 		  the ACD for real-time agent and call event data, the PG can monitor the IVR
                                 		  for call and application data and control the movement of calls into and out of
                                 		  the IVR. The IVR data is also forwarded to the CallRouter
                                 		  for call routing and reporting.

As shown in the
                                 		  following figure, you can install the IVR and ACD interface software
                                 		  on the same PG hardware platform.

### Network-Side VRU
                           	 with VRU and ACD PGs

The next
                                 		  configuration option places the VRU on the network side of the ACD. In this
                                 		  configuration, the VRU is connected to the network and potentially to the ACD.
                                 		  The VRU can receive calls directly from the network without ACD involvement.
                                 		  The Unified ICM can pre-route these calls, but it is not a requirement.

The VRU can also
                                 		  receive calls from the ACD (for example, when an agent transfers a call to the
                                 		  VRU). Again, the Unified ICM may or may not have routed these calls. The
                                 		  following figure shows an example.

After the VRU
                                 		  receives a call, it handles the call to completion or transfers the call
                                 		  off-VRU for subsequent handling. The VRU can also use post-routing to select a
                                 		  target for the transfer. If the VRU transfers the call to an ACD, the VRU may
                                 		  or may not request routing instructions from the Unified ICM.

This configuration
                                 		  is different from the earlier options in several ways:

The VRU is
                                       				connected to both the network and the ACD.

You can transfer
                                       				a call that originated in the network to the local ACD by tandem connecting a
                                       				second trunk with the original trunk. You can transfer a network call to a
                                       				remote ACD either by connecting a second trunk in tandem with the original
                                       				trunk, or by invoking a "call
                                          				  take-back" feature in the network.

You can use
                                       				post-routing to transfer a call that originated at the local ACD to any target.

### In-Network VRU with
                           	 ACD PG Only

In this
                                 		  configuration, the VRU is provided as a service by the network service
                                 		  provider. The PG monitors the ACD and forwards data to the Unified ICM system
                                 		  for call routing and reporting.

When the caller
                                 			 dials the toll-free number, the Unified ICM instructs the network to transfer
                                 			 the call to the network-based VRU. The network VRU then prompts the caller for
                                 			 input. If the caller requires additional information (such as speaking to an
                                 			 agent), the VRU dials a "hidden" toll-free number. The network then queries the Unified ICM system for a routing
                                 			 destination. The Unified ICM system returns a routing label and the network
                                 			 transfers the call to the specified ACD and DNIS. An agent at the ACD can
                                 			 handle the call to completion or transfer the call for subsequent handling.

### In-Network VRU with
                           	 VRU and ACD PGs

In this
                                 		  configuration, the VRU is provided as a service by the network provider. The
                                 		  network transfers all calls to a destination VRU. The VRU either handles a call
                                 		  to completion or transfers the call to another resource (for example, an agent
                                 		  at an ACD).

### VRU Transfer Routing
                           	 Using Third-Party Call Control

In this
                                 		  configuration, the VRU invokes a transfer request to transfer a call to the
                                 		  ACD. The VRU uses a CTI link to the ACD which sets variables in the transfer
                                 		  request (for example, CED, DNIS, CLID, Social Security number, or account
                                 		  number). This configuration is viable only if the VRU is attached to an ACD
                                 		  that supports post-routing. The following figure provides an example of this
                                 		  configuration.

When the ACD
                                 		  receives the transfer from the VRU, it makes a route request to the PG to
                                 		  conduct an enterprise-wide agent selection. The PG routing client sends a route
                                 		  request to the CallRouter. The CallRouter passes a response to the PG and on to
                                 		  the ACD. The ACD then transfers the call to the specified destination.

### VRU Programming and
                           	 Application Development

The Open VRU
                                 		  Interface allows the Unified ICM to see some level of VRU application-specific
                                 		  data (for example, menu selections). An VRU application developer can use the
                                 		  Open VRU Interface to implement call routing (routing client) and monitoring
                                 		  capabilities.

The VRU routing
                                 		  client allows the VRU to send route requests to the Unified ICM via the PG.
                                 		  These requests can include data variables such as Customer ID and Menu
                                 		  Selections. The Unified ICM system uses this data to instruct the VRU where to
                                 		  transfer the call. The application developer uses the VRU monitoring interface
                                 		  to send VRU port and application activity data to the Unified ICM system for
                                 		  call routing and reporting.

### VRU Peripheral
                           	 Gateway

The Cisco VRU
                                 		  interface software runs as a logical PG on a standard Peripheral Gateway
                                 		  hardware platform. A single PG hardware platform can support a maximum of two
                                 		  logical PGs. A single PG platform may run one or two VRU PGs or an VRU PG and
                                 		  an ACD PG. For example, you can have a PG hardware platform that runs an Aspect
                                 		  CallCenter PG and an VRU PG. A logical PG can have PIMs for one type of ACD,
                                 		  plus an VRU PIM. The hardware platform must have sufficient capacity to handle
                                 		  the aggregate load from all attached peripherals.

In the following
                                 		  figure, a duplexed set of PGs serve both an VRU system and an ACD system. These
                                 		  PGs are equipped with both ACD and VRU interface software.

The VRU Peripheral
                                 		  Gateway can run in simplexed or duplexed configurations. In a duplexed
                                 		  configuration, only one side of the PG has an active connection to the VRU at a
                                 		  time.

For information on
                                 		  how VRU systems fit into the Unified ICM data communications networks, see Datacom Requirements .

| Note | The VRU can also
                                          		  be on a System UCCE PG or a UCCE Generic PG. |
|---|---|

| Note | When multiple
                                          		  VRUs are connected to a PG, VRUs that use poll-based monitoring cannot be mixed
                                          		  with VRUs using any other kind of monitoring. |
|---|---|