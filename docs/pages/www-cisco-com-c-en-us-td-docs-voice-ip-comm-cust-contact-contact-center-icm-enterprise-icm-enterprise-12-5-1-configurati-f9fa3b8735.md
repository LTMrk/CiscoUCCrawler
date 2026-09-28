---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-icm-enterprise-icm-enterprise-12-5-1-configurati-f9fa3b8735
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/icm_enterprise/icm_enterprise_12_5_1/configuration/guide/ucce_b_1251-configuration-guide-unified-cce/ucce_b_1251-configuration-guide-unified-cce_chapter_01001.html
retrieved_at: 2026-08-16T14:51:24.787449+00:00
---

Configuration Guide for Cisco Unified ICM/Contact Center Enterprise, Release 12.5(1)

# Configuration Guide for Cisco Unified ICM/Contact Center Enterprise, Release 12.5(1)

Updated: February 5, 2020

Chapter: Routing and Routing Targets

## Chapter: Routing and Routing Targets

# Routing and Routing Targets

## Routes and Targets
                        	 Subsystem

For every routing
                              		  request it processes, the system software determines an announcement to be
                              		  played to the caller, a route for the call, or a special action such as
                              		  ring-no-answer or signal busy.

To see the elements
                              		  of the routes and targets subsystem and the order in which you must define
                              		  them, see the following figure. Note that elements in this subsystem depend on
                              		  elements defined in the routing client and peripheral subsystems. For example,
                              		  you must define a network trunk group and trunk group, which are part of the
                              		  peripheral subsystem, before you can define a peripheral target.

### Routing Targets

The system software can route a call to a carrier resource such as an
                                 		  announcement or to a target at a peripheral. A peripheral, such as an ACD, PBX,
                                 		  or Unified Communications Manager (Unified CM) dispatches calls within a contact center.

#### Peripheral
                              	 targets

Depending on the
                                 		capabilities of the peripheral and the type of routing instructions you use,
                                 		the system software might choose a specific agent at the peripheral to handle
                                 		the call. In that case, the peripheral merely dispatches the call to the chosen
                                 		agent. In other cases, the system software might specify only a group of agents
                                 		or a type of service to be provided to the caller.

The system software
                                 		can route to three types of peripheral targets:

Agent . A specific
                                       			 individual who receives calls through the peripheral. (The system software,
                                       			 however, cannot guarantee that the specific agent will be available when the
                                       			 call arrives.) The Queue to Agent node allows the targeting of a task (the work
                                       			 performed by an agent) to a script-specified agent. This node enables an agent
                                       			 to receive and operate on more than one task at a time.

Skill group . A group of
                                       			 agents who share a common set of skills and who can, therefore, all handle a
                                       			 specific type of calls. Each skill group contains one or more agents. If
                                       			 supported by the peripheral, each agent can be a member of more than one skill
                                       			 group.

Service . A type of
                                       			 processing the caller requires. For example, a peripheral might have services
                                       			 defined for sales, technical support, or opening new accounts. Each service has
                                       			 one or more skill groups whose members can provide the service. Each skill
                                       			 group can be associated with more than one service.

In the last two cases,
                                 		the peripheral must choose a specific agent within the group who can provide
                                 		the service. In each case, the peripheral plays a key role in completing the
                                 		routing that the system software has determined. Therefore, the system software
                                 		and the peripheral must be set up to complement each other. They must have the
                                 		same understanding of the agents, skill groups, and services available at each
                                 		site.

#### Scheduled Targets

Some routing clients also support scheduled targets . A scheduled target is a group of agents not
                                 		associated with a Peripheral Gateway. The system software cannot monitor the
                                 		group directly. Instead it relies on a periodic schedule to determine the
                                 		number of agents logged on to the group. The routing client informs the system
                                 		software when a call to the group ends. Since the system software knows how
                                 		many calls it has routed to the group, it can determine the number of calls in
                                 		progress. Based on this and the schedule, the system software can determine
                                 		whether the target can handle an additional call.

## Route Configuration

A route consists of two components:

The skill target (agent, skill group, service, translation route,
                                    				or service array) at a peripheral which can handle a call.

The service by which the peripheral classifies the call.

### Define a Route

- Agent Explorer

- Skill Group Explorer

- Service Explorer

- Service Array Explorer

- Translation Route Explorer

With the Explorer tools, you can define and update a route at the same
                                 		  time you define and update its target. To access all the tools for creating
                                 		  routes:

Click ICM
                                                				  Configure > Targets > Route .

See following figure.

### Modify a Route

Use the Configuration Manager's Route Bulk tool to create multiple
                                 		  routes. To create individual routes, use the Configuration Manager's Explorer
                                 		  tool appropriate for the route target. Follow the instructions in the online
                                 		  help.

To modify routes with the Explorer tools:

Step 1

In the appropriate Explorer window:

To define a new route, select the target for which you are
                                                   					 creating the route and click Add Route .

To modify a route, select the route.

Step 2

In the Route tab, enter values for the following fields:

Name . A unique name for the route. You might derive the
                                                   					 name for the route from the skill target and service associated with it. For
                                                   					 example, you might have a route associated with the Dallas.TeleSales service
                                                   					 and the Dallas.Sales skill group. You might name the route Dallas.TS_Sales .

Description . Text identifying the route.

Service name . (selection list) Every route must be
                                                   					 associated with a service. By choosing a service, you are implicitly
                                                   					 associating the route with the peripheral for that service. For a new route,
                                                   					 the drop-down list contains all the services defined for the selected
                                                   					 peripheral (or PG, in the case of a service array).

To assign the route to another service, in the tree list, drag
                                                   					 it to the desired peripheral. You can also move the route to the UNASSIGNED
                                                   					 list.

Warning

Step 3

Click Save . The system software saves your changes
                                          			 in the database.

### Set a Default Route for Each Peripheral

After you have defined routes, you can set a default route for each
                                 		  peripheral. The system software uses the default route to classify calls for
                                 		  statistical purposes.

For each call that arrives at a peripheral, the system software
                                 		  records monitoring information in the real-time and historical tables for the
                                 		  route associated with that call. If the system software cannot determine a
                                 		  route for the call, it uses the default route defined for the peripheral.

By defining a default route for each peripheral, you ensure that the
                                 		  system software captures route information for every call. You might want to
                                 		  create a special route for this purpose. You can then determine which calls are
                                 		  not being accounted for properly.

To set a default for each peripheral:

Step 1

In the Configuration Manager menu, select Tools > Explorer
                                                				  Tools > PG Explorer . The PG
                                          			 Explorer window appears.

Step 2

In the tree list window, select the peripheral you want to modify and click the Default Route tab.

Step 3

In the Default Route tab, select the enterprise name of a route from the selection list. The list includes all routes associated with skill targets
                                          at the chosen peripheral.

Step 4

After choosing the route, click Save to enter your edits into the database.

## Network Targets

Routing clients do not send calls directly to services, skill groups,
                              		  or agents. They send each call to an announcement or to a specific trunk group
                              		  at a peripheral. If the call is sent to a trunk group, the routing client can
                              		  also send a DNIS value for the call. The combination of trunk group and DNIS
                              		  value is a 
                              		  peripheral target.

You must define the announcements and peripheral targets that the
                              		  routing clients use. These are called network targets . Later, you can associate
                              		  a routing label with each 
                              		  network target.

### Define Peripheral Targets

A peripheral target is a combination of a network trunk group and a
                                 		  DNIS value. You must work with your interexchange carrier or other routing
                                 		  client to set up the trunk groups on which you expect to receive calls and the
                                 		  DNIS values that are sent with them.

To define peripheral targets:

Step 1

In the Configuration Manager menu, select Configure
                                                				  ICM > Targets > Target from the menu bar.

The resulting menu (see the following) allows you to create multiple peripheral targets, using the Peripheral Target Bulk
                                             configuration
                                             				tool or creating a peripheral target for a service, a service array, a skill
                                             				group, a translation route, or an agent. Select the appropriate tool for your
                                             				needs.

Step 2

Use the online help if you have questions.

Step 3

When finished, click Save .

## Announcement Configuration Information

You must provide information about any announcements to which you want
                           		  to route calls. You must work with the IXC or other routing
                           		  client to set up announcements within the network and assign labels to them.
                           		  You can then enter information about the labels into the Unified ICM system.

### Add Announcement Configuration Information

To add announcement configuration information:

Step 1

In the Configuration Manager menu, select Tools > Explorer
                                                				  Tools > Announcement Explorer .
                                          			 The Announcement Explorer window appears.

Step 2

Click Retrieve . This enables the Add Announcement button.

Step 3

Click Add Announcement .

Step 4

In the Announcement tab, enter values for the following fields:

Name . A unique name for the
                                                   					 announcement.

Description . Text identifying the
                                                   					 announcement.

Step 5

To associate a label with the announcement:

In the tree list window select one from the UNASSIGNED group
                                                   					 and drag it to the announcement.

Select the announcement and click Add Label . Then in the Label tab, enter
                                                   					 the appropriate field information.

Step 6

Click Save to save the announcement configuration
                                          			 settings. The system software automatically generates a unique Network Target
                                          			 ID value.

## Labels

After defining announcements and peripheral targets, you must define
                              		  the labels that your routing clients use to reference network targets. The
                              		  label is the value that the system software returns to the routing client. The
                              		  routing client then translates the label to an announcement or peripheral
                              		  target (trunk group and DNIS) that the peripheral will convert to the skill
                              		  target and service you specify.

### Label Types

In defining a label,
                                 		  you must specify a label type by
                                 		  selecting an option from the Type drop-down list in the Label Configuration
                                 		  selection box.

The following table
                                 		  lists the configured label types the system software supports. In addition to
                                 		  these labels, a script can create a dynamic label,
                                 		  which is defined in real time through a script expression and then passed to a
                                 		  routing client.

Label type

Description

Routing
                                             					 clients

How to send
                                             					 label

Normal

Maps to a
                                             					 trunk group and DNIS or announcement defined by the routing client.

All

Specify an
                                             					 associated route in a routing script target.

DNIS Override

Sends a
                                             					 value along with the label that overrides the DNIS value of the routing client.

MCI

Specify an
                                             					 associated route in a routing script target.

Busy

Plays a busy
                                             					 signal for the caller.

All

Use a Busy
                                             					 or Termination script node.

Ring

Plays an
                                             					 unanswered ring for the caller.

AT&T GTN

Use a Ring
                                             					 or Termination script node.

Post-Query

Specifies a
                                             					 re-entry point in the network routing plan. The routing client begins
                                             					 processing the routing plan from that point.

All

Use a Return
                                             					 Label script node.

The Normal and DNIS
                                 		  Override types are used for peripheral targets (and hence, for routes) or for
                                 		  announcements. Busy, Ring, and Post-Query labels are not associated with any
                                 		  target in the Unified ICM configuration. The routing client uses its own special targets for labels of
                                 		  these types.

For more information
                                 		  on targets within scripts, refer to the Scripting and Media Routing Guide for Cisco Unified ICM/Contact Center Enterprise .

### Label Setup

To set up a label, you create configuration information and associate
                              		the label with a network target.

#### Create Label

To create a label,
                                    		  follow these steps:

Step 1

In the
                                             			 Configuration Manager menu, select Configure
                                                   				  ICM > Targets > Label .

This displays
                                                				the following menu options for configuring a label:

Label Bulk

Label List

Service
                                                      					 Explorer

Service
                                                      					 Array Explorer

Skill Group
                                                      					 Explorer

Translation
                                                      					 Route Explorer

Agent
                                                      					 Explorer

Announcement
                                                      					 Explorer

Network VRU
                                                      					 Explorer

Step 2

Select the tool
                                             			 you need:

Use the
                                                      					 Label Bulk tool to configure many labels at a time.

Use the
                                                      					 Label List tool to configure individual labels for any network targets.

Use the
                                                      					 remaining Explorer tools to configure labels for a specific network target
                                                      					 (services, service arrays, skill groups, translation routes, agents,
                                                      					 announcements, network VRUs).

Step 3

Enter values for
                                             			 the following fields. Use the online help if you have questions:

Routing Client (required)

The
                                                      					 enterprise name of the routing client that can receive this label.

Label (required)

The literal
                                                      					 string of characters to be returned to the routing client.

Label Type . (required)

The type of
                                                      					 label. The valid types depend on the type of the routing client.

Target type

(selection
                                                      					 list) Indicates the type of the network target associated with the label:
                                                      					 Network Announcement, PBX/ACD Peripheral (that is, a peripheral target), a
                                                      					 scheduled target, or a network VRU.

Network target . (list and bulk tools only)

(selection
                                                      					 list) Indicates the announcement, peripheral target, or scheduled target
                                                      					 associated with the label.

Customer . (list and bulk tools only)

The customer
                                                      					 associated with the label.

Description .

Any other
                                                      					 information you want about the label.

The following
                                                				table lists which targets are valid for each label type.

Label

ACD/PBX

Network
                                                            						  announcement

Scheduled target

Network
                                                            						  device

Network VRU

Normal

Valid

Valid

Valid

Valid

Valid

DNIS
                                                            						  Override

Valid

Valid

Valid

Valid

Valid

Busy

—

—

—

—

Valid

Ring

—

—

—

—

Valid

Post-Query

Valid

—

Valid

Valid

Valid

Step 4

Click Save .

### Label
                           	 Mapping

For some routing
                                 		  clients, all labels are valid for all dialed number/script selectors. For other
                                 		  routing clients, you must specify which labels are valid for each dialed
                                 		  number/script selector. You specify whether the mapping of labels to dialed
                                 		  number/script selectors is necessary when you configure the routing client.

### Map Specific Labels to a Dialed Number/Script Selector

To map specific labels to a dialed number/script selector, follow
                                 		  these steps:

Step 1

In the Configuration Manager menu, select Tools > List
                                                				  Tools > Dialed Number/Script Selector
                                                				  List . The Dialed Number/Script Selector List window
                                          			 appears.

Step 2

Select the filters you want and click Retrieve . The enterprise names for the
                                          			 retrieved dialed number/script selectors are listed in the list box.

Step 3

Select the enterprise name for the dialed number/script selector
                                          			 you want.

Step 4

Click the Dialed Number Label tab.

The Name column displays a list of all labels currently associated
                                             				with that dialed number/script selector.

Step 5

Click Add .

Step 6

In the Add Label dialog, select a label name and
                                          			 click OK .

Step 7

Click Save .

### Set a Default Label for Each Dialed Number/Script Selector

After you have defined labels, you can set a default label for each
                                 		  dialed number/script selector. If the system software fails to find a label by
                                 		  running the routing scripts for the call type, it uses the default label for
                                 		  the dialed number/script selector.

You can use Configuration Manager's Dialed Number Bulk tool to
                                 		  configure many dialed number/script selectors at a time or the Dialed
                                 		  Number/Script Selector List tool to configure one at a time. The following
                                 		  instructions show how to use the Dialed Number/Script Selector List tool.

To set a default label for each dialed number/script selector:

Step 1

In the Configuration Manager's menu, select Tools > List
                                                				  Tools > Dialed Number/Script Selector
                                                				  List . The Dialed Number/Script Selector List window
                                          			 appears.

Step 2

Select the filters you want and click Retrieve . The enterprise names for the dialed
                                          			 number/script selectors retrieved are listed in the list box.

Step 3

Select the dialed number/script selector you want and click the Attributes tab.

Step 4

In the Default label field, select the enterprise
                                          			 name of a label from the selection list. This list includes all labels
                                          			 associated with the same routing client as the dialed number/script selector.

Step 5

After choosing the label, click Save .

## Service Arrays

Service arrays are closely tied to network trunk groups. Typically,
                              		  you use service arrays in cases where:

You have similar peripheral services defined on multiple VRUs.

The VRUs all share the same network group.

By grouping the services of multiple VRUs into a service array, you
                              		  can send calls to a single target (a service array) and let the network deliver
                              		  the call to any one of the peripheral services that make up the service array.
                              		  For example, if several VRUs each support a Quotes service, you can define a
                              		  Quotes service array for those services.

### Configure Service Arrays

To configure service arrays, proceed along the following steps:

Step 1

In the Configuration Manager menu, select Configure
                                                				  ICM > Targets > VRU Service
                                                				  Arrays > Service Array Explorer .
                                          			 The Service Array Explorer window appears.

Step 2

In the Select filter data box, select the appropriate filters and
                                          			 click Retrieve . This enables the Add Service array button and displays a list
                                          			 of all currently defined service arrays associated with the selected PG.

Step 3

You can define a new service array or modify an existing one:

To set up a new service array, click Add Service array .

To modify an existing service array, select it in the tree
                                                   					 list window.

Step 4

In the Service Array tab for the selected service
                                          			 array, enter values for the following fields:

Name . A unique name for the service
                                                   					 array.

Description . Additional information
                                                   					 about the service array.

Step 5

Click the Members tab.

This tab lists the services that are current service array members
                                             				of the selected PG.

To add service members, click Add . Then in the Add Service Member
                                                   					 window, select the name of a service from the list of available records and
                                                   					 click OK . The Available records list contains
                                                   					 all the services connected to the peripherals associated with the selected PG.

To remove a service member, select it in the list and click Remove .

Step 6

Add or modify a route associated with the service array:

To add a route, select the service array in the tree list box, and click Add Route . Or in the tree list box, select a route from the UNASSIGNED group and drag it to the service array. Then in the Route tab, enter or modify the values in the Name , Description and Service name fields.

To modify the route, select it in the tree list box, and
                                                   					 modify the Name and Description in the Route tab.

Step 7

Add or modify one or more peripheral targets for the route:

To add a peripheral target, select the route and click Add Peripheral target . Or in the tree
                                                   					 list box, select a peripheral target from the UNASSIGNED group and drag it to
                                                   					 the route. Then in the Peripheral target tab, enter the following:

DNIS . The DNIS value for the peripheral target. The
                                                         						  routing client delivers this value to the trunk group along with the call.

Description . Any additional information about the
                                                         						  DNIS value.

Network trunk group . The group on which to deliver
                                                         						  calls for the service array.

Step 8

To add or modify a label for the peripheral target:

To add a label, select the peripheral target in the tree list
                                                   					 box, and click Add Label . Or in the tree list box,
                                                   					 select a label from the UNASSIGNED group and drag it to the peripheral target.
                                                   					 Then in the Label tab, enter or modify the following:

Routing client . The enterprise name of the routing
                                                         						  client that can receive this label.

Label . The literal string of characters to be
                                                         						  returned to the routing client.

Label type . The type of label. The valid types
                                                         						  depend on the type of the routing client.

Customer . The name of the customer.

Description . Any additional information about the
                                                         						  label.

To modify the label, select it in the tree list box, and
                                                   					 modify the preceding fields in the Route tab.

Step 9

Click Save to save the changes to the database.

Step 10

Click Close to close the Service Array Explorer.

## Application
                        	 Wizard

The Application
                              		  wizard provides an alternate method for defining labels, peripheral targets,
                              		  and routes and associating them with services at a peripheral.

Before starting the
                              		  Application wizard, you must have defined the routing client, peripheral,
                              		  network trunk groups (and associated trunk groups), and services to be used.
                              		  Within the Application wizard you can create dialed numbers, labels, peripheral
                              		  targets, and routes.

## Use the Application
                        	 Wizard

To use the
                              		  Application wizard, follow these steps:

Step 1

In the
                                       			 Configuration Manager menu, select Tools > Wizards > Application
                                             				  Wizard . The Routing window appears.

Step 2

Choose the type
                                       			 of application you want to set up (Pre-Routing or Post-Routing) and click Next to continue. The Routing Client and Dialed
                                       			 Number window appears, displaying information about all the configured routing
                                       			 clients of the type you selected.

Step 3

Specify the
                                       			 following:

Routing Client . Click to
                                                					 select one or more routing clients for the application. (A check mark to the
                                                					 left of the routing client indicates it is selected.)

Dialed Number . Click the
                                                					 row and select a number from the drop-down list or enter a new dialed number
                                                					 value.

Step 4

Click Next . The Peripheral window appears.

Step 5

Specify the
                                       			 following:

Peripheral . Click to
                                                					 select one or more peripherals to which you want the application to deliver
                                                					 calls.

Number of Network Trunks .
                                                					 The number of network trunk groups to be targeted at each peripheral.

Step 6

Click Next . The Network Trunk Group window appears,
                                       			 displaying the peripherals and routing clients you have previously selected.

Step 7

For each row,
                                       			 specify the following:

Network Trunk Group .
                                                					 Click the row and select from the drop-down list.

# DNIS . The number of
                                                					 peripheral targets (DNIS values) to define for each network trunk group.

Step 8

Click Next . The Route DNIS and Label window appears.

Step 9

For each network
                                       			 trunk group, specify the following:

Label . (This value does
                                                					 not have to be defined in the Unified ICM database.) The value the system software returns to the routing client to
                                                					 indicate the destination of the call.

DNIS . (This value does
                                                					 not have to be defined in the Unified ICM database.) The value the routing client sends to the network trunk group to
                                                					 indicate the destination of the call.

Service Peripheral Name .
                                                					 Click the row and select a predefined service at the peripheral from the
                                                					 drop-down list.

Route . Name of the route
                                                					 to be associated with the service. Select from the drop-down list or enter a
                                                					 new route name.

Step 10

Click Next . The Application Wizard displays a dialog
                                       			 listing the changes that will be made to the Unified ICM database.

Step 11

Click Finish to save the changes and exit the Application
                                       			 Wizard.

## Translation Routes

A translation route is a special destination for a call that allows
                              		  you to deliver other information along with the call. You do this by delivering
                              		  the call first to the translation route. While the routing client is processing
                              		  the call, the system software delivers the final destination for the call to
                              		  the Peripheral Gateway along with any other necessary information. The
                              		  peripheral then works with the PG to reroute the call to the ultimate target
                              		  and ensure that the appropriate information is also delivered.

A single translation route can be used to send information to any
                              		  number of different targets. However, because the PG must uniquely identify the
                              		  call, you cannot perform translation routing on two calls to the same
                              		  peripheral target simultaneously. To avoid this, you typically define a set of
                              		  peripheral targets and routes, for each translation route.

## Translation Route
                        	 Wizard

You can define
                              		  translation routes within the Configuration Manager. However, defining the
                              		  correct associations with peripheral targets, labels, and routes is
                              		  complicated. To automate much of the process, use the translation route wizard.

### Create a Translation
                           	 Route

To create a
                                 		  translation route, follow these steps:

Step 1

In the
                                          			 Configuration Manager, select Tools > Wizards > Translation Route
                                                				  Wizard . The Translation Route Wizard introductory
                                          			 dialog opens.

Step 2

Click Next . The Select Configuration Task dialog appears.

Step 3

To create a
                                          			 translation route, choose Create
                                             				New and click Next . The Define translation route dialog appears.

Step 4

Enter a long and
                                          			 short name for the translation route and, optionally, a description — the short
                                          			 name is used in forming target names — and click Next . The Select configuration dialog appears.

Step 5

Use the
                                          			 drop-down list to choose the configuration. The graphic changes to show the
                                          			 configuration you select.

A
                                                         				  translation route can be associated with a single peripheral or with multiple
                                                         				  VRUs associated with a single PG. It can handle calls originating from a single
                                                         				  routing client or from multiple routing clients. (The Multiple ACD type is not
                                                         				  currently supported.)

Step 6

Click Next . The Select peripheral gateway, peripherals,
                                          			 and services dialog appears.

Step 7

Specify the
                                          			 following:

Peripheral gateway .
                                                   					 (scrolling list) The gateway target for the translation route.

Peripheral . (scrolling
                                                   					 list) The single peripheral or the peripheral to route calls to.

Service/Service array .
                                                   					 (scrolling list) If the translation route is associated with a single
                                                   					 peripheral, then select the service associated with the translation route. If
                                                   					 the translation route is associated with multiple VRUs, then select a service
                                                   					 array.

Step 8

Click Next . The Select routing clients and dialed numbers
                                          			 appears.

Use this dialog
                                             				to specify the routing client or routing clients from which translation routed
                                             				calls originate. For each routing client, you can also specify which specific
                                             				dialed numbers are used for translation routed calls.

Step 9

Select a routing
                                          			 client from the Pre-Routing Client list or the Post-Routing Client list. The
                                          			 Dialed Number list updates to show the dialed numbers associated with the
                                          			 selected routing client.

Step 10

Select a dialed
                                          			 number you want to use with the translation route and click the Add button. The number appears in the list at the
                                          			 bottom of the dialog. The translation route wizard maps the translation route's
                                          			 labels to each of these dialed numbers.

Step 11

Click Next . The Select network trunk groups for routing
                                          			 clients dialog appears.

For each routing
                                             				client you have selected, you must select at least one network trunk group to
                                             				be used in peripheral targets associated with the translation route.

Step 12

Select a routing
                                          			 client, select a network trunk group value for it, and click Add . The network trunk group appears in the list at
                                          			 the bottom of the dialog.

Step 13

Click Next . The Configure DNIS dialog appears.

Use this dialog
                                             				to specify the DNIS values to be used in peripheral targets associated with the
                                             				translation route.

Step 14

Do one of the
                                          			 following:

To enter a
                                                   					 specific DNIS value, click Add DNIS and enter the value.

To add a
                                                   					 range of DNIS values, typically required by a translation route, click Add DNIS Range . A dialog prompts you to enter a
                                                   					 starting and ending DNIS value. The translation route wizard automatically
                                                   					 generates the DNIS values in the range.

Step 15

Click Next . The Configure label dialog appears.

Use this
                                             				dialog to define a label for each peripheral target. A label consists of a
                                             				prefix and a suffix. Each DNIS value requires a unique label.

Step 16

Do one of the
                                          			 following:

Enter
                                                   					 prefixes and suffixes individually.

Use the
                                                   					 buttons in this dialog to set a range of values or base the prefix or suffix
                                                   					 values on the DNIS values.

Step 17

Click Next . The Wizard complete dialog appears.

Step 18

Click Create
                                             				translation route to create the translation route and its
                                          			 associated entities. First, the translation route wizard displays a success
                                          			 message and then the dialog appears as follows.

Step 19

Do one of the
                                          			 following:

To see
                                                   					 details about the translation route you just created, click Run Report .

To return
                                                   					 to the beginning of the translation route wizard and perform a new task, select Start New Task and click Finish .

To exit
                                                   					 the translation route wizard, click Finish .

| Note | You must have defined the skill target and service before you can
                                       		  configure a route. Follow the steps in the Configuration Manager's Step by Step
                                       		  Configuration menu when configuring your Unified ICM system. |
|---|---|

| Click ICM
                                                				  Configure > Targets > Route . See following figure. Figure 2. Configuration Manager Route Tools |
|---|

| Step 1 | In the appropriate Explorer window: To define a new route, select the target for which you are
                                                   					 creating the route and click Add Route . To modify a route, select the route. |
|---|---|
| Step 2 | In the Route tab, enter values for the following fields: Name . A unique name for the route. You might derive the
                                                   					 name for the route from the skill target and service associated with it. For
                                                   					 example, you might have a route associated with the Dallas.TeleSales service
                                                   					 and the Dallas.Sales skill group. You might name the route Dallas.TS_Sales . Description . Text identifying the route. Service name . (selection list) Every route must be
                                                   					 associated with a service. By choosing a service, you are implicitly
                                                   					 associating the route with the peripheral for that service. For a new route,
                                                   					 the drop-down list contains all the services defined for the selected
                                                   					 peripheral (or PG, in the case of a service array). To assign the route to another service, in the tree list, drag
                                                   					 it to the desired peripheral. You can also move the route to the UNASSIGNED
                                                   					 list. Warning When you break the association
                                                      				between a route and a peripheral, the system software removes the Route ID
                                                      				value from all peripheral targets that reference that route. | Warning | When you break the association
                                                      				between a route and a peripheral, the system software removes the Route ID
                                                      				value from all peripheral targets that reference that route. |
| Warning | When you break the association
                                                      				between a route and a peripheral, the system software removes the Route ID
                                                      				value from all peripheral targets that reference that route. |
| Step 3 | Click Save . The system software saves your changes
                                          			 in the database. |

| Warning | When you break the association
                                                      				between a route and a peripheral, the system software removes the Route ID
                                                      				value from all peripheral targets that reference that route. |
|---|---|

| Step 1 | In the Configuration Manager menu, select Tools > Explorer
                                                				  Tools > PG Explorer . The PG
                                          			 Explorer window appears. |
|---|---|
| Step 2 | In the tree list window, select the peripheral you want to modify and click the Default Route tab. |
| Step 3 | In the Default Route tab, select the enterprise name of a route from the selection list. The list includes all routes associated with skill targets
                                          at the chosen peripheral. |
| Step 4 | After choosing the route, click Save to enter your edits into the database. |

| Step 1 | In the Configuration Manager menu, select Configure
                                                				  ICM > Targets > Target from the menu bar. The resulting menu (see the following) allows you to create multiple peripheral targets, using the Peripheral Target Bulk
                                             configuration
                                             				tool or creating a peripheral target for a service, a service array, a skill
                                             				group, a translation route, or an agent. Select the appropriate tool for your
                                             				needs. Figure 3. Configuration Manager Target Submenu |
|---|---|
| Step 2 | Use the online help if you have questions. |
| Step 3 | When finished, click Save . |

| Step 1 | In the Configuration Manager menu, select Tools > Explorer
                                                				  Tools > Announcement Explorer .
                                          			 The Announcement Explorer window appears. |
|---|---|
| Step 2 | Click Retrieve . This enables the Add Announcement button. |
| Step 3 | Click Add Announcement . |
| Step 4 | In the Announcement tab, enter values for the following fields: Name . A unique name for the
                                                   					 announcement. Description . Text identifying the
                                                   					 announcement. Note You can save at this point and then add the
                                                      				label information in the following step. | Note | You can save at this point and then add the
                                                      				label information in the following step. |
| Note | You can save at this point and then add the
                                                      				label information in the following step. |
| Step 5 | To associate a label with the announcement: In the tree list window select one from the UNASSIGNED group
                                                   					 and drag it to the announcement. Select the announcement and click Add Label . Then in the Label tab, enter
                                                   					 the appropriate field information. Note A description of the Label tab fields and buttons is in the online help. | Note | A description of the Label tab fields and buttons is in the online help. |
| Note | A description of the Label tab fields and buttons is in the online help. |
| Step 6 | Click Save to save the announcement configuration
                                          			 settings. The system software automatically generates a unique Network Target
                                          			 ID value. |

| Note | You can save at this point and then add the
                                                      				label information in the following step. |
|---|---|

| Note | A description of the Label tab fields and buttons is in the online help. |
|---|---|

| Note | For an AT&T ICP connection, the system software treats a CRP
                                       		  code as a label. |
|---|---|

| Note | Each label you
                                          		  define is valid only for a specific routing client; not all label types are
                                          		  valid for all types of routing clients. Check with your carrier for the latest
                                          		  information about supported label types. |
|---|---|

| Label type | Description | Routing
                                             					 clients | How to send
                                             					 label |
|---|---|---|---|
| Normal | Maps to a
                                             					 trunk group and DNIS or announcement defined by the routing client. | All | Specify an
                                             					 associated route in a routing script target. |
| DNIS Override | Sends a
                                             					 value along with the label that overrides the DNIS value of the routing client. | MCI | Specify an
                                             					 associated route in a routing script target. |
| Busy | Plays a busy
                                             					 signal for the caller. | All | Use a Busy
                                             					 or Termination script node. |
| Ring | Plays an
                                             					 unanswered ring for the caller. | AT&T GTN | Use a Ring
                                             					 or Termination script node. |
| Post-Query | Specifies a
                                             					 re-entry point in the network routing plan. The routing client begins
                                             					 processing the routing plan from that point. | All | Use a Return
                                             					 Label script node. |

| Step 1 | In the
                                             			 Configuration Manager menu, select Configure
                                                   				  ICM > Targets > Label . This displays
                                                				the following menu options for configuring a label: Label Bulk Label List Service
                                                      					 Explorer Service
                                                      					 Array Explorer Skill Group
                                                      					 Explorer Translation
                                                      					 Route Explorer Agent
                                                      					 Explorer Announcement
                                                      					 Explorer Network VRU
                                                      					 Explorer |
|---|---|
| Step 2 | Select the tool
                                             			 you need: Use the
                                                      					 Label Bulk tool to configure many labels at a time. Use the
                                                      					 Label List tool to configure individual labels for any network targets. Use the
                                                      					 remaining Explorer tools to configure labels for a specific network target
                                                      					 (services, service arrays, skill groups, translation routes, agents,
                                                      					 announcements, network VRUs). |
| Step 3 | Enter values for
                                             			 the following fields. Use the online help if you have questions: Routing Client (required) The
                                                      					 enterprise name of the routing client that can receive this label. Label (required) The literal
                                                      					 string of characters to be returned to the routing client. Label Type . (required) The type of
                                                      					 label. The valid types depend on the type of the routing client. Target type (selection
                                                      					 list) Indicates the type of the network target associated with the label:
                                                      					 Network Announcement, PBX/ACD Peripheral (that is, a peripheral target), a
                                                      					 scheduled target, or a network VRU. Note The
                                                               					 Target type is a filter for the Network target field. The Target type selected
                                                               					 is not retained unless a Network target is selected. Network target . (list and bulk tools only) (selection
                                                      					 list) Indicates the announcement, peripheral target, or scheduled target
                                                      					 associated with the label. Customer . (list and bulk tools only) The customer
                                                      					 associated with the label. Description . Any other
                                                      					 information you want about the label. The following
                                                				table lists which targets are valid for each label type. Table 2. Valid Label
                                                      				Targets Label ACD/PBX Network
                                                            						  announcement Scheduled target Network
                                                            						  device Network VRU Normal Valid Valid Valid Valid Valid DNIS
                                                            						  Override Valid Valid Valid Valid Valid Busy — — — — Valid Ring — — — — Valid Post-Query Valid — Valid Valid Valid | Note | The
                                                               					 Target type is a filter for the Network target field. The Target type selected
                                                               					 is not retained unless a Network target is selected. | Label | ACD/PBX | Network
                                                            						  announcement | Scheduled target | Network
                                                            						  device | Network VRU | Normal | Valid | Valid | Valid | Valid | Valid | DNIS
                                                            						  Override | Valid | Valid | Valid | Valid | Valid | Busy | — | — | — | — | Valid | Ring | — | — | — | — | Valid | Post-Query | Valid | — | Valid | Valid | Valid |
| Note | The
                                                               					 Target type is a filter for the Network target field. The Target type selected
                                                               					 is not retained unless a Network target is selected. |
| Label | ACD/PBX | Network
                                                            						  announcement | Scheduled target | Network
                                                            						  device | Network VRU |
| Normal | Valid | Valid | Valid | Valid | Valid |
| DNIS
                                                            						  Override | Valid | Valid | Valid | Valid | Valid |
| Busy | — | — | — | — | Valid |
| Ring | — | — | — | — | Valid |
| Post-Query | Valid | — | Valid | Valid | Valid |
| Step 4 | Click Save . |

| Note | The
                                                               					 Target type is a filter for the Network target field. The Target type selected
                                                               					 is not retained unless a Network target is selected. |
|---|---|

| Label | ACD/PBX | Network
                                                            						  announcement | Scheduled target | Network
                                                            						  device | Network VRU |
|---|---|---|---|---|---|
| Normal | Valid | Valid | Valid | Valid | Valid |
| DNIS
                                                            						  Override | Valid | Valid | Valid | Valid | Valid |
| Busy | — | — | — | — | Valid |
| Ring | — | — | — | — | Valid |
| Post-Query | Valid | — | Valid | Valid | Valid |

| Step 1 | In the Configuration Manager menu, select Tools > List
                                                				  Tools > Dialed Number/Script Selector
                                                				  List . The Dialed Number/Script Selector List window
                                          			 appears. |
|---|---|
| Step 2 | Select the filters you want and click Retrieve . The enterprise names for the
                                          			 retrieved dialed number/script selectors are listed in the list box. |
| Step 3 | Select the enterprise name for the dialed number/script selector
                                          			 you want. |
| Step 4 | Click the Dialed Number Label tab. The Name column displays a list of all labels currently associated
                                             				with that dialed number/script selector. Note For a call associated with this dialed number/script selector,
                                                      				the system software can return only labels assigned to the dialed number/script
                                                      				selector. | Note | For a call associated with this dialed number/script selector,
                                                      				the system software can return only labels assigned to the dialed number/script
                                                      				selector. |
| Note | For a call associated with this dialed number/script selector,
                                                      				the system software can return only labels assigned to the dialed number/script
                                                      				selector. |
| Step 5 | Click Add . |
| Step 6 | In the Add Label dialog, select a label name and
                                          			 click OK . Note For labels to appear in this dialog selection box, they must
                                                      				have been previously defined for the selected dialed number/script selector's
                                                      				routing client. Use the Label List tool to define labels. | Note | For labels to appear in this dialog selection box, they must
                                                      				have been previously defined for the selected dialed number/script selector's
                                                      				routing client. Use the Label List tool to define labels. |
| Note | For labels to appear in this dialog selection box, they must
                                                      				have been previously defined for the selected dialed number/script selector's
                                                      				routing client. Use the Label List tool to define labels. |
| Step 7 | Click Save . |

| Note | For a call associated with this dialed number/script selector,
                                                      				the system software can return only labels assigned to the dialed number/script
                                                      				selector. |
|---|---|

| Note | For labels to appear in this dialog selection box, they must
                                                      				have been previously defined for the selected dialed number/script selector's
                                                      				routing client. Use the Label List tool to define labels. |
|---|---|

| Step 1 | In the Configuration Manager's menu, select Tools > List
                                                				  Tools > Dialed Number/Script Selector
                                                				  List . The Dialed Number/Script Selector List window
                                          			 appears. |
|---|---|
| Step 2 | Select the filters you want and click Retrieve . The enterprise names for the dialed
                                          			 number/script selectors retrieved are listed in the list box. |
| Step 3 | Select the dialed number/script selector you want and click the Attributes tab. |
| Step 4 | In the Default label field, select the enterprise
                                          			 name of a label from the selection list. This list includes all labels
                                          			 associated with the same routing client as the dialed number/script selector. |
| Step 5 | After choosing the label, click Save . |

| Note | Within a routing script, you can explicitly invoke the default
                                          		  label for the current dialed number/script selector by using a Termination
                                          		  node. |
|---|---|

| Step 1 | In the Configuration Manager menu, select Configure
                                                				  ICM > Targets > VRU Service
                                                				  Arrays > Service Array Explorer .
                                          			 The Service Array Explorer window appears. |
|---|---|
| Step 2 | In the Select filter data box, select the appropriate filters and
                                          			 click Retrieve . This enables the Add Service array button and displays a list
                                          			 of all currently defined service arrays associated with the selected PG. |
| Step 3 | You can define a new service array or modify an existing one: To set up a new service array, click Add Service array . Note To create subsequent service arrays for the same PG, select
                                                            					 the PG in the tree list window and then click Add Service array . To modify an existing service array, select it in the tree
                                                   					 list window. | Note | To create subsequent service arrays for the same PG, select
                                                            					 the PG in the tree list window and then click Add Service array . |
| Note | To create subsequent service arrays for the same PG, select
                                                            					 the PG in the tree list window and then click Add Service array . |
| Step 4 | In the Service Array tab for the selected service
                                          			 array, enter values for the following fields: Name . A unique name for the service
                                                   					 array. Description . Additional information
                                                   					 about the service array. |
| Step 5 | Click the Members tab. This tab lists the services that are current service array members
                                             				of the selected PG. To add service members, click Add . Then in the Add Service Member
                                                   					 window, select the name of a service from the list of available records and
                                                   					 click OK . The Available records list contains
                                                   					 all the services connected to the peripherals associated with the selected PG. To remove a service member, select it in the list and click Remove . |
| Step 6 | Add or modify a route associated with the service array: To add a route, select the service array in the tree list box, and click Add Route . Or in the tree list box, select a route from the UNASSIGNED group and drag it to the service array. Then in the Route tab, enter or modify the values in the Name , Description and Service name fields. To modify the route, select it in the tree list box, and
                                                   					 modify the Name and Description in the Route tab. |
| Step 7 | Add or modify one or more peripheral targets for the route: To add a peripheral target, select the route and click Add Peripheral target . Or in the tree
                                                   					 list box, select a peripheral target from the UNASSIGNED group and drag it to
                                                   					 the route. Then in the Peripheral target tab, enter the following: DNIS . The DNIS value for the peripheral target. The
                                                         						  routing client delivers this value to the trunk group along with the call. Description . Any additional information about the
                                                         						  DNIS value. Network trunk group . The group on which to deliver
                                                         						  calls for the service array. |
| Step 8 | To add or modify a label for the peripheral target: To add a label, select the peripheral target in the tree list
                                                   					 box, and click Add Label . Or in the tree list box,
                                                   					 select a label from the UNASSIGNED group and drag it to the peripheral target.
                                                   					 Then in the Label tab, enter or modify the following: Routing client . The enterprise name of the routing
                                                         						  client that can receive this label. Label . The literal string of characters to be
                                                         						  returned to the routing client. Label type . The type of label. The valid types
                                                         						  depend on the type of the routing client. Customer . The name of the customer. Description . Any additional information about the
                                                         						  label. To modify the label, select it in the tree list box, and
                                                   					 modify the preceding fields in the Route tab. |
| Step 9 | Click Save to save the changes to the database. |
| Step 10 | Click Close to close the Service Array Explorer. |

| Note | To create subsequent service arrays for the same PG, select
                                                            					 the PG in the tree list window and then click Add Service array . |
|---|---|

| Note | The Application
                                       		  wizard does not allow you to associate routes and targets with skill groups or
                                       		  agents. It allows you to target only services. |
|---|---|

| Step 1 | In the
                                       			 Configuration Manager menu, select Tools > Wizards > Application
                                             				  Wizard . The Routing window appears. |
|---|---|
| Step 2 | Choose the type
                                       			 of application you want to set up (Pre-Routing or Post-Routing) and click Next to continue. The Routing Client and Dialed
                                       			 Number window appears, displaying information about all the configured routing
                                       			 clients of the type you selected. Figure 4. Application Wizard—Routing Client and Dialed
                                             				  Number |
| Step 3 | Specify the
                                       			 following: Routing Client . Click to
                                                					 select one or more routing clients for the application. (A check mark to the
                                                					 left of the routing client indicates it is selected.) Dialed Number . Click the
                                                					 row and select a number from the drop-down list or enter a new dialed number
                                                					 value. Note You must
                                                   				specify a dialed number for each routing client selected. | Note | You must
                                                   				specify a dialed number for each routing client selected. |
| Note | You must
                                                   				specify a dialed number for each routing client selected. |
| Step 4 | Click Next . The Peripheral window appears. Figure 5. Application Wizard—Peripheral |
| Step 5 | Specify the
                                       			 following: Peripheral . Click to
                                                					 select one or more peripherals to which you want the application to deliver
                                                					 calls. Number of Network Trunks .
                                                					 The number of network trunk groups to be targeted at each peripheral. |
| Step 6 | Click Next . The Network Trunk Group window appears,
                                       			 displaying the peripherals and routing clients you have previously selected. Figure 6. Application Wizard—Network Trunk Group |
| Step 7 | For each row,
                                       			 specify the following: Network Trunk Group .
                                                					 Click the row and select from the drop-down list. # DNIS . The number of
                                                					 peripheral targets (DNIS values) to define for each network trunk group. |
| Step 8 | Click Next . The Route DNIS and Label window appears. Figure 7. Application Wizard—Service, Route, DNIS, and Label |
| Step 9 | For each network
                                       			 trunk group, specify the following: Label . (This value does
                                                					 not have to be defined in the Unified ICM database.) The value the system software returns to the routing client to
                                                					 indicate the destination of the call. DNIS . (This value does
                                                					 not have to be defined in the Unified ICM database.) The value the routing client sends to the network trunk group to
                                                					 indicate the destination of the call. Service Peripheral Name .
                                                					 Click the row and select a predefined service at the peripheral from the
                                                					 drop-down list. Route . Name of the route
                                                					 to be associated with the service. Select from the drop-down list or enter a
                                                					 new route name. |
| Step 10 | Click Next . The Application Wizard displays a dialog
                                       			 listing the changes that will be made to the Unified ICM database. |
| Step 11 | Click Finish to save the changes and exit the Application
                                       			 Wizard. |

| Note | You must
                                                   				specify a dialed number for each routing client selected. |
|---|---|

| Note | You can also use
                                       		  the translation route wizard to view configuration or integrity reports on
                                       		  translation routes, update existing translation routes, and delete translation
                                       		  routes and their associated entities. |
|---|---|

| Step 1 | In the
                                          			 Configuration Manager, select Tools > Wizards > Translation Route
                                                				  Wizard . The Translation Route Wizard introductory
                                          			 dialog opens. |
|---|---|
| Step 2 | Click Next . The Select Configuration Task dialog appears. |
| Step 3 | To create a
                                          			 translation route, choose Create
                                             				New and click Next . The Define translation route dialog appears. Figure 8. Define
                                                				  Translation Route Note The graphic
                                                      				on the left of the dialog shows the entities you will be defining while using
                                                      				the translation route wizard. | Note | The graphic
                                                      				on the left of the dialog shows the entities you will be defining while using
                                                      				the translation route wizard. |
| Note | The graphic
                                                      				on the left of the dialog shows the entities you will be defining while using
                                                      				the translation route wizard. |
| Step 4 | Enter a long and
                                          			 short name for the translation route and, optionally, a description — the short
                                          			 name is used in forming target names — and click Next . The Select configuration dialog appears. Figure 9. Select
                                                				  Configuration |
| Step 5 | Use the
                                          			 drop-down list to choose the configuration. The graphic changes to show the
                                          			 configuration you select. Note A
                                                         				  translation route can be associated with a single peripheral or with multiple
                                                         				  VRUs associated with a single PG. It can handle calls originating from a single
                                                         				  routing client or from multiple routing clients. (The Multiple ACD type is not
                                                         				  currently supported.) | Note | A
                                                         				  translation route can be associated with a single peripheral or with multiple
                                                         				  VRUs associated with a single PG. It can handle calls originating from a single
                                                         				  routing client or from multiple routing clients. (The Multiple ACD type is not
                                                         				  currently supported.) |
| Note | A
                                                         				  translation route can be associated with a single peripheral or with multiple
                                                         				  VRUs associated with a single PG. It can handle calls originating from a single
                                                         				  routing client or from multiple routing clients. (The Multiple ACD type is not
                                                         				  currently supported.) |
| Step 6 | Click Next . The Select peripheral gateway, peripherals,
                                          			 and services dialog appears. Figure 10. Select
                                                				  Peripheral Gateway, Peripherals, and Services |
| Step 7 | Specify the
                                          			 following: Peripheral gateway .
                                                   					 (scrolling list) The gateway target for the translation route. Peripheral . (scrolling
                                                   					 list) The single peripheral or the peripheral to route calls to. Service/Service array .
                                                   					 (scrolling list) If the translation route is associated with a single
                                                   					 peripheral, then select the service associated with the translation route. If
                                                   					 the translation route is associated with multiple VRUs, then select a service
                                                   					 array. |
| Step 8 | Click Next . The Select routing clients and dialed numbers
                                          			 appears. Figure 11. Select
                                                				  Routing Clients and Dialed Numbers Use this dialog
                                             				to specify the routing client or routing clients from which translation routed
                                             				calls originate. For each routing client, you can also specify which specific
                                             				dialed numbers are used for translation routed calls. |
| Step 9 | Select a routing
                                          			 client from the Pre-Routing Client list or the Post-Routing Client list. The
                                          			 Dialed Number list updates to show the dialed numbers associated with the
                                          			 selected routing client. |
| Step 10 | Select a dialed
                                          			 number you want to use with the translation route and click the Add button. The number appears in the list at the
                                          			 bottom of the dialog. The translation route wizard maps the translation route's
                                          			 labels to each of these dialed numbers. Note Some routing
                                                      				clients do not require mappings of labels to specific dialed numbers. The
                                                      				dialed number list is automatically disabled for such routing clients. You need
                                                      				only select the routing client and click the Add button to add it to the list. You can also use
                                                      				the Disable Dialed Number Selection option to manually disable the dialed
                                                      				number list. The translation route wizard then does not create mappings of
                                                      				dialed numbers to labels for the routing client. | Note | Some routing
                                                      				clients do not require mappings of labels to specific dialed numbers. The
                                                      				dialed number list is automatically disabled for such routing clients. You need
                                                      				only select the routing client and click the Add button to add it to the list. You can also use
                                                      				the Disable Dialed Number Selection option to manually disable the dialed
                                                      				number list. The translation route wizard then does not create mappings of
                                                      				dialed numbers to labels for the routing client. |
| Note | Some routing
                                                      				clients do not require mappings of labels to specific dialed numbers. The
                                                      				dialed number list is automatically disabled for such routing clients. You need
                                                      				only select the routing client and click the Add button to add it to the list. You can also use
                                                      				the Disable Dialed Number Selection option to manually disable the dialed
                                                      				number list. The translation route wizard then does not create mappings of
                                                      				dialed numbers to labels for the routing client. |
| Step 11 | Click Next . The Select network trunk groups for routing
                                          			 clients dialog appears. Figure 12. Select
                                                				  Network Trunk Groups for Routing Clients For each routing
                                             				client you have selected, you must select at least one network trunk group to
                                             				be used in peripheral targets associated with the translation route. |
| Step 12 | Select a routing
                                          			 client, select a network trunk group value for it, and click Add . The network trunk group appears in the list at
                                          			 the bottom of the dialog. |
| Step 13 | Click Next . The Configure DNIS dialog appears. Figure 13. Configure
                                                				  DNIS Use this dialog
                                             				to specify the DNIS values to be used in peripheral targets associated with the
                                             				translation route. |
| Step 14 | Do one of the
                                          			 following: To enter a
                                                   					 specific DNIS value, click Add DNIS and enter the value. To add a
                                                   					 range of DNIS values, typically required by a translation route, click Add DNIS Range . A dialog prompts you to enter a
                                                   					 starting and ending DNIS value. The translation route wizard automatically
                                                   					 generates the DNIS values in the range. Note DNIS values
                                                      				with leading zeroes, while valid, are different from DNIS values without
                                                      				leading zeroes. For example, 400, 0400, and 00400 are three different and
                                                      				unique DNIS values. | Note | DNIS values
                                                      				with leading zeroes, while valid, are different from DNIS values without
                                                      				leading zeroes. For example, 400, 0400, and 00400 are three different and
                                                      				unique DNIS values. |
| Note | DNIS values
                                                      				with leading zeroes, while valid, are different from DNIS values without
                                                      				leading zeroes. For example, 400, 0400, and 00400 are three different and
                                                      				unique DNIS values. |
| Step 15 | Click Next . The Configure label dialog appears. Figure 14. Configure
                                                				  Label Use this
                                             				dialog to define a label for each peripheral target. A label consists of a
                                             				prefix and a suffix. Each DNIS value requires a unique label. |
| Step 16 | Do one of the
                                          			 following: Enter
                                                   					 prefixes and suffixes individually. Use the
                                                   					 buttons in this dialog to set a range of values or base the prefix or suffix
                                                   					 values on the DNIS values. |
| Step 17 | Click Next . The Wizard complete dialog appears. Figure 15. Wizard
                                                				  Complete Initial View |
| Step 18 | Click Create
                                             				translation route to create the translation route and its
                                          			 associated entities. First, the translation route wizard displays a success
                                          			 message and then the dialog appears as follows. Figure 16. Wizard
                                                				  Complete Success View |
| Step 19 | Do one of the
                                          			 following: To see
                                                   					 details about the translation route you just created, click Run Report . To return
                                                   					 to the beginning of the translation route wizard and perform a new task, select Start New Task and click Finish . To exit
                                                   					 the translation route wizard, click Finish . |

| Note | The graphic
                                                      				on the left of the dialog shows the entities you will be defining while using
                                                      				the translation route wizard. |
|---|---|

| Note | A
                                                         				  translation route can be associated with a single peripheral or with multiple
                                                         				  VRUs associated with a single PG. It can handle calls originating from a single
                                                         				  routing client or from multiple routing clients. (The Multiple ACD type is not
                                                         				  currently supported.) |
|---|---|

| Note | Some routing
                                                      				clients do not require mappings of labels to specific dialed numbers. The
                                                      				dialed number list is automatically disabled for such routing clients. You need
                                                      				only select the routing client and click the Add button to add it to the list. You can also use
                                                      				the Disable Dialed Number Selection option to manually disable the dialed
                                                      				number list. The translation route wizard then does not create mappings of
                                                      				dialed numbers to labels for the routing client. |
|---|---|

| Note | DNIS values
                                                      				with leading zeroes, while valid, are different from DNIS values without
                                                      				leading zeroes. For example, 400, 0400, and 00400 are three different and
                                                      				unique DNIS values. |
|---|---|