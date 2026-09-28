---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-icm-enterprise-icm-enterprise-12-6-1-user-guide--772a0317e8
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/icm_enterprise/icm_enterprise_12_6_1/User/guide/reporting-concepts-for-cisco-unified-icm-contact-center-enterprise-release-12-6-1/routing-and-queuing.html
retrieved_at: 2026-08-16T20:42:43.429707+00:00
---

Reporting Concepts for Cisco Unified ICM-Contact Center Enterprise, Release 12.6(1)

# Reporting Concepts for Cisco Unified ICM-Contact Center Enterprise, Release 12.6(1)

Updated: June 27, 2023

Chapter: Routing and Queuing

## Chapter: Routing and Queuing

# Routing and Queuing

## Routing

When Unified CCE software receives a routing request, it determines the appropriate destination for the call by running routing scripts.

These scripts use real-time information about activity at
                              the contact centers to find the destination best able to handle the call. You
                              can monitor how the system is handling calls and can make changes to the
                              scripts when needed, using the Script Editor.

A destination
                              (called a routing target ) can be a network target such an
                              announcement or a ring, or a skill target such as an agent, a skill group, or a
                              service. Once these targets are defined in the Configuration Manager , they can
                              be specified in the routing script.

### Pre-routing

Pre-routing is a routing decision that is run before the call terminates at the call center. With pre-routing, the Network
                                 Interface Controller (NIC) receives the route request from the Interexchange Carrier (IXC) and passes the call information
                                 along to Unified CCE software.

Unified CCE bases pre-routing decisions on real-time data gathered by the PGs at the call center sites. Unified CCE then runs the appropriate script that defines how the call is to be routed.

A pre-routing
                                 		  request therefore determines the initial destination for a call.

### Post-routing

Post-routing is a routing decision made after the call has initially been processed at a VRU or call center. Post-routing
                                 enables Unified CCE to process calls when an ACD, VRU, or PBX generates a route request via the PG.

Unified CCE runs scripts to process the route request and return the destination address. This directs the ACD/PBX to send the call to
                                 an agent, skill group, service or Call Type in the same call center or at a different call center. In making a post-routing
                                 decision, Unified CCE software can use all the same information and scripts used in pre-routing.

A post-routing is sent by the peripheral to refine the
                                 original route or redirect the call.

### Translation Routing

Translation routing
                                 is the term used when additional information is sent along with a call.

This type of routing is necessary because the carrier can deliver voice , but has no way to deliver data to the peripheral.

Unified CCE software works with the PG to deliver the call to the final destination on the peripheral and to ensure that the appropriate
                                 information collected for the call is also delivered to the agent's desktop.

After the data is delivered to the peripheral, the
                                 PG receives back information about which agent the call is sent to.

You define Translation Routes with the Configuration Manager, using the
                                 Translation Route Wizard.

Translation routing is always used when a call
                                 moves from one peripheral to another. A call can also be translation routed
                                 from the network.

The term ICM TranslationRoute is
                                       used when calls are translation routed to a peripheral that is an
                                       ACD.

The term TranslationRouteToVRU is used when calls
                                       are translation routed to a peripheral that is a VRU.

Translation routing plays a significant role in the accuracy of reporting
                                 and allows for cradle-to-grave call tracking and reporting. Some reporting
                                 metrics gathered for Call Types and skill groups are applicable only if calls
                                 are translation routed.

### Skills-Based Routing

Skills-based routing is a routing decision
                                 whereby a call is routed to the skill group that has agents with the
                                 appropriate expertise.

## Queuing

Queued calls are calls that are being
                              held until an agent is available.

Unified CCE software calculates a number of call center metrics based on the time spent in queues.

It is important to understand the two models of queuing and how queuing
                              affects reporting metrics.

### ACD Queuing

ACD queues are used to queue calls
                                 on a targeted ACD and are controlled by the ACD .

Unified CCE might route a call to the ACD, based on knowledge gathered by the PGs that a certain skill group or service at that ACD is
                                 best suited to answer the call.

Once the call arrives at the
                                 ACD, if an agent is not available, the ACD queues the call to the skill group.
                                 Optionally a call can be queued to a skill group on the ACD during agent
                                 transfers or resulting from a call treatment provided on the ACD.

### Enterprise
                           	 Queuing

Unified CCE controls Enterprise queues using the Service Control Interface (SCI), irrespective of the telephony platform chosen to queue the call.

In this model, calls
                                 		  are held at a "network-level" VRU that has an enterprise view of available agents, based on the skill groups
                                 		  and services configured for the peripheral.

The following
                                 		  telephony platforms are supported for Enterprise queuing:

Cisco Voice Portal and Cisco IP-IVR, when connected to Unified CCE by a VRU PG

A third-party VRU that supports service control and is connected to Unified CCE by a VRU PG

A VRU at the TDM Network that supports service control and is connected to Unified CCE by a NIC

For deployments where Unified CCE provides integration to an ACD for agent level routing, the ACD itself is used as the telephony platform that queues the
                                       call as the Unified CCE directs.

Enterprise queues
                                 		  are an efficient way to route a call in your enterprise network. Enterprise
                                 		  queues are also a cost-effective way to save on toll charges before terminating
                                 		  a call on the ACD.

### How Calls Offered and Calls Queued Are Incremented

The Skill_Group_Real_Time database
                                 tracks calls offered and calls queued in separate fields.

Therefore, there is no double counting of calls queued and offered at the
                                 ACD and calls queued and offered at the network.

### Effect of Enterprise Queues on Reporting

The use of enterprise queues affects Call
                                 Type, Skill Group, and Service reporting.

The reporting metrics
                                 that are affected include queued metrics, answered metrics, service level
                                 metrics, and abandoned metrics.

The reporting of these metrics is
                                 also affected by whether or not the call was
                                 routed when sent
                                 to an ACD. For more information, see, translation-routed .

Some reporting
                                                   metrics for skill groups and call types are applicable only if calls are
                                                   translation routed.

Translation routing plays a
                                                   significant role in the accuracy of reporting. Some reporting metrics gathered
                                                   for Call Types and skill groups are applicable only if calls are translation
                                                   routed. Calls can be translation routed either to a VRU Peripheral or to an
                                                   ACD.

Translation routing is primarily applicable when Unified CCE software is used for Enterprise Routing to traditional ACDs. This includes deployments connected to legacy ACDs using any
                                                   supported TDM PG such as Aspect PG and deployments connected to Cisco Unified System Contact Center using Unified CCE Gateway PG. Translation Routing enables Unified CCE for cradle to grave reporting.

For deployments where Unified CCE provides integrations to an ACD for Enterprise Routing, the following is true:

Unified CCE system reports on ACD queue metrics.

When Unified CCE software is used to provide initial call treatment and/or enterprise queuing, Unified CCE software reports on enterprise queue metrics. However, once the call is routed to an ACD the ACD may queue the call. In this
                                                         case, Unified CCE software reports on both enterprise queue and ACD queue metrics.

Unified CCE system uses a Service Control VRU as the telephony platform for enterprise queuing.

Reporting is the same whether Unified CCE script uses a Send To VRU node or a Translation Route To VRU node.

#### Call
                                 Type Metrics

When a call is
                                    translation-routed :

The AnswerWaitTime , ASA , and Service Level include both the time spent in the
                                       Enterprise queue and the time spent in the ACD queue.

The
                                       measurement of AnswerWaitTime for a call begins when the call is queued. The
                                       measurement of Service Level begins when the call arrives at the routing script
                                       or when its Call Type is changed.

This method of measurement means that if self-service
                                       is performed on a call before the call is queued to an agent, the routing
                                       script must be set up to change the Call Type when self-service is completed.
                                       Otherwise, the time spent in self-service will negatively impact the Service
                                       Level.

Abandoned statistics are
                                       classified in three ways:

Calls that abandoned while ringing at the agent desktop.

Calls that abandoned in an Enterprise queue
                                             while waiting for an available agent.

Total
                                             number of calls that abandoned. This number includes calls that abandoned in a VRU
                                             (prompting), calls abandoned in both Enterprise queue and ACD queue, and calls
                                             that abandoned at the agent.

When a call is not
                                    translation-routed :

The Call Type Abandoned metrics allow you to determine the number of
                                       calls that abandoned in an enterprise queue while waiting for an available
                                       agent and the number of calls that abandoned while in self-service.

However, they do not allow you to determine the number of calls
                                       that were abandoned after they left the VRU and before an agent answered them.

The Call Type Answered metrics will
                                       always be zero and are not applicable.

The Call Type Service Level metrics are not applicable.

#### Skill Group Metrics

When a call is translation-routed :

The Skill Group Answered metrics include only time spent in the ACD queue.

When a call is not
                                    translation-routed :

The Skill Group Queued metrics are applicable.

The
                                       Skill Group Abandoned metrics allow you to determine the
                                       number of calls that abandoned in an enterprise queue while waiting for an
                                       available agent, but they do not allow you to determine the number of calls
                                       that abandoned after they left the VRU and before an agent answered them.
                                       The ACD report shows calls that abandoned after they arrived at the
                                       ACD.

The Skill Group Answered metrics
                                       do not include any time spent in the enterprise queue and therefore are not
                                       applicable.

#### Service
                                 Metrics

If a Service Control VRU is used for VRU
                                 application, the Service metrics can be used to provide performance measures
                                 for the VRU service. The type of VRU and configuration determines the
                                 information and usefulness of the metrics reported for the VRU service.

The metrics reported for Unified CCE Services defined for the ACD peripherals do not include any time spent in the enterprise queue. Hence the service metrics
                                 are not useful when using an enterprise queue.

## Precision Queues

Precision Routing is a feature available with Cisco Unified CCE . Precision Routing enhances and can replace traditional routing. Traditional routing looks at all the skills to which an
                           agent belongs and defines the hierarchy of skills to map business needs. However, traditional routing is restricted by its
                           single dimensional nature. Precision Routing provides multidimensional routing with simple configuration, scripting, and reporting.
                           Agents are represented through multiple attributes with proficiencies so that the capabilities of each agent are accurately
                           exposed, bringing more value to the business.

You can use a combination of attributes to create multidimensional precision queues. Using Unified CCE scripting, you can dynamically map the precision queues to direct a call to the agent that best matches the precise needs
                           of the caller.

For more information on precision routing, see the Cisco Unified Contact Center Enterprise Features Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-feature-guides-list.html .

| Note | Your ACD Supplement Guide describes the features of Unified CCE post-routing available with the ACD, as well as any considerations you should be aware of when using post-routing or Translation
                                          Routing on the PG. |
|---|---|

| Note | Refer to your ACD Supplement
                                             Guide to see if your ACD supports translation routing and for any
                                          considerations when you use translation routing on the
                                          PG. |
|---|---|

| Note | Some reporting
                                                   metrics for skill groups and call types are applicable only if calls are
                                                   translation routed. Translation routing plays a
                                                   significant role in the accuracy of reporting. Some reporting metrics gathered
                                                   for Call Types and skill groups are applicable only if calls are translation
                                                   routed. Calls can be translation routed either to a VRU Peripheral or to an
                                                   ACD. Translation routing is primarily applicable when Unified CCE software is used for Enterprise Routing to traditional ACDs. This includes deployments connected to legacy ACDs using any
                                                   supported TDM PG such as Aspect PG and deployments connected to Cisco Unified System Contact Center using Unified CCE Gateway PG. Translation Routing enables Unified CCE for cradle to grave reporting. For deployments where Unified CCE provides integrations to an ACD for Enterprise Routing, the following is true: Unified CCE system reports on ACD queue metrics. When Unified CCE software is used to provide initial call treatment and/or enterprise queuing, Unified CCE software reports on enterprise queue metrics. However, once the call is routed to an ACD the ACD may queue the call. In this
                                                         case, Unified CCE software reports on both enterprise queue and ACD queue metrics. Unified CCE system uses a Service Control VRU as the telephony platform for enterprise queuing. Reporting is the same whether Unified CCE script uses a Send To VRU node or a Translation Route To VRU node. |
|---|---|

| Note | Although the total abandons includes
                                                      calls that abandoned at the ACD, there is no separate count for only those
                                                      calls that abandoned at the ACD. |
|---|---|

| Note | None of the skill group metrics
                                          include time spent in self-service, or calls that ended during self-service. A
                                          call is not associated with a skill group until it is queued, and a call is
                                          queued after self-service is complete. |
|---|---|

| Note | Precision Routing is supported only on Unified CCE Communications Manager PG. |
|---|---|

| Note | Precision Routing is only supported for inbound Unified CCE agents. |
|---|---|