---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-icm-enterprise-icm-enterprise-12-6-2-user-ucce-b-f2aab26e95
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/icm_enterprise/icm_enterprise_12_6_2/user/ucce_b_1262_outbound_options_guide/ucce_m_1262_dialer-detail-table.html
retrieved_at: 2026-08-16T20:33:10.523882+00:00
---

Outbound Option Guide for Unified Contact Center Enterprise, Release 12.6(2)

# Outbound Option Guide for Unified Contact Center Enterprise, Release 12.6(2)

Updated: August 19, 2025

Chapter: Dialer Detail Table

## Chapter: Dialer Detail Table

# Dialer Detail Table

## About the
                        	 Dialer_Detail Table

The Dialer_Detail table is a historical table that is present in the Unified CCE database in Releases 7.2(2) and later. Its
                              purpose is to allow detailed dialer records to be written to the Logger databases and replicated to each HDS database.

This table can become very large. Running custom reporting queries against it while it is on the HDS can degrade performance. To optimize performance, extract the data from the HDS into your own custom database on a separate server (one that is not
                              used for other CCE components). Use only DBDateTime (date and time of the record that was written to the HDSdatabase) to perform the extraction.
                              The table on the custom database can be indexed according to the custom reporting needs.

### Advantages

Data stored in this table helps in managing the system and generating custom reports.

For example, the table stores the following information:

The Account Number for the contact and the Call Result, so that the last termination
                                       code can be obtained for each contact.

An identifier for the Agent so that callbacks scheduled by each agent can be determined.

Additional data for troubleshooting of Outbound Dialer attempts, such as the CallID that was used to place the call.

### Data Flow

After making an attempt to contact a customer, the Dialer sends the results to the
                                       Campaign Manager in a CloseCustomerRecord message.

Results for Personal Callback attempts are sent to the Campaign Manager using a ClosePersonalCallbackRecord message.

Campaign Manager then sends a Dialer Detail record to the Router.

At this point, the message flow is identical to all other historical data in the
                                       system.

The Router passes the historical data information to the Historical Logger
                                       process.

The Historical Logger process commits the data to the Logger database.

The Replication process on the Logger passes the historical data to the Replication
                                       process on the Historical Data Server (HDS).

The Replication process on the HDS commits the data to the HDS database.

### Fault Tolerance

When the Router is down or the Campaign Manager loses the connection to the Router, the
                                 Campaign Manager stores Dialer_Detail records in a file on the server where Campaign Manager
                                 is running. All the Dialer_Detail records in the cached file are sent to the Router when the
                                 connection is restored.

## Dialer_Detail Table Database Fields and Descriptions

For a full description of the database fields for the Dialer_Detail table, see the Database Schema Handbook for Cisco Unified Contact Center Enterprise .

### CallResult Codes
                           	 and Values

The CallResult
                                 		  field can be populated with the following values:

Value

Description

0

Dialer has not yet attempted to contact that customer record

2

Error condition while dialing

3

Number reported not in service by network

4

No ringback from network when dial attempted

5

Operator intercept returned from network when dial attempted

6

No dial tone when dialer port went off hook

7

Number reported as invalid by the network

8

Customer phone did not answer

9

Customer phone was busy

10

Customer answered and was connected to agent

11

Fax machine detected

12

Answering machine detected

13

Dialer stopped dialing customer due to lack of agents or network stopped dialing before it was complete

14

Customer requested callback

15

Answering machine requested callback

16

Call was abandoned by the dialer due to lack of agents

17

Failed to reserve agent for personal callback.

18

Agent rejected a preview call or personal callback call.

19

Agent rejected a preview call with the close option.

20

Customer has been abandoned to an IVR

21

Customer dropped call within configured abandoned time

22

In Unified CCE, the call
                                             									result indicates an answering machine detection which did not
                                             									meet termination conditions. One such example is a network
                                             									voicemail message indicating a mailbox is full or not setup
                                             									properly. In TDM switches, it indicates a network answering
                                             									machine detection, such as a network voicemail.

23

Number successfully contacted but wrong number

24

Number successfully contacted but reached the wrong person

25

The following circumstances are reported where a call record is returned from the dialer without being attempted:

The campaign is disabled.

The outbound percentage for the campaign skill group is set to zero in an admin script.

With personal callback in certain situations where the agent is logged out or not available before the configured CallbackTimeLimit
                                                   is exceeded.

26

The number was on the do not call list

27

Call disconnected by the carrier or the network while ringing

28

Dead air or low voice volume call

29

SIP message received from dialer is not supported by voice gateway.

30

SIP message received from dialer is not authorized by voice gateway.

31

Invalid sip message sent by dialer to voice gateway.

32

Call cancelled because the dialer lost connection with the Campaign Manager.

33

Agent timed-out accepting preview or personal callback call.

This Call Result is supported from 12.0 ES33 onwards.

### CallStatusZone
                           	 Values

The CallStatusZone1
                                 		  and CallStatusZone2 fields can be populated with the following values that show
                                 		  the current status of the customer record for the zone.

For campaigns created using API, CallStatusZone2 is not applicable.

The values are:

Value

Description

A

Active:
                                             					 Stored in CallStatusZoneX (1 or 2). A zone is set to active when it has been
                                             					 sent to a dialer for dialing.

B

A callback
                                             					 was requested. Stored in CallStatusZone1 and CallStatusZone2 field when a
                                             					 regular callback (non personal callback) has been scheduled. The Callback time
                                             					 itself is stored in both the CallbackDateTimeZone1 and CallbackDateTimeZone2
                                             					 columns since the callback overrides the individual zones.

C

Closed:
                                             					 Record has been closed for that particular zone, so the record will not be
                                             					 retried again for that zone (zone1 or zone2).

D

Dialed.
                                             					 Record has been dialed for that particular zone.

F

F= Fax Machine. Stored in CallStatusZoneX (1 or 2)

L

L = Not Allocated. Invalid number used for a Personal Callback.

J

Agent
                                             					 rejected (closed out the record)

M

The maximum
                                             					 number of attempts has been reached. Stored in both CallStatusZone1 and
                                             					 CallStatusZone2. A record is set to "M" when
                                             					 it has dialed the maximum times as specified in the campaign and will not be
                                             					 retried again. Both zones are set to "M" to
                                             					 indicate no further calling in either zone.

P

Pending.
                                             					 Stored in CallStatusZoneX (1 or 2). This is the initial state of a record
                                             					 before any dialing has taken place. The record remains in the pending state for
                                             					 a particular zone until all of the numbers specified for that zone are dialed.
                                             					 A pending contact which has already dialed at least one dialer from its
                                             					 sequence will have at least one CallBackDateTimeXX column filled in with a
                                             					 retry time.

R

Retry.
                                             					 Stored in CallStatusZoneX (1 or 2) for the zone where the Retry is scheduled.
                                             					 The retry time itself is stored in the CallbackDateTimeZoneX (1 or 2) as well
                                             					 as in the individual number column CallbackDateTimeXX, where XX is the number
                                             					 to be retried (01 - 10). Call can be retried for a variety of reasons,
                                             					 including receiving a busy or no answer result.

This value will be updated once all phones of the record are dialed out.

S

A personal
                                             					 callback was requested. Stored in both CallStatusZone1 and CallStatusZone2. A
                                             					 record is set to "S" when
                                             					 it has been scheduled for a personal callback. Both zones are set to "S" to
                                             					 indicate that the record has been moved to the personal callback list.

U

Unknown:
                                             					 Stored in CallStatusZone1 and CallStatusZone2. A record is set to Unknown if
                                             					 its status was Active when the Campaign Manager started or the Dialer
                                             					 re-started. The record will stay in the Unknown state until it gets an update.
                                             					 If the Campaign Manager fails to get an update within sixty minutes, it will
                                             					 return the record to Pending.

X

For a
                                             					 personal callback, the agent is not available, and the reschedule mode is
                                             					 Abandon. (This value is used for CallStatusZone1 only.)

### DialingMode Values

The DialingMode field can be populated with the following values that show the campaign
                                 mode for the call. This field is NULL for Do Not Call entries.

Values are shown in the following table.

Value

Description

1

Predictive only

2

Predictive blended

3

Preview only

4

Preview blended

5

Progressive only

6

Progressive blended

7

Direct preview only

8

Direct preview blended

### Mode types and definitions

The following table lists the mode definitions:

Mode

Definition

N

None

P

Preview

D

Preview Direct

R

Predictive

G

Progressive

A

Callback

### CallResults
                           	 Table

The following
                                 		  CallResults table maps the call result to the campaign call report.

Call Result

Description

Reporting Column

Counted as Attempt?

Detected Live Voice?

Retry Action

2

Error condition while dialing

None

No

No

Regular outbound calls are not retried and are returned to the closed state.

Callback calls are retried as Dialer Abandoned.

3

Number reported not in service by network

None

Yes

No

None

5

Operator intercept returned from network when dial attempted

SITTone

Yes

No

None

6

No dial tone when dialer port went off hook

NoDialTone

Yes

No

No answer

7

Number reported as invalid by the network

SITTone

Yes

No

None

8

Customer phone did not answer

NoAnswer

No

No

No answer

9

Customer phone was busy

Busy

Yes

No

Busy

10

Customer answered and was connected to agent

Voice

Yes

Yes

None

11

Fax machine detected

Fax

Yes

No

None

12

Answering machine detected

AnsweringMachine

Yes

No, but transfer to agent possible

Answering Machine, if needed

13

Dialer stopped dialing customer due to lack of agents or network stopped dialing before it was complete.

Cancelled

Yes

No

Dialer Abandoned

14

Customer requested callback

Callback & PersonalCallback

Yes

Yes

None

15

Answering machine requested callback

Callback & PersonalCallback

Yes

No

None

16

Call was abandoned by the dialer due to lack of agents

Abandon

Yes

Yes

Dialer Abandoned

17

Failed to reserve agent for personal callback

None

No

No

Based on the callback mode configuration.

For more details, see About Personal Callbacks

18

Agent has rejected a preview call or personal callback call

AgentRejected

No

No

For Preview calls: No Answer.

For Personal Callback calls: None.

19

Agent has rejected a preview call with the close option

AgentClosed

No

No

None

20

Customer has been abandoned to an IVR

AbandonToIVR

Yes

Yes

Dialer Abandoned, if needed

21

Customer dropped call within configured abandoned time

CustomerAbandon

Yes

Yes

Customer Abandoned

22

Mostly used with TDM switches - network answering machine, such as a network voicemail

NetworkAnsMachine

Yes

No

Answering Machine, if needed

23

Number successfully contacted but wrong number

WrongNumber

Yes

Yes

None

24

Number successfully contacted but reached the wrong person

CustomerNotHome

Yes

Yes

Customer not home

25

The following circumstances are reported where a call record is returned from the dialer without being attempted:

The campaign is disabled.

The outbound percentage for the campaign skill group is set to zero in an admin script.

With personal callback in certain situations where the agent is logged out or not available before the configured CallbackTimeLimit
                                                   is exceeded.

None

No

No

None, but returned to the pending state

26

The number was on the do not call list

None

No

No

None

27

Network disconnected while alerting

NoRingBack

No

No

No answer

28

Low Energy or Dead Air call detected by CPA

NoRingBack

No

No

No answer

29

SIP message received from dialer is not supported by voice gateway

30

SIP message received from dialer is not authorized by voice gateway

31

Invalid sip message sent by dialer to voice gateway

32

Call cancelled because the dialer lost connection with the Campaign Manager

Cancelled

Yes

No

None

33

Agent timed-out accepting preview or personal callback call

This Call Result is supported from 12.0 ES33 onwards.

None

No

No

No Answer

Only based on the PersonalCallbackReattempt registry settings in the CampaignManager, the callback requests with CallResults
                                             values 2,4,6,8,9, and 16 are not counted as attempted. Such callback records are immediately closed with callStatus as C and no redialing occurs

### Outbound dialer call
                              	 result for combinations of PSTN and status code

The following
                                 		  dialer call results corresponds to the combinations of PSTN cause code and
                                 		  Status code specified in the Dialer_ Detail table.

Status code:
                                 		  Status code is a 3-digit integer result code that indicates the outcome of an
                                 		  attempt to understand and satisfy a SIP request.

PSTN cause code:
                                 		  In signaling context, PSTN cause codes are used to indicate certain events or
                                 		  conditions in the network.

CheckCallState: Indicates whether the call is active or not . TRUE
                                 		  value implies that the call is active.

CallState: Indicates the intermediate call state. When a call is
                                 		  active, it can have any one of the following values - CS_INITIATED, CS_ALERTED,
                                 		  and CS_CONNECTED.

DialerCallResult: Indicates the SIP Dialer call result for the
                                 		  respective SIP status code and PSTN cause code.

| Value | Description |
|---|---|
| 0 | Dialer has not yet attempted to contact that customer record |
| 2 | Error condition while dialing |
| 3 | Number reported not in service by network |
| 4 | No ringback from network when dial attempted |
| 5 | Operator intercept returned from network when dial attempted |
| 6 | No dial tone when dialer port went off hook |
| 7 | Number reported as invalid by the network |
| 8 | Customer phone did not answer |
| 9 | Customer phone was busy |
| 10 | Customer answered and was connected to agent |
| 11 | Fax machine detected |
| 12 | Answering machine detected |
| 13 | Dialer stopped dialing customer due to lack of agents or network stopped dialing before it was complete |
| 14 | Customer requested callback |
| 15 | Answering machine requested callback |
| 16 | Call was abandoned by the dialer due to lack of agents |
| 17 | Failed to reserve agent for personal callback. |
| 18 | Agent rejected a preview call or personal callback call. |
| 19 | Agent rejected a preview call with the close option. |
| 20 | Customer has been abandoned to an IVR |
| 21 | Customer dropped call within configured abandoned time |
| 22 | In Unified CCE, the call
                                             									result indicates an answering machine detection which did not
                                             									meet termination conditions. One such example is a network
                                             									voicemail message indicating a mailbox is full or not setup
                                             									properly. In TDM switches, it indicates a network answering
                                             									machine detection, such as a network voicemail. |
| 23 | Number successfully contacted but wrong number |
| 24 | Number successfully contacted but reached the wrong person |
| 25 | The following circumstances are reported where a call record is returned from the dialer without being attempted: The campaign is disabled. The outbound percentage for the campaign skill group is set to zero in an admin script. With personal callback in certain situations where the agent is logged out or not available before the configured CallbackTimeLimit
                                                   is exceeded. |
| 26 | The number was on the do not call list |
| 27 | Call disconnected by the carrier or the network while ringing |
| 28 | Dead air or low voice volume call |
| 29 | SIP message received from dialer is not supported by voice gateway. |
| 30 | SIP message received from dialer is not authorized by voice gateway. |
| 31 | Invalid sip message sent by dialer to voice gateway. |
| 32 | Call cancelled because the dialer lost connection with the Campaign Manager. |
| 33 | Agent timed-out accepting preview or personal callback call. Note This Call Result is supported from 12.0 ES33 onwards. | Note | This Call Result is supported from 12.0 ES33 onwards. |
| Note | This Call Result is supported from 12.0 ES33 onwards. |

| Note | This Call Result is supported from 12.0 ES33 onwards. |
|---|---|

| Note | For campaigns created using API, CallStatusZone2 is not applicable. |
|---|---|

| Value | Description |
|---|---|
| A | Active:
                                             					 Stored in CallStatusZoneX (1 or 2). A zone is set to active when it has been
                                             					 sent to a dialer for dialing. |
| B | A callback
                                             					 was requested. Stored in CallStatusZone1 and CallStatusZone2 field when a
                                             					 regular callback (non personal callback) has been scheduled. The Callback time
                                             					 itself is stored in both the CallbackDateTimeZone1 and CallbackDateTimeZone2
                                             					 columns since the callback overrides the individual zones. |
| C | Closed:
                                             					 Record has been closed for that particular zone, so the record will not be
                                             					 retried again for that zone (zone1 or zone2). |
| D | Dialed.
                                             					 Record has been dialed for that particular zone. |
| F | F= Fax Machine. Stored in CallStatusZoneX (1 or 2) |
| L | L = Not Allocated. Invalid number used for a Personal Callback. |
| J | Agent
                                             					 rejected (closed out the record) |
| M | The maximum
                                             					 number of attempts has been reached. Stored in both CallStatusZone1 and
                                             					 CallStatusZone2. A record is set to "M" when
                                             					 it has dialed the maximum times as specified in the campaign and will not be
                                             					 retried again. Both zones are set to "M" to
                                             					 indicate no further calling in either zone. |
| P | Pending.
                                             					 Stored in CallStatusZoneX (1 or 2). This is the initial state of a record
                                             					 before any dialing has taken place. The record remains in the pending state for
                                             					 a particular zone until all of the numbers specified for that zone are dialed.
                                             					 A pending contact which has already dialed at least one dialer from its
                                             					 sequence will have at least one CallBackDateTimeXX column filled in with a
                                             					 retry time. |
| R | Retry.
                                             					 Stored in CallStatusZoneX (1 or 2) for the zone where the Retry is scheduled.
                                             					 The retry time itself is stored in the CallbackDateTimeZoneX (1 or 2) as well
                                             					 as in the individual number column CallbackDateTimeXX, where XX is the number
                                             					 to be retried (01 - 10). Call can be retried for a variety of reasons,
                                             					 including receiving a busy or no answer result. This value will be updated once all phones of the record are dialed out. |
| S | A personal
                                             					 callback was requested. Stored in both CallStatusZone1 and CallStatusZone2. A
                                             					 record is set to "S" when
                                             					 it has been scheduled for a personal callback. Both zones are set to "S" to
                                             					 indicate that the record has been moved to the personal callback list. |
| U | Unknown:
                                             					 Stored in CallStatusZone1 and CallStatusZone2. A record is set to Unknown if
                                             					 its status was Active when the Campaign Manager started or the Dialer
                                             					 re-started. The record will stay in the Unknown state until it gets an update.
                                             					 If the Campaign Manager fails to get an update within sixty minutes, it will
                                             					 return the record to Pending. |
| X | For a
                                             					 personal callback, the agent is not available, and the reschedule mode is
                                             					 Abandon. (This value is used for CallStatusZone1 only.) |

| Value | Description |
|---|---|
| 1 | Predictive only |
| 2 | Predictive blended |
| 3 | Preview only |
| 4 | Preview blended |
| 5 | Progressive only |
| 6 | Progressive blended |
| 7 | Direct preview only |
| 8 | Direct preview blended |

| Mode | Definition |
|---|---|
| N | None |
| P | Preview |
| D | Preview Direct |
| R | Predictive |
| G | Progressive |
| A | Callback |

| Call Result | Description | Reporting Column | Counted as Attempt? | Detected Live Voice? | Retry Action |
|---|---|---|---|---|---|
| 2 | Error condition while dialing | None | No | No | Regular outbound calls are not retried and are returned to the closed state. Callback calls are retried as Dialer Abandoned. |
| 3 | Number reported not in service by network | None | Yes | No | None |
| 5 | Operator intercept returned from network when dial attempted | SITTone | Yes | No | None |
| 6 | No dial tone when dialer port went off hook | NoDialTone | Yes | No | No answer |
| 7 | Number reported as invalid by the network | SITTone | Yes | No | None |
| 8 | Customer phone did not answer | NoAnswer | No | No | No answer |
| 9 | Customer phone was busy | Busy | Yes | No | Busy |
| 10 | Customer answered and was connected to agent | Voice | Yes | Yes | None |
| 11 | Fax machine detected | Fax | Yes | No | None |
| 12 | Answering machine detected | AnsweringMachine | Yes | No, but transfer to agent possible | Answering Machine, if needed |
| 13 | Dialer stopped dialing customer due to lack of agents or network stopped dialing before it was complete. | Cancelled | Yes | No | Dialer Abandoned |
| 14 | Customer requested callback | Callback & PersonalCallback | Yes | Yes | None |
| 15 | Answering machine requested callback | Callback & PersonalCallback | Yes | No | None |
| 16 | Call was abandoned by the dialer due to lack of agents | Abandon | Yes | Yes | Dialer Abandoned |
| 17 | Failed to reserve agent for personal callback | None | No | No | Based on the callback mode configuration. For more details, see About Personal Callbacks |
| 18 | Agent has rejected a preview call or personal callback call | AgentRejected | No | No | For Preview calls: No Answer. For Personal Callback calls: None. |
| 19 | Agent has rejected a preview call with the close option | AgentClosed | No | No | None |
| 20 | Customer has been abandoned to an IVR | AbandonToIVR | Yes | Yes | Dialer Abandoned, if needed |
| 21 | Customer dropped call within configured abandoned time | CustomerAbandon | Yes | Yes | Customer Abandoned |
| 22 | Mostly used with TDM switches - network answering machine, such as a network voicemail | NetworkAnsMachine | Yes | No | Answering Machine, if needed |
| 23 | Number successfully contacted but wrong number | WrongNumber | Yes | Yes | None |
| 24 | Number successfully contacted but reached the wrong person | CustomerNotHome | Yes | Yes | Customer not home |
| 25 | The following circumstances are reported where a call record is returned from the dialer without being attempted: The campaign is disabled. The outbound percentage for the campaign skill group is set to zero in an admin script. With personal callback in certain situations where the agent is logged out or not available before the configured CallbackTimeLimit
                                                   is exceeded. | None | No | No | None, but returned to the pending state |
| 26 | The number was on the do not call list | None | No | No | None |
| 27 | Network disconnected while alerting | NoRingBack | No | No | No answer |
| 28 | Low Energy or Dead Air call detected by CPA | NoRingBack | No | No | No answer |
| 29 | SIP message received from dialer is not supported by voice gateway |  |  |  |  |
| 30 | SIP message received from dialer is not authorized by voice gateway |  |  |  |  |
| 31 | Invalid sip message sent by dialer to voice gateway |  |  |  |  |
| 32 | Call cancelled because the dialer lost connection with the Campaign Manager | Cancelled | Yes | No | None |
| 33 | Agent timed-out accepting preview or personal callback call Note This Call Result is supported from 12.0 ES33 onwards. | Note | This Call Result is supported from 12.0 ES33 onwards. | None | No | No | No Answer |
| Note | This Call Result is supported from 12.0 ES33 onwards. |

| Note | This Call Result is supported from 12.0 ES33 onwards. |
|---|---|

| Note | Only based on the PersonalCallbackReattempt registry settings in the CampaignManager, the callback requests with CallResults
                                             values 2,4,6,8,9, and 16 are not counted as attempted. Such callback records are immediately closed with callStatus as C and no redialing occurs |
|---|---|

| StatusCode | PSTNCauseCode | CheckCallState | CallState | DialerCallResult | System Type Values (from Dialer detail: CallResult) |
|---|---|---|---|---|---|
| 400 | 41 | FALSE | CS_NONE | INVALID_NETWORK_MSG | 31 |
| 401 | 57 | FALSE | CS_NONE | NOT_AUTHORIZED | 30 |
| 403 | 57 | FALSE | CS_NONE | NOT_IN_SERVICE | 3 |
| 404 | 0 | FALSE | CS_NONE | NUMBER_NOT_ALLOCATED | 7 |
| 404 | 1 | FALSE | CS_NONE | NUMBER_NOT_ALLOCATED | 7 |
| 404 | 31 | FALSE | CS_NONE | NUMBER_NOT_ALLOCATED | 7 |
| 404 | 20 | FALSE | CS_NONE | NOT_IN_SERVICE | 3 |
| 405 | 63 | FALSE | CS_NONE | NOT_IN_SERVICE | 3 |
| 406 | 88 | FALSE | CS_NONE | NOT_SUPPORTED | 29 |
| 407 | 57 | FALSE | CS_NONE | NOT_AUTHORIZED | 30 |
| 408 | 120 | FALSE | CS_NONE | NO_DIALTONE | 6 |
| 409 | 47 | FALSE | CS_NONE | NOT_SUPPORTED | 29 |
| 410 | 22 | FALSE | CS_NONE | NUMBER_NOT_ALLOCATED | 7 |
| 411 | 47 | FALSE | CS_NONE | NOT_SUPPORTED | 29 |
| 412 | 38 | FALSE | CS_NONE | NOT_AUTHORIZED | 30 |
| 413 | 127 | FALSE | CS_NONE | NOT_SUPPORTED | 29 |
| 415 | 47 | FALSE | CS_NONE | NOT_SUPPORTED | 29 |
| 417 | 47 | FALSE | CS_NONE | NOT_SUPPORTED | 29 |
| 420 | 95 | FALSE | CS_NONE | INVALID_NETWORK_MSG | 31 |
| 421 | 95 | FALSE | CS_NONE | NOT_SUPPORTED | 29 |
| 422 | 100 | FALSE | CS_NONE | NOT_SUPPORTED | 29 |
| 422 | 100 | FALSE | CS_NONE | STOPPED | 13 |
| 422 | 100 | TRUE | CS_CONNECTED | STOPPED | 13 |
| 423 | 47 | FALSE | CS_NONE | NOT_SUPPORTED | 29 |
| 424 | 41 | FALSE | CS_NONE | INVALID_NETWORK_MSG | 31 |
| 428 | 41 | FALSE | CS_NONE | NOT_SUPPORTED | 29 |
| 429 | 41 | FALSE | CS_NONE | NOT_SUPPORTED | 29 |
| 430 | 127 | FALSE | CS_NONE | INVALID_NETWORK_MSG | 31 |
| 433 | 57 | FALSE | CS_NONE | NOT_SUPPORTED | 29 |
| 436 | 41 | FALSE | CS_NONE | NOT_SUPPORTED | 29 |
| 437 | 41 | FALSE | CS_NONE | NOT_SUPPORTED | 29 |
| 438 | 41 | FALSE | CS_NONE | INVALID_NETWORK_MSG | 31 |
| 439 | 88 | FALSE | CS_NONE | NOT_SUPPORTED | 29 |
| 470 | 41 | FALSE | CS_NONE | NOT_AUTHORIZED | 30 |
| 480 | 18 | TRUE | CS_INITIATED | NO_RINGBACK | 4 |
| 480 | 18 | TRUE | CS_ALERTED | NO_ANSWER | 8 |
| 480 | 19 | FALSE | CS_NONE | NO_ANSWER | 8 |
| 480 | 20 | TRUE | CS_INITIATED | NO_RINGBACK | 4 |
| 480 | 20 | TRUE | CS_ALERTED | NO_RINGBACK | 4 |
| 480 | 20 | TRUE | CS_CONNECTED | CUSTOMER_ABANDONED | 21 |
| 480 | 20 | TRUE | CS_NONE | NO_RINGBACK | 4 |
| 481 | 127 | FALSE | CS_NONE | CUSTOMER_ABANDONED | 21 |
| 482 | 25 | FALSE | CS_NONE | STOPPED | 13 |
| 482 | 25 | TRUE | CS_INITIATED | STOPPED | 13 |
| 482 | 25 | TRUE | CS_ALERTED | STOPPED | 13 |
| 482 | 25 | TRUE | CS_CONNECTED | STOPPED | 13 |
| 484 | 28 | FALSE | CS_NONE | NUMBER_NOT_ALLOCATED | 7 |
| 485 | 1 | FALSE | CS_NONE | NUMBER_NOT_ALLOCATED | 7 |
| 486 | 0 | FALSE | CS_NONE | BUSY | 9 |
| 486 | 17 | FALSE | CS_NONE | BUSY | 9 |
| 487 | 127 | TRUE | CS_NONE | NO_DIALTONE | 6 |
| 487 | 127 | TRUE | CS_INITIATED | NO_RINGBACK | 4 |
| 487 | 127 | TRUE | CS_ALERTED | NO_ANSWER | 8 |
| 488 | 47 | FALSE | CS_NONE | NOT_SUPPORTED | 29 |
| 489 | 41 | FALSE | CS_NONE | NOT_SUPPORTED | 29 |
| 491 | 31 | FALSE | CS_NONE | ABANDON | 16 |
| 491 | 31 | TRUE | CS_CONNECTED | ABANDON | 16 |
| 493 | 97 | FALSE | CS_NONE | NOT_SUPPORTED | 29 |
| 494 | 57 | FALSE | CS_NONE | NOT_AUTHORIZED | 30 |
| 500 | 4 | FALSE | CS_NONE | NUMBER_NOT_ALLOCATED | 7 |
| 500 | 5 | FALSE | CS_NONE | NUMBER_NOT_ALLOCATED | 7 |
| 500 | 6 | FALSE | CS_NONE | NO_DIALTONE | 6 |
| 500 | 44 | FALSE | CS_NONE | NO_DIALTONE | 6 |
| 500 | 8 | TRUE | CS_INITIATED | NO_RINGBACK | 4 |
| 500 | 9 | TRUE | CS_INITIATED | NO_RINGBACK | 4 |
| 500 | 39 | TRUE | CS_INITIATED | NO_RINGBACK | 4 |
| 500 | 16 | TRUE | CS_INITIATED | NO_RINGBACK | 4 |
| 500 | 16 | TRUE | CS_ALERTED | NO_ANSWER | 8 |
| 500 | 16 | TRUE | CS_CONNECTED | CUSTOMER_ABANDONED | 21 |
| 500 | 44 | FALSE | CS_NONE | NO_DIALTONE | 6 |
| 500 | 46 | FALSE | CS_NONE | BUSY | 9 |
| 500 | 63 | FALSE | CS_NONE | NUMBER_NOT_ALLOCATED | 7 |
| 500 | 86 | FALSE | CS_NONE | CUSTOMER_ABANDONED | 21 |
| 501 | 79 | FALSE | CS_NONE | NOT_SUPPORTED | 29 |
| 502 | 38 | FALSE | CS_NONE | NO_DIALTONE | 6 |
| 502 | 0 | FALSE | CS_NONE | NO_DIALTONE | 6 |
| 503 | 0 | FALSE | CS_NONE | NO_DIALTONE | 6 |
| 503 | 34 | FALSE | CS_NONE | NO_DIALTONE | 6 |
| 503 | 41 | FALSE | CS_NONE | NO_DIALTONE | 6 |
| 503 | 42 | FALSE | CS_NONE | NO_DIALTONE | 6 |
| 503 | 47 | FALSE | CS_NONE | NO_DIALTONE | 6 |
| 503 | 87 | FALSE | CS_NONE | NO_DIALTONE | 6 |
| 504 | 102 | FALSE | CS_NONE | NOT_SUPPORTED | 29 |
| 505 | 127 | FALSE | CS_NONE | NOT_SUPPORTED | 29 |
| 513 | 100 | FALSE | CS_NONE | NOT_SUPPORTED | 29 |
| 580 | 47 | FALSE | CS_NONE | NO_DIALTONE | 6 |
| 604 | 1 | FALSE | CS_NONE | NUMBER_NOT_ALLOCATED | 7 |
| 600 | 17 | FALSE | CS_NONE | BUSY | 9 |