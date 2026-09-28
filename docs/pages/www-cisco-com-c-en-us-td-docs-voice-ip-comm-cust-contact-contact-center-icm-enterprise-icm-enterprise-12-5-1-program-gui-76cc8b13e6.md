---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-icm-enterprise-icm-enterprise-12-5-1-program-gui-76cc8b13e6
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/icm_enterprise/icm_enterprise_12_5_1/program/guide/ucce_b_cisco-contact-center-gateway-deployment12_5/ucce_b_cisco-contact-center-gateway-deployment12_5_chapter_01.html
retrieved_at: 2026-08-16T20:30:51.498460+00:00
---

Cisco Contact Center Gateway Deployment Guide for Cisco Unified ICM/CCE 12.5(1)

# Cisco Contact Center Gateway Deployment Guide for Cisco Unified ICM/CCE 12.5(1)

Updated: February 6, 2020

Chapter: Cisco Contact Center Gateway

## Chapter: Cisco Contact Center Gateway

# Cisco Contact Center Gateway

## Cisco Contact
                        	 Center Gateway Feature

The Cisco Contact Center
                           		Gateway feature uses the Unified CCE PG which connects the Unified ICM
                           		system to a Unified CCE system. Unified CCE Peripheral Gateway allows
                           		Unified CCE to appear as a traditional ACD connected to the Unified ICM system.
                           		The Unified CCE Gateway PG provides the Unified ICM system with a PG that
                           		communicates with the CTI interface of the Unified CCE System PG.

You can use the Cisco Contact Center Gateway feature for deployments
                           		with geographically distributed call centers. Each call center has remote
                           		survivability and administrative independence. You can integrate new contact 
                           		centers into an existing Unified ICM environment with many TDM ACD sites.
                           		Peripherals that are legacy ACDs and gateway types can use a single minimum
                           		expected delay (MED) script node to transfer a call to the best site.

Cisco Contact Center Gateway PG provides all standard Peripheral
                           		Interface Manager (PIM) data and functionality including:

- Call event notification

- Agent State notification

- Translation Routing

- Pre- and Post-Routing

- Real-time data

- Historical data

Cisco Contact Center Gateway also provides an autoconfiguration feature,
                           		which reduces the need for repeating configuration tasks between Unified CCE
                           		and the Unified ICM systems.

## Parent/Child
                        	 Deployments

The different roles of the
                           		systems in a Contact Center Gateway deployment are:

A parent ICM
                                             				  can have TDM PGs and Gateway PGs.

Each Unified CCE Peripheral Gateway in a child deployment can connect
                                       		  to only one Unified ICM parent instance. However, one Unified ICM parent
                                       		  instance can support multiple Unified CCE children.

When deploying the
                           		Contact Center Gateway, you first get the child system working and then
                           		integrate the child with the parent system. For reporting purposes, collocate
                           		the Unified CCE Gateway PG with the System PG on the child. Collocating the PGs
                           		helps to preserve connectivity. If the System PG and the Gateway PG lose
                           		connectivity, you can lose reporting data on call activity.

## Gateway
                        	 Autoconfiguration

Autoconfiguration is a Contact Center Gateway feature that automatically uploads basic configuration data from the child to
                           populate tables on the parent Unified ICM for the corresponding gateway PG. Autoconfiguration is enabled by default. The uploaded
                           tables contain agent, skill group, service, call type, and device information.

When autoconfiguration is enabled, the Configuration Manager on the Unified ICM parent does not permit manual configuration
                           of agents, and skill groups, services entries.

Upon startup, the PG PIM remembers the configuration level (keys) from
                           		the last time the PIM obtained configuration information. The PIM then requests
                           		current configuration information from the child and applies any configuration
                           		changes that were made at the child, while the parent Unified ICM system was disconnected from the child CCE system. While
                           the PIM is connected, it continues to make dynamic configuration
                           		changes and also updates the parent database to reflect the changes.

## Gateway Deployment
                        	 Types

This section discusses the supported Cisco Contact Center Gateway
                           		deployment models.

### Multiple Parents
                           	 with Single Child

This figure shows a deployment where two
                              		customers, each running a Unified ICM parent, outsource calls to a provider
                              		site running Unified CCE with System PGs. The provider site has two Unified CCE
                              		System PGs. Each System PG connects to the respective Unified CCE Gateway PG
                              		for its Unified ICM parent. By routing through separate PGS, this deployment
                              		prevents a customer from seeing the other customer's data. Each customer
                              		provides call treatment (prompting) and queuing using Cisco Unified Customer
                              		Voice Portal (Unified CVP) before routing calls to the provider site. The
                              		provider site can also queue calls using the Cisco Unified IP IVR (Unified IP
                              		IVR) that is connected to the System PG.

For this deployment, the agents are broken up into two peripherals, each
                              		on its own PG. If there is local queuing, a separate Unified IP IVR or Unified
                              		CVP is required. The provider realizes some economies over having a separate
                              		Unified CCE setup for each Unified ICM parent. The provider can use the same
                              		Unified CCE CallRouter, Logger, and AW/HDS to handle both customers.

You can use either Unified CVP or Unified IP IVR as the Voice Response
                                          		  Unit (VRU) on the child. The illustrated deployment uses Unified IP IVR.

Call
                                          		  types on the Unified CCE child must not span peripherals. Each peripheral on
                                          		  the child requires a separate set of Call Types. This requirement keeps the
                                          		  correlation between the Call Type on the child to a single peripheral on a
                                          		  parent. Otherwise, the Unified ICM parent (Services) sees only a subset of the
                                          		  calls that correspond to the Call Type on the child.

### Single Parent with
                           	 Multiple IP IVR-Based Children

This deployment shows a Unified ICM parent connected to two Unified CCE children with System PGs through two Unified CCE Gateway
                              PGs. Each Gateway PG can connect to only one System PG.

The Unified CCE child systems can be branch offices or service
                                          		  bureaus.

This deployment allows translation routing of calls from the Unified ICM
                              		parent to either of the two Unified CCE children. The parent treats each child
                              		as a separate ACD. In the example shown here, Unified CVP does the network
                              		queuing from the Unified ICM parent. This deployment model enables these
                              		possibilities:

The child sites can route incoming calls to itself through Voice Gateways that are not related to the parent site. This local
                                    routing ensures continued operations at the call center if the WAN connection is not reliable.

You can phase-in Unified CCE deployments alongside TDM ACDs. The option to add more Unified CCE child sites enables you to
                                    add capacity over time.

The child sites can post-route and translation route to other child sites through the parent site. These routing options enable
                                    transfers and consults between the child sites.

The parent site can control child sites that are either branch offices or one or more external service providers.

### Parent Unified CVP
                           	 Controls Multiple Child Unified CCE Sites

This figure shows a parent Unified ICM system deployed with Unified CVP and its own AW/HDS server. Each distributed site has
                              a complete Unified CCE deployment that loads both the Central Controller and the Unified CCE System PG. There is also a local
                              Administration & Data Server machine for the Unified CCE to perform that site's configuration, scripting, and reporting tasks.
                              The Unified CCE Gateway PG connects the Unified CCE child to the Unified ICM parent.

Unified CCE also supports CVP. But, information on queued calls at the child CVP is not available at the parent through the
                                          Unified CCE Gateway PG. That information is available when the child uses IP IVR. Because that information is not available,
                                          the parent cannot use minimum expected delay (MED) over services in its queueing when the child uses CVP.

In this deployment, the distributed Unified CCE systems act as their own local IP ACDs. The child sites have no visibility
                              to any of the other sites. Agents at Child 1 cannot see any of the calls or reports from Child 2. CVP provides a virtual network
                              queue across all the distributed sites controlled by the parent. The parent site has visibility into all the distributed sites
                              and sends the call to the next available agent from the virtual queue.

The Unified CVP at the parent site controls the calls coming into the
                              		distributed sites. The parent site's CVP provides call queuing and treatment in
                              		the VoiceXML Browser in the voice gateway. If the voice gateway at a child site
                              		loses its connection to the parent CVP, the child site uses its IP IVR for a
                              		local backup. The local IP IVR also provides local queue treatment when the
                              		local agents do not answer calls. For example, the local IP IVR can handle a
                              		Reroute On No Answer (RONA) call, rather than sending the call to the CVP to be
                              		requeued. But, the child sites cannot queue such calls to another child site.

If you use Unified CVP to queue at the child, this deployment never populates SkillGroupRealTime.CallsQueuedNow . However, if IP-IVR is used under System PG, you can see this status. Also, the Parent cannot use any function that depends
                              on queue statistics to operate properly. For example, MED is not accurate since it does not consider queue time on the CVP
                              peripheral.

## Routing in Gateway
                        	 Deployments

Routing is when a routing client (a PG or
                           		NIC) queries the CallRouter for a destination to which to send a call. The
                           		different types of routing use and pass different information and target
                           		different call destinations.

Before you can route calls to a child, both the parent and child require
                           		routing scripts.

### Call Data Transfer
                           	 Between Parent and Child

During a call flow, call data passes between the parent and child systems only during the following scenarios:

Data passes from the child to the parent when the child sends a ROUTE_REQUEST_EVENT to the parent. This event happens during
                                    a Translation Route dialog or a Post-Route dialog initiated from the child. The child raises the event when the child transfers
                                    a call to a route point that the parent controls.

Data passes from the parent to the child when the parent responds to a ROUTE_REQUEST_EVENT with a ROUTE_SELECT_EVENT. This
                                    event happens during a Translation routing dialog or a Post-Route dialog initiated from the child. This parent raises the
                                    event when the parent transfers a call at the child to a route point that the parent controls.

Data passes from the child to the parent when the child sends a CALL_DATA_UPDATE_EVENT after data is updated at the child.

In the
                              		parent-to-child or child-to-parent call flow, only a subset of call variables
                              		and ECC variables are passed to the call flow. MAPVAR and MAPECC variables (if
                              		present) filter all ECC and call variable transfers.

This table lists
                              		call data that is transferred between parent and child. Any variables not
                              		mentioned here are not transferred. You can only transfer ECC variables that
                              		have the same name on both systems. The table does not account for any
                              		additional restrictions that MAPVAR and MAPECC might import.

Item

To Parent
                                          					 in Route Request

To Child
                                          					 in Route Select

To Parent
                                          					 from Call Data update and other events

Call
                                          					 Variables 1-10

Yes

Yes

Yes

ECC
                                          					 Variables

Yes

Yes

Yes

ANI

Yes

No

No

User To
                                          					 User Info

Yes

No

No

Dialed
                                          					 Number (DNIS)

Yes

No

No

Caller
                                          					 Entered Digits(CED)

Yes

No

No

Call Wrap
                                          					 Up Data

No

No

Yes

For more information about Unified ICM variables, see the Configuration Guide for Cisco Unified ICM/Contact Center Enterprise at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-installation-and-configuration-guides-list.html .

## Reporting in
                        	 Gateway Deployments

There are two levels of reporting in Contact Center Gateway deployments:

ACD (child)

Enterprise (parent)

The addition of the
                           		Gateway PGs does not affect the reports on the ACD level; you can run Unified
                           		CCE reports that accurately reflect the state of the child system.

However, the data
                           		that the child system feeds to the parent does not always correlate on both
                           		systems. This lack of correlation affects the reports on the enterprise level.
                           		Discrepancies can occur due to timing period issues. Discrepancies can also
                           		occur because the Contact Center Gateway does not populate certain database
                           		fields.

The system cannot
                           		report on locally queued calls on a Unified CCE child that uses Unified CVP, so
                           		those calls are not reflected in the statistics.

For more information on reporting, see the Cisco Unified Contact Center Enterprise Reporting User Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-user-guide-list.html .

## Upgrade
                        	 Considerations for Gateway Deployments

You can upgrade the
                           		parent and child sites independently in a Parent/Child deployment, as long as
                           		you stay within the version compatibility bounds. If you are using Unified IP
                           		IVR, select a Unified CCE version that is compatible with the Unified
                           		Communications Manager version.

See the Contact Center Enterprise Compatibility Matrix at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-device-support-tables-list.html to determine the correct versions to use.

Consult the
                           		following documents for upgrade information as appropriate for your
                           		Parent/Child deployment:

Component

Documents

Unified
                                       					 Communications Manager

https://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-callmanager/tsd-products-support-series-home.html

Unified
                                       					 ICM or Unified CCE

https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-installation-guides-list.html

Unified
                                       					 CVP

https://www.cisco.com/c/en/us/support/customer-collaboration/unified-customer-voice-portal/tsd-products-support-series-home.html

| Note | A parent ICM
                                             				  can have TDM PGs and Gateway PGs. |
|---|---|

| Note | Each Unified CCE Peripheral Gateway in a child deployment can connect
                                       		  to only one Unified ICM parent instance. However, one Unified ICM parent
                                       		  instance can support multiple Unified CCE children. |
|---|---|

| Note | You can use either Unified CVP or Unified IP IVR as the Voice Response
                                          		  Unit (VRU) on the child. The illustrated deployment uses Unified IP IVR. |
|---|---|

| Note | Call
                                          		  types on the Unified CCE child must not span peripherals. Each peripheral on
                                          		  the child requires a separate set of Call Types. This requirement keeps the
                                          		  correlation between the Call Type on the child to a single peripheral on a
                                          		  parent. Otherwise, the Unified ICM parent (Services) sees only a subset of the
                                          		  calls that correspond to the Call Type on the child. |
|---|---|

| Note | The Unified CCE child systems can be branch offices or service
                                          		  bureaus. |
|---|---|

| Important | Unified CCE also supports CVP. But, information on queued calls at the child CVP is not available at the parent through the
                                          Unified CCE Gateway PG. That information is available when the child uses IP IVR. Because that information is not available,
                                          the parent cannot use minimum expected delay (MED) over services in its queueing when the child uses CVP. |
|---|---|

| Item | To Parent
                                          					 in Route Request | To Child
                                          					 in Route Select | To Parent
                                          					 from Call Data update and other events |
|---|---|---|---|
| Call
                                          					 Variables 1-10 | Yes | Yes | Yes |
| ECC
                                          					 Variables | Yes | Yes | Yes |
| ANI | Yes | No | No |
| User To
                                          					 User Info | Yes | No | No |
| Dialed
                                          					 Number (DNIS) | Yes | No | No |
| Caller
                                          					 Entered Digits(CED) | Yes | No | No |
| Call Wrap
                                          					 Up Data | No | No | Yes |

| Component | Documents |
|---|---|
| Unified
                                       					 Communications Manager | https://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-callmanager/tsd-products-support-series-home.html |
| Unified
                                       					 ICM or Unified CCE | https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-installation-guides-list.html |
| Unified
                                       					 CVP | https://www.cisco.com/c/en/us/support/customer-collaboration/unified-customer-voice-portal/tsd-products-support-series-home.html |