---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-icm-enterprise-icm-enterprise-12-6-1-installatio-07acb5370d
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/icm_enterprise/icm_enterprise_12_6_1/installation/guide/ucce_b_cti-os-system-manager-guide12-6-1/ucce_b_cti-os-system-manager-guide12-5_chapter_01010.html
retrieved_at: 2026-08-16T20:06:37.850781+00:00
---

CTI OS System Manager Guide for Cisco Unified ICM, Release 12.6(1)

# CTI OS System Manager Guide for Cisco Unified ICM, Release 12.6(1)

Updated: May 12, 2021

Chapter: Peripheral-Specific Support

## Chapter: Peripheral-Specific Support

# Peripheral-Specific Support

## TDM peripherals

Different
                           		  peripheral manufacturers provide varying levels of support for CTI specific
                           		  features. You must take these differences into account when writing a CTI OS
                           		  client application. As far as possible, the CTI OS Server and agent desktop
                           		  simulate the hardphone behavior of the peripheral in question. The CTI OS
                           		  Supervisor Desktop for Unified CCE is specific to Unified CCE and is currently not supported
                           		  on the TDM switches because they do not, in general, provide the Supervisory
                           		  features that Unified CCE provides.

The peripherals
                                       			 mentioned in this chapter are the ones that CTI OS supports. Please contact Cisco CTI Product Management
                                       			 if you are interested in CTI OS support for a peripheral not mentioned here.

This chapter
                           		  provides the following information:

Peripheral-specific equivalents for some common Unified ICM
                                 				terms

A list of
                                 				Unified ICM features that some peripherals do not support

A table of CTI
                                 				call event types that are unavailable for different peripheral types

A table of CTI
                                 				OS client control requests that are unsupported by different peripheral types

Differences and
                                 				limitations in the level of CTI support provided by various
                                 				peripherals—including a list of CTI Server agent states and the corresponding
                                 				terminology/functionality associated with the various peripherals

## General Unified ICM Support

This section describes differences in how various peripherals implement Unified ICM functionality.

### Peripheral-Specific
                           	 Terminology

Different
                                 		  peripheral manufacturers use different terminology for Unified ICM terms such
                                 		  as agents, skill groups, and services. For example, other manufacturers might
                                 		  call a service an application, a split, or a gate. The following table lists
                                 		  several Unified ICM terms and provides peripheral-specific equivalents.

Unified ICM
                                             					 Term

Peripheral-Specific Equivalent

Agent

Agent

Peripheral
                                             					 target

Unified CCE : Agent Target

Others : Trunk group and
                                             					 DNIS 1

Service

Aspect Contact Server :
                                             					 Application

Avaya DEFINITY ECS :
                                             					 Vector Directory Number (VDN)

Avaya Aura CC
                                                						(Symposium) : Application

Skill
                                             					 group

Aspect
                                                						Contact Server : Agent group

Avaya
                                                						DEFINITY ECS : Skill group or hunt group 2

Avaya
                                                						Aura CC (Symposium) : Skill Set

Others : Skill group

Trunk

Aspect
                                                						Contact Server : Instrument 3

Avaya
                                                						Aura CC (Symposium) : None

Others : Trunk

Trunk
                                             					 group

Avaya
                                                						Aura CC (Symposium) : Route

Others : Trunk group

In some
                                 		  cases, the Unified ICM concept is very close to the corresponding ACD feature.
                                 		  For example, the Unified ICM concept of a service is very similar to the Aspect
                                 		  concept of an application. In other cases, the ACD does not have a feature that
                                 		  maps exactly to the Unified ICM feature. In these cases, you might choose a
                                 		  different mapping than shown in the table above. For example, although it might
                                 		  make sense to associate each VDN on a DEFINITY ECS with an Unified ICM service,
                                 		  you could also map each hunt group to a service.

On an
                                 		  Avaya DEFINITY ECS running in EAS mode, each skill group may have multiple
                                 		  subgroups depending on the switch configuration. Unified ICM emulates this by
                                 		  automatically creating additional skill groups for these peripheral types.

#### Unified ICM Feature
                              	 Limitations

Peripheral
                                                   					 Type

Restrictions

Aspect
                                                   					 Contact Server

Only one
                                                   					 skill group assignment per agent

Avaya
                                                   					 DEFINITY ECS

None

Unified CCE  System PG

Does not
                                                   					 support Trunks or Trunk Groups

Avaya Aura
                                                   					 CC (Symposium)

No
                                                   					 Peripheral Service Level reporting

No Trunk
                                                   					 Group Real Time or Trunk Group Half Hour data elements

## CTI OS
                        	 Support

This section
                           		describes how different peripheral types implement and support CTI OS
                           		functionality. It includes the following information:

A table of call
                                 			 event types that are unavailable for different peripheral types

A table of client
                                 			 control requests that are unsupported by different peripheral types

A list of other
                                 			 peripheral-specific differences and limitations

A table of agent
                                 			 states

### Call Events

The
                                 		  following table lists the call events that are not available from different
                                 		  peripheral types:

The entry "none" indicates that the event is available from all supported peripherals.

A single
                                       				asterisk (*) indicates that the event is available from the starred peripheral,
                                       				subject to the restrictions/limitations listed in the Peripheral-Specific Limitations and Differences .

A double
                                       				asterisk (**) indicates that the event is available from Aspect when the PG is
                                       				configured to use the Aspect Event Link.

Unavailable
                                             					 Event

Peripherals

AGENT_PRE_CALL

Aspect,
                                             					 DEFINITY, Avaya Aura CC (Symposium), 
                                             					 IVR

AGENT_PRE_CALL_ABORT

Aspect,
                                             					 DEFINITY, Avaya Aura CC (Symposium), 
                                             					 IVR

AGENT_STATE

None

BEGIN_CALL

None

CALL_
                                             					 CLEARED

Aspect*

CALL_CONFERENCED

Aspect**,IVR

CALL_CONNECTION_ CLEARED

None

CALL_DATA_UPDATE

None

CALL_DELIVERED

Aspect*

CALL_DEQUEUED

DEFINITY,
                                             					 Avaya Aura CC (Symposium), Unified CCE, IVR

CALL_DIVERTED

Aspect,
                                             					 Unified CCE, Avaya Aura CC (Symposium)

CALL_ESTABLISHED

IVR

CALL_FAILED

Aspect,
                                             					 Avaya Aura CC (Symposium), 
                                             					 IVR

CALL_HELD

Aspect**,
                                             					 IVR

CALL_ORIGINATED

Aspect,
                                             					 DEFINITY*, Avaya Aura CC (Symposium)

CALL_QUEUED

Unified CCE, IVR

CALL_REACHED_NETWORK

Aspect,
                                             					 Avaya Aura CC (Symposium),
                                             					 IVR

CALL_RETRIEVED

Aspect**,
                                             					 IVR

CALL_
                                             					 SERVICE_ INITIATED

Aspect**,
                                             					 DEFINITY*, IVR

CALL_TRANSFERRED

IVR

CALL_TRANSLATION_ ROUTE

Unified CCE

END_CALL

None

RTP_STARTED_EVENT

Aspect,
                                             					 Avaya Aura CC (Symposium),
                                             					 IVR

RTP_STOPPED_EVENT

Aspect,
                                             					 Avaya Aura CC (Symposium), 
                                             					 IVR

SYSTEM

None

#### Client Control
                              	 Requests

The
                                    		  following table lists the client control requests that are not supported by the
                                    		  different peripheral types.

Unavailable
                                                					 Request

Peripherals

ALTERNATE_CALL

Avaya Aura
                                                					 CC (Symposium)

ANSWER_CALL

IVR

CLEAR_CALL

IVR

CLEAR_CONNECTION

IVR

CONFERENCE_CALL

IVR

CONSULTATION_CALL

IVR

DEFLECT_CALL

Aspect,
                                                					 Avaya Aura CC (Symposium), 
                                                					 IVR

HOLD_CALL

IVR

MAKE_CALL

IVR

MAKE_PREDICTIVE_ CALL

IVR

QUERY_AGENT_STATE

IVR

QUERY_DEVICE_INFO

IVR

RECONNECT_CALL

IVR

RETRIEVE_CALL

IVR

SEND_DTMF_SIGNAL

Aspect,
                                                					 Avaya Aura CC (Symposium), 
                                                					 IVR

SET_AGENT_STATE

IVR

SNAPSHOT_CALL

IVR

SNAPSHOT_DEVICE

IVR

TRANSFER_CALL

IVR

### Peripheral-Specific Limitations and Differences

This section lists CTI OS-related restrictions and implementation differences for various peripherals.

- MAKE_CALL is only supported when the agent is in the NotReady state for an UCCE peripheral.

MAKE_CALL is not supported for the remaining peripherals supported by CTI OS.

The call continues to be active even after a party is released from the conference.

#### Aspect Contact Server

AgentExtension and AgentInstrument are defined as the port number
                                          				that the teleset is connected to.

Events marked by an asterisk (*) are available when the PG is
                                          				configured to use the Aspect EventLink.

Call Alerting (Call Delivered, LocalConnectionState =
                                          				LCS_ALERTING) is available when the EventLink is used.

Outbound calls on some trunk types do not always provide Call
                                          				Cleared events. Interflow calls that are accepted, but handled by the
                                          				originating site, sometimes also do not provide Call Cleared events.

Outbound calls require that you specify the CallPlacementType in
                                          				an outbound request.

Conference calls can have a maximum of three parties.

In a single-step/blind transfer of a call, the initial call must
                                          				come in over a trunk (be a CCT call) and the dialed number must go to a CCT.

In a regular call transfer, the consult call can be either a CCT
                                          				call or an agent_inside call.

Alternate call operations require that the initial call is a CCT
                                          				call. The second call (consult call) can be either a CCT call or an
                                          				agent_inside call.

In the MAKE_PREDICTIVE_CALL_REQ message, the AnswerDetectControl1
                                          				field must contain the binary value of the Application Bridge AD_PARAM setting,
                                          				and the AnswerDetectControl2 field must contain the binary value of the
                                          				Application Bridge ANS_MAP setting.

Transfer and Conference behavior is modeled after hardphone
                                          				behavior. To initiate a Transfer or a Conference, use the
                                          				MakeCall control (Transfer Init and Conference Init buttons are unavailable) to make a second (consult) call. After you
                                          make this call, the
                                          				Transfer Complete and Conference Complete buttons are available to complete
                                          				the desired action.

#### Avaya DEFINITY
                              	 ECS

AgentExtension
                                          				and AgentInstrument are defined as the station extension.

DEFINITY ECS
                                          				events are the same with or without EAS (Expert Agent Selection).

Both EAS and
                                          				non-EAS versions maintain a list of preconfigured agent groups. When you log in
                                          				with EAS, the agent is automatically logged in to all preconfigured Agent
                                          				groups. When you log in without EAS, the agent is logged in to only those
                                          				groups that you specify in the login request.

The Cisco
                                          				Peripheral Interface Module (PIM)—the Cisco proprietary interface between a
                                          				peripheral and the Peripheral Gateway (PG)—does support call events on inside
                                          				calls only when Unified ICM monitors the agent's station (agent station appears
                                          				in the Unified ICM Peripheral Monitor Table), when the call goes through a
                                          				monitored VDN, or when the call is originated by a CTI MakeCallReq. An agent on
                                          				the switch originates Inside calls. Inside calls include consult calls before a
                                          				transfer or conference. After the transfer or conference completes, you can see
                                          				call events for the merged ACD call.

Auto Answer
                                          				agents must have the phone off the hook or you cannot log in to the agent.
                                          				Manual Answer agents must leave the phone on the hook.

Applications
                                          				must wait a time interval of three times the refresh rate (defined in the Avaya
                                          				Call Management System) between login or logout attempts. Failure to do so may
                                          				cause the PIM to miss the login event and result in a failed call request.

If a third-party
                                          				action fails, an ASAI cause value returns for CTI OS clients that access a
                                          				DEFINITY ECS switch. If you have a copy of the DEFINITY
                                             				  Technical Reference Manual , you can determine the actual
                                          				cause of the failure by performing the following steps:

Refer to the
                                                					 following table of "DEFINITY
                                                   						Cause Values" to obtain the DEFINITY ECS value that corresponds to the
                                                					 returned ASAI cause value.

Refer to the
                                                					 following table "Third-party request/section in DEFINITY manual" to find the
                                                					 chapter of the DEFINITY
                                                   						Technical Reference Manual that discusses the third-party
                                                					 action that you attempted.

Refer to the
                                                					 chapter specified in the table "Third-party request/section in DEFINITY manual" for an
                                                					 explanation of the DEFINITY ECS cause value.

ASAI Value

DEFINITY ECS
                                                					 Value

Cause Value

Description

-MAX_LONG

none

*C_NUSE_LONG

The ECS does
                                                					 not return a value.

0

CS0/28

*C_INVLDNUM

Invalid
                                                					 origination or destination address.

1

CS0/111

*C_PROTERR

Capability
                                                					 sequence was violated or underlying protocol error was detected; the ECS
                                                					 returned an unrecognized value.

2

CS3/40

*C_RESUNAVL

Resources to
                                                					 fulfill service are not available.

3

CS0/50

*C_FACUNSUB

Capability
                                                					 is implemented but not subscribed to by requester.

4

CS3/79

*C_SER_UNIMP

Incompatible
                                                					 options selected.

5

CS0/96

*C_MAND_INFO

One of the
                                                					 required parameters is missing.

6

CS0/100

*C_INVLDIE

Value
                                                					 specified in parameter is not allowed or defined.

7

CS3/63

*C_SERV_UNAVIL

Domain or
                                                					 call is being monitored by another adjunct.

8

CS3/86

*C_CALLID_TERM

Call is no
                                                					 longer in active state.

9

CS0/98

*C_INCOM_ST

Message
                                                					 not compatible with call state.

10

CS0/81

*C_INVALID_CRV

Invalid
                                                					 call identifier (sao_id) also known as cluster_id is used or call does not
                                                					 exist.

11

CS3/80

*C_INCOM_OPT

Incompatible options used to establish the call.

12

CS0/102

*C_REC_TIMER

Timer
                                                					 expired.

13

CS3/15

*C_NOLOGIN

Agent not
                                                					 logged in to split.

14

CS3/11

*C_NOSPLIT_MEM

Agent not
                                                					 member of specified split or split number specified incorrectly.

15

CS0/17

*C_USER_BUSY

Domain or
                                                					 call is being monitored by another adjunct.

16

CS0/18

*C_NOUSE_RESP

Originating address does not respond to service.

17

CS3/43

*C_PERM_DENIED

Permission
                                                					 checks for service have failed.

18

CS3/87

*C_CLUST_TERM

Association terminated because service is not active.

19

CS3/27

*C_OUT_OF_SERV

Domain was
                                                					 removed by administration.

20

CS3/12

*C_INCS_AGT_ST

Agent not
                                                					 in compatible state.

21

CS3/13

*C_MAXLOGIN

Agent
                                                					 logged in to maximum number of splits.

22

CS3/14

*C_INC_PASWD

Invalid
                                                					 login password.

23

CS3/16

*C_AGT_STATE

Request to
                                                					 put agent in the state that the agent is already in.

24

CS3/41

*C_BAD_ADMIN

ACD not
                                                					 provisioned or optioned.

25

CS0/16

*C_NORMAL

General termination; call routed successfully.

26

CS0/42

*C_NETCONJ

Association terminated because of network congestion.

27

CS0/99

*C_BAD_IE

Unknown
                                                					 information element detected.

28

CS3/22

*C_QUEFULL

Queue is
                                                					 full.

29

CS3/42

C_REORDER_
                                                					 DENIAL

Reorder/Denial.

30

CS3/46

C_ADMIN_
                                                					 PROGRESS

Administration is in progress; request cannot be serviced.

31

CS3/53

C_FEATURE_
                                                					 REJECTED

The ECS
                                                					 has rejected a request from the adjunct.

32

CS0/1

C_UNASSIGNED_ NUM

Unassigned
                                                					 number.

33

CS0/21

C_CALL_
                                                					 REJECTED

Call
                                                					 rejected.

34

CS0/22

C_NUM_
                                                					 CHANGED

Number
                                                					 changed.

35

CS0/31

C_NORMAL_
                                                					 UNSPECIF

General, unspecified.

36

CS0/34

C_NO_CIRCUIT

No circuit
                                                					 or channel available.

37

CS0/41

C_TEMP_FAILURE

Temporary
                                                					 Failure.

38

CS0/58

C_BEARER_CAP_ UNAVAIL

Bearer
                                                					 capability not presently available.

39

CS0/88

C_INCOMPAT_ DESTINATION

Incompatible destination.

40

CS0/95

C_INVALID_
                                                					 MESSAGE

Invalid
                                                					 message, unspecified (backward compatibility).

41

CS0/97

C_NON_EXIST_ MESSAGE

Message
                                                					 nonexistent/ not implemented.

42

CS0/127

C_UNSPECIFIED

Unspecified.

43

CS3/19

C_NO_ANSWER

No answer.

44

CS3/20

C_NO_TRUNKS

Trunks not
                                                					 available.

45

CS3/21

C_NO_
                                                					 CLASSIFIERS

Classifiers not available.

46

CS3/30

C_REDIRECT

Redirected.

47

CS3/38

C_NETWORK_
                                                					 OUT_OF_ORDER

Network
                                                					 out of order.

48

Undefined

*C_CAUSE_
                                                					 UNKNOWN

Undefined
                                                					 value returned from the ECS.

49

CS0/52

*C_OUT_CALL_ BARRED

Outgoing
                                                					 call was barred.

50

CS3/23

C_REMAINS_IN_Q

Call
                                                					 remains in queue.

51

CS0/65

C_BEARER_SVC_ NOT_IMPL

Bearer
                                                					 service not implemented.

52

CS3/17

C_TIMED_
                                                					 ANSWER

Assumed
                                                					 answer based on internal timer.

53

CS3/18

C_VOICE_
                                                					 ENERGY_ANSWER

Voice
                                                					 energy detected by the ECS.

54

CS0/82

C_NO_TONE_
                                                					 CHANNEL

Channel or
                                                					 tone do not exist (no tone connected to the specified call).

55

CS3/24

C_ANSWERING_ MACHINE

Answering
                                                					 machine detected.

56

CS0/29

C_FACILITY_ REJECTED

Facility
                                                					 rejected.

57

CS3/25

C_FORWARD_
                                                					 BUSY

Redirection cause.

58

CS3/26

C_COVER_BUSY

Redirection cause.

59

CS3/28

C_COV_DONT_ ANS

Redirection cause.

60

CS3/31

C_FORWARD_ALL

Redirection cause.

61

CS3/8

C_LISTEN_ONLY

Single-Step Conference listen only.

62

CS3/9

C_LISTEN_TALK

Single-Step Conference listen-talk.

For example, an
                                    		  ASAI value of 15 corresponds to the DEFINITY ECS value of CSO/17 (C_USER_BUSY).

Third-party Action or Request

Chapter in
                                                					 Manual

Third-party actions via Call Control: Auto Dial (3PAD), Clear
                                                					 (3PCC), Deflect (Redirect) (3PREDIR), Drop (Selective Drop) (3PSD),
                                                					 Listen-Disconnect, Listen-Reconnect, Selective Hold (3PSH), Make Call (3PMC)
                                                					 (or Predictive Call), Relinquish Control (3PRC), Reconnect (Retrieve) (3PR),
                                                					 Send DTMF (3PSDS), Take Control (3PTC)

Chapter 4:
                                                					 ASAI and Call Control

Third-Party actions via Domain Control: Auto Dial (3PAD), Domain
                                                					 Control (3PDC), Answer (3PANS), Merge (Transfer/Conference) (3PM)

Chapter 5:
                                                					 ASAI and Domain Control

Call
                                                					 Routing (RT_REQ, RT_SEL, RT_END)

Chapter 7:
                                                					 ASAI and Call Routing

Agent
                                                					 State change: Login, Logout, Change Workmode: NotReady (AUX), Ready (AVAIL),
                                                					 WorkReady (ACW), and so forth.) Activating/Canceling Call Forwarding
                                                					 Activating/Canceling Send All Calls

Chapter 8:
                                                					 ASAI and Request Feature Capabilities

Value
                                                					 Queries

Chapter 9:
                                                					 ASAI and Value Query Capabilities

Set Value:
                                                					 Message Waiting Indicator (MWI) Set Billing Type

Chapter
                                                					 10: ASAI and Set Value Capabilities

For example,
                                    		  Chapter 8, "ASAI and Request
                                       			 Feature Capabilities" discusses third-party login requests.

When TSAPI
                                    		  interface of Avaya peripheral is used, PIM maps CSTA error is returned by TSAPI
                                    		  CSTA APIs to ASAI error codes. The following tables display the mapping API by
                                    		  API bases.

CSTA
                                                					 Error Code Returned by TSAPI

ICM CSTA
                                                					 error code

Mapped
                                                					 Cause ASAI Value

INVALID_CSTA_DEVICE_IDENTIFIER (12) - An invalid device identifier or extension
                                                					 is specified in the alerting call.

GENERIC_OPERATION_REJECTION (71)

C_INVLDNUM(0)

[One of
                                                					 the parameters was invalid]

INVALID_CSTA_CONNECTION_IDENTIFIER (13) - An incorrect callID or an incorrect
                                                					 deviceID is specified.

GENERIC_OPERATION_REJECTION (71)

C_INVLDNUM(0)

[ One of
                                                					 the parameters was invalid]

GENERIC_STATE_INCOMPATIBILITY (21) - The station user did not go off-hook
                                                					 within five seconds and cannot be forced off-hook.

GENERIC_OPERATION_REJECTION (71)

C_NOUSE_RESP(16)

[Originating address does not respond to service]

INVALID_OBJECT_STATE (22) - The specified connection at the station is not in
                                                					 alerting, connected, held, or bridged state.

GENERIC_OPERATION_REJECTION (71)

C_INCOM_ST(9)

[Message
                                                					 not compatible with call state]

NO_CALL_TO_ANSWER (28) - The call was redirected to coverage within the
                                                					 five-second interval.

GENERIC_OPERATION_REJECTION (71)

C_INVALID_CRV(10)

[ Invalid
                                                					 call identifier (sao_id), also known as cluster_id is used or call does not
                                                					 exist]

GENERIC_SYSTEM_RESOURCE_ AVAILABILITY (31) - The client attempted to add a
                                                					 seventh party to a call with six active parties.

GENERIC_OPERATION_REJECTION (71)

C_RESUNAVL(40)

[Resources to fulfill service are not available]

RESOURCE_BUSY (33) - The user at the station is busy on a call or there is no
                                                					 idle appearance available.

GENERIC_OPERATION_REJECTION (71)

C_USER_BUSY(15)

[Domain
                                                					 or call is being monitored by another adjunct]

GENERIC_SUBSCRIBED_RESOURCE_ AVAILABILITY (41) - The device identifier
                                                					 specified for alerting a call corresponds to a SIP station and the "Type of
                                                					 3PCC Enabled" for the station is not set to "Avaya".

GENERIC_OPERATION_REJECTION (71)

C_FACUNSUB(3)

[Capability is implemented but not subscribed to by requester]

MISTYPED_ARGUMENT_REJECTION (74) - DYNAMIC_ID is specified in alerting call.

GENERIC_OPERATION_REJECTION (71)

C_SER_UNIMP(4)

[
                                                					 Incompatible options selected]

CSTA
                                                					 Error Code Returned by TSAPI

ICM CSTA
                                                					 error code

Mapped
                                                					 Cause ASAI Value

GENERIC_UNSPECIFIED (0) - The specified data provided for the userInfo parameter exceeds the maximum size. For
                                                					 private data versions 2-5, the maximum length for userInfo is 32 bytes. Beginning with private data
                                                					 version 6, the maximum length was increased to 96 bytes.

GENERIC_OPERATION_REJECTION (71)

C_INVLDIE(6)

[Value
                                                					 specified in parameter is not allowed or defined]

INVALID_OBJECT_STATE (22) - The specified connection at the station is not
                                                					 currently active (is either in alerting or held state) so it cannot be dropped.

GENERIC_OPERATION_REJECTION (71)

C_INCOM_ST(9)

[Message
                                                					 not compatible with call state]

NO_ACTIVE_CALL (24) - The connectionID contained in the request is invalid.
                                                					 CallID may be incorrect too.

GENERIC_OPERATION_REJECTION (71)

C_INVALID_CRV(10)

[ Invalid
                                                					 call identifier (sao_id), also known as cluster_id is used or call does not
                                                					 exist]

NO_CONNECTION_TO_CLEAR (27) - The connectionID contained in the request is
                                                					 invalid. CallID may be correct, but deviceID is wrong.

GENERIC_OPERATION_REJECTION (71)

C_INVLDNUM(0)

[ One of
                                                					 the entered parameters was invalid]

RESOURCE_BUSY (33) - The switch is busy with another CSTA request. This happens
                                                					 when two AE Services servers are issuing requests (Hold Call, Retrieve Call,
                                                					 Clear Connection, and so on) to the same device.

GENERIC_OPERATION_REJECTION (71)

C_USER_BUSY(15)

[Domain
                                                					 or call is being monitored by another adjunct]

CSTA
                                                					 Error Code Returned by TSAPI

ICM CSTA
                                                					 error code

Mapped
                                                					 Cause ASAI Value

INVALID_CSTA_DEVICE_IDENTIFIER (12) - An invalid device identifier or extension
                                                					 is specified in heldCall or activeCall.

GENERIC_OPERATION_REJECTION (71)

C_INVLDNUM(0)

[One of
                                                					 the entered parameters was invalid]

INVALID_CSTA_CONNECTION_IDENTIFIER (13) - The controlling deviceID, inheldCall,
                                                					 or activeCall has not been specified correctly.

GENERIC_OPERATION_REJECTION (71)

C_INVLDNUM(0)

[One of
                                                					 the entered parameters was invalid]

GENERIC_STATE_INCOMPATIBILITY (21) - Both calls are alerting, both calls are
                                                					 being service-observed, or an active call is in a vector processing stage.

GENERIC_OPERATION_REJECTION (71)

C_REORDER_ ENIAL(29)

[Reorder/Denial]

INVALID_OBJECT_STATE (22) - The connections specified in the request are not in
                                                					 valid states for the operation to take place. For example, it does not have one
                                                					 call active and one call in the held state as required.

GENERIC_OPERATION_REJECTION (71)

C_INVLDNUM(0)

[One of
                                                					 the entered parameters was invalid]

RESOURCE_BUSY (33) - The switch is busy with another CSTA request. This can
                                                					 happen when two AE Services servers are issuing requests ( Hold Call, Retrieve
                                                					 Call, Clear Connection, Conference Call, and so on) to the same device.

GENERIC_OPERATION_REJECTION (71)

C_USER_BUSY(15)

[Domain
                                                					 or call is being monitored by another adjunct]

CONFERENCE_MEMBER_LIMIT_EXCEEDED (38) - The request attempted to add a seventh
                                                					 party to an existing six-party conference call. If a station places a six-party
                                                					 conference call on hold and another party adds another station (so that there
                                                					 are again six active parties on the call which is the limit of the
                                                					 Communication Manager), then the station with the call on hold will not be able
                                                					 to retrieve the call.

GENERIC_OPERATION_REJECTION (71)

C_REORDER_DENIAL (29)

[Reorder/Denial]

GENERIC_SUBSCRIBED_RESOURCE_ AVAILABILITY (41) - The device identifier
                                                					 specified in activeCall and heldCall corresponds to a SIP station and the "Type
                                                					 of 3PCC Enabled" for the station is not set to "Avaya".

GENERIC_OPERATION_REJECTION (71)

C_FACUNSUB(3)

[Capability is implemented but not subscribed to by requester]

MISTYPED_ARGUMENT_REJECTION (74) - DYNAMIC_ID is specified inheldCall or
                                                					 activeCall.

GENERIC_OPERATION_REJECTION (71)

C_SER_UNIMP(4)

[Incompatible options selected]

CSTA
                                                					 Error Code Returned by TSAPI

ICM CSTA
                                                					 error code

Mapped
                                                					 Cause ASAI Value

INVALID_CSTA_DEVICE_IDENTIFIER (12) - An invalid device identifier or extension
                                                					 is specified in activeCall.

GENERIC_OPERATION_REJECTION (71)

C_INVLDNUM(0)

[One of
                                                					 the entered parameters was invalid]

INVALID_CSTA_CONNECTION_IDENTIFIER (13) - The connection identifier contained
                                                					 in the request is invalid or does not correspond to a station.

GENERIC_OPERATION_REJECTION (71)

C_INVLDNUM(0)

[One of
                                                					 the entered parameters was invalid]

NO_ACTIVE_CALL (24) - The party to be put on hold is not currently active (for
                                                					 example, in the alerting state) so it cannot be put on hold.

GENERIC_OPERATION_REJECTION (71)

C_INCOM_ST(9)

[Message
                                                					 not compatible with call state]

RESOURCE_BUSY (33) - The switch is busy with another CSTA request. This can
                                                					 happen when two AEI Services servers are issuing requests (Hold Call, Retrieve
                                                					 Call, Clear Connection, and so on) for the same device.

GENERIC_OPERATION_REJECTION (71)

C_USER_BUSY(15)

[Domain
                                                					 or call is being monitored by another adjunct]

GENERIC_SUBSCRIBED_RESOURCE_ AVAILABILITY (41) - The device identifier
                                                					 specified in activeCall corresponds to a SIP station and the "Type of 3PCC
                                                					 Enabled" administered for the station is not set to "Avaya".

GENERIC_OPERATION_REJECTION (71)

C_FACUNSUB(3)

[Capability is implemented but not subscribed to by requester]

OUTSTANDING_REQUEST_LIMIT_ EXCEEDED (44) - The client attempted to put a third
                                                					 party on hold while two parties are on hold already, on an analog station.

GENERIC_OPERATION_REJECTION (71)

C_INCOM_ST(9)

[Message
                                                					 not compatible with call state]

MISTYPED_ARGUMENT_REJECTION (74) - DYNAMIC_ID is specified inactiveCall.

GENERIC_OPERATION_REJECTION (71)

C_SER_UNIMP(4)

[Incompatible options selected]

CSTA
                                                					 Error Code Returned by TSAPI

ICM CSTA
                                                					 error code

Mapped
                                                					 Cause ASAI Value

GENERIC_UNSPECIFIED (0) - The specified data provided for the userInfoparameter
                                                					 exceeds the maximum allowable size. For private data versions 2-5, the maximum
                                                					 length of userInfo is 32 bytes. Beginning with private data version 6, the
                                                					 maximum length of userInfo is 96 bytes.

GENERIC_OPERATION_REJECTION (71)

C_INVLDIE(6)

[Value
                                                					 specified in parameter is not allowed or defined]

INVALID_CALLING_DEVICE (5) - The callingDevice is out of service
                                                					 or not administered correctly in the switch.

GENERIC_OPERATION_REJECTION (71)

C_OUT_OF_SERV(19)

[Domain
                                                					 was removed by Administration]

INVALID_CSTA_DEVICE_IDENTIFIER (12) - An invalid device
                                                					 identifier or extension is specified in callingDevice.

GENERIC_OPERATION_REJECTION (71)

C_INVLDNUM(0)

[One of
                                                					 the entered parameters was invalid]

GENERIC_STATE_INCOMPATIBILITY (21) - The originator does not go off-hook within
                                                					 five seconds after originating the call and cannot be forced off-hook.

GENERIC_OPERATION_REJECTION (71)

C_NOUSE_RESP(16)

[Originating address does not respond to service]

RESOURCE_BUSY (33) - The user is busy on another call and cannot originate this
                                                					 call, or the switch is busy with another CSTA request. This can happen when two
                                                					 AE Services servers are issuing requests ( Hold Call, Retrieve Call, Clear
                                                					 Connection, Make Call, and so on) for the same device.

GENERIC_OPERATION_REJECTION (71)

C_USER_BUSY(15)

[Domain
                                                					 or call is being monitored by another adjunct]

GENERIC_SUBSCRIBED_RESOURCE_ AVAILABILITY (41) - The device identifier
                                                					 specified in callingDevice corresponds to a SIP station and the "Type of 3PCC
                                                					 Enabled" administered for the station is not set to "Avaya".

GENERIC_OPERATION_REJECTION (71)

C_FACUNSUB(3)

[Capability is implemented but not

subscribed to by requester]

CSTA
                                                					 Error Code Returned by TSAPI

ICM CSTA
                                                					 error code

Mapped
                                                					 Cause ASAI Value

INVALID_CSTA_DEVICE_IDENTIFIER (12) - An invalid device identifier or extension
                                                					 is specified in heldCall.

GENERIC_OPERATION_REJECTION (71)

C_INVLDNUM(0)

[Invalid
                                                					 origination or destination address]

INVALID_CSTA_CONNECTION_IDENTIFIER (13) - The connectionID contained in the
                                                					 request is invalid.

GENERIC_OPERATION_REJECTION (71)

C_INVLDNUM(0)

[Invalid
                                                					 origination or destination address]

GENERIC_STATE_INCOMPATIBILITY (21) - The user was on-hook when the request was
                                                					 made and did not go off-hook within five seconds (call remains on hold).

GENERIC_OPERATION_REJECTION (71)

C_NOUSE_RESP(16)

[Originating address does not respond to service]

NO_ACTIVE_CALL (24) - The specified call at the station is cleared and so it
                                                					 cannot be retrieved.

GENERIC_OPERATION_REJECTION (71)

C_INVALID_CRV(10)

[Invalid
                                                					 call identifier (sao_id) also known as cluster_id is used or call does not
                                                					 exist]

NO_HELD_CALL (25) - The specified connection at the station is not in the held
                                                					 state (for example, in the alerting state) and so it cannot be retrieved.

GENERIC_OPERATION_REJECTION (71)

C_INCOM_ST(9)

[Message
                                                					 not compatible with call state]

RESOURCE_BUSY (33) - The switch is busy with another CSTA request. This can
                                                					 happen when two AE Services servers are issuing requests (Hold Call, Retrieve
                                                					 Call, Clear Connection, Conference Call, and so on) for the same device.

GENERIC_OPERATION_REJECTION (71)

C_USER_BUSY(15)

[Domain
                                                					 or call is being monitored by another adjunct]

CONFERENCE_MEMBER_LIMIT_EXCEEDED (38) - The client attempted to add a seventh
                                                					 party to a six-party conference call.

GENERIC_OPERATION_REJECTION (71)

C_RESUNAVL(40)

[Resources to fulfill service are not available]

GENERIC_SUBSCRIBED_RESOURCE_ AVAILABILITY (41) - The device identifier
                                                					 specified in heldCall corresponds to a SIP station and the "Type of 3PCC
                                                					 Enabled" administered for the station is not set to "Avaya".

GENERIC_OPERATION_REJECTION (71)

C_FACUNSUB(3)

[Capability is implemented but not subscribed to by requester]]

MISTYPED_ARGUMENT_REJECTION (74) - DYNAMIC_ID is specified in heldCall.

GENERIC_OPERATION_REJECTION (71)

C_SER_UNIMP(4)

[Incompatible options selected]

CSTA
                                                					 Error Code Returned by TSAPI

ICM CSTA
                                                					 error code

Mapped
                                                					 Cause ASAI Value

INVALID_CSTA_DEVICE_IDENTIFIER (12) - An invalid device identifier or extension
                                                					 was specified in heldCall or activeCall.

GENERIC_OPERATION_REJECTION (71)

C_INVLDNUM(0)

[One of
                                                					 the entered parameters was invalid]

INVALID_CSTA_CONNECTION_IDENTIFIER (13) - The controllingdeviceID in activeCall
                                                					 or heldCall has not been specified correctly.

GENERIC_OPERATION_REJECTION (71)

C_INVLDNUM(0)

[One of
                                                					 the entered parameters was invalid]

Both
                                                         						  calls are alerting

Both
                                                         						  calls are being service-observed

An
                                                         						  active call is in a vector-processing stage

The
                                                         						  Trunk-to-Trunk Transfer feature is not enabled on Avaya Communication Manager

GENERIC_OPERATION_REJECTION (71)

C_REORDER_DENIAL (29)

[Reorder/Denial]

INVALID_OBJECT_STATE (22) - The connections specified in the request are not in
                                                					 valid states for the operation to take place. For example, the transferring
                                                					 device does not have one active call and one held call as required.

GENERIC_OPERATION_REJECTION (71)

C_INCOM_ST(9)

[Message
                                                					 not compatible with call state]

INVALID_CONNECTION_ID_FOR_ACTIVE_ CALL (23) - The callID inactiveCall or
                                                					 heldCall has not been specified correctly.

GENERIC_OPERATION_REJECTION (71)

C_INVLDNUM(0)

[One of
                                                					 the entered parameters was invalid]

RESOURCE_BUSY (33) - The switch is busy with another CSTA request. This can
                                                					 happen when two AE Services servers are issuing requests (Hold Call, Retrieve
                                                					 Call, Clear Connection, Transfer Call, and so on) for the same device.

GENERIC_OPERATION_REJECTION (71)

C_REORDER_ DENIAL(29)

[Reorder/Denial]

GENERIC_SUBSCRIBED_RESOURCE_ AVAILABILITY (41) - The device identifier
                                                					 specified in activeCall and heldCall corresponds to a SIP station and the "Type
                                                					 of 3PCC Enabled" administered for the station is not set to "Avaya".

GENERIC_OPERATION_REJECTION (71)

C_FACUNSUB(3)

[Capability is implemented but not subscribed to by requester]

MISTYPED_ARGUMENT_REJECTION (74) - DYNAMIC_ID is specified in heldCall or
                                                					 activeCall.

GENERIC_OPERATION_REJECTION (71)

C_SER_UNIMP(4)

[Incompatible options selected]

CSTA
                                                					 Error Code Returned by TSAPI

ICM CSTA
                                                					 error code

Mapped
                                                					 Cause ASAI Value

NO_ACTIVE_CALL (24) - The callID of the connectionID specified in the request
                                                					 is invalid.

GENERIC_OPERATION_REJECTION (71)

C_INVALID_CRV(10)

[Invalid
                                                					 call identifier (sao_id) also known as cluster_id is used or call does not
                                                					 exist]

CSTA
                                                					 Error Code Returned by TSAPI

ICM CSTA
                                                					 error code

Mapped
                                                					 Cause ASAI Value

The
                                                         						  request attempted to log out an ACD agent who is already logged out

The
                                                         						  request attempted to log an ACD agent into a split of which they are not a
                                                         						  member

The
                                                         						  request attempted to log in an ACD agent with an incorrect password

The
                                                         						  request attempted to log in an ACD agent at a station where the Auto Answer
                                                         						  feature is enabled, but the station is not off-hook.

GENERIC_UNSPECIFIED (0)

C_NOLOGIN

[for
                                                					 agent logout request when agent not logged in]

C_INC_PASWD(22)

[for
                                                					 agent login request]

C_INCS_AGT_ST

[for any
                                                					 other set agent state requests]

GENERIC_OPERATION (1) - The request attempted to log in an ACD agent that is
                                                					 already logged in.

For TP
                                                					 login Request:

SPECIFIED_EXTENSION_ALREADY_ IN_USE(283) [Other Agent is already logged in on
                                                      						  device]

SPECIFIED_AGENT_ALREADY_ SIGNED_ON(259) [Same Agent is logged on same device]

GENERIC_OPERATION_REJECTION (71) [station not in service]

GENERIC_OPERATION (1)

For TP
                                                					 login Request:

C_CAUSE_ UNKNOWN [Other Agent is already logged in on device/Same Agent is
                                                      						  logged on same device - not to be used]

C_OUT_OF_SERV [Station not in service]

C_AGT_STATE (23) [for all requests other than login]

VALUE_OUT_OF_RANGE (3)

- The workMode private
                                                      						parameter is not valid for the agentMode

The
                                                         						  reason code is outside of the acceptable range (1- 9 or 1-99). (CS0/100)

INVALID_AGENT_WORKMODE [for work-mode change requests]

INVALID_AGENT_REASON_CODE [for logout requests]

C_CAUSE_
                                                					 UNKNOWN

(Not to be
                                                					 used)

OBJECT_NOT_KNOWN (4)

- service request did not
                                                      						specify a valid on-PBX station for the ACD agent in device

agentGroup or device parameters were NULL

agentID parameter was NULL when agentMode was set to AM_LOG_IN

GENERIC_UNSPECIFIED_REJECTION (70)

C_INVLDNUM(0)

[One of
                                                					 the entered parameters was invalid]

INVALID_CSTA_DEVICE_IDENTIFIER (12) - An invalid device identifier has been
                                                					 specified in the device.

GENERIC_UNSPECIFIED_REJECTION (70)

C_INVLDNUM(0)

[One of
                                                					 the entered parameters was invalid]

INVALID_FEATURE (15) - The feature is not available for the agentGroup or the
                                                					 enablePending feature is not available for the switch version.

GENERIC_UNSPECIFIED_REJECTION (70)

C_SERV_UNAVIL(7)

[Domain
                                                					 or call is being monitored by another adjunct]

INVALID_OBJECT_TYPE (18) (CS3/80) - A reason code was specified, but the
                                                					 specified workMode was not WM_AUX_WORK or AM_LOG_OUT.

GENERIC_UNSPECIFIED_REJECTION (70)

C_INCOM_OPT(11)

[Incompatible options used to establish the call]

A work
                                                         						  mode change was requested for a non-ACD agent

The
                                                         						  Agent station is maintenance busy or out of service

GENERIC_UNSPECIFIED_REJECTION (70)

C_MAXLOGIN(21)

[for
                                                					 login requests - Agent logged in to maximum number of splits]

C_INCS_AGT_ST

[for all
                                                					 other requests other than login]

GENERIC_SYSTEM_RESOURCE_ AVAILABILITY (31) - The request cannot complete due to
                                                					 lack of available switch resources.

GENERIC_UNSPECIFIED_REJECTION (70)

C_RESUNAVL(2)

[Resources to fulfill service are not available]

RESOURCE_BUSY (33) - The service attempted to change the state of an ACD agent
                                                					 that is currently on a call.

GENERIC_UNSPECIFIED_REJECTION (70)

C_USER_BUSY(17)

[Domain
                                                					 or call is being monitored by another adjunct]

GENERIC_SUBSCRIBED_RESOURCE_ AVAILABILITY (41) - The device identifier
                                                					 specified in device corresponds to a SIP station and the "Type of 3PCC Enabled"
                                                					 administered for the station is not set to "Avaya".

GENERIC_UNSPECIFIED_REJECTION (70)

C_FACUNSUB(3)

[Capability is implemented but not

subscribed to by requester]

The following
                                    		  errors apply to every CSTA Service that is supported by the TSAPI Service.

CSTA
                                                					 Error Code Returned by TSAPI

ICM CSTA
                                                					 error code

Mapped
                                                					 Cause ASAI Value

GENERIC_UNSPECIFIED (0) - An error has occurred. The TSAPI Service could not
                                                					 provide a specific error value.

GENERIC_UNSPECIFIED (0)

C_CAUSE_
                                                					 UNKNOWN

GENERIC_OPERATION (1) - The CTI protocol is broken d or the service invoked is
                                                					 not consistent with a CTI application association.

GENERIC_OPERATION (1)

C_PROTERR(1)

[Capability sequence was violated or underlying protocol error was detected; an
                                                					 unrecognized value was returned by the ECS]

REQUEST_INCOMPATIBLE_WITH_ OBJECT (2) - The service request does not correspond
                                                					 to a CTI application association.

GENERIC_UNSPECIFIED_REJECTION (70)

C_FEATURE_REJECTED (31)

[The ECS
                                                					 has rejected a request from the adjunct]

VALUE_OUT_OF_RANGE (3) - Communication Manager detects that a required
                                                					 parameter is missing from the request or an out-of-range value has been
                                                					 specified.

GENERIC_UNSPECIFIED_REJECTION (70)

C_MAND_INFO(5)

[One of
                                                					 the required parameters is missing]

OBJECT_NOT_KNOWN (4) - The TSAPI Service detects that a required parameter is
                                                					 missing in the request. For example, the deviceIDof a connectionID is not
                                                					 specified in a service request.

GENERIC_UNSPECIFIED_REJECTION (70)

C_MAND_INFO(5)

[One of
                                                					 the required parameters is missing]

INVALID_FEATURE (15) - The TSAPI Service detects a CSTA Service request that is
                                                					 not supported by Communication Manager.

GENERIC_UNSPECIFIED_REJECTION (70)

C_SERV_UNAVIL(7)

[Domain
                                                					 or call is being monitored by another adjunct]

GENERIC_SYSTEM_RESOURCE_ AVAILABILITY (31) - The request cannot be completed
                                                					 due to lack of available switch resources.

GENERIC_UNSPECIFIED_REJECTION (70)

C_RESUNAVL(2)

[Resources to fulfill service are not available]

RESOURCE_OUT_OF_SERVICE (34) - An application can receive this error code when a single CSTA Service request is ending unusually
                                                due to protocol error.

GENERIC_UNSPECIFIED_REJECTION (70)

C_PROTERR(1)

NETWORK_BUSY (35) - Communication Manager is not accepting the request at this
                                                					 time because of processor overload. The application may wish to retry the
                                                					 request but should not do so immediately.

GENERIC_UNSPECIFIED_REJECTION (70)

C_NETCONJ

GENERIC_SUBSCRIBED_RESOURCE_ AVAILABILITY (41) - The TSAPI Service could not
                                                					 acquire the license(s) needed to satisfy the request.

GENERIC_OPERATION_REJECTION (71)

C_FACUNSUB(3)

[Capability is implemented but not subscribed to by requester]

OUTSTANDING_REQUEST_LIMIT_ EXCEEDED (44) - The given request cannot be
                                                					 processed due to a system resource limit on the device.

GENERIC_OPERATION_REJECTION (71)

C_RESUNAVL(2)

[Resources to fulfill service are not available]

GENERIC_UNSPECIFIED_REJECTION (70) - This is a TSAPI Service internal error,
                                                					 but it cannot be more specific. The system administrator should check the AE
                                                					 Services OAM error logs for more information about this error.

GENERIC_UNSPECIFIED_REJECTION (70)

C_CAUSE_
                                                					 UNKNOWN

GENERIC_OPERATION_REJECTION (71) - This is a TSAPI Service internal error, but
                                                					 not a defined error. The system administrator should check the TSAPI Service
                                                					 error logs for more information about this error.

GENERIC_OPERATION_REJECTION (71)

C_CAUSE_
                                                					 UNKNOWN

DUPLICATE_INVOCATION_REJECTION (72) - The TSAPI Service detects that
                                                					 theinvokeID in the service request is being used by another outstanding service
                                                					 request. This service request is rejected. The outstanding service request with
                                                					 the same invokeID is still valid.

GENERIC_OPERATION_REJECTION (71)

C_SER_UNIMP(4)

[Incompatible options selected]

UNRECOGNIZED_OPERATION_ REJECTION (73) - The TSAPI Service detects that the
                                                					 service request from a client application is not defined in the API. A CSTA
                                                					 request with a 0 or negative invokeID will receive this error.

GENERIC_OPERATION_REJECTION (71)

C_SER_UNIMP(4)

[Incompatible options selected]

RESOURCE_LIMITATION_REJECTION (75) - The TSAPI Service detects that it lacks
                                                					 internal resources such as the memory or data records to process a service
                                                					 request. A system administrator should check the TSAPI Service error logs for
                                                					 more detailed information about this error. This failure may reflect a
                                                					 temporary situation. The application should retry the request.

GENERIC_OPERATION_REJECTION (71)

C_TEMP_FAILURE(37)

[Temporary Failure]

ACS_HANDLE_TERMINATION_REJECTION (76) - The TSAPI Service detects that
                                                					 anacsOpenStream session is terminating. The TSAPI Service sends this error for
                                                					 every outstanding CSTA request of this ACS Handle.

For
                                                					 example, a user may power off the PC before the application issues
                                                					 anacsCloseStream request and waits for the confirmation event. In this case,
                                                					 the acsCloseStream is issued by the TSAPI Service on behalf of the application
                                                					 and there is no application to receive this error. If an application issues
                                                					 anacsCloseStream request and waits for its confirmation event, the application
                                                					 will receive this error for every outstanding request.

GENERIC_OPERATION_REJECTION (71)

C_CAUSE_
                                                					 UNKNOWN

SERVICE_TERMINATION_REJECTION (77) - The TSAPI Service detects that it cannot
                                                					 provide the service due to the failure or shutting down of the communication
                                                					 link between the Telephony Server and Communication Manager. The TSAPI Service
                                                					 sends this error for every outstanding CSTA request that effects every ACS
                                                					 Handle. Although the link is down or Communication Manager is out of service,
                                                					 the TSAPI Service remains loaded and advertised. When the TSAPI Service is in
                                                					 this state, all CSTA Service requests from a client will receive a negative
                                                					 acknowledgment with this error code.

GENERIC_OPERATION_REJECTION (71)

C_CAUSE_
                                                					 UNKNOWN

REQUEST_TIMEOUT_REJECTION (78) - The TSAPI Service did not receive the response
                                                					 of a service request sent to Communication Manager more than 30 seconds ago.
                                                					 The request is canceled and negatively acknowledged with this error code. When
                                                					 this occurs, the communication link between the TSAPI Service and Communication
                                                					 Manager may be out of service or congested. Congestion may occur when TSAPI
                                                					 applications exceed the capacity of the TSAPI Service.

GENERIC_OPERATION_REJECTION (71)

C_REC_TIMER(12)

[Timer
                                                					 expired]

REQUESTS_ON_DEVICE_EXCEEDED_ REJECTION (79) - The TSAPI Service processes one
                                                					 service request at a time for every device. The TSAPI Service queues CSTA
                                                					 requests for a device. Only a limited number of CSTA requests are queued on a
                                                					 device. If this number is exceeded, the incoming client request is negatively
                                                					 acknowledged with this error code. Usually an application sends one request and
                                                					 waits for its completion before it makes another request. The
                                                					 MAX_-REQS_QUEUED_PER_DEVICE parameter has no effect on this class of
                                                					 applications.

Situations
                                                					 of sending a sequence of requests without waiting for their completion are
                                                					 rare. However, if this is the case, set the MAX_REQS_QUEUED_-PER_DEVICE
                                                					 parameter to a proper value. The default value for MAX_-REQS_QUEUED_PER_DEVICE
                                                					 is 4.

GENERIC_OPERATION_REJECTION (71)

C_QUEFULL(28)

[Queue is
                                                					 full]

#### Unified CCE System PG

MAKE_CALL is
                                          				only supported when the agent is in the NotReady state. An agent cannot make
                                          				new calls when in wrapup mode.

Consult and
                                          				blind transfers are supported. However, placing a call on hold, making a new
                                          				call, and then completing the transfer is not supported.

The consult call
                                          				must be in the Talking state before the Transfer/Conference can be completed.
                                          				Therefore, if an Alternate is done in the middle of a Transfer/Conference, the
                                          				operation can only be completed after a second Alternate is done to restore
                                          				status quo.

Completing a
                                          				conference or a transfer to a consulted agent on hold is not supported.

Transferring
                                          				conferences to an unobserved party is not supported.

Overlapping
                                          				transfer and conference consult operations on the same parties are not
                                          				supported. For example, Agent A calls Agent B. During the conversation, Agent A
                                          				must conference consult Agent C. Agent B feels that Agent D has more
                                          				information, so Agent B then transfer consults to Agent D. To end the call,
                                          				Agent A completes the conference and Agent B completes the transfer. This would
                                          				fail.

Only the
                                          				conference initiator can add parties to the conference.

Calls do not get
                                          				queued at the Unified CM but instead at some queue point. Because of this,
                                          				skill group queue statistics are not available via the
                                          				QUERY_SKILL_GROUP_STATISTICS_REQ. CTI can monitor service controlled VRUs to
                                          				get queued and dequeued events, as well as established events.

RTP_STARTED_EVENT and RTP_STOPPED_EVENT are particular to
                                          				Unified CCE to support recording vendors.

AGENT_PRECALL_EVENT and AGENT_PRECALL_ABORT_EVENT are particular
                                          				to Unified CCE. They provide call context data before the routed call arrives.

A
                                          				CALL_CONNECTION_CLEARED_EVENT may be received with a cause of CEC_REDIRECTED
                                          				for the following cases:

Agent calls
                                                					 a CTI Route Point and call is directed to another resource

Agent calls
                                                					 an VRU and the VRU redirects the call

Agent calls
                                                					 a number with a forwarding option turned on

You can only
                                          				monitor devices that have agents logged in via CTI OS. The Unified ICM
                                          				Peripheral Monitor Table is not supported for the Unified CCE PG.

The Unified CM
                                          				Shared line feature (agents share the same extension) is not supported.

Agent Desk
                                          				Settings control some agent behaviors. These are configured in Unified ICM and
                                          				downloaded by the agent desktop upon startup. WrapupInMode is the wrapup mode
                                          				variable for incoming calls and WrapupOutMode is the wrapup mode variable for
                                          				outgoing calls. The valid values for these parameters are:

REQUIRED

For either
                                                					 incoming or outgoing calls, the agent has no option but to go to the Wrapup
                                                					 state when a call ends. While the agent is on the call, all agent state buttons
                                                					 are disabled. While the agent is in the wrapup state, the Ready and NotReady
                                                					 buttons must be enabled.

Clicking
                                                					 either the Ready or NotReady buttons must dismiss the Wrapup dialog box and put
                                                					 the agent in the state that was chosen. However, if the wrapup timer was
                                                					 enabled in the PG configuration and timeout occurs before an agent state is
                                                					 chosen, the agent state automatically changes as follows:

If the
                                                      						  timeout occurred at the end of an incoming call, the agent state changes to
                                                      						  Ready.

If the
                                                      						  timeout occurred at the end of an outgoing call, the agent state changes to
                                                      						  NotReady.

REQUIRED_WITH_DATA

The same as
                                                					 REQUIRED, but the agent must input some data into the Wrapup dialog box before
                                                					 exiting the dialog box and going to a Ready or NotReady state. This applies
                                                					 only to WrapupInMode.

OPTIONAL

For either
                                                					 incoming or outgoing calls, the agent can only enter any after call
                                                					 state—Wrapup, Ready or NotReady—by clicking the appropriate button.

NOT_ALLOWED

For either
                                                					 incoming or outgoing calls, the agent is only able to enter the Ready or
                                                					 NotReady states. The wrapup button is disabled.

Points of
                                    		  note for API users:

If the wrapup
                                          				mode is REQUIRED_WITH_DATA, SetAgentState for returning to ready or not ready
                                          				fails with an error code of CF_WRAPUP_DATA_REQUIRED (280) if there is no wrapup
                                          				data entered into a call.

If Logout Reason
                                          				or NotReady Reasons are required, an error of CF_REASON_CODE_REQUIRED (281) is
                                          				received if the reasons are not assigned in set agent state request. You must
                                          				also create Logout Reason and NotReady Reason dialog boxes in the Reason Code
                                          				if you require these properties.

For more
                                    		  information about reason code and wrapup modes, see the Administration Guide for Cisco Unified Contact Center Enterprise .

The PG also uses
                                          				the Supervisor Interface periodically to interrogate the switch to examine
                                          				agent configuration change. The period interval is controlled by the Windows
                                          				Registry entry "MonitorGroupTimerQuery" . If there is an agent skill group
                                          				assignment change, the PG knows only when it next interrogates the switch.

### UCCE Error Codes

The following table provides a brief description of the
                                 		  error message and what they indicate.

Error

Indicates

PERERR_TELDRIVE

The telephony driver layer generated the error.

PERERR_JTCLIENT

The JTAPI client generated the error.

PERERR_JTAPPLAY

The JTAPI application layer generated the error.

PERERR_GW_E

The JTAPI gateway generated the error.

PERERR_CM

Cisco Unified Communications Manager generated the error.

The following table lists error codes and their
                                 		  descriptions.

Some of these values appear over two lines due to space
                                             			 limitations.

Return Value/ Code

Error Message

Description

Got an exception on a call to "transfer" with the ACTIVE call
                                             					 specified (method "run" in class ThreadTransferCall).

#### Avaya Aura CC (Symposium)

The Peripheral Gateway (and thus CTI OS clients) do
                                          				not receive a CallEstablished Event for an off-switch call. As a result of this
                                          				limitation, some features—such as blind conference or transfer operation
                                          				off-switch—are not supported. The soft phone receives no notification that the
                                          				call has been connected off-switch, and thus the application requires manual
                                          				intervention from the agent (who heard a dial-tone, a ring, or an answer, and
                                          				so forth) before completing the conference or transfer operation.

The Transfer button is not enabled after an off-switch consult.

Single-step/blind transfer or conference is not supported.
                                          				Transfer and conference calls must be consultative.

Consultative Transfer to a supervisor is not supported.

Users cannot transfer to an AgentID.

Users cannot put a conference or consultative call on hold,
                                          				therefore the button is disabled.

There is a delay when switching from the NotReady state to the
                                          				Ready state.

There is no equivalent to the AACC state WalkAway. The ACD
                                          				gives a NOT_READY state to Unified ICM, but the switch rejects a request to set
                                          				WalkAway to Not_Ready.

Third-party call control and agent control requests issued through
                                          				the CTI Server interface sometimes return a Peripheral error code in the
                                          				failure indication message if the request fails. For the Avaya Aura CC (Symposium), this
                                          				Peripheral error code is either a Status value or a Cause value. Generally,
                                          				Status values are returned for call requests such as MakeCall and Cause values
                                          				are returned for agent control requests such as SetAgentState. The Avaya Aura CC (Symposium) Status and Cause values are
                                          defined in the two following tables.

The ALTERNATE_CALL request is not supported with
                                          				the Avaya Aura CC (Symposium) (for more information, see Call Events ).

Status Value (hex/dec)

Description

Invalid Parameters

0A00 / 2560

Invalid calling TN

0A01 / 2561

Invalid calling DN; wrong DN specified

0A02 / 2562

Incomplete calling DN

0A03 / 2563

Invalid called DN

0A04 / 2564

Incomplete called DN

0A05 / 2565

Invalid called TN

0A06 / 2566

Invalid origination manner

0A07 / 2567

Invalid destination manner

0A08 / 2568

Invalid origination user type

0A09 / 2569

Invalid customer number

0A0A / 2570

System or data base error

Unsuccessful Call Origination

0B00 / 2816

Origination party busy

0B01 / 2817

Origination resource blocking

0B02 / 2818

Origination set is maintenance busy

0B03 / 2819

500/2500 set is onhook

0B04 / 2820

Origination DN busy

0B05 / 2821

Origination is ringing

0B06 / 2822

Unable to disconnect origination (that is, already
                                                					 disconnected)

0B07 / 2823

Origination access restriction blocking

0B08 / 2824

Origination call on permanent hold

0B0A / 2826

System or data base error

0B0B / 2827

Origination receiving end to end signaling

0B0C / 2828

The call is currently in an ACD queue

0B0E / 2830

Origination set invoked hold

0B14 / 2836

Transfer key not configured

0B15 / 2837

Transfer key not idle

0B16 / 2838

Set active in conference call

0B17 / 2839

Transfer or MPO/TSA class of service not configured

0B18 / 2840

Cannot put call on hold

0B1D / 2845

No active call exists on set

0B1E / 2846

No held call exists on set

Unsuccessful Call Termination

0C00 / 3072

Terminating party is busy

0C01 / 3073

Destination resource blocking

0C02 / 3074

Destination in invalid state

0C07 / 3079

Destination access restriction blocking

0D0A / 3338

System or database error

Network Interceptions

0C08 / 3080

Unassigned number

0C09 / 3081

No route to destination

0C0A / 3082

No user responding

0C0B / 3083

Number changed

0C0C / 3084

Destination out of service

0C0D / 3085

Invalid number format

0C0E / 3086

No circuit available

0C0F / 3087

Network out of order

0C10 / 3088

Temporary failure

0C11 / 3089

Equipment congestion

Network Interceptions with In-Band Information

0C19 / 3097

Terminating party is busy

0C1A / 3098

Unassigned number

0C1B / 3099

No route to destination

0C1C / 3100

No user responding

0C1D / 3101

Number changed

0C1E / 3102

Destination out of service

0C1F / 3103

Invalid number format

0C20 / 3104

No circuit available

0C21 / 3105

Network out of order

0C22 / 3106

Temporary failure

0C23 / 3107

Equipment congestion

0C24 / 3108

Interworking, unspecified

0CFE / 3326

Other cause

Unsuccessful Conference or Transfer Operation

0D00 / 3328

Cannot complete conference

0D01 / 3329

Cannot initiate transfer

0D02 / 3330

Cannot complete transfer

0D03 / 3331

Cannot retrieve original call

0D04 / 3332

Fast Transfer initiation failed

0D05 / 3333

Fast Transfer completion failed

0D0B / 3339

Hold Request failed

Cause Value (hex/dec)

Description

1002 / 4098

Access restricted

1003 / 4099

Resource unavailable

1004 / 4100

Invalid customer number

1005 / 4101

Invalid origination address

1006 / 4102

Invalid destination address

1007 / 4103

Invalid manner

1008 / 4104

Unsuccessful retrieve original

1009 / 4105

Unsuccessful transfer

100A / 4106

Unsuccessful conference

100B / 4107

Unsuccessful answer request

100C / 4108

Unsuccessful release request

1070 / 4208

Refer to Connection Status IE

2004 / 8196

The target DN is invalid

2005 / 8197

The target DN is not AST

2006 / 8198

The Customer Number is invalid

2007 / 8199

The feature could not be invoked

2008 / 8200

The feature is not configured on the set

2009 / 8201

The requested feature is out of valid range

200A / 8202

The target set is not ACD agent

200B / 8203

The target set is a Virtual Agent

200C / 8204

The set is maintenance busy

200D / 8205

Set is in wrong state for invocation

200E / 8206

Set is in target state

200F / 8207

No NRDY/RDY while ACD set is logged out

2010 / 8208

Package C customer cannot use NRDY with IDN call

2011 / 8209

Feature IE is missing or invalid

2012 / 8210

DN IE is missing or invalid

2013 / 8211

Agent ID IE is missing or invalid

2014 / 8212

Agent ID is invalid

2015 / 8213

CFW DN IE is invalid

2016 / 8214

The Call Forward DN is too long

2017 / 8215

The Call Forward DN is invalid

2018 / 8216

User is invoking Call Forward

2019 / 8217

MSB/MSI not supported for 500/2500 sets

201A / 8218

500/2500 ACD agent already changed status

201B / 8219

500/2500 ACD agent set is being rung

201C / 8220

User is manually logging in 500 /2500 ACD set

##### Swap Feature in Avaya Aura Contact Center (Symposium) ACD

The Swap feature enables the agents to swap or alternate
                                       		  between customer calls and consult calls, both from hardphones as well as
                                       		  softphones.

The Swap feature deploys a CTI toolbar with Unified ICM,
                                       		  offering most of the phone set functionalities. One of the most important
                                       		  functionalities is that it allows the agent to swap or alternate between
                                       		  primary and consult calls during a Consultation Call.

The agent performing the transfer must carry out a swap, or
                                       		  alternate between the primary key (ACD or DN) and the secondary key of
                                       		  transfer. On the phone set, an agent can perform a swap by using the transfer or
                                       		  primary key of the used line (ACD or DN).

The Swap feature is
                                                   			 not supported when CTI OS is used with the Avay Aura Contact Center (Symposium).

###### Dependencies and Patches for Swap Feature Support in
                                       		  Softphones and Hardphones

The following patches are required for Swap feature
                                       		  support.

Symposium SCCS 5.0:

SU 05

SUS0501/02/03

NN_SCCS_5.0_DP_050302_S (mandatory)

NN_SCCS_5.0_DP_050301_S (optional)

NCCM 6.0:

SU03

SUS0301

PEP_030130_RU

Nortel CS1000 Succession 4.0 or 4.5:

MPLR20429

MPLR21764

##### Enabling Swap Feature on Unified ICM

You can enable the Swap feature with the help of Config REGISTRY Key called NortelSwapPatchInstalled. This key is created
                                       when you install the patch. Set the value of this registry key to 1 before starting the PG.

If there are multiple instances of the Avaya Aura Contact Center PG in the same box, you must set the registry NortelSwapPatchInstalled
                                       to 1 for all the PG instances. This allows the CTI OS Server to enable the alternate button on the client desktop.

### Agent States

This
                                 		  section presents the agent-state terminology and functionality used by CTI OS
                                 		  Server and how it corresponds to the terminology and functionality of various
                                 		  call center peripherals.

State

Peripheral-Specific Equivalent

Available

The agent is
                                             					 ready to accept a call.

Aspect Contact Server: Avail

Avaya DEFINITY ECS: AVAIL

Avaya Aura CC
                                                						(Symposium): Idle

BusyOther

The agent is
                                             					 busy performing a task associated with another active Skill Group.

Aspect Contact Server: MSG (if Aspect Event Link is not being used)

Avaya DEFINITY ECS: OTHER

Avaya Aura CC
                                                						(Symposium): No equivalent

Hold

The agent
                                             					 currently has all calls on hold.

Aspect Contact Server: HOLD

Avaya DEFINITY ECS: No
                                             					 equivalent

Avaya Aura CC (Symposium): On Hold, On Hold Walkaway

Login

The agent
                                             					 has logged in to the ACD. It does not necessarily indicate that the agent is
                                             					 ready to accept calls.

Although
                                             					 viewed as a state by CTI Server, this state is more of an event, and
                                             					 is not treated as a state by the switches.

Logout

The agent
                                             					 has logged out of the ACD and cannot accept any additional calls.

Aspect Contact Server: Signed Off

Avaya DEFINITY ECS: No
                                             					 equivalent

Avaya Aura CC
                                                						(Symposium): Logout

NotReady

The agent is
                                             					 logged in but is unavailable for any call work.

Aspect Contact Server: Idle

Avaya DEFINITY ECS: AUX

Avaya Aura CC
                                                						(Symposium): Not Ready Walkaway (however, this state requires the agent to click
                                             					 Hold and physically unplug the headset – because a physical act is involved, a
                                             					 software request to set the agent state to NotReady fails), Emergency

Reserved

The agent
                                             					 is reserved for a call that arrives at the ACD shortly.

Aspect
                                                						Contact Server: RSVD

Avaya
                                                						DEFINITY ECS: No equivalent

Avaya
                                                						Aura CC (Symposium): Call Presented

Talking

The agent
                                             					 is currently talking on a call (inbound, outbound, or inside).

Aspect
                                                						Contact Server: Talking ACD1, Talking ACD2, Talking ACT1, Talking ACT2,
                                             					 Talking Out1, Talking Out2, Talking Inside, Supervisor Line, MSG, HELP (MSG and
                                             					 HELP correspond to Talking only if Aspect Event Link is being used.)

Avaya
                                                						DEFINITY ECS: AUX-IN, AUX-OUT, ACD-IN, ACD-OUT, ACW-IN, ACW-OUT, DACD

Avaya
                                                						Aura CC (Symposium): Active, Consultation

Unknown

The agent
                                             					 state is currently unknown.

Aspect
                                                						Contact Server: No equivalent

Avaya
                                                						DEFINITY ECS: UNKNOWN

Avaya
                                                						Aura CC (Symposium): No equivalent

WorkNotReady

The agent
                                             					 is performing after-call work and is not ready to receive a call after the work
                                             					 is complete.

Aspect
                                                						Contact Server: No equivalent

Avaya
                                                						DEFINITY ECS: No equivalent

Avaya
                                                						Aura CC (Symposium): No equivalent

WorkReady

The agent
                                             					 is performing after-call work and is ready to receive a call after the work is
                                             					 complete.

Aspect
                                                						Contact Server: Wrap-up

Avaya
                                                						DEFINITY ECS: ACW, DACW

Avaya
                                                						Aura CC (Symposium): Not Ready, Break, Busy

| Note | The peripherals
                                       			 mentioned in this chapter are the ones that CTI OS supports. Please contact Cisco CTI Product Management
                                       			 if you are interested in CTI OS support for a peripheral not mentioned here. |
|---|---|

| Unified ICM
                                             					 Term | Peripheral-Specific Equivalent |
|---|---|
| Agent | Agent |
| Peripheral
                                             					 target | Unified CCE : Agent Target Others : Trunk group and
                                             					 DNIS 1 |
| Service | Aspect Contact Server :
                                             					 Application Avaya DEFINITY ECS :
                                             					 Vector Directory Number (VDN) Avaya Aura CC
                                                						(Symposium) : Application |
| Skill
                                             					 group | Aspect
                                                						Contact Server : Agent group Avaya
                                                						DEFINITY ECS : Skill group or hunt group 2 Avaya
                                                						Aura CC (Symposium) : Skill Set Others : Skill group |
| Trunk | Aspect
                                                						Contact Server : Instrument 3 Avaya
                                                						Aura CC (Symposium) : None Others : Trunk |
| Trunk
                                             					 group | Avaya
                                                						Aura CC (Symposium) : Route Others : Trunk group |

| Peripheral
                                                   					 Type | Restrictions |
|---|---|
| Aspect
                                                   					 Contact Server | Only one
                                                   					 skill group assignment per agent |
| Avaya
                                                   					 DEFINITY ECS | None |
| Unified CCE  System PG | Does not
                                                   					 support Trunks or Trunk Groups |
| Avaya Aura
                                                   					 CC (Symposium) | No
                                                   					 Peripheral Service Level reporting No Trunk
                                                   					 Group Real Time or Trunk Group Half Hour data elements |

| Unavailable
                                             					 Event | Peripherals |
|---|---|
| AGENT_PRE_CALL | Aspect,
                                             					 DEFINITY, Avaya Aura CC (Symposium), 
                                             					 IVR |
| AGENT_PRE_CALL_ABORT | Aspect,
                                             					 DEFINITY, Avaya Aura CC (Symposium), 
                                             					 IVR |
| AGENT_STATE | None |
| BEGIN_CALL | None |
| CALL_
                                             					 CLEARED | Aspect* |
| CALL_CONFERENCED | Aspect**,IVR |
| CALL_CONNECTION_ CLEARED | None |
| CALL_DATA_UPDATE | None |
| CALL_DELIVERED | Aspect* |
| CALL_DEQUEUED | DEFINITY,
                                             					 Avaya Aura CC (Symposium), Unified CCE, IVR |
| CALL_DIVERTED | Aspect,
                                             					 Unified CCE, Avaya Aura CC (Symposium) |
| CALL_ESTABLISHED | IVR |
| CALL_FAILED | Aspect,
                                             					 Avaya Aura CC (Symposium), 
                                             					 IVR |
| CALL_HELD | Aspect**,
                                             					 IVR |
| CALL_ORIGINATED | Aspect,
                                             					 DEFINITY*, Avaya Aura CC (Symposium) |
| CALL_QUEUED | Unified CCE, IVR |
| CALL_REACHED_NETWORK | Aspect,
                                             					 Avaya Aura CC (Symposium),
                                             					 IVR |
| CALL_RETRIEVED | Aspect**,
                                             					 IVR |
| CALL_
                                             					 SERVICE_ INITIATED | Aspect**,
                                             					 DEFINITY*, IVR |
| CALL_TRANSFERRED | IVR |
| CALL_TRANSLATION_ ROUTE | Unified CCE |
| END_CALL | None |
| RTP_STARTED_EVENT | Aspect,
                                             					 Avaya Aura CC (Symposium),
                                             					 IVR |
| RTP_STOPPED_EVENT | Aspect,
                                             					 Avaya Aura CC (Symposium), 
                                             					 IVR |
| SYSTEM | None |

| Unavailable
                                                					 Request | Peripherals |
|---|---|
| ALTERNATE_CALL | Avaya Aura
                                                					 CC (Symposium) |
| ANSWER_CALL | IVR |
| CLEAR_CALL | IVR |
| CLEAR_CONNECTION | IVR |
| CONFERENCE_CALL | IVR |
| CONSULTATION_CALL | IVR |
| DEFLECT_CALL | Aspect,
                                                					 Avaya Aura CC (Symposium), 
                                                					 IVR |
| HOLD_CALL | IVR |
| MAKE_CALL | IVR |
| MAKE_PREDICTIVE_ CALL | IVR |
| QUERY_AGENT_STATE | IVR |
| QUERY_DEVICE_INFO | IVR |
| RECONNECT_CALL | IVR |
| RETRIEVE_CALL | IVR |
| SEND_DTMF_SIGNAL | Aspect,
                                                					 Avaya Aura CC (Symposium), 
                                                					 IVR |
| SET_AGENT_STATE | IVR |
| SNAPSHOT_CALL | IVR |
| SNAPSHOT_DEVICE | IVR |
| TRANSFER_CALL | IVR |

| Note | MAKE_CALL is only supported when the agent is in the NotReady state for an UCCE peripheral. MAKE_CALL is not supported for the remaining peripherals supported by CTI OS. The call continues to be active even after a party is released from the conference. |
|---|---|

| ASAI Value | DEFINITY ECS
                                                					 Value | Cause Value | Description |
|---|---|---|---|
| -MAX_LONG | none | *C_NUSE_LONG | The ECS does
                                                					 not return a value. |
| 0 | CS0/28 | *C_INVLDNUM | Invalid
                                                					 origination or destination address. |
| 1 | CS0/111 | *C_PROTERR | Capability
                                                					 sequence was violated or underlying protocol error was detected; the ECS
                                                					 returned an unrecognized value. |
| 2 | CS3/40 | *C_RESUNAVL | Resources to
                                                					 fulfill service are not available. |
| 3 | CS0/50 | *C_FACUNSUB | Capability
                                                					 is implemented but not subscribed to by requester. |
| 4 | CS3/79 | *C_SER_UNIMP | Incompatible
                                                					 options selected. |
| 5 | CS0/96 | *C_MAND_INFO | One of the
                                                					 required parameters is missing. |
| 6 | CS0/100 | *C_INVLDIE | Value
                                                					 specified in parameter is not allowed or defined. |
| 7 | CS3/63 | *C_SERV_UNAVIL | Domain or
                                                					 call is being monitored by another adjunct. |
| 8 | CS3/86 | *C_CALLID_TERM | Call is no
                                                					 longer in active state. |
| 9 | CS0/98 | *C_INCOM_ST | Message
                                                					 not compatible with call state. |
| 10 | CS0/81 | *C_INVALID_CRV | Invalid
                                                					 call identifier (sao_id) also known as cluster_id is used or call does not
                                                					 exist. |
| 11 | CS3/80 | *C_INCOM_OPT | Incompatible options used to establish the call. |
| 12 | CS0/102 | *C_REC_TIMER | Timer
                                                					 expired. |
| 13 | CS3/15 | *C_NOLOGIN | Agent not
                                                					 logged in to split. |
| 14 | CS3/11 | *C_NOSPLIT_MEM | Agent not
                                                					 member of specified split or split number specified incorrectly. |
| 15 | CS0/17 | *C_USER_BUSY | Domain or
                                                					 call is being monitored by another adjunct. |
| 16 | CS0/18 | *C_NOUSE_RESP | Originating address does not respond to service. |
| 17 | CS3/43 | *C_PERM_DENIED | Permission
                                                					 checks for service have failed. |
| 18 | CS3/87 | *C_CLUST_TERM | Association terminated because service is not active. |
| 19 | CS3/27 | *C_OUT_OF_SERV | Domain was
                                                					 removed by administration. |
| 20 | CS3/12 | *C_INCS_AGT_ST | Agent not
                                                					 in compatible state. |
| 21 | CS3/13 | *C_MAXLOGIN | Agent
                                                					 logged in to maximum number of splits. |
| 22 | CS3/14 | *C_INC_PASWD | Invalid
                                                					 login password. |
| 23 | CS3/16 | *C_AGT_STATE | Request to
                                                					 put agent in the state that the agent is already in. |
| 24 | CS3/41 | *C_BAD_ADMIN | ACD not
                                                					 provisioned or optioned. |
| 25 | CS0/16 | *C_NORMAL | General termination; call routed successfully. |
| 26 | CS0/42 | *C_NETCONJ | Association terminated because of network congestion. |
| 27 | CS0/99 | *C_BAD_IE | Unknown
                                                					 information element detected. |
| 28 | CS3/22 | *C_QUEFULL | Queue is
                                                					 full. |
| 29 | CS3/42 | C_REORDER_
                                                					 DENIAL | Reorder/Denial. |
| 30 | CS3/46 | C_ADMIN_
                                                					 PROGRESS | Administration is in progress; request cannot be serviced. |
| 31 | CS3/53 | C_FEATURE_
                                                					 REJECTED | The ECS
                                                					 has rejected a request from the adjunct. |
| 32 | CS0/1 | C_UNASSIGNED_ NUM | Unassigned
                                                					 number. |
| 33 | CS0/21 | C_CALL_
                                                					 REJECTED | Call
                                                					 rejected. |
| 34 | CS0/22 | C_NUM_
                                                					 CHANGED | Number
                                                					 changed. |
| 35 | CS0/31 | C_NORMAL_
                                                					 UNSPECIF | General, unspecified. |
| 36 | CS0/34 | C_NO_CIRCUIT | No circuit
                                                					 or channel available. |
| 37 | CS0/41 | C_TEMP_FAILURE | Temporary
                                                					 Failure. |
| 38 | CS0/58 | C_BEARER_CAP_ UNAVAIL | Bearer
                                                					 capability not presently available. |
| 39 | CS0/88 | C_INCOMPAT_ DESTINATION | Incompatible destination. |
| 40 | CS0/95 | C_INVALID_
                                                					 MESSAGE | Invalid
                                                					 message, unspecified (backward compatibility). |
| 41 | CS0/97 | C_NON_EXIST_ MESSAGE | Message
                                                					 nonexistent/ not implemented. |
| 42 | CS0/127 | C_UNSPECIFIED | Unspecified. |
| 43 | CS3/19 | C_NO_ANSWER | No answer. |
| 44 | CS3/20 | C_NO_TRUNKS | Trunks not
                                                					 available. |
| 45 | CS3/21 | C_NO_
                                                					 CLASSIFIERS | Classifiers not available. |
| 46 | CS3/30 | C_REDIRECT | Redirected. |
| 47 | CS3/38 | C_NETWORK_
                                                					 OUT_OF_ORDER | Network
                                                					 out of order. |
| 48 | Undefined | *C_CAUSE_
                                                					 UNKNOWN | Undefined
                                                					 value returned from the ECS. |
| 49 | CS0/52 | *C_OUT_CALL_ BARRED | Outgoing
                                                					 call was barred. |
| 50 | CS3/23 | C_REMAINS_IN_Q | Call
                                                					 remains in queue. |
| 51 | CS0/65 | C_BEARER_SVC_ NOT_IMPL | Bearer
                                                					 service not implemented. |
| 52 | CS3/17 | C_TIMED_
                                                					 ANSWER | Assumed
                                                					 answer based on internal timer. |
| 53 | CS3/18 | C_VOICE_
                                                					 ENERGY_ANSWER | Voice
                                                					 energy detected by the ECS. |
| 54 | CS0/82 | C_NO_TONE_
                                                					 CHANNEL | Channel or
                                                					 tone do not exist (no tone connected to the specified call). |
| 55 | CS3/24 | C_ANSWERING_ MACHINE | Answering
                                                					 machine detected. |
| 56 | CS0/29 | C_FACILITY_ REJECTED | Facility
                                                					 rejected. |
| 57 | CS3/25 | C_FORWARD_
                                                					 BUSY | Redirection cause. |
| 58 | CS3/26 | C_COVER_BUSY | Redirection cause. |
| 59 | CS3/28 | C_COV_DONT_ ANS | Redirection cause. |
| 60 | CS3/31 | C_FORWARD_ALL | Redirection cause. |
| 61 | CS3/8 | C_LISTEN_ONLY | Single-Step Conference listen only. |
| 62 | CS3/9 | C_LISTEN_TALK | Single-Step Conference listen-talk. |

| Third-party Action or Request | Chapter in
                                                					 Manual |
|---|---|
| Third-party actions via Call Control: Auto Dial (3PAD), Clear
                                                					 (3PCC), Deflect (Redirect) (3PREDIR), Drop (Selective Drop) (3PSD),
                                                					 Listen-Disconnect, Listen-Reconnect, Selective Hold (3PSH), Make Call (3PMC)
                                                					 (or Predictive Call), Relinquish Control (3PRC), Reconnect (Retrieve) (3PR),
                                                					 Send DTMF (3PSDS), Take Control (3PTC) | Chapter 4:
                                                					 ASAI and Call Control |
| Third-Party actions via Domain Control: Auto Dial (3PAD), Domain
                                                					 Control (3PDC), Answer (3PANS), Merge (Transfer/Conference) (3PM) | Chapter 5:
                                                					 ASAI and Domain Control |
| Call
                                                					 Routing (RT_REQ, RT_SEL, RT_END) | Chapter 7:
                                                					 ASAI and Call Routing |
| Agent
                                                					 State change: Login, Logout, Change Workmode: NotReady (AUX), Ready (AVAIL),
                                                					 WorkReady (ACW), and so forth.) Activating/Canceling Call Forwarding
                                                					 Activating/Canceling Send All Calls | Chapter 8:
                                                					 ASAI and Request Feature Capabilities |
| Value
                                                					 Queries | Chapter 9:
                                                					 ASAI and Value Query Capabilities |
| Set Value:
                                                					 Message Waiting Indicator (MWI) Set Billing Type | Chapter
                                                					 10: ASAI and Set Value Capabilities |

| CSTA
                                                					 Error Code Returned by TSAPI | ICM CSTA
                                                					 error code | Mapped
                                                					 Cause ASAI Value |
|---|---|---|
| INVALID_CSTA_DEVICE_IDENTIFIER (12) - An invalid device identifier or extension
                                                					 is specified in the alerting call. | GENERIC_OPERATION_REJECTION (71) | C_INVLDNUM(0) [One of
                                                					 the parameters was invalid] |
| INVALID_CSTA_CONNECTION_IDENTIFIER (13) - An incorrect callID or an incorrect
                                                					 deviceID is specified. | GENERIC_OPERATION_REJECTION (71) | C_INVLDNUM(0) [ One of
                                                					 the parameters was invalid] |
| GENERIC_STATE_INCOMPATIBILITY (21) - The station user did not go off-hook
                                                					 within five seconds and cannot be forced off-hook. | GENERIC_OPERATION_REJECTION (71) | C_NOUSE_RESP(16) [Originating address does not respond to service] |
| INVALID_OBJECT_STATE (22) - The specified connection at the station is not in
                                                					 alerting, connected, held, or bridged state. | GENERIC_OPERATION_REJECTION (71) | C_INCOM_ST(9) [Message
                                                					 not compatible with call state] |
| NO_CALL_TO_ANSWER (28) - The call was redirected to coverage within the
                                                					 five-second interval. | GENERIC_OPERATION_REJECTION (71) | C_INVALID_CRV(10) [ Invalid
                                                					 call identifier (sao_id), also known as cluster_id is used or call does not
                                                					 exist] |
| GENERIC_SYSTEM_RESOURCE_ AVAILABILITY (31) - The client attempted to add a
                                                					 seventh party to a call with six active parties. | GENERIC_OPERATION_REJECTION (71) | C_RESUNAVL(40) [Resources to fulfill service are not available] |
| RESOURCE_BUSY (33) - The user at the station is busy on a call or there is no
                                                					 idle appearance available. | GENERIC_OPERATION_REJECTION (71) | C_USER_BUSY(15) [Domain
                                                					 or call is being monitored by another adjunct] |
| GENERIC_SUBSCRIBED_RESOURCE_ AVAILABILITY (41) - The device identifier
                                                					 specified for alerting a call corresponds to a SIP station and the "Type of
                                                					 3PCC Enabled" for the station is not set to "Avaya". | GENERIC_OPERATION_REJECTION (71) | C_FACUNSUB(3) [Capability is implemented but not subscribed to by requester] |
| MISTYPED_ARGUMENT_REJECTION (74) - DYNAMIC_ID is specified in alerting call. | GENERIC_OPERATION_REJECTION (71) | C_SER_UNIMP(4) [
                                                					 Incompatible options selected] |

| CSTA
                                                					 Error Code Returned by TSAPI | ICM CSTA
                                                					 error code | Mapped
                                                					 Cause ASAI Value |
|---|---|---|
| GENERIC_UNSPECIFIED (0) - The specified data provided for the userInfo parameter exceeds the maximum size. For
                                                					 private data versions 2-5, the maximum length for userInfo is 32 bytes. Beginning with private data
                                                					 version 6, the maximum length was increased to 96 bytes. | GENERIC_OPERATION_REJECTION (71) | C_INVLDIE(6) [Value
                                                					 specified in parameter is not allowed or defined] |
| INVALID_OBJECT_STATE (22) - The specified connection at the station is not
                                                					 currently active (is either in alerting or held state) so it cannot be dropped. | GENERIC_OPERATION_REJECTION (71) | C_INCOM_ST(9) [Message
                                                					 not compatible with call state] |
| NO_ACTIVE_CALL (24) - The connectionID contained in the request is invalid.
                                                					 CallID may be incorrect too. | GENERIC_OPERATION_REJECTION (71) | C_INVALID_CRV(10) [ Invalid
                                                					 call identifier (sao_id), also known as cluster_id is used or call does not
                                                					 exist] |
| NO_CONNECTION_TO_CLEAR (27) - The connectionID contained in the request is
                                                					 invalid. CallID may be correct, but deviceID is wrong. | GENERIC_OPERATION_REJECTION (71) | C_INVLDNUM(0) [ One of
                                                					 the entered parameters was invalid] |
| RESOURCE_BUSY (33) - The switch is busy with another CSTA request. This happens
                                                					 when two AE Services servers are issuing requests (Hold Call, Retrieve Call,
                                                					 Clear Connection, and so on) to the same device. | GENERIC_OPERATION_REJECTION (71) | C_USER_BUSY(15) [Domain
                                                					 or call is being monitored by another adjunct] |

| CSTA
                                                					 Error Code Returned by TSAPI | ICM CSTA
                                                					 error code | Mapped
                                                					 Cause ASAI Value |
|---|---|---|
| INVALID_CSTA_DEVICE_IDENTIFIER (12) - An invalid device identifier or extension
                                                					 is specified in heldCall or activeCall. | GENERIC_OPERATION_REJECTION (71) | C_INVLDNUM(0) [One of
                                                					 the entered parameters was invalid] |
| INVALID_CSTA_CONNECTION_IDENTIFIER (13) - The controlling deviceID, inheldCall,
                                                					 or activeCall has not been specified correctly. | GENERIC_OPERATION_REJECTION (71) | C_INVLDNUM(0) [One of
                                                					 the entered parameters was invalid] |
| GENERIC_STATE_INCOMPATIBILITY (21) - Both calls are alerting, both calls are
                                                					 being service-observed, or an active call is in a vector processing stage. | GENERIC_OPERATION_REJECTION (71) | C_REORDER_ ENIAL(29) [Reorder/Denial] |
| INVALID_OBJECT_STATE (22) - The connections specified in the request are not in
                                                					 valid states for the operation to take place. For example, it does not have one
                                                					 call active and one call in the held state as required. | GENERIC_OPERATION_REJECTION (71) | C_INVLDNUM(0) [One of
                                                					 the entered parameters was invalid] |
| RESOURCE_BUSY (33) - The switch is busy with another CSTA request. This can
                                                					 happen when two AE Services servers are issuing requests ( Hold Call, Retrieve
                                                					 Call, Clear Connection, Conference Call, and so on) to the same device. | GENERIC_OPERATION_REJECTION (71) | C_USER_BUSY(15) [Domain
                                                					 or call is being monitored by another adjunct] |
| CONFERENCE_MEMBER_LIMIT_EXCEEDED (38) - The request attempted to add a seventh
                                                					 party to an existing six-party conference call. If a station places a six-party
                                                					 conference call on hold and another party adds another station (so that there
                                                					 are again six active parties on the call which is the limit of the
                                                					 Communication Manager), then the station with the call on hold will not be able
                                                					 to retrieve the call. | GENERIC_OPERATION_REJECTION (71) | C_REORDER_DENIAL (29) [Reorder/Denial] |
| GENERIC_SUBSCRIBED_RESOURCE_ AVAILABILITY (41) - The device identifier
                                                					 specified in activeCall and heldCall corresponds to a SIP station and the "Type
                                                					 of 3PCC Enabled" for the station is not set to "Avaya". | GENERIC_OPERATION_REJECTION (71) | C_FACUNSUB(3) [Capability is implemented but not subscribed to by requester] |
| MISTYPED_ARGUMENT_REJECTION (74) - DYNAMIC_ID is specified inheldCall or
                                                					 activeCall. | GENERIC_OPERATION_REJECTION (71) | C_SER_UNIMP(4) [Incompatible options selected] |

| CSTA
                                                					 Error Code Returned by TSAPI | ICM CSTA
                                                					 error code | Mapped
                                                					 Cause ASAI Value |
|---|---|---|
| INVALID_CSTA_DEVICE_IDENTIFIER (12) - An invalid device identifier or extension
                                                					 is specified in activeCall. | GENERIC_OPERATION_REJECTION (71) | C_INVLDNUM(0) [One of
                                                					 the entered parameters was invalid] |
| INVALID_CSTA_CONNECTION_IDENTIFIER (13) - The connection identifier contained
                                                					 in the request is invalid or does not correspond to a station. | GENERIC_OPERATION_REJECTION (71) | C_INVLDNUM(0) [One of
                                                					 the entered parameters was invalid] |
| NO_ACTIVE_CALL (24) - The party to be put on hold is not currently active (for
                                                					 example, in the alerting state) so it cannot be put on hold. | GENERIC_OPERATION_REJECTION (71) | C_INCOM_ST(9) [Message
                                                					 not compatible with call state] |
| RESOURCE_BUSY (33) - The switch is busy with another CSTA request. This can
                                                					 happen when two AEI Services servers are issuing requests (Hold Call, Retrieve
                                                					 Call, Clear Connection, and so on) for the same device. | GENERIC_OPERATION_REJECTION (71) | C_USER_BUSY(15) [Domain
                                                					 or call is being monitored by another adjunct] |
| GENERIC_SUBSCRIBED_RESOURCE_ AVAILABILITY (41) - The device identifier
                                                					 specified in activeCall corresponds to a SIP station and the "Type of 3PCC
                                                					 Enabled" administered for the station is not set to "Avaya". | GENERIC_OPERATION_REJECTION (71) | C_FACUNSUB(3) [Capability is implemented but not subscribed to by requester] |
| OUTSTANDING_REQUEST_LIMIT_ EXCEEDED (44) - The client attempted to put a third
                                                					 party on hold while two parties are on hold already, on an analog station. | GENERIC_OPERATION_REJECTION (71) | C_INCOM_ST(9) [Message
                                                					 not compatible with call state] |
| MISTYPED_ARGUMENT_REJECTION (74) - DYNAMIC_ID is specified inactiveCall. | GENERIC_OPERATION_REJECTION (71) | C_SER_UNIMP(4) [Incompatible options selected] |

| CSTA
                                                					 Error Code Returned by TSAPI | ICM CSTA
                                                					 error code | Mapped
                                                					 Cause ASAI Value |
|---|---|---|
| GENERIC_UNSPECIFIED (0) - The specified data provided for the userInfoparameter
                                                					 exceeds the maximum allowable size. For private data versions 2-5, the maximum
                                                					 length of userInfo is 32 bytes. Beginning with private data version 6, the
                                                					 maximum length of userInfo is 96 bytes. | GENERIC_OPERATION_REJECTION (71) | C_INVLDIE(6) [Value
                                                					 specified in parameter is not allowed or defined] |
| INVALID_CALLING_DEVICE (5) - The callingDevice is out of service
                                                					 or not administered correctly in the switch. | GENERIC_OPERATION_REJECTION (71) | C_OUT_OF_SERV(19) [Domain
                                                					 was removed by Administration] |
| INVALID_CSTA_DEVICE_IDENTIFIER (12) - An invalid device
                                                					 identifier or extension is specified in callingDevice. | GENERIC_OPERATION_REJECTION (71) | C_INVLDNUM(0) [One of
                                                					 the entered parameters was invalid] |
| GENERIC_STATE_INCOMPATIBILITY (21) - The originator does not go off-hook within
                                                					 five seconds after originating the call and cannot be forced off-hook. | GENERIC_OPERATION_REJECTION (71) | C_NOUSE_RESP(16) [Originating address does not respond to service] |
| RESOURCE_BUSY (33) - The user is busy on another call and cannot originate this
                                                					 call, or the switch is busy with another CSTA request. This can happen when two
                                                					 AE Services servers are issuing requests ( Hold Call, Retrieve Call, Clear
                                                					 Connection, Make Call, and so on) for the same device. | GENERIC_OPERATION_REJECTION (71) | C_USER_BUSY(15) [Domain
                                                					 or call is being monitored by another adjunct] |
| GENERIC_SUBSCRIBED_RESOURCE_ AVAILABILITY (41) - The device identifier
                                                					 specified in callingDevice corresponds to a SIP station and the "Type of 3PCC
                                                					 Enabled" administered for the station is not set to "Avaya". | GENERIC_OPERATION_REJECTION (71) | C_FACUNSUB(3) [Capability is implemented but not subscribed to by requester] |

| CSTA
                                                					 Error Code Returned by TSAPI | ICM CSTA
                                                					 error code | Mapped
                                                					 Cause ASAI Value |
|---|---|---|
| INVALID_CSTA_DEVICE_IDENTIFIER (12) - An invalid device identifier or extension
                                                					 is specified in heldCall. | GENERIC_OPERATION_REJECTION (71) | C_INVLDNUM(0) [Invalid
                                                					 origination or destination address] |
| INVALID_CSTA_CONNECTION_IDENTIFIER (13) - The connectionID contained in the
                                                					 request is invalid. | GENERIC_OPERATION_REJECTION (71) | C_INVLDNUM(0) [Invalid
                                                					 origination or destination address] |
| GENERIC_STATE_INCOMPATIBILITY (21) - The user was on-hook when the request was
                                                					 made and did not go off-hook within five seconds (call remains on hold). | GENERIC_OPERATION_REJECTION (71) | C_NOUSE_RESP(16) [Originating address does not respond to service] |
| NO_ACTIVE_CALL (24) - The specified call at the station is cleared and so it
                                                					 cannot be retrieved. | GENERIC_OPERATION_REJECTION (71) | C_INVALID_CRV(10) [Invalid
                                                					 call identifier (sao_id) also known as cluster_id is used or call does not
                                                					 exist] |
| NO_HELD_CALL (25) - The specified connection at the station is not in the held
                                                					 state (for example, in the alerting state) and so it cannot be retrieved. | GENERIC_OPERATION_REJECTION (71) | C_INCOM_ST(9) [Message
                                                					 not compatible with call state] |
| RESOURCE_BUSY (33) - The switch is busy with another CSTA request. This can
                                                					 happen when two AE Services servers are issuing requests (Hold Call, Retrieve
                                                					 Call, Clear Connection, Conference Call, and so on) for the same device. | GENERIC_OPERATION_REJECTION (71) | C_USER_BUSY(15) [Domain
                                                					 or call is being monitored by another adjunct] |
| CONFERENCE_MEMBER_LIMIT_EXCEEDED (38) - The client attempted to add a seventh
                                                					 party to a six-party conference call. | GENERIC_OPERATION_REJECTION (71) | C_RESUNAVL(40) [Resources to fulfill service are not available] |
| GENERIC_SUBSCRIBED_RESOURCE_ AVAILABILITY (41) - The device identifier
                                                					 specified in heldCall corresponds to a SIP station and the "Type of 3PCC
                                                					 Enabled" administered for the station is not set to "Avaya". | GENERIC_OPERATION_REJECTION (71) | C_FACUNSUB(3) [Capability is implemented but not subscribed to by requester]] |
| MISTYPED_ARGUMENT_REJECTION (74) - DYNAMIC_ID is specified in heldCall. | GENERIC_OPERATION_REJECTION (71) | C_SER_UNIMP(4) [Incompatible options selected] |

| CSTA
                                                					 Error Code Returned by TSAPI | ICM CSTA
                                                					 error code | Mapped
                                                					 Cause ASAI Value |
|---|---|---|
| INVALID_CSTA_DEVICE_IDENTIFIER (12) - An invalid device identifier or extension
                                                					 was specified in heldCall or activeCall. | GENERIC_OPERATION_REJECTION (71) | C_INVLDNUM(0) [One of
                                                					 the entered parameters was invalid] |
| INVALID_CSTA_CONNECTION_IDENTIFIER (13) - The controllingdeviceID in activeCall
                                                					 or heldCall has not been specified correctly. | GENERIC_OPERATION_REJECTION (71) | C_INVLDNUM(0) [One of
                                                					 the entered parameters was invalid] |
| GENERIC_STATE_INCOMPATIBILITY (21) - The request failed due to one of the
                                                					 following reasons: Both
                                                         						  calls are alerting Both
                                                         						  calls are being service-observed An
                                                         						  active call is in a vector-processing stage The
                                                         						  Trunk-to-Trunk Transfer feature is not enabled on Avaya Communication Manager | GENERIC_OPERATION_REJECTION (71) | C_REORDER_DENIAL (29) [Reorder/Denial] |
| INVALID_OBJECT_STATE (22) - The connections specified in the request are not in
                                                					 valid states for the operation to take place. For example, the transferring
                                                					 device does not have one active call and one held call as required. | GENERIC_OPERATION_REJECTION (71) | C_INCOM_ST(9) [Message
                                                					 not compatible with call state] |
| INVALID_CONNECTION_ID_FOR_ACTIVE_ CALL (23) - The callID inactiveCall or
                                                					 heldCall has not been specified correctly. | GENERIC_OPERATION_REJECTION (71) | C_INVLDNUM(0) [One of
                                                					 the entered parameters was invalid] |
| RESOURCE_BUSY (33) - The switch is busy with another CSTA request. This can
                                                					 happen when two AE Services servers are issuing requests (Hold Call, Retrieve
                                                					 Call, Clear Connection, Transfer Call, and so on) for the same device. | GENERIC_OPERATION_REJECTION (71) | C_REORDER_ DENIAL(29) [Reorder/Denial] |
| GENERIC_SUBSCRIBED_RESOURCE_ AVAILABILITY (41) - The device identifier
                                                					 specified in activeCall and heldCall corresponds to a SIP station and the "Type
                                                					 of 3PCC Enabled" administered for the station is not set to "Avaya". | GENERIC_OPERATION_REJECTION (71) | C_FACUNSUB(3) [Capability is implemented but not subscribed to by requester] |
| MISTYPED_ARGUMENT_REJECTION (74) - DYNAMIC_ID is specified in heldCall or
                                                					 activeCall. | GENERIC_OPERATION_REJECTION (71) | C_SER_UNIMP(4) [Incompatible options selected] |

| CSTA
                                                					 Error Code Returned by TSAPI | ICM CSTA
                                                					 error code | Mapped
                                                					 Cause ASAI Value |
|---|---|---|
| NO_ACTIVE_CALL (24) - The callID of the connectionID specified in the request
                                                					 is invalid. | GENERIC_OPERATION_REJECTION (71) | C_INVALID_CRV(10) [Invalid
                                                					 call identifier (sao_id) also known as cluster_id is used or call does not
                                                					 exist] |

| CSTA
                                                					 Error Code Returned by TSAPI | ICM CSTA
                                                					 error code | Mapped
                                                					 Cause ASAI Value |
|---|---|---|
| GENERIC_UNSPECIFIED (0) - The request failed due to one of the following
                                                					 reasons: The
                                                         						  request attempted to log out an ACD agent who is already logged out The
                                                         						  request attempted to log an ACD agent into a split of which they are not a
                                                         						  member The
                                                         						  request attempted to log in an ACD agent with an incorrect password The
                                                         						  request attempted to log in an ACD agent at a station where the Auto Answer
                                                         						  feature is enabled, but the station is not off-hook. | GENERIC_UNSPECIFIED (0) | C_NOLOGIN [for
                                                					 agent logout request when agent not logged in] C_INC_PASWD(22) [for
                                                					 agent login request] C_INCS_AGT_ST [for any
                                                					 other set agent state requests] |
| GENERIC_OPERATION (1) - The request attempted to log in an ACD agent that is
                                                					 already logged in. | For TP
                                                					 login Request: SPECIFIED_EXTENSION_ALREADY_ IN_USE(283) [Other Agent is already logged in on
                                                      						  device] SPECIFIED_AGENT_ALREADY_ SIGNED_ON(259) [Same Agent is logged on same device] GENERIC_OPERATION_REJECTION (71) [station not in service] For non
                                                					 TP login Request: GENERIC_OPERATION (1) | For TP
                                                					 login Request: C_CAUSE_ UNKNOWN [Other Agent is already logged in on device/Same Agent is
                                                      						  logged on same device - not to be used] C_OUT_OF_SERV [Station not in service] C_AGT_STATE (23) [for all requests other than login] |
| VALUE_OUT_OF_RANGE (3) The
                                                					 request failed due to one of the following reasons: The workMode private
                                                      						parameter is not valid for the agentMode The
                                                         						  reason code is outside of the acceptable range (1- 9 or 1-99). (CS0/100) | INVALID_AGENT_WORKMODE [for work-mode change requests] INVALID_AGENT_REASON_CODE [for logout requests] | C_CAUSE_
                                                					 UNKNOWN (Not to be
                                                					 used) |
| OBJECT_NOT_KNOWN (4) The
                                                					 request failed due to one of the following reasons: service request did not
                                                      						specify a valid on-PBX station for the ACD agent in device agentGroup or device parameters were NULL agentID parameter was NULL when agentMode was set to AM_LOG_IN | GENERIC_UNSPECIFIED_REJECTION (70) | C_INVLDNUM(0) [One of
                                                					 the entered parameters was invalid] |
| INVALID_CSTA_DEVICE_IDENTIFIER (12) - An invalid device identifier has been
                                                					 specified in the device. | GENERIC_UNSPECIFIED_REJECTION (70) | C_INVLDNUM(0) [One of
                                                					 the entered parameters was invalid] |
| INVALID_FEATURE (15) - The feature is not available for the agentGroup or the
                                                					 enablePending feature is not available for the switch version. | GENERIC_UNSPECIFIED_REJECTION (70) | C_SERV_UNAVIL(7) [Domain
                                                					 or call is being monitored by another adjunct] |
| INVALID_OBJECT_TYPE (18) (CS3/80) - A reason code was specified, but the
                                                					 specified workMode was not WM_AUX_WORK or AM_LOG_OUT. | GENERIC_UNSPECIFIED_REJECTION (70) | C_INCOM_OPT(11) [Incompatible options used to establish the call] |
| GENERIC_STATE_INCOMPATIBILITY (21) A work
                                                         						  mode change was requested for a non-ACD agent The
                                                         						  Agent station is maintenance busy or out of service | GENERIC_UNSPECIFIED_REJECTION (70) | C_MAXLOGIN(21) [for
                                                					 login requests - Agent logged in to maximum number of splits] C_INCS_AGT_ST [for all
                                                					 other requests other than login] |
| GENERIC_SYSTEM_RESOURCE_ AVAILABILITY (31) - The request cannot complete due to
                                                					 lack of available switch resources. | GENERIC_UNSPECIFIED_REJECTION (70) | C_RESUNAVL(2) [Resources to fulfill service are not available] |
| RESOURCE_BUSY (33) - The service attempted to change the state of an ACD agent
                                                					 that is currently on a call. | GENERIC_UNSPECIFIED_REJECTION (70) | C_USER_BUSY(17) [Domain
                                                					 or call is being monitored by another adjunct] |
| GENERIC_SUBSCRIBED_RESOURCE_ AVAILABILITY (41) - The device identifier
                                                					 specified in device corresponds to a SIP station and the "Type of 3PCC Enabled"
                                                					 administered for the station is not set to "Avaya". | GENERIC_UNSPECIFIED_REJECTION (70) | C_FACUNSUB(3) [Capability is implemented but not subscribed to by requester] |

| CSTA
                                                					 Error Code Returned by TSAPI | ICM CSTA
                                                					 error code | Mapped
                                                					 Cause ASAI Value |
|---|---|---|
| GENERIC_UNSPECIFIED (0) - An error has occurred. The TSAPI Service could not
                                                					 provide a specific error value. | GENERIC_UNSPECIFIED (0) | C_CAUSE_
                                                					 UNKNOWN |
| GENERIC_OPERATION (1) - The CTI protocol is broken d or the service invoked is
                                                					 not consistent with a CTI application association. | GENERIC_OPERATION (1) | C_PROTERR(1) [Capability sequence was violated or underlying protocol error was detected; an
                                                					 unrecognized value was returned by the ECS] |
| REQUEST_INCOMPATIBLE_WITH_ OBJECT (2) - The service request does not correspond
                                                					 to a CTI application association. | GENERIC_UNSPECIFIED_REJECTION (70) | C_FEATURE_REJECTED (31) [The ECS
                                                					 has rejected a request from the adjunct] |
| VALUE_OUT_OF_RANGE (3) - Communication Manager detects that a required
                                                					 parameter is missing from the request or an out-of-range value has been
                                                					 specified. | GENERIC_UNSPECIFIED_REJECTION (70) | C_MAND_INFO(5) [One of
                                                					 the required parameters is missing] |
| OBJECT_NOT_KNOWN (4) - The TSAPI Service detects that a required parameter is
                                                					 missing in the request. For example, the deviceIDof a connectionID is not
                                                					 specified in a service request. | GENERIC_UNSPECIFIED_REJECTION (70) | C_MAND_INFO(5) [One of
                                                					 the required parameters is missing] |
| INVALID_FEATURE (15) - The TSAPI Service detects a CSTA Service request that is
                                                					 not supported by Communication Manager. | GENERIC_UNSPECIFIED_REJECTION (70) | C_SERV_UNAVIL(7) [Domain
                                                					 or call is being monitored by another adjunct] |
| GENERIC_SYSTEM_RESOURCE_ AVAILABILITY (31) - The request cannot be completed
                                                					 due to lack of available switch resources. | GENERIC_UNSPECIFIED_REJECTION (70) | C_RESUNAVL(2) [Resources to fulfill service are not available] |
| RESOURCE_OUT_OF_SERVICE (34) - An application can receive this error code when a single CSTA Service request is ending unusually
                                                due to protocol error. | GENERIC_UNSPECIFIED_REJECTION (70) | C_PROTERR(1) [Capability sequence was violated or underlying protocol
                                             				  error was detected; an unrecognized value was returned by the ECS] |
| NETWORK_BUSY (35) - Communication Manager is not accepting the request at this
                                                					 time because of processor overload. The application may wish to retry the
                                                					 request but should not do so immediately. | GENERIC_UNSPECIFIED_REJECTION (70) | C_NETCONJ |
| GENERIC_SUBSCRIBED_RESOURCE_ AVAILABILITY (41) - The TSAPI Service could not
                                                					 acquire the license(s) needed to satisfy the request. | GENERIC_OPERATION_REJECTION (71) | C_FACUNSUB(3) [Capability is implemented but not subscribed to by requester] |
| OUTSTANDING_REQUEST_LIMIT_ EXCEEDED (44) - The given request cannot be
                                                					 processed due to a system resource limit on the device. | GENERIC_OPERATION_REJECTION (71) | C_RESUNAVL(2) [Resources to fulfill service are not available] |
| GENERIC_UNSPECIFIED_REJECTION (70) - This is a TSAPI Service internal error,
                                                					 but it cannot be more specific. The system administrator should check the AE
                                                					 Services OAM error logs for more information about this error. | GENERIC_UNSPECIFIED_REJECTION (70) | C_CAUSE_
                                                					 UNKNOWN |
| GENERIC_OPERATION_REJECTION (71) - This is a TSAPI Service internal error, but
                                                					 not a defined error. The system administrator should check the TSAPI Service
                                                					 error logs for more information about this error. | GENERIC_OPERATION_REJECTION (71) | C_CAUSE_
                                                					 UNKNOWN |
| DUPLICATE_INVOCATION_REJECTION (72) - The TSAPI Service detects that
                                                					 theinvokeID in the service request is being used by another outstanding service
                                                					 request. This service request is rejected. The outstanding service request with
                                                					 the same invokeID is still valid. | GENERIC_OPERATION_REJECTION (71) | C_SER_UNIMP(4) [Incompatible options selected] |
| UNRECOGNIZED_OPERATION_ REJECTION (73) - The TSAPI Service detects that the
                                                					 service request from a client application is not defined in the API. A CSTA
                                                					 request with a 0 or negative invokeID will receive this error. | GENERIC_OPERATION_REJECTION (71) | C_SER_UNIMP(4) [Incompatible options selected] |
| RESOURCE_LIMITATION_REJECTION (75) - The TSAPI Service detects that it lacks
                                                					 internal resources such as the memory or data records to process a service
                                                					 request. A system administrator should check the TSAPI Service error logs for
                                                					 more detailed information about this error. This failure may reflect a
                                                					 temporary situation. The application should retry the request. | GENERIC_OPERATION_REJECTION (71) | C_TEMP_FAILURE(37) [Temporary Failure] |
| ACS_HANDLE_TERMINATION_REJECTION (76) - The TSAPI Service detects that
                                                					 anacsOpenStream session is terminating. The TSAPI Service sends this error for
                                                					 every outstanding CSTA request of this ACS Handle. For
                                                					 example, a user may power off the PC before the application issues
                                                					 anacsCloseStream request and waits for the confirmation event. In this case,
                                                					 the acsCloseStream is issued by the TSAPI Service on behalf of the application
                                                					 and there is no application to receive this error. If an application issues
                                                					 anacsCloseStream request and waits for its confirmation event, the application
                                                					 will receive this error for every outstanding request. | GENERIC_OPERATION_REJECTION (71) | C_CAUSE_
                                                					 UNKNOWN |
| SERVICE_TERMINATION_REJECTION (77) - The TSAPI Service detects that it cannot
                                                					 provide the service due to the failure or shutting down of the communication
                                                					 link between the Telephony Server and Communication Manager. The TSAPI Service
                                                					 sends this error for every outstanding CSTA request that effects every ACS
                                                					 Handle. Although the link is down or Communication Manager is out of service,
                                                					 the TSAPI Service remains loaded and advertised. When the TSAPI Service is in
                                                					 this state, all CSTA Service requests from a client will receive a negative
                                                					 acknowledgment with this error code. | GENERIC_OPERATION_REJECTION (71) | C_CAUSE_
                                                					 UNKNOWN |
| REQUEST_TIMEOUT_REJECTION (78) - The TSAPI Service did not receive the response
                                                					 of a service request sent to Communication Manager more than 30 seconds ago.
                                                					 The request is canceled and negatively acknowledged with this error code. When
                                                					 this occurs, the communication link between the TSAPI Service and Communication
                                                					 Manager may be out of service or congested. Congestion may occur when TSAPI
                                                					 applications exceed the capacity of the TSAPI Service. | GENERIC_OPERATION_REJECTION (71) | C_REC_TIMER(12) [Timer
                                                					 expired] |
| REQUESTS_ON_DEVICE_EXCEEDED_ REJECTION (79) - The TSAPI Service processes one
                                                					 service request at a time for every device. The TSAPI Service queues CSTA
                                                					 requests for a device. Only a limited number of CSTA requests are queued on a
                                                					 device. If this number is exceeded, the incoming client request is negatively
                                                					 acknowledged with this error code. Usually an application sends one request and
                                                					 waits for its completion before it makes another request. The
                                                					 MAX_-REQS_QUEUED_PER_DEVICE parameter has no effect on this class of
                                                					 applications. Situations
                                                					 of sending a sequence of requests without waiting for their completion are
                                                					 rare. However, if this is the case, set the MAX_REQS_QUEUED_-PER_DEVICE
                                                					 parameter to a proper value. The default value for MAX_-REQS_QUEUED_PER_DEVICE
                                                					 is 4. | GENERIC_OPERATION_REJECTION (71) | C_QUEFULL(28) [Queue is
                                                					 full] |

| Error | Indicates |
|---|---|
| PERERR_TELDRIVE | The telephony driver layer generated the error. |
| PERERR_JTCLIENT | The JTAPI client generated the error. |
| PERERR_JTAPPLAY | The JTAPI application layer generated the error. |
| PERERR_GW_E | The JTAPI gateway generated the error. |
| PERERR_CM | Cisco Unified Communications Manager generated the error. |

| Note | Some of these values appear over two lines due to space
                                             			 limitations. |
|---|---|

| Return Value/ Code | Error Message | Description |
|---|---|---|
| -1 PERERR_UNKNOWN | Unknown Peripheral Error. | The Peripheral error specified does not exist. |
| 10001 PERERR_TELDRIVE_ LOCKTPSERVICES | A logic error occurred prior to Locking TP
                                          				  Services. | The TP Services cannot be locked by the thread
                                          				  because they are already locked. This is a serious logic condition and should
                                          				  be reported/resolved. |
| 10002 PERERR_TELDRIVE_ LOCKINSTANCE | A logic error occurred prior to Locking the
                                          				  Client Instance. | The Client Instance cannot be locked by the
                                          				  thread because it is already locked. This is a serious logic condition and
                                          				  should be reported/resolved. |
| 10003 PERERR_TELDRIVE_ LOCKTELDRIVELAYER | A logic error occurred prior to Locking the
                                          				  Telephony Driver Layer. | The Telephony Driver Layer cannot be locked by
                                          				  the thread because it is already locked. This is a serious logic condition and
                                          				  should be reported/resolved. |
| 10004 PERERR_TELDRIVE_ NOINSTRUMENTFOR
                                          				  EXTENSION | The extension number specified is not
                                          				  associated with any known instrument. | An instrument with the number specified cannot
                                          				  be found for any instrument. Perhaps an invalid extension was specified. |
| 10101 PERERR_TELDRIVE_ AGENTALREADYLOGGEDOUT | The agent is already LOGGED out. | An attempt was made to log out an agent that
                                          				  is already logged out. This attempt failed. |
| 10102 PERERR_TELDRIVE_ AGENTALREADYSIGNEDON | The agent is already LOGGED ON. | An attempt was made to log in an agent that is
                                          				  already logged in. This attempt failed. |
| 10103 PERERR_TELDRIVE_ AGENTAVAILORWORK | The requested function cannot be performed
                                          				  since the agent is AVAILABLE or in a CALL WORK State. | This can occur when an agent tries to make a
                                          				  call from an AVAILABLE, or WORK state. |
| 10104 PERERR_TELDRIVE_ AGENTCANTGOUNVAILABLE | The Agent cannot go UNAVAILABLE due to
                                          				  possible calls. | When this error occurs, the ROUTER did not
                                          				  approve the agent going unavailable. Typically retrying this makes it succeed. |
| 10105 PERERR_TELDRIVE_ AGENTNOTINATEAM | Agent is not a TEAM member– cannot make
                                          				  supervisor call. | The agent is trying to make a supervisor
                                          				  assist call but is not a member of a team. |
| 10106 PERERR_TELDRIVE_ AGENTRESERVED | Agent is RESERVED – cannot make call. | This error occurs when the agent is trying to
                                          				  make a call or consult call but is currently RESERVED for an incoming call. |
| 10107 PERERR_TELDRIVE_ AGENTTEAMNOTFOUND | Internal Logic Error – Agent Team not found. | The agent team specified in the agent object
                                          				  cannot be found. This indicates an internal error that should be reported and
                                          				  resolved. |
| 10108 PERERR_TELDRIVE_ BADSTATETRANSITION | The state transition is invalid from the
                                          				  current state. | The routine
                                          				  ValidateAgentPrevalentStateTransition determined that the desired transition
                                          				  was illegal from the current state. |
| 10109 PERERR_TELDRIVE_ CALLTYPENOTVALIDFOR
                                          				  DIALPLAN | The agent is attempting to make a call that is
                                          				  not valid for their defined call plan. | The call type that the call was classified
                                          				  into is not allowed for the dialed Number Plan used. |
| 10111 PERERR_TELDRIVE_ CANTGOREADYFROM
                                          				  CURRENTSTATE | Cannot transition to READY from current state. | Based upon transition rules, the agent cannot
                                          				  go READY. Examples: You cannot go READY from TALKING. |
| 10112 PERERR_TELDRIVE_ CANTLOGOUTFROM
                                          				  CURRENTSTATE | The agent cannot log out from the current
                                          				  state. | The agent must be NOT READY in order to log
                                          				  out. |
| 13042 PERERR_GW_E_ THREADCLEARCALL_
                                          				  DROP_EXCEPTION | JTAPI Gateway – Error on CLEAR CALL operation
                                          				  – Exception. | The routine run in object ThreadClearCall got
                                          				  an exception (not of type CiscoJTapiException) on a call to "drop". |
| 13044 PERERR_GW_E_ THREADCLEARCONNECTION_
                                          				  UNKNOWN_CONNECTION | JTAPI Gateway – Error on CLEARCONNECTION
                                          				  operation – Unknown connection ID. |  |
| 13045 PERERR_GW_E_ THREADCONFERENCECALL_
                                          				  ACTIVE_CONN_NOT_TALKING | JTAPI Gateway – Error on CONFERENCE operation
                                          				  – ACTIVE connection not in proper state. | The connection specified in the active
                                          				  connection is not in the TALKING state. |
| 13046 PERERR_GW_E_ THREADCONFERENCECALL_
                                          				  BAD_ACTIVE_CONNECTION | JTAPI Gateway – Error on CONFERENCE operation
                                          				  – ACTIVE connection not found. |  |
| 13047 PERERR_GW_E_THREAD CONFERENCECALL_
                                          				  BAD_HELD_CONNECTION | JTAPI Gateway – Error on CONFERENCE operation
                                          				  – HELD connection not found. |  |
| 13048 PERERR_GW_E_THREAD CONFERENCECALL_
                                          				  CREATECALL_NULL_CALL | JTAPI Gateway – Error on CONFERENCE operation. | The routine run in object ThreadConferenceCall
                                          				  got a null call returned from "createcall". |
| 13049 PERERR_GW_E_THREAD CONFERENCECALL_
                                          				  EXCEPTION_ADDPARTY | JTAPI Gateway – Error on CONFERENCE operation. | The routine run in object ThreadConferenceCall
                                          				  got an exception (not of type CiscoJTapiException) on a call to "addparty". |
| 13050 PERERR_GW_E_THREAD CONFERENCECALL_
                                          				  EXCEPTION_ CONFERENCE_NEW | JTAPI Gateway – Error on CONFERENCE operation. | The routine run in object ThreadConferenceCall
                                          				  got an exception (not of type CiscoJTapiException) on a call to "conference"
                                          				  for the NEW call. |
| 13051 PERERR_GW_E_ THREADCONFERENCECALL_
                                          				  EXCEPTION_CONFERENCE_HELD | JTAPI Gateway – Error on CONFERENCE operation. | The routine run in object ThreadConferenceCall
                                          				  got an exception (not of type CiscoJTapiException) on a call to "conference"
                                          				  for the HELD call. |
| 13052 PERERR_GW_E_ THREADCONFERENCECALL_
                                          				  EXCEPTION_CONSULT | JTAPI Gateway – Error on CONFERENCE operation. | The routine run in object ThreadConferenceCall
                                          				  got an exception (not of type CiscoJTapiException) on a call to "consult". |
| 13053 PERERR_GW_E_ THREADCONFERENCECALL_
                                          				  EXCEPTION_CREATECALL | JTAPI Gateway – Error on CONFERENCE operation. | The routine run in object ThreadConferenceCall
                                          				  got an exception (not of type CiscoJTapiException) on a call to "consult". |
| 13054 PERERR_GW_E_ THREADCONFERENCE
                                          				  CALL_EXCEPTION_ SETCONFERENCEENABLE | JTAPI Gateway – Error on CONFERENCE operation. | The routine run in object ThreadConferenceCall
                                          				  got an exception (not of type CiscoJTapiException) on a call to
                                          				  "setconferenceenable". |
| 13055 PERERR_GW_E_ THREADCONFERENCE
                                          				  CALL_EXCEPTION_ SETTRANSFERCONTROLLER | JTAPI Gateway – Error on CONFERENCE operation. | The routine run in object ThreadConferenceCall
                                          				  got an exception (not of type CiscoJTapiException) on a call to
                                          				  "settransfercontroller". |
| 13056 PERERR_GW_E_THREAD CONFERENCECALL_
                                          				  HELD_CONN_NOT_HELD | JTAPI Gateway – Error on CONFERENCE operation
                                          				  – HELD connection not HELD | The connection passed for the held connection
                                          				  is not in the HELD state. |
| 13057 PERERR_GW_E_THREAD CONFERENCECALL_
                                          				  NULL_DIALED_NUMBER | JTAPI Gateway – Error on CONFERENCE operation
                                          				  – Invalid Dialed Number. | A NULL dialed number was specified for the
                                          				  consultation number. |
| 13058 PERERR_GW_E_THREAD CONSULTATIONCALL_
                                          				  CREATECALL_NULL_CALL | JTAPI Gateway – Operation error on CONSULT
                                          				  operation. | The routine run in object
                                          				  ThreadConsultationCall got a null call returned from "createCall". |
| 13059 PERERR_GW_E_THREAD CONSULTATIONCALL_
                                          				  EXCEPTION_CONSULT | JTAPI Gateway – Error on CONSULT operation. | The routine run in object
                                          				  ThreadConsultationCall got an exception on a call to "settransfercontroller". |
| 13060 PERERR_GW_E_THREAD CONSULTATIONCALL_
                                          				  EXCEPTION_CREATECALL | JTAPI Gateway – Error on CONSULT operation. | The routine run in object
                                          				  ThreadConsultationCall got an exception on a call to "createCall". |
| 13061 PERERR_GW_E_THREAD CONSULTATIONCALL_
                                          				  EXCEPTION_SET CONFERENCEENABLE | JTAPI Gateway – Error on CONSULT operation. | The routine run in object
                                          				  ThreadConsultationCall got an exception on a call to "setConferenceEnable". |
| 13062 PERERR_GW_E_THREAD CONSULTATIONCALL_
                                          				  INVALID_CONSULT_TYPE | JTAPI Gateway – Error on CONSULT operation –
                                          				  Invalid Consult type. | The type specified is not TRANSFER or
                                          				  CONFERENCE. |
| 13063 PERERR_GW_E_THREAD CONSULTATIONCALL_
                                          				  NO_ACTIVE_CONNECTION | JTAPI Gateway – Error on CONSULT operation –
                                          				  No Active Connection. | The ACTIVE connection specified in the request
                                          				  does not exist. |
| 13064 PERERR_GW_E_THREAD ESCAPESERVICE_
                                          				  CREATECALL_NULL_CALL1 | JTAPI Gateway – Error on SUPERVISOR (escape)
                                          				  operation. | Got a NULL call returned from "createCall"
                                          				  (method "CreateNewCall" in class ThreadEscapeService). |
| 13065 PERERR_GW_E_THREAD ESCAPESERVICE_
                                          				  CREATECALL_NULL_CALL2 | JTAPI Gateway – Error on SUPERVISOR (escape)
                                          				  operation. | Got a NULL call returned from "createCall"
                                          				  (method "CreateConsultCall" in class ThreadEscapeService). |
| 13066 PERERR_GW_E_THREAD ESCAPESERVICE_
                                          				  CREATECALL_NULL_CALL3 | JTAPI Gateway – Error on SUPERVISOR (escape)
                                          				  operation. | Got a NULL call returned from "createCall"
                                          				  (method "CreateBlindConferenceCall" in class ThreadEscapeService). |
| 13067 PERERR_GW_E_THREAD ESCAPESERVICE_
                                          				  EXCEPTION_CONFERENCE | JTAPI Gateway – Error on SUPERVISOR (escape)
                                          				  operation. | Got an exception on a call to "conference"
                                          				  (method "CreateBlindConferenceCall" in class ThreadEscapeService). |
| 13068 PERERR_GW_E_THREAD ESCAPESERVICE_
                                          				  EXCEPTION_CONNECT | JTAPI Gateway – Error on SUPERVISOR (escape)
                                          				  operation. | Got an exception on a call to "connect"
                                          				  (method "CreateNewCall" in class ThreadEscapeService). |
| 13069 PERERR_GW_E_THREAD ESCAPESERVICE_
                                          				  EXCEPTION_CONSULT1 | JTAPI Gateway – Error on SUPERVISOR (escape)
                                          				  operation. | Got an exception on a call to "consult"
                                          				  (method "CreateConsultCall" in class ThreadEscapeService). |
| 13070 PERERR_GW_E_THREAD ESCAPESERVICE_
                                          				  EXCEPTION_CONSULT2 | JTAPI Gateway – Error on SUPERVISOR (escape)
                                          				  operation. | Got an exception on a call to "consult"
                                          				  (method "CreateBlindConferenceCall" in class ThreadEscapeService). |
| 13071 PERERR_GW_E_THREAD ESCAPESERVICE_
                                          				  EXCEPTION_CREATECALL1 | JTAPI Gateway – Error on SUPERVISOR (escape)
                                          				  operation. | Got an exception on a call to "createCall"
                                          				  (method "CreateNewCall" in class ThreadEscapeService). |
| 13072 PERERR_GW_E_THREAD ESCAPESERVICE_
                                          				  EXCEPTION_CREATECALL2 | JTAPI Gateway – Error on SUPERVISOR (escape)
                                          				  operation. | Got an exception on a call to "createCall"
                                          				  (method "CreateConsultCall" in class ThreadEscapeService). |
| 13073 PERERR_GW_E_THREAD ESCAPESERVICE_
                                          				  EXCEPTION_CREATECALL3 | JTAPI Gateway – Error on SUPERVISOR (escape)
                                          				  operation. | Got an exception on a call to "createCall"
                                          				  (method "CreateBlindConferenceCall" in class ThreadEscapeService). |
| 13074 PERERR_GW_E_THREAD ESCAPESERVICE_
                                          				  EXCEPTION_GETADDRESS | JTAPI Gateway – Error on SUPERVISOR (escape)
                                          				  operation. | Got an exception on a call to "getAddress"
                                          				  (method "CreateNewCall" in class ThreadEscapeService). |
| 13075 PERERR_GW_E_THREAD ESCAPESERVICE_
                                          				  EXCEPTION_GETTERMINALS | JTAPI Gateway – Error on SUPERVISOR (escape)
                                          				  operation. | Got an exception on a call to "getTerminals"
                                          				  (method "CreateNewCall" in class ThreadEscapeService). |
| 13076 PERERR_GW_E_THREAD ESCAPESERVICE_
                                          				  EXCEPTION_SETCONFERENCEENABLE1 | JTAPI Gateway – Error on SUPERVISOR (escape)
                                          				  operation | Got an exception on a call to
                                          				  "setConferenceEnable" (method "CreateConsultCall" in class ThreadEscapeService). |
| 13077 PERERR_GW_E_THREAD ESCAPESERVICE_
                                          				  EXCEPTION_SETCONFERENCEENABLE2 | JTAPI Gateway – Error on SUPERVISOR (escape)
                                          				  operation | Got an exception on a call to
                                          				  "setConferenceEnable" (method "CreateBlindConference" in class
                                          				  ThreadEscapeService). |
| 13078 PERERR_GW_E_THREAD ESCAPESERVICE_
                                          				  INVALID_EMERGENCY_ ALERT_TYPE | JTAPI Gateway – Error on SUPERVISOR (escape)
                                          				  operation – Invalid Alert Type. | The Alert type specified was not CONSULT or
                                          				  BLIND_CONFERENCE. |
| 13079 PERERR_GW_E_THREAD ESCAPESERVICE_
                                          				  INVALID_SUPERVISOR_ ASSIST_TYPE | JTAPI Gateway – Error on SUPERVISOR (escape)
                                          				  operation – Invalid Alert Type. | The Alert type specified was not CONSULT or
                                          				  BLIND_CONFERENCE. |
| 13080 PERERR_GW_E_THREAD ESCAPESERVICE_
                                          				  NO_TERMINAL_LIST | JTAPI Gateway – Error on SUPERVISOR (escape)
                                          				  operation. | Got a NULL terminal list from "getTerminals"
                                          				  (method "CreateNewCall" in class ThreadEscapeService). |
| 13081 PERERR_GW_E_THREAD HOLDCALL_
                                          				  CALL_NOT_CONTROLLED | JTAPI Gateway – Error on HOLD operation –
                                          				  Uncontrolled Call. | The call specified is not a controlled call. |
| 13082 PERERR_GW_E_THREAD HOLDCALL_
                                          				  EXCEPTION_HOLD | JTAPI Gateway – Error on HOLD operation –
                                          				  Exception. | Got an exception on a call to "hold" (method
                                          				  "run" in class ThreadHoldCall). |
| 13083 PERERR_GW_E_THREAD MAKECALL_
                                          				  CREATECALL_NULL_CALL | JTAPI Gateway – Error on MAKE CALL operation –
                                          				  Can't create call. | Got a NULL call returned from "createCall"
                                          				  (method "run" in class ThreadMakeCall). |
| 13084 PERERR_GW_E_THREAD MAKECALL_
                                          				  CREATE_CALL_FAILURE | JTAPI Gateway – Error on MAKE CALL operation –
                                          				  Can't create call. | Got an exception on a call to "createCall"
                                          				  (method "run" in class ThreadMakeCall). |
| 13085 PERERR_GW_E_THREAD MAKECALL_
                                          				  GENERIC_CM_ERROR | JTAPI Gateway – Error on MAKE CALL operation –
                                          				  Exception. | Got an exception on a call to "connect"
                                          				  (method "run" in class ThreadMakeCall). |
| 13086 PERERR_GW_E_THREAD MAKECALL_
                                          				  NULL_TERMINAL_LIST | JTAPI Gateway – Error on MAKE CALL operation. | Got a NULL terminal list returned from
                                          				  "getTerminals" (method "run" in class ThreadMakeCall). |
| 13087 PERERR_GW_E_THREAD MAKECALL_
                                          				  PROVIDER_GETADDRESS | JTAPI Gateway – Error on MAKE CALL operation. | Got an exception on a call to "getAddress"
                                          				  (method "run" in class ThreadMakeCall). |
| 13088 PERERR_GW_E_THREAD MAKECALL_
                                          				  PROVIDER_GETTERMINAL | JTAPI Gateway – Error on MAKE CALL operation. | Got an exception on a call to "getTerminals"
                                          				  (method "run" in class ThreadMakeCall). |
| 13089 PERERR_GW_E_THREAD REDIRECTCALL_
                                          				  EXCEPTION_REDIRECT | JTAPI Gateway – Error on REDIRECT operation –
                                          				  Exception. | Got an exception on a call to "redirect"
                                          				  (method "run" in class ThreadRedirectCall). |
| 13090 PERERR_GW_E_THREAD RETRIEVECALL_
                                          				  CALL_NOT_CONTROLLED | JTAPI Gateway – Error on RETRIEVE operation –
                                          				  Uncontrolled Call. | The call specified is not a controlled call. |
| 13091 PERERR_GW_E_THREAD RETRIEVECALL_
                                          				  EXCEPTION_UNHOLD | JTAPI Gateway – Error on RETRIEVE operation –
                                          				  Exception. | Got an exception on a call to "unhold" (method
                                          				  "run" in class ThreadRetrieveCall). |
| 13092 PERERR_GW_E_THREAD SENDDTMF_EXCEPTION_
                                          				  GENERATEDTMF | JTAPI Gateway – Error on SEND DTMF operation –
                                          				  Exception. | Got an exception on a call to "generateDTMF"
                                          				  (method "run" in class ThreadSendDTMF). |
| 13093 PERERR_GW_E_THREAD SENDDTMF_
                                          				  INVALID_CONNECTION | JTAPI Gateway – Error on SEND DTMF operation –
                                          				  Invalid Connection ID. | The method "run" in class ThreadSendDTMF got a
                                          				  null connection from a call to "findTerminalConnection". |
| 13094 PERERR_GW_E_THREAD SENDDTMF_
                                          				  NOT_MEDIATERMINAL CONNECTION | JTAPI Gateway – Error on SEND DTMF operation –
                                          				  No Media. |  |
| 13095 PERERR_GW_E_THREAD SUPERVISECALL_ACTIVE_
                                          				  CONN_NOT_TALKING | JTAPI Gateway – Error on SUPERVISE operation –
                                          				  ACTIVE connection not in proper state. | The connection specified in the active
                                          				  connection is not in the TALKING state. |
| 13096 PERERR_GW_E_THREAD SUPERVISECALL_
                                          				  ALREADY_BARGED_IN | JTAPI Gateway – Error on SUPERVISE operation –
                                          				  Cannot Barge in, already barged into. | The call specified on the barge in request has
                                          				  already been barged into. |
| 13097 PERERR_GW_E_THREAD SUPERVISECALL_
                                          				  CREATECALL_NULL_CALL | JTAPI Gateway – Error on SUPERVISE operation –
                                          				  Can't create call. | The routine run in object ThreadSuperviseCall
                                          				  got a null call returned from "createcall". |
| 13098 PERERR_GW_E_THREAD SUPERVISECALL_
                                          				  EXCEPTION_ANSWER1 | JTAPI Gateway – Error on SUPERVISE operation –
                                          				  Exception. | Got an exception on a call to "answer" (method
                                          				  "DirectSupervisorBargeIn" in class ThreadSuperviseCall). |
| 13099 PERERR_GW_E_THREAD SUPERVISECALL_
                                          				  EXCEPTION_ANSWER2 | JTAPI Gateway – Error on SUPERVISE operation –
                                          				  Exception. | Got an exception on a call to "answer" (method
                                          				  "BargeInBlindConferenceCall" in class ThreadSuperviseCall). |
| 13100 PERERR_GW_E_THREAD SUPERVISECALL_
                                          				  EXCEPTION_CONFERENCE1 | JTAPI Gateway – Error on SUPERVISE operation –
                                          				  Exception. | Got an exception on a call to "conference"
                                          				  (method "SupervisorBargeInCall" in class ThreadSuperviseCall). |
| 13101 PERERR_GW_E_THREAD SUPERVISECALL_
                                          				  EXCEPTION_CONFERENCE2 | JTAPI Gateway – Error on SUPERVISE operation –
                                          				  Exception. | Got an exception on a call to "conference"
                                          				  (method "DirectSupervisorBargeIn" in class ThreadSuperviseCall). |
| 13102 PERERR_GW_E_THREAD SUPERVISECALL_
                                          				  EXCEPTION_CONSULT | JTAPI Gateway – Error on SUPERVISE operation –
                                          				  Exception. | Got an exception on a call to "conference"
                                          				  (method "DirectSupervisorBargeIn" in class ThreadSuperviseCall). |
| 13103 PERERR_GW_E_THREAD SUPERVISECALL_
                                          				  EXCEPTION_CREATECALL | JTAPI Gateway – Error on SUPERVISE operation –
                                          				  Exception. | Got an exception on a call to "createCall"
                                          				  (method "DirectSupervisorBargeIn" in class ThreadSuperviseCall). |
| 13104 PERERR_GW_E_THREAD SUPERVISECALL_
                                          				  EXCEPTION_DISCONNECT1 | JTAPI Gateway – Error on SUPERVISE operation –
                                          				  Exception. | Got an exception on a call to "disconnect"
                                          				  (method "DropSupervisorCall" in class ThreadSuperviseCall). |
| 13105 PERERR_GW_E_THREAD SUPERVISECALL_
                                          				  EXCEPTION_DISCONNECT2 | JTAPI Gateway – Error on SUPERVISE operation –
                                          				  Exception. | Got an exception on a call to "disconnect"
                                          				  (method "InterceptCall" in class ThreadSuperviseCall). |
| 13106 PERERR_GW_E_THREAD SUPERVISECALL_
                                          				  EXCEPTION_SET CONFERENCEENABLE | JTAPI Gateway – Error on SUPERVISE operation –
                                          				  Exception. | Got an exception on a call to "disconnect"
                                          				  (method "DirectSupervisorBargeIn" in class ThreadSuperviseCall). |
| 13107 PERERR_GW_E_THREAD SUPERVISECALL_
                                          				  HELD_CONN_NOT_HELD1 | JTAPI Gateway – Error on SUPERVISE operation –
                                          				  HELD connection is not HELD. | The connection specified for the HELD call is
                                          				  not in the held state (method "BargInCall" class ThreadSuperviseCall). |
| 13108 PERERR_GW_E_THREAD SUPERVISECALL_
                                          				  HELD_CONN_NOT_HELD2 | JTAPI Gateway – Error on SUPERVISE operation –
                                          				  HELD connection is not HELD. | The connection specified for the HELD call is
                                          				  not in the held state (method "DirectSupervisorBargeIn" class
                                          				  ThreadSuperviseCall). |
| 13109 PERERR_GW_E_THREAD SUPERVISECALL_
                                          				  INVALID_ACTION | JTAPI Gateway – Error on SUPERVISE operation –
                                          				  Invalid action. The action specified was not CLEAR, BARGE_IN or INTERCEPT. |  |
| 13110 PERERR_GW_E_THREAD SUPERVISECALL_
                                          				  INVALID_ACTIVE_ CONNECTION | JTAPI Gateway – Error on SUPERVISE operation –
                                          				  No ACTIVE connection. | The connection specified in the active
                                          				  connection does not exist. |
| 13111 PERERR_GW_E_THREAD SUPERVISECALL_
                                          				  INVALID_AGENT_CALLID1 | JTAPI Gateway – Error on SUPERVISE operation –
                                          				  Bad Call ID. | The call ID in the agent object is invalid
                                          				  (method "BargeInCall" class ThreadSuperviseCall). |
| 13112 PERERR_GW_E_THREAD SUPERVISECALL_
                                          				  INVALID_AGENT_CALLID2 | JTAPI Gateway – Error on SUPERVISE operation –
                                          				  Bad Call ID. | The call ID in the agent object is invalid
                                          				  (method "DirectSupervisorBargeIn" class ThreadSuperviseCall). |
| 13113 PERERR_GW_E_THREAD SUPERVISECALL_
                                          				  INVALID_AGENT_ CONNECTION1 | JTAPI Gateway – Error on SUPERVISE operation –
                                          				  Bad Connection ID. | The connection ID in the agent object is
                                          				  invalid (method "BargeInCall" class ThreadSuperviseCall). |
| 13114 PERERR_GW_E_THREAD SUPERVISECALL_
                                          				  INVALID_AGENT_ CONNECTION2 | JTAPI Gateway – Error on SUPERVISE operation –
                                          				  Bad Connection ID. | The connection ID in the agent object is
                                          				  invalid (method "InterceptCall" class ThreadSuperviseCall). |
| 13115 PERERR_GW_E_THREAD SUPERVISECALL_
                                          				  INVALID_HELD_ CONNECTION | JTAPI Gateway – Error on SUPERVISE operation –
                                          				  Invalid HELD connection. | The connection ID in the agent object is
                                          				  invalid (method "BargeInCall" class ThreadSuperviseCall). |
| 13116 PERERR_GW_E_THREAD SUPERVISECALL_
                                          				  INVALID_SUPERVISOR_ CONNECTION1 | JTAPI Gateway – Error on SUPERVISE operation –
                                          				  Invalid Supervisor connection. | The connection ID in the agent object is
                                          				  invalid (method "DropSupervisorCall" class ThreadSuperviseCall). |
| 13117 PERERR_GW_E_THREAD SUPERVISECALL_
                                          				  INVALID_SUPERVISOR_ CONNECTION2 | JTAPI Gateway – Error on SUPERVISE operation –
                                          				  Invalid Supervisor connection. | The connection ID in the agent object is
                                          				  invalid (method "BargeInCall" class ThreadSuperviseCall). |
| 13118 PERERR_GW_E_THREAD SUPERVISECALL_
                                          				  INVALID_SUPERVISOR_ CONNECTION3 | JTAPI Gateway – Error on SUPERVISE operation –
                                          				  Invalid Supervisor connection. | The connection ID in the agent object is
                                          				  invalid (method "DirectSupervisorBargeIn" class ThreadSuperviseCall). |
| 13119 PERERR_GW_E_THREAD SUPERVISECALL_
                                          				  INVALID_SUPERVISOR_ CONNECTION4 | JTAPI Gateway – Error on SUPERVISE operation –
                                          				  Invalid Supervisor connection. | The connection ID in the agent object is
                                          				  invalid (method "BargeInBlindTransferCall" class ThreadSuperviseCall). |
| 13120 PERERR_GW_E_THREAD SUPERVISECALL_
                                          				  SUPERVISOR_NOT_TALKING | JTAPI Gateway – Error on SUPERVISE operation –
                                          				  Supervisor Connection not TALKING. | The supervisor's connection is not in the
                                          				  talking state (method "DirectSupervisorBargeIn" class ThreadSuperviseCall). |
| 13121 PERERR_GW_E_THREAD TRANSFERCALL_
                                          				  ACTIVE_CONN_NOT_TALKING | JTAPI Gateway – Error on SUPERVISE operation –
                                          				  Connection not TALKING. | The connection is not in the talking state
                                          				  (method "BargeInCall" class ThreadSuperviseCall). |
| 13122 PERERR_GW_E_ THREADTRANSFERCALL_
                                          				  EXCEPTION_SETTRANSFER CONTROLLER | JTAPI Gateway – Error on SUPERVISE operation –
                                          				  Exception. | The method "run" in class ThreadTransferCall got
                                          				  an exception on a call to "setTransferController". |
| 13123 PERERR_GW_E_THREAD TRANSFERCALL_
                                          				  EXCEPTION_TRANSFER1 | JTAPI Gateway – Error on SUPERVISE operation –
                                          				  Exception. | The method "run" in class ThreadTransferCall got
                                          				  an exception on a call to "transfer" with the HELD call specified. |
| 13124 PERERR_GW_E_THREAD TRANSFERCALL_
                                          				  EXCEPTION_TRANSFER2 | JTAPI Gateway – Error on SUPERVISE operation –
                                          				  Exception. | Got an exception on a call to "transfer" with the ACTIVE call
                                             					 specified (method "run" in class ThreadTransferCall). |
| 13125 PERERR_GW_E_THREAD TRANSFERCALL_
                                          				  HELD_CONN_NOT_HELD | JTAPI Gateway – Error on TRANSFER operation
                                          				  HELD connection not HELD. | The connection passed for the held connection
                                          				  is not in the HELD state. |
| 13126 PERERR_GW_E_THREAD TRANSFERCALL_
                                          				  INVALID_ACTIVE_ CONNECTION | JTAPI Gateway – Error on TRANSFER operation –
                                          				  No ACTIVE. | The connection specified in the active
                                          				  connection does not exist. |
| 13127 PERERR_GW_E_THREAD TRANSFERCALL_
                                          				  INVALID_HELD_ CONNECTION | JTAPI Gateway – Error on TRANSFER operation
                                          				  Invalid HELD connection. | The connection ID in the agent object is
                                          				  invalid. |
| 20000 PERERR_CM_UNSPECIFIED | An unspecifiedCall Manager – error occurred on
                                          				  the operation. |  |
| 20001 PERERR_CM_TIMEOUT | A time-out CallManager – occurred on the
                                          				  operation. | An operation exceeded the time limit that was
                                          				  configured/allocated for that operation. |
| 20002 PERERR_CM_NO_ACTIVE_ DEVICE_
                                          				  FOR_THIRDPARTY | CallManager – Undescribed Error. |  |
| 20003 PERERR_CM_EXISTING_ FIRSTPARTY | CallManager – Line was specified that was not
                                          				  found. |  |
| 20004 PERERR_CM_ILLEGAL_ HANDLE | CallManager – Handle is unknown to the system. |  |
| 20005 PERERR_CM_UNDEFINED_ LINE | CallManager – Undescribed Error. |  |
| 20006 PERERR_CM_ILLEGAL_ CALLINGPARTY | CallManager – Attempt to originate call using
                                          				  a calling party that is not on the device. |  |
| 20007 PERERR_CM_CALL_ ALREADY_EXISTS | CallManager – Another call already exists on
                                          				  the line. |  |
| 20008 PERERR_CM_ LINECONTROL_FAILURE | CallManager – Line control refuses to let a
                                          				  new call because of its state (probably bug). |  |
| 20009 PERERR_CM_ILLEGAL_ CALLSTATE | CallManager – Line is not in a legal state to
                                          				  invoke the command. |  |
| 20010 PERERR_CM_ CALLHANDLE_ NOTINCOMINGCALL –
                                          				  CallManager | Attempt to answer a call that either does not
                                          				  exist or is not in the correct state. |  |
| 20011 PERERR_CM_ TRANSFERFAILED_ DESTINATION_
                                          				  UNALLOCATED | CallManager – Attempt to transfer to a
                                          				  directory number that is not registered. |  |
| 20013 PERERR_CM_ TRANSFERFAILED_
                                          				  DESTINATION_BUSY | CallManager – Attempt to transfer to a busy
                                          				  destination. |  |
| 20014 PERERR_CM_ TRANSFERFAILED | CallManager – Transfer failed. | Probable cause is one of the call legs was
                                          				  hung up or disconnected from the far end. |
| 20015 PERERR_CM_HOLDFAILED | CallManager – Hold was rejected by line
                                          				  control or call control. |  |
| 20017 PERERR_CM_RETRIEVE FAILED | CallManager – Retrieve was rejected by line
                                          				  control or call control. |  |
| 20018 PERERR_CM_DB_NO_ MORE_DEVICES | CallManager – Error No longer used. |  |
| 20020 PERERR_CM_DB_ILLEGAL_ DEVICE_TYPE | CallManager – Error No longer used. |  |
| 20021 PERERR_CM_DB_ERROR | CallManager – Device query contained an
                                          				  illegal device type. |  |
| 20022 PERERR_CM_CANNOT_ TERMINATE_MEDIA_ON_
                                          				  PHONE | CallManager – Media cannot be terminated by an
                                          				  application when the device has a physical phone (the phone always terminates
                                          				  the media). |  |
| 20025 PERERR_CM_UNKNOWN_ GLOBAL_CALL_HANDLE | CallManager – Error no longer used. |  |
| 20026 PERERR_CM_DEVICE_ NOT_OPEN | CallManager – Command issued on a line that
                                          				  must be open. |  |
| 20027 PERERR_CM_ASSOCIATED_ LINE_NOT_OPEN | CallManager – Undescribed Error. |  |
| 20028 PERERR_CM_SSAPI_NOT_ REGISTERED | CallManager – Redirect command was issued when
                                          				  the internal supporting interface was not initialized. |  |
| 20029 PERERR_CM_REDIRECT_ CALL_DOES_NOT_EXIST | CallManager – Attempt to redirect a call that
                                          				  does not exist or is no longer active. |  |
| 20048 PERERR_CM_REDIRECT_ CALLINFO_ERR | CallManager – Internal error returned from
                                          				  call control. |  |
| 20049 PERERR_CM_REDIRECT_ ERR | CallManager – Internal error returned from
                                          				  call control. |  |
| 20050 PERERR_CM_REDIRECT_ CALL_CALL_TABLE_FULL | CallManager – Internal error returned from
                                          				  call control. |  |
| 20051 PERERR_CM_REDIRECT_ CALL_PROTOCOL_ERROR | CallManager – Internal error returned from
                                          				  call control. |  |
| 20052 PERERR_CM_REDIRECT_ CALL_UNKNOWN_
                                          				  DESTINATION | CallManager – Attempt to redirect to an
                                          				  unknown destination. |  |
| 20053 PERERR_CM_REDIRECT_ CALL_DIGIT_ANALYSIS_
                                          				  TIMEOUT | CallManager – Internal error returned from
                                          				  call control |  |
| 20054 PERERR_CM_REDIRECT_ CALL_MEDIA_
                                          				  CONNECTION_FAILED | CallManager – Internal error returned from
                                          				  call control. |  |
| 20055 PERERR_CM_REDIRECT_
                                          				  CALL_PARTY_TABLE_FULL | CallManager – Internal error returned from
                                          				  call control. |  |
| 20056 PERERR_CM_REDIRECT_ CALL_ORIGINATOR_
                                          				  ABANDONED | CallManager – Far end hung up on the call
                                          				  being redirected. |  |
| 20057 PERERR_CM_REDIRECT_ CALL_UNKNOWN_PARTY | CallManager – Internal error returned from
                                          				  call control. |  |
| 20058 PERERR_CM_REDIRECT_ CALL_INCOMPATIBLE_
                                          				  STATE | CallManager – Internal error returned from
                                          				  call control. |  |
| 20059 PERERR_CM_REDIRECT_
                                          				  CALL_PENDING_REDIRECT_ TRANSACTION | CallManager – Internal error returned from
                                          				  call control. |  |
| 20060 PERERR_CM_REDIRECT_ CALL_UNKNOWN_ERROR | CallManager – Internal error returned from
                                          				  call control. |  |
| 20061 PERERR_CM_REDIRECT_ CALL_NORMAL_CLEARING | CallManager – Internal error returned from
                                          				  call control. |  |
| 20062 PERERR_CM_REDIRECT_ CALL_UNRECOGNIZED_
                                          				  MANAGER | CallManager – Internal error returned from
                                          				  call control. |  |
| 20063 PERERR_CM_REDIRECT_
                                          				  CALL_DESTINATION_BUSY | CallManager – Redirect destination is busy. |  |
| 20064 PERERR_CM_REDIRECT_
                                          				  CALL_DESTINATION_OUT_ OF_ORDER | CallManager – Redirect destination is out of
                                          				  order. |  |
| 20065 PERERR_CM_CANNOT_ OPEN_DEVICE | CallManager – Device open failed because the
                                          				  associated device is shutting down (unregistering). |  |
| 20066 PERERR_CM_TRANSFER FAILED_OUTSTANDING_
                                          				  TRANSFER | CallManager – Existing transfer still in
                                          				  progress. |  |
| 20067 PERERR_CM_TRANSFER FAILED_CALLCONTROL_
                                          				  TIMEOUT | CallManager – Expected response from call
                                          				  control not received during a transfer. |  |
| 20068 PERERR_CM_CALLHANDLE_ UNKNOWN_TO_
                                          				  LINECONTROL | CallManager – Attempt to redirect call that
                                          				  was unknown to line control. |  |
| 20069 PERERR_CM_OPERATION_ NOT_AVAILABLE_IN_
                                          				  CURRENT_STATE | CallManager – Undescribed Error. |  |
| 20070 PERERR_CM_ CONFERENCE_FULL | CallManager – Undescribed Error. |  |
| 20071 PERERR_CM_MAX_ NUMBER_OF_CTI_
                                          				  CONNECTIONS_REACHED | CallManager – Undescribed Error. |  |
| 20080 PERERR_CM_ INCOMPATIBLE_
                                          				  PROTOCOL_VERSION | CallManager – Undescribed Error. |  |
| 20081 PERERR_CM_ UNRECOGNIZABLE_PDU | CallManager – QBE protocol error (bug). |  |
| 20082 PERERR_CM_ILLEGAL_ MESSAGE_FORMAT | CallManager – QBE protocol error (bug). |  |
| 20094 PERERR_CM_DIRECTORY_
                                          				  TEMPORARY_UNAVAILABLE | CallManager – Undescribed Error. |  |
| 20095 PERERR_CM_DIRECTORY_ LOGIN_NOT_ALLOWED | CallManager – Undescribed Error. |  |
| 20096 PERERR_CM_DIRECTORY_ LOGIN_FAILED | CallManager – Login to the directory server
                                          				  failed when opening the provider. |  |
| 20097 PERERR_CM_PROVIDER_ NOT_OPEN | CallManager – Attempt to issue a CTI command
                                          				  before the provider was open. |  |
| 20098 PERERR_CM_PROVIDER_ ALREADY_OPEN | CallManager – Attempt to reopen a provider. |  |
| 20099 PERERR_CM_NOT_ INITIALIZED | CallManager – Attempt to open a provider
                                          				  before CTI initialization completes. |  |
| 20100 PERERR_CM_CLUSTER_ LINK_FAILURE | CallManager – Link failed to one of the call
                                          				  managers in the cluster (network error). |  |
| 20101 PERERR_CM_LINE_INFO_ DOES_NOT_EXIST | CallManager – Undescribed Error. |  |
| 20102 PERERR_CM_DIGIT_ GENERATION_ALREADY_IN_
                                          				  PROGRESS | CallManager – Undescribed Error. |  |
| 20103 PERERR_CM_DIGIT_ GENERATION_WRONG_
                                          				  CALL_HANDLE | CallManager – Undescribed Error. |  |
| 20104 PERERR_CM_DIGIT_ GENERATION_WRONG_
                                          				  CALL_STATE | CallManager – Undescribed Error. |  |
| 20105 PERERR_CM_DIGIT_ GENERATION_CALLSTATE_
                                          				  CHANGED | CallManager – Undescribed Error. |  |
| 20112 PERERR_CM_RETRIEVE
                                          				  FAILED_ACTIVE_CALL_ON_ LINE | CallManager – Undescribed Error. |  |
| 20113 PERERR_CM_INVALID_LINE_ HANDLE | CallManager – Undescribed Error. |  |
| 20114 PERERR_CM_LINE_NOT_ PRIMARY | CallManager – Undescribed Error. |  |
| 20115 PERERR_CM_CFWDALL_ ALREADY_SET | CallManager – Undescribed Error. |  |
| 20116 PERERR_CM_CFWDALL_ DESTN_INVALID | CallManager – Undescribed Error. |  |
| 20117 PERERR_CM_CFWDALL_ ALREADY_OFF | CallManager – Undescribed Error. |  |
| 20119 PERERR_CM_DEVICE_OUT_ OF_SERVICE | CallManager – Undescribed Error. |  |
| 20120 PERERR_CM_MSGWAITING_ DESTN_INVALID | CallManager – Undescribed Error. |  |
| 20121 PERERR_CM_DARES_ INVALID_REQ_TYPE | CallManager – Undescribed Error. |  |
| 20122 PERERR_CM_ CONFERENCE_ FAILED | CallManager – Undescribed Error. |  |
| 20123 PERERR_CM_ CONFERENCE_INVALID_
                                          				  PARTICIPANT | CallManager – Undescribed Error. |  |
| 20124 PERERR_CM_ CONFERENCE_ALREADY_ PRESENT | CallManager – Undescribed Error. |  |
| 20125 PERERR_CM_ CONFERENCE_INACTIVE | CallManager – Undescribed Error. |  |
| 20126 PERERR_CM_TRANSFER_ INACTIVE | CallManager – Undescribed Error. |  |
| 20153 PERERR_CM_COMMAND_ NOT_IMPLEMENTED_ON_
                                          				  DEVICE | CallManager – Device does not support the
                                          				  command. | Undescribed Error. |
| 20512 PERERR_CM_PROVIDER_ CLOSED | CallManager – Undescribed Error. |  |
| 20513 PERERR_CM_PROTOCOL_ TIMEOUT | CallManager – Undescribed Error. |  |
| 24095 PERERR_CM_GENERAL | CallManager – Unknown CallManager Failure on
                                          				  Operation. | An error response was received for a request
                                          				  issued to the call manager, but no error code could be extracted. This is
                                          				  always the case in the Encore Release. Please refer to the JTAPI log for more
                                          				  information. |

| Status Value (hex/dec) | Description |
|---|---|
| Invalid Parameters |
| 0A00 / 2560 | Invalid calling TN |
| 0A01 / 2561 | Invalid calling DN; wrong DN specified |
| 0A02 / 2562 | Incomplete calling DN |
| 0A03 / 2563 | Invalid called DN |
| 0A04 / 2564 | Incomplete called DN |
| 0A05 / 2565 | Invalid called TN |
| 0A06 / 2566 | Invalid origination manner |
| 0A07 / 2567 | Invalid destination manner |
| 0A08 / 2568 | Invalid origination user type |
| 0A09 / 2569 | Invalid customer number |
| 0A0A / 2570 | System or data base error |
| Unsuccessful Call Origination |
| 0B00 / 2816 | Origination party busy |
| 0B01 / 2817 | Origination resource blocking |
| 0B02 / 2818 | Origination set is maintenance busy |
| 0B03 / 2819 | 500/2500 set is onhook |
| 0B04 / 2820 | Origination DN busy |
| 0B05 / 2821 | Origination is ringing |
| 0B06 / 2822 | Unable to disconnect origination (that is, already
                                                					 disconnected) |
| 0B07 / 2823 | Origination access restriction blocking |
| 0B08 / 2824 | Origination call on permanent hold |
| 0B0A / 2826 | System or data base error |
| 0B0B / 2827 | Origination receiving end to end signaling |
| 0B0C / 2828 | The call is currently in an ACD queue |
| 0B0E / 2830 | Origination set invoked hold |
| 0B14 / 2836 | Transfer key not configured |
| 0B15 / 2837 | Transfer key not idle |
| 0B16 / 2838 | Set active in conference call |
| 0B17 / 2839 | Transfer or MPO/TSA class of service not configured |
| 0B18 / 2840 | Cannot put call on hold |
| 0B1D / 2845 | No active call exists on set |
| 0B1E / 2846 | No held call exists on set |
| Unsuccessful Call Termination |
| 0C00 / 3072 | Terminating party is busy |
| 0C01 / 3073 | Destination resource blocking |
| 0C02 / 3074 | Destination in invalid state |
| 0C07 / 3079 | Destination access restriction blocking |
| 0D0A / 3338 | System or database error |
| Network Interceptions |
| 0C08 / 3080 | Unassigned number |
| 0C09 / 3081 | No route to destination |
| 0C0A / 3082 | No user responding |
| 0C0B / 3083 | Number changed |
| 0C0C / 3084 | Destination out of service |
| 0C0D / 3085 | Invalid number format |
| 0C0E / 3086 | No circuit available |
| 0C0F / 3087 | Network out of order |
| 0C10 / 3088 | Temporary failure |
| 0C11 / 3089 | Equipment congestion |
| Network Interceptions with In-Band Information |
| 0C19 / 3097 | Terminating party is busy |
| 0C1A / 3098 | Unassigned number |
| 0C1B / 3099 | No route to destination |
| 0C1C / 3100 | No user responding |
| 0C1D / 3101 | Number changed |
| 0C1E / 3102 | Destination out of service |
| 0C1F / 3103 | Invalid number format |
| 0C20 / 3104 | No circuit available |
| 0C21 / 3105 | Network out of order |
| 0C22 / 3106 | Temporary failure |
| 0C23 / 3107 | Equipment congestion |
| 0C24 / 3108 | Interworking, unspecified |
| 0CFE / 3326 | Other cause |
| Unsuccessful Conference or Transfer Operation |
| 0D00 / 3328 | Cannot complete conference |
| 0D01 / 3329 | Cannot initiate transfer |
| 0D02 / 3330 | Cannot complete transfer |
| 0D03 / 3331 | Cannot retrieve original call |
| 0D04 / 3332 | Fast Transfer initiation failed |
| 0D05 / 3333 | Fast Transfer completion failed |
| 0D0B / 3339 | Hold Request failed |

| Cause Value (hex/dec) | Description |
|---|---|
| 1002 / 4098 | Access restricted |
| 1003 / 4099 | Resource unavailable |
| 1004 / 4100 | Invalid customer number |
| 1005 / 4101 | Invalid origination address |
| 1006 / 4102 | Invalid destination address |
| 1007 / 4103 | Invalid manner |
| 1008 / 4104 | Unsuccessful retrieve original |
| 1009 / 4105 | Unsuccessful transfer |
| 100A / 4106 | Unsuccessful conference |
| 100B / 4107 | Unsuccessful answer request |
| 100C / 4108 | Unsuccessful release request |
| 1070 / 4208 | Refer to Connection Status IE |
| 2004 / 8196 | The target DN is invalid |
| 2005 / 8197 | The target DN is not AST |
| 2006 / 8198 | The Customer Number is invalid |
| 2007 / 8199 | The feature could not be invoked |
| 2008 / 8200 | The feature is not configured on the set |
| 2009 / 8201 | The requested feature is out of valid range |
| 200A / 8202 | The target set is not ACD agent |
| 200B / 8203 | The target set is a Virtual Agent |
| 200C / 8204 | The set is maintenance busy |
| 200D / 8205 | Set is in wrong state for invocation |
| 200E / 8206 | Set is in target state |
| 200F / 8207 | No NRDY/RDY while ACD set is logged out |
| 2010 / 8208 | Package C customer cannot use NRDY with IDN call |
| 2011 / 8209 | Feature IE is missing or invalid |
| 2012 / 8210 | DN IE is missing or invalid |
| 2013 / 8211 | Agent ID IE is missing or invalid |
| 2014 / 8212 | Agent ID is invalid |
| 2015 / 8213 | CFW DN IE is invalid |
| 2016 / 8214 | The Call Forward DN is too long |
| 2017 / 8215 | The Call Forward DN is invalid |
| 2018 / 8216 | User is invoking Call Forward |
| 2019 / 8217 | MSB/MSI not supported for 500/2500 sets |
| 201A / 8218 | 500/2500 ACD agent already changed status |
| 201B / 8219 | 500/2500 ACD agent set is being rung |
| 201C / 8220 | User is manually logging in 500 /2500 ACD set |

| Note | The Swap feature is
                                                   			 not supported when CTI OS is used with the Avay Aura Contact Center (Symposium). |
|---|---|

| State | Peripheral-Specific Equivalent |
|---|---|
| Available The agent is
                                             					 ready to accept a call. | Aspect Contact Server: Avail Avaya DEFINITY ECS: AVAIL Avaya Aura CC
                                                						(Symposium): Idle |
| BusyOther The agent is
                                             					 busy performing a task associated with another active Skill Group. | Aspect Contact Server: MSG (if Aspect Event Link is not being used) Avaya DEFINITY ECS: OTHER Avaya Aura CC
                                                						(Symposium): No equivalent |
| Hold The agent
                                             					 currently has all calls on hold. | Aspect Contact Server: HOLD Avaya DEFINITY ECS: No
                                             					 equivalent Avaya Aura CC (Symposium): On Hold, On Hold Walkaway |
| Login The agent
                                             					 has logged in to the ACD. It does not necessarily indicate that the agent is
                                             					 ready to accept calls. | Although
                                             					 viewed as a state by CTI Server, this state is more of an event, and
                                             					 is not treated as a state by the switches. |
| Logout The agent
                                             					 has logged out of the ACD and cannot accept any additional calls. | Aspect Contact Server: Signed Off Avaya DEFINITY ECS: No
                                             					 equivalent Avaya Aura CC
                                                						(Symposium): Logout |
| NotReady The agent is
                                             					 logged in but is unavailable for any call work. | Aspect Contact Server: Idle Avaya DEFINITY ECS: AUX Avaya Aura CC
                                                						(Symposium): Not Ready Walkaway (however, this state requires the agent to click
                                             					 Hold and physically unplug the headset – because a physical act is involved, a
                                             					 software request to set the agent state to NotReady fails), Emergency |
| Reserved The agent
                                             					 is reserved for a call that arrives at the ACD shortly. | Aspect
                                                						Contact Server: RSVD Avaya
                                                						DEFINITY ECS: No equivalent Avaya
                                                						Aura CC (Symposium): Call Presented |
| Talking The agent
                                             					 is currently talking on a call (inbound, outbound, or inside). | Aspect
                                                						Contact Server: Talking ACD1, Talking ACD2, Talking ACT1, Talking ACT2,
                                             					 Talking Out1, Talking Out2, Talking Inside, Supervisor Line, MSG, HELP (MSG and
                                             					 HELP correspond to Talking only if Aspect Event Link is being used.) Avaya
                                                						DEFINITY ECS: AUX-IN, AUX-OUT, ACD-IN, ACD-OUT, ACW-IN, ACW-OUT, DACD Avaya
                                                						Aura CC (Symposium): Active, Consultation |
| Unknown The agent
                                             					 state is currently unknown. | Aspect
                                                						Contact Server: No equivalent Avaya
                                                						DEFINITY ECS: UNKNOWN Avaya
                                                						Aura CC (Symposium): No equivalent |
| WorkNotReady The agent
                                             					 is performing after-call work and is not ready to receive a call after the work
                                             					 is complete. | Aspect
                                                						Contact Server: No equivalent Avaya
                                                						DEFINITY ECS: No equivalent Avaya
                                                						Aura CC (Symposium): No equivalent |
| WorkReady The agent
                                             					 is performing after-call work and is ready to receive a call after the work is
                                             					 complete. | Aspect
                                                						Contact Server: Wrap-up Avaya
                                                						DEFINITY ECS: ACW, DACW Avaya
                                                						Aura CC (Symposium): Not Ready, Break, Busy |