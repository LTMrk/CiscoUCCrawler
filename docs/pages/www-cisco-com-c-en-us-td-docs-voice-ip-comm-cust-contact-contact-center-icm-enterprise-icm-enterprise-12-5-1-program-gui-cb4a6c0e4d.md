---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-icm-enterprise-icm-enterprise-12-5-1-program-gui-cb4a6c0e4d
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/icm_enterprise/icm_enterprise_12_5_1/program/guide/ucce_b_cisco-contact-center-gateway-deployment12_5/ucce_b_cisco-contact-center-gateway-deployment12_5_chapter_011.html
retrieved_at: 2026-08-16T20:31:00.458665+00:00
---

Cisco Contact Center Gateway Deployment Guide for Cisco Unified ICM/CCE 12.5(1)

# Cisco Contact Center Gateway Deployment Guide for Cisco Unified ICM/CCE 12.5(1)

Updated: February 6, 2020

Chapter: Contact Center Gateway with Unifed CCE Deployment

## Chapter: Contact Center Gateway with Unifed CCE Deployment

# Contact Center Gateway with Unifed CCE Deployment

## Contact Center
                        	 Gateway Setup Prerequisities

Before setting up your Cisco Contact Center Gateway, complete these prerequisite steps:

Install and configure a Unified CCE child system. See the Cisco Unified Contact Center Enterprise Installation and Upgrade Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-installation-guides-list.html and the Configuration Guide for Cisco Unified ICM/Contact Center Enterprise at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-installation-and-configuration-guides-list.html for detailed instructions.

To enable call transfers from a parent cluster to a child cluster, first satisfy the Unified Communications Manager IP Telephony
                                             requirements. For example, deploy a Device Trunk such as H.225 Trunk (Gatekeeper Controlled) or Intercluster Trunk (Non-Gatekeeper
                                             Controlled). For more information, see the Cisco Unified Communications Manager documentation at https://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-callmanager/tsd-products-support-series-home.html .

Test your child Unified CCE system to verify that everything works correctly and that you can route calls.

Install and configure a Unified ICM parent system, which includes installing a redundant pair of Unified CCE Gateway PGs.

Collect the necessary configuration information. Although many elements are configured automatically, some elements require
                                 manual setup. For example, for the CTI Server, you need the host names or IP addresses and connection ports for Side A and
                                 Side B. You also need the Peripheral ID when setting up a system peripheral.

### Enable Application
                           	 Routing on Child

In the Configuration Manager
                                          			 of the Unified CCE child, select Tools > List
                                                				  Tools > Dialed Number/Script Selector
                                                				  List .

In the Attributes tab, check Permit Application Routing for those route
                                          			 points on which you post route or translation route to the parent.

### Special
                           	 Configuration for Unified CCE Child with Unified CVP

A Unified CCE child can use Unified CVP as its VRU.

A Unified CCE child system that uses Unified CVP requires the following:

The Unified CCE VRU Peripheral Gateway is mapped to the Unified Communications Manager routing label.

The Unified Communications Manager route pattern must be associated with the child Unified CVP.

The SIP static route for Unified CVP must point to the child Unified Communications Manager.

For more information on configuring Unified CVP, see the Configuration Guide for
                                       				  Cisco Unified Customer Voice Portal at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-customer-voice-portal/products-installation-and-configuration-guides-list.html .

### Configure the
                           	 Unified CCE Gateway PG

Start the Configuration
                                          			 Manager on the Admin Workstation.

Follow the standard procedure for installing a PG 
                                          			 with the following
                                          			 Unified CCE Gateway-specific settings:

- In the Peripheral Gateway Properties dialog, for Client Type Selection , select Unified CCE Gateway as your “switch” PG
                                             				type.

- You cannot also
                                             				select VRU. If you attempt to add a VRU in this case, an error message appears.

- In the Advanced tab of the PG Explorer, ensure that Agent autoconfiguration is disabled for the
                                             				Unified CCE Gateway PG to function properly.

#### What to do next

When you bring up the Gateway PG, the autoconfiguration takes place.

### Other
                           	 Configuration on the Parent

Some autoconfiguration happens between the parent and child. You
                              		configure other elements manually in the Configuration Manager so that call
                              		flows work properly:

Configure a Network Trunk Group and a Trunk Group on the Unified CCE Gateway PG. This task is used when configuring peripheral
                                    targets.

Configure Routes, Peripheral Targets, and Labels for the routing clients for the autoconfigured Services (child call types).
                                    The routing clients are the Unified CCE Gateway PG and the parent VRU (either Unified CVP or Unified IP IVR). Configure corresponding
                                    route points that match the labels in Unified Communications Manager. Add the labels to the child as dialed numbers with Permit
                                    Application Routing enabled.

Add the autoconfigured Skill Groups as Service Members. If you do not add these Service Members, you cannot use MED.

To pass call context from the parent to the child, you must translation route all calls. Create translation routes, routes,
                                    peripheral targets, and labels for the Unified CCE Gateway PG and the parent routing clients.

See the Configuration Guide for Cisco Unified ICM/Contact Center Enterprise at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-installation-and-configuration-guides-list.html for more information.

### Script to Verify
                           	 Deployment

Create a script that can interact with the Unified CCE Gateway to verify your deployment. Be sure that the script targets
                              a skill group, either directly or through a service. For example, you can create scripts for Longest Available Agent (LAA)
                              for skill groups and Minimum Expected Delay (MED) for Services. If the script uses a translation route, create the translation
                              route before you create the script.

For more information about scripting, see the Scripting and Media Routing Guide for Cisco Unified ICM/Contact Center Enterprise at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-user-guide-list.html .

For instructions on creating a Translation Route, see Configuration Guide for Cisco Unified ICM/Contact Center Enterprise at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-installation-and-configuration-guides-list.html .

### Unified ICM
                           	 Service Startup

You start the Unified ICM Service for the Enterprise Gateway PG in the Unified ICM Service Control dialog. Select the Services
                              name for the Enterprise Gateway PG and click Start.

After the child and the parent Unified ICM establish a connection, the
                              		child configuration propagates to the parent Unified ICM Configuration Manager.
                              		Agent configuration information on the child propagates to the parent. The
                              		agent information is dimmed on the parent because you cannot modify or delete
                              		that information at the parent level.

For general information about Unified ICM Service Control, see the Configuration Guide for Cisco Unified ICM/Contact Center Enterprise at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-installation-and-configuration-guides-list.html .

## Enterprise Gateway
                        	 Autoconfiguration

Follow the same procedure
                           		as Autoconfiguration with Enterprise Gateway .

### Autoconfiguration
                           	 Maintenance

The following points provide help with autoconfiguration
                              		maintenance:

- You can find errors from the
                                 		  last run of the autoconfiguration dialog in the AutoConfigError.txt file. The file is in the main
                                 		  PG directory for a Unified CCE Gateway PG, for example, C:\icm\cust1\PG1A\AutoConfigError.txt . You can
                                 		  view the file with any text editor. The file contains the time and date and a brief error message as to why an
                                 		  element could not be configured. If this file does not exist, that means the
                                 		  last configuration run was clean.

- Periodically, manually
                                 		  delete entries in the Service, Agent, and Skill Group tables that allow
                                 		  deletion. An item that does not allow deletion shows a circle with a line
                                 		  through it next to the item. You can delete items on the parent after they are
                                 		  deleted on the child. When you delete an item on the child, the parent does not
                                 		  also delete that item automatically.

- Most autoconfiguration
                                 		  errors occur (in Enterprise cases) because of deleted records. Use the Deleted
                                 		  Objects tool in the parent to permanently delete any deleted records. You can
                                 		  access this tool in Configuration Manager by choosing Tools > Miscellaneous
                                       				Tools > Deleted Objects . This
                                 		  task reduces the number of autoconfiguration errors. The fewer records that are
                                 		  marked for deletion that still exist, the smaller the chance that
                                 		  autoconfiguration gets duplicate errors when creating objects.

Do not confuse Contact Center Gateway autoconfiguration with Agent
                                          		  autoconfiguration. (Agent autoconfiguration is an option available on the
                                          		  Advanced tab in the PG Explorer.) Ensure that Agent autoconfiguration is
                                          		  disabled so that the Unified CCE Gateway PG can function properly.

## Enterprise Gateway
                        	 Routing

The script on the Unified ICM parent interacts with the Unified CCE
                           		Gateway PG.

Ensure that all remotely handled route points (Application routing
                           		enabled) have default "local" scripts. The default "local" script runs in case
                           		no host (parent) is available. Include Post Route points in the scripts as well
                           		as translation route destinations.

The following simple routing
                           		script has an LAA node. That node selects the skill
                           		group with the longest available agent (if an agent is available) among skill
                           		groups on the same ACD or a different ACD. If no agents are available, then the
                           		script selects the Service with the Minimum Expected Delay (MED) among the
                           		services on the same or a different ACD.

Scripting in a Contact Center Gateway deployment is no different than
                                       		  the scripting between Unified ICM and all other TDMs. Either skill groups or
                                       		  services are targeted, not agents.

### Routing
                           	 Configuration

To Post-route a call from the child Unified CCE to the parent
                              		Unified ICM, you must:

- Create a transfer number on
                                 		  the child's Unified Communications Manager cluster as a CTI Route Point (a
                                 		  Unified Communications Manager object). When an agent on the child wants to
                                 		  post-route a callback through Unified ICM, the call transfers to that dialed
                                 		  number.

- Configure the transfer
                                 		  number in both the child and the parent. In the child, tag the number to allow
                                 		  application routing. Application routing means that the route request passes up
                                 		  to the parent for a response. In case the parent does not respond, the child
                                 		  also needs backup scripting to handle the call locally.

You cannot use the DN for a CTI Route Point on a different CTI Route Point in another partition. Ensure that DNs are unique
                                          across all CTI Route Points on all partitions.

In the Parent, you must:

- Create the dialed number for
                                 		  the transfer CTI Route Point.

- Build a call type and
                                 		  associated script to perform the post-route in the parent Unified ICM.

The parent script can instruct the child system:

- To transfer the call to
                                 		  another child (through a translation route to the other child's skill group).

- To transfer the call to a
                                 		  destination on the same child.

Or with Unified CVP, the script can instruct CVP to connect the
                                    			 callback to the network queue (provided the call came from there originally).

If CVP is present at the Parent, the Parent/Child design assumes
                                    			 that the parent CVP gets all the calls first and is the network queue point.
                                    			 That assumption does simplify the call delivery, RONA, and subsequent
                                    			 transfers.

If you use Unified IP IVR to do the enterprise queuing at the parent
                              		Unified ICM, be aware of the following:

- There is no built-in RONA
                                 		  timeout for that model, like Cisco has with CVP. In the IP IVR case, you must
                                 		  script locally for RONA at the Child. In that script, you can reroute the call
                                 		  to the parent Unified ICM or hold the call in queue locally for the next local
                                 		  agent.

- For subsequent transfers
                                 		  between child systems, there is extra work to translation route the calls to
                                 		  the parent IP IVR in the parent post-routing script.

In the child, you must:

- Create the dialed number for
                                 		  the transfer CTI Route Point.

- Enable application routing
                                 		  and build backup treatment in case the parent does not respond. The call sits
                                 		  in a CTI Route Point that can timeout. So, you need a way to deal with that
                                 		  call when the Unified ICM does not return a route.

The following routing scripts show sample parent and child call flow
                              		configurations. The first script runs the external script, ICMVisibleQAnn1,
                              		that uses Unified CVP for network queuing in the Parent system:

The second
                              		script runs an external script, VisibleQ, that uses Unified IP IVR for queuing
                              		in the Child system:

### Translation
                           	 Routing

A translation route is a special destination for
                              		a call that allows you to deliver call information along with the call.
                              		Translation routing maintains the association between a call and its related
                              		data throughout the life of the call. Translation routing plays a significant
                              		role in the accuracy of reporting and allows for "cradle-to-grave" call
                              		tracking and reporting. Some reporting metrics for call types and skill groups
                              		are applicable only if calls are translation-routed.

The call is delivered first to the translation route. While the routing
                              		client processes the call, the Unified ICM delivers the final destination for
                              		the call to the PG with any other necessary information. The peripheral then
                              		works with the PG to reroute the call and the appropriate information to the
                              		ultimate target.

You can create a translation route with either the Translation Route
                              		Explorer or the Translation Route Wizard. If you create a translation route
                              		with the Wizard, you can later modify it through the Explorer. The Wizard is
                              		helpful when creating multiple translation routes. After you create the
                              		translation route, you create a translation route script.

#### Create Translation
                              	 Route with Translation Route Explorer

You can define translation routes in the Unified ICM Configuration
                                    		  Manager with the Translation Route Explorer. See the
                                    		  online help for information on the specific fields in the Explorer.

In the Configuration Manager,
                                             			 select Tools > Explorer
                                                   				  Tools > Translation Route
                                                   				  Explorer .

Set up a translation route associated with the peripheral.

Set up one or more routes and associated peripheral targets for
                                             			 the translation route.

Set up a label on the original routing client for the call to
                                             			 access each of the peripheral targets associated with the translation route.

For each peripheral target that you want to access through a
                                             			 translation route, set up a label with the peripheral as the routing client.

#### Create Translation
                              	 Route with Translation Route Wizard

##### Before you begin

Before you begin creating the translation route, configure a
                                    		  Peripheral Gateway (PG), Network Trunk Group, Routing Clients, Trunk Groups,
                                    		  and Trunks.

Before using the Translation Route Wizard , go to Tools > Explorer
                                          				Tools > PG Explorer . On the Peripheral tab, check the Enable post routing option. In the Routing client tab, name the routing client.

This example procedure is for a relatively simple deployment model
                                                			 that has one parent, one child, and Unified CVP at the parent.

In the Configuration Manager,
                                             			 select Tools > Wizards > Translation
                                                   				  Route Wizard .

Click Next .

Select Create New and click Next .

Enter a long name for the translation route in the Name . Click Next .

From the drop-down list, select Single peripheral, multiple routing clients and click Next .

Select the PG for the Unified CCE Gateway PG from the Peripheral Gateway list and the peripheral for
                                             			 that PG from the Peripheral list. Click Next .

Select routing clients from the Post Routing Client list for the Unified CCE
                                             			 Gateway PG and for Unified CVP. Do not select anything from the Pre Routing Client list. The Dialed Number list is dimmed, so you cannot
                                             			 select any dialed numbers. Click Next .

Select the routing client for the Gateway PG and click Add . Then select the routing client for
                                             			 Unified CVP and click Add .

Click Next .

The DNIS is the value the network returns to the Gateway or
                                                            				  Unified Communications Manager to indicate the dialed number. If the DNIS is
                                                            				  attached to a route, the route must have its Service field populated. You do
                                                            				  not have to define the DNIS in the Unified ICM database.

Click Add DNIS range and enter a beginning DNIS
                                             			 (such as 1110000) and an ending DNIS (such as 1110010). Then, click OK .

For simplicity, use the same DNIS and label, and click Next .

Click Set prefix = DNIS for each routing client.

The label does not always match the DNIS. Usually the label
                                                            				  consists of a prefix (for example, 1800123), followed by the DNIS.

Select the Include DNIS string as is radio button, and
                                             			 click OK .

Click Next .

Click Create Translation Route .

After getting a success message, run a Translation Route Configuration Report and
                                             			 check the values.

### Configure Unified IP IVR for Translation Routing

If you use Unified IP IVR instead of Unified CVP in a translation route, there are some extra configurations necessary in Unified IP IVR. You add a Unified ICM translation routing application, and then assign a JTAPI trigger to this application.

Before configuring a translation routing application, first upload the VRU scripts required by the application.

In Unified CCE Administration, select Applications > Application Management .

Click Add a New Application .

From the Application Type drop-down menu, select Unified ICM  Translation Routing .

Enter the name of the Unified CCE translation routing script in the Name field.

Press Tab to automatically populate the Description field.

In the ID field, accept the ID, or enter a unique ID.

In Maximum Number of Sessions field, enter the maximum number of simultaneous sessions that the application can handle.

In the Enabled field, accept the default radio button Yes .

In the Timeout field, enter a value.

From the Default Script drop-down, choose the script to runs when a system error occurs or when the Unified ICM routes to the default treatment.

Click Add .

Click OK .

Click Add New Trigger .

From the Trigger Type drop-down menu, select Unified CM/Unified CME Telephony and click Next .

In Unified CCE Administration, select Subsystems > Unified CM Telephony .

On the Unified CM Telephony Configuration navigation bar, click the Unified CM Telephony Triggers hyperlink.

Click Add a New Unified CM Telephony Trigger .

Complete the fields on this page (see the online Help for additional information), then click Add .

### Call Flow Creation Tips

Before creating a call flow, consider the following:

- Network Consultative transfer is not supported with Unified CVP in a Parent/Child environment. Disable network transfer for
                                 the call flow to work.

- Use the IP address, not a name, when configuring SIP trunks on Cisco Unified CallManager.

### Call Flow with Unified CVP at Parent

Typically, a parent Unified ICM system (including CVP, VXML, and PSTN gateways) is located in a different location than a
                              child Cisco Unified CCE system. This section describes a sample Parent/Child call flow; the components and the configuration
                              were tested and verified in this contact center test environment.

This call flow information was taken from the Cisco Tested Call Flows page at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/uc_system/UC8-0-2/cc_system_arch/ch4_flow.html?dtid=osscdc000283 . See that site for additional information about the necessary configuration and scripting for these call flows.

In this call flow, the CVP Application Browser, CVP SIP subsystem service, and Media Server are represented as separate entities.
                                          However, they are all on the same  CVP call control server.

The call flow on the Parent system works as follows:

The call comes from the PSTN into an IOS SIP Gateway that originates a SIP call to Unified SIP Proxy.

Unified SIP Proxy sends the SIP call to the CVP SIP subsystem service.

The Unified CVP SIP subsystem service sends the details of the call to the Unified CVP Call Server using HTTP.

The Unified CVP Call Server sends a NEW_CALL event to the Unified ICM.

Unified ICM, upon receipt of the NEW_CALL event, sends a temporary Connect label to connect a VRU to the Unified CVP Call
                                    Server.

The Unified CVP Call Server sends the label with a correlation ID to the CVP SIP subsystem service.

The Unified CVP SIP subsystem service sends the label to Unified SIP Proxy.

Unified SIP Proxy sends the call to the VXML gateway.

The VRU functionality of the PSTN Gateway sends a message to the appropriate Unified CVP Call Server. The Call Server, in
                                    turn, sends a REQUEST_INSTRUCTION message to Unified ICM.

Unified ICM uses the correlation ID. The correlation ID was relayed to Unified ICM, with the call that it processed earlier,
                                    as a part of the REQUEST_INSTRUCTION message.

Unified ICM, upon receipt of the REQUEST_INSTRUCTION message, also sends a CONNECT_TO_RESOURCE event back to the Unified CVP
                                    Call Server.

The Unified CVP Call Server acknowledges Unified ICM with a RESOURCE_CONNECTED event. Then, Unified ICM executes the routing
                                    script that is enabled for that call.

Upon execution of the routing script by Unified ICM, the Unified CVP Call Server gets a RUN_SCRIPT_REQ event from Unified
                                    ICM.

The Unified CVP Call Server runs the script and sends instructions to the Unified CVP SIP subsystem client (PSTN GW) by HTTP
                                    (VXML) to play the media file.

The Unified CVP SIP subsystem client sends HTTP requests to the HTTP Media Server to get the media file. The client then plays
                                    the media file out to the caller.

The contents of the media file request the caller to respond to the prompts in the recording.

The Unified CVP SIP subsystem client detects the response or caller-entered digits (CED). The client sends the response to
                                    the Unified CVP Call Server which then forwards the response to Unified ICM.

Unified ICM does the following:

Receives the CED and determines the appropriate child system to handle the call by returning a label for the peripheral target.
                                          In this example, the peripheral is the child Unified ICM.

Sends a PRE_ROUTE message to the Unified CCE Gateway.

Unified ICM instructs the Unified CVP Call Server, with a CONNECT event, to start setting up the IP Transfer to the peripheral
                                    target. In this example, the label for the peripheral target is defined as a CTI route point on the Unified Communications
                                    Manager in the child system.

The Unified CVP Call Server sends a VXML Transfer to the Unified CVP SIP subsystem service to start call setup to the peripheral
                                    target.

The Unified CVP SIP subsystem service sends several SIP messages to Unified SIP Proxy to:

Open and close the appropriate RTP path to the originating PSTN Gateway and the VRU.

Set up the call to the child Unified Communications Manager.

The call arrives at the translation route destination on the child system.

#### Agent Available on Child

After the call arrives in the Child System, the call flow works as follows if an agent is available:

- The call comes to the CTI route point on the Unified Communications Manager of the child system. Unified Communications Manager
                                    sends a ROUTE_REQUEST message (to determine that the Gateway PG is registered for control of this route point) to the System
                                    PG for Unified CCE.

- The System PG for Unified CCE recognizes that the route point is registered by the parent Gateway PG. The System PG then sends
                                    a ROUTE_REQUEST message to the Unified CCE Gateway PG.

- The Unified CCE Gateway PG matches up the DNIS on the route point (translation route). The PG then responds with a ROUTE_SELECT
                                    (and a label), which is a CTI route point on the child Unified Communications Manager and also a configured DN on the child.

- The System PG for Unified CCE sends the ROUTE_RESPONSE to the child Unified Communications Manager.

- Because the response is a configured DN, the System PG  sends a NEW_CALL to the child Unified CCE Rogger.

- The CallRouter runs a script, selects an available agent, and returns a Connect for the label of that agent device.

- The System PG for Unified CCE returns a ROUTE_RESPONSE to the Unified Communications Manager.

- The call reaches an available agent.

#### Agent Unavailable on Child

After the call arrives in the Child System, the call flow works as follows if an agent is not available:

- The call comes to the CTI route point on the Unified Communications Manager of the child system. Unified Communications Manager
                                    sends a ROUTE_REQUEST message (to determine that the Gateway PG is registered for control of this route point) to the System
                                    PG for Unified CCE.

- The System PG for Unified CCE recognizes that the route point is registered by the parent Gateway PG. The System PG then sends
                                    a ROUTE_REQUEST message to the Unified CCE Gateway PG.

- he Unified CCE Gateway PG matches up the DNIS on the route point (translation route). The PG then responds with a ROUTE_SELECT
                                    (and a label), which is a CTI route point on the child Unified Communications Manager and also a configured DN on the child.

- The System PG for Unified CCE sends the ROUTE_RESPONSE to the child Unified Communications Manager.

- Because the response is a configured DN, the System PG  sends a NEW_CALL to the child Unified CCE Rogger.

- The script determines the skill group that can best answer the call and checks for agent availability. Since an agent is unavailable
                                    to answer the call, the Unified CCE script places the call in a queue for the specific skill group.

On Unified IP IVR, this CTI route point is defined as a JTAPI Trigger. Unified IP IVR is in the same Unified Communications
                                                   Manager cluster as the call.

- When the call arrives, the JTAPI link on Unified Communications Manager informs Unified IP IVR, which in turn informs the
                                    System PG for Unified CCE.

- When the System PG for Unified CCE receives the incoming call arrival message, the System PG sends a REQUEST_INSTRUCTION to
                                    the Unified CCE Router.

- Unified CCE  instructs Unified IP IVR, through the System PG, to play the queue messages for the caller with a RUN_SCRIPT.
                                    The queue messages continue until an agent is available to take the call.

- Sends a PRE_CALL message to the System PG for Unified CCE with call context information. The System PG reserves the agent
                                          and waits for the call to arrive at the agent phone.

- Instructs Unified IP IVR to redirect the call from the agent queue to the available agent through the System PG.

- Unified IP IVR then sends the call to the Unified Communications Manager. The call then continues through  the call flow for
                                    an available agent.

### Call Flow with Translation Route

The following routing script uses a translation route. The routing script supports a call flow where the call originates at the child Unified CVP and no agent is available. The call is then queued locally until an agent
                              becomes available to answer the call.

#### Queue to Unified CVP on Child

Populate the following Set Variable nodes (used with Unified CVP):

call.user.microapp.media_server = <voice_browser_address>

call.user.microapp.locale = en-us

call.user.microapp.app_media_lib = app

Add a Queue to Skill Group and call it SG1 .

Add Run External Script nodes that run the CVPCallImportant script.

Save the script and activate it.

| Note | To enable call transfers from a parent cluster to a child cluster, first satisfy the Unified Communications Manager IP Telephony
                                             requirements. For example, deploy a Device Trunk such as H.225 Trunk (Gatekeeper Controlled) or Intercluster Trunk (Non-Gatekeeper
                                             Controlled). For more information, see the Cisco Unified Communications Manager documentation at https://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-callmanager/tsd-products-support-series-home.html . |
|---|---|

| Step 1 | In the Configuration Manager
                                          			 of the Unified CCE child, select Tools > List
                                                				  Tools > Dialed Number/Script Selector
                                                				  List . |
|---|---|
| Step 2 | In the Attributes tab, check Permit Application Routing for those route
                                          			 points on which you post route or translation route to the parent. Check this option for dialed numbers from the
                                          			 parent, for translation routing DNIS/Label for the parent, and for anything
                                          			 transferred from the parent by post routing. |

| Step 1 | Start the Configuration
                                          			 Manager on the Admin Workstation. |
|---|---|
| Step 2 | Follow the standard procedure for installing a PG 
                                          			 with the following
                                          			 Unified CCE Gateway-specific settings: In the Peripheral Gateway Properties dialog, for Client Type Selection , select Unified CCE Gateway as your “switch” PG
                                             				type. You cannot also
                                             				select VRU. If you attempt to add a VRU in this case, an error message appears. In the Advanced tab of the PG Explorer, ensure that Agent autoconfiguration is disabled for the
                                             				Unified CCE Gateway PG to function properly. |

| Note | Do not confuse Contact Center Gateway autoconfiguration with Agent
                                          		  autoconfiguration. (Agent autoconfiguration is an option available on the
                                          		  Advanced tab in the PG Explorer.) Ensure that Agent autoconfiguration is
                                          		  disabled so that the Unified CCE Gateway PG can function properly. |
|---|---|

| Note | Scripting in a Contact Center Gateway deployment is no different than
                                       		  the scripting between Unified ICM and all other TDMs. Either skill groups or
                                       		  services are targeted, not agents. |
|---|---|

| Note | You cannot use the DN for a CTI Route Point on a different CTI Route Point in another partition. Ensure that DNs are unique
                                          across all CTI Route Points on all partitions. |
|---|---|

| Step 1 | In the Configuration Manager,
                                             			 select Tools > Explorer
                                                   				  Tools > Translation Route
                                                   				  Explorer . The Translation Route Explorer dialog appears. |
|---|---|
| Step 2 | Set up a translation route associated with the peripheral. You do not need a separate translation route for each possible
                                             			 skill target at the site. But, you need at least one translation route for each
                                             			 peripheral that you want to target. For example, if Peripherals A and B both
                                             			 route only to Peripheral C, you only need translation routes on Peripheral C.
                                             			 You need labels for Peripheral A and Peripheral B as well. |
| Step 3 | Set up one or more routes and associated peripheral targets for
                                             			 the translation route. Typically, all peripheral targets for a translation route refer
                                             			 to the same trunk group, but with different Dialed Number Identification
                                             			 Service (DNIS) values. |
| Step 4 | Set up a label on the original routing client for the call to
                                             			 access each of the peripheral targets associated with the translation route. |
| Step 5 | For each peripheral target that you want to access through a
                                             			 translation route, set up a label with the peripheral as the routing client. The online help guides you through completion of the fields in the Explorer. More detailed information can be found in the
                                             Configuration Guide for Cisco Unified ICM/Contact Center Enterprise. |

| Note | This example procedure is for a relatively simple deployment model
                                                			 that has one parent, one child, and Unified CVP at the parent. |
|---|---|

| Step 1 | In the Configuration Manager,
                                             			 select Tools > Wizards > Translation
                                                   				  Route Wizard . The Translation Route Wizard appears. |
|---|---|
| Step 2 | Click Next . The Select Configuration Task page appears. |
| Step 3 | Select Create New and click Next . The Define Translation Route page appears. The left
                                             			 panel shows the entities that are defined while using the Translation Route
                                             			 Wizard. |
| Step 4 | Enter a long name for the translation route in the Name . Click Next . The Short name field automatically populates based
                                             			 on the long name. The short name is used in forming target names. You can also
                                             			 enter an optional Description . The Select Configuration page opens. |
| Step 5 | From the drop-down list, select Single peripheral, multiple routing clients and click Next . The Select Peripheral Gateway, Peripherals, and
                                                				Services page opens. |
| Step 6 | Select the PG for the Unified CCE Gateway PG from the Peripheral Gateway list and the peripheral for
                                             			 that PG from the Peripheral list. Click Next . The service is the call type that propagated from the child to
                                             			 the parent. The Select Routing Clients and Dialed Numbers page
                                             			 opens. |
| Step 7 | Select routing clients from the Post Routing Client list for the Unified CCE
                                             			 Gateway PG and for Unified CVP. Do not select anything from the Pre Routing Client list. The Dialed Number list is dimmed, so you cannot
                                             			 select any dialed numbers. Click Next . The Select Network Trunk Groups for Routing Clients page opens. |
| Step 8 | Select the routing client for the Gateway PG and click Add . Then select the routing client for
                                             			 Unified CVP and click Add . The Routing Client and Network Trunk Group information appears at the
                                             			 bottom of the page. |
| Step 9 | Click Next . The Configure DNIS page opens. Note The DNIS is the value the network returns to the Gateway or
                                                            				  Unified Communications Manager to indicate the dialed number. If the DNIS is
                                                            				  attached to a route, the route must have its Service field populated. You do
                                                            				  not have to define the DNIS in the Unified ICM database. | Note | The DNIS is the value the network returns to the Gateway or
                                                            				  Unified Communications Manager to indicate the dialed number. If the DNIS is
                                                            				  attached to a route, the route must have its Service field populated. You do
                                                            				  not have to define the DNIS in the Unified ICM database. |
| Note | The DNIS is the value the network returns to the Gateway or
                                                            				  Unified Communications Manager to indicate the dialed number. If the DNIS is
                                                            				  attached to a route, the route must have its Service field populated. You do
                                                            				  not have to define the DNIS in the Unified ICM database. |
| Step 10 | Click Add DNIS range and enter a beginning DNIS
                                             			 (such as 1110000) and an ending DNIS (such as 1110010). Then, click OK . The DNIS list appears on the page with all the numbers in
                                             			 the range listed. |
| Step 11 | For simplicity, use the same DNIS and label, and click Next . The Configure Label page opens. |
| Step 12 | Click Set prefix = DNIS for each routing client. A Set Prefix = DNIS page opens. Note The label does not always match the DNIS. Usually the label
                                                            				  consists of a prefix (for example, 1800123), followed by the DNIS. | Note | The label does not always match the DNIS. Usually the label
                                                            				  consists of a prefix (for example, 1800123), followed by the DNIS. |
| Note | The label does not always match the DNIS. Usually the label
                                                            				  consists of a prefix (for example, 1800123), followed by the DNIS. |
| Step 13 | Select the Include DNIS string as is radio button, and
                                             			 click OK . The DNIS , Label , and Prefix lists populate with the numbers. |
| Step 14 | Click Next . The final page appears. |
| Step 15 | Click Create Translation Route . |
| Step 16 | After getting a success message, run a Translation Route Configuration Report and
                                             			 check the values. For a Parent/Child deployment to work properly, the configuration
                                             			 of the Parent, Child, Unified Communications Manager, Unified CVP, and the IOS
                                             			 gateway must match. Add all the numbers in the translation route to the child
                                             			 Unified CCE (as Dialed Numbers with Permit Application Routing enabled) and
                                             			 Unified Communications Manager (as Route Points). Ensure that the numbers match
                                             			 across the deployment (parent, child, and Unified Communications Manager). |

| Note | The DNIS is the value the network returns to the Gateway or
                                                            				  Unified Communications Manager to indicate the dialed number. If the DNIS is
                                                            				  attached to a route, the route must have its Service field populated. You do
                                                            				  not have to define the DNIS in the Unified ICM database. |
|---|---|

| Note | The label does not always match the DNIS. Usually the label
                                                            				  consists of a prefix (for example, 1800123), followed by the DNIS. |
|---|---|

| Note | Before configuring a translation routing application, first upload the VRU scripts required by the application. |
|---|---|

| Step 1 | In Unified CCE Administration, select Applications > Application Management . |
|---|---|
| Step 2 | Click Add a New Application . |
| Step 3 | From the Application Type drop-down menu, select Unified ICM  Translation Routing . |
| Step 4 | Enter the name of the Unified CCE translation routing script in the Name field. |
| Step 5 | Press Tab to automatically populate the Description field. |
| Step 6 | In the ID field, accept the ID, or enter a unique ID. This field corresponds to the service identifier of the call that was reported to the Cisco Unified ICM and configured in
                                          the Unified ICM translation route. |
| Step 7 | In Maximum Number of Sessions field, enter the maximum number of simultaneous sessions that the application can handle. |
| Step 8 | In the Enabled field, accept the default radio button Yes . |
| Step 9 | In the Timeout field, enter a value. This value is the maximum number of seconds that the system waits to invoke the application before rejecting a contact. |
| Step 10 | From the Default Script drop-down, choose the script to runs when a system error occurs or when the Unified ICM routes to the default treatment. |
| Step 11 | Click Add . A message confirms successful execution. |
| Step 12 | Click OK . |
| Step 13 | Click Add New Trigger . The Add a New Trigger page opens. |
| Step 14 | From the Trigger Type drop-down menu, select Unified CM/Unified CME Telephony and click Next . |
| Step 15 | In Unified CCE Administration, select Subsystems > Unified CM Telephony . |
| Step 16 | On the Unified CM Telephony Configuration navigation bar, click the Unified CM Telephony Triggers hyperlink. The Unified CM Telephony Trigger Configuration summary web page opens. |
| Step 17 | Click Add a New Unified CM Telephony Trigger . The Unified CM Telephony Trigger Configuration web page opens. |
| Step 18 | Complete the fields on this page (see the online Help for additional information), then click Add . The Unified CM Telephony Trigger Configuration summary web page opens, displaying the new Unified CM Telephony trigger. |

| Note | This call flow information was taken from the Cisco Tested Call Flows page at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/uc_system/UC8-0-2/cc_system_arch/ch4_flow.html?dtid=osscdc000283 . See that site for additional information about the necessary configuration and scripting for these call flows. |
|---|---|

| Note | In this call flow, the CVP Application Browser, CVP SIP subsystem service, and Media Server are represented as separate entities.
                                          However, they are all on the same  CVP call control server. |
|---|---|

| Note | On Unified IP IVR, this CTI route point is defined as a JTAPI Trigger. Unified IP IVR is in the same Unified Communications
                                                   Manager cluster as the call. |
|---|---|

| Step 1 | Populate the following Set Variable nodes (used with Unified CVP): call.user.microapp.media_server = <voice_browser_address> call.user.microapp.locale = en-us call.user.microapp.app_media_lib = app |
|---|---|
| Step 2 | Add a Queue to Skill Group and call it SG1 . |
| Step 3 | Add Run External Script nodes that run the CVPCallImportant script. |
| Step 4 | Save the script and activate it. |