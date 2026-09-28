---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-icm-enterprise-icm-enterprise-12-6-1-reference-g-0d9eaa4c05
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/icm_enterprise/icm_enterprise_12_6_1/reference/guide/ucce_b_database-schema-handbook_12_6_1/ucce_b_database-schema-handbook_12_6_1_chapter_0100.html
retrieved_at: 2026-08-16T19:27:32.983202+00:00
---

Database Schema Handbook for Cisco Unified ICM/Contact Center Enterprise, Release 12.6(1)

# Database Schema Handbook for Cisco Unified ICM/Contact Center Enterprise, Release 12.6(1)

Updated: May 14, 2021

Chapter: Field Values

## Chapter: Field Values

# Field Values

## Access Levels

Several tables include an AccessLevel field that indicates the rights
                              		  a user or group has to access an object or class.

Access Level Values

Meaning

10

Read

20

Reference

30

Maintenance (create, read, update, delete)

## AgentState

The 
                              		  Agent Real Time, Agent Skill Group Real Time, and Agent state trace tables ( see Agent_Real_Time , Agent_Skill_Group_Real_Time , and Agent_State_Trace )  use the AgentState field,
                              		  which indicates the agent's state.

The meaning for this field varies depending on the table that uses
                                          		  it.

Agent State Values

Meaning (Agent_Real_Time / Agent_Skill_Group_Real_Time)

Meaning (Agent_State_Trace)

0

Logged Off

Logged Off

1

Logged On

Logged On

2

Not Ready

Not Ready

3

Ready

Ready

4

Talking

Talking

5

Work Not Ready

Work Not Ready

6

Work Ready

Work Ready

7

Busy Other

Busy Other

8

Reserved

Reserved

9

Unknown

Call Initiated

10

Calls On Hold

Call Held

11

Active

Active

12

Paused

Paused

13

Interrupted

Interrupted

14

Not Active

Not Active is an agent state when the agent is signed into a nonvoice skill group or precision queue.  This state is the equivalent
                                                      of Ready for voice.

Not Active

The Type field indicates the recurrence pattern of the schedule.

Type Values

Meaning

1

Daily (the DayType field indicates which days of the week)

2

Weekly (the DayType field indicates which days of the week)

3

Biweekly (the DayType field indicates which days of the
                                          						week)

4

Monthly (the Day field specifies the day of month)

5

Monthly (the DayPosition and DayType fields indicate day of
                                          						the month)

6

Yearly (the month and day fields specify the day of year)

7

Yearly (the DayPosition, DayType, and Month specify the day
                                          						of year)

8

Range (the starting and ending date and times specify the
                                          						range)

## Application Gateway: Fault Tolerance

The Fault Tolerance field in the
                              Application Gateway Table (see Application_Gateway ) takes these values:

0 = none

1 = Duplicate Request

Each
                                    router will manage a connection to a different host. Each time a scripts
                                    initiates a request, both routers will ask their corresponding host. Both
                                    routers will believe the response from whichever host responds first. This
                                    method is the most reliable, but has the added expense of requiring two hosts
                                    to interface to. Even if a host (or a connection) fails, all requests will be
                                    satisfied.

2 = Alternate Request

Each router
                                    will manage a connection to a different host. The routers will take turns,
                                    sending half the requests to the host connected to side A, and the other half
                                    to the host connected to side B. If either host fails, the entire load will be
                                    directed to the surviving host. When a host (or connection) fails, some
                                    requests may be lost. This is because by the time the router can figure out
                                    that a host is not going to respond, it is too late to ask the other host and
                                    still route the call within the deadline imposed by the network

3 = Hot Standby

The hot standby method. Each router will
                                    manage a connection to a different host. All requests will be directed to the
                                    designated primary host. If the host (or connection) fails, all requests will
                                    be directed to the backup host. This option may also lose some requests on
                                    failures.

## Client Type

The Client Type
                              		  field in the Peripheral (see Peripheral )
                              		  and in the Routing_Client Table (see Routing_Client )
                              		  takes these values:

1 = Avaya DEFINITY ECS
                                    				(non-EAS)

2 = MCI

3 = Sprint

4 = Aspect

5 = Nortel Meridian

6 = Rockwell Galaxy
                                    				(without priority enhancements) (Not supported)

7 =GTN

8 = Generic NIC

9 = Avaya G2

10 = Rockwell Galaxy (Not
                                    				supported)

11 = Rockwell Spectrum (Not supported)

12 = Avaya DEFINITY ECS
                                    				(EAS)

13 = VRU

14 = British Telecom NIC

15 = VRU Polled

16 = INCRP NIC

17 = Nortel NIC

18 = DMS 100 (Not Supported)

19 = Siemens Hicom 300 E
                                    				(9006) (Not supported)

20 = France Telecom

21 = Stentor NIC (Not
                                    				Supported)

22 = Ameritech

23 = BT INAP NIC

24 = Siemens ROLM 9751
                                    				CBX (9005) (Not supported)

25 = ICR Protocol NIC

26 = Alcatel 4400 (Not
                                    				supported)

27 = NEC NEAX 2x00

28 = ACP 1000

29 = Avaya Aura Contact
                                    				Center (AACC)

30 = Enterprise Agent

31 = Call Routing Service
                                    				Protocol (CRSP)

32 = Ericsson MD110

33 = Wireless INAP NIC

34 = Energis INAP NIC

35 = AUCS INAP NIC

36 = Concert NIC

37 = Deutsche Telecom NIC

38 = CAIN NIC

39 = Telfort INAP NIC

40 = BT V2 NIC

41 = TIM INAP NIC

42 = Generic PG

43 = Reserved

44 = GKTMP NIC
                                    				(Gatekeeper NIC) (Not supported)

45 = SS7IN NIC (SS7 Intelligent Network)

46 = NTL NIC

47 = Media Routing

48 = Non-Voice Agent PIM

49 = UCC Express
                                    				Gateway

50 = UCC Enterprise
                                    				Gateway

51 = System PG

ARS PIM is
                                                   					 deprecated in release 10.0(1).

## Customer Options Type

The Type field in the 
                              		  Customer Options Table (see Customer_Options ) indicates a type of option that
                              		  is enabled or disabled for a customer.

Type Values

Meaning

1

Allow quick-edit of Announcement node

2

Allow quick-edit of Call Type node

3

Allow quick-edit of Caller Entered Digits node

4

Allow quick-edit of Calling Line ID node

5

Allow quick-edit of Dialed Number node

6

Allow quick-edit of Goto Script node

7

Allow quick-edit of Percent Allocation node

8

Allow quick-edit of Requalify node

9

Allow quick-edit of Run VRU Script node

10

Allow quick-edit of Scheduled Select node

11

Allow quick-edit of Switch node

12

Allow quick-edit of Time node

50

Bill for VRU time

51

Customer billing data

## Days

Both the 
                              		  Admin Script Schedule Map Table (see Admin_Script_Schedule_Map ) and the Recurring
                              		  Schedule Map Table use values to indicate the day of the week, day of the
                              		  month, day position, and day type.

Values

Meaning

Day of the Week

0x01 = Sunday

0x02 = Monday

0x04 = Tuesday

0x08 = Wednseday

0x10 = Thursday

0x20 = Friday

0x40 = Saturday

Day of the Month

0 = Applies to every day

1-31 = Specifies the day of month

Day Position

0 = First day of the type in a month

1 = Second day of the type in a month

2 = Third day of the type in a month

3 = Fourth day of the type in a month

4 = Last day of the type in a month

5 = Every day of the type in a month

Day Type

0-6 = Specifies a day (Sunday through Saturday,
                                          						respectively)

7 = Every day

8 = Every weekday

9 = Every weekend day

## Dialed Number Map: ANIWildCardType

The ANIWildCardType field in the 
                              		  Dialed Number Map Table (see Dialed_Number_Map ) indicates how the system
                              		  software should interpret the value given in the ANIWildCard field.

ANIWildCardType Value

Meaning

0

Unknown

1

NPA (3-digit match)

2

NPA-NXX (6-digit match)

3

Match (all digits are match)

4

Region

5

All (match all ANIs)

6

Prefix

## Dialer Detail:
                        	 CallResult

The CallResult field
                              		  in the Dialer Detail (see Dialer_Detail )
                              		  can be populated with the following values:

System
                                          						Type Values

Meaning

2

Error condition while dialing.

3

Number reported not in service by network.

4

No ringback from network when dial attempted.

5

Operator intercept returned from network when dial attempted.

6

No dial tone when dialer port went off hook.

7

Number reported as invalid by the network.

8

Customer phone did not answer.

9

Customer phone was busy.

10

Customer answered and was connected to agent.

11

Fax machine detected.

12

Answering machine detected.

13

Dialer stopped dialing customer due to lack of agents or network stopped dialing before it was complete.

14

Customer requested callback.

15

Answering machine requested callback.

16

Call connected with customer was abandoned by the dialer due to lack of agents.

17

Failed to reserve agent for personal callback.

18

Agent has skipped or rejected a preview call.

19

Agent has skipped or rejected a preview call with the close option.

20

Customer has been abandoned to an IVR.

21

Customer dropped call within configured abandoned time.

22

In Unified CCE, the call
                                          									result indicates an answering machine detection which did not
                                          									meet termination conditions. One such example is a network
                                          									voicemail message indicating a mailbox is full or not setup
                                          									properly. In TDM switches, it indicates a network answering
                                          									machine detection, such as a network voicemail.

23

Number successfully contacted but wrong number. (Not supported).

24

Number successfully contacted but reached the wrong person. (Not supported).

25

Dialer has flushed this record because there is a change in the skillgroup, or a change in the campaign, or there are no agents
                                          available.

26

The number was on the do not call list.

27

Call disconnected by the carrier or the network while ringing.

28

Dead air or low voice volume call.

29

Received message is not supported by voice gateway.

30

Received message is not authorized by voice gateway.

31

Invalid message received by voice gateway.

32

Call cancelled because the dialer lost connection with the Campaign Manager.

33

Agent timed-out accepting preview or personal callback call.

This Call Result is supported from 12.0 ES33 onwards.

## Dialer Detail:
                        	 CallStatusZone

The CallStatusZone1
                              		  and CallStatusZone2 fields in the Dialer Detail (see Dialer_Detail )
                              		  can be populated with the following values that show the current status of the
                              		  customer record for the zone.

The values are:

A = Active.
                                    				Stored in CallStatusZoneX (1 or 2). A zone is set to active when it has been
                                    				sent to a dialer for dialing

B = A callback was requested. Stored in CallStatusZone1 and CallStatusZone2 field when a regular callback (non personal callback)
                                    has been scheduled. The Callback time itself is stored in both the CallbackDateTimeZone1 and CallbackDateTimeZone2 columns
                                    since the callback overrides the individual zones.

C = Closed.
                                    				Record has been closed for that particular zone, so the record will not be
                                    				retried again for that zone.

D=Dialed. Record
                                    				has been dialed for that particular zone.

F= Fax Machine. Stored in CallStatusZoneX (1 or 2).

L = Not
                                    				Allocated. Invalid number used for a Personal Callback.

J = Agent
                                    				rejected (closed out the record).

M = Max Calls.
                                    				The maximum number of attempts has been reached. Stored in both CallStatusZone1
                                    				and CallStatusZone2. A record is set to "M" when it has dialed the maximum
                                    				times as specified in the campaign and will not be retried again. Both zones
                                    				are set to "M" to indicate no further calling in either zone.

P = Pending. Stored in CallStatusZoneX (1 or 2). This is the initial state of a record before any dialing has taken place.
                                    The record remains in the pending state for a particular zone until all of the numbers specified for that zone are dialed.
                                    A pending contact which has already dialed at least once from its sequence will have at least one CallBackDateTime column
                                    filled in with a retry time.

R = Retry.
                                    				Stored in CallStatusZoneX (1 or 2) for the zone where the Retry is scheduled.
                                    				The retry time itself is stored in the CallbackDateTimeZoneX (1 or 2) as well
                                    				as in the individual number column CallbackDateTimeXX, where XX is the number
                                    				to be retried (01 - 10). Call can be retried for a variety of reasons including
                                    				receiving a busy or no answer result, etc.

S = A personal
                                    				callback was requested. Stored in both CallStatusZone1 and CallStatusZone2. A
                                    				record is set to "S" when it has been scheduled for a personal callback. Both
                                    				zones are set to "S" to indicate that it has been moved to the personal
                                    				callback list

U = Unknown.
                                    				Stored in CallStatusZone1 and CallStatusZone2. A record is set to Unknown if
                                    				its status was "A" when the Campaign Manager started. If the Campaign Manager
                                    				shuts down when a record is at a dialer, it no longer knows its status when it
                                    				restarts. Therefore, it will remain in "U" state until the record is returned
                                    				to it.

X = Agent not
                                    				Available. For a personal callback, the agent is not available, and the
                                    				reschedule mode is Abandon. (CallStatusZone1 only)

## Dialer Detail: DialingMode

The DialingMode field in the
                              Dialer Detail (see Dialer_Detail ) can be populated with the following values that show the campaign mode
                              for the call. This field is NULL for Do Not Call entries.

Values are:

1 = Predictive
                                    only

2 = Predictive blended

3 =
                                    Preview only

4 = Preview blended

5
                                    = Progressive only

6 = Progressive blended

7. = Direct preview only

8. = Direct preview
                                    blended

## Event Fields

The SystemType field in the 
                              		  Event (see Event )  indicates the type of system within the
                              		  system software that generated the event.

System Type Values

Meaning

0

Unknown

1

CallRouter

2

Peripheral Gateway (PG)

3

Network Interface Controller (NIC)

4

Administration & DataServer (ADS)

5

Logger

6

Listener

7

CTI Gateway

8

Blended Agent Dialer

## ICR Locks Fields

The LockType field in the 
                              		  ICR Locak Table (see ICR_Locks ) indicates a kind of lock.

Value

Meaning

0

Master lock (applies to configuration data and script.

1

Configuration lock (no longer used)

2

Script Lock(applies to an individual script)

3

Application lock (no longer used)

## LabelType Fields

The LabelType field in the 
                              		  Label Table (see Label )  indicates the type of the routing label.

LabelType Values

Meaning

0

Normal

1

DNIS Override (the system software returns the specific DNIS
                                          						value to be used with the label)

2

Busy (instructs the routing client to play a busy signal to
                                          						caller)

3

Ring (instructs the routing client to play an unanswered
                                          						ring to caller)

4

Post-Query (instructs the routing client to re-enter its
                                          						call processing plan at a specific point)

5

Resource (used internally for special routing client
                                          						resources, such as a network VRU)

## Logical Interface
                        	 Controller Fields

The
                              		  LogicalControllerType field uses a subset of the values for Event.SystemType
                              		  listed in the following table. The ClientType field indicates the type of
                              		  peripheral or routing client associated with the controller:

Value

Meaning

1

Avaya
                                          						DEFINITY ECS, without Expert Agent Selection (EAS)

2

MCI

3

Sprint

4

Aspect
                                          						CallCenter

5

Nortel
                                          						Meridian

6

Rockwell
                                          						Galaxy without priority enhancements (r1.3)

(Not
                                          						supported)

7

AT&T
                                          						GTN

8

Generic
                                          						Network Interface Controller (GenNIC)

9

Avaya G2

10

Rockwell
                                          						Galaxy (Not supported)

11

Rockwell
                                          						Spectrum (Not supported)

12

Avaya
                                          						DEFINITY ECS, with Expert Agent Selection (EAS)

13

Voice
                                          						Response Unit (VRU)

14

British
                                          						Telecom NIC

15

Voice
                                          						Response Unit (VRU), polled

16

INCRP NIC

17

Nortel NIC

18

DMS 100 (Not
                                             						  supported)

19

Siemens
                                          						Hicom 300 E, 9006 (Not supported)

20

France
                                          						Telecom

21

Ameritech

22

BT INAP
                                          						NIC

23

Siemens
                                          						ROLM 9751 CBX, 9005 (Not supported)

24

ICR
                                          						Protocol (ICRP) NIC

25

Alcatel
                                          						4400 (Not supported)

26

NEC NEAX
                                          						2x00

27

ACP 1000

28

AACC.

29

Enterprise Agent

30

Call
                                          						Routing Service Protocol (CRSP) NIC

31

Ericsson
                                          						MD110

32

able
                                          						& Wireless Corp. (CWC) INAP NIC

33

Energis
                                          						INAP NIC

34

AUCS
                                          						INAP NIC

35

Concert
                                          						NIC

36

Deutsche
                                          						Telecom NIC

37

CAIN NIC

38

Telfort
                                          						INAP NIC

39

BT V2
                                          						NIC

40

TIM INAP
                                          						NIC

41

Generic
                                          						PG

42

CeM

## Network Vru
                        	 Type

The Type field in
                              		  the Network Vru Table (see Network_Vru )
                              		  indicates the type of interface the system software uses to communicate with
                              		  the VRU.

Type
                                          						Values

Interface

1

Normal
                                          						label type and a correlation ID.

2

Normal
                                          						label type and a DNIS.

3

Resource
                                          						label type and a correlation ID. The routing client can automatically take back
                                          						the call from the VRU when the system software returns a destination label.

4

Resource
                                          						label type and a DNIS.

5

Resource
                                          						label type and either a correlation ID or a DNIS.

6

No label,
                                          						no correlation ID, and no DNIS (call is already at the VRU).

7

Similar to
                                          						Type 3, but the system software automatically instructs the VRU to release the
                                          						call when it sends a destination label to the routing client.

8

Similar to
                                          						Type 2, but a Type 8 VRU is used when the NAM has a routing client that
                                          						controls the call to the VRU.

9

Queuing
                                          						for Network VRU controlled by the Unified CCE System PG.

10

Simplifies
                                          						configuration requirements in Unified CVP Comprehensive Model deployments.

## Port Status

The values for the Port Status field in the
                              Dialer_Port_Real_Time Table (see Dialer_Port_Real_Time ) are listed below:

290 = port allocated for future dial

300 = port released

310 = reservation call started

320 = agent reserved

330 = customer call started

340 = customer has been contacted

350 = call transferred to agent

360 = customer conversation complete

370 = agent completed with call

## Route Call Detail
                        	 Fields

This section has
                              		  values for three fields in the Route_Call_Detail Table (see Route_Call_Detail ):
                              		  RequestType, OriginatorType, and TargetType.

The RequestType
                                 			 field indicates the type of route request processed.

Value

Meaning

1

Pre- Routing request

2

Blind
                                          						transfer or network VRU

3

Announced
                                          						transfer or MCI 800 call

4

Overflow

5

Re-route

6

Post- Routing request

The OriginatorType
                                 			 field indicates where the route request came from.

Value

Meaning

0

Unknown

1

Trunk

2

Teleset

3

Voice
                                          						Response Unit (VRU)

4

Trunk
                                          						Group

The Route Call Detail Target Type is a numeric value representing the implementation result of the routing script.

Following is a list
                              		  of possible values this field (shown in terms of the value, type, and
                              		  description):

0 = resultNone Call routing ended badly.

1 = resultDefaultRoute Call routing ended using a default route.

2 = resultRouteAgent Call routing ended with a route to an agent.

3 = resultRouteService Call routing ended with a route to a service.

4 = resultRouteGroup Call routing ended with a route to a skill
                                    				group.

5 = resultAnnouncement Call routing ended with an announcement.

6 = resultBusy Call routing ended in a Busy node.

7 = resultRing Call routing ended in a Ring node.

8 = resultNone Call routing ended in a Label node.

9 = resultNetworkDefault Call routing ended in a Termination node using a network
                                    				default route

10 = resultRouteServiceArray Call routing ended with a route to a service array.

11 = resultMultipleLabels Call routing ended badly.

12 = resultScheduledTarget - Call routing ended in a Scheduled
                                    				Target node(busy link functionality).

13 = resultDone Only applicable to an AdminScript that ends with no errors.

14 = resultAborted Call disconnected.

15 = =
                                       				  resultReleaseCall Call routing ended with a Release Call node.

16 = resultQueuedTooLong Call routing exceeded the queue limit.

17 = resultSendAgent Call routing ended with an Agent to Agent node.

18 = resultDynamicLabel Call routing ended with a dynamic label
                                    				node.

19 = resultDivertDynamicLabels Call routing ended with a divert-on-busy dynamic label.

20 = resultQueuedDialogFailure The administrator asked to fail
                                    				queued calls.

21 = resultRouteAgentAndGroup Call routing ended with a route to
                                    				an agent in a specified group.

22 = resultSendPQ Call routing ended with a route to a Precision Queue.

23 = resultPickPullAgent Successful pick or pull request routed to agent.

24 = resultPickPullError Unsuccessful pick or pull request.

## Router Error Codes

The Router sets RouterErrorCode in the RCD when error conditions are detected and increments the Call_Type_Interval.ErrorCount for the current interval.

A Route_Call_Detail.RouterErrorCode value of 448 is treated as an abandoned call and does not increment the Call_Type_Interval.ErrorCount .

References in the guide to DeskLink and Enterprise Agent are specific to resources associated with a Unified CCE Peripheral.

The Router Log Viewer tool provides methods for viewing the System Events that are defined in this guide. Router Log Viewer tool is an ICM Admin Workstation tool that provides a live stream of errors as they are reported by the Router. This may
                           be utilized to capture the error conditions specified in the guide.

The following defines the set of valid values for Router_Call_Detail.RouterErrorCode .

Some internally used error codes are not updated in the RCD.

RouterErrorCode=62

This is generated when the Router received a call route request from routing client with a dialed number that is not configured.

RouterErrorCode=63

This is generated when the Router was unable to find a call type for Specified dialed number, caller entered digits and ANI
                                 in route request.

RouterErrorCode=64

This is generated when there is no script that is scheduled to run at the current time for the identified call type and dialed
                                 number from the route request.

RouterErrorCode=65

This is generated when the script run did not yield a result due to lack route configuration for the dialed number and the
                                 associated call type.

RouterErrorCode=66

This is generated when there is no default label that is configured for dialed number, yet the Router needed one.

RouterErrorCode=67

This is generated when there is no label that is configured for announcement for the dialed number in the Central Controller.

RouterErrorCode=68

This is generated when there is no peripheral target that is configured in the Central Controller for route with routing client.

RouterErrorCode=69

This is generated when there is no valid label that is configured for the peripheral target.

RouterErrorCode=70

This is generated when of an incorrect configuration in the translation route.

RouterErrorCode=71

No peripheral target is available.

RouterErrorCode=123

This is generated when the routes were configured for the translation route.

RouterErrorCode=124

This is generated when the peripheral to which a translation route is directed is not online. The translation route cannot
                                 be completed. The peripheral (ACD) cannot be seen by the ICM. It may be down or the Peripheral Gateway (PG) may not be able
                                 to see the peripheral due to communications problems between the ACD and the PG.

RouterErrorCode=126

This is generated when the specified ACD/IVR is not visible to the Peripheral Gateway. No call or agent state information
                                 is being received by the Router from this site. Routing to this site is impacted.

RouterErrorCode=230

This is generated when a script indicated that a busy label should be returned to routing client for dialed number , but no
                                 such label is configured.

RouterErrorCode=231

This is generated when a script indicated that a ring label should be returned to routing client for dialed number, but no
                                 such label is configured.

RouterErrorCode=232

This is generated when a script indicated that a label should be returned to routing client for dialed number, but no such
                                 label is configured.

RouterErrorCode=257

This is generated when there is no peripheral target available for translation route with routing client.

RouterErrorCode=258

This is generated when there are no labels for the peripheral target and the routing client.

RouterErrorCode=274

This is generated when there are no free routes available to use for the translation route. This is typically caused either
                                 when all the routes are used for translation routing.

RouterErrorCode=433

This is generated when the router could not locate a call associated with this DialogID.

RouterErrorCode=434

This is generated when the router could not locate a valid label for the Network VRU.

RouterErrorCode=435

This is the default error that the system uses when a specific error is not identified.

RouterErrorCode=448

This is generated when the customer disconnects the call at the routing client. This is not a routing error.

RouterErrorCode=485

This is generated when a call (dialed number) from PG routing client claimed to be from a VRU, but the routing client's associated
                                 peripheral had no network VRU configured, so the router was unable to determine which VRU the call was from.

RouterErrorCode=486

This is generated when a call with unknown dialed number from NIC routing client claimed to be from a VRU, but since the dialed
                                 number was unknown, it was not possible to determine which VRU the call was from.

RouterErrorCode=487

This is generated when a call with dialed number from NIC routing client claimed to be from a VRU, but since the customer
                                 was unknown, it was not possible to determine which VRU the call was from.

RouterErrorCode=488

This is generated when a call with dialed number from NIC routing client claimed to be from a VRU, but since the customer
                                 was not configured with a Network VRU (or there is no default NetworkVRU), it was not possible to determine which VRU the
                                 call was from.

RouterErrorCode=490

This is generated when the Routing to DeskLink route fails to find an agent in the SkillGroup node.

RouterErrorCode=491

This is generated when the router attempts to send DeviceTargetPreCallInd to unconnected peripheral. An attempt was made to
                                 route an enterprise agent call to a peripheral not currently on-line to the router.

This probably indicates a configuration inconsistency.

RouterErrorCode=492

This is generated when an attempt was made to route an enterprise agent call to a peripheral not connected with the correct
                                 OPI revision.

This probably indicates a configuration inconsistency.

RouterErrorCode=495

This is generated when the router attempted to send call to agent on peripheral who has no device target. A script attempted
                                 to send an enterprise agent call to an agent who has no device target that is assigned by the peripheral gateway.

RouterErrorCode=499

This is generated when the call on dialed number gets stopped for exceeding the maximum queue time limit. The call was sent
                                 to the default label.

RouterErrorCode=545

This is generated when the Router received a task request from routing client with a dialed number that is configured with
                                 the wrong media routing domain.

RouterErrorCode=547

This is generated when a call was received from routing client with an unknown media routing domain. This probably indicates
                                 a configuration inconsistency.

RouterErrorCode=564

This is generated when of incorrect label configuration for scheduled target in the Cisco Unified Contact Center Enterprise
                                 script.

RouterErrorCode=594

This is generated when there is no label available for the peripheral target and the routing client.

RouterErrorCode=595

This is generated when no peripheral targets for route have valid labels for every routing client that is targeted by translation
                                 route.

## Object Types:
                        	 Security

Several tables
                              		  related to security include an ObjectType field that indicates the type of
                              		  object to which security is applied.

Object
                                          						Type Values

Meaning

2000

Dialed
                                          						Number

2001

Call Type

2002

Peripheral

2003

Trunk
                                          						Group

2004

Service

2005

Skill
                                          						Group

2006

Agent

2007

Announcement

2008

Translation Route

2009

Label

2010

Route

2011

Script
                                          						Table

2012

Business
                                          						Entity

2013

Master
                                          						Script

2014

Enterprise
                                          						Service

2015

Enterprise
                                          						Skill Group

2016

Schedule

2017

Schedule
                                          						Source

2018

Agent Desk
                                          						Settings

2019

Agent
                                          						Team

2020

Application Gateway

2021

Enterprise Agent Group

2022

Network
                                          						Trunk Group

2023

Service
                                          						Array

2024

Device
                                          						Target (deprecated)

2025

Logical
                                          						Interface Controller

2026

User
                                          						Variable

2027

User
                                          						Formula

2028

Schedule
                                          						Report

2029

Network
                                          						VRU Script

2030

Scheduled Target

2031

Network
                                          						VRU

2032

Expanded
                                          						Call Variable

2033

Campaign

2034

Dialer

2035

Import
                                          						Rule

2036

Query
                                          						Rule

2100

System

2101

Network
                                          						Interface

2102

Peripheral Global

2103

Call

2104

Network/Peripheral

## Object Types: User
                        	 Variable

The ObjectType field
                              		  in the 
                              		  User Variable Table (see User_Variable )
                              		  takes one of these values:

0 = Unknown

1 = Service

2 = Skill Group

3 = Agent

4 = Translation Route

5 = Agent Administration
                                    				Group

6 = Announcement

7 = Call Type

8 = Enterprise Service

9 = Enterprise Skill
                                    				Group

10 = Region

11 = Dialed Number

12 = Logical Interface Controller

13 = Physical Interface
                                    				Controller

14 = Peripheral

15 = Routing Client

16 = Trunk Group

17 = Route

18 = Peripheral Target

19 = Label

20 = Master Script

21 = Script Table

22 = Script Table Column

23 = Script

24 = Schedule

25 = ICR View

26 = View Column

27 = Network Trunk Group

28 = Service Array

29 = Application Gateway

30 = Device Target
                                    				(deprecated)

31 = User Variable

32 = User Formula

33 = Network VRU Script

34 = Scheduled Target

35 = Network VRU

36 = Skill Group Member

37 = Expanded Call Variable

38 = Agent Team

39 = Campaign

40 = Dialer

41 = Import Rule

42 = Query Rule

43 = Campaign Query Rule

44 = Dialer Port Map

45 = Message Category

46 = Message
                                    				Destination

47 = Response Template

## Peripheral Real Time Status Field

The Status field in the
                              Peripheral Real Time table (see Peripheral_Real_Time ) can take these values:

The current
                              failure state of the peripheral is indicated by the status code:

0 = normal operation. The JTAPI Subsystem must be in
                                    service and all other subsystems are in service.

1 - 31 = failures that do not affect functionality. The
                                    JTAPI Subsystem must be in service and some other subsystems are not in
                                    service.

32-63 = degraded operation
                                    (call routing still possible). The JTAPI Subsystem is in partial service and
                                    all other subsystems are in service.

64 =
                                    no call processing

The JTAPI Subsystem is out of service and all
                                    other subsystems are in service.

65 - 127 = failures that prevent call routing

The JTAPI Subsystem
                                    is out of service and some other subsystems are not in service.

The JTAPI Subsystem reports "in service" if it can process calls and if
                                    all the configuration you specify can be initialized.

It reports
                                    "out of service" if it is not configured, if the CTI Manager is down, or if all
                                    of its configuration could not be initialized.

It reports "partial
                                    service" if some of its configuration could be initialize but not all of it.

When we are in a range, the Unified IP IVR simply increases the
                                    status by one for each subsystem (except the JTAPI subsystem) it finds to not
                                    be in service.

These values are dependant upon the peripheral
                                    connected to the PIM.

All PIMs use the previously discussed status
                                    codes, with the exception of the Avaya and the Unified IP IVR
                                    PIMs.

The Email and
                                             										Web Manager PIM receives its Status
                                    values from the Init event and the Status event.

The VRU
                                       PIM receives its status values from the Init Event, the Status Event,
                                    and Poll confirmation.

The Avaya PIM only uses four failure states:

0 = normal operation.

1 =
                                          failures that do not affect functionality.

32 =
                                          degraded operation (call routing still possible).

64 = failures that prevent call
                                          routing.

## Reason Codes

In addition to
                              		  reason codes that you have defined, the Unified CCE system uses predefined Not
                              		  Ready and Logout reason codes. The following tables describe these predefined
                              		  Not Ready and Logout reason codes. For more information see the Cisco Unified Contact Center Enterprise Reporting User Guide .
                              		  Also refer to the Reason_Code table.

Predefined
                                          						Not Ready Reason Code

999

A
                                          						Finesse supervisor forced an agent state change.

50002

A
                                          						CTI client component failed, causing the agent state to be displayed as Not
                                          						Ready. This could be due to closing the agent desktop application, heartbeat
                                          						timeout, or a CTI server client failure (such as Finesse).

50005

The
                                          						agent's state was changed to Not Ready because the agent either answered or
                                          						made a non-ACD call.

50006

When agent places call in Available state, the Unified CCE system temporarily changes the state to Not Ready with this reason
                                          code to prevent calls from routing to the agent.

50010

The agent did not receive multiple consecutive calls routed to them. The system makes the agent Not Ready automatically so
                                          that additional calls are not routed to the agent. By default, the number of consecutive calls missed before the agent is
                                          made Not Ready is 2.

51004

This
                                          						reason codes applies if an agent logs onto an extension which already has a
                                          						call or if the agent is on a call when the PG restarts.

50041

The
                                          						agent's state was changed to Not Ready because the call fails when the agent's
                                          						phone line rings busy.

32767

The
                                          						agent's state was changed to Not Ready because the agent did not answer a call
                                          						and the call was redirected to a different agent or skill group.

20001

The
                                          						agent's state was changed to Not Ready and the agent was forcibly logged out.

20002

This is
                                          						the normal logout reason code condition from Not Ready.

20003

If the
                                          						agent is not in Not Ready state, a request is made to place the agent in Not
                                          						Ready state and then a logout request is made to log the agent out.

Supervisor
                                          						Not Ready

This code
                                          						is reserved.

Predefined
                                          						Logout Reason Code

Description

-1

The agent
                                          						reinitialized due to peripheral restart.

-2

The PG reset the agent, usually due to a PG failure.

-3

An
                                          						administrator modified the agent's extension while the agent was logged in.

50002

A
                                          						CTI client component failed, causing the agent state to be displayed as logged
                                          						out. This could be due to closing the agent desktop application, heartbeat
                                          						timeout, or a CTI client failure (such as Finesse).

50003

The agent
                                          						was logged out because the Unified CM reported the agent's device as out of
                                          						service.

50004

The agent
                                          						was logged out due to agent inactivity as configured in agent desk settings.

50020

For
                                          						reskilling operations on active agents, the agent was logged out of the skill
                                          						group due to a reskilling operation that removed the skill group assignment to
                                          						that agent. This reason code is used in the Agent_Event_Detail record and the
                                          						Agent_Skill_Group_Logout record to identify the skill group the agent was
                                          						removed from (due to the reskilling operation).

50030

The agent
                                          						was logged out because the agent was logged into dynamic device target that was
                                          						using the same dialed number (DN) as the PG static device target.

50040

The mobile
                                          						agent was logged out because the call failed.

50042

The
                                          						mobile agent was logged out because the phone line disconnected when using
                                          						nailed connection mode.

20003

Forces
                                          						the logout request.

999

A supervisor forced an agent state change to Logout.

## Service Fields

The Unified ICM/Unified CCE software can use any of three formulas to
                              		  calculate the service level for a service.

The formulas differ in the way they treat calls that were abandoned
                              		  before the service level threshold expired.

The value of the ServiceLevelType field indicates the type of service
                              		  level calculation used.

Value

Meaning

0

Use default value from Peripheral record.

1

Ignore Abandoned Calls. Remove the abandoned calls from the
                                          						calculation.

2

Abandoned Calls have negative impact. Treat abandoned calls
                                          						as though they exceeded the service level threshold.

3

Abandoned Calls have positive impact. Treat abandoned calls
                                          						as though they were answered within the service level threshold.

Note that regardless of which calculation you choose, the system
                              		  software always tracks separately the number of calls abandoned before the
                              		  threshold expired.

In addition to tracking the service level as calculated by the system
                              		  software, the historical and real-time tables also track the service level as
                              		  calculated by the peripheral.

In the 
                              		  Peripheral (see Peripheral ), the PeripheralServiceLevelType field
                              		  indicates how the peripheral itself calculates the service level. Aspect
                              		  CallCenter ACDs can calculate service level in several different ways.

Valid options for Aspect types are:

1 = Service Level 1

2 = Service Level 2

3 = Service Level 3

4 = Service Level as Calculated by Call Center.

If this field is 0 for a service, the system software assumes the
                                    				default specified for the associated peripheral.

If the peripheral is not an Aspect ACD, the type must be 4
                                    				(calculated by the peripheral).

If the peripheral is not an Aspect ACD, the type must be 4 (calculated
                              		  by the peripheral).

## Service Real Time: Service Mode Indicator Field

In the 
                              		  Service_Real_Time Table (see Service_Real_Time ), the ServiceModeIndicator field
                              		  indicates the current mode of the service.

Value

Meaning

1

Day Service

2

Night Service

3

Closed with Answer

4

Closed with No Answer

5

Transition

6

Open

13

Pilot Status Other

## Survey Question (For Future Use)

The value in the following table represents the KPI metrics used in the Survey

Question Type Value

Meaning

1

Customer Satisfaction (CSAT)

2

Customer Effort (CES)

3

Net Promoter Score (NPS)

## Target Types: Script
                        	 Cross Reference and Scheduled Report Input

For the Script Cross Reference table (see Script_Cross_Reference ) the TargetType field indicates the type of object referenced by the script. That is, it indicates the table referenced by
                              the Script_Cross_Reference.ForeignKey field.

For the Scheduled Report Input table (see Schedule_Report_Input ), the Target Type is a unique identifier for the report input row.

Target
                                          						Type Values

Meaning

0

Unknown

1

Service

2

Skill
                                          						Group

3

Agent

4

Translation Route

5

Agent
                                          						Administration Group

6

Announcement

7

Call Type

8

Enterprise
                                          						Service

9

Enterprise
                                          						Skill Group

10

Region

11

Dialed
                                          						Number

12

Logical
                                          						Interface Controller

13

Physical
                                          						Interface Controller

14

Peripheral

15

Routing
                                          						Client

16

Trunk
                                          						Group

17

Route

18

Peripheral Target

19

Label

20

Master
                                          						Script

21

Script
                                          						Table

22

Script
                                          						Table Column

23

Script

24

Schedule

25

ICR View

26

View
                                          						Column

27

Network
                                          						Trunk Group

28

Service
                                          						Array

29

Application Gateway

30

Device
                                          						Target (deprecated)

31

User
                                          						Variable

32

User
                                          						Formula

33

Network
                                          						VRU Script

34

Scheduled Target

35

Network
                                          						VRU

36

Skill
                                          						Group Member

37

Expanded
                                          						Call Variable

38

Agent
                                          						Team

39

Campaign

40

Dialer

41

Import
                                          						Rule

42

Query
                                          						Rule

43

Campaign
                                          						Query Rule

44

Dialer
                                          						Port Map

45

Message
                                          						Category

46

Message
                                          						Destination

47

Response
                                          						Template

48

Enterprise Route

49

Person

50

Media
                                          						Routing Domain Member

51

Media
                                          						Routing Domain

52

Application Path

53

Peripheral MRD

54

Script
                                          						Queue Meters

55

Campaign
                                          						Target Sequence

56

Microapp
                                          						Defaults

57

Microapp
                                          						Currency

58

Microapp
                                          						Locale

59

Object Call

60

Dialer Skill Group

61

ECC Payload

62

Call Type Skill Group

63

Translation Route Meters

64

Attribute

65

Precision Queue

66

Precision Queue Step

67

Precision Queue Term

68

Precision Queue Step Member

69

Attribute Set

70

Attribute Set Member

71

Precision Queue Member

72

Congestion Control

73

Precision Queue Step Meter

80

Contact Share Group

81

Machine Address

82

Machine Host

83

Machine Service

84

Department

85

Contact Share Rule

86

Contact Share Queue

87

Business Hours

88

Business Hours Weekday

89

Business Hours Special Day

90

Business Hours Calendar

91

Business Hours Reason

92

Time Zone Location

The
                              		  Script_Cross_Reference.LocalID field indicates the script object that
                              		  references the target. The Script_Cross_Reference.ForeignKey indicates the
                              		  specific configuration record referenced.

## Termination Call
                        	 Detail: Call Disposition and CallDispositionFlag Fields

The Termination Call
                              		  Detail Table (see Termination_Call_Detail )
                              		  has two fields that provide details on why the call was considered handled,
                              		  abandoned, and so forth.

The Call
                                 			 Disposition field gives the final disposition of call (or how the call
                              		  terminated).

1 = Abandoned in Network

In Unified
                                       				  ICM , indicates the call was abandoned, or dropped, before being terminated
                                    				at a target device (for instance, an ACD, IVR, Desklink, etc.).

In Unified CCE , indicates that the call was routed to an agent but it never arrived or arrived after the PIM reservation timed-out. (The
                                    default timeout is 30 seconds.) An agent will be set to Not Ready if it misses two consecutive routed calls, Peripheral Call
                                    Type will usually be two, and the Call Type ID and Network Target ID will be filled in.

In Outbound
                                       				  Option , this result code indicates customer phone not in service.

2 = Abandoned in Local
                                       				  Queue

In Unified
                                       				  ICM, indicates the call was abandoned in the ACD queue while queued to an
                                    				ACD answering resources (for instance, a skill group, voice port, trunk, etc.)

In Unified
                                       				  CCE . Indicates that VRU Peripheral call was abandoned while in the queue
                                    				(only for VRU LEG call type).

VRU Service
                                                				  Control Queue Reporting has to be enabled.

In Outbound
                                       				  Option , this result code indicates an outbound call was abandoned either by
                                    				the customer or dialer.

3 = Abandoned Ring

In Unified ICM , indicates the call was abandoned while ringing at a device. For example, the caller did not wait for the call to be answered
                                    but disconnected while the call was ringing.

In Unified CCE , indicates that the caller disconnected while phone was ringing at the agent desktop.

4 = Abandoned Delay

In Unified
                                       				  ICM , indicates the call was abandoned without having been answered but not
                                    				while ringing or in a queue. Typically, a call marked Abandoned Delay was
                                    				delayed due to switch processing. Because of the delay, the caller ended up
                                    				dropping the call before it could be answered.

In Unified
                                       				  CCE , indicates that the destination was not connected when the call
                                    				terminated. This might mean that:

The agent
                                          					 logged out

The agent picked up the phone and then disconnected without dialing digits.

Route
                                          					 requests were logged on the Cisco Communication Manager PG that were not
                                          					 immediately redirected to an agent.

5 = Abandoned Interflow

In Unified
                                       				  ICM , indicates an interflow call that dropped before the call could be
                                    				handled by an answering resource. Interflow calls are calls between ACDs.
                                    				Abandoned Interflow is supported only by PIMs that track interflow calls.
                                    				Currently, this includes only the Aspect CallCenter PIM.

Does not apply
                                    				to Unified
                                       				  CCE .

6 = Abandoned Agent
                                       				  Terminal

In Unified ICM , indicates the call was dropped while being held at an agent device. For example, the caller is connected to an agent; the
                                    agent puts the caller on hold; the caller gets tired of waiting and disconnects the call.

In Unified CCE, indicates that the caller disconnected while on hold on the Unified CM PG, which generally indicates a training issue for
                                    the agent. On the VRU PG with Service Control Queue reporting checked, this usually indicates caller abandoned..

7 = Short

In Unified
                                       				  ICM , indicates the call was abandoned before reaching the abandoned call
                                    				wait time. Short calls are technically abandoned calls, but they are not
                                    				counted in the Unified ICM CallsAbandoned counts for the associated
                                    				service/route. Short calls are, however, counted as offered calls in the
                                    				CallsOffered and ShortCall counts.

Also applies to Unified
                                       				  CCE. In addition, route requests would be counted as short calls if so
                                    				configured.

8 = Busy

Not used in Unified
                                       				  ICM .

Does not apply
                                    				to Unified
                                       				  CCE .

In Outbound
                                       				  Option , this result code indicates an outbound call resulted in a busy
                                    				signal.

9 = Forced Busy

The call was
                                    				made busy by the ACD because there were no answering resources available to
                                    				handle the call. Currently, only the Avaya Aura PIM supports Forced Busy.

Does not apply
                                    				to Unified
                                       				  CCE .

10 = Disconnect/drop no
                                       				  answer

Only the
                                    				Meridian PIMs support the disconnect/drop no answer call disposition. For the
                                    				Meridian ACD, disconnect/drop no answer indicates that the ACD performed a
                                    				"forced disconnect" .Disconnect/drop no answer calls are counted as either
                                    				abandoned or short calls in the system software's service and route tables.

In Unified
                                       				  CCE , indicates that an agent-initiated call was not answered. (If agent
                                    				picked up the phone but did not dial any digits, the CallDisposition would be 4, Abandoned
                                       				  Delay .)

11 = Disconnect/drop busy

Does not apply
                                    				to Unified
                                       				  CCE.

12 = Disconnect/drop reorder

Does not apply
                                    				to Unified
                                       				  CCE .

13 = Disconnect/drop handled
                                       				  primary route

In Unified
                                       				  ICM, indicates the call was handled by an agent and was neither conferenced
                                    				nor transferred. These calls are counted as handled calls in Unified ICM
                                    				Schema's service, route, and skill group tables.

In Unified
                                       				  CCE , indicates that a call was routed to an agent on the Cisco
                                    				Communication Manager PG and handled without a transfer or conference. This
                                    				call disposition is also used for non-routed calls handled by the agent if wrap
                                    				up is used. On the VRU PG, this indicates that the call was handled by the VRU.
                                    				However, it does not indicate if the caller abandoned or disconnected the call
                                    				after the call was handled by the VRU.

Just in case
                                    				the script ends without routing the call, the RouterErrorCode field in the
                                    				Route Call Detail records will indicate the cause. Additionally, you can verify
                                    				if the ServiceLevelAband and ServiceLevelCallsOffered database fields in the
                                    				CTHH report are incremented. The incremented fields indicate that the caller
                                    				abandoned the call when the call was at the VRU.

14 = Disconnect/drop handled
                                       				  other In Unified
                                       				  ICM and Unified
                                       				  CCE , indicates the call was handled by a non-agent or unmonitored device
                                    				(for example, a voice mail system). These calls are counted as handled calls in
                                    				Unified ICM schema's service, route, and skill group tables.

15 = Redirected /
                                       				  Rejected

In Unified
                                       				  ICM , this indicates the call was redirected such that the PIM no longer can receive events
                                    				for the call. In other words, the PIM no longer has a way of referencing or
                                    				tracking the call. For example, the call might have been redirected to a
                                    				non-Unified ICM monitored device and then returned to the switch with a
                                    				different call ID. The Unified ICM generates the Termination Call Detail record
                                    				with only the data originally tracked for the call. Calls marked as Redirected
                                    				are counted as Overflow Out calls in the Unified ICM service and route tables.

In Unified
                                       				  CCE , to more accurately reflect call status, CallDisposition is set to 15
                                    				( Redirected ) instead
                                    				of 4 (Abandon Delay) when:

A call
                                          					 leaves a CTI route point to be sent to an IVR.

An agent
                                          					 transfers the call to another skillgroup and no agent is available, so the call
                                          					 is sent to an IVR.

16 = Cut Through

Not currently
                                    				used.

17 = Intraflow

Not currently
                                    				used.

18 = Interflow

Not currently
                                    				used.

19 = Ring No Answer

Not currently
                                    				used in Unified
                                       				  ICM.

In Unified CCE , this indicates the call wasn't answered by the agent within the Ring No Answer Time (set in the agent desktop setting in
                                    Unified ICM Configuration) or that the call was pulled back because of no answer as a result of CVP's RNA timeout expiring.

For nonvoice tasks, this indicates a RONA condition.  The task was not accepted within the MRD TaskStartTimeout.

In Outbound
                                       				  Option, this result code indicates an outbound call was not answered in the
                                    				alloted time.

20 = Intercept reorder

Does not apply
                                    				to Unified
                                       				  CCE.

In Outbound
                                       				  Option, this result code indicates the Dialer did not receive a ring back
                                    				from the ACD on the network.

21 = Intercept denial

Does not apply
                                    				to Unified
                                       				  CCE.

In Outbound
                                       				  Option, this result code indicates the customer call was intercepted by the
                                    				operator.

22 = Time Out

Supported only
                                    				by the Avaya ACD Manager PIM. Time out indicates that for an unknown reason the
                                    				PIM is no longer receiving events for the call. The Time Out call disposition
                                    				provides a way to "clean up" the call since events for the call can no longer
                                    				be monitored. Time out calls are counted as TerminatedOther in the Unified ICM
                                    				service and route tables.

Does not apply
                                    				to Unified CCE.

In Outbound
                                       				  Option, this result code indicates the Dialer is unable to detect a dial
                                    				tone.

23 = Voice Energy

Not currently
                                    				used in Unified
                                       				  ICM .

In Unified
                                       				  CCE , this indicates the outbound call was picked up by a person or an
                                    				answering machine.

In Outbound
                                       				  Option , this result code indicates the outbound call was picked up by a
                                    				person.

24 = Non-classified Energy
                                       				  Detected

Not currently
                                    				used in Unified
                                       				  ICM .

In Outbound
                                       				  Option , this result code indicates the outbound call reached a FAX machine.

25 = No Cut Through

Not currently
                                    				used.

26 = U-Abort

In the Unified
                                       				  ICM, this indicates the call ended abnormally.

In Unified
                                       				  CCE , the Unified CM indicated the call ended due to one of the following
                                    				reasons: network congestion, network not obtainable, or resource not available.
                                    				Such reasons may be due to errors in media set up.

In Outbound
                                       				  Option , this result code indicates the outbound call was stopped before the
                                    				customer picked up.

27 = Failed Software

In Unified
                                       				  ICM , either the PIM detected an error condition or an event did not occur
                                    				for a call for an extended period of time. For example, an inbound call with
                                    				Call ID 1 and associated with Trunk 1 might be marked failed if the PIM
                                    				received a different call ID associated with Trunk 1. This would indicate a
                                    				missing Disconnect event for Call ID 1.

If no events
                                    				are being tracked for the call, the call is eventually timed out. The failed
                                    				call is marked as a Forced Closed call in the Unified ICM Service and Route
                                    				tables.

In Unified
                                       				  CCE , generally indicates that Unified CM PG terminated the call because it
                                    				had exceeded the time allowed for this state. (The default is 1 hour in the
                                    				NULL state when agent has been removed, and 8 hours in the connected state. The
                                    				value is configurable.)

28 = Blind Transfer

In the Unified
                                       				  ICM , a transfer scenario involves a primary call and a secondary call. If
                                    				the secondary call is transferred to a queue or another non-connected device,
                                    				then the primary call (the one being transferred) is set to Blind Transfer.

In Unified
                                       				  CCE (Unified CM PG), this indicates that the call was transferred before
                                    				the destination answered. For Unified ICM (VRU PG), this indicates that the IVR
                                    				indicated the call was successfully redirected.

29 = Announced Transfer

In Unified ICM and Unified CCE , a transfer scenario involves a primary call and
                                    				a secondary call. If the secondary call is connected to another answering
                                    				device, or is put on hold at the device, then the primary call (the call being
                                    				transferred) is marked as Announced Transfer.

30 = Conferenced

In Unified
                                       				  ICM and Unified
                                       				  CCE , the call was terminated (dropped out of the conference). Conference
                                    				time is tracked in the system software's Skill Group tables for the skill group
                                    				that initiated the conference.

31 = Duplicate Transfer

Does not apply
                                    				to Unified
                                       				  CCE .

32 = Unmonitored Device

Not currently
                                    				used.

33 = Answering Machine

In Unified
                                       				  ICM , this indicates the call was answered by an answering machine. Does not
                                    				apply to Unified
                                       				  CCE .

In Outbound Option ,
                                    				indicates the call was picked up by an answering machine.

34 = Network Blind Transfer

In Unified
                                       				  ICM , indicates the call was transferred by the network to a different
                                    				peripheral. Does not apply to Unified CCE
                                       				  unless there is an ISN installation.

35 = Task Abandoned in
                                       				  Router

The NewTask
                                    				dialogue associated with the task was terminated before the Router could send a
                                    				DoThisWithTask message to the application instance that issued the NewTask.

36 = Task Abandoned Before
                                       				  Offered

This disposition is deprecated beginning in the 11.5(1) release.  Nonvoice tasks that RONA increment  disposition 19 instead
                                    of 36.

37 = Task Abandoned While
                                       				  Offered

This disposition is only defined for multi-session chat tasks. A task is given this disposition if an agent who is working
                                    on one chat session is assigned another chat session, and the customer involved in the new chat session disconnects before
                                    the agent begins chatting with the customer.

38 = Normal End Task

The task was
                                    				handled by an agent.

Only applies
                                    				to non-voice tasks.

39 = Can't Obtain Task
                                       				  ID

When an
                                    				application sends the system software an Offer Application Task or Start
                                    				Application Task request, it waits for the Unified ICM to send a response
                                    				containing that Task ID that Unified ICM has assigned to the task. If OPC is
                                    				unable to obtain a task ID from the Router (because the Router is down, or the
                                    				network connection between OPC and the Router is down), OPC will terminate the
                                    				task with disposition 39 "Can't Obtain Task ID".

40 = Agent Logged Out
                                       				  During Task

The agent
                                    				logged out of an MRD without terminating the task.

41 = Maximum Task Lifetime
                                       				  Exceeded

The system
                                    				software did not receive an End Task message for this task within the maximum
                                    				task lifetime of the MRD with which the task is associated.

42 = Application Path Went
                                       				  Down

The Task Life
                                    				timed out while the system software was attempting to communicate with the
                                    				application instance associated with the task. (This might have occurred either
                                    				because the application instance was down, or the network connection between
                                    				Unified ICM and the application instance was down.)

43 = Unified ICM Routing
                                       				  Complete

Not currently
                                    				used.

44 = Unified ICM Routing
                                       				  Disabled

Not currently
                                    				used.

45 = Application Invalid
                                       				  MRD ID

Not currently
                                    				used.

46 = Application Invalid
                                       				  Dialog ID

Not currently
                                    				used.

47 = Application Duplicate
                                       				  Dialogue ID

Not currently
                                    				used.

48 = Application Invalid
                                       				  Invoke ID

Not currently
                                    				used.

49 = Application Invalid
                                       				  Script Selector

The task was rejected because of an invalid Script Selector in the Task Routing request.

50 = Application Terminate
                                       				  Dialogue

Not currently
                                    				used.

51 = Task Ended During
                                       				  Application Init

The
                                    				application instance notified the system software that a task that existed
                                    				prior to the loss of connection was not initialized by the application once
                                    				connection was restored.

52 = Called Party
                                       				  Disconnected.

CD 52 expected
                                    				when called party disconnects, with CVP being the routing client.

53 = Partial call

This code
                                    				simplifies the process of distinguishing interim from final TCD records at
                                    				reporting or extract time.

Records that
                                    				contain this CallDisposition code are considered interim records.

OPC will be
                                    				changed to set a new "PartialCall" EventCause when it receives a
                                    				GEO_NewTransaction_Ind message from any PIM, and OPC's
                                    				EventCauseToDisposition() needs to translate that EventCause to the new
                                    				"PartialCall" CallDisposition.

54 = Drop Network
                                       				  Consult

A Network
                                    				Consult was established, and the agent then reconnected.

55 = Network Consult
                                       				  Transfer

The Network
                                    				Consult was established, and then the transfer was completed.

57 = Abandon Network
                                       				  Consult

The Network
                                    				Consult was never established (ringing, but not answered), and the agent gives
                                    				up and reconnects.

58 = Router Requery Before
                                       				  Answer

Router
                                    				Received a Requery Event from CVP before the Agent PG indicated the call was
                                    				answered by an agent.

59 = Router Requery After
                                       				  Answer

Router
                                    				Received a Requery Event from CVP after the Agent PG indicated the call was
                                    				answered by an agent.

60 = Network Error

Router
                                    				received a Network Error for a call targeting an agent before the call arrived
                                    				to the agent.

61 = Network Error Before
                                       				  Answer

Router
                                    				Received a Network Error Event from CVP before the Agent PG indicated the call
                                    				was answered by an agent.

62 = Network Error After
                                       				  Answer

Router
                                    				Received a Network Error Event from CVP after the Agent PG indicated the call
                                    				was answered by an agent.

63 = Task Transfer

The task was transferred. The initiating application sent a new task request to CCE for routing that includes the task id
                                    of the first task.

64 = Application Disconnected

Used for single ApplicationPath failures, for ApplicationInstances supporting multiple Client Connections using the same ApplicationPath
                                    (UQ.Path). In this case the Application Path is not considered down, because the other client instance of the Application
                                    is still connected. This occurs when a TaskLive timeout occurs or and agent logs in again to the ApplicationPath.

65 = Task Transferred on Agent Logout

The agent logged out of the MRD with an active task, and the task was transferred.

66 = Pick / Pull Request Error

The pick or pull request failed.

The CallDispositionFlag field provides detail on the call disposition.

Flags are:

DBCDF_HANDLED
                                    				= 1

DBCDF_ABANDONED = 2

DBCDF_SHORT =
                                    				3

DBCDF_ERROR =
                                    				4

DBCDF_REDIRECTED = 5

DBCDF_REQUERY
                                    				= 6

DBCDF_INCOMPLETE = 7

## Termination Call
                        	 Detail: Peripheral Call Type

The
                              		  PeripheralCallType field in the 
                              		  Termination Call Detail
                              			 Table (see Termination_Call_Detail ) offers information about the type of the call as reported by the
                              		  peripheral.

Valid settings for
                              		  this field are:

1 = ACD In

In Unified
                                       				  ICM (VRU PG), all calls are of this type.

In Unified
                                       				  CCE (Unified CM PG), generally indicates that this is a post-route request.

2 = Pre-Route ACD In

In Unified
                                       				  CCE , indicates call was routed to this destination so the Unified CM PG has
                                    				routing information to associate with the call (router call key, call context).

3 = Pre-Route Direct
                                       				  Agent

Does not apply
                                    				to Unified
                                       				  CCE .

4 = Transfer In

In Unified CCE , indicates the call was transferred from another agent or device. The name value is misleading because it is used for calls
                                    transferred in or out.

5 = Overflow In

Does not apply
                                    				to Unified
                                       				  CCE .

6 = Other In

In Unified
                                       				  CCE , used for inbound calls that do not have route information/call context
                                    				associated. Applies to a call coming from an agent from the same peripheral.

7 = Auto Out

In Outbound
                                       				  option, indicates a Predictive /Progressive customer call.

8 = Agent Out

Does not apply
                                    				to Unified
                                       				  CCE.

9 = Out

In Unified
                                       				  CCE , indicates call was placed outside the Unified CM cluster or that a
                                    				network reached event was received.

10 = Agent Inside

11 = Offered

Does not apply
                                    				to Unified
                                       				  CCE.

12 = Consult

13 = Consult Offered

14 = Consult Conference

Does not apply
                                    				to Unified
                                       				  CCE.

15 = Conference , Supervisor Barge In

Supervisor Barge In is specified as returning a PeripheralCallType of 23, but currently returns 15, Conference, in the Termination Call Detail
                                                Table.

16 = Unmonitored

Does not apply
                                    				to Unified
                                       				  CCE .

17 = Preview

In Outbound
                                       				  Option indicates a Preview/Callback customer call.

18 = Reserved

In Outbound
                                       				  Option indicates a Reservation call.

19 = Supervisor Assist

20 = Emergency Call

21 = Supervisor Monitor

22 = Supervisor Whisper

Does not apply
                                    				to Unified
                                       				  CCE .

Supervisor Barge In

Supervisor Barge In is specified as returning a PeripheralCallType of 23, but currently returns 15, Conference, in the Termination Call Detail
                                                Table.

24 = Supervisor Intercept

25 = Task Routed by Unified CCE

Call type for nonvoice tasks routed by Unified CCE.

26 = Task Started by Application
                                       				  Instance

Call type for nonvoice tasks started by an agent or application.

27 = Reservation Preview

Call type for Outbound
                                       				  Option Reservation calls for Preview mode.

28 = Reservation Preview
                                       				  Direct

Call type for Outbound
                                       				  Option Reservation calls for Direct Preview mode.

29 = Reservation
                                       				  Predictive

Call type for Outbound
                                       				  Option Reservation calls for Predictive mode and Progressive mode.

30 = Reservation
                                       				  Callback

Call type for Outbound
                                       				  Option Reservation calls for Callback calls.

31 = Reservation Personal
                                       				  Callback

Call type for Outbound
                                       				  Option Reservation calls for Personal Callback calls.

32 = Customer Preview

Call type for Outbound
                                       				  Option Customer calls for Preview mode.

33 = Customer Preview
                                       				  Direct

Call type for Outbound
                                       				  Option Customer calls for Direct Preview mode.

34 = Customer
                                       				  Predictive

Call type for Outbound
                                       				  Option Customer calls for Predictive mode and Progressive mode for
                                    				agent-based campaigns.

35 = Customer Callback

Call type for Outbound
                                       				  Option Customer calls for callback calls.

36 = Customer Personal
                                       				  Callback

Call type for Outbound
                                       				  Option Customer calls for personal callback calls.

37 = Customer IVR

Call type for Outbound
                                       				  Option Customer calls for Transfer to IVR campaigns.

38 = Non-ACD Call

Call type for Multi-Line
                                       				  Agent . Agent placed or received a call on a secondary extension. In an
                                    				agent to agent call that includes both an ACD line and a non-ACD line, the ACD
                                    				line attributes take precedence.

39 = Play Agent
                                       				  Greeting

Route request
                                    				to play an Agent Greeting.

40 = Record Agent
                                       				  Greeting

Agent call for
                                    				recording an Agent Greeting.

41 = Voice Callback

Agent call for
                                    				outbound Voice Callback.

42 = Switch Leg

Switch Leg for VRU Peripheral call.

Identifies the switch leg of the call at CVP, deployed as a Type 10 VRU.

43 = VRU Leg

VRU Leg for VRU Peripheral call.

Identifies the VRU leg of the call at CVP, deployed as a Type 10 VRU. (This is only classified as VRU leg, if Queue Reporting has been enabled for the corresponding VRU PG, using Peripheral Gateway Setup). If enabled, calls abandoned in queue will
                                                have an Abandoned call disposition for the VRU leg of the call, instead of a Handled call disposition, which helps in identifying
                                                individual calls that were abandoned while being queued at CVP. The abandoned call disposition is restricted to only queued
                                                calls, and not to Self-service calls.

44 = Pick Request

Pick request from a non-Voice queue.

45 = Pull Request

Pull request from a non-Voice queue.

## Trunk Type

The Type field in the
                              Trunk Table (see Trunk )
                              allows these values to indicate the type of trunk:

1 = Local C.O.

2 = Foreign Exchange

3 =
                                    WATS

4 = DID/DNIS

5 = PRI

6 = Tie
                                    Line

7 =
                                    Interflow

| Access Level Values | Meaning |
|---|---|
| 10 | Read |
| 20 | Reference |
| 30 | Maintenance (create, read, update, delete) |

| Note | The meaning for this field varies depending on the table that uses
                                          		  it. |
|---|---|

| Agent State Values | Meaning (Agent_Real_Time / Agent_Skill_Group_Real_Time) | Meaning (Agent_State_Trace) |
|---|---|---|
| 0 | Logged Off | Logged Off |
| 1 | Logged On | Logged On |
| 2 | Not Ready | Not Ready |
| 3 | Ready | Ready |
| 4 | Talking | Talking |
| 5 | Work Not Ready | Work Not Ready |
| 6 | Work Ready | Work Ready |
| 7 | Busy Other | Busy Other |
| 8 | Reserved | Reserved |
| 9 | Unknown | Call Initiated |
| 10 | Calls On Hold | Call Held |
| 11 | Active | Active |
| 12 | Paused | Paused |
| 13 | Interrupted | Interrupted |
| 14 | Not Active Note Not Active is an agent state when the agent is signed into a nonvoice skill group or precision queue.  This state is the equivalent
                                                      of Ready for voice. | Note | Not Active is an agent state when the agent is signed into a nonvoice skill group or precision queue.  This state is the equivalent
                                                      of Ready for voice. | Not Active |
| Note | Not Active is an agent state when the agent is signed into a nonvoice skill group or precision queue.  This state is the equivalent
                                                      of Ready for voice. |

| Note | Not Active is an agent state when the agent is signed into a nonvoice skill group or precision queue.  This state is the equivalent
                                                      of Ready for voice. |
|---|---|

| Type Values | Meaning |
|---|---|
| 1 | Daily (the DayType field indicates which days of the week) |
| 2 | Weekly (the DayType field indicates which days of the week) |
| 3 | Biweekly (the DayType field indicates which days of the
                                          						week) |
| 4 | Monthly (the Day field specifies the day of month) |
| 5 | Monthly (the DayPosition and DayType fields indicate day of
                                          						the month) |
| 6 | Yearly (the month and day fields specify the day of year) |
| 7 | Yearly (the DayPosition, DayType, and Month specify the day
                                          						of year) |
| 8 | Range (the starting and ending date and times specify the
                                          						range) |

| Note | ARS PIM is
                                                   					 deprecated in release 10.0(1). |
|---|---|

| Type Values | Meaning |
|---|---|
| 1 | Allow quick-edit of Announcement node |
| 2 | Allow quick-edit of Call Type node |
| 3 | Allow quick-edit of Caller Entered Digits node |
| 4 | Allow quick-edit of Calling Line ID node |
| 5 | Allow quick-edit of Dialed Number node |
| 6 | Allow quick-edit of Goto Script node |
| 7 | Allow quick-edit of Percent Allocation node |
| 8 | Allow quick-edit of Requalify node |
| 9 | Allow quick-edit of Run VRU Script node |
| 10 | Allow quick-edit of Scheduled Select node |
| 11 | Allow quick-edit of Switch node |
| 12 | Allow quick-edit of Time node |
| 50 | Bill for VRU time |
| 51 | Customer billing data |

| Values | Meaning |
|---|---|
| Day of the Week | 0x01 = Sunday 0x02 = Monday 0x04 = Tuesday 0x08 = Wednseday 0x10 = Thursday 0x20 = Friday 0x40 = Saturday |
| Day of the Month | 0 = Applies to every day 1-31 = Specifies the day of month |
| Day Position | 0 = First day of the type in a month 1 = Second day of the type in a month 2 = Third day of the type in a month 3 = Fourth day of the type in a month 4 = Last day of the type in a month 5 = Every day of the type in a month |
| Day Type | 0-6 = Specifies a day (Sunday through Saturday,
                                          						respectively) 7 = Every day 8 = Every weekday 9 = Every weekend day |

| ANIWildCardType Value | Meaning |
|---|---|
| 0 | Unknown |
| 1 | NPA (3-digit match) |
| 2 | NPA-NXX (6-digit match) |
| 3 | Match (all digits are match) |
| 4 | Region |
| 5 | All (match all ANIs) |
| 6 | Prefix |

| Note | If the value is 4, then the ANIWildCard value is ignored and the
                                       		  RegionID value is used. |
|---|---|

| System
                                          						Type Values | Meaning |
|---|---|
| 2 | Error condition while dialing. |
| 3 | Number reported not in service by network. |
| 4 | No ringback from network when dial attempted. |
| 5 | Operator intercept returned from network when dial attempted. |
| 6 | No dial tone when dialer port went off hook. |
| 7 | Number reported as invalid by the network. |
| 8 | Customer phone did not answer. |
| 9 | Customer phone was busy. |
| 10 | Customer answered and was connected to agent. |
| 11 | Fax machine detected. |
| 12 | Answering machine detected. |
| 13 | Dialer stopped dialing customer due to lack of agents or network stopped dialing before it was complete. |
| 14 | Customer requested callback. |
| 15 | Answering machine requested callback. |
| 16 | Call connected with customer was abandoned by the dialer due to lack of agents. |
| 17 | Failed to reserve agent for personal callback. |
| 18 | Agent has skipped or rejected a preview call. |
| 19 | Agent has skipped or rejected a preview call with the close option. |
| 20 | Customer has been abandoned to an IVR. |
| 21 | Customer dropped call within configured abandoned time. |
| 22 | In Unified CCE, the call
                                          									result indicates an answering machine detection which did not
                                          									meet termination conditions. One such example is a network
                                          									voicemail message indicating a mailbox is full or not setup
                                          									properly. In TDM switches, it indicates a network answering
                                          									machine detection, such as a network voicemail. |
| 23 | Number successfully contacted but wrong number. (Not supported). |
| 24 | Number successfully contacted but reached the wrong person. (Not supported). |
| 25 | Dialer has flushed this record because there is a change in the skillgroup, or a change in the campaign, or there are no agents
                                          available. |
| 26 | The number was on the do not call list. |
| 27 | Call disconnected by the carrier or the network while ringing. |
| 28 | Dead air or low voice volume call. |
| 29 | Received message is not supported by voice gateway. |
| 30 | Received message is not authorized by voice gateway. |
| 31 | Invalid message received by voice gateway. |
| 32 | Call cancelled because the dialer lost connection with the Campaign Manager. |
| 33 | Agent timed-out accepting preview or personal callback call. Note This Call Result is supported from 12.0 ES33 onwards. | Note | This Call Result is supported from 12.0 ES33 onwards. |
| Note | This Call Result is supported from 12.0 ES33 onwards. |

| Note | This Call Result is supported from 12.0 ES33 onwards. |
|---|---|

| System Type Values | Meaning |
|---|---|
| 0 | Unknown |
| 1 | CallRouter |
| 2 | Peripheral Gateway (PG) |
| 3 | Network Interface Controller (NIC) |
| 4 | Administration & DataServer (ADS) |
| 5 | Logger |
| 6 | Listener |
| 7 | CTI Gateway |
| 8 | Blended Agent Dialer |

| Note | If the event is generated by a PG or an AT&T NIC, the
                                       		  Event.SystemId field indicates the specific machine. For a CallRouter or
                                       		  Logger, Event.SystemId is always 0. |
|---|---|

| Value | Meaning |
|---|---|
| 0 | Master lock (applies to configuration data and script. |
| 1 | Configuration lock (no longer used) |
| 2 | Script Lock(applies to an individual script) |
| 3 | Application lock (no longer used) |

| Note | If the event is generated by a PG or an AT&T NIC, the
                                       		  Event.SystemId field indicates the specific machine. For a CallRouter or
                                       		  Logger, Event.SystemId is always 0. |
|---|---|

| LabelType Values | Meaning |
|---|---|
| 0 | Normal |
| 1 | DNIS Override (the system software returns the specific DNIS
                                          						value to be used with the label) |
| 2 | Busy (instructs the routing client to play a busy signal to
                                          						caller) |
| 3 | Ring (instructs the routing client to play an unanswered
                                          						ring to caller) |
| 4 | Post-Query (instructs the routing client to re-enter its
                                          						call processing plan at a specific point) |
| 5 | Resource (used internally for special routing client
                                          						resources, such as a network VRU) |

| Note | Not all label types are valid for all routing client types. |
|---|---|

| Value | Meaning |
|---|---|
| 1 | Avaya
                                          						DEFINITY ECS, without Expert Agent Selection (EAS) 1 |
| 2 | MCI |
| 3 | Sprint |
| 4 | Aspect
                                          						CallCenter |
| 5 | Nortel
                                          						Meridian |
| 6 | Rockwell
                                          						Galaxy without priority enhancements (r1.3) (Not
                                          						supported) 2 |
| 7 | AT&T
                                          						GTN |
| 8 | Generic
                                          						Network Interface Controller (GenNIC) |
| 9 | Avaya G2 |
| 10 | Rockwell
                                          						Galaxy (Not supported) |
| 11 | Rockwell
                                          						Spectrum (Not supported) |
| 12 | Avaya
                                          						DEFINITY ECS, with Expert Agent Selection (EAS) |
| 13 | Voice
                                          						Response Unit (VRU) |
| 14 | British
                                          						Telecom NIC |
| 15 | Voice
                                          						Response Unit (VRU), polled |
| 16 | INCRP NIC |
| 17 | Nortel NIC |
| 18 | DMS 100 (Not
                                             						  supported) |
| 19 | Siemens
                                          						Hicom 300 E, 9006 (Not supported) |
| 20 | France
                                          						Telecom |
| 21 | Ameritech |
| 22 | BT INAP
                                          						NIC |
| 23 | Siemens
                                          						ROLM 9751 CBX, 9005 (Not supported) |
| 24 | ICR
                                          						Protocol (ICRP) NIC |
| 25 | Alcatel
                                          						4400 (Not supported) |
| 26 | NEC NEAX
                                          						2x00 |
| 27 | ACP 1000 |
| 28 | AACC. |
| 29 | Enterprise Agent |
| 30 | Call
                                          						Routing Service Protocol (CRSP) NIC |
| 31 | Ericsson
                                          						MD110 |
| 32 | able
                                          						& Wireless Corp. (CWC) INAP NIC |
| 33 | Energis
                                          						INAP NIC |
| 34 | AUCS
                                          						INAP NIC |
| 35 | Concert
                                          						NIC |
| 36 | Deutsche
                                          						Telecom NIC |
| 37 | CAIN NIC |
| 38 | Telfort
                                          						INAP NIC |
| 39 | BT V2
                                          						NIC |
| 40 | TIM INAP
                                          						NIC |
| 41 | Generic
                                          						PG |
| 42 | CeM |

| Type
                                          						Values | Interface |
|---|---|
| 1 | Normal
                                          						label type and a correlation ID. |
| 2 | Normal
                                          						label type and a DNIS. |
| 3 | Resource
                                          						label type and a correlation ID. The routing client can automatically take back
                                          						the call from the VRU when the system software returns a destination label. |
| 4 | Resource
                                          						label type and a DNIS. |
| 5 | Resource
                                          						label type and either a correlation ID or a DNIS. |
| 6 | No label,
                                          						no correlation ID, and no DNIS (call is already at the VRU). |
| 7 | Similar to
                                          						Type 3, but the system software automatically instructs the VRU to release the
                                          						call when it sends a destination label to the routing client. |
| 8 | Similar to
                                          						Type 2, but a Type 8 VRU is used when the NAM has a routing client that
                                          						controls the call to the VRU. |
| 9 | Queuing
                                          						for Network VRU controlled by the Unified CCE System PG. |
| 10 | Simplifies
                                          						configuration requirements in Unified CVP Comprehensive Model deployments. |

| Value | Meaning |
|---|---|
| 1 | Pre- Routing request |
| 2 | Blind
                                          						transfer or network VRU |
| 3 | Announced
                                          						transfer or MCI 800 call |
| 4 | Overflow |
| 5 | Re-route |
| 6 | Post- Routing request |

| Value | Meaning |
|---|---|
| 0 | Unknown |
| 1 | Trunk |
| 2 | Teleset |
| 3 | Voice
                                          						Response Unit (VRU) |
| 4 | Trunk
                                          						Group |

| Note | A Route_Call_Detail.RouterErrorCode value of 448 is treated as an abandoned call and does not increment the Call_Type_Interval.ErrorCount . |
|---|---|

| Note | Some internally used error codes are not updated in the RCD. |
|---|---|

| Object
                                          						Type Values | Meaning |
|---|---|
| 2000 | Dialed
                                          						Number |
| 2001 | Call Type |
| 2002 | Peripheral |
| 2003 | Trunk
                                          						Group |
| 2004 | Service |
| 2005 | Skill
                                          						Group |
| 2006 | Agent |
| 2007 | Announcement |
| 2008 | Translation Route |
| 2009 | Label |
| 2010 | Route |
| 2011 | Script
                                          						Table |
| 2012 | Business
                                          						Entity |
| 2013 | Master
                                          						Script |
| 2014 | Enterprise
                                          						Service |
| 2015 | Enterprise
                                          						Skill Group |
| 2016 | Schedule |
| 2017 | Schedule
                                          						Source |
| 2018 | Agent Desk
                                          						Settings |
| 2019 | Agent
                                          						Team |
| 2020 | Application Gateway |
| 2021 | Enterprise Agent Group |
| 2022 | Network
                                          						Trunk Group |
| 2023 | Service
                                          						Array |
| 2024 | Device
                                          						Target (deprecated) |
| 2025 | Logical
                                          						Interface Controller |
| 2026 | User
                                          						Variable |
| 2027 | User
                                          						Formula |
| 2028 | Schedule
                                          						Report |
| 2029 | Network
                                          						VRU Script |
| 2030 | Scheduled Target |
| 2031 | Network
                                          						VRU |
| 2032 | Expanded
                                          						Call Variable |
| 2033 | Campaign |
| 2034 | Dialer |
| 2035 | Import
                                          						Rule |
| 2036 | Query
                                          						Rule |
| 2100 | System |
| 2101 | Network
                                          						Interface |
| 2102 | Peripheral Global |
| 2103 | Call |
| 2104 | Network/Peripheral |

| Predefined
                                          						Not Ready Reason Code |  |
|---|---|
| 999 | A
                                          						Finesse supervisor forced an agent state change. |
| 50002 | A
                                          						CTI client component failed, causing the agent state to be displayed as Not
                                          						Ready. This could be due to closing the agent desktop application, heartbeat
                                          						timeout, or a CTI server client failure (such as Finesse). |
| 50005 | The
                                          						agent's state was changed to Not Ready because the agent either answered or
                                          						made a non-ACD call. |
| 50006 | When agent places call in Available state, the Unified CCE system temporarily changes the state to Not Ready with this reason
                                          code to prevent calls from routing to the agent. |
| 50010 | The agent did not receive multiple consecutive calls routed to them. The system makes the agent Not Ready automatically so
                                          that additional calls are not routed to the agent. By default, the number of consecutive calls missed before the agent is
                                          made Not Ready is 2. |
| 51004 | This
                                          						reason codes applies if an agent logs onto an extension which already has a
                                          						call or if the agent is on a call when the PG restarts. |
| 50041 | The
                                          						agent's state was changed to Not Ready because the call fails when the agent's
                                          						phone line rings busy. |
| 32767 | The
                                          						agent's state was changed to Not Ready because the agent did not answer a call
                                          						and the call was redirected to a different agent or skill group. |
| 20001 | The
                                          						agent's state was changed to Not Ready and the agent was forcibly logged out. |
| 20002 | This is
                                          						the normal logout reason code condition from Not Ready. |
| 20003 | If the
                                          						agent is not in Not Ready state, a request is made to place the agent in Not
                                          						Ready state and then a logout request is made to log the agent out. |
| Supervisor
                                          						Not Ready | This code
                                          						is reserved. |

| Predefined
                                          						Logout Reason Code | Description |
|---|---|
| -1 | The agent
                                          						reinitialized due to peripheral restart. |
| -2 | The PG reset the agent, usually due to a PG failure. |
| -3 | An
                                          						administrator modified the agent's extension while the agent was logged in. |
| 50002 | A
                                          						CTI client component failed, causing the agent state to be displayed as logged
                                          						out. This could be due to closing the agent desktop application, heartbeat
                                          						timeout, or a CTI client failure (such as Finesse). |
| 50003 | The agent
                                          						was logged out because the Unified CM reported the agent's device as out of
                                          						service. |
| 50004 | The agent
                                          						was logged out due to agent inactivity as configured in agent desk settings. |
| 50020 | For
                                          						reskilling operations on active agents, the agent was logged out of the skill
                                          						group due to a reskilling operation that removed the skill group assignment to
                                          						that agent. This reason code is used in the Agent_Event_Detail record and the
                                          						Agent_Skill_Group_Logout record to identify the skill group the agent was
                                          						removed from (due to the reskilling operation). |
| 50030 | The agent
                                          						was logged out because the agent was logged into dynamic device target that was
                                          						using the same dialed number (DN) as the PG static device target. Note Device target is deprecated. | Note | Device target is deprecated. |
| Note | Device target is deprecated. |
| 50040 | The mobile
                                          						agent was logged out because the call failed. |
| 50042 | The
                                          						mobile agent was logged out because the phone line disconnected when using
                                          						nailed connection mode. |
| 20003 | Forces
                                          						the logout request. |
| 999 | A supervisor forced an agent state change to Logout. |

| Note | Device target is deprecated. |
|---|---|

| Value | Meaning |
|---|---|
| 0 | Use default value from Peripheral record. |
| 1 | Ignore Abandoned Calls. Remove the abandoned calls from the
                                          						calculation. |
| 2 | Abandoned Calls have negative impact. Treat abandoned calls
                                          						as though they exceeded the service level threshold. |
| 3 | Abandoned Calls have positive impact. Treat abandoned calls
                                          						as though they were answered within the service level threshold. |

| Value | Meaning |
|---|---|
| 1 | Day Service |
| 2 | Night Service |
| 3 | Closed with Answer |
| 4 | Closed with No Answer |
| 5 | Transition |
| 6 | Open |
| 13 | Pilot Status Other |

| Question Type Value | Meaning |
|---|---|
| 1 | Customer Satisfaction (CSAT) |
| 2 | Customer Effort (CES) |
| 3 | Net Promoter Score (NPS) |

| Target
                                          						Type Values | Meaning |
|---|---|
| 0 | Unknown |
| 1 | Service |
| 2 | Skill
                                          						Group |
| 3 | Agent |
| 4 | Translation Route |
| 5 | Agent
                                          						Administration Group |
| 6 | Announcement |
| 7 | Call Type |
| 8 | Enterprise
                                          						Service |
| 9 | Enterprise
                                          						Skill Group |
| 10 | Region |
| 11 | Dialed
                                          						Number |
| 12 | Logical
                                          						Interface Controller |
| 13 | Physical
                                          						Interface Controller |
| 14 | Peripheral |
| 15 | Routing
                                          						Client |
| 16 | Trunk
                                          						Group |
| 17 | Route |
| 18 | Peripheral Target |
| 19 | Label |
| 20 | Master
                                          						Script |
| 21 | Script
                                          						Table |
| 22 | Script
                                          						Table Column |
| 23 | Script |
| 24 | Schedule |
| 25 | ICR View |
| 26 | View
                                          						Column |
| 27 | Network
                                          						Trunk Group |
| 28 | Service
                                          						Array |
| 29 | Application Gateway |
| 30 | Device
                                          						Target (deprecated) |
| 31 | User
                                          						Variable |
| 32 | User
                                          						Formula |
| 33 | Network
                                          						VRU Script |
| 34 | Scheduled Target |
| 35 | Network
                                          						VRU |
| 36 | Skill
                                          						Group Member |
| 37 | Expanded
                                          						Call Variable |
| 38 | Agent
                                          						Team |
| 39 | Campaign |
| 40 | Dialer |
| 41 | Import
                                          						Rule |
| 42 | Query
                                          						Rule |
| 43 | Campaign
                                          						Query Rule |
| 44 | Dialer
                                          						Port Map |
| 45 | Message
                                          						Category |
| 46 | Message
                                          						Destination |
| 47 | Response
                                          						Template |
| 48 | Enterprise Route |
| 49 | Person |
| 50 | Media
                                          						Routing Domain Member |
| 51 | Media
                                          						Routing Domain |
| 52 | Application Path |
| 53 | Peripheral MRD |
| 54 | Script
                                          						Queue Meters |
| 55 | Campaign
                                          						Target Sequence |
| 56 | Microapp
                                          						Defaults |
| 57 | Microapp
                                          						Currency |
| 58 | Microapp
                                          						Locale |
| 59 | Object Call |
| 60 | Dialer Skill Group |
| 61 | ECC Payload |
| 62 | Call Type Skill Group |
| 63 | Translation Route Meters |
| 64 | Attribute |
| 65 | Precision Queue |
| 66 | Precision Queue Step |
| 67 | Precision Queue Term |
| 68 | Precision Queue Step Member |
| 69 | Attribute Set |
| 70 | Attribute Set Member |
| 71 | Precision Queue Member |
| 72 | Congestion Control |
| 73 | Precision Queue Step Meter |
| 80 | Contact Share Group |
| 81 | Machine Address |
| 82 | Machine Host |
| 83 | Machine Service |
| 84 | Department |
| 85 | Contact Share Rule |
| 86 | Contact Share Queue |
| 87 | Business Hours |
| 88 | Business Hours Weekday |
| 89 | Business Hours Special Day |
| 90 | Business Hours Calendar |
| 91 | Business Hours Reason |
| 92 | Time Zone Location |

| Note | VRU Service
                                                				  Control Queue Reporting has to be enabled. |
|---|---|

| Note | When the
                                             				short call abandon timer is configured, single step transfers (local
                                             				transfers), being blind transfers by definition, have a Call Disposition of 7
                                             				(short call abandon) and a Peripheral Call Type of 4 (transfer) |
|---|---|

| Note | The consult
                                             				leg would have this disposition for a successful single step transfer. |
|---|---|

| Note | This
                                             				disposition will also be reported on a consult leg for a successful network
                                             				consult transfer. |
|---|---|

| Note | Supervisor Barge In is specified as returning a PeripheralCallType of 23, but currently returns 15, Conference, in the Termination Call Detail
                                                Table. |
|---|---|

| Note | Supervisor Barge In is specified as returning a PeripheralCallType of 23, but currently returns 15, Conference, in the Termination Call Detail
                                                Table. |
|---|---|

| Note | Identifies the switch leg of the call at CVP, deployed as a Type 10 VRU. |
|---|---|

| Note | Identifies the VRU leg of the call at CVP, deployed as a Type 10 VRU. (This is only classified as VRU leg, if Queue Reporting has been enabled for the corresponding VRU PG, using Peripheral Gateway Setup). If enabled, calls abandoned in queue will
                                                have an Abandoned call disposition for the VRU leg of the call, instead of a Handled call disposition, which helps in identifying
                                                individual calls that were abandoned while being queued at CVP. The abandoned call disposition is restricted to only queued
                                                calls, and not to Self-service calls. |
|---|---|