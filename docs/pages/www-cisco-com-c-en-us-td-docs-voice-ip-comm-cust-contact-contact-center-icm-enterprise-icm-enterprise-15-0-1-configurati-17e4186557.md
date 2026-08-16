---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-icm-enterprise-icm-enterprise-15-0-1-configurati-17e4186557
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/icm_enterprise/icm_enterprise_15_0_1/configuration/guide/ucce_b_1501_icm-to-icm-gateway-user-guide/ucce_m_1501_icm-to-icm-gateway-overview.html
retrieved_at: 2026-08-16T14:34:14.749493+00:00
---

ICM to ICM Gateway User Guide for Unified CCE, Release 15.0(1)

# ICM to ICM Gateway User Guide for Unified CCE, Release 15.0(1)

## Results

Updated: April 30, 2025

Chapter: ICM-to-ICM Gateway Overview

## Chapter: ICM-to-ICM Gateway Overview

# ICM-to-ICM Gateway Overview

## ICM-to-ICM Gateway

ICM-to-ICM Gateway extends the Unified CCE capability by allowing agents to simultaneously post-route calls
                              		  and supply additional call-related information to a second agent on a different ICM . This feature enables the initial agent to pass on
                              		  gathered information without the customer's needing to repeat it to the second
                              		  agent.

Following are some business scenarios where ICM-to-ICM Gateway
                              		  functionality can be useful:

A customer calls the institutional department of a financial
                                    				corporation for customer service assistance with a company-sponsored 401k. The
                                    				customer then asks to be transferred to the retail department to obtain
                                    				assistance with a personal account.

Two companies merge (for example, a bank and an insurance company),
                                    				each of which has a contact center that uses Unified CCE .  The corporation can use the ICM-to-ICM Gateway
                                    		  to
                                    				transfer a call between the two companies; for example, to sell insurance to a
                                    				bank customer.

A customer calls a hotel to make a reservation. The hotel agent
                                    				asks whether they also want to rent a car, and then transfers
                                    				the calls to a car rental agent.

A company uses an outsourcer to handle part of its overflow
                                    				traffic. For example, the company service department handles paid support calls
                                    				in-house but transfers warranty service requests to the outsourcer.

A multinational corporation encompasses several geographic
                                    				regions; each geographic region has its own Unified CCE .

In all these cases, ICM-to-ICM Gateway enables the call-related data
                              		  to be transferred along with the call so the customer does not need to supply
                              		  this information again.

## ICM-to-ICM Gateway Call Flow

The following figure illustrates basic ICM-to-ICM Gateway call flow:

A Client ICM receives a request. This request could be a pre-route request
                                    				from a service provider network (in which case the routing client is a NIC) or
                                    				a post-route request from an ACD/IVR (in which case the PG acts as the routing
                                    				client)

The Client ICM executes a script. At some point, the script
                                    				begins a route request to the other Unified CCE , referred to as the Server ICM. The Server ICM must find a destination label for the call.

The Server ICM executes a script to select a destination label for
                                    				the call. The Server ICM handles this call as a normal route request, save for
                                    				the fact that the routing client is another ICM and not a service provider
                                    				network or an ACD/IVR. Once a destination label is selected, the Server ICM
                                    				sends it back to the Client ICM.

When the Client ICM receives the destination label from the Server
                                    				ICM, it automatically passes the label directly to the routing client that initiated the
                                    				route request.

### ICM-to-ICM Communication

The ICM-to-ICM Gateway link connects two ICMs through a Cisco
                                 		  proprietary protocol called INCRP (Intelligent Network Call Routing Protocol).
                                 		  Both ICMs have a component managing the connection.

The script node on the Client ICM is called an ICM Gateway . It sends the route requests and receives the
                                 		  responses (destination labels) from the Server ICM.

The component on the Server ICM is called an INCRP Network Interface Controller (INCRP NIC) . The NIC receives
                                 		  route requests and sends responses back to the requester. An ICM can have an
                                 		  INCRP NIC, as well as other types of NICs.

Both the ICM Gateway and the INCRP NIC run on the CallRouter, so no
                                 		  additional hardware is required.

The ICM-to-ICM link is a connection in one
                                 		  direction only. It allows the Client ICM to send route requests to the Server
                                 		  ICM, but not the other way around. It is possible to additionally reverse the
                                 		  roles of the Unified CCE s as well, so that each ICM can send call requests to each other.
                                 		  In this case, each Unified CCE needs an ICM Gateway and an INCRP NIC, as shown in the following figure.

INCRP only supports direct connections between two ICMs. Unified CCE instances that are not directly connected with an ICM-to-ICM link cannot
                                 		  send call requests through another ICM.

### Pre-routing

The following figure illustrates a call flow scenario for a call that is
                                 		  pre-routed from one ICM to another.

The Service Provider network sends a route request to the Client
                                       				ICM.

The Client ICM receives the pre-route request and executes a
                                       				routing script that determines that another Unified CCE instance must handle the route request, and forwards the route request to the Server
                                       				ICM.

The Server ICM executes a script that selects a peripheral target
                                       				for the call and sends the corresponding label to the Client ICM.

If the selected target is reached using a translation route, the
                                       				Server ICM sends the call context data to the selected peripheral, where it
                                       				waits for the call to arrive. If translation routing is not used, this step is
                                       				skipped.

The Client ICM forwards the destination label (that it received in
                                       				Step 3) to the network.

The network connects the call to the selected destination on the
                                       				Server ICM ACD/Agent.

If this call was a translation routed call, the ACD connected to the
                                       				Server ICM requests the call detail information from the PG where it has been
                                       				waiting since Step 4 and sends the call to an agent.

### Post-routing

The following figure a call flow scenario for a post-routed call
                                 		  transfer from one ICM to another.

A call terminates at an ACD that is connected to the Client ICM.
                                       				This call can be a pre-routed call or a call sent without ICM control.

The agent begins a post-route request in one of two ways:

The agent transfers the call to a special number on the ACD,
                                             					 which prompts the ACD to issue a post-route request to the Client ICM.

The agent sends a call transfer request to the CTI Server (not
                                             					 shown). This transfer request must have the post-route flag set, so that a
                                             					 post-route request is issued to the Client ICM before transferring the call.

Note

While the ICM Gateway works regardless of the Routing Client type,
                                       				the NICCallID data is only provided if the original Routing Client can
                                       				perform a network transfer. Since Peripheral Gateways are not capable of
                                       				performing network transfers, in this case the NICCallID field is not
                                       				meaningful. In addition, the NICCallID has no bearing on the pre-route, it is
                                       				only used during the post-route phase.

The Client ICM receives the post-route request along with the call
                                       				context and runs a scheduled script that determines that the Server ICM must handle the route request. The Client ICM
                                       forwards the route request to
                                       				the Server ICM.

The Server ICM selects a destination for the call and responds
                                       				back to the Client ICM with the selected label. The Server ICM also returns the
                                       				(possibly modified) call context to the Client ICM.

After receiving the label, Client ICM can validate (if enabled in
                                       				the Remote ICM Script Node), and then pass the label onto its routing client
                                       				(the PG in this case). If no label is received from the Server ICM (or the
                                       				Server ICM is not online), the Client ICM provides a destination label and sends
                                       				it to the routing client.

If the selected target was a peripheral target with an associated
                                       				translation route, the Server ICM sends the translation route information to
                                       				the PG, where the ACD waits until the call arrives at the ACD and the ACD
                                       				retrieves the information from the PG (in Step 8). If the selected target does
                                       				not use a translation route, this step is skipped. In that case, the call
                                       				context is still transferred to the Server ICM but it is not available for the
                                       				receiving ACD, since it cannot be matched with the call.

The original PG and the ACD transfer the call to its destination.
                                       				The PG sends the destination label to the ACD. The ACD uses that information to
                                       				disconnect the agent who requested the call transfer and connects the incoming
                                       				call leg to its destination using a tie line or public network trunk.

If this call is a translation route call, the ACD connected to the
                                       				Server ICM receives the call, requests the call detail information from the PG
                                       				(where it has been waiting since Step 6), and sends the call to an agent.

## Logical Connection Management and Fault Tolerance

Because the Unified CCE is typically deployed as a synchronous duplex pair, the
                              		  ICM-to-ICM Gateway is likewise deployed between Unified CCE pairs. This deployment leverages the Unified CCE fault-tolerant architecture and keeps the synchronous
                              		  CallRouter pairs in sync.

ICM-to-ICM Gateway addresses the following other possible points of
                              		  failure as follows:

In the case of a link failure, each INCRP NIC has a link to both
                                    				ICM Gateway components. Each INCRP NIC can therefore maintain communications
                                    				with the other ICM Gateway.

If an INCRP NIC fails, the Client CallRouters are synchronized and
                                    				can communicate via the remaining INCRP NIC.

Note

If an ICM-to-ICM Gateway fails, the CallRouters on the Server ICMs are
                                    				synchronized and can communicate via the remaining ICM-to-ICM Gateway.

Note

## ICM-to-ICM Gateway Requirements

Both the Client ICM and Server ICM must be supported releases of ICM, and they must be within one major version of each other.
                              If two connected ICMs are running different releases of ICM software, only the ICM-to-ICM Gateway features supported by the
                              lowest numbered release are available.

Refer to the Unified Contact Center Enterprise (Unified CCE) Software Compatibility Guide for more information.

### Contact Cisco

- Open a Support Case

- (Requires a Cisco Service Contract )

| Note | Network transfers do not work across instances. You cannot perform a Network Transfer from one Remote ICM instance to another Remote ICM instance, even if you have a mesh configuration. With a mesh configuration, you can only perform a local transfer within
                                                your ICM instance. For example, if one side of the Client ICM is co-located with only one side of the Server ICM, you can
                                                set the co-located instance as a preferred connection in order to avoid unnecessary WAN traffic to the other side. |
|---|---|

| Note | If a link failure or a NIC failure occurs, calls that were in
                                             				progress at the time of the failure may be lost. |
|---|---|

| Note | For a more complete discussion of Unified CCE Fault Tolerance, refer to the Solution Design Guide for Cisco Unified Contact Center Enterprise at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-implementation-design-guides-list.html and the Serviceability Guide for Cisco Contact Center Enterprise at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-installation-and-configuration-guides-list.html |
|---|---|