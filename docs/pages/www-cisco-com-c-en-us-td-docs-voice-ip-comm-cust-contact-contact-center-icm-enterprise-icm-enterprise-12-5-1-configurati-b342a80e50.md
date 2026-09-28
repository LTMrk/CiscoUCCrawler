---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-icm-enterprise-icm-enterprise-12-5-1-configurati-b342a80e50
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/icm_enterprise/icm_enterprise_12_5_1/configuration/guide/ucce_b_1251-configuration-guide-unified-cce/ucce_b_1251-configuration-guide-unified-cce_chapter_010.html
retrieved_at: 2026-08-16T14:50:55.344249+00:00
---

Configuration Guide for Cisco Unified ICM/Contact Center Enterprise, Release 12.5(1)

# Configuration Guide for Cisco Unified ICM/Contact Center Enterprise, Release 12.5(1)

Updated: February 5, 2020

Chapter: Routing a Call

## Chapter: Routing a Call

# Routing a Call

## Properly Route Calls

To properly route calls, three independent systems must work together:

The routing client

The system software

The peripheral that ultimately receives the call

The routing client requests a route from the system software,
                              		  receives a response, and delivers the call to the specified destination.

The system software receives a  routing request and determines the
                              		  appropriate destination for the call. The destination is an announcement (which
                              		  is played by the routing client), a scheduled target, or a specific target at a
                              		  peripheral (represented by a trunk group and dialed number identification service [DNIS]).

A peripheral is a switch at a call center, such as an ACD, a PBX,
                              		  or Unified Communications Manager (Unified CM) . The peripheral completes the routing by
                              		  dispatching the call to the specific target determined by the system software.

## Route a Call

The process of routing a call consists of the following steps:

A routing client requests a route from the system software.

The system software, using information supplied by the routing
                                    			 client, categorizes the request as a specific call type.

The system software runs a routing script scheduled for the call type to find a destination for the call. The destination
                                    can be a routing label, an announcement, or a skill target: a service, skill group, or agent. (If the script fails to find
                                    a destination, the system software uses a default destination based on the dialed number.)

A routing label is a character string value that the routing
                                    				client maps to a destination trunk group and, optionally, a DNIS value for the call.

The system software passes the routing label back to the routing
                                    			 client.

The routing client interprets the label to find the destination.

The routing client dispatches the call to the destination (with
                                    			 the appropriate DNIS value, if any).

The call is sent to a peripheral; the peripheral must determine the
                                    			 specific target for which the call is intended.

The peripheral typically makes this determination based on the
                                    				trunk group on which the call arrived and, optionally, the DNIS value sent with
                                    				the call. The peripheral then completes the routing by dispatching the call
                                    				appropriately.

The following sections describe the process in detail.

## Routing a
                        	 Call

Understanding the
                           		call-routing process helps you set up the configuration of your system software
                           		and create effective scripts.

## Routing Requests

The system software receives routing requests from routing clients,
                              		  where the type is either the specific IXC (for example, AT&T or MCI) or the specific type of the peripheral (for example,
                              voice response unit (VRU) or a specific
                              		  type of ACD).

Routing clients send messages to the system software. One type of
                              		  message is a route request . In this case, given a call, the routing client asks
                              		  the system software for a destination, or route, for that call. If the routing
                              		  client is an IXC, this is the only type of message that it sends.

Routing requests are of two types: pre-routing and post-routing . A Pre-Routing request is sent by an IXC to
                              		  determine the initial destination for a call. A Post-Routing request is sent by
                              		  the peripheral that receives the call to either refine the original route or redirect the call.

A routing request includes the following information about the call to
                              		  be routed:

Dialed Number (DN) . The number the caller dialed.

Calling Line ID (CLID) . The billing telephone
                                    				number for the caller. This value is also referred to as Automatic Number Identification (ANI).

Caller-Entered Digits (CED) . Digits the caller entered on a
                                    				touch-tone phone in response to prompts.

Post-Routing messages vary depending on the type of the peripheral.

## Targets

A target is the destination for a call. The target can be a label, an announcement defined by the routing client, or a target
                              at a peripheral.

A target at the peripheral is a service, skill group, or individual agent that the system software selects to handle the call.
                              This is called the skill target . Regardless of the specific skill target, every call routed by the system software must also be associated with a service.
                              The combination of a skill target and a service is a route .

A target represents a network trunk group at the peripheral and, optionally, a DNIS value. The routing client uses this type
                              of target, called a peripheral target , to route the call. Each peripheral target or announcement maps to a routing label.

The following figure shows the relationships among skill targets, routes, peripheral targets, announcements, and labels.

The system software works from top to bottom in the preceding figure:

A routing script determines a destination for the call.

The destination is a routing label that the system software can return directly to the routing client.

Otherwise, the destination is one of the following:

A skill target to receive the call

An announcement to be played

A scheduled target to receive the call

If the destination is a skill target, that skill target has an associated route.

The system software uses the route to find an associated peripheral target supported by the routing client.

The peripheral target is associated with a label. The system software returns that label to the routing client. If the destination
                                    is an announcement, the system software needs only to find the label associated with that announcement and return the label
                                    to the routing client.

The routing client processing depends on the type of the label. Some labels instruct the routing client to take a special
                                    action: playing a busy signal for the caller, playing an unanswered ring for the caller, or making a special query.

For normal labels, the routing client converts the label to an announcement, scheduled target, or peripheral target by working
                                    up from the bottom of the above figure.

The routing client receives a label from the system software in response to its route request. It translates that label into
                                    one of the following:

A peripheral target

An announcement

A scheduled target

An unrouted task that gets routed to a local agent

The result is an announcement, which plays the announcement for the caller. The result is a scheduled target, which delivers
                                    the call to that target.

The routing client delivers the call to the specified network trunk group at the peripheral and sends the specified DNIS value, if any, with it.

The peripheral itself must then recognize the network trunk group and DNIS for the call as it arrives and determine the associated
                                    service and skill target. The peripheral then completes the process by locating the appropriate agent to handle the call.

### System Processing

The following figure summarizes how the system software processes a
                              		route request.

The following subsections describe this processing.

#### Determine Call
                              	 Type

When the system
                                 		software receives a route request for a call, it first determines the call type
                                 		of the call. A call type is a
                                 		category of incoming Unified Intelligent Call
                                    		  Management (Unified ICM) routable tasks. Each call type has a
                                 		schedule that determines which routing script or scripts are active for that
                                 		call type at any time.

There are two classes
                                 		of call types:

Voice (phone
                                       			 calls)

Non-voice (for
                                       			 example, email and text chat)

Voice call types are
                                 		categorized by the dialed number (DN), the caller-entered digits (CED), and the
                                 		calling line ID (CLID).

Non-voice call types
                                 		are categorized by the Script Type Selector, Application String 1, and
                                 		Application String 2.

In either case, the
                                 		last two categories of the call type are optional. For voice call types, the
                                 		caller-entered digits and the calling line ID are optional, depending on the
                                 		call. For non-voice call types, Application String 1 and Application String 2
                                 		are optional, depending on the application.

While chat sessions
                                 		and blended collaboration are different from email and require call variables,
                                 		the call variables are not part of the call type definition.

For example, you might
                                 		define three call types to correspond to three sales regions within the
                                 		country. You might have a network prompt that lets the caller enter 1 for
                                 		sales, 2 for support, and 3 for information. If a call arrives for the dialed
                                 		number 800.486.0029, with a CLID from the 403 (San Jose region) area code, and
                                 		the caller enters 1 (sales) in response to the prompt, that call is classified
                                 		as Western Sales.

If another call
                                 		arrives with the same dialed number, but with a CLID from the 212 (New York
                                 		City) area code, and the caller-entered digit 1, that call is classified as
                                 		Eastern Sales.

You can define a
                                 		general default call type and a specific default call type for each routing
                                 		client. If the call qualifiers do not map to a specific call type, the system
                                 		software uses a default call type defined for the routing client. If no default
                                 		call type is defined for the routing client, the system software uses the
                                 		general default call type.

#### Run Script

Each call type has specific routing scripts scheduled for different times of day and different days of the year. The system
                                 software finds the script currently scheduled for the call type and runs it. If that script fails to find a suitable destination
                                 (that is, a label, announcement, or skill target) for the call, the system software uses a default target associated with
                                 the DN value.

If the system software
                                 		finds an announcement or scheduled target for the call, it can immediately
                                 		resolve that to a label to return to the routing client. If the system software
                                 		finds a skill target for the call, it must perform a few extra steps before it
                                 		finds a label.

#### Determine
                              	 Route

If the system software
                                 		finds a skill target for the call, that target has an associated route. You
                                 		specify the route when you set up the target within the routing script. A route
                                 		represents the combination of a skill target and a service. That is, a route
                                 		represents the destination for a call and the type of service to be provided to
                                 		the caller. Every call routed to a peripheral must have an associated service.

For example, the skill
                                 		target for a call might be the skill group Denver.PostSales and the associated service might be Denver.TechSupport . Another call might also be routed to the Denver.PostSales group with the associated service Denver.Upgrades .

#### Determine Trunk
                              	 Group and DNIS

After it has
                                 		determined a route for a call, the system software finds an associated
                                 		peripheral target (trunk group and DNIS). It is possible to have several
                                 		peripheral targets associated with the same route, but typically only one of
                                 		those targets is valid for the routing client. For example, if you have
                                 		switched access lines, two IXCs could direct calls to the same trunk group and
                                 		DNIS, but each requires a different label value for that target. Therefore, you
                                 		need to define two separate peripheral targets for the route. If more than one
                                 		peripheral target is associated with the route, the system software chooses the
                                 		first peripheral target that maps to a valid label for the routing client.

#### Determine
                              	 Label

Each peripheral
                                 		target, scheduled target, or announcement maps to one or more labels. The
                                 		system software finds the first label that is valid for the routing client and
                                 		dialed number and returns that label to the routing client. It is then up to
                                 		the routing client to interpret the label.

##### Default
                                    		  Label

It is possible that the system software may fail to find a call type for a route request. Also, the system software may run
                                    the script currently scheduled for a call type and fail to find a destination for the call. In these cases, it uses a default
                                    label that is defined for the dialed number. If no default label is defined for the dialed number, the system software returns
                                    an error to the routing client.

The routing client
                                    		  itself also has some default action defined. When you set up each routing
                                    		  client, you can specify the maximum time that client can wait for a response to
                                    		  a routing request. It may happen that the system software has not returned a destination for
                                    		  the call before the time limit is reached. Also the system software may return an
                                    		  error. In both these scenarios, the routing client performs its own default action.

### Routing Client

The routing client begins by requesting a route for a call from the
                                 		  system software. The system software processes the request as described in the
                                 		  preceding section and returns a label to the routing client.

The routing client has its own internal mappings for labels to
                                 		  announcements, scheduled targets, and peripheral targets.

It uses these mappings to interpret the label from the system
                                 		  software:

Busy . Routing client plays a busy signal for the caller.

Ring . Routing client plays an unanswered ring for the
                                       				caller.

Normal and the label maps to an announcement . Routing client plays the announcement for the
                                       				caller.

Normal and the label maps to a scheduled target . Routing client delivers the call to that
                                       				target.

Normal or DNIS Override and the label maps to a peripheral target (that is, a trunk group and a DNIS).
                                       				Routing client delivers the call and the specified DNIS value to that trunk
                                       				group. The peripheral then has responsibility for dispatching the call to the
                                       				appropriate skill target.

### Peripheral Processing

When a peripheral receives a call, it determines the trunk group on
                                 		  which the call arrived and the DNIS value, if any, associated with it. The
                                 		  peripheral must be programmed to map these values to the same service and skill
                                 		  target determined by the system software.

The peripheral, acting as a routing client, can also send a routing
                                 		  request to the system software.

## Translation Routes

Translation routes allow you to send additional information to a skill target along with the call..

A translation route is a temporary destination for a call. When the
                              		  system software returns a translation route label to the routing client, it
                              		  also sends a message directly to the peripheral gateway (PG) at the targeted
                              		  peripheral. This message alerts the PG that a call will be arriving that
                              		  requires route translation.

The message contains the following information:

The trunk group on which the call will arrive and the DNIS value
                                    				associated with it.

A label to be used by the PG to determine the ultimate skill
                                    				target of the call. This is a label that the PG can interpret to find the
                                    				correct destination.

Instructions for further processing to be performed by the PG.
                                    				This further processing might include, for example, looking up an account
                                    				number in a database.

When the peripheral sees the call arrive on the specified trunk group
                              		  and with the specified DNIS value, it passes this information to the PG. The PG
                              		  then combines it with the information it has received from the system software.
                              		  It then sends the call along with this information to the skill target
                              		  specified by the label it received. At the same time, the peripheral might, for
                              		  example, send a message to a host computer that controls the display on the
                              		  agent's workstation. This allows data, such as the caller's account
                              		  information, to be displayed on the screen when the call arrives. The PG
                              		  coordinates communication among the network, the peripheral, and the computer
                              		  application that controls the display.

To set up translation routing, you must do the following:

Set up a translation route associated with the peripheral. You do
                                    				not need a separate translation route for each possible skill target at the
                                    				site, but you need at least one for each peripheral that performs translation
                                    				routing.

Set up one or more routes and associated peripheral targets for
                                    				the translation route. Typically, all peripheral targets for a translation
                                    				route refer to the same trunk group, but with different DNIS values.

Set up a label for the original routing client for the call to
                                    				access each of the peripheral targets associated with the translation route.
                                    				For example, if the routing client is an IXC, you must
                                    				set up a label to the targets with the IXC. This allows the call to be
                                    				initially sent to the translation route at the peripheral.

For each peripheral target that you want to be able to ultimately
                                    				access via a translation route, set a label with the peripheral as the routing
                                    				client. For example, you might want to be able to send calls to the Atlanta
                                    				Support skill group through a translation route. To do this, you must configure
                                    				a label for that skill group with the Atlanta peripheral as the routing client.
                                    				This allows the peripheral to determine the ultimate destination for the call.

To display data on the agent's workstation when the call arrives,
                                    				you must configure the peripheral to inform the PG which agent is receiving the
                                    				call.

## Timeouts and Thresholds

In setting up your configuration, you need to specify several timeout
                              		  and timing threshold values.

For routing clients, you must specify the maximum time the system
                              		  software can spend before responding to each routing request. You must also
                              		  specify the maximum time for the routing client to wait for a response before
                              		  it stops sending new requests to the system software.

For each service at a peripheral, you must specify your goal for the
                              		  maximum time a caller must wait before the call is answered. The system
                              		  software uses this value in calculating the service level.

You can specify how to count abandoned calls in the service level
                              		  calculation. You can also specify the minimum time a call must be in the queue
                              		  before it can be considered abandoned.

For specific information about configuring routing clients,
                              		  peripherals, and services, see Chapters 4 through 7.

### Routing Client Wait Time

In some cases, a routing client might be unable to receive routing
                                 		  responses from the system software. Sometimes this affects only a single
                                 		  request, but other times the routing client loses contact with the system
                                 		  software for longer periods. You can specify the amount of time for the routing
                                 		  client to wait before giving up on a single request and the amount of time to
                                 		  wait before it stops sending any requests to the system software.

#### Timeout
                              	 Threshold

For AT&T
                                 		Intelligent Call Processing (ICP) connections, set the timeout threshold to
                                 		1500 milliseconds.

#### Late
                              	 Threshold

You can specify a
                                 		second threshold, the AT&T Intelligent Call Processing (ICP) connections,
                                 		by setting the late threshold to 500 milliseconds.

#### Timeout
                              	 Limit

The system software is
                                 		designed to be a highly reliable system. Distributed duplicated hardware and
                                 		software fault-tolerance ensure very high availability. However, the NIC uses a
                                 		timeout limit to provide a safety net to ensure that your calls continue to be
                                 		routed even if the system software were to become completely unavailable. If
                                 		the routing client receives no responses from the system software within the
                                 		timeout limit (and a minimum number of requests have been made), it stops
                                 		sending requests to the system software. You can set the minimum number of
                                 		requests that must be made (the consecutive timeout limit) when you set up the
                                 		NIC software. The default is 10.

When a routing request
                                 		first exceeds the timeout threshold, the NIC for the routing client starts a
                                 		timer. If the timer reaches the timeout limit before the routing client
                                 		receives any on-time routing responses from the system software, the NIC tells
                                 		the routing client to stop sending routing requests to the system software. An
                                 		on-time response is a response within the timeout threshold. You can specify
                                 		the timeout limit in seconds. For example, for AT&T ICP connections, set
                                 		the timeout limit to 10 seconds.

### Abandoned Call Wait Time

When a call is delivered to a peripheral, the caller might be placed in a queue waiting for an agent to become available.
                                 Generally, if the caller hangs up before they connect with an agent, the call is considered abandoned. A high number of abandoned
                                 calls might mean that you are losing business because callers are being made to wait too long.

However, if a caller hangs up almost immediately after they are placed in
                                 		  a queue, you might not want to count that as an abandoned call. In these cases,
                                 		  caller impatience or excessive queue times are not the problem; the caller
                                 		  probably hung up for another reason. Tracking these as abandoned calls can be
                                 		  misleading.

Therefore, you can specify a minimum amount of time that a caller must
                                 		  wait before the call can be considered abandoned. This value is called the abandoned call wait time . You can set this value for each
                                 		  peripheral. A typical value might be 10 seconds. This means that if the
                                 		  caller hangs up in the first 10 seconds, the call is not considered abandoned,
                                 		  nor is it counted as a call offered. If the caller waits at least 10 seconds
                                 		  and  hangs up, the call is counted as both offered and abandoned. (In the
                                 		  real-time data, a call is counted as offered as soon as it arrives at the
                                 		  peripheral. Therefore, a short call might appear as a call offered in the
                                 		  real-time data, but is not counted as offered in the historical data.)

### Service Level

Service level is a measure of how well you are meeting your
                                 		  goals for answering calls. For each service, you can set a goal for the maximum
                                 		  time a caller spends in a queue before being connected to an agent. This value
                                 		  is the service level threshold . The service level is usually expressed
                                 		  as the percentage of calls that are answered within the threshold.

To calculate the service level for a period of time, the system
                                 		  software determines the number of calls that have had a service level event
                                 		  within that period.

A service level event occurs when one of three things happens to a
                                 		  call:

It is answered within the service level threshold.

It is abandoned within the service level threshold.

It reaches the service level threshold without being answered or
                                       				abandoned.

All calls that have a service level event within a specified period
                                 		  are considered as service level calls offered for that period. This differs
                                 		  from a simple call's offered value, which counts each call at the time it is
                                 		  first offered to the service.

#### Service Level
                              	 Threshold

The service level
                                    		  threshold is the number of seconds you set as a goal for connecting a call
                                 		with an agent. When you set up a peripheral, you can specify a default service
                                 		level threshold for all services associated with that peripheral. When you set
                                 		up each service, you can choose to either use the default threshold set for the
                                 		peripheral or specify a threshold for the service itself in the Service Level
                                 		Threshold field. If you do not specify a service level threshold for an
                                 		individual service, the default threshold you specified for the peripheral is
                                 		used. Typically, you must set these values to match the service level
                                 		thresholds being used by the peripheral itself.

#### Service Level
                              	 Types

Different peripheral
                                 		types use slightly different formulas to calculate service level. The system
                                 		software provides a uniform calculation across all peripherals. This allows you
                                 		to apply uniform metrics and performance goals across all peripherals. However,
                                 		the system software also tracks the service level as calculated by the
                                 		peripheral itself. This is called the peripheral service
                                    		  level . You can use this value, for example, to continue to compare
                                 		performance to historical norms.

Some peripherals let
                                 		you select one of several types of service level calculation. You can specify
                                 		which of these types of service level you want the system software to track.

The uniform service
                                 		level calculation performed by the system software can be done in any of three
                                 		ways:

Abandoned calls ignored .
                                       			 The number of calls answered within the threshold divided by the number of
                                       			 calls that had a service level event minus the number of calls that were
                                       			 abandoned before exceeding the service level threshold. Calls abandoned before
                                       			 the service level threshold expired are removed from this calculation.

Abandoned calls have a
                                          				negative impact on service level . The number of calls answered within the
                                       			 threshold divided by the number of calls that had a service level event. This
                                       			 treats these abandoned calls as though they had exceeded the threshold.

Abandoned calls have a
                                          				positive impact as service level . The number of calls answered within the
                                       			 threshold plus the number of calls abandoned within the threshold, all divided
                                       			 by the number of calls that had a service level event. This treats these
                                       			 abandoned calls as though they were answered within the threshold.

The following example
                                 		illustrates these different ways of calculating service level.

Example service level calculations

Call Counts

Answered within service level
                                    		  threshold: 70

Abandoned within service
                                    		  level threshold: 10

Exceeded service level
                                    		  threshold: 20

Total service level events:
                                    		  100

Service Level
                                    		  Calculations

Abandoned calls ignored: 70 /
                                    		  (100 - 10) = 77.7%

Abandoned calls negatively
                                    		  impact: 70 / 100 = 70.0%

Abandoned calls positively
                                    		  impact: (70 + 10) / 100 = 80.0%

The value of the
                                 		service level type field for the service determines how the system software
                                 		treats abandoned calls. You set this value when you configure the service.

## Configure Service
                        	 Levels

### Configure Service
                           	 Level for All Call Types

Service levels are
                                 		  set at the System Information level for all call types. To view or change the
                                 		  default system-level settings for all call types:

Step 1

In the
                                          			 Configuration Manager, select Tools > Miscellaneous
                                                				  Tools > System Information .

Step 2

Specify a value
                                          			 for Service level threshold in seconds.

The default is 20
                                                				  seconds .

Step 3

Select the
                                          			 Service level type.

The options are: Abandoned
                                                				  Calls have Negative Impact , Abandoned
                                                				  Calls have Positive Impact , and Ignore
                                                				  Abandoned Calls .

The default is Ignore
                                                				  Abandoned Calls.

Step 4

Click Save .

### Configure Service
                           	 Level for Specific Call Types

To configure service
                                 		  levels for specific call types that override the System Information settings:

Step 1

In the
                                          			 Configuration Manager, select Tools > List
                                                				  Tools > Call Type Lists .

Step 2

Click Retrieve .

Step 3

Select the call
                                          			 type whose service level you want to set.

Step 4

For service
                                          			 level threshold, check the box to the right of the field to override the
                                          			 default from the System Information ( 20 seconds ).

Specify a
                                             				service level threshold value in seconds for this call type.

Step 5

For service
                                          			 level type, check the box to the right of the field to override the default.

Select from Ignore
                                                				  Abandoned Calls , Abandoned
                                                				  Calls have Negative Impact , and Abandoned
                                                				  Calls have Positive Impact .

Step 6

Click Save .

### Configure Service
                           	 Level for MRDs, Peripherals, and Skill Groups

Service level
                                 		  settings for media routing domains (MRDs), peripherals, and skill groups are
                                 		  hierarchical and are interpreted as follows:

MRD - The
                                    			 highest level. It is set in Configuration
                                          				  Manager > Tools > List Tools > Media Routing
                                          				  Domain .

The default
                                       				settings for the MRD are service level threshold = 30 seconds and service level type = Ignore
                                          				  Abandoned Calls . Ignore Abandoned Calls is the only value, and it is
                                       				protected.

Peripheral - Is
                                    			 set in Configuration
                                          				  Manager > Tools > List Tools > Service Level Threshold
                                          				  List .

The default
                                       				settings for a peripheral are taken from its MRD. You can override them.

Skill group - Is
                                    			 set in Configuration
                                          				  Manager > Explorer Tools > Skill Group
                                          				  Explorer > Advanced tab.

Skill group
                                       				default settings are taken from their peripheral. You can override them.

This example
                                 		  explains the configuration.

- The MRD has two
                                       				peripherals. Each peripheral has two skill groups. The service level threshold
                                       				for the MRD is set to the default of 30 seconds, By default, the service level
                                       				thresholds for both peripherals is 30 seconds and the service level thresholds
                                       				for all four skill groups is 30 seconds. Figure 3. MRD
                                             					 Hierarchy Example 1: Service Level Threshold at the MRD

- If you change
                                       				the service level threshold of peripheral 1 to 20 seconds, the service level
                                       				thresholds of skill groups 1 and 2 become 20 seconds. The service level
                                       				thresholds of skill groups 3 and 4 remain at 30 seconds. Figure 4. MRD
                                             					 Hierarchy Example 2: Changing the Peripheral

- If you want the
                                       				service level threshold of skill group 1 to be 45 seconds, you can
                                       				independently configure skill group 1 to have a service level threshold of 45
                                       				seconds. Figure 5. MRD
                                             					 Hierarchy Example 3: Changing the Skill Group

### Configure Service
                           	 Level for the MRD

To configure the
                                 		  service level settings for the MRD:

Step 1

In the
                                          			 Configuration Manager, select Tools > List
                                                				  Tools > Media Routing Domain List .

Step 2

Select the
                                          			 routing domain with the service level you want to modify.

Step 3

Click Retrieve .

Step 4

Select the MRD
                                          			 that has the service level you want to set.

Step 5

Specify a value
                                          			 in seconds for service level threshold. The default is 30 seconds.

Step 6

Service level
                                          			 type is protected and always shows Ignore Abandoned
                                             				Calls .

Step 7

Click Save .

### Configure Service
                           	 Level for a Peripheral

To configure service
                                 		  level settings for a peripheral:

Step 1

In the
                                          			 Configuration Manager, select Tools > List
                                                				  Tools > Service Level Threshold List .

Step 2

Click Retrieve to
                                          			 populate the list with the peripherals.

Step 3

Select the
                                          			 peripheral that has the service level you want to modify.

Step 4

Specify a value
                                          			 for service level threshold. The default is inherited from the MRD.

Your options are
                                             				to:

Retain the
                                                   					 default from the MRD.

Check the
                                                   					 Override MRD default box to unprotect the value and enter a new value in
                                                   					 seconds for the peripheral service level threshold.

Step 5

For Service
                                          			 level type, check the box to override the default. Select from Abandoned Calls
                                             				have Negative Impact , Abandoned Calls
                                             				have Positive Impact , and Ignore Abandoned
                                             				Calls .

For a non–Unified CCE peripheral and a voice MRD, select from Abandoned Calls have Negative Impact , Abandoned Calls have Positive Impact , and Ignore Abandoned Calls . For other MRDs, service level type is protected and always shows Ignore Abandoned Calls.

Step 6

Click Save .

### Configure Service
                           	 Level for Skill Groups

To configure service
                                 		  level settings for a skill group:

Step 1

In the
                                          			 Configuration Manager, select Explorer
                                                				  Tools > Skill Group Explorer .

Step 2

Click Retrieve .

Step 3

Select the skill
                                          			 group and click the Advanced tab.

Step 4

The service
                                          			 level threshold defaults to that of the peripheral.

Your options are
                                             				to:

Keep the
                                                   					 service level threshold setting of the peripheral.

Check the
                                                   					 Override Peripheral default box to unprotect the value and enter a new value in
                                                   					 seconds for the skill group service level threshold.

Step 5

The service
                                          			 level type defaults to that of the peripheral.

Your options are
                                             				to:

Keep the
                                                   					 setting of the peripheral.

From the
                                                   					 drop-down menu, change to: Abandoned
                                                      						Calls have Negative Impact, Abandoned Calls have Positive Impact , or Ignore
                                                      						Abandoned Calls .

Step 6

Click Save .

### Configure Service
                           	 Level for the Precision Queue

To configure
                                 		  service levels for precision queues:

Step 1

Use the
                                          			 Precision Queue gadget to select the precision queues whose service level you
                                          			 want to set.

Step 2

Specify a
                                          			 value for service level threshold.

Step 3

Click Save .

### Configure Service
                           	 Level for an Aspect Call Center PG

To configure service
                                 		  level settings for an Aspect Call Center PG:

Step 1

In the
                                          			 Configuration Manager, select Explorer
                                                				  Tools > PG Explorer .

Step 2

Click Retrieve .

Step 3

Select and
                                          			 expand the PG.

Step 4

Select the
                                          			 peripheral and click the Peripheral tab.

For all
                                             				peripherals except Aspect Call Center, the peripheral service level type field
                                             				is protected and shows Calculated by
                                                				  Call Center .

For Aspect Call
                                             				Center, choose the type of calculation to be performed by default. You can
                                             				override the default for each individual service.

| Note | If the destination
                                          		is itself a service, for example Chicago.Sales ,
                                          		the associated service must also be Chicago.Sales .
                                          		To associate a service skill target with a route for a different service would
                                          		skew the statistics for those services. |
|---|---|

| Step 1 | In the
                                          			 Configuration Manager, select Tools > Miscellaneous
                                                				  Tools > System Information . |
|---|---|
| Step 2 | Specify a value
                                          			 for Service level threshold in seconds. The default is 20
                                                				  seconds . |
| Step 3 | Select the
                                          			 Service level type. The options are: Abandoned
                                                				  Calls have Negative Impact , Abandoned
                                                				  Calls have Positive Impact , and Ignore
                                                				  Abandoned Calls . The default is Ignore
                                                				  Abandoned Calls. |
| Step 4 | Click Save . |

| Step 1 | In the
                                          			 Configuration Manager, select Tools > List
                                                				  Tools > Call Type Lists . |
|---|---|
| Step 2 | Click Retrieve . |
| Step 3 | Select the call
                                          			 type whose service level you want to set. |
| Step 4 | For service
                                          			 level threshold, check the box to the right of the field to override the
                                          			 default from the System Information ( 20 seconds ). Specify a
                                             				service level threshold value in seconds for this call type. |
| Step 5 | For service
                                          			 level type, check the box to the right of the field to override the default. Select from Ignore
                                                				  Abandoned Calls , Abandoned
                                                				  Calls have Negative Impact , and Abandoned
                                                				  Calls have Positive Impact . |
| Step 6 | Click Save . |

| Step 1 | In the
                                          			 Configuration Manager, select Tools > List
                                                				  Tools > Media Routing Domain List . |
|---|---|
| Step 2 | Select the
                                          			 routing domain with the service level you want to modify. |
| Step 3 | Click Retrieve . |
| Step 4 | Select the MRD
                                          			 that has the service level you want to set. |
| Step 5 | Specify a value
                                          			 in seconds for service level threshold. The default is 30 seconds. |
| Step 6 | Service level
                                          			 type is protected and always shows Ignore Abandoned
                                             				Calls . |
| Step 7 | Click Save . |

| Step 1 | In the
                                          			 Configuration Manager, select Tools > List
                                                				  Tools > Service Level Threshold List . |
|---|---|
| Step 2 | Click Retrieve to
                                          			 populate the list with the peripherals. |
| Step 3 | Select the
                                          			 peripheral that has the service level you want to modify. |
| Step 4 | Specify a value
                                          			 for service level threshold. The default is inherited from the MRD. Your options are
                                             				to: Retain the
                                                   					 default from the MRD. Check the
                                                   					 Override MRD default box to unprotect the value and enter a new value in
                                                   					 seconds for the peripheral service level threshold. |
| Step 5 | For Service
                                          			 level type, check the box to override the default. Select from Abandoned Calls
                                             				have Negative Impact , Abandoned Calls
                                             				have Positive Impact , and Ignore Abandoned
                                             				Calls . For a non–Unified CCE peripheral and a voice MRD, select from Abandoned Calls have Negative Impact , Abandoned Calls have Positive Impact , and Ignore Abandoned Calls . For other MRDs, service level type is protected and always shows Ignore Abandoned Calls. |
| Step 6 | Click Save . |

| Step 1 | In the
                                          			 Configuration Manager, select Explorer
                                                				  Tools > Skill Group Explorer . |
|---|---|
| Step 2 | Click Retrieve . |
| Step 3 | Select the skill
                                          			 group and click the Advanced tab. |
| Step 4 | The service
                                          			 level threshold defaults to that of the peripheral. Your options are
                                             				to: Keep the
                                                   					 service level threshold setting of the peripheral. Check the
                                                   					 Override Peripheral default box to unprotect the value and enter a new value in
                                                   					 seconds for the skill group service level threshold. |
| Step 5 | The service
                                          			 level type defaults to that of the peripheral. Your options are
                                             				to: Keep the
                                                   					 setting of the peripheral. From the
                                                   					 drop-down menu, change to: Abandoned
                                                      						Calls have Negative Impact, Abandoned Calls have Positive Impact , or Ignore
                                                      						Abandoned Calls . |
| Step 6 | Click Save . |

| Step 1 | Use the
                                          			 Precision Queue gadget to select the precision queues whose service level you
                                          			 want to set. |
|---|---|
| Step 2 | Specify a
                                          			 value for service level threshold. |
| Step 3 | Click Save . |

| Step 1 | In the
                                          			 Configuration Manager, select Explorer
                                                				  Tools > PG Explorer . |
|---|---|
| Step 2 | Click Retrieve . |
| Step 3 | Select and
                                          			 expand the PG. |
| Step 4 | Select the
                                          			 peripheral and click the Peripheral tab. For all
                                             				peripherals except Aspect Call Center, the peripheral service level type field
                                             				is protected and shows Calculated by
                                                				  Call Center . For Aspect Call
                                             				Center, choose the type of calculation to be performed by default. You can
                                             				override the default for each individual service. |