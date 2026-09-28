---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-customer-voice-portal-12-6-2-configuration-guide-0e3f5d155f
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/customer_voice_portal/12-6-2/configuration/guide/ccvp_b_1262-configuration-guide-for-cisco-unified-customer-voice-portal/ccvp_b_1252-configuration-guide-for-cisco-unified-customer-voice-portal-release-1252_chapter_010001.html
retrieved_at: 2026-08-21T11:58:21.267416+00:00
---

Configuration Guide for Cisco Unified Customer Voice Portal, Release 12.6(2)

# Configuration Guide for Cisco Unified Customer Voice Portal, Release 12.6(2)

Updated: April 28, 2023

Chapter: Unified ICME Warm
	 Consult Transfer/Conference

## Chapter: Unified ICME Warm
	 Consult Transfer/Conference

# Unified ICME Warm
                     	 Consult Transfer/Conference

When an agent
                        		attempts a warm consultative transfer/conference to another agent, but there is
                        		no agent available in the skill group to service the request, the first agent
                        		is placed in a queue to wait for the availability of an agent in the desired
                        		skill group. To place the first agent in queue, a call is initiated from
                        		Unified CM to Unified Customer Voice Portal (CVP), via a Translation Route to
                        		VRU, to provide queue music to the first agent. To Unified CVP, this appears as
                        		a new call from an IP phone.

Optionally,
                        		customer business call flows may require that IP phone users call Unified CVP
                        		directly. For example, you may have a corporate IP phone network that is
                        		serviced by a Unified CVP help desk call center. IP phone users with problems
                        		would call a Unified CVP number to open trouble tickets.

This chapter
                        		provides information about the minimal software component release requirements
                        		for the Unified ICME Warm Consult Transfer and Conference to Unified CVP
                        		feature for Type 7 VRUs. Resource sizing and configuration requirements are
                        		also included.

## Configure Unified
                        	 ICME Warm Consult Transfer/Conference to Unified CVP

Step 1

Install a new
                                       			 Call Server (see Installation and Upgrade
                                                				  Guide for Cisco Unified Customer Voice Portal for detailed information).

Define it
                                                					 as a Type 7 VRU in the Network VRU Explorer tool in Unified ICME.

Network Transfer Preferred must be disabled for this
                                                					 peripheral.

Add a new
                                                					 DNIS in the Add DNIS box on the ICM tab in the Operations
                                                					 Console. Ensure to add each translation route DNIS.

Step 2

If the
                                       			 Unified CVP machine resides in a different location from the Unified CM cluster
                                       			 initiating the calls, WAN bandwidth is a consideration because the prompts are
                                       			 played G.711 from the Unified CVP machine. In this case, size and configure the
                                       			 network appropriately. Wherever possible, Unified CVP should be co-located with
                                       			 Unified CM to eliminate these bandwidth requirements.

Step 3

Define a SIP
                                       			 trunk in the Unified CM , using
                                       			 the Unified CVP machine IP address as the Destination address in Device > Trunk > SIP
                                             				  Information .

Step 4

(Perform this
                                       			 step for IP-originated calls only). Determine if customer business call flows
                                       			 require that IP phone users call Unified CVP directly. In Unified CM
                                       			 administration, in "Route Plan" using route groups/lists/patterns, route Unified CVP DNIS’s to the Unified CVP
                                       			 gateway installed in Step 1.

If you want
                                          				to load-balance between two Unified CVP systems:

Create a
                                                					 route group and put both of the Unified CVP gateways in the route group, both
                                                					 with order priority 1.

Create a
                                                					 route list and put the route group in the route list.

Create a
                                                					 route pattern and assign the route list to the route pattern.

In
                                                					 Service Parameters for Unified CM, set Reorder Route List to True and the H225 TCP timer to 5 .

Step 5

Create a
                                       			 Unified ICME script similar to the script below. (See the Unified ICME
                                          				documentation for details). This script should be tied to the Dialed
                                       			 number and call type that the agent invokes to do a warm consultative
                                       			 transfer/conference. This dialed number’s Routing Client should be associated
                                       			 with a Unified CM peripheral from which the agent will be invoking the transfer
                                       			 or conference.

## Minimal Component
                        	 Version Requirement

See the https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-device-support-tables-list.html for the list of component versions that are required to use the Unified ICME
                           		Warm Consult Transfer and Conference to Unified CVP feature.

## Warm Transfer with
                        	 SIP Calls

If an agent
                           		performs a warm transfer to another agent and then that agent is queued, or a
                           		SendToVRU label returns to Unified CM using
                           		jtapi on the Unified CM PG
                           		connection, then you must associate a Route Pattern for that label with a SIP
                           		TRUNK to send to Unified CVP or the Proxy Server to ensure the call returns to
                           		Unified CVP. Unified CVP then sends the request
                              		  instruction message back to Unified ICME on
                           		the Unified CVP routing client and starts the queuing.

When using the Warm Transfer feature for SIP Calls with queuing, and the agent completes a consult transfer to ther caller
                           while the call is still in the queue (VXML Gateway) , then the call flow does not require MTP enabled on the SIP trunk that is associated with the VRU label route pattern.

## Set Up Unified
                        	 ICME Warm Consult Transfer

In this scenario, an agent transfers a call to another agent by
                              		  dialing that agent's ID. If the agent is unavailable, the originating agent is
                              		  placed in a queue to wait for the second agent to pick up the call.

For the first agent to be queued while waiting for another agent, set
                              		  up the following configuration:

Step 1

In the ICM Configuration Manager's PG Explorer tool Routing
                                       			 Client tabs, uncheck the NetworkTransferPreferred check box for Unified CM and Unified CVP routing clients.

Step 2

On the Advanced tab for the Unified CM routing client, select None for the Network VRU and the Type 10 VRU for the Unified
                                       			 CVP routing client.

Step 3

For the Type 10 VRU, in the ICM Configuration Manager's Network
                                       			 VRU Explorer tool, define a label for the Unified CM routing client as well as the Unified CVP routing client, and associate them
                                       			 with a customer instance.

Step 4

In the ICM Configuration Manager's Dialed Number List Tool,
                                       			 associate the dialed numbers for the incoming call as well as the transfer
                                       			 dialed number with the same customer instance.

When the second call is placed for the warm transfer and no agent
                                          				is available, the label defined on the Unified
                                             				  CM RC plus the correlation ID will be sent back via EAPIM/JGW to Unified
                                             				  CM . For example, if the label is 7777777777, with a correlation ID it
                                          				could be 777777777712345 because the call originated from the Unified
                                             				  CM RC, and also because the NetworkTransferPreferred check box is not
                                          				checked.

Step 5

In Unified
                                          				CM , select Call
                                             				  Routing > Route/Hunt > Route
                                             				  Pattern > Add New . Add a new
                                       			 route pattern to route the call to Unified CVP using the SIP trunk if you are
                                       			 adding from the Device Management menu (for example, 777! where ! allows label
                                       			 plus arbitrary length correlation ID).

When Unified CVP sees this call, it perceives it as a pre-routed call
                              		  with a correlation ID and sends it back to Unified ICME to continue the script.

Unified ICME sends a temporary connection back to Unified CVP, which queues the agent call
                              		  while the caller hears music on hold (MoH) from Unified CM .

| Note | For information
                                 		about using the Warm Consult Transfer feature with SIP and Type 10 VRUs, see Warm Transfer with SIP Calls .
                                 		For configuration procedure of Call Director and Comprehensive call flow models
                                 		using SIP, see Unified CVP Call Flow Models . |
|---|---|

| Step 1 | Install a new
                                       			 Call Server (see Installation and Upgrade
                                                				  Guide for Cisco Unified Customer Voice Portal for detailed information). Note It can be
                                                   				configured identically to all other Unified CVP machines, with the exception
                                                   				that you must add each Translation Route DNIS. Define it
                                                					 as a Type 7 VRU in the Network VRU Explorer tool in Unified ICME. Network Transfer Preferred must be disabled for this
                                                					 peripheral. Add a new
                                                					 DNIS in the Add DNIS box on the ICM tab in the Operations
                                                					 Console. Ensure to add each translation route DNIS. | Note | It can be
                                                   				configured identically to all other Unified CVP machines, with the exception
                                                   				that you must add each Translation Route DNIS. |
|---|---|---|---|
| Note | It can be
                                                   				configured identically to all other Unified CVP machines, with the exception
                                                   				that you must add each Translation Route DNIS. |
| Step 2 | If the
                                       			 Unified CVP machine resides in a different location from the Unified CM cluster
                                       			 initiating the calls, WAN bandwidth is a consideration because the prompts are
                                       			 played G.711 from the Unified CVP machine. In this case, size and configure the
                                       			 network appropriately. Wherever possible, Unified CVP should be co-located with
                                       			 Unified CM to eliminate these bandwidth requirements. |
| Step 3 | Define a SIP
                                       			 trunk in the Unified CM , using
                                       			 the Unified CVP machine IP address as the Destination address in Device > Trunk > SIP
                                             				  Information . |
| Step 4 | (Perform this
                                       			 step for IP-originated calls only). Determine if customer business call flows
                                       			 require that IP phone users call Unified CVP directly. In Unified CM
                                       			 administration, in "Route Plan" using route groups/lists/patterns, route Unified CVP DNIS’s to the Unified CVP
                                       			 gateway installed in Step 1. If you want
                                          				to load-balance between two Unified CVP systems: Create a
                                                					 route group and put both of the Unified CVP gateways in the route group, both
                                                					 with order priority 1. Create a
                                                					 route list and put the route group in the route list. Create a
                                                					 route pattern and assign the route list to the route pattern. In
                                                					 Service Parameters for Unified CM, set Reorder Route List to True and the H225 TCP timer to 5 . Note The
                                                   				Reorder Route List setting applies only for Unified CM 3.3
                                                   				and earlier. | Note | The
                                                   				Reorder Route List setting applies only for Unified CM 3.3
                                                   				and earlier. |
| Note | The
                                                   				Reorder Route List setting applies only for Unified CM 3.3
                                                   				and earlier. |
| Step 5 | Create a
                                       			 Unified ICME script similar to the script below. (See the Unified ICME
                                          				documentation for details). This script should be tied to the Dialed
                                       			 number and call type that the agent invokes to do a warm consultative
                                       			 transfer/conference. This dialed number’s Routing Client should be associated
                                       			 with a Unified CM peripheral from which the agent will be invoking the transfer
                                       			 or conference. |

| Note | It can be
                                                   				configured identically to all other Unified CVP machines, with the exception
                                                   				that you must add each Translation Route DNIS. |
|---|---|

| Note | The
                                                   				Reorder Route List setting applies only for Unified CM 3.3
                                                   				and earlier. |
|---|---|

| Note | These SIP calls
                                    		do not require MTP enablement on the SIP trunks. |
|---|---|

| Note | The MTP is not required if VXML GW version is IOS 12.4.(15)T8 or 12.4(20)T2 or later versions on these T releases. In cases, where there is SIP DTMF capability mismatch, MTP is required between Unified Customer Voice Portal (CVP) and Cisco
                                    Unified Communications Manager (CUCM). |
|---|---|

| Note | Unified CVP with a Type 10 VRU does not support multiple Network
                                       		  VRUs on the same Unified CVP peripheral device. Multiple customer instances can
                                       		  be used in order to address multiple Network VRUs, but they must then address
                                       		  different physical Unified CVP Call Servers as well. Calls that originate from
                                       		  an ACD or Unified CM, such as Warm Transfer/Conference, Helpdesk, or Outbound
                                       		  calls, are also limited to one Network VRU on any given Unified CVP Call
                                       		  Server. Note that the reverse is supported - multiple Unified CVP Call Servers
                                       		  can share the same Network VRU. |
|---|---|

| Step 1 | In the ICM Configuration Manager's PG Explorer tool Routing
                                       			 Client tabs, uncheck the NetworkTransferPreferred check box for Unified CM and Unified CVP routing clients. |
|---|---|
| Step 2 | On the Advanced tab for the Unified CM routing client, select None for the Network VRU and the Type 10 VRU for the Unified
                                       			 CVP routing client. |
| Step 3 | For the Type 10 VRU, in the ICM Configuration Manager's Network
                                       			 VRU Explorer tool, define a label for the Unified CM routing client as well as the Unified CVP routing client, and associate them
                                       			 with a customer instance. |
| Step 4 | In the ICM Configuration Manager's Dialed Number List Tool,
                                       			 associate the dialed numbers for the incoming call as well as the transfer
                                       			 dialed number with the same customer instance. When the second call is placed for the warm transfer and no agent
                                          				is available, the label defined on the Unified
                                             				  CM RC plus the correlation ID will be sent back via EAPIM/JGW to Unified
                                             				  CM . For example, if the label is 7777777777, with a correlation ID it
                                          				could be 777777777712345 because the call originated from the Unified
                                             				  CM RC, and also because the NetworkTransferPreferred check box is not
                                          				checked. |
| Step 5 | In Unified
                                          				CM , select Call
                                             				  Routing > Route/Hunt > Route
                                             				  Pattern > Add New . Add a new
                                       			 route pattern to route the call to Unified CVP using the SIP trunk if you are
                                       			 adding from the Device Management menu (for example, 777! where ! allows label
                                       			 plus arbitrary length correlation ID). |

| Note | When customized CTI clients are used, consult transfer mechanism
                                          			 is utilized to check if the second agent is really answering the call before
                                          			 the call is being finally transferred automatically by the customized CTI
                                          			 client. In this scenario, it is not required for the agents transferring the
                                          			 call to complete the transfer manually as customized CTI client automatically
                                          			 transfers the calls. However, this is applicable only when the second agent
                                          			 (called agent) answers the call and not before. Customized clients should wait
                                          			 for five seconds before completing the automatic consult transfer to avoid race
                                          			 conditions. |
|---|---|