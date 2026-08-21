---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-icm-enterprise-icm-enterprise-12-6-2-configurati-e0614b0247
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/icm_enterprise/icm_enterprise_12_6_2/configuration/guide/ucce_b_features-guide-1262/ucce_m_contact_sharing-1261.html
retrieved_at: 2026-08-21T11:55:25.011270+00:00
---

Cisco Unified Contact Center Enterprise Features Guide, Release 12.6(2)

# Cisco Unified Contact Center Enterprise Features Guide, Release 12.6(2)

Updated: April 30, 2025

Chapter: Contact Sharing

## Chapter: Contact Sharing

# Contact Sharing

## Contact Sharing
                        	 Overview

The Contact Sharing feature uses a Contact Director to distribute incoming contacts to up to 3 Unified CCE instances. The
                           3 instances can support a total of 24,000 active agents.

Contact Sharing uses extrapolation to distribute calls and increase the overall agent and call handling capacity. Contact
                           Sharing enables customers with multiple Unified Contact Center Enterprise (Unified CCE) systems to distribute calls across
                           those systems. The Contact Director (sometimes called an IVR ICM) acts as an initial entry point for the call. If the call
                           needs agent attention, Contact Sharing decides where to route the call based on Live Data real-time state information from
                           the Unified CCE target systems. You can configure Contact Sharing to base routing decisions on factors such as the number
                           of calls in queue, agent availability, average handle time, and custom calculations.

Use Unified CCE
                           		Administration to create and maintain the Contact Sharing groups and rules. A
                           		group is a collection of skill groups and precision queues across target
                           		systems. Each group has a rule that defines the logic for selecting the best
                           		skill group or precision queue in that group for a routing request. Each group
                           		has an Accept Queue
                              		  If condition to include or exclude the individual skill groups and
                           		precision queues from the group for the routing decision. You can then route
                           		the call to the Unified CCE target system whose precision queue or skill group
                           		is the best match for the group's rule. The target system's routing scripts
                           		determine the final method for handling the request.

Contact Sharing
                                       		  gadgets are enabled only for the Contact Director deployment type.

For Contact Director configuration limits, see the chapter on configuration limits in the Solution Design Guide for Cisco Unified Contact Center Enterprise at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-implementation-design-guides-list.html .

### Contact Sharing Call Flow

The basic Contact Sharing call flow runs as shown in this diagram:

A call comes into the Voice Gateway on the Contact Director.

The Voice Gateway passes the call to CVP for VRU processing.

When the caller opts to speak to an agent, CVP passes the call data to the Router through the VRU PG.

The Router runs a script that assigns the call to a particular Contact Sharing Group. The Router sends the call data to the
                                    Application Gateway to pass to that Contact Sharing node.

The Contact Sharing node uses the Group Rule to determine which skill group or precision queue in its Queue should get the
                                    call. The node passes the selected target instance and its extrapolated guess of the best  skill group or precision queue
                                    back to the Application Gateway.

The Application Gateway passes the information to the Router which routes the call to the selected target instance.

## Failover for
                        	 Contact Sharing

Like all the main
                           		components in Unified CCE, Contact Sharing nodes run in redundant pairs. The
                           		redundant pair operates in hot-standby mode. Side B’s data is kept in sync with
                           		Side A to ensure minimum failover time.

When the Side A
                           		process fails over, Side B takes over routing. Because the nodes operate in
                           		hot-standby mode, Side B does not reread Queues from the database. Side B
                           		requests a snapshot from Live Data. Until the snapshot arrives, Side B
                           		continues routing based on the last available Live Data modified by the current
                           		extrapolated data.

During failover,
                           		some route requests may receive an error. Error handling sends those requests
                           		to the default route. When Side A comes back online, it does not take over
                           		immediately. Side A remains in a ready state until Side B fails over.

The Contact Sharing
                           		process monitors the AW to see whether it has the latest configuration changes.
                           		If the AW configuration database does not have those changes or is not
                           		accessible, the Contact Sharing process switches to the alternate AW
                           		configuration data source.

When core components
                           		fail over on a target instance, reporting data can occasionally zero out. In
                           		that case, the Contact Sharing routing sends calls to the instance with
                           		reported resources. If Live Data does not zero out reporting data, then Contact
                           		Sharing continues to route on stale data until the snapshot information begins
                           		to arrive. If the active Contact Sharing side loses both Live Data connections,
                           		that side goes inactive and fails over to other side.

## Contact Director Installation and Setup

Contact Sharing runs on a Contact Director that you connect with up to three target Unified CCE deployments. You configure the Contact Director to monitor the Live Data feed from the targets. The task
                              flow for installing a Contact Director is as follows:

Task

See

Ensure that virtual machines are ready for installation.

Install Unified Communications Manager.

Installation Guide for Cisco Unified Communications Manager and IM and Presence Service

Install Unified CCE components (Router, Logger, Administration & Data Servers, peripherals).

Optionally, install Cisco Unified Intelligence Center.

Installation and Upgrade Guide for Cisco Unified Intelligence Center

Install Unified CVP.

Installation and Upgrade
                                                   				  Guide for Cisco Unified Customer Voice Portal

### Install Unified CCE

This section expands the installation process outlined in the Cisco Unified Contact Center Enterprise Installation and Upgrade Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-installation-guides-list.html .

After setting up the VMs for the Contact Director, you install the Unified CCE components. The install and configuration of
                                 a Contact Director varies slightly from a Unified CCE deployment. The following table lists the applicable parts of the Unified
                                 CCE install procedures with any necessary changes for the Contact Director:

Task

Steps

Contact
                                             						Director Notes

Install Unified CCE Component Software (running the ICM-CCEInstaller)

—

—

Set up Organizational Units

Add a
                                             						Domain

—

Add
                                             						Organizational Units

—

Add
                                             						Users to Security Groups

—

Set Up Unified CCE Central Controller Components

Add
                                             						Unified CCE Instance

—

Create
                                             						Logger Database

Select NAM .

Create
                                             						HDS Database

—

Add
                                             						Logger Component to Instance

Choose Hosted > Network Application Manager
                                                   							 (NAM) for the Logger Type .

Add
                                             						Router Component to Instance

Set the
                                             						following values for a Contact Director:

Check Enable Remote Network Routing .

Set
                                                   							 the NAM ID .

Check Contact Sharing when you create the Router.

Add
                                             						Administration & Data Server Component to Instance

For a Contact Director, choose Hosted > Network Administration & Data Server for Network Application Manager (NAM) for the Deployment Type .

Set up Peripheral Gateways

Configure Peripheral Gateways

—

Add
                                             						Peripherals to Peripheral Gateways

—

Set Up
                                             						Peripheral Gateways

—

Application Gateway Access Between Systems

Create
                                             						Unified ICM Application Gateway

—

Create
                                             						an INCRP on Each Target Instance

—

Set
                                             						Application Gateway Default Values

—

#### Application
                              	 Gateway Access Between Systems

The Contact
                                    		  Director uses a type of Unified ICM Application Gateway to access a target
                                    		  instance. After adding the components to the target instance, set up a Unified
                                    		  ICM Application Gateway in the Configuration Manager on the Administration
                                    		  & Data Server.

After setting up
                                    		  the Unified ICM Application Gateway, you can reference it with a Unified ICM
                                    		  Remote ICM node in a routing script on the Contact Director.

##### Create Unified ICM
                                 	 Application Gateway

This procedure
                                       		  creates a Unified ICM Application Gateway on the Contact Director. You also
                                       		  need an application gateway on each target Unified CCE system.

Step 1

Open the Configuration Manager on an Administration & Data
                                                			 Server that your Contact Director uses.

Step 2

Select Tools > List
                                                      				  Tools > Application Gateway List .

Step 3

Click Retrieve .

Step 4

Click Add .

Step 5

Specify the
                                                			 following values on the Attributes tab:

Field

Description

Name

A name for
                                                            					 the Unified ICM Application Gateway

Type

Select Remote ICM .

Preferred
                                                            					 Side

Indicates
                                                            					 the preferred side of the Application Gateway to use when both are available.
                                                            					 If only one side is available, that side is always used. This option applies
                                                            					 only for Custom Gateways. For Remote ICM systems, a suffix on the connection
                                                            					 address indicates the preference.

Encryption

Indicates
                                                            					 whether requests to the Application Gateway are encrypted. Select None .

Fault
                                                            					 Tolerance

Specify
                                                            					 the fault-tolerance strategy that the Application Gateway uses.

Connection

Select Duplex .

Description

Any
                                                            					 additional information about the Unified ICM Application Gateway.

Step 6

Save your
                                                			 changes to create the Unified ICM Application Gateway.

Copy down
                                                               				  the Unified ICM Application Gateway ID value. You use the ID when you set up
                                                               				  the INCRP NIC on the target instance.

Step 7

Select either
                                                			 of the Connection tabs to set the connection information.

Step 8

Click Enter
                                                   				Address .

Step 9

Specify the
                                                			 following information:

Field

Description

IP
                                                            					 Address/Name

Enter the
                                                            					 Public (high priority) IP address of the target instance. Alternatively, You
                                                            					 can use the SAN with assistance from your Cisco certified partner or TAC. Use
                                                            					 the same
                                                               						address that you specified for the INCRP NIC on the target instance. You
                                                            					 can use the hostname in place of the address.

Instance
                                                            					 Number

Enter the
                                                            					 number of the customer ICM on the target instance (0 — 24).

Side

Indicate
                                                            					 which side of the Contact Director prefers this connection:

Side A —Contact Director
                                                                  						  Side A prefers to use this connection.

Side B —Contact Director
                                                                  						  Side B prefers to use this connection.

None —Neither side of
                                                                  						  the Contact Director prefers to use this connection.

Both Side A and B —Both
                                                                  						  sides of the Contact Director prefer to use this connection.

Use this
                                                                        						setting to avoid unnecessary WAN traffic. For example, if you collocate Contact
                                                                        						Director Side A with target instance Side A, this correct choice avoids WAN
                                                                        						traffic to the other side.

The Enter Contact Director Address dialog displays different fields depending on the type of Application Gateway chosen.

Step 10

Repeat this
                                                			 process for the other side of the redundant pair.

Step 11

Save your work
                                                			 and exit the dialog.

##### Create an INCRP on
                                 	 Each Target Instance

The Contact
                                       		  Director communicates with the target instance by an INCRP NIC. Perform this
                                       		  procedure on each target instance.

Step 1

From the
                                                			 Configuration Manager menu on the target instance, select Tools
                                                   				> Explorer Tools > NIC Explorer . The NIC
                                                   				Explorer window appears.

Step 2

In the Select
                                                   				Filter Data box, click Retrieve .

Step 3

Select a NIC
                                                			 or click the Add
                                                   				NIC button to create a new NIC.

Step 4

Specify the
                                                			 following values on the Logical Interface Controller tab:

Name

An
                                                            					 enterprise name that serves as the NIC name.

Client
                                                            					 Type

Select INCRP .

Step 5

Click the Add
                                                   				Physical Interface Controller button.

Step 6

Specify an Enterprise Name and click OK .

Step 7

In the NIC
                                                			 tree window, click the routing client for your newly created NIC.

Step 8

Specify the
                                                			 following values on the Routing Client tab:

Option

Description

Name

An
                                                            					 enterprise name that serves as the Routing Client name.

Configuration Parameters

/customerID
                                                               						<RCID> where <RCID> is the Routing Client ID of the
                                                            					 matching routing client on the Contact Director.

Network Routing Client

The same value as the Name field.

Step 9

Click Save .

##### Set Application
                                 	 Gateway Default Values

If you see
                                       		  performance issues, the Cisco Technical Assistance Center might advise you to
                                       		  change some of the application gateway's default values. Use the following
                                       		  procedure to change these values.

Step 1

In the Configuration Manager , select Enterprise > System
                                                      				  Information > System
                                                      				  Information . The System
                                                   				Information dialog appears.

Step 2

In the Application Gateway section, select Remote
                                                   				ICM .

Step 3

Use the other
                                                			 tabs to set the default values for the Unified ICM Application Gateway
                                                			 connections. Take account of the Contact Director NIC settings for timeout,
                                                			 late, and so on as you set the Unified ICM Application Gateway timeout settings
                                                			 for a target Unified CCE system.

Step 4

Click OK and close the dialog.

### Install Cisco Unified Intelligence Center (Optional)

To run the Contact Sharing reports at the Contact Director site, you can install Cisco Unified Intelligence Center there.
                                 For installation procedures, see the Installation and Upgrade Guide for Cisco Unified Intelligence Center at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-intelligence-center/products-installation-guides-list.html .

### Install Unified CVP

The Contact Director uses Unified CVP for VRU processing of the incoming calls. For installation procedures, see the Installation and Upgrade
                                          				  Guide for Cisco Unified Customer Voice Portal at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-customer-voice-portal/products-installation-guides-list.html .

The Unified CCE Reference Designs specify that you use Unified CVP. In a non-Reference Design deployment, you can alternately
                                             use Unified IP IVR or a third-party VRU.

## Set Up Contact
                        	 Sharing

After installing the Contact Director and connecting the Contact Director to the target Unified CCE instances, you set up
                           the contact sharing feature as follows:

Task

See this Topic

Set up the contact sharing node on the Contact Director.

Set Up a Contact Sharing Node

Set up the machine inventory for the contact sharing node.

Set up Contact Sharing Machine Inventory

Add contact sharing rules.

Add and Maintain Rules

Add contact sharing groups.

Add and Maintain Groups

Your solution can only have one contact sharing node.

### Set Up a Contact
                           	 Sharing Node

You set up a contact sharing node, as opposed to the target instances, with the same procedure for setting up an application
                                 gateway.

Step 1

In the
                                          			 Configuration Manager, select Tools > List
                                                				  Tools > Application Gateway List . The Application Gateway List window appears.

Step 2

To enable Add , click Retrieve .

Step 3

Click Add . The Attributes tab appears.

Step 4

Fill out the Attributes tab as follows:

Name of
                                                      					 your contact sharing node

Contact
                                                      					 Share

Step 5

On the Connection Side A tab, set the Address field to the router's IP address. The
                                          			 default port is 5070.

Step 6

On the Connection Side B tab, set the Address field to the router's IP address. The
                                          			 default port is 5070.

Step 7

Click Save to create the contact sharing node.

### Set up Contact
                           	 Sharing Machine Inventory

You set up the
                                 		  machine inventory for contact sharing through the icm/bin/csMachineInventory.csv file. 
                                 		Changes to the machine inventory do not take effect until the router restarts.

Step 1

Open your
                                          			 machine inventory file for contact sharing, by default csMachineInventory.csv .

Step 2

Follow the
                                          			 instructions for editing the csMachineInventory.csv file. The instructions are
                                          			 contained within the file.

Step 3

Run the
                                          			 following command:

csMachineInventory.bat [options] username password inputfile

Machine
                                                   						inventory file, including the path, for contact sharing, by default csMachineInventory.csv

#### What to do next

If the router has already started, restart the router after setting up the machine inventory.

### Add and Maintain
                           	 Rules

Contact Sharing
                                             			 comes with a default rule that cannot be deleted or modified. The name of this
                                             			 rule is DefaultRule .

Step 1

Navigate to CCE Web Administration > Feature > Contact Share Rules .

Step 2

Click New to open the New
                                             				Rule window, or click an existing rule to open the Edit
                                             				Rule window.

Step 3

Complete the
                                          			 following fields:

Yes

Enter a name using up to 32 alphanumeric characters, periods
                                                         							 (.), and underscores (_). The name must start with an alphanumeric character.

Expression

Yes

Enter a formula that the Contact Share server uses to select the skill group or
                                                         							 precision queue from a Contact Sharing group for a routing request.

Description

No

Enter up to 255 characters to describe the rule.

Step 4

Click Save to return to the List window.

Step 5

To delete a
                                          			 rule, do one of the following:

- To delete a single rule,
                                             				hover over the row for that rule and click the trash can icon at the end of the row.

- To delete up to 50 rules,
                                             				check the check box for each rule that you want to delete. To select all rules
                                             				in a list, check the Select All check box in the list header. Click Delete .

Deleting a
                                             				rule is permanent.

#### Add a New Rule by
                              	 Copying an Existing Rule

You can also create a new rule by copying an existing rule. The Description and Expression fields are copied to the new rule.

Step 1

Navigate to Unified CCE Administration > Feature > Contact Share Rules .

Step 2

Either:

- Click the rule you want to
                                                				copy, and then click the Copy button in the Edit
                                                   				  Rule window.

- Hover over the row for that
                                                				rule, and click the copy icon that appears at the end of the row.

Step 3

Enter a Name for the rule, using up to 32 alphanumeric
                                             			 characters, periods (.), and underscores (_). The name must start with an
                                             			 alphanumeric character.

Step 4

Review Description and Expression fields that were copied from the original
                                             			 rule, and make any necessary changes.

Step 5

Click Save .

### Add and Maintain
                           	 Groups

#### Before you begin

Ensure that the Live Data connection is active before you configure Groups.

Step 1

Navigate to CCE Web Administration > Feature > Contact Share Groups .

Step 2

Click New to open the New
                                             				Group window, or click an existing group to open the Edit
                                             				Group window.

Step 3

Complete the
                                          			 following fields:

Yes

Enter a name using up to 32 alphanumeric characters, periods
                                                         							 (.), and underscores (_). The name must start with an alphanumeric character.

Description

No

Enter up to 255 characters to describe the group.

Rule

Yes

Select a rule that defines the logic for selecting a skill group
                                                         							 or precision queue in this group for a routing request:

Click the magnifying glass icon to display the Select Rule window.

Click the row to select a rule.

Accept Queue If

No

Enter a logical expression to determine if the individual skill
                                                         							 groups and precision queues in the group can be included in the routing
                                                         							 decision.

Step 4

Complete the
                                          			 Queues tab:

This tab shows
                                             				the list of queues for this group.

Click Add to open Add
                                                   					 Queues .

Click the
                                                				  queues you want to add to this group. The queues you chose appear on the List of Queues .

Close Add Queues .

Click Save on this tab to return to the List window.

The maximum number of queues is 100.

Step 5

To delete a
                                          			 group, do one of the following:

- To delete a single group, hover over the row for that group and click the trash can icon at the end of the row.

- To select all groups in a list, check the Select All check box in the list header. Click Delete .

Deleting a
                                             				group is permanent.

## Scripting for Contact Sharing

### Expression Formula
                           	 for Contact Sharing

#### About Contact
                              	 Sharing Expression Formula

You can enter
                                 		expressions for the following fields:

Field

Description

Accept Queue If for a group

A logical
                                             					 expression to determine whether to include the individual skill groups or
                                             					 precision queues in the Contact Sharing group in the routing decision. The
                                             					 field is a freeform editor with a maximum length of 512 characters. 
                                             				  Any result except zero evaluates as TRUE.

There is an implicit Accept Queue If of Queue.*.LoggedOn > 0 . You cannot override this implicit check.

Expression for
                                             					 a rule

A formula
                                             					 that the Contact Share server uses to calculate the value to be considered
                                             					 against other queues in a Contact Sharing group. The expression always selects
                                             					 the queue with the minimum value. The field is a freeform editor with a maximum
                                             					 length of 512 characters.

#### Contact Sharing
                              	 Expression Format

To evaluate all the
                                 		skill groups and precision queues in a Contact Sharing group, use this syntax:

```
Queue.*. <FieldName>
```

Where FieldName is the name of the field that the expression
                                 		evaluates, for example, Ready .

To evaluate a specific skill group or precision queue, use this syntax:

```
<ObjectType>.<InstanceName>/<TargetQueueName>.<FieldName>
```

ObjectType must be SkillGroup or PrecisionQueue.

InstanceName is the application gateway name.

TargetQueueName is the enterprise name of the skill group or precision queue in the target system.

FieldName is the name of the field that the expression evaluates.

#### Contact Sharing
                              	 Expression Examples

The following
                                 		examples demonstrate some basic Contact Sharing expressions.

##### Expression for
                                    		  a Group

A Contact Sharing
                                    		  group can take an Accept Queue If expression. The expression determines whether
                                    		  to include specific skill groups and precision queues in the group in the
                                    		  routing decision.

```
Queue.*.Avail > 5
```

This expression
                                    		  accepts all queues with more than five agents that are available.

##### Expression for a Skill Group

```
SkillGroup.<InstanceName>/<TargetQueueName>.Avail > 5
```

This expression accepts the named skill group if it has more than five agents available.

##### Expression for a Precision Queue

```
PrecisionQueue.<InstanceName>/<TargetQueueName>.Avail > 5
```

This expression accepts the named precision queue if it has more than five agents available.

##### Expression for
                                    		  a Rule

A rule must take
                                    		  an expression. The expression selects a skill group or precision queue from a
                                    		  Contact Sharing group.

```
-1 * (Queue.*.Avail)
```

This expression
                                    		  selects the queue with the most available agents.

##### Expression for MED Only

This expression calculates the Minimum Expected Delay (MED) to determine which target system receives the call for routing.

```
(Queue.*.QueuedNow+1)*(Queue.*.AvgHandledCallsTimeToInterval>0? 
Queue.*.AvgHandledCallsTimeToInterval: 120) / (Queue.*.Ready>0?Queue.*.Ready:1)
```

##### The Default
                                    		  Rule

Contact Sharing
                                    		  comes with a default rule. You cannot modify or delete the default rule. The
                                    		  default rule combines a MED calculation with an Agent Occupancy calculation to
                                    		  determine which target system receives the call for routing.

If there are calls in
                                       			 queue,

```
Queue.*.QueuedNow > 0?
```

Then use the MED
                                       			 calculation:

```
((Queue.*.QueuedNow+1)*(Queue.*.AvgHandledCallsTimeToInterval>0?
 Queue.*.AvgHandledCallsTimeToInterval: 120)/(Queue.*.Ready>0?Queue.*.Ready:1)):
```

Otherwise, use the Agent
                                       			 Occupancy calculation:

```
(((Queue.*.LoggedOnTimeToInterval - Queue.*.NotReadyTimeToInterval)==0
||(Queue.*.AvailTimeToInterval <= 10 * Queue.*.XAvail) )? 
0: -1*(Queue.*.AvailTimeToInterval-10 * Queue.*.XAvail)/
(Queue.*.LoggedOnTimeToInterval - Queue.*.NotReadyTimeToInterval))
```

This expression
                                    		  chooses a queue on the target instance with the least occupied agents or the
                                    		  least queued calls.

The default rule is only an example.  Customize the rule to match your needs or write your own rules.

#### Contact Sharing
                              	 Expression Reference

##### Supported
                                    		  Operations

The following
                                    		  table lists the supported operations:

Type of
                                                						Operation

Operator

Description

Conditional

&&

Conditional-AND

||

Conditional-OR

? :

Ternary
                                                						(shorthand for if-then-else statement)

ex. A ? B : C

If A,
                                                						then B, otherwise C.

Relational

==

Equal to

!=

Not
                                                						equal to

>

Greater
                                                						than

>=

Greater
                                                						than or equal to

<

Less
                                                						than

<=

Less
                                                						than or equal to

Bitwise
                                                						and Bit Shift

~

Unary
                                                						bitwise complement

<<

Signed
                                                						left shift

>>

Signed
                                                						right shift

&

Bitwise
                                                						AND, for strings, also used for string concatenation

^

Bitwise
                                                						exclusive OR

|

Bitwise
                                                						inclusive OR

Arithmetic

+

Addition

-

Subtraction

*

Multiplication

/

Division

%

Percentage

Prefix

+

Unary
                                                						plus operator; indicates positive value

-

Unary
                                                						minus operator; negates an expression

!

Logical complement operator; inverts the value of a boolean

Wildcard

*

Wildcard support similar to the expression used in router. For
                                                						example, in SkillGroup.*.Ready , the actual target replaces the
                                                						asterisk when applying the expression.

##### Supported Objects and Fields

The following table lists the fields available from the Live Data feed
                                    		  or calculated by Contact Sharing for use in Contact Sharing expressions:

Field Name

Description

ApplicationAvailable

The number of agents belonging to this Queue who are
                                                						currently ApplicationAvailable for the MRD to which the Queue belongs. An agent
                                                						is Application available if the agent is Not Routable and Available for the
                                                						MRD.

Avail

The extrapolated number of agents in the READY state for
                                                						this Queue. The extrapolation is as follows:

(The number of agents that Live Data reports in READY state)
                                                						- XAvail

If the extrapolation results in a negative number, Contact
                                                						Sharing sets this field to zero.

AvailTimeToInterval

Total seconds agents in the Queue have been in the READY
                                                						state during the current interval.

AvgHandledCallsTimeToInterval

Average handle time in seconds for calls counted as handled
                                                						by the Queue during the interval.

BusyOther

Number of agents currently in the BusyOther state for this
                                                						Queue.

CallsHandledToInterval

Calls that by been answered and have completed wrap-up by
                                                						the Queue during the interval.

Hold

The number of agents that have all active calls on hold.

ICMAvailable

The number of agents belonging to this Queue who are
                                                						currently ICMAvailable for the MRD to which the Queue belongs. An agent is ICM
                                                						available if the agent is Routable and Available for the MRD.

LoggedOn

Number of agents that are currently logged on to the Queue.

LoggedOnTimeToInterval

Total time, in seconds, agents were logged on to the Queue
                                                						during the current interval.

NotReady

Number of agents in the Not Ready state for the Queue.

NotReadyTimeToInterval

Total seconds agents in the Queue have been in the Not Ready
                                                						state during the interval.

QueuedNow

The extrapolated number of calls currently queued to this
                                                						Queue. The extrapolation is as follows:

(The number of calls that Live Data reports queued to the
                                                						Queue) + XQueuedNow

Ready

The number of agents who are Routable for the MRD associated
                                                						with this Queue, and whose state for this Queue is not currently NOT_READY or
                                                						WORK_NOT_READY.

ReseveredAgents

The number of agents for the Queue currently in the Reserved
                                                						state.

TalkingAutoOut

The number of agents in the Queue currently talking on
                                                						AutoOut (predictive) calls.

TalkingIn

The number of agents in the Queue currently talking on
                                                						inbound calls.

TalkingOther

The number of agents in the Queue currently talking on
                                                						internal calls, rather than inbound or outbound calls. Examples of other calls
                                                						include agent-to-agent transfers and supervisor calls.

TalkingOut

The number of agents in the Queue currently talking on
                                                						outbound calls.

TalkingPreview

The number of agents in the Queue currently talking on
                                                						outbound Preview calls.

TalkingReserve

The number of agents in the Queue currently talking on agent
                                                						reservation calls.

WorkNotReady

The number of agents in the Queue in the Work Not Ready
                                                						state.

WorkReady

The number of agents in the Queue in the Work Ready state.

XAvail

The number of Contact Sharing requests assigned to the
                                                						available agent count for this Queue during the extrapolation period. The
                                                						extrapolation period defaults to 10 seconds.

Contact Sharing request increments this field when QueuedNow
                                                						= 0 and Avail > 0.

XQueuedNow

The number of Contact Sharing requests assigned to the
                                                						queued call count for this Queue during the extrapolation period. The
                                                						extrapolation period defaults to 10 seconds.

Contact Sharing request increments this field when one of
                                                						the following conditions apply:

QueuedNow = 0 and Avail = 0

QueuedNow > 0 and Avail = 0

QueuedNow > 0 and Avail > 0

The following table lists the Call Variables that are available for
                                    		  use in Contact Sharing expressions:

Call Variable Name

Description

CallerEnteredDigits

Digits caller entered in response to prompts.

CallingLineID

Billing phone number of the caller. (Commonly referred to as
                                                						CLID).

CustomerProvidedDigits

Digits to be passed to the call recipient.

DialedNumberString

Phone number dialed by the caller.

PeripheralVariable1 through 10

Value passed to and from the peripheral.

RouterCallDay

An encoded value that indicates the date on which the
                                                						software processes the call.

RouterCallKey

A value that is unique among all calls the software has
                                                						processed since midnight. RouterCallDay and RouterCallKey combine to form a
                                                						unique call identifier.

RoutingClient

Name of the routing client making the route request.

### Routing and
                           	 Scripting for Contact Sharing

Contact Sharing uses two non-persistent call variables, Call.ContactShareStatus and Call.ContactShareTarget .

A successful route request returns Call.ContactShareStatus populated with the application
                              		gateway selected to receive the call. Use the call variable to route the call
                              		to the target Unified CCE instance.

Call.ContactShareTarget is populated only when the
                              		Gateway node takes a success path. The variable contains the target queue type
                              		and the target queue id. The target queue id is the Skill Group ID or Precision
                              		Queue ID on the target instance. The format is "Target Type, Target Queue ID".
                              		For example, "SG,5000 or PQ,5005". You can pass this data to the target
                              		instance in a call or ECC variable. Then, you have the Contact Sharing result
                              		available to use in scripting on the target instance.

### Error Handling for
                           	 Contact Sharing

If a Contact Share route request fails, the router populates Call.ContactShareStatus with the following error codes.
                              		The call flow takes the failure branch out of the Gateway node.
                              	 The error codes appear in the RCD table.

Status Variable

Description

CS_NOT_CONNECTED (2)

No connection to the contact share process.

CS_TIMED_OUT (3)

Request to the contact share process failed.

CS_CONFIG_ERROR (4)

Contact share process encountered a configuration related
                                          					 error.

CS_EXECUTION_ERROR (5)

Contact share process encountered an expression execution
                                          					 related error.

CS_APPGTW_ERROR (8)

Unable to lookup the application gateway with the code that
                                          					 the contact share process returned.

CS_UNKNOWN_ERROR (9)

Contact sharing encountered an unknown error.

The following error messages can also appear:

Status Variable

Description

ERROR_CONTACT_SHARE_GROUP_NOT_FOUND (1)

The Contact Share Group with the listed ID was not found.

ERROR_CONTACT_SHARE_RULE_NOT_FOUND (2)

The Contact Share Rule with the listed ID was not found.

ERROR_CONTACT_SHARE_RULE_EXPRESSION_INVALID (3)

The Contact Share Rule has an invalid rule expression.

ERROR_CONTACT_SHARE_GROUP_CONSIDERIF_EXPRESSION_INVALID (4)

The Contact Share Rule has an invalid AcceptQueueIf expression.

ERROR_CONTACT_SHARE_GROUP_NO_QUEUE_CONFIGURED (5)

There are no queues configured for the Contact Share Group.

ERROR_CONTACT_SHARE_ROUTING_EXCEPTION (6)

The route request failed for an unspecified reason.

ERROR_CONTACT_SHARE_ROUTING_NO_ELIGIBLE_TARGET (7)

No eligible queue was found for the route request.

ERROR_CONTACT_SHARE_ROUTING_TARGET_CONGESTED (8)

No eligible queue was found for the route request because of congestion control.

### Other Scripting
                           	 Considerations

A simple Contact Sharing script looks like the following:

Consider the
                                 		  following points when you create Contact Sharing scripts:

Always double check the logic in the routing to the Contact Sharing node.

Tip

If you see all calls routing to one target system, check the IP Addresses in the machine inventory table and your script.
                                                   The relationship between the Application Gateway ID and the IP Addresses might be wrong.

Use Call Tracer to test your
                                       				call flows.

Never put two Contact Sharing nodes in the same path of your script.

To search for a particular Contact Sharing node, use the string selection
                                       				type to search for the Contact Sharing Group name.

Contact Sharing returns the current Application Gateway name, not the
                                       				ID. If you change the Application Gateway name for one of your target systems, change your scripts to match the new name.

#### Script with Extrapolation in Mind

Contact Sharing's extrapolation assumes that the target systems route calls within the same Contact Sharing Group that the
                                 Contact Director used. If the target system's router does not follow this assumption, Contact Sharing's extrapolated data
                                 gets out of sync.

For Contact Sharing, have the target system route by one of the following methods:

Route to the skill group or precision queue specified in Call.ContactShareTarget . You can pass the value from the Contact Director to the target system in a call or ECC variable.

Route only among the same skill groups and precision queues that are part of the Contact Sharing Group that the Contact Director
                                       used.

| Note | Contact Sharing
                                       		  gadgets are enabled only for the Contact Director deployment type. |
|---|---|

| Task | See |
|---|---|
| Ensure that virtual machines are ready for installation. | Cisco Unified Contact Center Enterprise Installation and Upgrade Guide |
| Install Unified Communications Manager. | Installation Guide for Cisco Unified Communications Manager and IM and Presence Service |
| Install Unified CCE components (Router, Logger, Administration & Data Servers, peripherals). | Cisco Unified Contact Center Enterprise Installation and Upgrade Guide |
| Optionally, install Cisco Unified Intelligence Center. | Installation and Upgrade Guide for Cisco Unified Intelligence Center |
| Install Unified CVP. | Installation and Upgrade
                                                   				  Guide for Cisco Unified Customer Voice Portal |

| Task | Steps | Contact
                                             						Director Notes |
|---|---|---|
| Install Unified CCE Component Software (running the ICM-CCEInstaller) | — | — |
| Set up Organizational Units | Add a
                                             						Domain | — |
| Add
                                             						Organizational Units | — |
| Add
                                             						Users to Security Groups | — |
| Set Up Unified CCE Central Controller Components | Add
                                             						Unified CCE Instance | — |
| Create
                                             						Logger Database | Select NAM . |
| Create
                                             						HDS Database | — |
| Add
                                             						Logger Component to Instance | Choose Hosted > Network Application Manager
                                                   							 (NAM) for the Logger Type . |
| Add
                                             						Router Component to Instance | Set the
                                             						following values for a Contact Director: Check Enable Remote Network Routing . Set
                                                   							 the NAM ID . Check Contact Sharing when you create the Router. |
| Add
                                             						Administration & Data Server Component to Instance | For a Contact Director, choose Hosted > Network Administration & Data Server for Network Application Manager (NAM) for the Deployment Type . |
| Set up Peripheral Gateways | Configure Peripheral Gateways | — |
| Add
                                             						Peripherals to Peripheral Gateways | — |
| Set Up
                                             						Peripheral Gateways | — |
| After completing the standard installation, perform these Contact Director-specific setup procedures. |
| Application Gateway Access Between Systems | Create
                                             						Unified ICM Application Gateway | — |
| Create
                                             						an INCRP on Each Target Instance | — |
| Set
                                             						Application Gateway Default Values | — |

| Step 1 | Open the Configuration Manager on an Administration & Data
                                                			 Server that your Contact Director uses. |
|---|---|
| Step 2 | Select Tools > List
                                                      				  Tools > Application Gateway List . The Application Gateway List window appears. |
| Step 3 | Click Retrieve . |
| Step 4 | Click Add . The Attributes tab appears. |
| Step 5 | Specify the
                                                			 following values on the Attributes tab: Field Description Name A name for
                                                            					 the Unified ICM Application Gateway Type Select Remote ICM . Preferred
                                                            					 Side Indicates
                                                            					 the preferred side of the Application Gateway to use when both are available.
                                                            					 If only one side is available, that side is always used. This option applies
                                                            					 only for Custom Gateways. For Remote ICM systems, a suffix on the connection
                                                            					 address indicates the preference. Encryption Indicates
                                                            					 whether requests to the Application Gateway are encrypted. Select None . Fault
                                                            					 Tolerance Specify
                                                            					 the fault-tolerance strategy that the Application Gateway uses. Connection Select Duplex . Description Any
                                                            					 additional information about the Unified ICM Application Gateway. | Field | Description | Name | A name for
                                                            					 the Unified ICM Application Gateway | Type | Select Remote ICM . | Preferred
                                                            					 Side | Indicates
                                                            					 the preferred side of the Application Gateway to use when both are available.
                                                            					 If only one side is available, that side is always used. This option applies
                                                            					 only for Custom Gateways. For Remote ICM systems, a suffix on the connection
                                                            					 address indicates the preference. | Encryption | Indicates
                                                            					 whether requests to the Application Gateway are encrypted. Select None . | Fault
                                                            					 Tolerance | Specify
                                                            					 the fault-tolerance strategy that the Application Gateway uses. | Connection | Select Duplex . | Description | Any
                                                            					 additional information about the Unified ICM Application Gateway. |
| Field | Description |
| Name | A name for
                                                            					 the Unified ICM Application Gateway |
| Type | Select Remote ICM . |
| Preferred
                                                            					 Side | Indicates
                                                            					 the preferred side of the Application Gateway to use when both are available.
                                                            					 If only one side is available, that side is always used. This option applies
                                                            					 only for Custom Gateways. For Remote ICM systems, a suffix on the connection
                                                            					 address indicates the preference. |
| Encryption | Indicates
                                                            					 whether requests to the Application Gateway are encrypted. Select None . |
| Fault
                                                            					 Tolerance | Specify
                                                            					 the fault-tolerance strategy that the Application Gateway uses. |
| Connection | Select Duplex . |
| Description | Any
                                                            					 additional information about the Unified ICM Application Gateway. |
| Step 6 | Save your
                                                			 changes to create the Unified ICM Application Gateway. Note Copy down
                                                               				  the Unified ICM Application Gateway ID value. You use the ID when you set up
                                                               				  the INCRP NIC on the target instance. | Note | Copy down
                                                               				  the Unified ICM Application Gateway ID value. You use the ID when you set up
                                                               				  the INCRP NIC on the target instance. |
| Note | Copy down
                                                               				  the Unified ICM Application Gateway ID value. You use the ID when you set up
                                                               				  the INCRP NIC on the target instance. |
| Step 7 | Select either
                                                			 of the Connection tabs to set the connection information. |
| Step 8 | Click Enter
                                                   				Address . The Enter
                                                   				Contact Director Address dialog appears. |
| Step 9 | Specify the
                                                			 following information: Field Description IP
                                                            					 Address/Name Enter the
                                                            					 Public (high priority) IP address of the target instance. Alternatively, You
                                                            					 can use the SAN with assistance from your Cisco certified partner or TAC. Use
                                                            					 the same
                                                               						address that you specified for the INCRP NIC on the target instance. You
                                                            					 can use the hostname in place of the address. Instance
                                                            					 Number Enter the
                                                            					 number of the customer ICM on the target instance (0 — 24). Side Indicate
                                                            					 which side of the Contact Director prefers this connection: Side A —Contact Director
                                                                  						  Side A prefers to use this connection. Side B —Contact Director
                                                                  						  Side B prefers to use this connection. None —Neither side of
                                                                  						  the Contact Director prefers to use this connection. Both Side A and B —Both
                                                                  						  sides of the Contact Director prefer to use this connection. Note Use this
                                                                        						setting to avoid unnecessary WAN traffic. For example, if you collocate Contact
                                                                        						Director Side A with target instance Side A, this correct choice avoids WAN
                                                                        						traffic to the other side. Note The Enter Contact Director Address dialog displays different fields depending on the type of Application Gateway chosen. | Field | Description | IP
                                                            					 Address/Name | Enter the
                                                            					 Public (high priority) IP address of the target instance. Alternatively, You
                                                            					 can use the SAN with assistance from your Cisco certified partner or TAC. Use
                                                            					 the same
                                                               						address that you specified for the INCRP NIC on the target instance. You
                                                            					 can use the hostname in place of the address. | Instance
                                                            					 Number | Enter the
                                                            					 number of the customer ICM on the target instance (0 — 24). | Side | Indicate
                                                            					 which side of the Contact Director prefers this connection: Side A —Contact Director
                                                                  						  Side A prefers to use this connection. Side B —Contact Director
                                                                  						  Side B prefers to use this connection. None —Neither side of
                                                                  						  the Contact Director prefers to use this connection. Both Side A and B —Both
                                                                  						  sides of the Contact Director prefer to use this connection. Note Use this
                                                                        						setting to avoid unnecessary WAN traffic. For example, if you collocate Contact
                                                                        						Director Side A with target instance Side A, this correct choice avoids WAN
                                                                        						traffic to the other side. | Note | Use this
                                                                        						setting to avoid unnecessary WAN traffic. For example, if you collocate Contact
                                                                        						Director Side A with target instance Side A, this correct choice avoids WAN
                                                                        						traffic to the other side. | Note | The Enter Contact Director Address dialog displays different fields depending on the type of Application Gateway chosen. |
| Field | Description |
| IP
                                                            					 Address/Name | Enter the
                                                            					 Public (high priority) IP address of the target instance. Alternatively, You
                                                            					 can use the SAN with assistance from your Cisco certified partner or TAC. Use
                                                            					 the same
                                                               						address that you specified for the INCRP NIC on the target instance. You
                                                            					 can use the hostname in place of the address. |
| Instance
                                                            					 Number | Enter the
                                                            					 number of the customer ICM on the target instance (0 — 24). |
| Side | Indicate
                                                            					 which side of the Contact Director prefers this connection: Side A —Contact Director
                                                                  						  Side A prefers to use this connection. Side B —Contact Director
                                                                  						  Side B prefers to use this connection. None —Neither side of
                                                                  						  the Contact Director prefers to use this connection. Both Side A and B —Both
                                                                  						  sides of the Contact Director prefer to use this connection. Note Use this
                                                                        						setting to avoid unnecessary WAN traffic. For example, if you collocate Contact
                                                                        						Director Side A with target instance Side A, this correct choice avoids WAN
                                                                        						traffic to the other side. | Note | Use this
                                                                        						setting to avoid unnecessary WAN traffic. For example, if you collocate Contact
                                                                        						Director Side A with target instance Side A, this correct choice avoids WAN
                                                                        						traffic to the other side. |
| Note | Use this
                                                                        						setting to avoid unnecessary WAN traffic. For example, if you collocate Contact
                                                                        						Director Side A with target instance Side A, this correct choice avoids WAN
                                                                        						traffic to the other side. |
| Note | The Enter Contact Director Address dialog displays different fields depending on the type of Application Gateway chosen. |
| Step 10 | Repeat this
                                                			 process for the other side of the redundant pair. |
| Step 11 | Save your work
                                                			 and exit the dialog. |

| Field | Description |
|---|---|
| Name | A name for
                                                            					 the Unified ICM Application Gateway |
| Type | Select Remote ICM . |
| Preferred
                                                            					 Side | Indicates
                                                            					 the preferred side of the Application Gateway to use when both are available.
                                                            					 If only one side is available, that side is always used. This option applies
                                                            					 only for Custom Gateways. For Remote ICM systems, a suffix on the connection
                                                            					 address indicates the preference. |
| Encryption | Indicates
                                                            					 whether requests to the Application Gateway are encrypted. Select None . |
| Fault
                                                            					 Tolerance | Specify
                                                            					 the fault-tolerance strategy that the Application Gateway uses. |
| Connection | Select Duplex . |
| Description | Any
                                                            					 additional information about the Unified ICM Application Gateway. |

| Note | Copy down
                                                               				  the Unified ICM Application Gateway ID value. You use the ID when you set up
                                                               				  the INCRP NIC on the target instance. |
|---|---|

| Field | Description |
|---|---|
| IP
                                                            					 Address/Name | Enter the
                                                            					 Public (high priority) IP address of the target instance. Alternatively, You
                                                            					 can use the SAN with assistance from your Cisco certified partner or TAC. Use
                                                            					 the same
                                                               						address that you specified for the INCRP NIC on the target instance. You
                                                            					 can use the hostname in place of the address. |
| Instance
                                                            					 Number | Enter the
                                                            					 number of the customer ICM on the target instance (0 — 24). |
| Side | Indicate
                                                            					 which side of the Contact Director prefers this connection: Side A —Contact Director
                                                                  						  Side A prefers to use this connection. Side B —Contact Director
                                                                  						  Side B prefers to use this connection. None —Neither side of
                                                                  						  the Contact Director prefers to use this connection. Both Side A and B —Both
                                                                  						  sides of the Contact Director prefer to use this connection. Note Use this
                                                                        						setting to avoid unnecessary WAN traffic. For example, if you collocate Contact
                                                                        						Director Side A with target instance Side A, this correct choice avoids WAN
                                                                        						traffic to the other side. | Note | Use this
                                                                        						setting to avoid unnecessary WAN traffic. For example, if you collocate Contact
                                                                        						Director Side A with target instance Side A, this correct choice avoids WAN
                                                                        						traffic to the other side. |
| Note | Use this
                                                                        						setting to avoid unnecessary WAN traffic. For example, if you collocate Contact
                                                                        						Director Side A with target instance Side A, this correct choice avoids WAN
                                                                        						traffic to the other side. |

| Note | Use this
                                                                        						setting to avoid unnecessary WAN traffic. For example, if you collocate Contact
                                                                        						Director Side A with target instance Side A, this correct choice avoids WAN
                                                                        						traffic to the other side. |
|---|---|

| Note | The Enter Contact Director Address dialog displays different fields depending on the type of Application Gateway chosen. |
|---|---|

| Step 1 | From the
                                                			 Configuration Manager menu on the target instance, select Tools
                                                   				> Explorer Tools > NIC Explorer . The NIC
                                                   				Explorer window appears. |
|---|---|
| Step 2 | In the Select
                                                   				Filter Data box, click Retrieve . |
| Step 3 | Select a NIC
                                                			 or click the Add
                                                   				NIC button to create a new NIC. |
| Step 4 | Specify the
                                                			 following values on the Logical Interface Controller tab: Field Description Name An
                                                            					 enterprise name that serves as the NIC name. Client
                                                            					 Type Select INCRP . | Field | Description | Name | An
                                                            					 enterprise name that serves as the NIC name. | Client
                                                            					 Type | Select INCRP . |
| Field | Description |
| Name | An
                                                            					 enterprise name that serves as the NIC name. |
| Client
                                                            					 Type | Select INCRP . |
| Step 5 | Click the Add
                                                   				Physical Interface Controller button. The
                                                			 Physical Interface Controller dialog displays. |
| Step 6 | Specify an Enterprise Name and click OK . |
| Step 7 | In the NIC
                                                			 tree window, click the routing client for your newly created NIC. |
| Step 8 | Specify the
                                                			 following values on the Routing Client tab: Option Description Name An
                                                            					 enterprise name that serves as the Routing Client name. Configuration Parameters /customerID
                                                               						<RCID> where <RCID> is the Routing Client ID of the
                                                            					 matching routing client on the Contact Director. Network Routing Client The same value as the Name field. | Option | Description | Name | An
                                                            					 enterprise name that serves as the Routing Client name. | Configuration Parameters | /customerID
                                                               						<RCID> where <RCID> is the Routing Client ID of the
                                                            					 matching routing client on the Contact Director. | Network Routing Client | The same value as the Name field. |
| Option | Description |
| Name | An
                                                            					 enterprise name that serves as the Routing Client name. |
| Configuration Parameters | /customerID
                                                               						<RCID> where <RCID> is the Routing Client ID of the
                                                            					 matching routing client on the Contact Director. |
| Network Routing Client | The same value as the Name field. |
| Step 9 | Click Save . The
                                                			 newly defined NIC is saved in the database. A Physical Controller ID is assigned, and the To Be
                                                   				Inserted icon is removed from the tree window. |

| Field | Description |
|---|---|
| Name | An
                                                            					 enterprise name that serves as the NIC name. |
| Client
                                                            					 Type | Select INCRP . |

| Option | Description |
|---|---|
| Name | An
                                                            					 enterprise name that serves as the Routing Client name. |
| Configuration Parameters | /customerID
                                                               						<RCID> where <RCID> is the Routing Client ID of the
                                                            					 matching routing client on the Contact Director. |
| Network Routing Client | The same value as the Name field. |

| Step 1 | In the Configuration Manager , select Enterprise > System
                                                      				  Information > System
                                                      				  Information . The System
                                                   				Information dialog appears. |
|---|---|
| Step 2 | In the Application Gateway section, select Remote
                                                   				ICM . |
| Step 3 | Use the other
                                                			 tabs to set the default values for the Unified ICM Application Gateway
                                                			 connections. Take account of the Contact Director NIC settings for timeout,
                                                			 late, and so on as you set the Unified ICM Application Gateway timeout settings
                                                			 for a target Unified CCE system. |
| Step 4 | Click OK and close the dialog. |

| Note | The Unified CCE Reference Designs specify that you use Unified CVP. In a non-Reference Design deployment, you can alternately
                                             use Unified IP IVR or a third-party VRU. |
|---|---|

| Task | See this Topic |
|---|---|
| Set up the contact sharing node on the Contact Director. | Set Up a Contact Sharing Node |
| Set up the machine inventory for the contact sharing node. | Set up Contact Sharing Machine Inventory |
| Add contact sharing rules. | Add and Maintain Rules |
| Add contact sharing groups. | Add and Maintain Groups |

| Note | Your solution can only have one contact sharing node. |
|---|---|

| Step 1 | In the
                                          			 Configuration Manager, select Tools > List
                                                				  Tools > Application Gateway List . The Application Gateway List window appears. |
|---|---|
| Step 2 | To enable Add , click Retrieve . |
| Step 3 | Click Add . The Attributes tab appears. |
| Step 4 | Fill out the Attributes tab as follows: Option Description Name Name of
                                                      					 your contact sharing node Type Contact
                                                      					 Share Note The
                                                      				remaining fields are preset and cannot be modified. | Option | Description | Name | Name of
                                                      					 your contact sharing node | Type | Contact
                                                      					 Share | Note | The
                                                      				remaining fields are preset and cannot be modified. |
| Option | Description |
| Name | Name of
                                                      					 your contact sharing node |
| Type | Contact
                                                      					 Share |
| Note | The
                                                      				remaining fields are preset and cannot be modified. |
| Step 5 | On the Connection Side A tab, set the Address field to the router's IP address. The
                                          			 default port is 5070. |
| Step 6 | On the Connection Side B tab, set the Address field to the router's IP address. The
                                          			 default port is 5070. |
| Step 7 | Click Save to create the contact sharing node. |

| Option | Description |
|---|---|
| Name | Name of
                                                      					 your contact sharing node |
| Type | Contact
                                                      					 Share |

| Note | The
                                                      				remaining fields are preset and cannot be modified. |
|---|---|

| Step 1 | Open your
                                          			 machine inventory file for contact sharing, by default csMachineInventory.csv . |
|---|---|
| Step 2 | Follow the
                                          			 instructions for editing the csMachineInventory.csv file. The instructions are
                                          			 contained within the file. |
| Step 3 | Run the
                                          			 following command: csMachineInventory.bat [options] username password inputfile options:
                                                					 /list, /help, /config /list -
                                                					 This option lists the contact sharing machine inventory. /help -
                                                					 This option displays the usage of the tool. /config -
                                                					 This option configures the contact sharing machine inventory based on the input
                                                					 file. username Username
                                                					 for the REST API request password Password
                                                					 for the REST API request. inputfile Machine
                                                   						inventory file, including the path, for contact sharing, by default csMachineInventory.csv |

| Note | Contact Sharing
                                             			 comes with a default rule that cannot be deleted or modified. The name of this
                                             			 rule is DefaultRule . |
|---|---|

| Step 1 | Navigate to CCE Web Administration > Feature > Contact Share Rules . |
|---|---|
| Step 2 | Click New to open the New
                                             				Rule window, or click an existing rule to open the Edit
                                             				Rule window. |
| Step 3 | Complete the
                                          			 following fields: Field Required Description Name Yes Enter a name using up to 32 alphanumeric characters, periods
                                                         							 (.), and underscores (_). The name must start with an alphanumeric character. Expression Yes Enter a formula that the Contact Share server uses to select the skill group or
                                                         							 precision queue from a Contact Sharing group for a routing request. Description No Enter up to 255 characters to describe the rule. | Field | Required | Description | Name | Yes | Enter a name using up to 32 alphanumeric characters, periods
                                                         							 (.), and underscores (_). The name must start with an alphanumeric character. | Expression | Yes | Enter a formula that the Contact Share server uses to select the skill group or
                                                         							 precision queue from a Contact Sharing group for a routing request. | Description | No | Enter up to 255 characters to describe the rule. |
| Field | Required | Description |
| Name | Yes | Enter a name using up to 32 alphanumeric characters, periods
                                                         							 (.), and underscores (_). The name must start with an alphanumeric character. |
| Expression | Yes | Enter a formula that the Contact Share server uses to select the skill group or
                                                         							 precision queue from a Contact Sharing group for a routing request. |
| Description | No | Enter up to 255 characters to describe the rule. |
| Step 4 | Click Save to return to the List window. |
| Step 5 | To delete a
                                          			 rule, do one of the following: To delete a single rule,
                                             				hover over the row for that rule and click the trash can icon at the end of the row. To delete up to 50 rules,
                                             				check the check box for each rule that you want to delete. To select all rules
                                             				in a list, check the Select All check box in the list header. Click Delete . Deleting a
                                             				rule is permanent. |

| Field | Required | Description |
|---|---|---|
| Name | Yes | Enter a name using up to 32 alphanumeric characters, periods
                                                         							 (.), and underscores (_). The name must start with an alphanumeric character. |
| Expression | Yes | Enter a formula that the Contact Share server uses to select the skill group or
                                                         							 precision queue from a Contact Sharing group for a routing request. |
| Description | No | Enter up to 255 characters to describe the rule. |

| Step 1 | Navigate to Unified CCE Administration > Feature > Contact Share Rules . |
|---|---|
| Step 2 | Either: Click the rule you want to
                                                				copy, and then click the Copy button in the Edit
                                                   				  Rule window. Hover over the row for that
                                                				rule, and click the copy icon that appears at the end of the row. The New
                                                				Rule window opens. |
| Step 3 | Enter a Name for the rule, using up to 32 alphanumeric
                                             			 characters, periods (.), and underscores (_). The name must start with an
                                             			 alphanumeric character. |
| Step 4 | Review Description and Expression fields that were copied from the original
                                             			 rule, and make any necessary changes. |
| Step 5 | Click Save . |

| Step 1 | Navigate to CCE Web Administration > Feature > Contact Share Groups . |
|---|---|
| Step 2 | Click New to open the New
                                             				Group window, or click an existing group to open the Edit
                                             				Group window. |
| Step 3 | Complete the
                                          			 following fields: Field Required Description Name Yes Enter a name using up to 32 alphanumeric characters, periods
                                                         							 (.), and underscores (_). The name must start with an alphanumeric character. Description No Enter up to 255 characters to describe the group. Rule Yes Select a rule that defines the logic for selecting a skill group
                                                         							 or precision queue in this group for a routing request: Click the magnifying glass icon to display the Select Rule window. Click the row to select a rule. Accept Queue If No Enter a logical expression to determine if the individual skill
                                                         							 groups and precision queues in the group can be included in the routing
                                                         							 decision. | Field | Required | Description | Name | Yes | Enter a name using up to 32 alphanumeric characters, periods
                                                         							 (.), and underscores (_). The name must start with an alphanumeric character. | Description | No | Enter up to 255 characters to describe the group. | Rule | Yes | Select a rule that defines the logic for selecting a skill group
                                                         							 or precision queue in this group for a routing request: Click the magnifying glass icon to display the Select Rule window. Click the row to select a rule. | Accept Queue If | No | Enter a logical expression to determine if the individual skill
                                                         							 groups and precision queues in the group can be included in the routing
                                                         							 decision. |
| Field | Required | Description |
| Name | Yes | Enter a name using up to 32 alphanumeric characters, periods
                                                         							 (.), and underscores (_). The name must start with an alphanumeric character. |
| Description | No | Enter up to 255 characters to describe the group. |
| Rule | Yes | Select a rule that defines the logic for selecting a skill group
                                                         							 or precision queue in this group for a routing request: Click the magnifying glass icon to display the Select Rule window. Click the row to select a rule. |
| Accept Queue If | No | Enter a logical expression to determine if the individual skill
                                                         							 groups and precision queues in the group can be included in the routing
                                                         							 decision. |
| Step 4 | Complete the
                                          			 Queues tab: This tab shows
                                             				the list of queues for this group. Click Add to open Add
                                                   					 Queues . Click the
                                                				  queues you want to add to this group. The queues you chose appear on the List of Queues . Close Add Queues . Click Save on this tab to return to the List window. Note The maximum number of queues is 100. | Note | The maximum number of queues is 100. |
| Note | The maximum number of queues is 100. |
| Step 5 | To delete a
                                          			 group, do one of the following: To delete a single group, hover over the row for that group and click the trash can icon at the end of the row. To select all groups in a list, check the Select All check box in the list header. Click Delete . Deleting a
                                             				group is permanent. |

| Field | Required | Description |
|---|---|---|
| Name | Yes | Enter a name using up to 32 alphanumeric characters, periods
                                                         							 (.), and underscores (_). The name must start with an alphanumeric character. |
| Description | No | Enter up to 255 characters to describe the group. |
| Rule | Yes | Select a rule that defines the logic for selecting a skill group
                                                         							 or precision queue in this group for a routing request: Click the magnifying glass icon to display the Select Rule window. Click the row to select a rule. |
| Accept Queue If | No | Enter a logical expression to determine if the individual skill
                                                         							 groups and precision queues in the group can be included in the routing
                                                         							 decision. |

| Note | The maximum number of queues is 100. |
|---|---|

| Field | Description |
|---|---|
| Accept Queue If for a group | A logical
                                             					 expression to determine whether to include the individual skill groups or
                                             					 precision queues in the Contact Sharing group in the routing decision. The
                                             					 field is a freeform editor with a maximum length of 512 characters. 
                                             				  Any result except zero evaluates as TRUE. There is an implicit Accept Queue If of Queue.*.LoggedOn > 0 . You cannot override this implicit check. |
| Expression for
                                             					 a rule | A formula
                                             					 that the Contact Share server uses to calculate the value to be considered
                                             					 against other queues in a Contact Sharing group. The expression always selects
                                             					 the queue with the minimum value. The field is a freeform editor with a maximum
                                             					 length of 512 characters. |

| Note | The default rule is only an example.  Customize the rule to match your needs or write your own rules. |
|---|---|

| Type of
                                                						Operation | Operator | Description |
|---|---|---|
| Conditional | && | Conditional-AND |
| \|\| | Conditional-OR |
| ? : | Ternary
                                                						(shorthand for if-then-else statement) ex. A ? B : C If A,
                                                						then B, otherwise C. |
| Relational | == | Equal to |
| != | Not
                                                						equal to |
| > | Greater
                                                						than |
| >= | Greater
                                                						than or equal to |
| < | Less
                                                						than |
| <= | Less
                                                						than or equal to |
| Bitwise
                                                						and Bit Shift | ~ | Unary
                                                						bitwise complement |
| << | Signed
                                                						left shift |
| >> | Signed
                                                						right shift |
| & | Bitwise
                                                						AND, for strings, also used for string concatenation |
| ^ | Bitwise
                                                						exclusive OR |
| \| | Bitwise
                                                						inclusive OR |
| Arithmetic | + | Addition |
| - | Subtraction |
| * | Multiplication |
| / | Division |
| % | Percentage |
| Prefix | + | Unary
                                                						plus operator; indicates positive value |
| - | Unary
                                                						minus operator; negates an expression |
| ! | Logical complement operator; inverts the value of a boolean |
| Wildcard | * | Wildcard support similar to the expression used in router. For
                                                						example, in SkillGroup.*.Ready , the actual target replaces the
                                                						asterisk when applying the expression. |

| Field Name | Description |
|---|---|
| ApplicationAvailable | The number of agents belonging to this Queue who are
                                                						currently ApplicationAvailable for the MRD to which the Queue belongs. An agent
                                                						is Application available if the agent is Not Routable and Available for the
                                                						MRD. |
| Avail | The extrapolated number of agents in the READY state for
                                                						this Queue. The extrapolation is as follows: (The number of agents that Live Data reports in READY state)
                                                						- XAvail If the extrapolation results in a negative number, Contact
                                                						Sharing sets this field to zero. |
| AvailTimeToInterval | Total seconds agents in the Queue have been in the READY
                                                						state during the current interval. |
| AvgHandledCallsTimeToInterval | Average handle time in seconds for calls counted as handled
                                                						by the Queue during the interval. |
| BusyOther | Number of agents currently in the BusyOther state for this
                                                						Queue. |
| CallsHandledToInterval | Calls that by been answered and have completed wrap-up by
                                                						the Queue during the interval. |
| Hold | The number of agents that have all active calls on hold. |
| ICMAvailable | The number of agents belonging to this Queue who are
                                                						currently ICMAvailable for the MRD to which the Queue belongs. An agent is ICM
                                                						available if the agent is Routable and Available for the MRD. |
| LoggedOn | Number of agents that are currently logged on to the Queue. |
| LoggedOnTimeToInterval | Total time, in seconds, agents were logged on to the Queue
                                                						during the current interval. |
| NotReady | Number of agents in the Not Ready state for the Queue. |
| NotReadyTimeToInterval | Total seconds agents in the Queue have been in the Not Ready
                                                						state during the interval. |
| QueuedNow | The extrapolated number of calls currently queued to this
                                                						Queue. The extrapolation is as follows: (The number of calls that Live Data reports queued to the
                                                						Queue) + XQueuedNow |
| Ready | The number of agents who are Routable for the MRD associated
                                                						with this Queue, and whose state for this Queue is not currently NOT_READY or
                                                						WORK_NOT_READY. |
| ReseveredAgents | The number of agents for the Queue currently in the Reserved
                                                						state. |
| TalkingAutoOut | The number of agents in the Queue currently talking on
                                                						AutoOut (predictive) calls. |
| TalkingIn | The number of agents in the Queue currently talking on
                                                						inbound calls. |
| TalkingOther | The number of agents in the Queue currently talking on
                                                						internal calls, rather than inbound or outbound calls. Examples of other calls
                                                						include agent-to-agent transfers and supervisor calls. |
| TalkingOut | The number of agents in the Queue currently talking on
                                                						outbound calls. |
| TalkingPreview | The number of agents in the Queue currently talking on
                                                						outbound Preview calls. |
| TalkingReserve | The number of agents in the Queue currently talking on agent
                                                						reservation calls. |
| WorkNotReady | The number of agents in the Queue in the Work Not Ready
                                                						state. |
| WorkReady | The number of agents in the Queue in the Work Ready state. |
| XAvail | The number of Contact Sharing requests assigned to the
                                                						available agent count for this Queue during the extrapolation period. The
                                                						extrapolation period defaults to 10 seconds. Contact Sharing request increments this field when QueuedNow
                                                						= 0 and Avail > 0. |
| XQueuedNow | The number of Contact Sharing requests assigned to the
                                                						queued call count for this Queue during the extrapolation period. The
                                                						extrapolation period defaults to 10 seconds. Contact Sharing request increments this field when one of
                                                						the following conditions apply: QueuedNow = 0 and Avail = 0 QueuedNow > 0 and Avail = 0 QueuedNow > 0 and Avail > 0 |

| Call Variable Name | Description |
|---|---|
| CallerEnteredDigits | Digits caller entered in response to prompts. |
| CallingLineID | Billing phone number of the caller. (Commonly referred to as
                                                						CLID). |
| CustomerProvidedDigits | Digits to be passed to the call recipient. |
| DialedNumberString | Phone number dialed by the caller. |
| PeripheralVariable1 through 10 | Value passed to and from the peripheral. |
| RouterCallDay | An encoded value that indicates the date on which the
                                                						software processes the call. |
| RouterCallKey | A value that is unique among all calls the software has
                                                						processed since midnight. RouterCallDay and RouterCallKey combine to form a
                                                						unique call identifier. |
| RoutingClient | Name of the routing client making the route request. |

| Status Variable | Description |
|---|---|
| CS_NOT_CONNECTED (2) | No connection to the contact share process. |
| CS_TIMED_OUT (3) | Request to the contact share process failed. |
| CS_CONFIG_ERROR (4) | Contact share process encountered a configuration related
                                          					 error. |
| CS_EXECUTION_ERROR (5) | Contact share process encountered an expression execution
                                          					 related error. |
| CS_APPGTW_ERROR (8) | Unable to lookup the application gateway with the code that
                                          					 the contact share process returned. |
| CS_UNKNOWN_ERROR (9) | Contact sharing encountered an unknown error. |

| Status Variable | Description |
|---|---|
| ERROR_CONTACT_SHARE_GROUP_NOT_FOUND (1) | The Contact Share Group with the listed ID was not found. |
| ERROR_CONTACT_SHARE_RULE_NOT_FOUND (2) | The Contact Share Rule with the listed ID was not found. |
| ERROR_CONTACT_SHARE_RULE_EXPRESSION_INVALID (3) | The Contact Share Rule has an invalid rule expression. |
| ERROR_CONTACT_SHARE_GROUP_CONSIDERIF_EXPRESSION_INVALID (4) | The Contact Share Rule has an invalid AcceptQueueIf expression. |
| ERROR_CONTACT_SHARE_GROUP_NO_QUEUE_CONFIGURED (5) | There are no queues configured for the Contact Share Group. |
| ERROR_CONTACT_SHARE_ROUTING_EXCEPTION (6) | The route request failed for an unspecified reason. |
| ERROR_CONTACT_SHARE_ROUTING_NO_ELIGIBLE_TARGET (7) | No eligible queue was found for the route request. |
| ERROR_CONTACT_SHARE_ROUTING_TARGET_CONGESTED (8) | No eligible queue was found for the route request because of congestion control. |

| Tip | If you see all calls routing to one target system, check the IP Addresses in the machine inventory table and your script.
                                                   The relationship between the Application Gateway ID and the IP Addresses might be wrong. |
|---|---|