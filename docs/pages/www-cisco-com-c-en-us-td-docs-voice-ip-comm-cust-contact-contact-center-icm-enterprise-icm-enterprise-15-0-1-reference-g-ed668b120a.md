---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-icm-enterprise-icm-enterprise-15-0-1-reference-g-ed668b120a
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/icm_enterprise/icm_enterprise_15_0_1/reference/guide/ucce_b_cti-servermessage-reference-guide-for-1501/ucce-m-constants-and-status-codes-1501.html
retrieved_at: 2026-08-16T19:45:33.358168+00:00
---

CTI Server Message Reference Guide (Protocol Version 25) for Cisco Unified Contact Center Enterprise, Release 15.0(1)

# CTI Server Message Reference Guide (Protocol Version 25) for Cisco Unified Contact Center Enterprise, Release 15.0(1)

Updated: March 1, 2025

Chapter: Constants and Status Codes

## Chapter: Constants and Status Codes

# Constants and Status Codes

## In this chapter

This section lists the possible values for various status codes
                           and fields that can appear in CTI Server messages. These values are defined
                           in the CTILink.h file, located in the \icm\include directory.

## Failure Indication
                        	 Message Status Codes

This
                              		  table shows the status codes that may be included in the FAILURE_CONF and
                              		  FAILURE_EVENT messages.

Status Codes

Status Code

Description

Value

E_CTI_NO_ERROR

No error occurred.

0

E_CTI_INVALID_ VERSION

The CTI Server does not support the protocol version number requested by the CTI client.

1

E_CTI_INVALID_MESSAGE_LENGTH

A message with an invalid message length field was received.

2

E_CTI_INVALID_ FIELD_TAG

A message with an invalid floating field tag was received.

3

E_CTI_SESSION_ NOT_OPEN

No session is currently open on the connection.

4

E_CTI_SESSION_ ALREADY_ OPEN

A session is already open on the connection.

5

E_CTI_REQUIRED_ DATA_ MISSING

The request did not include one or more floating items that are required.

6

E_CTI_INVALID_ PERIPHERAL_ID

A message with an invalid PeripheralID value was received.

7

E_CTI_INVALID_ AGENT_ DATA

The provided agent data item(s) are invalid.

8

E_CTI_AGENT_NOT_ LOGGED_ON

The indicated agent is not currently logged on.

9

E_CTI_DEVICE_IN_ USE

The indicated agent teleset is already associated with a different CTI client.

10

E_CTI_NEW_ SESSION_ OPENED

This session is being terminated due to a new session open request from the client.

11

E_CTI_FUNCTION_ NOT_ AVAILABLE

A request message was received for a function or service that was not granted to the client.

12

E_CTI_INVALID_ CALLID

A request message was received with an invalid CallID value.

13

E_CTI_PROTECTED_ VARIABLE

The CTI client may not update the requested variable.

14

E_CTI_CTI_SERVER_ OFFLINE

The CTI Server is not able to function normally. The CTI client should close the session upon receipt of this error.

If a client using a CTI protocol version less than 24 tries to connect to a standby CTI Server, the client does not support
                                          active-standby functionality and will instead connect to the active side.

15

E_CTI_TIMEOUT

The CTI Server failed to respond to a request message within the time-out period, or no messages have been received from the
                                          CTI client within the IdleTimeout period.

16

E_CTI_UNSPECIFIED_FAILURE

An unspecified error occurred.

17

E_CTI_INVALID_ TIMEOUT

The IdleTimeout field contains a value that is less than 20 seconds (4 times the minimum heartbeat interval of 5 seconds).

18

E_CTI_INVALID_ SERVICE_MASK

The ServicesRequested field has unused bits set. All unused bit positions must be zero.

19

E_CTI_INVALID_ CALL_MSG_MASK

The CallMsgMask field has unused bits set. All unused bit positions must be zero.

20

E_CTI_INVALID_ AGENT_ STATE_ MASK

The AgentStateMask field has unused bits set. All unused bit positions must be zero.

21

E_CTI_INVALID_ RESERVED_ FIELD

A Reserved field has a non-zero value.

22

E_CTI_INVALID_ FIELD_ LENGTH

A floating field exceeds the allowable length for that field type.

23

E_CTI_INVALID_ DIGITS

A STRING field contains characters that are not digits (“0” through “9”).

24

E_CTI_BAD_ MESSAGE_ FORMAT

The message is improperly constructed. This may be caused by omitted or incorrectly sized fixed message fields.

25

E_CTI_INVALID_ TAG_FOR_MSG_ TYPE

A floating field tag is present that specifies a field that does not belong in this message type.

26

E_CTI_INVALID_ DEVICE_ID_ TYPE

A DeviceIDType field contains a value that is not in DeviceIDType Values .

27

E_CTI_INVALID_ LCL_CONN_ STATE

A LocalConnectionState field contains a value that is not in LocalConnectionState Values .

28

E_CTI_INVALID_ EVENT_ CAUSE

An EventCause field contains a value that is not in EventCause Values .

29

E_CTI_INVALID_ NUM_ PARTIES

The NumParties field contains a value that exceeds the maximum (16).

30

E_CTI_INVALID_ SYS_ EVENT_ID

The SystemEventID field contains a value that is not in SystemEventID Values .

31

E_CTI_ INCONSISTENT_ AGENT_DATA

The provided agent extension, agent id, and/or agent instrument values are inconsistent with each other.

32

E_CTI_INVALID_ CONNECTION_ID_ TYPE

A ConnectionDeviceIDType field contains a value that is not in ConnectionDeviceIDType Values .

33

E_CTI_INVALID_ CALL_TYPE

The CallType field contains a value that is not in CallType Values .

34

E_CTI_NOT_CALL_ PARTY

A CallDataUpdate or Release Call request specified a call that the client is not a party to.

35

E_CTI_INVALID_ PASSWORD

The ClientID and Client Password provided in an OPEN_REQ message is incorrect.

36

E_CTI_CLIENT_ DISCONNECTED

The client TCP/IP connection was disconnected without a CLOSE_REQ.

37

E_CTI_INVALID_ OBJECT_ STATE

An invalid object state value was provided.

38

E_CTI_INVALID_ NUM_ SKILL_GROUPS

An invalid NumSkillGroups value was provided.

39

E_CTI_INVALID_ NUM_LINES

An invalid NumLines value was provided.

40

E_CTI_INVALID_ LINE_TYPE

An invalid LineType value was provided.

41

E_CTI_INVALID_ ALLOCATION_STATE

An invalid AllocationState value was provided.

42

E_CTI_INVALID_ ANSWERING_ MACHINE

An invalid AnsweringMachine value was provided.

43

E_CTI_INVALID_ CALL_MANNER_ TYPE

An invalid CallMannerType value was provided.

44

E_CTI_INVALID_ CALL_PLACEMENT_ TYPE

An invalid CallPlacementType value was provided.

45

E_CTI_INVALID_ CONSULT_ TYPE

An invalid ConsultType value was provided.

46

E_CTI_INVALID_ FACILITY_ TYPE

An invalid FacilityType value was provided.

47

E_CTI_INVALID_ MSG_TYPE_ FOR_ VERSION

The provided MessageType is invalid for the opened protocol version.

48

E_CTI_INVALID_ TAG_FOR_ VERSION

A floating field tag value is invalid for the opened protocol version.

49

E_CTI_INVALID_ AGENT_WORK_ MODE

An invalid AgentWorkMode value was provided.

50

E_CTI_INVALID_ CALL_OPTION

An invalid call option value was provided.

51

E_CTI_INVALID_ DESTINATION_ COUNTRY

An invalid destination country value was provided.

52

E_CTI_INVALID_ ANSWER_DETECT_ MODE

An invalid answer detect mode value was provided.

53

E_CTI_MUTUALLY_ EXCLUS_DEVICEID_ TYPES

A peripheral monitor request may not specify both a call and a device.

54

E_CTI_INVALID_ MONITORID

An invalid monitorID value was provided.

55

E_CTI_SESSION_ MONITOR_ ALREADY_EXISTS

A requested session monitor was already created.

56

E_CTI_SESSION_ MONITOR_IS_ CLIENTS

A client may not monitor its own session.

57

E_CTI_INVALID_ CALL_CONTROL_ MASK

An invalid call control mask value was provided.

58

E_CTI_INVALID_ FEATURE_MASK

An invalid feature mask value was provided.

59

E_CTI_INVALID_ TRANSFER_ CONFERENCE_ SETUP_MASK

An invalid transfer conference setup mask value was provided.

60

E_CTI_INVALID_ ARRAY_INDEX

An invalid named array index value was provided.

61

E_CTI_INVALID_ CHARACTER

An invalid character value was provided.

62

E_CTI_CLIENT_NOT_FOUND

There is no open session with a matching ClientID.

63

E_CTI_SUPERVISOR_NOT_FOUND

The agent’s supervisor is unknown or does not have an open CTI session.

64

E_CTI_TEAM_NOT_ FOUND

The agent is not a member of an agent team.

65

E_CTI_NO_CALL_ ACTIVE

The specified agent does not have an active call.

66

E_CTI_NAMED_ VARIABLE_NOT_ CONFIGURED

The specified named variable is not configured in the Unified CCE.

67

E_CTI_NAMED_ ARRAY_NOT_ CONFIGURED

The specified named array is not configured in the Unified CCE.

68

E_CTI_INVALID_ CALL_VARIABLE_ MASK

The specified call variable mask in not valid.

69

E_CTI_ELEMENT_ NOT_FOUND

An internal error occurred manipulating a named variable or named array element.

70

E_CTI_INVALID_ DISTRIBUTION_TYPE

The specified distribution type is invalid.

71

E_CTI_INVALID_ SKILL_GROUP

The specified skill group is invalid.

72

E_CTI_TOO_MUCH_ DATA

The total combined size of named variables and named arrays may not exceed the limit of 2000 bytes.

73

E_CTI_VALUE_TOO_LONG

The value of the specified named variable or named array element exceeds the maximum permissible length.

74

E_CTI_SCALAR_ FUNCTION_ON_ ARRAY

A NamedArray was specified with a NamedVariable tag.

75

E_CTI_ARRAY_ FUNCTION_ON_ SCALAR

A NamedVariable was specified with a NamedArray tag.

76

E_CTI_INVALID_ NUM_NAMED_ VARIABLES

The value in the NumNamedVariables field is different than the number of NamedVariable floating fields in the message.

77

E_CTI_INVALID_ NUM_NAMED_ ARRAYS

The value in the NumNamedArrays field is different than the number of NamedArray floating fields in the message.

78

E_CTI_INVALID_RTP_DIRECTION

The RTP direction value is invalid.

79

E_CTI_INVALID_RTP_TYPE

The RTP type value is invalid.

80

E_CTI_CALLED_ PARTY_DISPOSITION

The called party disposition is invalid.

81

E_CTI_INVALID_ SUPERVISORY_ ACTION

The supervisory action is invalid.

82

E_CTI_AGENT_ TEAM_MONITOR_ ALREADY_EXISTS

The agent team monitor already exists.

83

E_CTI_INVALID_ SERVICE

The ServiceNumber or ServiceID value is invalid.

84

E_CTI_SERVICE_ CONFLICT

The ServiceNumber and ServiceID values given represent different services.

85

E_CTI_SKILL_ GROUP_CONFLICT

The SkillGroupNumber/SkillGroupPriority and SkillGroupID values given represent different skill groups.

86

E_CTI_INVALID_ DEVICE

The specified device is invalid.

87

E_CTI_INVALID_MR_DOMAIN

Media Routing Domain is invalid.

88

E_CTI_MONITOR_ ALREADY_EXISTS

Monitor already exists.

89

E_CTI_MONITOR_ TERMINATED

Monitor has terminated.

90

E_CTI_INVALID_ TASK_MSG_MASK

The task msg mask is invalid.

91

E_CTI_SERVER_NOT_MASTER

The server is a standby server.

92

E_CTI_INVALID_CSD

The CSD Specified is invalid (Unified CCX Only).

93

E_CTI_JTAPI_CCM_ PROBLEM

Indicates a JTAPI or Unified CM problem.

94

E_INVALID_CONFIG_ MSG_MASK

Indicates a bad config mask in OPEN_REQ.

95

E_CTI_AUTO_ CONFIG_RESET

Indicates a configuration change (Unified CCX only).

96

E_CTI_INVALID_ MONITOR_STATUS

Indicates an invalid monitor.

97

E_CTI_INVALID_ REQUEST_TYPE

Indicates an invalid request ID type.

98

E_CTI_INVALID_CLIENT_ FOR_STANDBY

Standby CTIServer returns this error code when:

The clients without ServiceMask CTI_SERVICE_ACTIVE_STANDBY (0x02000000) connects.

107

E_CTI_INVALID_UNIQUE_ INSTANCE_ID

This status code is returned as a failure response for the OPEN_REQ message when the UniqueInstanceID element is present in
                                          the message but its value is empty (0 length).

108

E_CTI_DUPLICATE_UNIQUE_ INSTANCE_ID

This status code is returned as a failure response for the OPEN_REQ message when there is an existing Client Instance found
                                          with same UniqueInstanceID in the OPEN_REQ message.

109

E_CTI_SERVER_IN_ MAINTENANCE_MODE

This status code is returned as a failure response for the OPEN_REQ message a client is trying to open a session with CTI
                                          Server when Maintenance Mode is in progress.

The code is used to close the client session when the active CTI Server stops for Maintenance Mode.

110

## SystemEventID
                        	 Values

This
                              		  table shows the SystemEventID values that may be included in the SYSTEM_EVENT
                              		  messages.

SystemEventID

Description

Value

SYS_CENTRAL_ CONTROLLER_ONLINE

The PG has
                                          					 resumed communication with the Unified CCE Central Controller.

1

SYS_CENTRAL_ CONTROLLER_OFFLINE

The PG is
                                          					 unable to communicate with the Unified CCE Central Controller.

2

SYS_PERIPHERAL_ ONLINE

A
                                          					 peripheral monitored by the PG has gone online. SystemEventArg1 contains the
                                          					 PeripheralID of the peripheral.

3

SYS_PERIPHERAL_ OFFLINE

A
                                          					 peripheral monitored by the PG has gone offline. SystemEventArg1 contains the
                                          					 PeripheralID of the peripheral.

4

SYS_TEXT_FYI

Broadcast
                                          					 of informational “text” floating field.

5

SYS_PERIPHERAL_ GATEWAY_OFFLINE

The CTI
                                          					 Server is unable to communicate with the Unified CCE Peripheral Gateway.

6

SYS_CTI_SERVER_ OFFLINE

The local
                                          					 software component is unable to communicate with the CTI Server.

7

SYS_CTI_SERVER_ ONLINE

The local
                                          					 software component has resumed communication with the CTI Server.

8

SYS_HALF_HOUR_ CHANGE

The
                                          					 Unified CCE Central Controller time has changed to a new half hour.

9

SYS_INSTRUMENT_ OUT_OF_SERVICE

An
                                          					 Enterprise Agent device target has been removed from service. SystemEventArg1
                                          					 contains the PeripheralID of the peripheral, and SystemEventText contains the
                                          					 AgentInstrument that was removed from service.

10

SYS_INSTRUMENT_ BACK_IN_SERVICE

An
                                          					 Enterprise Agent device target has been returned to service. SystemEventArg1
                                          					 contains the PeripheralID of the peripheral, and SystemEventText contains the
                                          					 AgentInstrument that was returned to service.

11

## Special
                        	 Values

This table shows
                              		  the values used to define sizes and limits, indicate special IDs, and
                              		  unspecified data elements.

Constant

Description

Value

MAX_NUM_CTI_ CLIENTS

The
                                          					 maximum number of CTI clients that can be in a message list.

16

MAX_NUM_
                                          					 PARTIES

The
                                          					 maximum number of conference call parties that can be in a message list.

16

MAX_NUM_
                                          					 DEVICES

The
                                          					 maximum number of call devices that can be in a message list.

16

MAX_NUM_
                                          					 CALLS

The
                                          					 maximum number of calls that can be in a message list.

16

MAX_NUM_
                                          					 SKILL_GROUPS

The
                                          					 maximum number of skill group fields that can be in a message list.

20

MAX_NUM_LINES

The
                                          					 maximum number of teleset line fields that can be in a message list.

10

NULL_
                                          					 CALL_ID

No call ID
                                          					 is supplied.

0xFFFFFFFF

NULL_
                                          					 PERIPHERAL_ID

No
                                          					 peripheral ID is supplied.

0xFFFFFFFF

NULL_SERVICE

No service
                                          					 is supplied.

0xFFFFFFFF

NULL_SKILL_ GROUP

No skill
                                          					 group is supplied.

0xFFFFFFFF

NULL_CALLTYPE

Indicates
                                          					 that no CallType is supplied.

0xFFFF

## Tag Values

This
                              		  table shows the values used in the tag subfield of floating fields.

Floating
                                          					 Field Tag

Using
                                          					 Messages

Value

CLIENT_ID_TAG

OPEN_REQ

1

CLIENT_PASSWORD_ TAG

OPEN_REQ

2

CLIENT_SIGNATURE_ TAG

OPEN_REQ,
                                          					 AGENT_STATE_EVENT

3

AGENT_EXTENSION_ TAG

OPEN_REQ,
                                          					 OPEN_CONF, AGENT_STATE_EVENT

4

AGENT_ID_TAG

OPEN_REQ,
                                          					 OPEN_CONF, AGENT_STATE_EVENT, SET_AGENT_STATE_EVENT

5

AGENT_
                                          					 INSTRUMENT_ TAG

OPEN_REQ,
                                          					 OPEN_CONF, AGENT_STATE_EVENT, QUERY_AGENT_STATE_REQ, SET_AGENT_STATE_REQ,
                                          					 MAKE_CALL_REQ

6

TEXT_TAG

SYSTEM_EVENT, CLIENT_EVENT_REPORT_REQ, AGENT_TASKS_END_EVENT

7

ANI_TAG

BEGIN_CALL_EVENT, CALL_ DATA_UPDATE_EVENT, CALL_
                                          					 TRANSLATION_ROUTE_EVENT, SNAPSHOT_CALL_ CONF

8

UUI_TAG

BEGIN_CALL_EVENT, CALL_DATA_UPDATE_EVENT,
                                          					 CALL_TRANSLATION_ROUTE_ EVENT, CONSULTATION_ CALL_REQ, MAKE_CALL_REQ,
                                          					 TRANSFER_CALL_REQ, SNAPSHOT_CALL_CONF

9

DNIS_TAG

BEGIN_CALL_EVENT, CALL_ DATA_UPDATE_EVENT, CALL_
                                          					 TRANSLATION_ROUTE_ EVENT, SNAPSHOT_CALL_ CONF

10

DIALED_NUMBER_ TAG

BEGIN_CALL_EVENT, CALL_DATA_UPDATE_EVENT,
                                          					 CALL_TRANSLATION_ROUTE_ EVENT, CONSULTATION_ CALL_ REQ, MAKE_CALL_REQ,
                                          					 TRANSFER_CALL_REQ, SNAPSHOT_CALL_CONF

11

CED_TAG

BEGIN_CALL_EVENT, CALL_ DATA_UPDATE_EVENT, CALL_
                                          					 TRANSLATION_ROUTE_ EVENT, SNAPSHOT_CALL_ CONF

12

CALL_VAR_1_TAG through CALL_VAR_10_TAG

BEGIN_CALL_EVENT, CALL_DATA_UPDATE_EVENT, CALL_TRANSLATION_ROUTE_ EVENT, CONSULTATION_ CALL_REQ, MAKE_CALL_REQ, TRANSFER_CALL_REQ,
                                          SNAPSHOT_CALL_CONF, SNAPSHOT_TASK_RESP , SNAPSHOT_TASK_EVENT

13-22

CTI_CLIENT_ SIGNATURE_TAG

BEGIN_CALL_EVENT, CALL_DATA_UPDATE_EVENT, SNAPSHOT_CALL_CONF

23

CTI_CLIENT_ TIMESTAMP_TAG

BEGIN_CALL_EVENT, CALL_DATA_UPDATE_EVENT, SNAPSHOT_CALL_CONF

24

CONNECTION_ DEVID_ TAG

Any CALL
                                          					 EVENT message, most CLIENT CONTROL messages.

25

ALERTING_DEVID_ TAG

CALL_DELIVERED_EVENT

26

CALLING_DEVID_TAG

CALL_DELIVERED_EVENT, CALL_ESTABLISHED_EVENT,
                                          					 CALL_ORIGINATED_EVENT, CALL_SERVICE_INITIATED_EVENT, CALL_QUEUED_EVENT,
                                          					 SET_DEVICE_ATTRIBUTES_REQ

27

CALLED_DEVID_TAG

CALL_DELIVERED_EVENT, CALL_ESTABLISHED_EVENT,
                                          					 CALL_ORIGINATED_EVENT, CALL_QUEUED_EVENT,

28

LAST_REDIRECT_ DEVID_TAG

CALL_DELIVERED_EVENT, CALL_ESTABLISHED_EVENT, CALL_QUEUED_EVENT

29

ANSWERING_DEVID_ TAG

CALL_ESTABLISHED_EVENT

30

HOLDING_DEVID_ TAG

CALL_HELD_EVENT

31

RETRIEVING_DEVID_ TAG

CALL_RETRIEVED_EVENT

32

RELEASING_DEVID_ TAG

CALL_CONNECTION_ CLEARED_EVENT

33

FAILING_DEVID_TAG

CALL_FAILED_EVENT

34

PRIMARY_DEVID_ TAG

CALL_CONFERENCED_EVENT, CALL_TRANSFERRED_EVENT

35

SECONDARY_DEVID_ TAG

CALL_CONFERENCED_EVENT, CALL_TRANSFERRED_EVENT

36

CONTROLLER_ DEVID_ TAG

CALL_CONFERENCED_EVENT

37

ADDED_PARTY_ DEVID_TAG

CALL_CONFERENCED_EVENT

38

PARTY_CALLID_TAG

CALL_CONFERENCED_EVENT, CALL_TRANSFERRED_EVENT,
                                          					 CONFERENCE_CALL_CONF, TRANSFER_CALL_CONF

39

PARTY_DEVID_TYPE_ TAG

CALL_CONFERENCED_EVENT, CALL_TRANSFERRED_EVENT,
                                          					 CONFERENCE_CALL_CONF, TRANSFER_CALL_CONF

40

PARTY_DEVID_TAG

CALL_CONFERENCED_EVENT, CALL_TRANSFERRED_EVENT,
                                          					 CONFERENCE_CALL_CONF, TRANSFER_CALL_CONF

41

TRANSFERRING_ DEVID_TAG

CALL_TRANSFERRED_EVENT

42

TRANSFERRED_ DEVID_TAG

CALL_TRANSFERRED_EVENT

43

DIVERTING_DEVID_ TAG

CALL_DIVERTED_EVENT

44

QUEUE_DEVID_TAG

CALL_QUEUED_EVENT

45

CALL_WRAPUP_ DATA_ TAG

BEGIN_CALL_EVENT, CALL_DATA_UPDATE_EVENT, SET_CALL_DATA_REQ,
                                          					 CONSULTATION_CALL_REQ, MAKE_CALL_REQ, TRANSFER_CALL_REQ, SNAPSHOT_CALL_CONF

46

NEW_CONNECTION_ DEVID_TAG

CALL_DATA_UPDATE_EVENT, CONFERENCE_CALL_CONF,
                                          					 CONSULTATION_CALL_CONF, MAKE_CALL_CONF, TRANSFER_CALL_CONF

47

TRUNK_USED_ DEVID_ TAG

CALL_REACHED_NETWORK_ EVENT

48

AGENT_PASSWORD_ TAG

SET_AGENT_STATE_REQ

49

ACTIVE_CONN_ DEVID_ TAG

ALTERNATE_CALL_REQ, CONFERENCE_CALL_REQ, CONSULTATION_CALL_REQ,
                                          					 RECONNECT_CALL_REQ, TRANSFER_CALL_REQ

50

FACILITY_CODE_TAG

CONSULTATION_CALL_REQ, MAKE_CALL_REQ, TRANSFER_CALL_REQ

51

OTHER_CONN_ DEVID_ TAG

ALTERNATE_CALL_REQ

52

HELD_CONN_DEVID_ TAG

CONFERENCE_CALL_REQ, RECONNECT_CALL_REQ, RETRIEVE_CALL_REQ,
                                          					 TRANSFER_CALL_REQ

53

(reserved)

54-55

CALL_CONN_ CALLID_ TAG

SNAPSHOT_CALL_CONF, SNAPSHOT_DEVICE_CONF

56

CALL_CONN_DEVID_ TYPE_TAG

SNAPSHOT_CALL_CONF, SNAPSHOT_DEVICE_CONF

57

CALL_CONN_DEVID_ TAG

SNAPSHOT_CALL_CONF, SNAPSHOT_DEVICE_CONF

58

CALL_DEVID_TYPE_ TAG

SNAPSHOT_CALL_CONF

59

CALL_DEVID_TAG

SNAPSHOT_CALL_CONF

60

CALL_DEV_CONN_ STATE_TAG

SNAPSHOT_CALL_CONF

61

SKILL_GROUP_ NUMBER_TAG

CALL_QUEUED_EVENT, CALL_DEQUEUED_EVENT, QUERY_AGENT_STATE_CONF

62

SKILL_GROUP_ID_ TAG

CALL_QUEUED_EVENT, CALL_DEQUEUED_EVENT, QUERY_AGENT_STATE_CONF

63

SKILL_GROUP_ PRIORITY_TAG

CALL_QUEUED_EVENT, CALL_DEQUEUED_EVENT, QUERY_AGENT_STATE_CONF

64

SKILL_GROUP_ STATE_ TAG

QUERY_AGENT_STATE_CONF

65

OBJECT_NAME_TAG

CLIENT_EVENT_REPORT

66

DTMF_STRING_TAG

SEND_DTMF_SIGNAL_REQ

67

POSITION_ID_TAG

SET_AGENT_STATE_REQ

68

SUPERVISOR_ID_TAG

SET_AGENT_STATE_REQ

69

LINE_HANDLE_TAG

QUERY_DEVICE_INFO_CONF

70

LINE_TYPE_TAG

QUERY_DEVICE_INFO_CONF

71

ROUTER_CALL_KEY_ DAY_TAG

BEGIN_CALL_EVENT, CALL_ DATA_UPDATE_EVENT, CALL_
                                          					 TRANSLATION_ROUTE_EVENT, SNAPSHOT_CALL_ CONF

72

ROUTER_CALL_KEY_ CALLID_TAG

BEGIN_CALL_EVENT, CALL_ DATA_UPDATE_EVENT, CALL_
                                          					 TRANSLATION_ROUTE_EVENT, SNAPSHOT_CALL_ CONF

73

ROUTER_CALL_KEY_SEQUENCE_NUM_TAG

AGENT_LEGACY_PRE_CALL_EVENT, BEGIN_CALL_EVENT,
                                          					 CALL_DATA_UPDATE_EVENT, CALL_TRANSLATION_ROUTE_EVENT, AGENT_PRE_CALL_EVENT,
                                          					 AGENT_PRE_CALL_ABORT_EVENT

110

(reserved)

74

CALL_STATE_TAG

SNAPSHOT_DEVICE_CONF

75

MONITORED_DEVID_TAG

MONITOR_START_REQ

76

AUTHORIZATION_ CODE_TAG

CONFERENCE_CALL_REQ, CONSULTATION_CALL_REQ, MAKE_CALL_REQ,
                                          					 MAKE_PREDICTIVE_CALL_REQ, TRANSFER_CALL_REQ

77

ACCOUNT_CODE_TAG

CONFERENCE_CALL_REQ, CONSULTATION_CALL_REQ, MAKE_CALL_REQ,
                                          					 MAKE_PREDICTIVE_CALL_REQ, TRANSFER_CALL_REQ

78

ORIGINATING_DEVID_TAG

MAKE_PREDICTIVE_CALL_REQ

79

ORIGINATING_LINE _ID_TAG

MAKE_PREDICTIVE_CALL_REQ

80

CLIENT_ADDRESS_ TAG

CLIENT_SESSION_OPENED_EVENT, CLIENT_SESSION_CLOSED_EVENT

81

NAMED_VARIABLE_ TAG

BEGIN_CALL_EVENT, CALL_DATA_UPDATE_EVENT, AGENT_PRE_CALL_EVENT, CALL_TRANSLATION_ROUTE_ EVENT, SET_CALL_DATA_REQ, CONFERENCE_CALL_REQ,
                                          CONSULTATION_CALL_REQ, MAKE_CALL_REQ, MAKE_PREDICTIVE_CALL_REQ, TRANSFER_CALL_REQ, SNAPSHOT_CALL_CONF, REGISTER_VARIABLES_REQ,
                                          SNAPSHOT_TASK_RESP, SNAPSHOT_TASK_EVENT

82

NAMED_ARRAY_TAG

BEGIN_CALL_EVENT, CALL_DATA_UPDATE_EVENT, AGENT_PRE_CALL_EVENT, CALL_TRANSLATION_ROUTE_ EVENT, SET_CALL_DATA_REQ, CONFERENCE_CALL_REQ,
                                          CONSULTATION_CALL_REQ, MAKE_CALL_REQ, MAKE_PREDICTIVE_CALL_REQ, TRANSFER_CALL_REQ, SNAPSHOT_CALL_CONF, REGISTER_VARIABLES_REQ,
                                          SNAPSHOT_TASK_RESP, SNAPSHOT_TASK_EVENT

83

CALL_CONTROL_ TABLE_TAG

MAKE_CALL_REQ, MAKE_PREDICTIVE_CALL_REQ,

84

SUPERVISOR_ INSTRUMENT_TAG

SUPERVISE_CALL_REQ

85

ATC_AGENT_ID_TAG

AGENT_TEAM_CONFIG_EVENT

86

AGENT_FLAGS_TAG

AGENT_TEAM_CONFIG_EVENT

87

ATC_AGENT_STATE_ TAG

AGENT_TEAM_CONFIG_EVENT

88

ATC_STATE_ DURATION_TAG

AGENT_TEAM_CONFIG_EVENT

89

AGENT_
                                          					 CONNECTION_DEVID_ TAG

SUPERVISE_CALL_REQ

90

SUPERVISOR_ CONNECTION_ DEVID_TAG

SUPERVISE_CALL_REQ,

91

LIST_TEAM_ID_TAG

LIST_AGENT_TEAM_CONF

92

DEFAULT_DEVICE_ PORT_ADDRESS_TAG

AGENT_DESK_SETTINGS_CONF

93

SERVICE_NAME_TAG

REGISTER_SERVICE_REQ

94

CUSTOMER_PHONE_ NUMBER_TAG

SET_CALL_DATA_REQ, CALL_DATA_UPDATE_EVENT

95

CUSTOMER_ ACCOUNT_NUMBER_TAG

SET_CALL_DATA_REQ, CALL_DATA_UPDATE_EVENT

96

APP_PATH_ID_TAG

OPEN_REQ

97

SCRIPT_SELECTOR_TAG

SNAPSHOT_TASK_RESP, SNAPSHOT_TASK_EVENT

99

APPLICATION_STRING1_TAG

SNAPSHOT_TASK_RESP, SNAPSHOT_TASK_EVENT

100

APPLICATION_STRING2_TAG

SNAPSHOT_TASK_RESP, SNAPSHOT_TASK_EVENT

101

ROUTER_CALL_KEY_SEQUENCE_NUM_TAG

AGENT_LEGACY_PRE_CALL_EVENT, BEGIN_CALL_EVENT,
                                          					 CALL_DATA_UPDATE_EVENT, CALL_TRANSLATION_ROUTE_EVENT, AGENT_PRE_CALL_EVENT,
                                          					 AGENT_PRE_CALL_ABORT_EVENT

110

TRUNK_NUMBER_ TAG

CALL_DELIVERED_EVENT, CALL_ESTABLISHED_EVENT,
                                          					 CALL_REACHED_NETWORK_ EVENT

121

TRUNK_GROUP_ NUMBER_TAG

CALL_DELIVERED_EVENT, CALL_ESTABLISHED_EVENT,
                                          					 CALL_REACHED_NETWORK_EVENT

122

EXT_AGENT_STATE_ TAG

AGENT_STATE_EVENT

123

DEQUEUE_TYPE_TAG

CALL_DEQUEUED_EVENT

124

SENDING_ADDRESS_ TAG

RTP_STARTED_EVENT, RTP_STOPPED_EVENT

125

SENDING_PORT_TAG

RTP_STARTED_EVENT RTP_STOPPED_EVENT

126

Unused

127-128

MAX_QUEUED_TAG

CONFIG_SERVICE_EVENT, CONFIG_DEVICE_EVENT

129

QUEUE_ID_TAG

QUEUE_UPDATED_EVENT

130

CUSTOMER_ID_TAG

CONFIG_REQUEST_EVENT

131

SERVICE_SKILL_ TARGET_ID_TAG

CONFIG_SERVICE_EVENT

132

PERIPHERAL_NAME_ TAG

CONFIG_SERVICE_EVENT, CONFIG_SKILL_GROUP_EVENT,
                                          					 CONFIG_AGENT_EVENT, CONFIG_DIALED_NUMBER_ EVENT

133

DESCRIPTION_TAG

CONFIG_SERVICE_EVENT, CONFIG_SKILL_GROUP_EVENT,
                                          					 CONFIG_AGENT_EVENT, CONFIG_DIALED_NUMBER_EVENT

CONFIG_MRD_EVENT

134

SERVICE_MEMBER_ ID_TAG

CONFIG_SKILL_GROUP_EVENT

135

SERVICE_MEMBER_ PRIORITY_TAG

CONFIG_SKILL_GROUP_EVENT

136

FIRST_NAME_TAG

CONFIG_AGENT_EVENT

137

LAST_NAME_TAG

CONFIG_AGENT_EVENT

138

SKILL_GROUP_TAG

CONFIG_AGENT_EVENT

139

AGENT_SKILL_ TARGET_ID_TAG

CONFIG_AGENT_EVENT

141

SERVICE_TAG

CONFIG_DIALED_NUMBER_ EVENT

142

Reserved

143-149

DURATION_TAG

AGENT_STATE_EVENT

150

Reserved

151-172

EXTENSION_TAG

CONFIG_SKILL_GROUP_EVENT, CONFIG_SERVICE_EVENT,
                                          					 CONFIG_AGENT_EVENT,CONFIG_DEVICE_EVENT

173

SERVICE_LEVEL_ THRESHOLD_TAG

CONFIG_SERVICE_EVENT

174

SERVICE_LEVEL_ TYPE_TAG

CONFIG_SERVICE_EVENT

175

CONFIG_PARAM_TAG

CONFIG_SKILL_GROUP_EVENT, CONFIG_SERVICE_EVENT

176

SERVICE_CONFIG_ KEY_TAG

CONFIG_KEY_EVENT, CONFIG_BEGIN_EVENT

177

SKILL_GROUP_ CONFIG_KEY_TAG

CONFIG_KEY_EVENT, CONFIG_BEGIN_EVENT

178

AGENT_CONFIG_ KEY_TAG

CONFIG_KEY_EVENT, CONFIG_BEGIN_EVENT

179

DEVICE_CONFIG_ KEY_TAG

CONFIG_KEY_EVENT, CONFIG_BEGIN_EVENT

180

Unused

181-182

RECORD_TYPE_TAG

CONFIG_AGENT_EVENT, CONFIG_DEVICE_EVENT, CONFIG_SERVICE_EVENT,
                                          					 CONFIG_SKILL_GROUP_EVENT

183

PERIPHERAL_ NUMBER_TAG

CONFIG_AGENT_EVENT, CONFIG_DEVICE_EVENT, CONFIG_SERVICE_EVENT,
                                          					 CONFIG_SKILL_GROUP_EVENT

184

AGENT_SKILL_ TARGET_ID_TAG

CONFIG_AGENT_EVENT

185

NUM_SERVICE_ MEMBERS_TAG

CONFIG_SERVICE_EVENT

186

SERVICE_MEMBER_ TAG

CONFIG_SERVICE_EVENT

187

SERVICE_PRIORITY_ TAG

CONFIG_SERVICE_EVENT

188

AGENT_TYPE_TAG

CONFIG_AGENT_EVENT

189

LOGIN_ID_TAG

CONFIG_AGENT_EVENT

190

NUM_SKILLS_TAG

CONFIG_AGENT_EVENT

191

SKILL_GROUP_SKILL_TARGET_ID_TAG

CONFIG_SKILL_GROUP_EVENT

192

SERVICE_ID_TAG

CONFIG_DEVICE_EVENT

193

AGENT_ID_LONG_ TAG

OPEN_REQ, OPEN_REQ, OPEN_REQ_CONF, AGENT_STATE_EVENT,
                                          					 RTP_STARTED_EVENT, RTP_STOPPED_EVENT, SUPERVISE_CALL_REQ, EMERGENCY_CALL_EVENT,
                                          					 USER_MESSAGE_REQ, SET_AGENT_STATE_REQ, SET_AGENT_STATE_CONF,
                                          					 QUERY_AGENT_STATE_REQ, QUERY_AGENT_STATE_CONF, AGENT_UPDATED_EVENT

194

DEVICE_TYPE_TAG

CONFIG_DEVICE_EVENT

195

Unused

196-197

ENABLE_TAG

ROUTE_REGISTER_EVENT

198

DEVICEID_TAG

ROUTE_REQUEST_EVENT

199

TIMEOUT_TAG

ROUTE_REQUEST_EVENT

200

CURRENT_ROUTE_ TAG

ROUTE_REQUEST_EVENT

201

SECONDARY_ CONNECTION_CALL_ ID

CALL_DELIVERED_EVENT

202

PRIORITY_QUEUE_ NUMBER_TAG

CALL_QUEUED_EVENT

203

TEAM_NAME_TAG

TEAM_CONFIG_EVENT

204

MEMBER_TYPE_TAG

TEAM_CONFIG_EVENT

205

EVENT_DEVICE_ID_ TAG

SYSTEM_EVENT

206

LOGIN_NAME_TAG (V11)

CONFIG_AGENT_EVENT

207

PERIPHERAL_ID_TAG (V11)

CONFIG_AGENT_EVENT, CONFIG_SERVICE_EVENT,
                                          					 CONFIG_SKILL_GROUP_EVENT, CONFIG_DEVICE_EVENT

208

CALL_TYPE_KEY_ CONFIG_TAG (V11)

CONFIG_KEY_EVENT

209

CALL_TYPE_ID_TAG (V11)

AGENT_PRE_CALL_EVENT, CONFIG_CALL_TYPE_EVENT, SET_APP_DATA

210

CUSTOMER_ DEFINITION_ID_TAG (V11)

CONFIG_CALL_TYPE_EVENT

211

ENTERPRISE_NAME_ TAG (V11)

CONFIG_CALL_TYPE_EVENT

CONFIG_MRD_EVENT

212

OLD_PERIPHERAL_ NUMBER_TAG

CONFIG_SKILL_GROUP_EVENT, CONFIG_CALL_TYPE_EVENT

213

CUR_LOGIN_ID

CONFIG_AGENT_EVENT

214

ANI_II_TAG

BEGIN_CALL_EVENT, CALL_TRANSLATION_ROUTE_ EVENT,
                                          					 CALL_DATA_UPDATE, CALL_DELIVERED_EVENT, AGENT_PRE_CALL_EVENT,
                                          					 SET_CALL_DATA_REQ, SNAPSHOT_CALL_REQ, ROUTE_REQUEST_EVENT

215

MR_DOMAIN_ID_TAG

CONFIG_SKILL_GROUP_EVENT, CONFIG_SERVICE_EVENT

CONFIG_MRD_EVENT

216

CTIOS_CIL_CLIENT_ ID_TAG

SET_CALL_DATA_REQ, ALTERNATE_CALL_REQ, ANSWER_CALL_REQ,
                                          					 CLEAR_CALL_REQ, CLEAR_CONNECTION_REQ, DEFLECT_CALL_REQ, HOLD_CALL_REQ,
                                          					 RECONNECT_CALL_REQ, RETRIEVE_CALL_REQ, SEND_DTMF_SIGNAL_REQ,
                                          					 CHANGE_MONITOR_MASK_REQ, USER_MESSAGE_REQ, SESSION_MONITOR_START_REQ,
                                          					 SESSION_MONITOR_STOP_REQ, MONITOR_AGENT_TEAM_START_REQ, MONITOR_AGENT_TEAM_
                                          					 STOP_REQ, FAILURE_CONF, CONTROL_FAILURE_CONF

217

SILENT_MONITOR_ STATUS_TAG

SNAPSHOT_DEVICE_CONF

218

REQUESTING_ DEVICE_ID_TAG

CALL_CLEAR_CONNECTION_REQ

219

REQUESTING_ DEVICE_ID_ TYPE_TAG

CALL_CLEAR_CONNECTION_REQ

220

PRE_CALL_INVOKE_ ID_TAG

AGENT_PRE_CALL_EVENT, SET_APP_DATA

221

ENTERPRISE_ QUEUE_TIME

222

CALL_REFERENCE_ ID_TAG

BEGIN_CALL_EVENT, CALL_DATA_UPDATE_EVENT, CALL_TERMINATION_EVNT,
                                          					 SNAPSHOT_CALL_CONF

223

MULTI_LINE_AGENT_ CONTROL_TAG

OPEN_CONF

224

NETWORK_
                                          					 CONTROLLED_TAG

ROUTE_SELECT_EVENT

225

Used

226-227

NUM_PERIPHERALS_ TAG

OPEN_CONF

228

COC_CONNECTION_ CALL_ID_TAG

CALL_SERVICE_INITIATED_ EVENT, ROUTE_REQUEST_EVENT, SNAPSHOT
                                          					 _CALL_CONF

229

COC_CONNECTION_ DEVICE_ID_TYPE_ TAG

CALL_SERVICE_INITIATED_ EVENT, ROUTE_REQUEST_EVENT, SNAPSHOT
                                          					 _CALL_CONF

230

COC_CONNECTION_ DEVICE_ID_TAG

CALL_SERVICE_INITIATED_ EVENT, ROUTE_REQUEST_EVENT, SNAPSHOT
                                          					 _CALL_CONF

231

CALL_ORIGINATED_ FROM_TAG

SET_CALL_DATA_REQ

232

SET_APPDATA_CALLID_TAG

233

CLIENT_SHARE_KEY_TAG

234

AGENT_TEAM_NAME_TAG

AGENT_TEAM_CONFIG_EVENT

243

DIRECTION_TAG

AGENT_STATE_EVENT

244

OPTIONS_TAG

ROUTE_REQUEST_EVENT (internal use only for ACMI PIM)

245

FLT_MRD_ID_TAG

CONFIG_MEDIA_ROUTING_DOMAIN_EVENT (Internal Cisco Use Only)

246

MEDIA_CLASS_ID_TAG

CONFIG_MEDIA_ROUTING_DOMAIN_EVENT and

CONFIG_MEDIA_CLASS_EVENT (Internal Cisco Use Only)

247

TASK_LIFE_TAG

CONFIG_MEDIA_ROUTING_DOMAIN_EVENT and

CONFIG_MEDIA_CLASS_EVENT (Internal Cisco Use Only)

248

TASK_START_TIMEOUT_TAG

CONFIG_MEDIA_ROUTING_DOMAIN_EVENT and

CONFIG_MEDIA_CLASS_EVENT (Internal Cisco Use Only)

249

MAX_TASK_DURATION_TAG

CONFIG_MEDIA_ROUTING_DOMAIN_EVENT and

CONFIG_MEDIA_CLASS_EVENT (Internal Cisco Use Only)

CONFIG_MRD_EVENT

250

INTERRUPTIBLE_TAG

CONFIG_MEDIA_ROUTING_DOMAIN_EVENT (Internal Cisco Use Only)

CONFIG_MRD_EVENT

251

MAX_CALLS_IN_QUEUE_TAG

CONFIG_MEDIA_ROUTING_DOMAIN_EVENT (Internal Cisco Use Only)

252

MAX_CALLS_IN_QUEUE_PER_CALL_TYPE_TAG

CONFIG_MEDIA_ROUTING_DOMAIN_EVENT (Internal Cisco Use Only)

253

MAX_TIME_IN_QUEUE_TAG

CONFIG_MEDIA_ROUTING_DOMAIN_EVENT (Internal Cisco Use Only)

254

INTERNAL_AGENT_STATE_TAG

QUERY_AGENT_STATE_CONF (internal use only for CCX)

255

Unused

256

SSO_ENABLED_TAG

CONFIG_AGENT_EVENT, SET_AGENT_STATE_REQ

257

FLT_TASK_ID_TAG

AGENT_TASKS_RESP, AGENT_TASKS_EVENT

258

FLT_ICM_DISP_TAG

MEDIA_LOGOUT_IND

259

FLT_APP_DISP_TAG

MEDIA_LOGOUT_IND

260

NUM_MRDS_TAG

CONFIG_AGENT_EVENT, DESKTOP_CONNECTED_IND

261

FLT_AGENT_MRD_ID_TAG

CONFIG_AGENT_EVENT, DESKTOP_CONNECTED_IND

262

FLT_AGENT_MRD_STATE_TAG

CONFIG_AGENT_EVENT

263

FLT_PRECISION_QUEUE_ID_TAG

CONFIG_SKILL_GROUP_EVENT

264

FLT_PRECISION_QUEUE_NAME_TAG

CONFIG_SKILL_GROUP_EVENT

265

MAX_BEYOND_TASK_LIMIT_TAG

AGENT_STATE_EVENT,

QUERY_AGENT_STATE_CONF,

MEDIA_LOGIN_REQ,

AGENT_INIT_REQ

266

AGENT_DESK_SETTINGS_ID_TAG

CONFIG_AGENT_EVENT

267

XFER_IN_WHILE_LOGGED_OUT_TAG

OFFER_APPLICATION_TASK_REQ

START_APPLICATION_TASK_REQ

268

PERIPHERAL_CONFIG_KEY_TAG

CONFIG_KEY_EVENT

269

AGENT_DESK_SETTINGS_CONFIG_KEY_TAG

CONFIG_AGENT_EVENT

270

CONFIG_PERIPHERAL_ID_TAG

CONFIG_PERIPHERAL_EVENT

271

DEFAULT_AGENT_DESK_SETTINGS_ID_TAG

CONFIG_PERIPHERAL_EVENT

272

FLT_DESK_SETTINGS_MASK_TAG

CONFIG_AGENT_DESK_SETTINGS_EVENT

273

FLT_WRAP_UP_DATA_INCOMING_MODE_TAG

CONFIG_AGENT_DESK_SETTINGS_EVENT

274

FLT_WRAP_UP_DATA_OUTGOING_MODE_TAG

CONFIG_AGENT_DESK_SETTINGS_EVENT

275

FLT_LOGOUT_NON_ACTIVITY_TIME_TAG

CONFIG_AGENT_DESK_SETTINGS_EVENT

276

FLT_QUALITY_RECORDING_RATE_TAG

CONFIG_AGENT_DESK_SETTINGS_EVENT

277

FLT_RING_NO_ANSWER_TIME_TAG

CONFIG_AGENT_DESK_SETTINGS_EVENT

278

FLT_SILENT_MONITOR_WARNING_MESSAGE_TAG

CONFIG_AGENT_DESK_SETTINGS_EVENT

279

FLT_SILENT_MONITOR_AUDIBLE_INDICATION_TAG

CONFIG_AGENT_DESK_SETTINGS_EVENT

280

FLT_SUPERVISOR_ASSIST_CALL_METHOD_TAG

CONFIG_AGENT_DESK_SETTINGS_EVENT

281

FLT_EMERGENCY_CALL_METHOD_TAG

CONFIG_AGENT_DESK_SETTINGS_EVENT

282

FLT_AUTO_RECORD_ON_EMERGENCY_TAG

CONFIG_AGENT_DESK_SETTINGS_EVENT

283

FLT_RECORDING_MODE_TAG

CONFIG_AGENT_DESK_SETTINGS_EVENT

284

FLT_WORK_MODE_TIMER_TAG

CONFIG_AGENT_DESK_SETTINGS_EVENT

285

FLT_RING_NO_ANSWER_DN_ID_TAG

CONFIG_AGENT_DESK_SETTINGS_EVENT

286

FLT_DEFAULT_DEVICE_PORT_ADDRESS_TAG

CONFIG_AGENT_DESK_SETTINGS_EVENT

287

DESKTOP_CONNECTED_FLAG_TAG

AGENT_TASKS_REQUEST_EVENT

288

PLAY_TONE_DIRECTION_TAG

START_NETWORK_RECORDING_REQ

289

INVOCATION_TYPE_TAG

START_NETWORK_RECORDING_REQ, STOP_NETWORK_RECORDING_REQ

290

RECORDER_ADDRESS_TAG

NETWORK_RECORDING_TARGET_INFO_EVENT

291

TERMINAL_NAME_TAG

NETWORK_RECORDING_TARGET_INFO_EVENT

292

MEDIA_FORKING_DEVICE_NAME_TAG

NETWORK_RECORDING_TARGET_INFO_EVENT

293

PROTOCOL_REFERENCE_GUID_TAG

NETWORK_RECORDING_TARGET_INFO_EVENT

AGENT_PRE_CALL_EVENT

294

MEDIA_FORKING_CLUSTER_ID_TAG

NETWORK_RECORDING_TARGET_INFO_EVENT

295

RECORDER_URI_TAG

NETWORK_RECORDING_TARGET_INFO_EVENT

296

RECORDER_ERROR_MSG_TAG

NETWORK_RECORDING_TARGET_INFO_EVENT

297

RECORDER_TYPE_TAG

NETWORK_RECORDING_TARGET_INFO_EVENT

298

RECORDER_STATUS_TAG

NETWORK_RECORDING_TARGET_INFO_EVENT

299

RECORDING_DEVICE_ID_TAG

NETWORK_RECORDING_STARTED_EVENT, NETWORK_RECORDING_ENDED_EVENT, NETWORK_RECORDING_FAILED_EVENT, NETWORK_RECORDING_TARGET_INFO_EVENT

300

FLT_TERM_TYPE

CONFIG_TERMINAL_EVENT

302

FLT_TERM_DEVICE_NAME

CONFIG_TERMINAL_EVENT,CONFIG_AGENT_EVENT, SET_AGENT_STATE_REQ, AGENT_STATE_EVENT

303

FLT__TERM_TYPE_NAME

CONFIG_TERMINAL_EVENT

304

FLT_NUM_INSTRUMENTS

CONFIG_TERMINAL_EVENT

305

ACD_SHARED_LINE_USAGE

AGENT_DESK_SETTINGS_CONF

CONFIG_AGENT_DESK_SETTINGS_EVENT

306

PLAY_ZIP_TONE

AGENT_DESK_SETTINGS_CONF

CONFIG_AGENT_DESK_SETTINGS_EVENT

307

FLT_ENABLED_SERVICES

CONFIG_AGENT_SERVICE_EVENT

SET_AGENT_SERVICE_DATA_REQ

309

NUM_OF_ENABLED_SERVICES

CONFIG_AGENT_SERVICE_EVENT

SET_AGENT_SERVICE_DATA_REQ

310

CCAI_CONFIG_ID

AGENT_PRE_CALL_EVENT

311

MEDIA_TYPE_TAG

MEDIA_LOGIN_REQ

312

MEDIA_PROVIDER_TAG

MEDIA_LOGIN_REQ

313

## AgentState
                        	 Values

This
                              		  table shows the agent state values that may appear in the
                              		  QUERY_AGENT_STATE_CONF messages.

State Name

Description

Value

AGENT_STATE_ LOGIN

The agent
                                          					 has logged on to the ACD. It does not necessarily indicate that the agent is
                                          					 ready to accept calls.

0

AGENT_STATE_ LOGOUT

The agent
                                          					 has logged out of the ACD and cannot accept any additional calls.

1

AGENT_STATE_ NOT_ READY

The agent
                                          					 is unavailable for any call work.

2

AGENT_STATE_ AVAILABLE

The agent
                                          					 is ready to accept a call.

3

AGENT_STATE_ TALKING

The agent
                                          					 is currently talking on a call (inbound, outbound, or inside).

4

AGENT_STATE_ WORK_NOT_READY

The agent
                                          					 is performing after call work, but will not be ready to receive a call when
                                          					 completed.

5

AGENT_STATE_ WORK_ READY

The agent
                                          					 is performing after call work, and will be ready to receive a call when
                                          					 completed.

6

AGENT_STATE_ BUSY_ OTHER

The agent
                                          					 is busy performing a task associated with another active SkillGroup.

7

AGENT_STATE_ RESERVED

The agent
                                          					 is reserved for a call that will arrive at the ACD shortly.

8

AGENT_STATE_ UNKNOWN

The agent
                                          					 state is currently unknown.

9

AGENT_STATE_ HOLD

The agent
                                          					 currently has all calls on hold.

10

AGENT_STATE_ ACTIVE

The agent
                                          					 state is currently active.

11

AGENT_STATE_ PAUSED

The agent
                                          					 state is currently paused.

12

AGENT_STATE_ INTERRUPTED

The agent
                                          					 state is currently interrupted.

13

AGENT_STATE_NOT_ACTIVE

The agent
                                          					 state is currently not active.

14

## PGStatusCode
                        	 Values

This
                              		  table shows the PGStatusCode values that may be included in the SYSTEM_EVENT
                              		  message.

PGStatus

Description

Mask Value

PGS_OPC_DOWN

Communication lost between the CTI Server and the PG’s Open
                                          					 Peripheral Controller (OPC) process. No call or agent state event messages can
                                          					 be sent due to this condition.

0x00000001

PGS_CC_DOWN

Communication lost between the PG and the Unified CCE Central
                                          					 Controller. Primarily affects translation routing and post-routing, other call
                                          					 and agent event messages can still be sent.

0x00000002

PGS_PERIPHERAL_OFFLINE

One or
                                          					 more of the peripherals monitored by the PG are offline.

0x00000004

PGS_CTI_SERVER_OFFLINE

Loss of
                                          					 communication between the CTI Server and the CTI Client. This status code is
                                          					 not reported by a software layer between the CTI Server and the client
                                          					 application.

0x00000008

PGS_LIMITED_FUNCTION

This
                                          					 status code may be reported by a software layer between the CTI Server and the
                                          					 client application when PGS_CTI_SERVER_ OFFLINE is true to indicate that
                                          					 limited local call control is possible.

0x00000010

## PeripheralType
                        	 Values

This
                              		  table shows the PeripheralType values that may be included in the Client Events
                              		  service messages.

Peripheral
                                          					 Type

Description

Value

PT_NONE

Not
                                          					 Applicable

0xffff

PT_MERIDIAN

Northern
                                          					 Telecom Meridian ACD

2

PT_G2

Lucent G2

3

PT_DEFINITY_ECS_ NON_EAS

Lucent
                                          					 DEFINITY ECS (without Expert Agent Selection)

4

PT_DEFINITY_ECS_ EAS

Lucent
                                          					 DEFINITY ECS (with Expert Agent Selection)

5

PT_GALAXY

Obsolete

6

PT_SPECTRUM

Obsolete

7

PT_VRU

VRU (event
                                          					 type interface)

8

PT_VRU_POLLED

VRU
                                          					 (polled type interface)

9

PT_DMS100

Obsolete

10

PT_SIEMENS_9006

Siemens
                                          					 Hicom ACD (9006)

11

PT_SIEMENS_9005

Siemens
                                          					 9751 CBX Release 9005 (Rolm 9005)

12

PT_ALCATEL

Alcatel
                                          					 4400 ACD

13

PT_NEC_NEAX_2x00

Obsolete

14

PT_
                                          					 ACP_1000

Ericsson
                                          					 ACP1000

15

PT_ENTERPRISE_ AGENT

Unified
                                          					 CCE Manager

17

PT_MD110

Ericsson
                                          					 MD-110

18

PT_MEDIA_ROUTING

Media
                                          					 Routing

19

PT_GENERIC

Generic

20

PT_ACMI_CRS

A
                                          					 Gateway PG over Unified CCX

21

PT_ACMI_IPCC

A
                                          					 Gateway PG over Unified CCE or Unified CCX

22

PT_ARS

A system
                                          					 using the ARS PG

24

PT_ACMI_ERS

A system
                                          					 using the ERS PG

25

PT_ACMI_EXPERT_ADVISOR

Obsolete

26

{reserved}

27

## LocalConnectionState Values

This
                              		  table shows the LocalConnectionState values.

LocalConnectionState

Description

Value

LCS_NONE

Not
                                          					 applicable

0xffff

LCS_NULL

No
                                          					 relationship between call and device.

0

LCS_INITIATE

Device
                                          					 requesting service (“dialing”).

1

LCS_ALERTING

Device is
                                          					 alerting (“ringing”).

2

LCS_CONNECT

Device is
                                          					 actively participating in the call.

3

LCS_HOLD

Device is
                                          					 inactively participating in the call.

4

LCS_QUEUED

Device is
                                          					 stalled attempting to connect to a call, or a call is stalled attempting to
                                          					 connect to a device.

5

LCS_FAIL

A
                                          					 device-to-call or call-to-device connection attempt has been aborted.

6

## EventCause
                        	 Values

These tables show the EventCause values.

EventCause

Value

CEC_NONE

0xffff

CEC_ACTIVE_MONITOR

1

CEC_ALTERNATE

2

CEC_BUSY

3

CEC_CALL_BACK

4

CEC_CALL_CANCELLED

5

CEC_CALL_FORWARD_ALWAYS

6

CEC_CALL_FORWARD_BUSY

7

CEC_CALL_FORWARD_NO_ANSWER

8

CEC_CALL_FORWARD

9

CEC_CALL_NOT_ANSWERED

10

CEC_CALL_PICKUP

11

CEC_CAMP_ON

12

CEC_DEST_NOT_OBTAINABLE

13

CEC_DO_NOT_DISTURB

14

CEC_INCOMPATIBLE_DESTINATION

15

CEC_INVALID_ACCOUNT_CODE

16

CEC_KEY_CONFERENCE

17

CEC_LOCKOUT

18

CEC_MAINTENANCE

19

CEC_NETWORK_CONGESTION

20

CEC_NETWORK_NOT_OBTAINABLE

21

CEC_NEW_CALL

22

CEC_NO_AVAILABLE_AGENTS

23

CEC_OVERRIDE

24

CEC_PARK

25

CEC_OVERFLOW

26

CEC_RECALL

27

CEC_REDIRECTED

28

CEC_REORDER_TONE

29

CEC_RESOURCES_NOT_AVAILABLE

30

CEC_SILENT_MONITOR

31

CEC_TRANSFER

32

CEC_TRUNKS_BUSY

33

CEC_VOICE_UNIT_INITIATOR

34

CEC_TIME_OUT

35

CEC_NEW_CALL_INTERFLOW

36

CEC_SIMULATION_INIT_REQUEST

37

CEC_SIMULATION_RESET_REQUEST

38

CEC_CTI_LINK_DOWN

39

CEC_PERIPHERAL_RESET_REQUEST

40

CEC_MD110_CONFERENCE_TRANSFER

41

CEC_REMAINS_IN_Q

42

CEC_SUPERVISOR_ASSIST

43

CEC_EMERGENCY_CALL

44

CEC_SUPERVISOR_CLEAR

45

CEC_SUPERVISOR_MONITOR

46

CEC_SUPERVISOR_WHISPER

47

CEC_SUPERVISOR_BARGE_IN

48

CEC_SUPERVISOR_INTERCEPT

49

CEC_CALL_PARTY_UPDATE_IND

50

CEC_CONSULT

51

CEC_NIC_CALL_CLEAR

52

CEC_DNP

53

CEC_ ROUTER_REQUERY_BEFORE_ANSWER

54

CEC_ROUTER_REQUERY_AFTER_ANSWER

55

CEC_ NETWORK_ERROR

56

CEC_ NETWORK_ERROR_BEFORE_ANSWER

57

CEC_NETWORK_ERROR_AFTER_ANSWER

58

CEC_ GREETING

59

CEC_ RECORD_AGENT_GREETING

60

CEC_SNAPSHOT

61

CEC_ MAX_QUEUE_EXCEEDED

62

Extended
                                 				Call Cleared Event Causes

EventCause

Value

CECX_ABAND_NETWORK

1001

CECX_ABAND_LOCAL_QUEUE

1002

CECX_ABAND_RING

1003

CECX_ABAND_DELAY

1004

CECX_ABAND_INTERFLOW

1005

CECX_ABAND_AGENT_TERMINAL

1006

CECX_SHORT

1007

CECX_BUSY

1008

CECX_FORCED_BUSY

1009

CECX_DROP_NO_ANSWER

1010

CECX_DROP_BUSY

1011

CECX_DROP_REORDER

1012

CECX_DROP_HANDLED_PRIMARY_ROUTE

1013

CECX_DROP_HANDLED_OTHER

1014

CECX_REDIRECTED

1015

CECX_CUT_THROUGH

1016

CECX_INTRAFLOW

1017

CECX_INTERFLOW

1018

CECX_RING_NO_ANSWER

1019

CECX_INTERCEPT_REORDER

1020

CECX_INTERCEPT_DENIAL

1021

CECX_TIME_OUT

1022

CECX_VOICE_ENERGY

1023

CECX_NONCLASSIFIED_ENERGY_DETECT

1024

CECX_NO_CUT_THROUGH

1025

CECX_UABORT

1026

CECX_FAILED_SOFTWARE

1027

CECX_BLIND_TRANSFER

1028

CECX_ANNOUNCED_TRANSFER

1029

CECX_CONFERENCED

1030

CECX_DUPLICATE_TRANSFER

1031

CECX_UNMONITORED_DEVICE

1032

CECX_ANSWERING_MACHINE

1033

CECX_NETWORK_BLIND_TRANSFER

1034

CECX_TASK_ABANDONED_IN_ROUTER

1035

CECX_TASK_ABANDONED_BEFORE_OFFERED

1036

CECX_TASK_ABANDONED_WHILE_OFFERED

1037

CECX_NORMAL_END_TASK

1038

CECX_CANT_OBTAIN_TASK_ID

1039

CECX_AGENT_LOGGED_OUT_DURING_TASK

1040

CECX_MAX_TASK_LIFETIME_EXCEEDED

1041

CECX_APPLICATION_PATH_WENT_DOWN

1042

CECX_ICM_ROUTING_COMPLETE

1043

CECX_ICM_ROUTING_DISABLED

1044

CECX_APPL_INVALID_MRD_ID

1045

CECX_APPL_INVALID_DIALOGUE_ID

1056

CECX_APPL_DUPLICATE_DIALOGUE_ID

1047

CECX_APPL_INVALID_INVOKE_ID

1048

CECX_APPL_INVALID_SCRIPT_SELECTOR

1049

CECX_APPL_TERMINATE_DIALOGUE

1050

CECX_TASK_ENDED_DURING_APP_INIT

1051

CECX_CALLED_PARTY_DISCONNECTED

1052

CECX_PARTIAL_CALL

1053

CECX_DROP_NETWORK_CONSULT

1054

CECX_NETWORK_CONSULT_TRANSFER

1055

CECX_NETWORK_CONFERENCE

1056

CECX_ABAND_NETWORK_CONSULT

1057

## DeviceIDType
                        	 Values

This
                              		  table shows the DeviceIDType values.

Device ID
                                          					 Type

Description

Value

DEVID_NONE

No device
                                          					 ID is provided.

0xffff

DEVID_DEVICE_IDENTIFIER

The
                                          					 provided device ID identifies a peripheral teleset (extension).

0

DEVID_TRUNK_IDENTIFIER

The
                                          					 provided device ID identifies a peripheral Trunk.

70

DEVID_TRUNK_GROUP_ IDENTIFIER

The
                                          					 provided device ID identifies a peripheral Trunk Group.

71

DEVID_IP_PHONE_MAC_ IDENTIFIER

The
                                          					 provided device ID identifiers the MAC address of an IP phone (Unified CCX
                                          					 ONLY).

72

DEVID_CTI_PORT

The
                                          					 provided device ID identifiers a CTI PORT (Unified CCX ONLY).

73

DEVID_ROUTE_POINT

The
                                          					 provided device ID identifies a ROUTE POINT.

74

DEVID_EXTERNAL

The
                                          					 provided device ID is an ANI number or some other external identifier.

75

DEVID_AGENT_DEVICE

The
                                          					 provided device ID is the ID of an AGENT Device (phone).

76

DEVID_QUEUE

The
                                          					 provided device ID is the ID of a QUEUE.

77

DEVID_NON_ACD_DEVICE_ IDENTIFIER

The
                                          					 provided device ID identifies a peripheral telset (extension) that is
                                          					 classified as being a non-ACD extension.

78

DEVID_SHARED_DEVICE_ IDENTIFIER

The
                                          					 provided device ID identifies a peripheral telset (extension) that is
                                          					 classified as being a shared line (0 or more telsets share this extension).

79

## CallType
                        	 Values

This
                              		  table shows the CallType values.

CallType

Description

Value

CALLTYPE_ACD_IN

Inbound ACD call.

In Unified CCE, it indicates that this is a post route request.

1

CALLTYPE
                                          					 _PREROUTE_ ACD_IN

Translation routed inbound ACD call.

2

CALLTYPE
                                          					 _PREROUTE_ DIRECT_AGENT

Translation routed call to a specific agent.

3

CALLTYPE
                                          					 _TRANSFER_IN

Transferred inbound call.

4

CALLTYPE
                                          					 _OVERFLOW_IN

Overflowed
                                          					 inbound call.

5

CALLTYPE
                                          					 _OTHER_IN

Inbound
                                          					 call.

6

CALLTYPE
                                          					 _AUTO_OUT

Automatic
                                          					 out call.

7

CALLTYPE
                                          					 _AGENT_OUT

Agent out
                                          					 call.

8

CALLTYPE
                                          					 _OUT

Outbound
                                          					 call.

9

CALLTYPE
                                          					 _AGENT_INSIDE

Agent
                                          					 inside call.

10

CALLTYPE
                                          					 _OFFERED

Blind
                                          					 transferred call.

11

CALLTYPE
                                          					 _CONSULT

Consult
                                          					 call.

12

CALLTYPE
                                          					 _CONSULT_ OFFERRED

Announced
                                          					 transferred call.

13

CALLTYPE
                                          					 _CONSULT_ CONFERENCE

Conferenced consult call.

14

CALLTYPE
                                          					 _CONFERENCE

Conference
                                          					 call.

15

CALLTYPE_UNMONITORED

Inside or
                                          					 outbound call for which no call events will be received.

16

CALLTYPE_PREVIEW

Automatic
                                          					 out call in which the agent is given the option to proceed to dial a contact.

17

CALLTYPE_RESERVATION

Call made
                                          					 to reserve an agent for some other function.

18

CALLTYPE_ASSIST

Call to
                                          					 supervisor for assistance.

19

CALLTYPE_EMERGENCY

Emergency
                                          					 call.

20

CALLTYPE_SUPERVISOR_ MONITOR

Supervisor
                                          					 silently monitoring call.

21

CALLTYPE_SUPERVISOR_ WHISPER

Supervisor monitoring call, agent can hear supervisor.

22

CALLTYPE_SUPERVISOR_ BARGEIN

Supervisor conferenced into call.

23

CALLTYPE_SUPERVISOR_ INTERCEPT

Supervisor replaces agent on call.

24

CALLTYPE_TASK_ROUTED_BY_ICM

Task
                                          					 routed by Unified CCE

25

CALLTYPE_TASK_ROUTED_BY_APPLICATION

Task
                                          					 routed by application

26

CALLTYPE_NON_ACD

Agent
                                          					 call that is a non-ACD routed call.

27

RESERVATION_PREVIEW

Call
                                          					 type for Outbound Option Reservation calls for Preview mode.

27

RESERVATION_PREVIEW_DIRECT

Call
                                          					 type for Outbound Option Reservation calls for Direct Preview mode.

28

RESERVATION_PREDICTIVE

Call
                                          					 type for Outbound Option Reservation calls for Predictive mode and Progressive
                                          					 mode.

29

RESERVATION_CALLBACK

Call
                                          					 type for Outbound Option Reservation calls for Callback calls.

30

RESERVATION_PERSONAL_CALLBACK

Call
                                          					 type for Outbound Option Reservation calls for Personal Callback calls.

31

CUSTOMER_PREVIEW

Call
                                          					 type for Outbound Option Customer calls for Preview mode.

32

CUSTOMER_PREVIEW_DIRECT

Call
                                          					 type for Outbound Option

Customer
                                          					 calls for Direct Preview

33

CUSTOMER_PREDICTIVE

Call
                                          					 type for Outbound Option Customer calls for Predictive mode and Progreassive
                                          					 modefor agentbased campaigns.

34

CUSTOMER_CALLBACK

Call
                                          					 type for Outbound Option Customer calls for callback calls.

35

CUSTOMER_PERSONAL

Call
                                          					 type for Outbound Option Customer calls for personal callback calls.

36

CUSTOMER_IVR

Call
                                          					 type for Outbound Option Customer calls for Transfer to IVR campaigns.

37

CALLTYPE_NON_ACD

Agent
                                          					 call that is a non-ACD call.

38

CALLTYPE_PLAY_AGENT_GREETING

An agent
                                          					 greeting route request.

39

CALLTYPE_RECORD_AGENT_GREETING

Record
                                          					 agent greeting call initiated by AGENT_GREETING_CONTROL_REQ.

40

CALLTYPE_VOICE_CALL_BACK

Voice
                                          					 callback using the Agent Request API.

41

## ConnectionDeviceIDType Values

This
                              		  table shows the possible ConnectionDeviceIDType values.

ConnectionDevice IDType

Description

Value

CONNECTION_ID_ NONE

No
                                          					 ConnectionDeviceID is provided.

0xffff

CONNECTION_ID_ STATIC

The
                                          					 ConnectionDeviceID value is stable over time (between calls).

0

CONNECTION_ID_ DYNAMIC

The
                                          					 ConnectionDeviceID value is dynamic and may change between calls.

1

## LineType
                        	 Values

This
                              		  table shows the possible LineType values.

LineType

Description

Value

LINETYPE_INBOUND_ ACD

Line used
                                          					 for inbound ACD calls.

0

LINETYPE_OUTBOUND_ACD

Line used
                                          					 for outbound ACD calls.

1

LINETYPE_INSIDE

Line used
                                          					 for inside calls.

2

LINETYPE_UNKNOWN

Line used
                                          					 for any purpose.

3

LINETYPE_SUPERVISOR

Line used
                                          					 for supervisor calls.

4

LINETYPE_MESSAGE

Line used
                                          					 for voice messages.

5

LINETYPE_HELP

Line used
                                          					 for assistance.

6

LINETYPE_OUTBOUND

Line used
                                          					 for outbound non-ACD calls.

7

LINETYPE_DID

Line used
                                          					 for direct inward dialed calls.

8

LINETYPE_SILENT_ MONITOR

Line used
                                          					 for silent monitor.

9

LINETYPE_NON_ACD_IN

Line used
                                          					 for inbound non-ACD calls.

10

LINETYPE_NON_ACD_OUT

Line used
                                          					 for outbound non-ACD calls.

11

## ControlFailureCode
                        	 Values

This
                              		  table shows the possible ControlFailureCode values.

FailureCode

Description

Value

CF_GENERIC_UNSPECIFIED

An error
                                          					 has occurred that is not one of the following error types.

0

CF_GENERIC_OPERATION

An
                                          					 operation error occurred (no specific details available).

1

CF_REQUEST_ INCOMPATIBLE_WITH_ OBJECT

The
                                          					 request is not compatible with the object.

2

CF_VALUE_OUT_OF_ RANGE

The
                                          					 parameter has a value that is not in the range defined for the server.

3

CF_OBJECT_NOT_KNOWN

The
                                          					 parameter has a value that is not known to the server.

4

CF_INVALID_CALLING_ DEVICE

The
                                          					 calling device is invalid.

5

CF_INVALID_CALLED_ DEVICE

The called
                                          					 device is invalid

6

CF_INVALID_FORWARDING_ DESTINATION

The
                                          					 forwarding destination device is invalid.

7

CF_PRIVILEGE_VIOLATION_ ON_SPECIFIED_DEVICE

The
                                          					 specified device is not authorized for the service.

8

CF_PRIVILEGE_VIOLATION_ ON_CALLED_DEVICE

The called
                                          					 device is not authorized for the service.

9

CF_PRIVILEGE_VIOLATION_ ON_CALLING_DEVICE

The
                                          					 calling device is not authorized for the service.

10

CF_INVALID_CSTA_CALL_ IDENTIFIER

The call
                                          					 identifier is invalid.

11

CF_INVALID_CSTA_DEVICE_ IDENTIFIER

The device
                                          					 identifier is invalid.

12

CF_INVALID_CSTA_ CONNECTION_IDENTIFIER

The
                                          					 connection identifier is invalid.

13

CF_INVALID_DESTINATION

The
                                          					 request specified a destination that is invalid.

14

CF_INVALID_FEATURE

The
                                          					 request specified a feature that is invalid.

15

CF_INVALID_ALLOCATION_ STATE

The
                                          					 request specified an allocation state that is invalid.

16

CF_INVALID_CROSS_REF_ID

The
                                          					 request specified a cross- reference ID that is not in use at this time.

17

CF_INVALID_OBJECT_TYPE

The
                                          					 request specified an invalid object type.

18

CF_SECURITY_VIOLATION

Security
                                          					 error (no specific details available).

19

CF_GENERIC_STATE_ INCOMPATIBILITY

The
                                          					 request is not compatible with the condition of a related device.

21

CF_INVALID_OBJECT_STATE

The
                                          					 object is in the incorrect state for the request.

22

CF_INVALID_CONNECTION_ ID_FOR_ACTIVE_CALL

The
                                          					 active connection ID in the request is invalid.

23

CF_NO_ACTIVE_CALL

There is
                                          					 no active call for the request.

24

CF_NO_HELD_CALL

There is
                                          					 no held call for the request.

25

CF_NO_CALL_TO_CLEAR

There is
                                          					 no call associated with the given connection ID.

26

CF_NO_CONNECTION_TO_ CLEAR

There is
                                          					 no call connection for the given connection ID.

27

CF_NO_CALL_TO_ANSWER

There is
                                          					 no alerting call to be answered.

28

CF_NO_CALL_TO_ COMPLETE

There is
                                          					 no active call to be completed.

29

CF_GENERIC_SYSTEM_ RESOURCE_AVAILABILITY

The
                                          					 request failed due to lack of system resources (no specific details available).

31

CF_SERVICE_BUSY

The
                                          					 service is temporarily unavailable.

32

CF_RESOURCE_BUSY

An
                                          					 internal resource is busy.

33

CF_RESOURCE_OUT_OF_ SERVICE

The
                                          					 service requires a resource that is out of service.

34

CF_NETWORK_BUSY

The
                                          					 server sub-domain is busy.

35

CF_NETWORK_OUT_OF_ SERVICE

The
                                          					 server sub-domain is out of service.

36

CF_
                                          					 OVERALL_MONITOR_ LIMIT_EXCEEDED

The
                                          					 request would exceed the server’s overall resource limits.

37

CF_CONFERENCE_MEMBER_ LIMIT_EXCEEDED

The
                                          					 request would exceed the server’s limit on the number of conference members.

38

CF_
                                          					 GENERIC_SUBSCRIBED_ RESOURCE_AVAILABILITY

The
                                          					 request failed due to lack of purchased or contracted resources (no specific
                                          					 details available).

41

CF_
                                          					 OBJECT_MONITOR_ LIMIT_EXCEEDED

The
                                          					 request would exceed the server’s specific resource limits.

42

CF_
                                          					 EXTERNAL_TRUNK_ LIMIT_EXCEEDED

The
                                          					 request would exceed the limit of external trunks.

43

CF_
                                          					 OUTSTANDING_ REQUEST_LIMIT_EXCEEDED

The
                                          					 request would exceed the limit of outstanding requests.

44

CF_GENERIC_ PERFORMANCE_ MANAGEMENT

The
                                          					 request failed as a performance management mechanism (no specific details
                                          					 available).

51

CF_PERFORMANCE_LIMIT_ EXCEEDED

The
                                          					 request failed because a performance management limit was exceeded.

52

CF_
                                          					 SEQUENCE_NUMBER_ VIOLATED

The
                                          					 server has detected an error in the sequence number of the operation.

61

CF_
                                          					 TIME_STAMP_ VIOLATED

The
                                          					 server has detected an error in the time stamp of the operation.

62

CF_
                                          					 PAC_VIOLATED

The
                                          					 server has detected an error in the PAC of the operation.

63

CF_
                                          					 SEAL_VIOLATED

The
                                          					 server has detected an error in the Seal of the operation.

64

CF_
                                          					 GENERIC_UNSPECIFIED_ REJECTION

The
                                          					 request has been rejected (no specific details available).

70

CF_
                                          					 GENERIC_OPERATION_ REJECTION

The
                                          					 requested operation has been rejected (no specific details available).

71

CF_
                                          					 DUPLICATE_ INVOCATION_REJECTION

The
                                          					 request duplicated another request for the same service.

72

CF_
                                          					 UNRECOGNIZED_ OPERATION_REJECTION

The
                                          					 request specified an unrecognized operation.

73

CF_MISTYPED_ARGUMENT_ REJECTION

The
                                          					 request contained a parameter of the wrong type for the requested operation.

74

CF_
                                          					 RESOURCE_LIMITATION_ REJECTION

The
                                          					 request would have exceeded a resource limitation.

75

CF_
                                          					 ACS_HANDLE_ TERMINATION_REJECTION

The
                                          					 request specified an ACS handle that is no longer in use.

76

CF_
                                          					 SERVICE_ TERMINATION_REJECTION

The
                                          					 request failed because the required service has been terminated.

77

CF_
                                          					 REQUEST_TIMEOUT_ REJECTION

The
                                          					 request failed because a timeout limit was exceeded.

78

CF_REQUESTS_ON_DEVICE_ EXCEEDED_REJECTION

The
                                          					 request would have exceeded the limits of the device.

79

Extended
                                 				Control Failure Codes

FailureCode

Description

Value

CF_INVALID_AGENT_ID_ SPECIFIED

The
                                          						request specified an invalid AgentID.

256

CF_INVALID_PASSWORD_ SPECIFIED

The
                                          						request specified an invalid agent password.

257

CF_INVALID_AGENT_ID_ OR_PASSWORD_SPECIFIED

The
                                          						request specified an invalid AgentID and/or invalid agent password.

258

CF_SPECIFIED_AGENT_ ALREADY_SIGNED_ON

The
                                          						request failed because the specified agent is already logged in.

259

CF_INVALID_LOGON_ DEVICE_SPECIFIED

The
                                          						request specified an invalid logon device.

260

CF_INVALID_ANSWERING_ DEVICE_SPECIFIED

The
                                          						request specified an invalid answering device.

261

CF_INVALID_SKILL_ GROUP_SPECIFIED

The
                                          						request specified an invalid agent skill group.

262

CF_INVALID_CLASS_OF_ SERVICE_SPECIFIED

The
                                          						request specified an invalid class of service.

263

CF_INVALID_TEAM_ SPECIFIED

The
                                          						request specified an invalid team.

264

CF_INVALID_AGENT_ WORKMODE

The
                                          						request specified an invalid agent work mode.

265

CF_INVALID_AGENT_ REASON_CODE

The
                                          						request specified an invalid agent reason code.

266

CF_ADJUNCT_SWITCH_ COMM_ERROR

A
                                          						communication error occurred on the datalink between the Unified CCE and the
                                          						ACD.

267

CF_AGENT_NOT_PARTY_ ON_CALL

The
                                          						specified agent is not a party on the indicated call.

268

CF_INTERNAL_ PROCESSING_ERROR

An
                                          						internal error occurred in the ACD while processing the request.

269

CF_TAKE_CALL_CONTROL_ REJECTION

The
                                          						ACD refused an Unified CCE request to take control of a call.

270

CF_TAKE_DOMAIN_ CONTROL_REJECTION

The
                                          						ACD refused an Unified CCE request to take control of a domain.

271

CF_REQUESTED_SERVICE_ NOT_REGISTERED

The
                                          						Unified CCE is not registered on the ACD for the requested service.

272

CF_INVALID_CONSULT_ TYPE

The
                                          						consult type is invalid.

273

CF_ANSMAP_OR_ ADPARAM_FIELD_NOT_VALID

The
                                          						Ansmap or Asparam field are not valid.

274

CF_INVALID_CALL_ CONTROL_TABLE_ SPECIFIED

The
                                          						call control table is invalid.

275

CF_INVALID_DIGITS_ RNATIMEOUT_AMSDELAY_ OR_COUNTRY

276

CF_ANSWER_DETECT_ PORT_UNAVAILABLE

277

CF_VIRTUAL_AGENT_ UNAVAILABLE

278

CF_TAKEBACK_N_XFER_ ROUTE_END

279

CF_WRAPUP_DATA_ REQUIRED

280

CF_REASON_CODE_ REQUIRED

281

CF_INVALID_TRUNK_ID_ SPECIFIED

282

CF_SPECIFIED_EXTENSION_ ALREADY_IN_USE

283

CF_ARBITRARY_CONF_OR_ XFER_NOT_SUPPORTED

284

CF_NETWORK_TRANSFER_OR_ CONSULT

285

CF_NETWORK_TRANSFER_OR_ CONSULT_FAILED

286

CF_DEVICE_RESTRICTED

287

CF_LINE_RESTRICTED

288

CF_AGENT_ACCOUNT_ LOCKED_OUT

289

CF_DROP_ANY_PARTY_NOT_ ENABLED_CTI

290

CF_MAXIMUM_LINE_LIMIT_ EXCEEDED

291

CF_SHARED_LINES_NOT_ SUPPORTED

292

CF_EXTENSION_NOT_UNIQUE

293

CF_UNKNOWN_ INTERFACE_ CTRLR_ID

The
                                          						Interface Controller ID is unknown.

1001

CF_INVALID_INTERFACE_ CTRLR_TYPE

The
                                          						Interface Controller type is invalid.

1002

CF_SOFTWARE_REV_NO_ SUPPORTED

The
                                          						current software revision is not supported.

1003

CF_UNKNOWN_PID

The
                                          						PeripheralID is unknown.

1004

CF_INVALID_TABLE_ SPECIFIED

An
                                          						invalid table was specified.

1005

CF_PD_SERVICE_INACTIVE

The
                                          						peripheral data service is not active.

1006

CF_UNKNOWN_ROUTING_ CLIENT_ID

The
                                          						RoutingClientID is unknown.

1007

CF_RC_SERVICE_ INACTIVATE

The
                                          						routing client service is not active.

1008

CF_INVALID_DIALED_ NUMBER

The
                                          						dialed number is invalid.

1009

CF_INVALID_PARAMETER

A
                                          						parameter in the request is invalid.

1010

CF_UNKNOWN_ROUTING_ PROBLEM

An
                                          						unspecified error occurred during routing.

1011

CF_UNSUPPORTED_PD_ MESSAGE_REVISION

The
                                          						requested peripheral data service protocol version is not supported.

1012

CF_UNSUPPORTED_RC_ MESSAGE_REVISION

The
                                          						requested routing client service protocol version is not supported.

1013

CF_UNSUPPORTED_IC_ MESSAGE_REVISION

The
                                          						requested interface controller service protocol version is not supported.

1014

CF_RC_SERVICE_ INACTIVATE_PIM

The
                                          						peripheral interface is not active.

1015

CF_AGENT_GREETING_CONTROL_OPERATION_FAILURE

This
                                          						error occurs if AGENT_GREETING_CONTROL_REQ request fails.

Notes:
                                          						All detailed errors are defined as Peripheral Error Codes.

1016

## AllocationState
                        	 Values

This
                              		  table shows the AllocationState values.

AllocationState

Description

Value

ALLOC_CALL_ DELIVERED

Connect
                                          					 call to originating device when call is delivered (alerting).

0

ALLOC_CALL_ ESTABLISHED

Connect
                                          					 call to originating device when call is established (answered).

1

## ForwardType
                        	 Values

This
                              		  table shows the ForwardType values.

ForwardType

Description

Value

FWT_IMMEDIATE

Forward
                                          					 all calls.

0

FWT_BUSY

Forward
                                          					 only when busy.

1

FWT_NO_ANS

Forward
                                          					 after no answer.

2

FWT_BUSY_INT

Forward on
                                          					 busy for internal calls.

3

FWT_BUSY_EXT

Forward on
                                          					 busy for external calls.

4

FWT_NO_ANS_INT

Forward
                                          					 after no answer for internal calls.

5

FWT_NO_ANS_EXT

Forward
                                          					 after no answer for external calls.

6

## TypeOfDevice
                        	 Values

This
                              		  table shows the TypeOfDevice values.

TypeOfDevice

Description

Value

DEVT_STATION

A
                                          					 traditional telephone device, consisting of one or more buttons and one or more
                                          					 lines.

0

DEVT_LINE

A
                                          					 communications interface to one or more stations.

1

DEVT_BUTTON

An
                                          					 instance of a call manipulation point at an individual station.

2

DEVT_ACD

A
                                          					 mechanism that distributes calls.

3

DEVT_TRUNK

A device
                                          					 used to access other switching domains.

4

DEVT_OPERATOR

A device
                                          					 that interacts with a call party to assist in call setup or provide other
                                          					 telecommunications service.

5

DEVT_STATION_ GROUP

Two or
                                          					 more stations used interchangeably or addressed identically.

16

DEVT_LINE_GROUP

A set of
                                          					 communications interfaces to one or more stations.

17

DEVT_BUTTON_ GROUP

Two or
                                          					 more instances of a call manipulation point at an individual station.

18

DEVT_ACD_GROUP

A call
                                          					 distributor device as well as the devices to which it distributes calls.

19

DEVT_TRUNK_ GROUP

A set of
                                          					 trunks providing connectivity to the same place. Individual trunks within the
                                          					 group may be used interchangeably.

20

DEVT_OPERATOR_ GROUP

Two or
                                          					 more operator devices used interchangeably or addressed identically.

21

DEVT_CTI_PORT_ SCCP

A CTI port
                                          					 on a Unified CM device.

22

DEVT_CTI_PORT_SIP

A CTI port
                                          					 on a SIP device.

23

DEVT_OTHER

A device
                                          					 that does not fall into any of the preceding categories.

255

## ClassOfDevice
                        	 Values

This
                              		  table shows the ClassOfDevice values.

ClassOfDevice

Description

Value

DEVC_OTHER

A class of
                                          					 device not covered by the following image, data, or voice classes.

10x

DEVC_IMAGE

A device
                                          					 that is used to make digital data calls involving imaging or high speed circuit
                                          					 switched data in general.

20x

DEVC_DATA

A device
                                          					 that is used to make digital data calls (both circuit switched and packet
                                          					 switched).

40x

DEVC_VOICE

A device
                                          					 that is used to make audio calls.

80x

## CallPlacementType
                        	 Values

This
                              		  table shows the CallPlacementType values.

CallPlacementType

Description

Value

CPT_UNSPECIFIED

Use
                                          					 default call placement.

0

CPT_LINE_CALL

An inside
                                          					 line call.

1

CPT_OUTBOUND

An
                                          					 outbound call.

2

CPT_OUTBOUND_NO_ ACCESS_CODE

An
                                          					 outbound call that will not require an access code.

3

CPT_DIRECT_POSITION

A call
                                          					 placed directly to a specific position.

4

CPT_DIRECT_AGENT

A call
                                          					 placed directly to a specific agent.

5

CPT_SUPERVISOR_ASSIST

A call
                                          					 placed to a supervisor for call handling assistance.

6

## CallMannerType
                        	 Values

This
                              		  table shows the CallMannerType values.

CallMannerType

Description

Value

CMT_UNSPECIFIED

Use
                                          					 default call manner.

0

CMT_POLITE

Attempt
                                          					 the call only if the originating device is idle.

1

CMT_BELLIGERENT

2

CMT_SEMI_POLITE

Attempt
                                          					 the call only if the originating device is idle or is receiving dial tone.

3

CMT_RESERVED

Reserved

4

## CallOption
                        	 Values

This
                              		  table shows the CallOption values.

CallOption

Description

Value

COPT_UNSPECIFIED

No call
                                          					 options specified, use defaults.

0

COPT_CALLING_ AGENT_ONLINE

Attempt
                                          					 the call only if the calling agent is “online” (available to interact with the
                                          					 destination party).

1

COPT_CALLING_ AGENT_RESERVED

Obsolete
                                          					 with DMS-100.

2

COPT_CALLING_ AGENT_NOT_ RESERVED

Obsolete
                                          					 with DMS-100.

3

COPT_CALLING_ AGENT_BUZZ_BASE

Obsolete
                                          					 with DMS-100.

4

COPT_CALLING_ AGENT_BEEP_HSET

Obsolete
                                          					 with DMS-100.

5

COPT_SERVICE_ CIRCUIT_ON

Causes a
                                          					 call classifier to be applied to the call (ACM ECS).

6

## ConsultType
                        	 Values

This
                              		  table shows the ConsultType values.

ConsultType

Description

Value

CT_UNSPECIFIED

Default
                                          					 (consult call).

0

CT_TRANSFER

Consult
                                          					 call prior to transfer.

1

CT_CONFERENCE

Consult
                                          					 call prior to conference.

2

## FacilityType
                        	 Values

This
                              		  table shows the FacilityType values.

FacilityType

Description

Value

FT_UNSPECIFIED

Use
                                          					 default facility type.

0

FT_TRUNK_GROUP

Facility
                                          					 is a trunk group.

1

FT_SKILL_GROUP

Facility
                                          					 is a skill group or split.

2

## AnsweringMachine
                        	 Values

This
                              		  table shows the AnsweringMachine values.

AnsweringMachine

Description

Value

AM_UNSPECIFIED

Use
                                          					 default behavior.

0

AM_CONNECT

Connect
                                          					 call to agent when call is answered by an answering machine.

1

AM_DISCONNECT

Disconnect
                                          					 call when call is answered by an answering machine.

2

AM_NONE

Do not use
                                          					 answering machine detection.

3

AM_NONE_NO_ MODEM

Do not use
                                          					 answering machine detection, but disconnect call if answered by a modem.

4

AM_CONNECT_NO_MODEM

Connect
                                          					 call when call is answered by an answering machine, disconnect call if answered
                                          					 by a modem.

5

## AnswerDetectMode
                        	 Values

This
                              		  table shows the AnswerDetectMode values.

AnswerDetectMode

Description

Value

ADM_UNSPECIFIED

Use
                                          					 default behavior.

0

ADM_VOICE_
                                          					 THRESHOLD

Report
                                          					 call answered by an answering machine when initial voice duration exceeds time
                                          					 threshold.

1

ADM_VOICE_END

Report
                                          					 call answered by an answering machine when initial voice segment ends.

2

ADM_VOICE_END_ DELAY

Report
                                          					 call answered by an answering machine after a fixed delay following the end of
                                          					 the initial voice segment.

3

ADM_VOICE_AND_ BEEP

Report
                                          					 call answered by an answering machine after a beep tone following the end of
                                          					 the initial voice segment (excluding beep tone without any preceding voice).

4

ADM_BEEP

Report
                                          					 call answered by an answering machine after a beep tone following the end of
                                          					 the initial voice segment (including beep tone without any preceding voice).

5

## AgentWorkMode
                        	 Values

This
                              		  table shows the AgentWorkMode values.

AgentWorkMode

Description

Value

AWM_UNSPECIFIED

Use
                                          					 default behavior.

0

AWM_AUTO_IN

Agent
                                          					 automatically becomes available after handling a call.

1

AWM_MANUAL_IN

Agent must
                                          					 explicitly indicate availability after handling a call.

2

RA_CALL_BY_CALL

Remote
                                          					 agent Call by Call mode.

3

RA_NAILED_
                                          					 CONNECTION

Remote
                                          					 agent NailedUp mode.

4

## DestinationCountry
                        	 Values

This
                              		  table shows the DestinationCountry values.

DestinationCountry

Description

Value

DEST_UNSPECIFIED

Unspecified or unknown, use default behavior.

0

DEST_US_AND_ CANADA

Call
                                          					 destination is in the United States or Canada.

1

## CTI Service
                        	 Masks

This
                              		  table shows the CTIService masks.

MaskName

Description

Value

CTI_SERVICE_ DEBUG

Causes all
                                          					 messages exchanged during the current session to be captured to a file for
                                          					 later analysis.

0x80000000

CTI_SERVICE_ CLIENT_ EVENTS

Client
                                          					 receives call and agent state change events associated with a specific ACD
                                          					 phone.

0x00000001

CTI_SERVICE_CALL_ DATA_UPDATE

Client may
                                          					 modify call context data.

0x00000002

CTI_SERVICE_ CLIENT_CONTROL

Client may
                                          					 control calls and agent states associated with a specific ACD phone.

0x00000004

CTI_SERVICE_ CONNECTION_ MONITOR

Establishment and termination of this session cause
                                          					 corresponding Unified CCE Alarm events to be generated.

0x00000008

CTI_SERVICE_ALL_ EVENTS

Client
                                          					 receives all call and agent state change events (associated with any ACD
                                          					 phone).

0x00000010

CTI_SERVICE_ PERIPHERAL_ MONITOR

Client may
                                          					 dynamically add and remove devices and/or calls that it wishes to receive call
                                          					 and agent state events for.

0x00000020

CTI_SERVICE_ CLIENT_MONITOR

Client
                                          					 receives notification when all other CTI client sessions are opened and closed,
                                          					 and may monitor the activity of other CTI client sessions.

0x00000040

CTI_SERVICE_ SUPERVISOR

Client may
                                          					 request supervisor services.

0x00000080

CTI_SERVICE_ SERVER

Client
                                          					 identify itself as server application.

0x00000100

CTI_SERVICE_ AGENT_REPORTING

Client may
                                          					 reporting/routing ARM(Agent Reporting And Management) messages.

0x00000400

CTI_SERVICE_ALL_ TASK_EVENTS

Client
                                          					 receives all task events.

0x00000800

CTI_SERVICE_ TASK_MONITOR

Client
                                          					 receives monitored task events.

0x00001000

CTI_AGENT_STATE_CONTROL_ONLY

Client can
                                          					 change agent state only. Call control is not allowed. If a client requests for
                                          					 CTI_SERVICE_ CLIENT_CONTROL, the server may grant this flag to indicate that
                                          					 only agent state change is allowed.

0x00002000

Unused

0x00004000

CTI_DEVICE_STATE_CONTROL

The
                                          					 client/server wishes to register and get resource state change requests.

0x00008000

CTI_SERVICE_ UPDATE_EVENTS

Requests
                                          					 that this client receive update notification events. (No data)

0x00080000

CTI_SERVICE_ IGNORE_ DUPLICATE_ AGENT_EVENTS

Request to
                                          					 suppress duplicate agent state events.

0x00100000

CTI_SERVICE_ IGNORE_CONF

Do not
                                          					 send confirmations for third party requests.

0x00200000

CTI_SERVICE_ACD_ LINE_ONLY

Request
                                          					 that events for non-ACD lines not be sent. (Unified CCE only)

0x00400000

## Disposition Code
                        	 Values

This
                              		  table shows the Disposition Code values.

Disposition Code

Meaning

1

Abandoned
                                          					 in Network

2

Abandoned
                                          					 in Local Queue

3

Abandoned
                                          					 Ring

4

Abandoned
                                          					 Delay

5

Abandoned
                                          					 Interflow

6

Abandoned
                                          					 Agent Terminal

7

Short

8

Busy

9

Forced
                                          					 Busy

10

Disconnect/drop no answer

11

Disconnect/drop busy

12

Disconnect/drop reorder

13

Disconnect/drop handled primary route

14

Disconnect/drop handled other

15

Redirected

16

Cut
                                          					 Through

17

Intraflow

18

Interflow

19

Ring No
                                          					 Answer

20

Intercept
                                          					 reorder

21

Intercept
                                          					 denial

22

Time Out

23

Voice
                                          					 Energy

24

Non-classified Energy Detected

25

No Cut
                                          					 Through

26

U-Abort

27

Failed
                                          					 Software

28

Blind
                                          					 Transfer

29

Announced
                                          					 Transfer

30

Conferenced

31

Duplicate Transfer

32

Unmonitored Device

33

Answering Machine

34

Network
                                          					 Blind Transfer

35

Task
                                          					 Abandoned in Router

36

Task
                                          					 Abandoned Before Offered

37

Task
                                          					 Abandoned While Offered

38

Normal
                                          					 End Task

39

Can't
                                          					 Obtain Task ID

40

Agent
                                          					 Logged Out During Task

41

Maximum
                                          					 Task Lifetime Exceeded

42

Application Path Went Down

43

Unified
                                          					 CCE Routing Complete

44

Unified
                                          					 CCE Routing Disabled

45

Application Invalid MRD ID

46

Application Invalid Dialogue ID

47

Application Duplicate Dialogue ID

48

Application Invalid Invoke ID

49

Application Invalid Script Selector

50

Application Terminate Dialogue

51

Task
                                          					 Ended During Application Init

52

Called
                                          					 Party Disconnected

53

Partial
                                          					 Call

54

Drop
                                          					 Network Consult

55

Network
                                          					 Consult Transfer

57

Abandon
                                          					 Network Consult

58

Router
                                          					 Requery Before Answer

59

Router
                                          					 Requery After Answer

60

Network
                                          					 Error

61

Network
                                          					 Error Before Answer

62

Network
                                          					 Error After Answer

63

Task
                                          					 Transfer

64

Application Disconnected

65

Task
                                          					 Transferred on Agent Logout

## Agent Service
                        	 Request Masks

This
                              		  table shows the Agent Service Request masks.

DestinationCountry

Description

Value

OUTBOUND_SUPPORT

The agent
                                          					 login can support outbound feature.

0x1

## Silent Monitor
                        	 Status Values

This
                              		  table shows the Silent Monitor Status Values.

DestinationCountry

Description

Value

SILENT_MONITOR_ NONE

Normal
                                          					 call (non-silent monitor call).

0

SILENT_MONITOR_ INITIATOR

Initiator
                                          					 of silent monitor call.

1

SILENT_MONITOR_ TARGET

Monitor
                                          					 target of silent monitor call.

2

## Agent Internal
                        	 States Message Values

This
                              		  table shows the Agent’s Internal States and their Message Values.

State Name

Description

Value

AGENT_STATE_LOGIN

The agent
                                          					 has logged on to the ACD. It does not necessarily indicate that the agent is
                                          					 ready to accept calls.

0

AGENT_STATE_LOGOUT

The agent
                                          					 has logged out of the ACD and cannot accept any additional calls.

1

AGENT_STATE_NOT_READY

The agent
                                          					 is unavailable for any call work.

2

AGENT_STATE_AVAILABLE

The agent
                                          					 is ready to accept a call.

3

AGENT_STATE_TALKING

The agent
                                          					 is currently talking on a call (inbound, outbound, or inside).

4

AGENT_STATE_WORK_NOT_READY

The agent
                                          					 is performing after call work, but will not be ready to receive a call when
                                          					 completed.

5

AGENT_STATE_WORK_READY

The agent
                                          					 is performing after call work, but will be ready to receive a call when
                                          					 completed.

6

AGENT_STATE_BUSY_OTHER

The agent
                                          					 is busy performing a task associated with another active SkillGroup.

7

AGENT_STATE_ACTIVE

The agent
                                          					 state is currently active.

11

## TaskState
                        	 Values

This
                              		  table shows the TaskState values that may appear in SNAPSHOT_TASK_RESP
                              		  messages.

State Name

Description

Value

TASK_STATE_PRE_CALL

Pre Call
                                          					 Message has been sent to client.

0

TASK_STATE_ACTIVE

Task is
                                          					 actively being worked on; Start Task has been received for this task.

1

TASK_STATE_WRAPUP

Wrap up
                                          					 task has been received for this task.

2

TASK_STATE_PAUSED

Task is
                                          					 paused; Pause Task has been received for this task.

3

TASK_STATE_OFFERED

Offer Task
                                          					 has been received for this task.

4

ASK_STATE_INTERRUPTED

Task is
                                          					 interrupted; Agent Interrupt Accepted Ind is received.

5

TASK_STATE_NOT_READY

Not used.

6

TASK_STATE_LOGGED_OUT

Task is
                                          					 terminated.

7

## In this chapter

This section lists the possible values for various status codes
                           and fields that can appear in CTI Server messages. These values are defined
                           in the CTILink.h file, located in the \icm\include directory.

## Failure Indication
                        	 Message Status Codes

This
                              		  table shows the status codes that may be included in the FAILURE_CONF and
                              		  FAILURE_EVENT messages.

Status Codes

Status Code

Description

Value

E_CTI_NO_ERROR

No error occurred.

0

E_CTI_INVALID_ VERSION

The CTI Server does not support the protocol version number requested by the CTI client.

1

E_CTI_INVALID_MESSAGE_LENGTH

A message with an invalid message length field was received.

2

E_CTI_INVALID_ FIELD_TAG

A message with an invalid floating field tag was received.

3

E_CTI_SESSION_ NOT_OPEN

No session is currently open on the connection.

4

E_CTI_SESSION_ ALREADY_ OPEN

A session is already open on the connection.

5

E_CTI_REQUIRED_ DATA_ MISSING

The request did not include one or more floating items that are required.

6

E_CTI_INVALID_ PERIPHERAL_ID

A message with an invalid PeripheralID value was received.

7

E_CTI_INVALID_ AGENT_ DATA

The provided agent data item(s) are invalid.

8

E_CTI_AGENT_NOT_ LOGGED_ON

The indicated agent is not currently logged on.

9

E_CTI_DEVICE_IN_ USE

The indicated agent teleset is already associated with a different CTI client.

10

E_CTI_NEW_ SESSION_ OPENED

This session is being terminated due to a new session open request from the client.

11

E_CTI_FUNCTION_ NOT_ AVAILABLE

A request message was received for a function or service that was not granted to the client.

12

E_CTI_INVALID_ CALLID

A request message was received with an invalid CallID value.

13

E_CTI_PROTECTED_ VARIABLE

The CTI client may not update the requested variable.

14

E_CTI_CTI_SERVER_ OFFLINE

The CTI Server is not able to function normally. The CTI client should close the session upon receipt of this error.

If a client using a CTI protocol version less than 24 tries to connect to a standby CTI Server, the client does not support
                                          active-standby functionality and will instead connect to the active side.

15

E_CTI_TIMEOUT

The CTI Server failed to respond to a request message within the time-out period, or no messages have been received from the
                                          CTI client within the IdleTimeout period.

16

E_CTI_UNSPECIFIED_FAILURE

An unspecified error occurred.

17

E_CTI_INVALID_ TIMEOUT

The IdleTimeout field contains a value that is less than 20 seconds (4 times the minimum heartbeat interval of 5 seconds).

18

E_CTI_INVALID_ SERVICE_MASK

The ServicesRequested field has unused bits set. All unused bit positions must be zero.

19

E_CTI_INVALID_ CALL_MSG_MASK

The CallMsgMask field has unused bits set. All unused bit positions must be zero.

20

E_CTI_INVALID_ AGENT_ STATE_ MASK

The AgentStateMask field has unused bits set. All unused bit positions must be zero.

21

E_CTI_INVALID_ RESERVED_ FIELD

A Reserved field has a non-zero value.

22

E_CTI_INVALID_ FIELD_ LENGTH

A floating field exceeds the allowable length for that field type.

23

E_CTI_INVALID_ DIGITS

A STRING field contains characters that are not digits (“0” through “9”).

24

E_CTI_BAD_ MESSAGE_ FORMAT

The message is improperly constructed. This may be caused by omitted or incorrectly sized fixed message fields.

25

E_CTI_INVALID_ TAG_FOR_MSG_ TYPE

A floating field tag is present that specifies a field that does not belong in this message type.

26

E_CTI_INVALID_ DEVICE_ID_ TYPE

A DeviceIDType field contains a value that is not in DeviceIDType Values .

27

E_CTI_INVALID_ LCL_CONN_ STATE

A LocalConnectionState field contains a value that is not in LocalConnectionState Values .

28

E_CTI_INVALID_ EVENT_ CAUSE

An EventCause field contains a value that is not in EventCause Values .

29

E_CTI_INVALID_ NUM_ PARTIES

The NumParties field contains a value that exceeds the maximum (16).

30

E_CTI_INVALID_ SYS_ EVENT_ID

The SystemEventID field contains a value that is not in SystemEventID Values .

31

E_CTI_ INCONSISTENT_ AGENT_DATA

The provided agent extension, agent id, and/or agent instrument values are inconsistent with each other.

32

E_CTI_INVALID_ CONNECTION_ID_ TYPE

A ConnectionDeviceIDType field contains a value that is not in ConnectionDeviceIDType Values .

33

E_CTI_INVALID_ CALL_TYPE

The CallType field contains a value that is not in CallType Values .

34

E_CTI_NOT_CALL_ PARTY

A CallDataUpdate or Release Call request specified a call that the client is not a party to.

35

E_CTI_INVALID_ PASSWORD

The ClientID and Client Password provided in an OPEN_REQ message is incorrect.

36

E_CTI_CLIENT_ DISCONNECTED

The client TCP/IP connection was disconnected without a CLOSE_REQ.

37

E_CTI_INVALID_ OBJECT_ STATE

An invalid object state value was provided.

38

E_CTI_INVALID_ NUM_ SKILL_GROUPS

An invalid NumSkillGroups value was provided.

39

E_CTI_INVALID_ NUM_LINES

An invalid NumLines value was provided.

40

E_CTI_INVALID_ LINE_TYPE

An invalid LineType value was provided.

41

E_CTI_INVALID_ ALLOCATION_STATE

An invalid AllocationState value was provided.

42

E_CTI_INVALID_ ANSWERING_ MACHINE

An invalid AnsweringMachine value was provided.

43

E_CTI_INVALID_ CALL_MANNER_ TYPE

An invalid CallMannerType value was provided.

44

E_CTI_INVALID_ CALL_PLACEMENT_ TYPE

An invalid CallPlacementType value was provided.

45

E_CTI_INVALID_ CONSULT_ TYPE

An invalid ConsultType value was provided.

46

E_CTI_INVALID_ FACILITY_ TYPE

An invalid FacilityType value was provided.

47

E_CTI_INVALID_ MSG_TYPE_ FOR_ VERSION

The provided MessageType is invalid for the opened protocol version.

48

E_CTI_INVALID_ TAG_FOR_ VERSION

A floating field tag value is invalid for the opened protocol version.

49

E_CTI_INVALID_ AGENT_WORK_ MODE

An invalid AgentWorkMode value was provided.

50

E_CTI_INVALID_ CALL_OPTION

An invalid call option value was provided.

51

E_CTI_INVALID_ DESTINATION_ COUNTRY

An invalid destination country value was provided.

52

E_CTI_INVALID_ ANSWER_DETECT_ MODE

An invalid answer detect mode value was provided.

53

E_CTI_MUTUALLY_ EXCLUS_DEVICEID_ TYPES

A peripheral monitor request may not specify both a call and a device.

54

E_CTI_INVALID_ MONITORID

An invalid monitorID value was provided.

55

E_CTI_SESSION_ MONITOR_ ALREADY_EXISTS

A requested session monitor was already created.

56

E_CTI_SESSION_ MONITOR_IS_ CLIENTS

A client may not monitor its own session.

57

E_CTI_INVALID_ CALL_CONTROL_ MASK

An invalid call control mask value was provided.

58

E_CTI_INVALID_ FEATURE_MASK

An invalid feature mask value was provided.

59

E_CTI_INVALID_ TRANSFER_ CONFERENCE_ SETUP_MASK

An invalid transfer conference setup mask value was provided.

60

E_CTI_INVALID_ ARRAY_INDEX

An invalid named array index value was provided.

61

E_CTI_INVALID_ CHARACTER

An invalid character value was provided.

62

E_CTI_CLIENT_NOT_FOUND

There is no open session with a matching ClientID.

63

E_CTI_SUPERVISOR_NOT_FOUND

The agent’s supervisor is unknown or does not have an open CTI session.

64

E_CTI_TEAM_NOT_ FOUND

The agent is not a member of an agent team.

65

E_CTI_NO_CALL_ ACTIVE

The specified agent does not have an active call.

66

E_CTI_NAMED_ VARIABLE_NOT_ CONFIGURED

The specified named variable is not configured in the Unified CCE.

67

E_CTI_NAMED_ ARRAY_NOT_ CONFIGURED

The specified named array is not configured in the Unified CCE.

68

E_CTI_INVALID_ CALL_VARIABLE_ MASK

The specified call variable mask in not valid.

69

E_CTI_ELEMENT_ NOT_FOUND

An internal error occurred manipulating a named variable or named array element.

70

E_CTI_INVALID_ DISTRIBUTION_TYPE

The specified distribution type is invalid.

71

E_CTI_INVALID_ SKILL_GROUP

The specified skill group is invalid.

72

E_CTI_TOO_MUCH_ DATA

The total combined size of named variables and named arrays may not exceed the limit of 2000 bytes.

73

E_CTI_VALUE_TOO_LONG

The value of the specified named variable or named array element exceeds the maximum permissible length.

74

E_CTI_SCALAR_ FUNCTION_ON_ ARRAY

A NamedArray was specified with a NamedVariable tag.

75

E_CTI_ARRAY_ FUNCTION_ON_ SCALAR

A NamedVariable was specified with a NamedArray tag.

76

E_CTI_INVALID_ NUM_NAMED_ VARIABLES

The value in the NumNamedVariables field is different than the number of NamedVariable floating fields in the message.

77

E_CTI_INVALID_ NUM_NAMED_ ARRAYS

The value in the NumNamedArrays field is different than the number of NamedArray floating fields in the message.

78

E_CTI_INVALID_RTP_DIRECTION

The RTP direction value is invalid.

79

E_CTI_INVALID_RTP_TYPE

The RTP type value is invalid.

80

E_CTI_CALLED_ PARTY_DISPOSITION

The called party disposition is invalid.

81

E_CTI_INVALID_ SUPERVISORY_ ACTION

The supervisory action is invalid.

82

E_CTI_AGENT_ TEAM_MONITOR_ ALREADY_EXISTS

The agent team monitor already exists.

83

E_CTI_INVALID_ SERVICE

The ServiceNumber or ServiceID value is invalid.

84

E_CTI_SERVICE_ CONFLICT

The ServiceNumber and ServiceID values given represent different services.

85

E_CTI_SKILL_ GROUP_CONFLICT

The SkillGroupNumber/SkillGroupPriority and SkillGroupID values given represent different skill groups.

86

E_CTI_INVALID_ DEVICE

The specified device is invalid.

87

E_CTI_INVALID_MR_DOMAIN

Media Routing Domain is invalid.

88

E_CTI_MONITOR_ ALREADY_EXISTS

Monitor already exists.

89

E_CTI_MONITOR_ TERMINATED

Monitor has terminated.

90

E_CTI_INVALID_ TASK_MSG_MASK

The task msg mask is invalid.

91

E_CTI_SERVER_NOT_MASTER

The server is a standby server.

92

E_CTI_INVALID_CSD

The CSD Specified is invalid (Unified CCX Only).

93

E_CTI_JTAPI_CCM_ PROBLEM

Indicates a JTAPI or Unified CM problem.

94

E_INVALID_CONFIG_ MSG_MASK

Indicates a bad config mask in OPEN_REQ.

95

E_CTI_AUTO_ CONFIG_RESET

Indicates a configuration change (Unified CCX only).

96

E_CTI_INVALID_ MONITOR_STATUS

Indicates an invalid monitor.

97

E_CTI_INVALID_ REQUEST_TYPE

Indicates an invalid request ID type.

98

E_CTI_INVALID_CLIENT_ FOR_STANDBY

Standby CTIServer returns this error code when:

The clients without ServiceMask CTI_SERVICE_ACTIVE_STANDBY (0x02000000) connects.

107

E_CTI_INVALID_UNIQUE_ INSTANCE_ID

This status code is returned as a failure response for the OPEN_REQ message when the UniqueInstanceID element is present in
                                          the message but its value is empty (0 length).

108

E_CTI_DUPLICATE_UNIQUE_ INSTANCE_ID

This status code is returned as a failure response for the OPEN_REQ message when there is an existing Client Instance found
                                          with same UniqueInstanceID in the OPEN_REQ message.

109

E_CTI_SERVER_IN_ MAINTENANCE_MODE

This status code is returned as a failure response for the OPEN_REQ message a client is trying to open a session with CTI
                                          Server when Maintenance Mode is in progress.

The code is used to close the client session when the active CTI Server stops for Maintenance Mode.

110

## SystemEventID
                        	 Values

This
                              		  table shows the SystemEventID values that may be included in the SYSTEM_EVENT
                              		  messages.

SystemEventID

Description

Value

SYS_CENTRAL_ CONTROLLER_ONLINE

The PG has
                                          					 resumed communication with the Unified CCE Central Controller.

1

SYS_CENTRAL_ CONTROLLER_OFFLINE

The PG is
                                          					 unable to communicate with the Unified CCE Central Controller.

2

SYS_PERIPHERAL_ ONLINE

A
                                          					 peripheral monitored by the PG has gone online. SystemEventArg1 contains the
                                          					 PeripheralID of the peripheral.

3

SYS_PERIPHERAL_ OFFLINE

A
                                          					 peripheral monitored by the PG has gone offline. SystemEventArg1 contains the
                                          					 PeripheralID of the peripheral.

4

SYS_TEXT_FYI

Broadcast
                                          					 of informational “text” floating field.

5

SYS_PERIPHERAL_ GATEWAY_OFFLINE

The CTI
                                          					 Server is unable to communicate with the Unified CCE Peripheral Gateway.

6

SYS_CTI_SERVER_ OFFLINE

The local
                                          					 software component is unable to communicate with the CTI Server.

7

SYS_CTI_SERVER_ ONLINE

The local
                                          					 software component has resumed communication with the CTI Server.

8

SYS_HALF_HOUR_ CHANGE

The
                                          					 Unified CCE Central Controller time has changed to a new half hour.

9

SYS_INSTRUMENT_ OUT_OF_SERVICE

An
                                          					 Enterprise Agent device target has been removed from service. SystemEventArg1
                                          					 contains the PeripheralID of the peripheral, and SystemEventText contains the
                                          					 AgentInstrument that was removed from service.

10

SYS_INSTRUMENT_ BACK_IN_SERVICE

An
                                          					 Enterprise Agent device target has been returned to service. SystemEventArg1
                                          					 contains the PeripheralID of the peripheral, and SystemEventText contains the
                                          					 AgentInstrument that was returned to service.

11

## Special
                        	 Values

This table shows
                              		  the values used to define sizes and limits, indicate special IDs, and
                              		  unspecified data elements.

Constant

Description

Value

MAX_NUM_CTI_ CLIENTS

The
                                          					 maximum number of CTI clients that can be in a message list.

16

MAX_NUM_
                                          					 PARTIES

The
                                          					 maximum number of conference call parties that can be in a message list.

16

MAX_NUM_
                                          					 DEVICES

The
                                          					 maximum number of call devices that can be in a message list.

16

MAX_NUM_
                                          					 CALLS

The
                                          					 maximum number of calls that can be in a message list.

16

MAX_NUM_
                                          					 SKILL_GROUPS

The
                                          					 maximum number of skill group fields that can be in a message list.

20

MAX_NUM_LINES

The
                                          					 maximum number of teleset line fields that can be in a message list.

10

NULL_
                                          					 CALL_ID

No call ID
                                          					 is supplied.

0xFFFFFFFF

NULL_
                                          					 PERIPHERAL_ID

No
                                          					 peripheral ID is supplied.

0xFFFFFFFF

NULL_SERVICE

No service
                                          					 is supplied.

0xFFFFFFFF

NULL_SKILL_ GROUP

No skill
                                          					 group is supplied.

0xFFFFFFFF

NULL_CALLTYPE

Indicates
                                          					 that no CallType is supplied.

0xFFFF

## Tag Values

This
                              		  table shows the values used in the tag subfield of floating fields.

Floating
                                          					 Field Tag

Using
                                          					 Messages

Value

CLIENT_ID_TAG

OPEN_REQ

1

CLIENT_PASSWORD_ TAG

OPEN_REQ

2

CLIENT_SIGNATURE_ TAG

OPEN_REQ,
                                          					 AGENT_STATE_EVENT

3

AGENT_EXTENSION_ TAG

OPEN_REQ,
                                          					 OPEN_CONF, AGENT_STATE_EVENT

4

AGENT_ID_TAG

OPEN_REQ,
                                          					 OPEN_CONF, AGENT_STATE_EVENT, SET_AGENT_STATE_EVENT

5

AGENT_
                                          					 INSTRUMENT_ TAG

OPEN_REQ,
                                          					 OPEN_CONF, AGENT_STATE_EVENT, QUERY_AGENT_STATE_REQ, SET_AGENT_STATE_REQ,
                                          					 MAKE_CALL_REQ

6

TEXT_TAG

SYSTEM_EVENT, CLIENT_EVENT_REPORT_REQ, AGENT_TASKS_END_EVENT

7

ANI_TAG

BEGIN_CALL_EVENT, CALL_ DATA_UPDATE_EVENT, CALL_
                                          					 TRANSLATION_ROUTE_EVENT, SNAPSHOT_CALL_ CONF

8

UUI_TAG

BEGIN_CALL_EVENT, CALL_DATA_UPDATE_EVENT,
                                          					 CALL_TRANSLATION_ROUTE_ EVENT, CONSULTATION_ CALL_REQ, MAKE_CALL_REQ,
                                          					 TRANSFER_CALL_REQ, SNAPSHOT_CALL_CONF

9

DNIS_TAG

BEGIN_CALL_EVENT, CALL_ DATA_UPDATE_EVENT, CALL_
                                          					 TRANSLATION_ROUTE_ EVENT, SNAPSHOT_CALL_ CONF

10

DIALED_NUMBER_ TAG

BEGIN_CALL_EVENT, CALL_DATA_UPDATE_EVENT,
                                          					 CALL_TRANSLATION_ROUTE_ EVENT, CONSULTATION_ CALL_ REQ, MAKE_CALL_REQ,
                                          					 TRANSFER_CALL_REQ, SNAPSHOT_CALL_CONF

11

CED_TAG

BEGIN_CALL_EVENT, CALL_ DATA_UPDATE_EVENT, CALL_
                                          					 TRANSLATION_ROUTE_ EVENT, SNAPSHOT_CALL_ CONF

12

CALL_VAR_1_TAG through CALL_VAR_10_TAG

BEGIN_CALL_EVENT, CALL_DATA_UPDATE_EVENT, CALL_TRANSLATION_ROUTE_ EVENT, CONSULTATION_ CALL_REQ, MAKE_CALL_REQ, TRANSFER_CALL_REQ,
                                          SNAPSHOT_CALL_CONF, SNAPSHOT_TASK_RESP , SNAPSHOT_TASK_EVENT

13-22

CTI_CLIENT_ SIGNATURE_TAG

BEGIN_CALL_EVENT, CALL_DATA_UPDATE_EVENT, SNAPSHOT_CALL_CONF

23

CTI_CLIENT_ TIMESTAMP_TAG

BEGIN_CALL_EVENT, CALL_DATA_UPDATE_EVENT, SNAPSHOT_CALL_CONF

24

CONNECTION_ DEVID_ TAG

Any CALL
                                          					 EVENT message, most CLIENT CONTROL messages.

25

ALERTING_DEVID_ TAG

CALL_DELIVERED_EVENT

26

CALLING_DEVID_TAG

CALL_DELIVERED_EVENT, CALL_ESTABLISHED_EVENT,
                                          					 CALL_ORIGINATED_EVENT, CALL_SERVICE_INITIATED_EVENT, CALL_QUEUED_EVENT,
                                          					 SET_DEVICE_ATTRIBUTES_REQ

27

CALLED_DEVID_TAG

CALL_DELIVERED_EVENT, CALL_ESTABLISHED_EVENT,
                                          					 CALL_ORIGINATED_EVENT, CALL_QUEUED_EVENT,

28

LAST_REDIRECT_ DEVID_TAG

CALL_DELIVERED_EVENT, CALL_ESTABLISHED_EVENT, CALL_QUEUED_EVENT

29

ANSWERING_DEVID_ TAG

CALL_ESTABLISHED_EVENT

30

HOLDING_DEVID_ TAG

CALL_HELD_EVENT

31

RETRIEVING_DEVID_ TAG

CALL_RETRIEVED_EVENT

32

RELEASING_DEVID_ TAG

CALL_CONNECTION_ CLEARED_EVENT

33

FAILING_DEVID_TAG

CALL_FAILED_EVENT

34

PRIMARY_DEVID_ TAG

CALL_CONFERENCED_EVENT, CALL_TRANSFERRED_EVENT

35

SECONDARY_DEVID_ TAG

CALL_CONFERENCED_EVENT, CALL_TRANSFERRED_EVENT

36

CONTROLLER_ DEVID_ TAG

CALL_CONFERENCED_EVENT

37

ADDED_PARTY_ DEVID_TAG

CALL_CONFERENCED_EVENT

38

PARTY_CALLID_TAG

CALL_CONFERENCED_EVENT, CALL_TRANSFERRED_EVENT,
                                          					 CONFERENCE_CALL_CONF, TRANSFER_CALL_CONF

39

PARTY_DEVID_TYPE_ TAG

CALL_CONFERENCED_EVENT, CALL_TRANSFERRED_EVENT,
                                          					 CONFERENCE_CALL_CONF, TRANSFER_CALL_CONF

40

PARTY_DEVID_TAG

CALL_CONFERENCED_EVENT, CALL_TRANSFERRED_EVENT,
                                          					 CONFERENCE_CALL_CONF, TRANSFER_CALL_CONF

41

TRANSFERRING_ DEVID_TAG

CALL_TRANSFERRED_EVENT

42

TRANSFERRED_ DEVID_TAG

CALL_TRANSFERRED_EVENT

43

DIVERTING_DEVID_ TAG

CALL_DIVERTED_EVENT

44

QUEUE_DEVID_TAG

CALL_QUEUED_EVENT

45

CALL_WRAPUP_ DATA_ TAG

BEGIN_CALL_EVENT, CALL_DATA_UPDATE_EVENT, SET_CALL_DATA_REQ,
                                          					 CONSULTATION_CALL_REQ, MAKE_CALL_REQ, TRANSFER_CALL_REQ, SNAPSHOT_CALL_CONF

46

NEW_CONNECTION_ DEVID_TAG

CALL_DATA_UPDATE_EVENT, CONFERENCE_CALL_CONF,
                                          					 CONSULTATION_CALL_CONF, MAKE_CALL_CONF, TRANSFER_CALL_CONF

47

TRUNK_USED_ DEVID_ TAG

CALL_REACHED_NETWORK_ EVENT

48

AGENT_PASSWORD_ TAG

SET_AGENT_STATE_REQ

49

ACTIVE_CONN_ DEVID_ TAG

ALTERNATE_CALL_REQ, CONFERENCE_CALL_REQ, CONSULTATION_CALL_REQ,
                                          					 RECONNECT_CALL_REQ, TRANSFER_CALL_REQ

50

FACILITY_CODE_TAG

CONSULTATION_CALL_REQ, MAKE_CALL_REQ, TRANSFER_CALL_REQ

51

OTHER_CONN_ DEVID_ TAG

ALTERNATE_CALL_REQ

52

HELD_CONN_DEVID_ TAG

CONFERENCE_CALL_REQ, RECONNECT_CALL_REQ, RETRIEVE_CALL_REQ,
                                          					 TRANSFER_CALL_REQ

53

(reserved)

54-55

CALL_CONN_ CALLID_ TAG

SNAPSHOT_CALL_CONF, SNAPSHOT_DEVICE_CONF

56

CALL_CONN_DEVID_ TYPE_TAG

SNAPSHOT_CALL_CONF, SNAPSHOT_DEVICE_CONF

57

CALL_CONN_DEVID_ TAG

SNAPSHOT_CALL_CONF, SNAPSHOT_DEVICE_CONF

58

CALL_DEVID_TYPE_ TAG

SNAPSHOT_CALL_CONF

59

CALL_DEVID_TAG

SNAPSHOT_CALL_CONF

60

CALL_DEV_CONN_ STATE_TAG

SNAPSHOT_CALL_CONF

61

SKILL_GROUP_ NUMBER_TAG

CALL_QUEUED_EVENT, CALL_DEQUEUED_EVENT, QUERY_AGENT_STATE_CONF

62

SKILL_GROUP_ID_ TAG

CALL_QUEUED_EVENT, CALL_DEQUEUED_EVENT, QUERY_AGENT_STATE_CONF

63

SKILL_GROUP_ PRIORITY_TAG

CALL_QUEUED_EVENT, CALL_DEQUEUED_EVENT, QUERY_AGENT_STATE_CONF

64

SKILL_GROUP_ STATE_ TAG

QUERY_AGENT_STATE_CONF

65

OBJECT_NAME_TAG

CLIENT_EVENT_REPORT

66

DTMF_STRING_TAG

SEND_DTMF_SIGNAL_REQ

67

POSITION_ID_TAG

SET_AGENT_STATE_REQ

68

SUPERVISOR_ID_TAG

SET_AGENT_STATE_REQ

69

LINE_HANDLE_TAG

QUERY_DEVICE_INFO_CONF

70

LINE_TYPE_TAG

QUERY_DEVICE_INFO_CONF

71

ROUTER_CALL_KEY_ DAY_TAG

BEGIN_CALL_EVENT, CALL_ DATA_UPDATE_EVENT, CALL_
                                          					 TRANSLATION_ROUTE_EVENT, SNAPSHOT_CALL_ CONF

72

ROUTER_CALL_KEY_ CALLID_TAG

BEGIN_CALL_EVENT, CALL_ DATA_UPDATE_EVENT, CALL_
                                          					 TRANSLATION_ROUTE_EVENT, SNAPSHOT_CALL_ CONF

73

ROUTER_CALL_KEY_SEQUENCE_NUM_TAG

AGENT_LEGACY_PRE_CALL_EVENT, BEGIN_CALL_EVENT,
                                          					 CALL_DATA_UPDATE_EVENT, CALL_TRANSLATION_ROUTE_EVENT, AGENT_PRE_CALL_EVENT,
                                          					 AGENT_PRE_CALL_ABORT_EVENT

110

(reserved)

74

CALL_STATE_TAG

SNAPSHOT_DEVICE_CONF

75

MONITORED_DEVID_TAG

MONITOR_START_REQ

76

AUTHORIZATION_ CODE_TAG

CONFERENCE_CALL_REQ, CONSULTATION_CALL_REQ, MAKE_CALL_REQ,
                                          					 MAKE_PREDICTIVE_CALL_REQ, TRANSFER_CALL_REQ

77

ACCOUNT_CODE_TAG

CONFERENCE_CALL_REQ, CONSULTATION_CALL_REQ, MAKE_CALL_REQ,
                                          					 MAKE_PREDICTIVE_CALL_REQ, TRANSFER_CALL_REQ

78

ORIGINATING_DEVID_TAG

MAKE_PREDICTIVE_CALL_REQ

79

ORIGINATING_LINE _ID_TAG

MAKE_PREDICTIVE_CALL_REQ

80

CLIENT_ADDRESS_ TAG

CLIENT_SESSION_OPENED_EVENT, CLIENT_SESSION_CLOSED_EVENT

81

NAMED_VARIABLE_ TAG

BEGIN_CALL_EVENT, CALL_DATA_UPDATE_EVENT, AGENT_PRE_CALL_EVENT, CALL_TRANSLATION_ROUTE_ EVENT, SET_CALL_DATA_REQ, CONFERENCE_CALL_REQ,
                                          CONSULTATION_CALL_REQ, MAKE_CALL_REQ, MAKE_PREDICTIVE_CALL_REQ, TRANSFER_CALL_REQ, SNAPSHOT_CALL_CONF, REGISTER_VARIABLES_REQ,
                                          SNAPSHOT_TASK_RESP, SNAPSHOT_TASK_EVENT

82

NAMED_ARRAY_TAG

BEGIN_CALL_EVENT, CALL_DATA_UPDATE_EVENT, AGENT_PRE_CALL_EVENT, CALL_TRANSLATION_ROUTE_ EVENT, SET_CALL_DATA_REQ, CONFERENCE_CALL_REQ,
                                          CONSULTATION_CALL_REQ, MAKE_CALL_REQ, MAKE_PREDICTIVE_CALL_REQ, TRANSFER_CALL_REQ, SNAPSHOT_CALL_CONF, REGISTER_VARIABLES_REQ,
                                          SNAPSHOT_TASK_RESP, SNAPSHOT_TASK_EVENT

83

CALL_CONTROL_ TABLE_TAG

MAKE_CALL_REQ, MAKE_PREDICTIVE_CALL_REQ,

84

SUPERVISOR_ INSTRUMENT_TAG

SUPERVISE_CALL_REQ

85

ATC_AGENT_ID_TAG

AGENT_TEAM_CONFIG_EVENT

86

AGENT_FLAGS_TAG

AGENT_TEAM_CONFIG_EVENT

87

ATC_AGENT_STATE_ TAG

AGENT_TEAM_CONFIG_EVENT

88

ATC_STATE_ DURATION_TAG

AGENT_TEAM_CONFIG_EVENT

89

AGENT_
                                          					 CONNECTION_DEVID_ TAG

SUPERVISE_CALL_REQ

90

SUPERVISOR_ CONNECTION_ DEVID_TAG

SUPERVISE_CALL_REQ,

91

LIST_TEAM_ID_TAG

LIST_AGENT_TEAM_CONF

92

DEFAULT_DEVICE_ PORT_ADDRESS_TAG

AGENT_DESK_SETTINGS_CONF

93

SERVICE_NAME_TAG

REGISTER_SERVICE_REQ

94

CUSTOMER_PHONE_ NUMBER_TAG

SET_CALL_DATA_REQ, CALL_DATA_UPDATE_EVENT

95

CUSTOMER_ ACCOUNT_NUMBER_TAG

SET_CALL_DATA_REQ, CALL_DATA_UPDATE_EVENT

96

APP_PATH_ID_TAG

OPEN_REQ

97

SCRIPT_SELECTOR_TAG

SNAPSHOT_TASK_RESP, SNAPSHOT_TASK_EVENT

99

APPLICATION_STRING1_TAG

SNAPSHOT_TASK_RESP, SNAPSHOT_TASK_EVENT

100

APPLICATION_STRING2_TAG

SNAPSHOT_TASK_RESP, SNAPSHOT_TASK_EVENT

101

ROUTER_CALL_KEY_SEQUENCE_NUM_TAG

AGENT_LEGACY_PRE_CALL_EVENT, BEGIN_CALL_EVENT,
                                          					 CALL_DATA_UPDATE_EVENT, CALL_TRANSLATION_ROUTE_EVENT, AGENT_PRE_CALL_EVENT,
                                          					 AGENT_PRE_CALL_ABORT_EVENT

110

TRUNK_NUMBER_ TAG

CALL_DELIVERED_EVENT, CALL_ESTABLISHED_EVENT,
                                          					 CALL_REACHED_NETWORK_ EVENT

121

TRUNK_GROUP_ NUMBER_TAG

CALL_DELIVERED_EVENT, CALL_ESTABLISHED_EVENT,
                                          					 CALL_REACHED_NETWORK_EVENT

122

EXT_AGENT_STATE_ TAG

AGENT_STATE_EVENT

123

DEQUEUE_TYPE_TAG

CALL_DEQUEUED_EVENT

124

SENDING_ADDRESS_ TAG

RTP_STARTED_EVENT, RTP_STOPPED_EVENT

125

SENDING_PORT_TAG

RTP_STARTED_EVENT RTP_STOPPED_EVENT

126

Unused

127-128

MAX_QUEUED_TAG

CONFIG_SERVICE_EVENT, CONFIG_DEVICE_EVENT

129

QUEUE_ID_TAG

QUEUE_UPDATED_EVENT

130

CUSTOMER_ID_TAG

CONFIG_REQUEST_EVENT

131

SERVICE_SKILL_ TARGET_ID_TAG

CONFIG_SERVICE_EVENT

132

PERIPHERAL_NAME_ TAG

CONFIG_SERVICE_EVENT, CONFIG_SKILL_GROUP_EVENT,
                                          					 CONFIG_AGENT_EVENT, CONFIG_DIALED_NUMBER_ EVENT

133

DESCRIPTION_TAG

CONFIG_SERVICE_EVENT, CONFIG_SKILL_GROUP_EVENT,
                                          					 CONFIG_AGENT_EVENT, CONFIG_DIALED_NUMBER_EVENT

CONFIG_MRD_EVENT

134

SERVICE_MEMBER_ ID_TAG

CONFIG_SKILL_GROUP_EVENT

135

SERVICE_MEMBER_ PRIORITY_TAG

CONFIG_SKILL_GROUP_EVENT

136

FIRST_NAME_TAG

CONFIG_AGENT_EVENT

137

LAST_NAME_TAG

CONFIG_AGENT_EVENT

138

SKILL_GROUP_TAG

CONFIG_AGENT_EVENT

139

AGENT_SKILL_ TARGET_ID_TAG

CONFIG_AGENT_EVENT

141

SERVICE_TAG

CONFIG_DIALED_NUMBER_ EVENT

142

Reserved

143-149

DURATION_TAG

AGENT_STATE_EVENT

150

Reserved

151-172

EXTENSION_TAG

CONFIG_SKILL_GROUP_EVENT, CONFIG_SERVICE_EVENT,
                                          					 CONFIG_AGENT_EVENT,CONFIG_DEVICE_EVENT

173

SERVICE_LEVEL_ THRESHOLD_TAG

CONFIG_SERVICE_EVENT

174

SERVICE_LEVEL_ TYPE_TAG

CONFIG_SERVICE_EVENT

175

CONFIG_PARAM_TAG

CONFIG_SKILL_GROUP_EVENT, CONFIG_SERVICE_EVENT

176

SERVICE_CONFIG_ KEY_TAG

CONFIG_KEY_EVENT, CONFIG_BEGIN_EVENT

177

SKILL_GROUP_ CONFIG_KEY_TAG

CONFIG_KEY_EVENT, CONFIG_BEGIN_EVENT

178

AGENT_CONFIG_ KEY_TAG

CONFIG_KEY_EVENT, CONFIG_BEGIN_EVENT

179

DEVICE_CONFIG_ KEY_TAG

CONFIG_KEY_EVENT, CONFIG_BEGIN_EVENT

180

Unused

181-182

RECORD_TYPE_TAG

CONFIG_AGENT_EVENT, CONFIG_DEVICE_EVENT, CONFIG_SERVICE_EVENT,
                                          					 CONFIG_SKILL_GROUP_EVENT

183

PERIPHERAL_ NUMBER_TAG

CONFIG_AGENT_EVENT, CONFIG_DEVICE_EVENT, CONFIG_SERVICE_EVENT,
                                          					 CONFIG_SKILL_GROUP_EVENT

184

AGENT_SKILL_ TARGET_ID_TAG

CONFIG_AGENT_EVENT

185

NUM_SERVICE_ MEMBERS_TAG

CONFIG_SERVICE_EVENT

186

SERVICE_MEMBER_ TAG

CONFIG_SERVICE_EVENT

187

SERVICE_PRIORITY_ TAG

CONFIG_SERVICE_EVENT

188

AGENT_TYPE_TAG

CONFIG_AGENT_EVENT

189

LOGIN_ID_TAG

CONFIG_AGENT_EVENT

190

NUM_SKILLS_TAG

CONFIG_AGENT_EVENT

191

SKILL_GROUP_SKILL_TARGET_ID_TAG

CONFIG_SKILL_GROUP_EVENT

192

SERVICE_ID_TAG

CONFIG_DEVICE_EVENT

193

AGENT_ID_LONG_ TAG

OPEN_REQ, OPEN_REQ, OPEN_REQ_CONF, AGENT_STATE_EVENT,
                                          					 RTP_STARTED_EVENT, RTP_STOPPED_EVENT, SUPERVISE_CALL_REQ, EMERGENCY_CALL_EVENT,
                                          					 USER_MESSAGE_REQ, SET_AGENT_STATE_REQ, SET_AGENT_STATE_CONF,
                                          					 QUERY_AGENT_STATE_REQ, QUERY_AGENT_STATE_CONF, AGENT_UPDATED_EVENT

194

DEVICE_TYPE_TAG

CONFIG_DEVICE_EVENT

195

Unused

196-197

ENABLE_TAG

ROUTE_REGISTER_EVENT

198

DEVICEID_TAG

ROUTE_REQUEST_EVENT

199

TIMEOUT_TAG

ROUTE_REQUEST_EVENT

200

CURRENT_ROUTE_ TAG

ROUTE_REQUEST_EVENT

201

SECONDARY_ CONNECTION_CALL_ ID

CALL_DELIVERED_EVENT

202

PRIORITY_QUEUE_ NUMBER_TAG

CALL_QUEUED_EVENT

203

TEAM_NAME_TAG

TEAM_CONFIG_EVENT

204

MEMBER_TYPE_TAG

TEAM_CONFIG_EVENT

205

EVENT_DEVICE_ID_ TAG

SYSTEM_EVENT

206

LOGIN_NAME_TAG (V11)

CONFIG_AGENT_EVENT

207

PERIPHERAL_ID_TAG (V11)

CONFIG_AGENT_EVENT, CONFIG_SERVICE_EVENT,
                                          					 CONFIG_SKILL_GROUP_EVENT, CONFIG_DEVICE_EVENT

208

CALL_TYPE_KEY_ CONFIG_TAG (V11)

CONFIG_KEY_EVENT

209

CALL_TYPE_ID_TAG (V11)

AGENT_PRE_CALL_EVENT, CONFIG_CALL_TYPE_EVENT, SET_APP_DATA

210

CUSTOMER_ DEFINITION_ID_TAG (V11)

CONFIG_CALL_TYPE_EVENT

211

ENTERPRISE_NAME_ TAG (V11)

CONFIG_CALL_TYPE_EVENT

CONFIG_MRD_EVENT

212

OLD_PERIPHERAL_ NUMBER_TAG

CONFIG_SKILL_GROUP_EVENT, CONFIG_CALL_TYPE_EVENT

213

CUR_LOGIN_ID

CONFIG_AGENT_EVENT

214

ANI_II_TAG

BEGIN_CALL_EVENT, CALL_TRANSLATION_ROUTE_ EVENT,
                                          					 CALL_DATA_UPDATE, CALL_DELIVERED_EVENT, AGENT_PRE_CALL_EVENT,
                                          					 SET_CALL_DATA_REQ, SNAPSHOT_CALL_REQ, ROUTE_REQUEST_EVENT

215

MR_DOMAIN_ID_TAG

CONFIG_SKILL_GROUP_EVENT, CONFIG_SERVICE_EVENT

CONFIG_MRD_EVENT

216

CTIOS_CIL_CLIENT_ ID_TAG

SET_CALL_DATA_REQ, ALTERNATE_CALL_REQ, ANSWER_CALL_REQ,
                                          					 CLEAR_CALL_REQ, CLEAR_CONNECTION_REQ, DEFLECT_CALL_REQ, HOLD_CALL_REQ,
                                          					 RECONNECT_CALL_REQ, RETRIEVE_CALL_REQ, SEND_DTMF_SIGNAL_REQ,
                                          					 CHANGE_MONITOR_MASK_REQ, USER_MESSAGE_REQ, SESSION_MONITOR_START_REQ,
                                          					 SESSION_MONITOR_STOP_REQ, MONITOR_AGENT_TEAM_START_REQ, MONITOR_AGENT_TEAM_
                                          					 STOP_REQ, FAILURE_CONF, CONTROL_FAILURE_CONF

217

SILENT_MONITOR_ STATUS_TAG

SNAPSHOT_DEVICE_CONF

218

REQUESTING_ DEVICE_ID_TAG

CALL_CLEAR_CONNECTION_REQ

219

REQUESTING_ DEVICE_ID_ TYPE_TAG

CALL_CLEAR_CONNECTION_REQ

220

PRE_CALL_INVOKE_ ID_TAG

AGENT_PRE_CALL_EVENT, SET_APP_DATA

221

ENTERPRISE_ QUEUE_TIME

222

CALL_REFERENCE_ ID_TAG

BEGIN_CALL_EVENT, CALL_DATA_UPDATE_EVENT, CALL_TERMINATION_EVNT,
                                          					 SNAPSHOT_CALL_CONF

223

MULTI_LINE_AGENT_ CONTROL_TAG

OPEN_CONF

224

NETWORK_
                                          					 CONTROLLED_TAG

ROUTE_SELECT_EVENT

225

Used

226-227

NUM_PERIPHERALS_ TAG

OPEN_CONF

228

COC_CONNECTION_ CALL_ID_TAG

CALL_SERVICE_INITIATED_ EVENT, ROUTE_REQUEST_EVENT, SNAPSHOT
                                          					 _CALL_CONF

229

COC_CONNECTION_ DEVICE_ID_TYPE_ TAG

CALL_SERVICE_INITIATED_ EVENT, ROUTE_REQUEST_EVENT, SNAPSHOT
                                          					 _CALL_CONF

230

COC_CONNECTION_ DEVICE_ID_TAG

CALL_SERVICE_INITIATED_ EVENT, ROUTE_REQUEST_EVENT, SNAPSHOT
                                          					 _CALL_CONF

231

CALL_ORIGINATED_ FROM_TAG

SET_CALL_DATA_REQ

232

SET_APPDATA_CALLID_TAG

233

CLIENT_SHARE_KEY_TAG

234

AGENT_TEAM_NAME_TAG

AGENT_TEAM_CONFIG_EVENT

243

DIRECTION_TAG

AGENT_STATE_EVENT

244

OPTIONS_TAG

ROUTE_REQUEST_EVENT (internal use only for ACMI PIM)

245

FLT_MRD_ID_TAG

CONFIG_MEDIA_ROUTING_DOMAIN_EVENT (Internal Cisco Use Only)

246

MEDIA_CLASS_ID_TAG

CONFIG_MEDIA_ROUTING_DOMAIN_EVENT and

CONFIG_MEDIA_CLASS_EVENT (Internal Cisco Use Only)

247

TASK_LIFE_TAG

CONFIG_MEDIA_ROUTING_DOMAIN_EVENT and

CONFIG_MEDIA_CLASS_EVENT (Internal Cisco Use Only)

248

TASK_START_TIMEOUT_TAG

CONFIG_MEDIA_ROUTING_DOMAIN_EVENT and

CONFIG_MEDIA_CLASS_EVENT (Internal Cisco Use Only)

249

MAX_TASK_DURATION_TAG

CONFIG_MEDIA_ROUTING_DOMAIN_EVENT and

CONFIG_MEDIA_CLASS_EVENT (Internal Cisco Use Only)

CONFIG_MRD_EVENT

250

INTERRUPTIBLE_TAG

CONFIG_MEDIA_ROUTING_DOMAIN_EVENT (Internal Cisco Use Only)

CONFIG_MRD_EVENT

251

MAX_CALLS_IN_QUEUE_TAG

CONFIG_MEDIA_ROUTING_DOMAIN_EVENT (Internal Cisco Use Only)

252

MAX_CALLS_IN_QUEUE_PER_CALL_TYPE_TAG

CONFIG_MEDIA_ROUTING_DOMAIN_EVENT (Internal Cisco Use Only)

253

MAX_TIME_IN_QUEUE_TAG

CONFIG_MEDIA_ROUTING_DOMAIN_EVENT (Internal Cisco Use Only)

254

INTERNAL_AGENT_STATE_TAG

QUERY_AGENT_STATE_CONF (internal use only for CCX)

255

Unused

256

SSO_ENABLED_TAG

CONFIG_AGENT_EVENT, SET_AGENT_STATE_REQ

257

FLT_TASK_ID_TAG

AGENT_TASKS_RESP, AGENT_TASKS_EVENT

258

FLT_ICM_DISP_TAG

MEDIA_LOGOUT_IND

259

FLT_APP_DISP_TAG

MEDIA_LOGOUT_IND

260

NUM_MRDS_TAG

CONFIG_AGENT_EVENT, DESKTOP_CONNECTED_IND

261

FLT_AGENT_MRD_ID_TAG

CONFIG_AGENT_EVENT, DESKTOP_CONNECTED_IND

262

FLT_AGENT_MRD_STATE_TAG

CONFIG_AGENT_EVENT

263

FLT_PRECISION_QUEUE_ID_TAG

CONFIG_SKILL_GROUP_EVENT

264

FLT_PRECISION_QUEUE_NAME_TAG

CONFIG_SKILL_GROUP_EVENT

265

MAX_BEYOND_TASK_LIMIT_TAG

AGENT_STATE_EVENT,

QUERY_AGENT_STATE_CONF,

MEDIA_LOGIN_REQ,

AGENT_INIT_REQ

266

AGENT_DESK_SETTINGS_ID_TAG

CONFIG_AGENT_EVENT

267

XFER_IN_WHILE_LOGGED_OUT_TAG

OFFER_APPLICATION_TASK_REQ

START_APPLICATION_TASK_REQ

268

PERIPHERAL_CONFIG_KEY_TAG

CONFIG_KEY_EVENT

269

AGENT_DESK_SETTINGS_CONFIG_KEY_TAG

CONFIG_AGENT_EVENT

270

CONFIG_PERIPHERAL_ID_TAG

CONFIG_PERIPHERAL_EVENT

271

DEFAULT_AGENT_DESK_SETTINGS_ID_TAG

CONFIG_PERIPHERAL_EVENT

272

FLT_DESK_SETTINGS_MASK_TAG

CONFIG_AGENT_DESK_SETTINGS_EVENT

273

FLT_WRAP_UP_DATA_INCOMING_MODE_TAG

CONFIG_AGENT_DESK_SETTINGS_EVENT

274

FLT_WRAP_UP_DATA_OUTGOING_MODE_TAG

CONFIG_AGENT_DESK_SETTINGS_EVENT

275

FLT_LOGOUT_NON_ACTIVITY_TIME_TAG

CONFIG_AGENT_DESK_SETTINGS_EVENT

276

FLT_QUALITY_RECORDING_RATE_TAG

CONFIG_AGENT_DESK_SETTINGS_EVENT

277

FLT_RING_NO_ANSWER_TIME_TAG

CONFIG_AGENT_DESK_SETTINGS_EVENT

278

FLT_SILENT_MONITOR_WARNING_MESSAGE_TAG

CONFIG_AGENT_DESK_SETTINGS_EVENT

279

FLT_SILENT_MONITOR_AUDIBLE_INDICATION_TAG

CONFIG_AGENT_DESK_SETTINGS_EVENT

280

FLT_SUPERVISOR_ASSIST_CALL_METHOD_TAG

CONFIG_AGENT_DESK_SETTINGS_EVENT

281

FLT_EMERGENCY_CALL_METHOD_TAG

CONFIG_AGENT_DESK_SETTINGS_EVENT

282

FLT_AUTO_RECORD_ON_EMERGENCY_TAG

CONFIG_AGENT_DESK_SETTINGS_EVENT

283

FLT_RECORDING_MODE_TAG

CONFIG_AGENT_DESK_SETTINGS_EVENT

284

FLT_WORK_MODE_TIMER_TAG

CONFIG_AGENT_DESK_SETTINGS_EVENT

285

FLT_RING_NO_ANSWER_DN_ID_TAG

CONFIG_AGENT_DESK_SETTINGS_EVENT

286

FLT_DEFAULT_DEVICE_PORT_ADDRESS_TAG

CONFIG_AGENT_DESK_SETTINGS_EVENT

287

DESKTOP_CONNECTED_FLAG_TAG

AGENT_TASKS_REQUEST_EVENT

288

PLAY_TONE_DIRECTION_TAG

START_NETWORK_RECORDING_REQ

289

INVOCATION_TYPE_TAG

START_NETWORK_RECORDING_REQ, STOP_NETWORK_RECORDING_REQ

290

RECORDER_ADDRESS_TAG

NETWORK_RECORDING_TARGET_INFO_EVENT

291

TERMINAL_NAME_TAG

NETWORK_RECORDING_TARGET_INFO_EVENT

292

MEDIA_FORKING_DEVICE_NAME_TAG

NETWORK_RECORDING_TARGET_INFO_EVENT

293

PROTOCOL_REFERENCE_GUID_TAG

NETWORK_RECORDING_TARGET_INFO_EVENT

AGENT_PRE_CALL_EVENT

294

MEDIA_FORKING_CLUSTER_ID_TAG

NETWORK_RECORDING_TARGET_INFO_EVENT

295

RECORDER_URI_TAG

NETWORK_RECORDING_TARGET_INFO_EVENT

296

RECORDER_ERROR_MSG_TAG

NETWORK_RECORDING_TARGET_INFO_EVENT

297

RECORDER_TYPE_TAG

NETWORK_RECORDING_TARGET_INFO_EVENT

298

RECORDER_STATUS_TAG

NETWORK_RECORDING_TARGET_INFO_EVENT

299

RECORDING_DEVICE_ID_TAG

NETWORK_RECORDING_STARTED_EVENT, NETWORK_RECORDING_ENDED_EVENT, NETWORK_RECORDING_FAILED_EVENT, NETWORK_RECORDING_TARGET_INFO_EVENT

300

FLT_TERM_TYPE

CONFIG_TERMINAL_EVENT

302

FLT_TERM_DEVICE_NAME

CONFIG_TERMINAL_EVENT,CONFIG_AGENT_EVENT, SET_AGENT_STATE_REQ, AGENT_STATE_EVENT

303

FLT__TERM_TYPE_NAME

CONFIG_TERMINAL_EVENT

304

FLT_NUM_INSTRUMENTS

CONFIG_TERMINAL_EVENT

305

ACD_SHARED_LINE_USAGE

AGENT_DESK_SETTINGS_CONF

CONFIG_AGENT_DESK_SETTINGS_EVENT

306

PLAY_ZIP_TONE

AGENT_DESK_SETTINGS_CONF

CONFIG_AGENT_DESK_SETTINGS_EVENT

307

FLT_ENABLED_SERVICES

CONFIG_AGENT_SERVICE_EVENT

SET_AGENT_SERVICE_DATA_REQ

309

NUM_OF_ENABLED_SERVICES

CONFIG_AGENT_SERVICE_EVENT

SET_AGENT_SERVICE_DATA_REQ

310

CCAI_CONFIG_ID

AGENT_PRE_CALL_EVENT

311

MEDIA_TYPE_TAG

MEDIA_LOGIN_REQ

312

MEDIA_PROVIDER_TAG

MEDIA_LOGIN_REQ

313

## AgentState
                        	 Values

This
                              		  table shows the agent state values that may appear in the
                              		  QUERY_AGENT_STATE_CONF messages.

State Name

Description

Value

AGENT_STATE_ LOGIN

The agent
                                          					 has logged on to the ACD. It does not necessarily indicate that the agent is
                                          					 ready to accept calls.

0

AGENT_STATE_ LOGOUT

The agent
                                          					 has logged out of the ACD and cannot accept any additional calls.

1

AGENT_STATE_ NOT_ READY

The agent
                                          					 is unavailable for any call work.

2

AGENT_STATE_ AVAILABLE

The agent
                                          					 is ready to accept a call.

3

AGENT_STATE_ TALKING

The agent
                                          					 is currently talking on a call (inbound, outbound, or inside).

4

AGENT_STATE_ WORK_NOT_READY

The agent
                                          					 is performing after call work, but will not be ready to receive a call when
                                          					 completed.

5

AGENT_STATE_ WORK_ READY

The agent
                                          					 is performing after call work, and will be ready to receive a call when
                                          					 completed.

6

AGENT_STATE_ BUSY_ OTHER

The agent
                                          					 is busy performing a task associated with another active SkillGroup.

7

AGENT_STATE_ RESERVED

The agent
                                          					 is reserved for a call that will arrive at the ACD shortly.

8

AGENT_STATE_ UNKNOWN

The agent
                                          					 state is currently unknown.

9

AGENT_STATE_ HOLD

The agent
                                          					 currently has all calls on hold.

10

AGENT_STATE_ ACTIVE

The agent
                                          					 state is currently active.

11

AGENT_STATE_ PAUSED

The agent
                                          					 state is currently paused.

12

AGENT_STATE_ INTERRUPTED

The agent
                                          					 state is currently interrupted.

13

AGENT_STATE_NOT_ACTIVE

The agent
                                          					 state is currently not active.

14

## PGStatusCode
                        	 Values

This
                              		  table shows the PGStatusCode values that may be included in the SYSTEM_EVENT
                              		  message.

PGStatus

Description

Mask Value

PGS_OPC_DOWN

Communication lost between the CTI Server and the PG’s Open
                                          					 Peripheral Controller (OPC) process. No call or agent state event messages can
                                          					 be sent due to this condition.

0x00000001

PGS_CC_DOWN

Communication lost between the PG and the Unified CCE Central
                                          					 Controller. Primarily affects translation routing and post-routing, other call
                                          					 and agent event messages can still be sent.

0x00000002

PGS_PERIPHERAL_OFFLINE

One or
                                          					 more of the peripherals monitored by the PG are offline.

0x00000004

PGS_CTI_SERVER_OFFLINE

Loss of
                                          					 communication between the CTI Server and the CTI Client. This status code is
                                          					 not reported by a software layer between the CTI Server and the client
                                          					 application.

0x00000008

PGS_LIMITED_FUNCTION

This
                                          					 status code may be reported by a software layer between the CTI Server and the
                                          					 client application when PGS_CTI_SERVER_ OFFLINE is true to indicate that
                                          					 limited local call control is possible.

0x00000010

## PeripheralType
                        	 Values

This
                              		  table shows the PeripheralType values that may be included in the Client Events
                              		  service messages.

Peripheral
                                          					 Type

Description

Value

PT_NONE

Not
                                          					 Applicable

0xffff

PT_MERIDIAN

Northern
                                          					 Telecom Meridian ACD

2

PT_G2

Lucent G2

3

PT_DEFINITY_ECS_ NON_EAS

Lucent
                                          					 DEFINITY ECS (without Expert Agent Selection)

4

PT_DEFINITY_ECS_ EAS

Lucent
                                          					 DEFINITY ECS (with Expert Agent Selection)

5

PT_GALAXY

Obsolete

6

PT_SPECTRUM

Obsolete

7

PT_VRU

VRU (event
                                          					 type interface)

8

PT_VRU_POLLED

VRU
                                          					 (polled type interface)

9

PT_DMS100

Obsolete

10

PT_SIEMENS_9006

Siemens
                                          					 Hicom ACD (9006)

11

PT_SIEMENS_9005

Siemens
                                          					 9751 CBX Release 9005 (Rolm 9005)

12

PT_ALCATEL

Alcatel
                                          					 4400 ACD

13

PT_NEC_NEAX_2x00

Obsolete

14

PT_
                                          					 ACP_1000

Ericsson
                                          					 ACP1000

15

PT_ENTERPRISE_ AGENT

Unified
                                          					 CCE Manager

17

PT_MD110

Ericsson
                                          					 MD-110

18

PT_MEDIA_ROUTING

Media
                                          					 Routing

19

PT_GENERIC

Generic

20

PT_ACMI_CRS

A
                                          					 Gateway PG over Unified CCX

21

PT_ACMI_IPCC

A
                                          					 Gateway PG over Unified CCE or Unified CCX

22

PT_ARS

A system
                                          					 using the ARS PG

24

PT_ACMI_ERS

A system
                                          					 using the ERS PG

25

PT_ACMI_EXPERT_ADVISOR

Obsolete

26

{reserved}

27

## LocalConnectionState Values

This
                              		  table shows the LocalConnectionState values.

LocalConnectionState

Description

Value

LCS_NONE

Not
                                          					 applicable

0xffff

LCS_NULL

No
                                          					 relationship between call and device.

0

LCS_INITIATE

Device
                                          					 requesting service (“dialing”).

1

LCS_ALERTING

Device is
                                          					 alerting (“ringing”).

2

LCS_CONNECT

Device is
                                          					 actively participating in the call.

3

LCS_HOLD

Device is
                                          					 inactively participating in the call.

4

LCS_QUEUED

Device is
                                          					 stalled attempting to connect to a call, or a call is stalled attempting to
                                          					 connect to a device.

5

LCS_FAIL

A
                                          					 device-to-call or call-to-device connection attempt has been aborted.

6

## EventCause
                        	 Values

These tables show the EventCause values.

EventCause

Value

CEC_NONE

0xffff

CEC_ACTIVE_MONITOR

1

CEC_ALTERNATE

2

CEC_BUSY

3

CEC_CALL_BACK

4

CEC_CALL_CANCELLED

5

CEC_CALL_FORWARD_ALWAYS

6

CEC_CALL_FORWARD_BUSY

7

CEC_CALL_FORWARD_NO_ANSWER

8

CEC_CALL_FORWARD

9

CEC_CALL_NOT_ANSWERED

10

CEC_CALL_PICKUP

11

CEC_CAMP_ON

12

CEC_DEST_NOT_OBTAINABLE

13

CEC_DO_NOT_DISTURB

14

CEC_INCOMPATIBLE_DESTINATION

15

CEC_INVALID_ACCOUNT_CODE

16

CEC_KEY_CONFERENCE

17

CEC_LOCKOUT

18

CEC_MAINTENANCE

19

CEC_NETWORK_CONGESTION

20

CEC_NETWORK_NOT_OBTAINABLE

21

CEC_NEW_CALL

22

CEC_NO_AVAILABLE_AGENTS

23

CEC_OVERRIDE

24

CEC_PARK

25

CEC_OVERFLOW

26

CEC_RECALL

27

CEC_REDIRECTED

28

CEC_REORDER_TONE

29

CEC_RESOURCES_NOT_AVAILABLE

30

CEC_SILENT_MONITOR

31

CEC_TRANSFER

32

CEC_TRUNKS_BUSY

33

CEC_VOICE_UNIT_INITIATOR

34

CEC_TIME_OUT

35

CEC_NEW_CALL_INTERFLOW

36

CEC_SIMULATION_INIT_REQUEST

37

CEC_SIMULATION_RESET_REQUEST

38

CEC_CTI_LINK_DOWN

39

CEC_PERIPHERAL_RESET_REQUEST

40

CEC_MD110_CONFERENCE_TRANSFER

41

CEC_REMAINS_IN_Q

42

CEC_SUPERVISOR_ASSIST

43

CEC_EMERGENCY_CALL

44

CEC_SUPERVISOR_CLEAR

45

CEC_SUPERVISOR_MONITOR

46

CEC_SUPERVISOR_WHISPER

47

CEC_SUPERVISOR_BARGE_IN

48

CEC_SUPERVISOR_INTERCEPT

49

CEC_CALL_PARTY_UPDATE_IND

50

CEC_CONSULT

51

CEC_NIC_CALL_CLEAR

52

CEC_DNP

53

CEC_ ROUTER_REQUERY_BEFORE_ANSWER

54

CEC_ROUTER_REQUERY_AFTER_ANSWER

55

CEC_ NETWORK_ERROR

56

CEC_ NETWORK_ERROR_BEFORE_ANSWER

57

CEC_NETWORK_ERROR_AFTER_ANSWER

58

CEC_ GREETING

59

CEC_ RECORD_AGENT_GREETING

60

CEC_SNAPSHOT

61

CEC_ MAX_QUEUE_EXCEEDED

62

Extended
                                 				Call Cleared Event Causes

EventCause

Value

CECX_ABAND_NETWORK

1001

CECX_ABAND_LOCAL_QUEUE

1002

CECX_ABAND_RING

1003

CECX_ABAND_DELAY

1004

CECX_ABAND_INTERFLOW

1005

CECX_ABAND_AGENT_TERMINAL

1006

CECX_SHORT

1007

CECX_BUSY

1008

CECX_FORCED_BUSY

1009

CECX_DROP_NO_ANSWER

1010

CECX_DROP_BUSY

1011

CECX_DROP_REORDER

1012

CECX_DROP_HANDLED_PRIMARY_ROUTE

1013

CECX_DROP_HANDLED_OTHER

1014

CECX_REDIRECTED

1015

CECX_CUT_THROUGH

1016

CECX_INTRAFLOW

1017

CECX_INTERFLOW

1018

CECX_RING_NO_ANSWER

1019

CECX_INTERCEPT_REORDER

1020

CECX_INTERCEPT_DENIAL

1021

CECX_TIME_OUT

1022

CECX_VOICE_ENERGY

1023

CECX_NONCLASSIFIED_ENERGY_DETECT

1024

CECX_NO_CUT_THROUGH

1025

CECX_UABORT

1026

CECX_FAILED_SOFTWARE

1027

CECX_BLIND_TRANSFER

1028

CECX_ANNOUNCED_TRANSFER

1029

CECX_CONFERENCED

1030

CECX_DUPLICATE_TRANSFER

1031

CECX_UNMONITORED_DEVICE

1032

CECX_ANSWERING_MACHINE

1033

CECX_NETWORK_BLIND_TRANSFER

1034

CECX_TASK_ABANDONED_IN_ROUTER

1035

CECX_TASK_ABANDONED_BEFORE_OFFERED

1036

CECX_TASK_ABANDONED_WHILE_OFFERED

1037

CECX_NORMAL_END_TASK

1038

CECX_CANT_OBTAIN_TASK_ID

1039

CECX_AGENT_LOGGED_OUT_DURING_TASK

1040

CECX_MAX_TASK_LIFETIME_EXCEEDED

1041

CECX_APPLICATION_PATH_WENT_DOWN

1042

CECX_ICM_ROUTING_COMPLETE

1043

CECX_ICM_ROUTING_DISABLED

1044

CECX_APPL_INVALID_MRD_ID

1045

CECX_APPL_INVALID_DIALOGUE_ID

1056

CECX_APPL_DUPLICATE_DIALOGUE_ID

1047

CECX_APPL_INVALID_INVOKE_ID

1048

CECX_APPL_INVALID_SCRIPT_SELECTOR

1049

CECX_APPL_TERMINATE_DIALOGUE

1050

CECX_TASK_ENDED_DURING_APP_INIT

1051

CECX_CALLED_PARTY_DISCONNECTED

1052

CECX_PARTIAL_CALL

1053

CECX_DROP_NETWORK_CONSULT

1054

CECX_NETWORK_CONSULT_TRANSFER

1055

CECX_NETWORK_CONFERENCE

1056

CECX_ABAND_NETWORK_CONSULT

1057

## DeviceIDType
                        	 Values

This
                              		  table shows the DeviceIDType values.

Device ID
                                          					 Type

Description

Value

DEVID_NONE

No device
                                          					 ID is provided.

0xffff

DEVID_DEVICE_IDENTIFIER

The
                                          					 provided device ID identifies a peripheral teleset (extension).

0

DEVID_TRUNK_IDENTIFIER

The
                                          					 provided device ID identifies a peripheral Trunk.

70

DEVID_TRUNK_GROUP_ IDENTIFIER

The
                                          					 provided device ID identifies a peripheral Trunk Group.

71

DEVID_IP_PHONE_MAC_ IDENTIFIER

The
                                          					 provided device ID identifiers the MAC address of an IP phone (Unified CCX
                                          					 ONLY).

72

DEVID_CTI_PORT

The
                                          					 provided device ID identifiers a CTI PORT (Unified CCX ONLY).

73

DEVID_ROUTE_POINT

The
                                          					 provided device ID identifies a ROUTE POINT.

74

DEVID_EXTERNAL

The
                                          					 provided device ID is an ANI number or some other external identifier.

75

DEVID_AGENT_DEVICE

The
                                          					 provided device ID is the ID of an AGENT Device (phone).

76

DEVID_QUEUE

The
                                          					 provided device ID is the ID of a QUEUE.

77

DEVID_NON_ACD_DEVICE_ IDENTIFIER

The
                                          					 provided device ID identifies a peripheral telset (extension) that is
                                          					 classified as being a non-ACD extension.

78

DEVID_SHARED_DEVICE_ IDENTIFIER

The
                                          					 provided device ID identifies a peripheral telset (extension) that is
                                          					 classified as being a shared line (0 or more telsets share this extension).

79

## CallType
                        	 Values

This
                              		  table shows the CallType values.

CallType

Description

Value

CALLTYPE_ACD_IN

Inbound ACD call.

In Unified CCE, it indicates that this is a post route request.

1

CALLTYPE
                                          					 _PREROUTE_ ACD_IN

Translation routed inbound ACD call.

2

CALLTYPE
                                          					 _PREROUTE_ DIRECT_AGENT

Translation routed call to a specific agent.

3

CALLTYPE
                                          					 _TRANSFER_IN

Transferred inbound call.

4

CALLTYPE
                                          					 _OVERFLOW_IN

Overflowed
                                          					 inbound call.

5

CALLTYPE
                                          					 _OTHER_IN

Inbound
                                          					 call.

6

CALLTYPE
                                          					 _AUTO_OUT

Automatic
                                          					 out call.

7

CALLTYPE
                                          					 _AGENT_OUT

Agent out
                                          					 call.

8

CALLTYPE
                                          					 _OUT

Outbound
                                          					 call.

9

CALLTYPE
                                          					 _AGENT_INSIDE

Agent
                                          					 inside call.

10

CALLTYPE
                                          					 _OFFERED

Blind
                                          					 transferred call.

11

CALLTYPE
                                          					 _CONSULT

Consult
                                          					 call.

12

CALLTYPE
                                          					 _CONSULT_ OFFERRED

Announced
                                          					 transferred call.

13

CALLTYPE
                                          					 _CONSULT_ CONFERENCE

Conferenced consult call.

14

CALLTYPE
                                          					 _CONFERENCE

Conference
                                          					 call.

15

CALLTYPE_UNMONITORED

Inside or
                                          					 outbound call for which no call events will be received.

16

CALLTYPE_PREVIEW

Automatic
                                          					 out call in which the agent is given the option to proceed to dial a contact.

17

CALLTYPE_RESERVATION

Call made
                                          					 to reserve an agent for some other function.

18

CALLTYPE_ASSIST

Call to
                                          					 supervisor for assistance.

19

CALLTYPE_EMERGENCY

Emergency
                                          					 call.

20

CALLTYPE_SUPERVISOR_ MONITOR

Supervisor
                                          					 silently monitoring call.

21

CALLTYPE_SUPERVISOR_ WHISPER

Supervisor monitoring call, agent can hear supervisor.

22

CALLTYPE_SUPERVISOR_ BARGEIN

Supervisor conferenced into call.

23

CALLTYPE_SUPERVISOR_ INTERCEPT

Supervisor replaces agent on call.

24

CALLTYPE_TASK_ROUTED_BY_ICM

Task
                                          					 routed by Unified CCE

25

CALLTYPE_TASK_ROUTED_BY_APPLICATION

Task
                                          					 routed by application

26

CALLTYPE_NON_ACD

Agent
                                          					 call that is a non-ACD routed call.

27

RESERVATION_PREVIEW

Call
                                          					 type for Outbound Option Reservation calls for Preview mode.

27

RESERVATION_PREVIEW_DIRECT

Call
                                          					 type for Outbound Option Reservation calls for Direct Preview mode.

28

RESERVATION_PREDICTIVE

Call
                                          					 type for Outbound Option Reservation calls for Predictive mode and Progressive
                                          					 mode.

29

RESERVATION_CALLBACK

Call
                                          					 type for Outbound Option Reservation calls for Callback calls.

30

RESERVATION_PERSONAL_CALLBACK

Call
                                          					 type for Outbound Option Reservation calls for Personal Callback calls.

31

CUSTOMER_PREVIEW

Call
                                          					 type for Outbound Option Customer calls for Preview mode.

32

CUSTOMER_PREVIEW_DIRECT

Call
                                          					 type for Outbound Option

Customer
                                          					 calls for Direct Preview

33

CUSTOMER_PREDICTIVE

Call
                                          					 type for Outbound Option Customer calls for Predictive mode and Progreassive
                                          					 modefor agentbased campaigns.

34

CUSTOMER_CALLBACK

Call
                                          					 type for Outbound Option Customer calls for callback calls.

35

CUSTOMER_PERSONAL

Call
                                          					 type for Outbound Option Customer calls for personal callback calls.

36

CUSTOMER_IVR

Call
                                          					 type for Outbound Option Customer calls for Transfer to IVR campaigns.

37

CALLTYPE_NON_ACD

Agent
                                          					 call that is a non-ACD call.

38

CALLTYPE_PLAY_AGENT_GREETING

An agent
                                          					 greeting route request.

39

CALLTYPE_RECORD_AGENT_GREETING

Record
                                          					 agent greeting call initiated by AGENT_GREETING_CONTROL_REQ.

40

CALLTYPE_VOICE_CALL_BACK

Voice
                                          					 callback using the Agent Request API.

41

## ConnectionDeviceIDType Values

This
                              		  table shows the possible ConnectionDeviceIDType values.

ConnectionDevice IDType

Description

Value

CONNECTION_ID_ NONE

No
                                          					 ConnectionDeviceID is provided.

0xffff

CONNECTION_ID_ STATIC

The
                                          					 ConnectionDeviceID value is stable over time (between calls).

0

CONNECTION_ID_ DYNAMIC

The
                                          					 ConnectionDeviceID value is dynamic and may change between calls.

1

## LineType
                        	 Values

This
                              		  table shows the possible LineType values.

LineType

Description

Value

LINETYPE_INBOUND_ ACD

Line used
                                          					 for inbound ACD calls.

0

LINETYPE_OUTBOUND_ACD

Line used
                                          					 for outbound ACD calls.

1

LINETYPE_INSIDE

Line used
                                          					 for inside calls.

2

LINETYPE_UNKNOWN

Line used
                                          					 for any purpose.

3

LINETYPE_SUPERVISOR

Line used
                                          					 for supervisor calls.

4

LINETYPE_MESSAGE

Line used
                                          					 for voice messages.

5

LINETYPE_HELP

Line used
                                          					 for assistance.

6

LINETYPE_OUTBOUND

Line used
                                          					 for outbound non-ACD calls.

7

LINETYPE_DID

Line used
                                          					 for direct inward dialed calls.

8

LINETYPE_SILENT_ MONITOR

Line used
                                          					 for silent monitor.

9

LINETYPE_NON_ACD_IN

Line used
                                          					 for inbound non-ACD calls.

10

LINETYPE_NON_ACD_OUT

Line used
                                          					 for outbound non-ACD calls.

11

## ControlFailureCode
                        	 Values

This
                              		  table shows the possible ControlFailureCode values.

FailureCode

Description

Value

CF_GENERIC_UNSPECIFIED

An error
                                          					 has occurred that is not one of the following error types.

0

CF_GENERIC_OPERATION

An
                                          					 operation error occurred (no specific details available).

1

CF_REQUEST_ INCOMPATIBLE_WITH_ OBJECT

The
                                          					 request is not compatible with the object.

2

CF_VALUE_OUT_OF_ RANGE

The
                                          					 parameter has a value that is not in the range defined for the server.

3

CF_OBJECT_NOT_KNOWN

The
                                          					 parameter has a value that is not known to the server.

4

CF_INVALID_CALLING_ DEVICE

The
                                          					 calling device is invalid.

5

CF_INVALID_CALLED_ DEVICE

The called
                                          					 device is invalid

6

CF_INVALID_FORWARDING_ DESTINATION

The
                                          					 forwarding destination device is invalid.

7

CF_PRIVILEGE_VIOLATION_ ON_SPECIFIED_DEVICE

The
                                          					 specified device is not authorized for the service.

8

CF_PRIVILEGE_VIOLATION_ ON_CALLED_DEVICE

The called
                                          					 device is not authorized for the service.

9

CF_PRIVILEGE_VIOLATION_ ON_CALLING_DEVICE

The
                                          					 calling device is not authorized for the service.

10

CF_INVALID_CSTA_CALL_ IDENTIFIER

The call
                                          					 identifier is invalid.

11

CF_INVALID_CSTA_DEVICE_ IDENTIFIER

The device
                                          					 identifier is invalid.

12

CF_INVALID_CSTA_ CONNECTION_IDENTIFIER

The
                                          					 connection identifier is invalid.

13

CF_INVALID_DESTINATION

The
                                          					 request specified a destination that is invalid.

14

CF_INVALID_FEATURE

The
                                          					 request specified a feature that is invalid.

15

CF_INVALID_ALLOCATION_ STATE

The
                                          					 request specified an allocation state that is invalid.

16

CF_INVALID_CROSS_REF_ID

The
                                          					 request specified a cross- reference ID that is not in use at this time.

17

CF_INVALID_OBJECT_TYPE

The
                                          					 request specified an invalid object type.

18

CF_SECURITY_VIOLATION

Security
                                          					 error (no specific details available).

19

CF_GENERIC_STATE_ INCOMPATIBILITY

The
                                          					 request is not compatible with the condition of a related device.

21

CF_INVALID_OBJECT_STATE

The
                                          					 object is in the incorrect state for the request.

22

CF_INVALID_CONNECTION_ ID_FOR_ACTIVE_CALL

The
                                          					 active connection ID in the request is invalid.

23

CF_NO_ACTIVE_CALL

There is
                                          					 no active call for the request.

24

CF_NO_HELD_CALL

There is
                                          					 no held call for the request.

25

CF_NO_CALL_TO_CLEAR

There is
                                          					 no call associated with the given connection ID.

26

CF_NO_CONNECTION_TO_ CLEAR

There is
                                          					 no call connection for the given connection ID.

27

CF_NO_CALL_TO_ANSWER

There is
                                          					 no alerting call to be answered.

28

CF_NO_CALL_TO_ COMPLETE

There is
                                          					 no active call to be completed.

29

CF_GENERIC_SYSTEM_ RESOURCE_AVAILABILITY

The
                                          					 request failed due to lack of system resources (no specific details available).

31

CF_SERVICE_BUSY

The
                                          					 service is temporarily unavailable.

32

CF_RESOURCE_BUSY

An
                                          					 internal resource is busy.

33

CF_RESOURCE_OUT_OF_ SERVICE

The
                                          					 service requires a resource that is out of service.

34

CF_NETWORK_BUSY

The
                                          					 server sub-domain is busy.

35

CF_NETWORK_OUT_OF_ SERVICE

The
                                          					 server sub-domain is out of service.

36

CF_
                                          					 OVERALL_MONITOR_ LIMIT_EXCEEDED

The
                                          					 request would exceed the server’s overall resource limits.

37

CF_CONFERENCE_MEMBER_ LIMIT_EXCEEDED

The
                                          					 request would exceed the server’s limit on the number of conference members.

38

CF_
                                          					 GENERIC_SUBSCRIBED_ RESOURCE_AVAILABILITY

The
                                          					 request failed due to lack of purchased or contracted resources (no specific
                                          					 details available).

41

CF_
                                          					 OBJECT_MONITOR_ LIMIT_EXCEEDED

The
                                          					 request would exceed the server’s specific resource limits.

42

CF_
                                          					 EXTERNAL_TRUNK_ LIMIT_EXCEEDED

The
                                          					 request would exceed the limit of external trunks.

43

CF_
                                          					 OUTSTANDING_ REQUEST_LIMIT_EXCEEDED

The
                                          					 request would exceed the limit of outstanding requests.

44

CF_GENERIC_ PERFORMANCE_ MANAGEMENT

The
                                          					 request failed as a performance management mechanism (no specific details
                                          					 available).

51

CF_PERFORMANCE_LIMIT_ EXCEEDED

The
                                          					 request failed because a performance management limit was exceeded.

52

CF_
                                          					 SEQUENCE_NUMBER_ VIOLATED

The
                                          					 server has detected an error in the sequence number of the operation.

61

CF_
                                          					 TIME_STAMP_ VIOLATED

The
                                          					 server has detected an error in the time stamp of the operation.

62

CF_
                                          					 PAC_VIOLATED

The
                                          					 server has detected an error in the PAC of the operation.

63

CF_
                                          					 SEAL_VIOLATED

The
                                          					 server has detected an error in the Seal of the operation.

64

CF_
                                          					 GENERIC_UNSPECIFIED_ REJECTION

The
                                          					 request has been rejected (no specific details available).

70

CF_
                                          					 GENERIC_OPERATION_ REJECTION

The
                                          					 requested operation has been rejected (no specific details available).

71

CF_
                                          					 DUPLICATE_ INVOCATION_REJECTION

The
                                          					 request duplicated another request for the same service.

72

CF_
                                          					 UNRECOGNIZED_ OPERATION_REJECTION

The
                                          					 request specified an unrecognized operation.

73

CF_MISTYPED_ARGUMENT_ REJECTION

The
                                          					 request contained a parameter of the wrong type for the requested operation.

74

CF_
                                          					 RESOURCE_LIMITATION_ REJECTION

The
                                          					 request would have exceeded a resource limitation.

75

CF_
                                          					 ACS_HANDLE_ TERMINATION_REJECTION

The
                                          					 request specified an ACS handle that is no longer in use.

76

CF_
                                          					 SERVICE_ TERMINATION_REJECTION

The
                                          					 request failed because the required service has been terminated.

77

CF_
                                          					 REQUEST_TIMEOUT_ REJECTION

The
                                          					 request failed because a timeout limit was exceeded.

78

CF_REQUESTS_ON_DEVICE_ EXCEEDED_REJECTION

The
                                          					 request would have exceeded the limits of the device.

79

Extended
                                 				Control Failure Codes

FailureCode

Description

Value

CF_INVALID_AGENT_ID_ SPECIFIED

The
                                          						request specified an invalid AgentID.

256

CF_INVALID_PASSWORD_ SPECIFIED

The
                                          						request specified an invalid agent password.

257

CF_INVALID_AGENT_ID_ OR_PASSWORD_SPECIFIED

The
                                          						request specified an invalid AgentID and/or invalid agent password.

258

CF_SPECIFIED_AGENT_ ALREADY_SIGNED_ON

The
                                          						request failed because the specified agent is already logged in.

259

CF_INVALID_LOGON_ DEVICE_SPECIFIED

The
                                          						request specified an invalid logon device.

260

CF_INVALID_ANSWERING_ DEVICE_SPECIFIED

The
                                          						request specified an invalid answering device.

261

CF_INVALID_SKILL_ GROUP_SPECIFIED

The
                                          						request specified an invalid agent skill group.

262

CF_INVALID_CLASS_OF_ SERVICE_SPECIFIED

The
                                          						request specified an invalid class of service.

263

CF_INVALID_TEAM_ SPECIFIED

The
                                          						request specified an invalid team.

264

CF_INVALID_AGENT_ WORKMODE

The
                                          						request specified an invalid agent work mode.

265

CF_INVALID_AGENT_ REASON_CODE

The
                                          						request specified an invalid agent reason code.

266

CF_ADJUNCT_SWITCH_ COMM_ERROR

A
                                          						communication error occurred on the datalink between the Unified CCE and the
                                          						ACD.

267

CF_AGENT_NOT_PARTY_ ON_CALL

The
                                          						specified agent is not a party on the indicated call.

268

CF_INTERNAL_ PROCESSING_ERROR

An
                                          						internal error occurred in the ACD while processing the request.

269

CF_TAKE_CALL_CONTROL_ REJECTION

The
                                          						ACD refused an Unified CCE request to take control of a call.

270

CF_TAKE_DOMAIN_ CONTROL_REJECTION

The
                                          						ACD refused an Unified CCE request to take control of a domain.

271

CF_REQUESTED_SERVICE_ NOT_REGISTERED

The
                                          						Unified CCE is not registered on the ACD for the requested service.

272

CF_INVALID_CONSULT_ TYPE

The
                                          						consult type is invalid.

273

CF_ANSMAP_OR_ ADPARAM_FIELD_NOT_VALID

The
                                          						Ansmap or Asparam field are not valid.

274

CF_INVALID_CALL_ CONTROL_TABLE_ SPECIFIED

The
                                          						call control table is invalid.

275

CF_INVALID_DIGITS_ RNATIMEOUT_AMSDELAY_ OR_COUNTRY

276

CF_ANSWER_DETECT_ PORT_UNAVAILABLE

277

CF_VIRTUAL_AGENT_ UNAVAILABLE

278

CF_TAKEBACK_N_XFER_ ROUTE_END

279

CF_WRAPUP_DATA_ REQUIRED

280

CF_REASON_CODE_ REQUIRED

281

CF_INVALID_TRUNK_ID_ SPECIFIED

282

CF_SPECIFIED_EXTENSION_ ALREADY_IN_USE

283

CF_ARBITRARY_CONF_OR_ XFER_NOT_SUPPORTED

284

CF_NETWORK_TRANSFER_OR_ CONSULT

285

CF_NETWORK_TRANSFER_OR_ CONSULT_FAILED

286

CF_DEVICE_RESTRICTED

287

CF_LINE_RESTRICTED

288

CF_AGENT_ACCOUNT_ LOCKED_OUT

289

CF_DROP_ANY_PARTY_NOT_ ENABLED_CTI

290

CF_MAXIMUM_LINE_LIMIT_ EXCEEDED

291

CF_SHARED_LINES_NOT_ SUPPORTED

292

CF_EXTENSION_NOT_UNIQUE

293

CF_UNKNOWN_ INTERFACE_ CTRLR_ID

The
                                          						Interface Controller ID is unknown.

1001

CF_INVALID_INTERFACE_ CTRLR_TYPE

The
                                          						Interface Controller type is invalid.

1002

CF_SOFTWARE_REV_NO_ SUPPORTED

The
                                          						current software revision is not supported.

1003

CF_UNKNOWN_PID

The
                                          						PeripheralID is unknown.

1004

CF_INVALID_TABLE_ SPECIFIED

An
                                          						invalid table was specified.

1005

CF_PD_SERVICE_INACTIVE

The
                                          						peripheral data service is not active.

1006

CF_UNKNOWN_ROUTING_ CLIENT_ID

The
                                          						RoutingClientID is unknown.

1007

CF_RC_SERVICE_ INACTIVATE

The
                                          						routing client service is not active.

1008

CF_INVALID_DIALED_ NUMBER

The
                                          						dialed number is invalid.

1009

CF_INVALID_PARAMETER

A
                                          						parameter in the request is invalid.

1010

CF_UNKNOWN_ROUTING_ PROBLEM

An
                                          						unspecified error occurred during routing.

1011

CF_UNSUPPORTED_PD_ MESSAGE_REVISION

The
                                          						requested peripheral data service protocol version is not supported.

1012

CF_UNSUPPORTED_RC_ MESSAGE_REVISION

The
                                          						requested routing client service protocol version is not supported.

1013

CF_UNSUPPORTED_IC_ MESSAGE_REVISION

The
                                          						requested interface controller service protocol version is not supported.

1014

CF_RC_SERVICE_ INACTIVATE_PIM

The
                                          						peripheral interface is not active.

1015

CF_AGENT_GREETING_CONTROL_OPERATION_FAILURE

This
                                          						error occurs if AGENT_GREETING_CONTROL_REQ request fails.

Notes:
                                          						All detailed errors are defined as Peripheral Error Codes.

1016

## AllocationState
                        	 Values

This
                              		  table shows the AllocationState values.

AllocationState

Description

Value

ALLOC_CALL_ DELIVERED

Connect
                                          					 call to originating device when call is delivered (alerting).

0

ALLOC_CALL_ ESTABLISHED

Connect
                                          					 call to originating device when call is established (answered).

1

## ForwardType
                        	 Values

This
                              		  table shows the ForwardType values.

ForwardType

Description

Value

FWT_IMMEDIATE

Forward
                                          					 all calls.

0

FWT_BUSY

Forward
                                          					 only when busy.

1

FWT_NO_ANS

Forward
                                          					 after no answer.

2

FWT_BUSY_INT

Forward on
                                          					 busy for internal calls.

3

FWT_BUSY_EXT

Forward on
                                          					 busy for external calls.

4

FWT_NO_ANS_INT

Forward
                                          					 after no answer for internal calls.

5

FWT_NO_ANS_EXT

Forward
                                          					 after no answer for external calls.

6

## TypeOfDevice
                        	 Values

This
                              		  table shows the TypeOfDevice values.

TypeOfDevice

Description

Value

DEVT_STATION

A
                                          					 traditional telephone device, consisting of one or more buttons and one or more
                                          					 lines.

0

DEVT_LINE

A
                                          					 communications interface to one or more stations.

1

DEVT_BUTTON

An
                                          					 instance of a call manipulation point at an individual station.

2

DEVT_ACD

A
                                          					 mechanism that distributes calls.

3

DEVT_TRUNK

A device
                                          					 used to access other switching domains.

4

DEVT_OPERATOR

A device
                                          					 that interacts with a call party to assist in call setup or provide other
                                          					 telecommunications service.

5

DEVT_STATION_ GROUP

Two or
                                          					 more stations used interchangeably or addressed identically.

16

DEVT_LINE_GROUP

A set of
                                          					 communications interfaces to one or more stations.

17

DEVT_BUTTON_ GROUP

Two or
                                          					 more instances of a call manipulation point at an individual station.

18

DEVT_ACD_GROUP

A call
                                          					 distributor device as well as the devices to which it distributes calls.

19

DEVT_TRUNK_ GROUP

A set of
                                          					 trunks providing connectivity to the same place. Individual trunks within the
                                          					 group may be used interchangeably.

20

DEVT_OPERATOR_ GROUP

Two or
                                          					 more operator devices used interchangeably or addressed identically.

21

DEVT_CTI_PORT_ SCCP

A CTI port
                                          					 on a Unified CM device.

22

DEVT_CTI_PORT_SIP

A CTI port
                                          					 on a SIP device.

23

DEVT_OTHER

A device
                                          					 that does not fall into any of the preceding categories.

255

## ClassOfDevice
                        	 Values

This
                              		  table shows the ClassOfDevice values.

ClassOfDevice

Description

Value

DEVC_OTHER

A class of
                                          					 device not covered by the following image, data, or voice classes.

10x

DEVC_IMAGE

A device
                                          					 that is used to make digital data calls involving imaging or high speed circuit
                                          					 switched data in general.

20x

DEVC_DATA

A device
                                          					 that is used to make digital data calls (both circuit switched and packet
                                          					 switched).

40x

DEVC_VOICE

A device
                                          					 that is used to make audio calls.

80x

## CallPlacementType
                        	 Values

This
                              		  table shows the CallPlacementType values.

CallPlacementType

Description

Value

CPT_UNSPECIFIED

Use
                                          					 default call placement.

0

CPT_LINE_CALL

An inside
                                          					 line call.

1

CPT_OUTBOUND

An
                                          					 outbound call.

2

CPT_OUTBOUND_NO_ ACCESS_CODE

An
                                          					 outbound call that will not require an access code.

3

CPT_DIRECT_POSITION

A call
                                          					 placed directly to a specific position.

4

CPT_DIRECT_AGENT

A call
                                          					 placed directly to a specific agent.

5

CPT_SUPERVISOR_ASSIST

A call
                                          					 placed to a supervisor for call handling assistance.

6

## CallMannerType
                        	 Values

This
                              		  table shows the CallMannerType values.

CallMannerType

Description

Value

CMT_UNSPECIFIED

Use
                                          					 default call manner.

0

CMT_POLITE

Attempt
                                          					 the call only if the originating device is idle.

1

CMT_BELLIGERENT

2

CMT_SEMI_POLITE

Attempt
                                          					 the call only if the originating device is idle or is receiving dial tone.

3

CMT_RESERVED

Reserved

4

## CallOption
                        	 Values

This
                              		  table shows the CallOption values.

CallOption

Description

Value

COPT_UNSPECIFIED

No call
                                          					 options specified, use defaults.

0

COPT_CALLING_ AGENT_ONLINE

Attempt
                                          					 the call only if the calling agent is “online” (available to interact with the
                                          					 destination party).

1

COPT_CALLING_ AGENT_RESERVED

Obsolete
                                          					 with DMS-100.

2

COPT_CALLING_ AGENT_NOT_ RESERVED

Obsolete
                                          					 with DMS-100.

3

COPT_CALLING_ AGENT_BUZZ_BASE

Obsolete
                                          					 with DMS-100.

4

COPT_CALLING_ AGENT_BEEP_HSET

Obsolete
                                          					 with DMS-100.

5

COPT_SERVICE_ CIRCUIT_ON

Causes a
                                          					 call classifier to be applied to the call (ACM ECS).

6

## ConsultType
                        	 Values

This
                              		  table shows the ConsultType values.

ConsultType

Description

Value

CT_UNSPECIFIED

Default
                                          					 (consult call).

0

CT_TRANSFER

Consult
                                          					 call prior to transfer.

1

CT_CONFERENCE

Consult
                                          					 call prior to conference.

2

## FacilityType
                        	 Values

This
                              		  table shows the FacilityType values.

FacilityType

Description

Value

FT_UNSPECIFIED

Use
                                          					 default facility type.

0

FT_TRUNK_GROUP

Facility
                                          					 is a trunk group.

1

FT_SKILL_GROUP

Facility
                                          					 is a skill group or split.

2

## AnsweringMachine
                        	 Values

This
                              		  table shows the AnsweringMachine values.

AnsweringMachine

Description

Value

AM_UNSPECIFIED

Use
                                          					 default behavior.

0

AM_CONNECT

Connect
                                          					 call to agent when call is answered by an answering machine.

1

AM_DISCONNECT

Disconnect
                                          					 call when call is answered by an answering machine.

2

AM_NONE

Do not use
                                          					 answering machine detection.

3

AM_NONE_NO_ MODEM

Do not use
                                          					 answering machine detection, but disconnect call if answered by a modem.

4

AM_CONNECT_NO_MODEM

Connect
                                          					 call when call is answered by an answering machine, disconnect call if answered
                                          					 by a modem.

5

## AnswerDetectMode
                        	 Values

This
                              		  table shows the AnswerDetectMode values.

AnswerDetectMode

Description

Value

ADM_UNSPECIFIED

Use
                                          					 default behavior.

0

ADM_VOICE_
                                          					 THRESHOLD

Report
                                          					 call answered by an answering machine when initial voice duration exceeds time
                                          					 threshold.

1

ADM_VOICE_END

Report
                                          					 call answered by an answering machine when initial voice segment ends.

2

ADM_VOICE_END_ DELAY

Report
                                          					 call answered by an answering machine after a fixed delay following the end of
                                          					 the initial voice segment.

3

ADM_VOICE_AND_ BEEP

Report
                                          					 call answered by an answering machine after a beep tone following the end of
                                          					 the initial voice segment (excluding beep tone without any preceding voice).

4

ADM_BEEP

Report
                                          					 call answered by an answering machine after a beep tone following the end of
                                          					 the initial voice segment (including beep tone without any preceding voice).

5

## AgentWorkMode
                        	 Values

This
                              		  table shows the AgentWorkMode values.

AgentWorkMode

Description

Value

AWM_UNSPECIFIED

Use
                                          					 default behavior.

0

AWM_AUTO_IN

Agent
                                          					 automatically becomes available after handling a call.

1

AWM_MANUAL_IN

Agent must
                                          					 explicitly indicate availability after handling a call.

2

RA_CALL_BY_CALL

Remote
                                          					 agent Call by Call mode.

3

RA_NAILED_
                                          					 CONNECTION

Remote
                                          					 agent NailedUp mode.

4

## DestinationCountry
                        	 Values

This
                              		  table shows the DestinationCountry values.

DestinationCountry

Description

Value

DEST_UNSPECIFIED

Unspecified or unknown, use default behavior.

0

DEST_US_AND_ CANADA

Call
                                          					 destination is in the United States or Canada.

1

## CTI Service
                        	 Masks

This
                              		  table shows the CTIService masks.

MaskName

Description

Value

CTI_SERVICE_ DEBUG

Causes all
                                          					 messages exchanged during the current session to be captured to a file for
                                          					 later analysis.

0x80000000

CTI_SERVICE_ CLIENT_ EVENTS

Client
                                          					 receives call and agent state change events associated with a specific ACD
                                          					 phone.

0x00000001

CTI_SERVICE_CALL_ DATA_UPDATE

Client may
                                          					 modify call context data.

0x00000002

CTI_SERVICE_ CLIENT_CONTROL

Client may
                                          					 control calls and agent states associated with a specific ACD phone.

0x00000004

CTI_SERVICE_ CONNECTION_ MONITOR

Establishment and termination of this session cause
                                          					 corresponding Unified CCE Alarm events to be generated.

0x00000008

CTI_SERVICE_ALL_ EVENTS

Client
                                          					 receives all call and agent state change events (associated with any ACD
                                          					 phone).

0x00000010

CTI_SERVICE_ PERIPHERAL_ MONITOR

Client may
                                          					 dynamically add and remove devices and/or calls that it wishes to receive call
                                          					 and agent state events for.

0x00000020

CTI_SERVICE_ CLIENT_MONITOR

Client
                                          					 receives notification when all other CTI client sessions are opened and closed,
                                          					 and may monitor the activity of other CTI client sessions.

0x00000040

CTI_SERVICE_ SUPERVISOR

Client may
                                          					 request supervisor services.

0x00000080

CTI_SERVICE_ SERVER

Client
                                          					 identify itself as server application.

0x00000100

CTI_SERVICE_ AGENT_REPORTING

Client may
                                          					 reporting/routing ARM(Agent Reporting And Management) messages.

0x00000400

CTI_SERVICE_ALL_ TASK_EVENTS

Client
                                          					 receives all task events.

0x00000800

CTI_SERVICE_ TASK_MONITOR

Client
                                          					 receives monitored task events.

0x00001000

CTI_AGENT_STATE_CONTROL_ONLY

Client can
                                          					 change agent state only. Call control is not allowed. If a client requests for
                                          					 CTI_SERVICE_ CLIENT_CONTROL, the server may grant this flag to indicate that
                                          					 only agent state change is allowed.

0x00002000

Unused

0x00004000

CTI_DEVICE_STATE_CONTROL

The
                                          					 client/server wishes to register and get resource state change requests.

0x00008000

CTI_SERVICE_ UPDATE_EVENTS

Requests
                                          					 that this client receive update notification events. (No data)

0x00080000

CTI_SERVICE_ IGNORE_ DUPLICATE_ AGENT_EVENTS

Request to
                                          					 suppress duplicate agent state events.

0x00100000

CTI_SERVICE_ IGNORE_CONF

Do not
                                          					 send confirmations for third party requests.

0x00200000

CTI_SERVICE_ACD_ LINE_ONLY

Request
                                          					 that events for non-ACD lines not be sent. (Unified CCE only)

0x00400000

## Disposition Code
                        	 Values

This
                              		  table shows the Disposition Code values.

Disposition Code

Meaning

1

Abandoned
                                          					 in Network

2

Abandoned
                                          					 in Local Queue

3

Abandoned
                                          					 Ring

4

Abandoned
                                          					 Delay

5

Abandoned
                                          					 Interflow

6

Abandoned
                                          					 Agent Terminal

7

Short

8

Busy

9

Forced
                                          					 Busy

10

Disconnect/drop no answer

11

Disconnect/drop busy

12

Disconnect/drop reorder

13

Disconnect/drop handled primary route

14

Disconnect/drop handled other

15

Redirected

16

Cut
                                          					 Through

17

Intraflow

18

Interflow

19

Ring No
                                          					 Answer

20

Intercept
                                          					 reorder

21

Intercept
                                          					 denial

22

Time Out

23

Voice
                                          					 Energy

24

Non-classified Energy Detected

25

No Cut
                                          					 Through

26

U-Abort

27

Failed
                                          					 Software

28

Blind
                                          					 Transfer

29

Announced
                                          					 Transfer

30

Conferenced

31

Duplicate Transfer

32

Unmonitored Device

33

Answering Machine

34

Network
                                          					 Blind Transfer

35

Task
                                          					 Abandoned in Router

36

Task
                                          					 Abandoned Before Offered

37

Task
                                          					 Abandoned While Offered

38

Normal
                                          					 End Task

39

Can't
                                          					 Obtain Task ID

40

Agent
                                          					 Logged Out During Task

41

Maximum
                                          					 Task Lifetime Exceeded

42

Application Path Went Down

43

Unified
                                          					 CCE Routing Complete

44

Unified
                                          					 CCE Routing Disabled

45

Application Invalid MRD ID

46

Application Invalid Dialogue ID

47

Application Duplicate Dialogue ID

48

Application Invalid Invoke ID

49

Application Invalid Script Selector

50

Application Terminate Dialogue

51

Task
                                          					 Ended During Application Init

52

Called
                                          					 Party Disconnected

53

Partial
                                          					 Call

54

Drop
                                          					 Network Consult

55

Network
                                          					 Consult Transfer

57

Abandon
                                          					 Network Consult

58

Router
                                          					 Requery Before Answer

59

Router
                                          					 Requery After Answer

60

Network
                                          					 Error

61

Network
                                          					 Error Before Answer

62

Network
                                          					 Error After Answer

63

Task
                                          					 Transfer

64

Application Disconnected

65

Task
                                          					 Transferred on Agent Logout

## Agent Service
                        	 Request Masks

This
                              		  table shows the Agent Service Request masks.

DestinationCountry

Description

Value

OUTBOUND_SUPPORT

The agent
                                          					 login can support outbound feature.

0x1

## Silent Monitor
                        	 Status Values

This
                              		  table shows the Silent Monitor Status Values.

DestinationCountry

Description

Value

SILENT_MONITOR_ NONE

Normal
                                          					 call (non-silent monitor call).

0

SILENT_MONITOR_ INITIATOR

Initiator
                                          					 of silent monitor call.

1

SILENT_MONITOR_ TARGET

Monitor
                                          					 target of silent monitor call.

2

## Agent Internal
                        	 States Message Values

This
                              		  table shows the Agent’s Internal States and their Message Values.

State Name

Description

Value

AGENT_STATE_LOGIN

The agent
                                          					 has logged on to the ACD. It does not necessarily indicate that the agent is
                                          					 ready to accept calls.

0

AGENT_STATE_LOGOUT

The agent
                                          					 has logged out of the ACD and cannot accept any additional calls.

1

AGENT_STATE_NOT_READY

The agent
                                          					 is unavailable for any call work.

2

AGENT_STATE_AVAILABLE

The agent
                                          					 is ready to accept a call.

3

AGENT_STATE_TALKING

The agent
                                          					 is currently talking on a call (inbound, outbound, or inside).

4

AGENT_STATE_WORK_NOT_READY

The agent
                                          					 is performing after call work, but will not be ready to receive a call when
                                          					 completed.

5

AGENT_STATE_WORK_READY

The agent
                                          					 is performing after call work, but will be ready to receive a call when
                                          					 completed.

6

AGENT_STATE_BUSY_OTHER

The agent
                                          					 is busy performing a task associated with another active SkillGroup.

7

AGENT_STATE_ACTIVE

The agent
                                          					 state is currently active.

11

## TaskState
                        	 Values

This
                              		  table shows the TaskState values that may appear in SNAPSHOT_TASK_RESP
                              		  messages.

State Name

Description

Value

TASK_STATE_PRE_CALL

Pre Call
                                          					 Message has been sent to client.

0

TASK_STATE_ACTIVE

Task is
                                          					 actively being worked on; Start Task has been received for this task.

1

TASK_STATE_WRAPUP

Wrap up
                                          					 task has been received for this task.

2

TASK_STATE_PAUSED

Task is
                                          					 paused; Pause Task has been received for this task.

3

TASK_STATE_OFFERED

Offer Task
                                          					 has been received for this task.

4

ASK_STATE_INTERRUPTED

Task is
                                          					 interrupted; Agent Interrupt Accepted Ind is received.

5

TASK_STATE_NOT_READY

Not used.

6

TASK_STATE_LOGGED_OUT

Task is
                                          					 terminated.

7

| Status Code | Description | Value |
|---|---|---|
| E_CTI_NO_ERROR | No error occurred. | 0 |
| E_CTI_INVALID_ VERSION | The CTI Server does not support the protocol version number requested by the CTI client. | 1 |
| E_CTI_INVALID_MESSAGE_LENGTH | A message with an invalid message length field was received. | 2 |
| E_CTI_INVALID_ FIELD_TAG | A message with an invalid floating field tag was received. | 3 |
| E_CTI_SESSION_ NOT_OPEN | No session is currently open on the connection. | 4 |
| E_CTI_SESSION_ ALREADY_ OPEN | A session is already open on the connection. | 5 |
| E_CTI_REQUIRED_ DATA_ MISSING | The request did not include one or more floating items that are required. | 6 |
| E_CTI_INVALID_ PERIPHERAL_ID | A message with an invalid PeripheralID value was received. | 7 |
| E_CTI_INVALID_ AGENT_ DATA | The provided agent data item(s) are invalid. | 8 |
| E_CTI_AGENT_NOT_ LOGGED_ON | The indicated agent is not currently logged on. | 9 |
| E_CTI_DEVICE_IN_ USE | The indicated agent teleset is already associated with a different CTI client. | 10 |
| E_CTI_NEW_ SESSION_ OPENED | This session is being terminated due to a new session open request from the client. | 11 |
| E_CTI_FUNCTION_ NOT_ AVAILABLE | A request message was received for a function or service that was not granted to the client. | 12 |
| E_CTI_INVALID_ CALLID | A request message was received with an invalid CallID value. | 13 |
| E_CTI_PROTECTED_ VARIABLE | The CTI client may not update the requested variable. | 14 |
| E_CTI_CTI_SERVER_ OFFLINE | The CTI Server is not able to function normally. The CTI client should close the session upon receipt of this error. If a client using a CTI protocol version less than 24 tries to connect to a standby CTI Server, the client does not support
                                          active-standby functionality and will instead connect to the active side. | 15 |
| E_CTI_TIMEOUT | The CTI Server failed to respond to a request message within the time-out period, or no messages have been received from the
                                          CTI client within the IdleTimeout period. | 16 |
| E_CTI_UNSPECIFIED_FAILURE | An unspecified error occurred. | 17 |
| E_CTI_INVALID_ TIMEOUT | The IdleTimeout field contains a value that is less than 20 seconds (4 times the minimum heartbeat interval of 5 seconds). | 18 |
| E_CTI_INVALID_ SERVICE_MASK | The ServicesRequested field has unused bits set. All unused bit positions must be zero. | 19 |
| E_CTI_INVALID_ CALL_MSG_MASK | The CallMsgMask field has unused bits set. All unused bit positions must be zero. | 20 |
| E_CTI_INVALID_ AGENT_ STATE_ MASK | The AgentStateMask field has unused bits set. All unused bit positions must be zero. | 21 |
| E_CTI_INVALID_ RESERVED_ FIELD | A Reserved field has a non-zero value. | 22 |
| E_CTI_INVALID_ FIELD_ LENGTH | A floating field exceeds the allowable length for that field type. | 23 |
| E_CTI_INVALID_ DIGITS | A STRING field contains characters that are not digits (“0” through “9”). | 24 |
| E_CTI_BAD_ MESSAGE_ FORMAT | The message is improperly constructed. This may be caused by omitted or incorrectly sized fixed message fields. | 25 |
| E_CTI_INVALID_ TAG_FOR_MSG_ TYPE | A floating field tag is present that specifies a field that does not belong in this message type. | 26 |
| E_CTI_INVALID_ DEVICE_ID_ TYPE | A DeviceIDType field contains a value that is not in DeviceIDType Values . | 27 |
| E_CTI_INVALID_ LCL_CONN_ STATE | A LocalConnectionState field contains a value that is not in LocalConnectionState Values . | 28 |
| E_CTI_INVALID_ EVENT_ CAUSE | An EventCause field contains a value that is not in EventCause Values . | 29 |
| E_CTI_INVALID_ NUM_ PARTIES | The NumParties field contains a value that exceeds the maximum (16). | 30 |
| E_CTI_INVALID_ SYS_ EVENT_ID | The SystemEventID field contains a value that is not in SystemEventID Values . | 31 |
| E_CTI_ INCONSISTENT_ AGENT_DATA | The provided agent extension, agent id, and/or agent instrument values are inconsistent with each other. | 32 |
| E_CTI_INVALID_ CONNECTION_ID_ TYPE | A ConnectionDeviceIDType field contains a value that is not in ConnectionDeviceIDType Values . | 33 |
| E_CTI_INVALID_ CALL_TYPE | The CallType field contains a value that is not in CallType Values . | 34 |
| E_CTI_NOT_CALL_ PARTY | A CallDataUpdate or Release Call request specified a call that the client is not a party to. | 35 |
| E_CTI_INVALID_ PASSWORD | The ClientID and Client Password provided in an OPEN_REQ message is incorrect. | 36 |
| E_CTI_CLIENT_ DISCONNECTED | The client TCP/IP connection was disconnected without a CLOSE_REQ. | 37 |
| E_CTI_INVALID_ OBJECT_ STATE | An invalid object state value was provided. | 38 |
| E_CTI_INVALID_ NUM_ SKILL_GROUPS | An invalid NumSkillGroups value was provided. | 39 |
| E_CTI_INVALID_ NUM_LINES | An invalid NumLines value was provided. | 40 |
| E_CTI_INVALID_ LINE_TYPE | An invalid LineType value was provided. | 41 |
| E_CTI_INVALID_ ALLOCATION_STATE | An invalid AllocationState value was provided. | 42 |
| E_CTI_INVALID_ ANSWERING_ MACHINE | An invalid AnsweringMachine value was provided. | 43 |
| E_CTI_INVALID_ CALL_MANNER_ TYPE | An invalid CallMannerType value was provided. | 44 |
| E_CTI_INVALID_ CALL_PLACEMENT_ TYPE | An invalid CallPlacementType value was provided. | 45 |
| E_CTI_INVALID_ CONSULT_ TYPE | An invalid ConsultType value was provided. | 46 |
| E_CTI_INVALID_ FACILITY_ TYPE | An invalid FacilityType value was provided. | 47 |
| E_CTI_INVALID_ MSG_TYPE_ FOR_ VERSION | The provided MessageType is invalid for the opened protocol version. | 48 |
| E_CTI_INVALID_ TAG_FOR_ VERSION | A floating field tag value is invalid for the opened protocol version. | 49 |
| E_CTI_INVALID_ AGENT_WORK_ MODE | An invalid AgentWorkMode value was provided. | 50 |
| E_CTI_INVALID_ CALL_OPTION | An invalid call option value was provided. | 51 |
| E_CTI_INVALID_ DESTINATION_ COUNTRY | An invalid destination country value was provided. | 52 |
| E_CTI_INVALID_ ANSWER_DETECT_ MODE | An invalid answer detect mode value was provided. | 53 |
| E_CTI_MUTUALLY_ EXCLUS_DEVICEID_ TYPES | A peripheral monitor request may not specify both a call and a device. | 54 |
| E_CTI_INVALID_ MONITORID | An invalid monitorID value was provided. | 55 |
| E_CTI_SESSION_ MONITOR_ ALREADY_EXISTS | A requested session monitor was already created. | 56 |
| E_CTI_SESSION_ MONITOR_IS_ CLIENTS | A client may not monitor its own session. | 57 |
| E_CTI_INVALID_ CALL_CONTROL_ MASK | An invalid call control mask value was provided. | 58 |
| E_CTI_INVALID_ FEATURE_MASK | An invalid feature mask value was provided. | 59 |
| E_CTI_INVALID_ TRANSFER_ CONFERENCE_ SETUP_MASK | An invalid transfer conference setup mask value was provided. | 60 |
| E_CTI_INVALID_ ARRAY_INDEX | An invalid named array index value was provided. | 61 |
| E_CTI_INVALID_ CHARACTER | An invalid character value was provided. | 62 |
| E_CTI_CLIENT_NOT_FOUND | There is no open session with a matching ClientID. | 63 |
| E_CTI_SUPERVISOR_NOT_FOUND | The agent’s supervisor is unknown or does not have an open CTI session. | 64 |
| E_CTI_TEAM_NOT_ FOUND | The agent is not a member of an agent team. | 65 |
| E_CTI_NO_CALL_ ACTIVE | The specified agent does not have an active call. | 66 |
| E_CTI_NAMED_ VARIABLE_NOT_ CONFIGURED | The specified named variable is not configured in the Unified CCE. | 67 |
| E_CTI_NAMED_ ARRAY_NOT_ CONFIGURED | The specified named array is not configured in the Unified CCE. | 68 |
| E_CTI_INVALID_ CALL_VARIABLE_ MASK | The specified call variable mask in not valid. | 69 |
| E_CTI_ELEMENT_ NOT_FOUND | An internal error occurred manipulating a named variable or named array element. | 70 |
| E_CTI_INVALID_ DISTRIBUTION_TYPE | The specified distribution type is invalid. | 71 |
| E_CTI_INVALID_ SKILL_GROUP | The specified skill group is invalid. | 72 |
| E_CTI_TOO_MUCH_ DATA | The total combined size of named variables and named arrays may not exceed the limit of 2000 bytes. | 73 |
| E_CTI_VALUE_TOO_LONG | The value of the specified named variable or named array element exceeds the maximum permissible length. | 74 |
| E_CTI_SCALAR_ FUNCTION_ON_ ARRAY | A NamedArray was specified with a NamedVariable tag. | 75 |
| E_CTI_ARRAY_ FUNCTION_ON_ SCALAR | A NamedVariable was specified with a NamedArray tag. | 76 |
| E_CTI_INVALID_ NUM_NAMED_ VARIABLES | The value in the NumNamedVariables field is different than the number of NamedVariable floating fields in the message. | 77 |
| E_CTI_INVALID_ NUM_NAMED_ ARRAYS | The value in the NumNamedArrays field is different than the number of NamedArray floating fields in the message. | 78 |
| E_CTI_INVALID_RTP_DIRECTION | The RTP direction value is invalid. | 79 |
| E_CTI_INVALID_RTP_TYPE | The RTP type value is invalid. | 80 |
| E_CTI_CALLED_ PARTY_DISPOSITION | The called party disposition is invalid. | 81 |
| E_CTI_INVALID_ SUPERVISORY_ ACTION | The supervisory action is invalid. | 82 |
| E_CTI_AGENT_ TEAM_MONITOR_ ALREADY_EXISTS | The agent team monitor already exists. | 83 |
| E_CTI_INVALID_ SERVICE | The ServiceNumber or ServiceID value is invalid. | 84 |
| E_CTI_SERVICE_ CONFLICT | The ServiceNumber and ServiceID values given represent different services. | 85 |
| E_CTI_SKILL_ GROUP_CONFLICT | The SkillGroupNumber/SkillGroupPriority and SkillGroupID values given represent different skill groups. | 86 |
| E_CTI_INVALID_ DEVICE | The specified device is invalid. | 87 |
| E_CTI_INVALID_MR_DOMAIN | Media Routing Domain is invalid. | 88 |
| E_CTI_MONITOR_ ALREADY_EXISTS | Monitor already exists. | 89 |
| E_CTI_MONITOR_ TERMINATED | Monitor has terminated. | 90 |
| E_CTI_INVALID_ TASK_MSG_MASK | The task msg mask is invalid. | 91 |
| E_CTI_SERVER_NOT_MASTER | The server is a standby server. | 92 |
| E_CTI_INVALID_CSD | The CSD Specified is invalid (Unified CCX Only). | 93 |
| E_CTI_JTAPI_CCM_ PROBLEM | Indicates a JTAPI or Unified CM problem. | 94 |
| E_INVALID_CONFIG_ MSG_MASK | Indicates a bad config mask in OPEN_REQ. | 95 |
| E_CTI_AUTO_ CONFIG_RESET | Indicates a configuration change (Unified CCX only). | 96 |
| E_CTI_INVALID_ MONITOR_STATUS | Indicates an invalid monitor. | 97 |
| E_CTI_INVALID_ REQUEST_TYPE | Indicates an invalid request ID type. | 98 |
| E_CTI_INVALID_CLIENT_ FOR_STANDBY | Standby CTIServer returns this error code when: The clients without ServiceMask CTI_SERVICE_ACTIVE_STANDBY (0x02000000) connects. | 107 |
| E_CTI_INVALID_UNIQUE_ INSTANCE_ID | This status code is returned as a failure response for the OPEN_REQ message when the UniqueInstanceID element is present in
                                          the message but its value is empty (0 length). | 108 |
| E_CTI_DUPLICATE_UNIQUE_ INSTANCE_ID | This status code is returned as a failure response for the OPEN_REQ message when there is an existing Client Instance found
                                          with same UniqueInstanceID in the OPEN_REQ message. | 109 |
| E_CTI_SERVER_IN_ MAINTENANCE_MODE | This status code is returned as a failure response for the OPEN_REQ message a client is trying to open a session with CTI
                                          Server when Maintenance Mode is in progress. The code is used to close the client session when the active CTI Server stops for Maintenance Mode. | 110 |

| SystemEventID | Description | Value |
|---|---|---|
| SYS_CENTRAL_ CONTROLLER_ONLINE | The PG has
                                          					 resumed communication with the Unified CCE Central Controller. | 1 |
| SYS_CENTRAL_ CONTROLLER_OFFLINE | The PG is
                                          					 unable to communicate with the Unified CCE Central Controller. | 2 |
| SYS_PERIPHERAL_ ONLINE | A
                                          					 peripheral monitored by the PG has gone online. SystemEventArg1 contains the
                                          					 PeripheralID of the peripheral. | 3 |
| SYS_PERIPHERAL_ OFFLINE | A
                                          					 peripheral monitored by the PG has gone offline. SystemEventArg1 contains the
                                          					 PeripheralID of the peripheral. | 4 |
| SYS_TEXT_FYI | Broadcast
                                          					 of informational “text” floating field. | 5 |
| SYS_PERIPHERAL_ GATEWAY_OFFLINE | The CTI
                                          					 Server is unable to communicate with the Unified CCE Peripheral Gateway. | 6 |
| SYS_CTI_SERVER_ OFFLINE | The local
                                          					 software component is unable to communicate with the CTI Server. | 7 |
| SYS_CTI_SERVER_ ONLINE | The local
                                          					 software component has resumed communication with the CTI Server. | 8 |
| SYS_HALF_HOUR_ CHANGE | The
                                          					 Unified CCE Central Controller time has changed to a new half hour. | 9 |
| SYS_INSTRUMENT_ OUT_OF_SERVICE | An
                                          					 Enterprise Agent device target has been removed from service. SystemEventArg1
                                          					 contains the PeripheralID of the peripheral, and SystemEventText contains the
                                          					 AgentInstrument that was removed from service. | 10 |
| SYS_INSTRUMENT_ BACK_IN_SERVICE | An
                                          					 Enterprise Agent device target has been returned to service. SystemEventArg1
                                          					 contains the PeripheralID of the peripheral, and SystemEventText contains the
                                          					 AgentInstrument that was returned to service. | 11 |

| Constant | Description | Value |
|---|---|---|
| MAX_NUM_CTI_ CLIENTS | The
                                          					 maximum number of CTI clients that can be in a message list. | 16 |
| MAX_NUM_
                                          					 PARTIES | The
                                          					 maximum number of conference call parties that can be in a message list. | 16 |
| MAX_NUM_
                                          					 DEVICES | The
                                          					 maximum number of call devices that can be in a message list. | 16 |
| MAX_NUM_
                                          					 CALLS | The
                                          					 maximum number of calls that can be in a message list. | 16 |
| MAX_NUM_
                                          					 SKILL_GROUPS | The
                                          					 maximum number of skill group fields that can be in a message list. | 20 |
| MAX_NUM_LINES | The
                                          					 maximum number of teleset line fields that can be in a message list. | 10 |
| NULL_
                                          					 CALL_ID | No call ID
                                          					 is supplied. | 0xFFFFFFFF |
| NULL_
                                          					 PERIPHERAL_ID | No
                                          					 peripheral ID is supplied. | 0xFFFFFFFF |
| NULL_SERVICE | No service
                                          					 is supplied. | 0xFFFFFFFF |
| NULL_SKILL_ GROUP | No skill
                                          					 group is supplied. | 0xFFFFFFFF |
| NULL_CALLTYPE | Indicates
                                          					 that no CallType is supplied. | 0xFFFF |

| Floating
                                          					 Field Tag | Using
                                          					 Messages | Value |
|---|---|---|
| CLIENT_ID_TAG | OPEN_REQ | 1 |
| CLIENT_PASSWORD_ TAG | OPEN_REQ | 2 |
| CLIENT_SIGNATURE_ TAG | OPEN_REQ,
                                          					 AGENT_STATE_EVENT | 3 |
| AGENT_EXTENSION_ TAG | OPEN_REQ,
                                          					 OPEN_CONF, AGENT_STATE_EVENT | 4 |
| AGENT_ID_TAG | OPEN_REQ,
                                          					 OPEN_CONF, AGENT_STATE_EVENT, SET_AGENT_STATE_EVENT | 5 |
| AGENT_
                                          					 INSTRUMENT_ TAG | OPEN_REQ,
                                          					 OPEN_CONF, AGENT_STATE_EVENT, QUERY_AGENT_STATE_REQ, SET_AGENT_STATE_REQ,
                                          					 MAKE_CALL_REQ | 6 |
| TEXT_TAG | SYSTEM_EVENT, CLIENT_EVENT_REPORT_REQ, AGENT_TASKS_END_EVENT | 7 |
| ANI_TAG | BEGIN_CALL_EVENT, CALL_ DATA_UPDATE_EVENT, CALL_
                                          					 TRANSLATION_ROUTE_EVENT, SNAPSHOT_CALL_ CONF | 8 |
| UUI_TAG | BEGIN_CALL_EVENT, CALL_DATA_UPDATE_EVENT,
                                          					 CALL_TRANSLATION_ROUTE_ EVENT, CONSULTATION_ CALL_REQ, MAKE_CALL_REQ,
                                          					 TRANSFER_CALL_REQ, SNAPSHOT_CALL_CONF | 9 |
| DNIS_TAG | BEGIN_CALL_EVENT, CALL_ DATA_UPDATE_EVENT, CALL_
                                          					 TRANSLATION_ROUTE_ EVENT, SNAPSHOT_CALL_ CONF | 10 |
| DIALED_NUMBER_ TAG | BEGIN_CALL_EVENT, CALL_DATA_UPDATE_EVENT,
                                          					 CALL_TRANSLATION_ROUTE_ EVENT, CONSULTATION_ CALL_ REQ, MAKE_CALL_REQ,
                                          					 TRANSFER_CALL_REQ, SNAPSHOT_CALL_CONF | 11 |
| CED_TAG | BEGIN_CALL_EVENT, CALL_ DATA_UPDATE_EVENT, CALL_
                                          					 TRANSLATION_ROUTE_ EVENT, SNAPSHOT_CALL_ CONF | 12 |
| CALL_VAR_1_TAG through CALL_VAR_10_TAG | BEGIN_CALL_EVENT, CALL_DATA_UPDATE_EVENT, CALL_TRANSLATION_ROUTE_ EVENT, CONSULTATION_ CALL_REQ, MAKE_CALL_REQ, TRANSFER_CALL_REQ,
                                          SNAPSHOT_CALL_CONF, SNAPSHOT_TASK_RESP , SNAPSHOT_TASK_EVENT | 13-22 |
| CTI_CLIENT_ SIGNATURE_TAG | BEGIN_CALL_EVENT, CALL_DATA_UPDATE_EVENT, SNAPSHOT_CALL_CONF | 23 |
| CTI_CLIENT_ TIMESTAMP_TAG | BEGIN_CALL_EVENT, CALL_DATA_UPDATE_EVENT, SNAPSHOT_CALL_CONF | 24 |
| CONNECTION_ DEVID_ TAG | Any CALL
                                          					 EVENT message, most CLIENT CONTROL messages. | 25 |
| ALERTING_DEVID_ TAG | CALL_DELIVERED_EVENT | 26 |
| CALLING_DEVID_TAG | CALL_DELIVERED_EVENT, CALL_ESTABLISHED_EVENT,
                                          					 CALL_ORIGINATED_EVENT, CALL_SERVICE_INITIATED_EVENT, CALL_QUEUED_EVENT,
                                          					 SET_DEVICE_ATTRIBUTES_REQ | 27 |
| CALLED_DEVID_TAG | CALL_DELIVERED_EVENT, CALL_ESTABLISHED_EVENT,
                                          					 CALL_ORIGINATED_EVENT, CALL_QUEUED_EVENT, | 28 |
| LAST_REDIRECT_ DEVID_TAG | CALL_DELIVERED_EVENT, CALL_ESTABLISHED_EVENT, CALL_QUEUED_EVENT | 29 |
| ANSWERING_DEVID_ TAG | CALL_ESTABLISHED_EVENT | 30 |
| HOLDING_DEVID_ TAG | CALL_HELD_EVENT | 31 |
| RETRIEVING_DEVID_ TAG | CALL_RETRIEVED_EVENT | 32 |
| RELEASING_DEVID_ TAG | CALL_CONNECTION_ CLEARED_EVENT | 33 |
| FAILING_DEVID_TAG | CALL_FAILED_EVENT | 34 |
| PRIMARY_DEVID_ TAG | CALL_CONFERENCED_EVENT, CALL_TRANSFERRED_EVENT | 35 |
| SECONDARY_DEVID_ TAG | CALL_CONFERENCED_EVENT, CALL_TRANSFERRED_EVENT | 36 |
| CONTROLLER_ DEVID_ TAG | CALL_CONFERENCED_EVENT | 37 |
| ADDED_PARTY_ DEVID_TAG | CALL_CONFERENCED_EVENT | 38 |
| PARTY_CALLID_TAG | CALL_CONFERENCED_EVENT, CALL_TRANSFERRED_EVENT,
                                          					 CONFERENCE_CALL_CONF, TRANSFER_CALL_CONF | 39 |
| PARTY_DEVID_TYPE_ TAG | CALL_CONFERENCED_EVENT, CALL_TRANSFERRED_EVENT,
                                          					 CONFERENCE_CALL_CONF, TRANSFER_CALL_CONF | 40 |
| PARTY_DEVID_TAG | CALL_CONFERENCED_EVENT, CALL_TRANSFERRED_EVENT,
                                          					 CONFERENCE_CALL_CONF, TRANSFER_CALL_CONF | 41 |
| TRANSFERRING_ DEVID_TAG | CALL_TRANSFERRED_EVENT | 42 |
| TRANSFERRED_ DEVID_TAG | CALL_TRANSFERRED_EVENT | 43 |
| DIVERTING_DEVID_ TAG | CALL_DIVERTED_EVENT | 44 |
| QUEUE_DEVID_TAG | CALL_QUEUED_EVENT | 45 |
| CALL_WRAPUP_ DATA_ TAG | BEGIN_CALL_EVENT, CALL_DATA_UPDATE_EVENT, SET_CALL_DATA_REQ,
                                          					 CONSULTATION_CALL_REQ, MAKE_CALL_REQ, TRANSFER_CALL_REQ, SNAPSHOT_CALL_CONF | 46 |
| NEW_CONNECTION_ DEVID_TAG | CALL_DATA_UPDATE_EVENT, CONFERENCE_CALL_CONF,
                                          					 CONSULTATION_CALL_CONF, MAKE_CALL_CONF, TRANSFER_CALL_CONF | 47 |
| TRUNK_USED_ DEVID_ TAG | CALL_REACHED_NETWORK_ EVENT | 48 |
| AGENT_PASSWORD_ TAG | SET_AGENT_STATE_REQ | 49 |
| ACTIVE_CONN_ DEVID_ TAG | ALTERNATE_CALL_REQ, CONFERENCE_CALL_REQ, CONSULTATION_CALL_REQ,
                                          					 RECONNECT_CALL_REQ, TRANSFER_CALL_REQ | 50 |
| FACILITY_CODE_TAG | CONSULTATION_CALL_REQ, MAKE_CALL_REQ, TRANSFER_CALL_REQ | 51 |
| OTHER_CONN_ DEVID_ TAG | ALTERNATE_CALL_REQ | 52 |
| HELD_CONN_DEVID_ TAG | CONFERENCE_CALL_REQ, RECONNECT_CALL_REQ, RETRIEVE_CALL_REQ,
                                          					 TRANSFER_CALL_REQ | 53 |
| (reserved) |  | 54-55 |
| CALL_CONN_ CALLID_ TAG | SNAPSHOT_CALL_CONF, SNAPSHOT_DEVICE_CONF | 56 |
| CALL_CONN_DEVID_ TYPE_TAG | SNAPSHOT_CALL_CONF, SNAPSHOT_DEVICE_CONF | 57 |
| CALL_CONN_DEVID_ TAG | SNAPSHOT_CALL_CONF, SNAPSHOT_DEVICE_CONF | 58 |
| CALL_DEVID_TYPE_ TAG | SNAPSHOT_CALL_CONF | 59 |
| CALL_DEVID_TAG | SNAPSHOT_CALL_CONF | 60 |
| CALL_DEV_CONN_ STATE_TAG | SNAPSHOT_CALL_CONF | 61 |
| SKILL_GROUP_ NUMBER_TAG | CALL_QUEUED_EVENT, CALL_DEQUEUED_EVENT, QUERY_AGENT_STATE_CONF | 62 |
| SKILL_GROUP_ID_ TAG | CALL_QUEUED_EVENT, CALL_DEQUEUED_EVENT, QUERY_AGENT_STATE_CONF | 63 |
| SKILL_GROUP_ PRIORITY_TAG | CALL_QUEUED_EVENT, CALL_DEQUEUED_EVENT, QUERY_AGENT_STATE_CONF | 64 |
| SKILL_GROUP_ STATE_ TAG | QUERY_AGENT_STATE_CONF | 65 |
| OBJECT_NAME_TAG | CLIENT_EVENT_REPORT | 66 |
| DTMF_STRING_TAG | SEND_DTMF_SIGNAL_REQ | 67 |
| POSITION_ID_TAG | SET_AGENT_STATE_REQ | 68 |
| SUPERVISOR_ID_TAG | SET_AGENT_STATE_REQ | 69 |
| LINE_HANDLE_TAG | QUERY_DEVICE_INFO_CONF | 70 |
| LINE_TYPE_TAG | QUERY_DEVICE_INFO_CONF | 71 |
| ROUTER_CALL_KEY_ DAY_TAG | BEGIN_CALL_EVENT, CALL_ DATA_UPDATE_EVENT, CALL_
                                          					 TRANSLATION_ROUTE_EVENT, SNAPSHOT_CALL_ CONF | 72 |
| ROUTER_CALL_KEY_ CALLID_TAG | BEGIN_CALL_EVENT, CALL_ DATA_UPDATE_EVENT, CALL_
                                          					 TRANSLATION_ROUTE_EVENT, SNAPSHOT_CALL_ CONF | 73 |
| ROUTER_CALL_KEY_SEQUENCE_NUM_TAG | AGENT_LEGACY_PRE_CALL_EVENT, BEGIN_CALL_EVENT,
                                          					 CALL_DATA_UPDATE_EVENT, CALL_TRANSLATION_ROUTE_EVENT, AGENT_PRE_CALL_EVENT,
                                          					 AGENT_PRE_CALL_ABORT_EVENT | 110 |
| (reserved) |  | 74 |
| CALL_STATE_TAG | SNAPSHOT_DEVICE_CONF | 75 |
| MONITORED_DEVID_TAG | MONITOR_START_REQ | 76 |
| AUTHORIZATION_ CODE_TAG | CONFERENCE_CALL_REQ, CONSULTATION_CALL_REQ, MAKE_CALL_REQ,
                                          					 MAKE_PREDICTIVE_CALL_REQ, TRANSFER_CALL_REQ | 77 |
| ACCOUNT_CODE_TAG | CONFERENCE_CALL_REQ, CONSULTATION_CALL_REQ, MAKE_CALL_REQ,
                                          					 MAKE_PREDICTIVE_CALL_REQ, TRANSFER_CALL_REQ | 78 |
| ORIGINATING_DEVID_TAG | MAKE_PREDICTIVE_CALL_REQ | 79 |
| ORIGINATING_LINE _ID_TAG | MAKE_PREDICTIVE_CALL_REQ | 80 |
| CLIENT_ADDRESS_ TAG | CLIENT_SESSION_OPENED_EVENT, CLIENT_SESSION_CLOSED_EVENT | 81 |
| NAMED_VARIABLE_ TAG | BEGIN_CALL_EVENT, CALL_DATA_UPDATE_EVENT, AGENT_PRE_CALL_EVENT, CALL_TRANSLATION_ROUTE_ EVENT, SET_CALL_DATA_REQ, CONFERENCE_CALL_REQ,
                                          CONSULTATION_CALL_REQ, MAKE_CALL_REQ, MAKE_PREDICTIVE_CALL_REQ, TRANSFER_CALL_REQ, SNAPSHOT_CALL_CONF, REGISTER_VARIABLES_REQ,
                                          SNAPSHOT_TASK_RESP, SNAPSHOT_TASK_EVENT | 82 |
| NAMED_ARRAY_TAG | BEGIN_CALL_EVENT, CALL_DATA_UPDATE_EVENT, AGENT_PRE_CALL_EVENT, CALL_TRANSLATION_ROUTE_ EVENT, SET_CALL_DATA_REQ, CONFERENCE_CALL_REQ,
                                          CONSULTATION_CALL_REQ, MAKE_CALL_REQ, MAKE_PREDICTIVE_CALL_REQ, TRANSFER_CALL_REQ, SNAPSHOT_CALL_CONF, REGISTER_VARIABLES_REQ,
                                          SNAPSHOT_TASK_RESP, SNAPSHOT_TASK_EVENT | 83 |
| CALL_CONTROL_ TABLE_TAG | MAKE_CALL_REQ, MAKE_PREDICTIVE_CALL_REQ, | 84 |
| SUPERVISOR_ INSTRUMENT_TAG | SUPERVISE_CALL_REQ | 85 |
| ATC_AGENT_ID_TAG | AGENT_TEAM_CONFIG_EVENT | 86 |
| AGENT_FLAGS_TAG | AGENT_TEAM_CONFIG_EVENT | 87 |
| ATC_AGENT_STATE_ TAG | AGENT_TEAM_CONFIG_EVENT | 88 |
| ATC_STATE_ DURATION_TAG | AGENT_TEAM_CONFIG_EVENT | 89 |
| AGENT_
                                          					 CONNECTION_DEVID_ TAG | SUPERVISE_CALL_REQ | 90 |
| SUPERVISOR_ CONNECTION_ DEVID_TAG | SUPERVISE_CALL_REQ, | 91 |
| LIST_TEAM_ID_TAG | LIST_AGENT_TEAM_CONF | 92 |
| DEFAULT_DEVICE_ PORT_ADDRESS_TAG | AGENT_DESK_SETTINGS_CONF | 93 |
| SERVICE_NAME_TAG | REGISTER_SERVICE_REQ | 94 |
| CUSTOMER_PHONE_ NUMBER_TAG | SET_CALL_DATA_REQ, CALL_DATA_UPDATE_EVENT | 95 |
| CUSTOMER_ ACCOUNT_NUMBER_TAG | SET_CALL_DATA_REQ, CALL_DATA_UPDATE_EVENT | 96 |
| APP_PATH_ID_TAG | OPEN_REQ | 97 |
| SCRIPT_SELECTOR_TAG | SNAPSHOT_TASK_RESP, SNAPSHOT_TASK_EVENT | 99 |
| APPLICATION_STRING1_TAG | SNAPSHOT_TASK_RESP, SNAPSHOT_TASK_EVENT | 100 |
| APPLICATION_STRING2_TAG | SNAPSHOT_TASK_RESP, SNAPSHOT_TASK_EVENT | 101 |
| ROUTER_CALL_KEY_SEQUENCE_NUM_TAG | AGENT_LEGACY_PRE_CALL_EVENT, BEGIN_CALL_EVENT,
                                          					 CALL_DATA_UPDATE_EVENT, CALL_TRANSLATION_ROUTE_EVENT, AGENT_PRE_CALL_EVENT,
                                          					 AGENT_PRE_CALL_ABORT_EVENT | 110 |
| TRUNK_NUMBER_ TAG | CALL_DELIVERED_EVENT, CALL_ESTABLISHED_EVENT,
                                          					 CALL_REACHED_NETWORK_ EVENT | 121 |
| TRUNK_GROUP_ NUMBER_TAG | CALL_DELIVERED_EVENT, CALL_ESTABLISHED_EVENT,
                                          					 CALL_REACHED_NETWORK_EVENT | 122 |
| EXT_AGENT_STATE_ TAG | AGENT_STATE_EVENT | 123 |
| DEQUEUE_TYPE_TAG | CALL_DEQUEUED_EVENT | 124 |
| SENDING_ADDRESS_ TAG | RTP_STARTED_EVENT, RTP_STOPPED_EVENT | 125 |
| SENDING_PORT_TAG | RTP_STARTED_EVENT RTP_STOPPED_EVENT | 126 |
| Unused |  | 127-128 |
| MAX_QUEUED_TAG | CONFIG_SERVICE_EVENT, CONFIG_DEVICE_EVENT | 129 |
| QUEUE_ID_TAG | QUEUE_UPDATED_EVENT | 130 |
| CUSTOMER_ID_TAG | CONFIG_REQUEST_EVENT | 131 |
| SERVICE_SKILL_ TARGET_ID_TAG | CONFIG_SERVICE_EVENT | 132 |
| PERIPHERAL_NAME_ TAG | CONFIG_SERVICE_EVENT, CONFIG_SKILL_GROUP_EVENT,
                                          					 CONFIG_AGENT_EVENT, CONFIG_DIALED_NUMBER_ EVENT | 133 |
| DESCRIPTION_TAG | CONFIG_SERVICE_EVENT, CONFIG_SKILL_GROUP_EVENT,
                                          					 CONFIG_AGENT_EVENT, CONFIG_DIALED_NUMBER_EVENT CONFIG_MRD_EVENT | 134 |
| SERVICE_MEMBER_ ID_TAG | CONFIG_SKILL_GROUP_EVENT | 135 |
| SERVICE_MEMBER_ PRIORITY_TAG | CONFIG_SKILL_GROUP_EVENT | 136 |
| FIRST_NAME_TAG | CONFIG_AGENT_EVENT | 137 |
| LAST_NAME_TAG | CONFIG_AGENT_EVENT | 138 |
| SKILL_GROUP_TAG | CONFIG_AGENT_EVENT | 139 |
| AGENT_SKILL_ TARGET_ID_TAG | CONFIG_AGENT_EVENT | 141 |
| SERVICE_TAG | CONFIG_DIALED_NUMBER_ EVENT | 142 |
| Reserved |  | 143-149 |
| DURATION_TAG | AGENT_STATE_EVENT | 150 |
| Reserved |  | 151-172 |
| EXTENSION_TAG | CONFIG_SKILL_GROUP_EVENT, CONFIG_SERVICE_EVENT,
                                          					 CONFIG_AGENT_EVENT,CONFIG_DEVICE_EVENT | 173 |
| SERVICE_LEVEL_ THRESHOLD_TAG | CONFIG_SERVICE_EVENT | 174 |
| SERVICE_LEVEL_ TYPE_TAG | CONFIG_SERVICE_EVENT | 175 |
| CONFIG_PARAM_TAG | CONFIG_SKILL_GROUP_EVENT, CONFIG_SERVICE_EVENT | 176 |
| SERVICE_CONFIG_ KEY_TAG | CONFIG_KEY_EVENT, CONFIG_BEGIN_EVENT | 177 |
| SKILL_GROUP_ CONFIG_KEY_TAG | CONFIG_KEY_EVENT, CONFIG_BEGIN_EVENT | 178 |
| AGENT_CONFIG_ KEY_TAG | CONFIG_KEY_EVENT, CONFIG_BEGIN_EVENT | 179 |
| DEVICE_CONFIG_ KEY_TAG | CONFIG_KEY_EVENT, CONFIG_BEGIN_EVENT | 180 |
| Unused |  | 181-182 |
| RECORD_TYPE_TAG | CONFIG_AGENT_EVENT, CONFIG_DEVICE_EVENT, CONFIG_SERVICE_EVENT,
                                          					 CONFIG_SKILL_GROUP_EVENT | 183 |
| PERIPHERAL_ NUMBER_TAG | CONFIG_AGENT_EVENT, CONFIG_DEVICE_EVENT, CONFIG_SERVICE_EVENT,
                                          					 CONFIG_SKILL_GROUP_EVENT | 184 |
| AGENT_SKILL_ TARGET_ID_TAG | CONFIG_AGENT_EVENT | 185 |
| NUM_SERVICE_ MEMBERS_TAG | CONFIG_SERVICE_EVENT | 186 |
| SERVICE_MEMBER_ TAG | CONFIG_SERVICE_EVENT | 187 |
| SERVICE_PRIORITY_ TAG | CONFIG_SERVICE_EVENT | 188 |
| AGENT_TYPE_TAG | CONFIG_AGENT_EVENT | 189 |
| LOGIN_ID_TAG | CONFIG_AGENT_EVENT | 190 |
| NUM_SKILLS_TAG | CONFIG_AGENT_EVENT | 191 |
| SKILL_GROUP_SKILL_TARGET_ID_TAG | CONFIG_SKILL_GROUP_EVENT | 192 |
| SERVICE_ID_TAG | CONFIG_DEVICE_EVENT | 193 |
| AGENT_ID_LONG_ TAG | OPEN_REQ, OPEN_REQ, OPEN_REQ_CONF, AGENT_STATE_EVENT,
                                          					 RTP_STARTED_EVENT, RTP_STOPPED_EVENT, SUPERVISE_CALL_REQ, EMERGENCY_CALL_EVENT,
                                          					 USER_MESSAGE_REQ, SET_AGENT_STATE_REQ, SET_AGENT_STATE_CONF,
                                          					 QUERY_AGENT_STATE_REQ, QUERY_AGENT_STATE_CONF, AGENT_UPDATED_EVENT | 194 |
| DEVICE_TYPE_TAG | CONFIG_DEVICE_EVENT | 195 |
| Unused |  | 196-197 |
| ENABLE_TAG | ROUTE_REGISTER_EVENT | 198 |
| DEVICEID_TAG | ROUTE_REQUEST_EVENT | 199 |
| TIMEOUT_TAG | ROUTE_REQUEST_EVENT | 200 |
| CURRENT_ROUTE_ TAG | ROUTE_REQUEST_EVENT | 201 |
| SECONDARY_ CONNECTION_CALL_ ID | CALL_DELIVERED_EVENT | 202 |
| PRIORITY_QUEUE_ NUMBER_TAG | CALL_QUEUED_EVENT | 203 |
| TEAM_NAME_TAG | TEAM_CONFIG_EVENT | 204 |
| MEMBER_TYPE_TAG | TEAM_CONFIG_EVENT | 205 |
| EVENT_DEVICE_ID_ TAG | SYSTEM_EVENT | 206 |
| LOGIN_NAME_TAG (V11) | CONFIG_AGENT_EVENT | 207 |
| PERIPHERAL_ID_TAG (V11) | CONFIG_AGENT_EVENT, CONFIG_SERVICE_EVENT,
                                          					 CONFIG_SKILL_GROUP_EVENT, CONFIG_DEVICE_EVENT | 208 |
| CALL_TYPE_KEY_ CONFIG_TAG (V11) | CONFIG_KEY_EVENT | 209 |
| CALL_TYPE_ID_TAG (V11) | AGENT_PRE_CALL_EVENT, CONFIG_CALL_TYPE_EVENT, SET_APP_DATA | 210 |
| CUSTOMER_ DEFINITION_ID_TAG (V11) | CONFIG_CALL_TYPE_EVENT | 211 |
| ENTERPRISE_NAME_ TAG (V11) | CONFIG_CALL_TYPE_EVENT CONFIG_MRD_EVENT | 212 |
| OLD_PERIPHERAL_ NUMBER_TAG | CONFIG_SKILL_GROUP_EVENT, CONFIG_CALL_TYPE_EVENT | 213 |
| CUR_LOGIN_ID | CONFIG_AGENT_EVENT | 214 |
| ANI_II_TAG | BEGIN_CALL_EVENT, CALL_TRANSLATION_ROUTE_ EVENT,
                                          					 CALL_DATA_UPDATE, CALL_DELIVERED_EVENT, AGENT_PRE_CALL_EVENT,
                                          					 SET_CALL_DATA_REQ, SNAPSHOT_CALL_REQ, ROUTE_REQUEST_EVENT | 215 |
| MR_DOMAIN_ID_TAG | CONFIG_SKILL_GROUP_EVENT, CONFIG_SERVICE_EVENT CONFIG_MRD_EVENT | 216 |
| CTIOS_CIL_CLIENT_ ID_TAG | SET_CALL_DATA_REQ, ALTERNATE_CALL_REQ, ANSWER_CALL_REQ,
                                          					 CLEAR_CALL_REQ, CLEAR_CONNECTION_REQ, DEFLECT_CALL_REQ, HOLD_CALL_REQ,
                                          					 RECONNECT_CALL_REQ, RETRIEVE_CALL_REQ, SEND_DTMF_SIGNAL_REQ,
                                          					 CHANGE_MONITOR_MASK_REQ, USER_MESSAGE_REQ, SESSION_MONITOR_START_REQ,
                                          					 SESSION_MONITOR_STOP_REQ, MONITOR_AGENT_TEAM_START_REQ, MONITOR_AGENT_TEAM_
                                          					 STOP_REQ, FAILURE_CONF, CONTROL_FAILURE_CONF | 217 |
| SILENT_MONITOR_ STATUS_TAG | SNAPSHOT_DEVICE_CONF | 218 |
| REQUESTING_ DEVICE_ID_TAG | CALL_CLEAR_CONNECTION_REQ | 219 |
| REQUESTING_ DEVICE_ID_ TYPE_TAG | CALL_CLEAR_CONNECTION_REQ | 220 |
| PRE_CALL_INVOKE_ ID_TAG | AGENT_PRE_CALL_EVENT, SET_APP_DATA | 221 |
| ENTERPRISE_ QUEUE_TIME |  | 222 |
| CALL_REFERENCE_ ID_TAG | BEGIN_CALL_EVENT, CALL_DATA_UPDATE_EVENT, CALL_TERMINATION_EVNT,
                                          					 SNAPSHOT_CALL_CONF | 223 |
| MULTI_LINE_AGENT_ CONTROL_TAG | OPEN_CONF | 224 |
| NETWORK_
                                          					 CONTROLLED_TAG | ROUTE_SELECT_EVENT | 225 |
| Used |  | 226-227 |
| NUM_PERIPHERALS_ TAG | OPEN_CONF | 228 |
| COC_CONNECTION_ CALL_ID_TAG | CALL_SERVICE_INITIATED_ EVENT, ROUTE_REQUEST_EVENT, SNAPSHOT
                                          					 _CALL_CONF | 229 |
| COC_CONNECTION_ DEVICE_ID_TYPE_ TAG | CALL_SERVICE_INITIATED_ EVENT, ROUTE_REQUEST_EVENT, SNAPSHOT
                                          					 _CALL_CONF | 230 |
| COC_CONNECTION_ DEVICE_ID_TAG | CALL_SERVICE_INITIATED_ EVENT, ROUTE_REQUEST_EVENT, SNAPSHOT
                                          					 _CALL_CONF | 231 |
| CALL_ORIGINATED_ FROM_TAG | SET_CALL_DATA_REQ | 232 |
| SET_APPDATA_CALLID_TAG |  | 233 |
| CLIENT_SHARE_KEY_TAG |  | 234 |
| AGENT_TEAM_NAME_TAG | AGENT_TEAM_CONFIG_EVENT | 243 |
| DIRECTION_TAG | AGENT_STATE_EVENT | 244 |
| OPTIONS_TAG | ROUTE_REQUEST_EVENT (internal use only for ACMI PIM) | 245 |
| FLT_MRD_ID_TAG | CONFIG_MEDIA_ROUTING_DOMAIN_EVENT (Internal Cisco Use Only) | 246 |
| MEDIA_CLASS_ID_TAG | CONFIG_MEDIA_ROUTING_DOMAIN_EVENT and CONFIG_MEDIA_CLASS_EVENT (Internal Cisco Use Only) | 247 |
| TASK_LIFE_TAG | CONFIG_MEDIA_ROUTING_DOMAIN_EVENT and CONFIG_MEDIA_CLASS_EVENT (Internal Cisco Use Only) | 248 |
| TASK_START_TIMEOUT_TAG | CONFIG_MEDIA_ROUTING_DOMAIN_EVENT and CONFIG_MEDIA_CLASS_EVENT (Internal Cisco Use Only) | 249 |
| MAX_TASK_DURATION_TAG | CONFIG_MEDIA_ROUTING_DOMAIN_EVENT and CONFIG_MEDIA_CLASS_EVENT (Internal Cisco Use Only) CONFIG_MRD_EVENT | 250 |
| INTERRUPTIBLE_TAG | CONFIG_MEDIA_ROUTING_DOMAIN_EVENT (Internal Cisco Use Only) CONFIG_MRD_EVENT | 251 |
| MAX_CALLS_IN_QUEUE_TAG | CONFIG_MEDIA_ROUTING_DOMAIN_EVENT (Internal Cisco Use Only) | 252 |
| MAX_CALLS_IN_QUEUE_PER_CALL_TYPE_TAG | CONFIG_MEDIA_ROUTING_DOMAIN_EVENT (Internal Cisco Use Only) | 253 |
| MAX_TIME_IN_QUEUE_TAG | CONFIG_MEDIA_ROUTING_DOMAIN_EVENT (Internal Cisco Use Only) | 254 |
| INTERNAL_AGENT_STATE_TAG | QUERY_AGENT_STATE_CONF (internal use only for CCX) | 255 |
| Unused |  | 256 |
| SSO_ENABLED_TAG | CONFIG_AGENT_EVENT, SET_AGENT_STATE_REQ | 257 |
| FLT_TASK_ID_TAG | AGENT_TASKS_RESP, AGENT_TASKS_EVENT | 258 |
| FLT_ICM_DISP_TAG | MEDIA_LOGOUT_IND | 259 |
| FLT_APP_DISP_TAG | MEDIA_LOGOUT_IND | 260 |
| NUM_MRDS_TAG | CONFIG_AGENT_EVENT, DESKTOP_CONNECTED_IND | 261 |
| FLT_AGENT_MRD_ID_TAG | CONFIG_AGENT_EVENT, DESKTOP_CONNECTED_IND | 262 |
| FLT_AGENT_MRD_STATE_TAG | CONFIG_AGENT_EVENT | 263 |
| FLT_PRECISION_QUEUE_ID_TAG | CONFIG_SKILL_GROUP_EVENT | 264 |
| FLT_PRECISION_QUEUE_NAME_TAG | CONFIG_SKILL_GROUP_EVENT | 265 |
| MAX_BEYOND_TASK_LIMIT_TAG | AGENT_STATE_EVENT, QUERY_AGENT_STATE_CONF, MEDIA_LOGIN_REQ, AGENT_INIT_REQ | 266 |
| AGENT_DESK_SETTINGS_ID_TAG | CONFIG_AGENT_EVENT | 267 |
| XFER_IN_WHILE_LOGGED_OUT_TAG | OFFER_APPLICATION_TASK_REQ START_APPLICATION_TASK_REQ | 268 |
| PERIPHERAL_CONFIG_KEY_TAG | CONFIG_KEY_EVENT | 269 |
| AGENT_DESK_SETTINGS_CONFIG_KEY_TAG | CONFIG_AGENT_EVENT | 270 |
| CONFIG_PERIPHERAL_ID_TAG | CONFIG_PERIPHERAL_EVENT | 271 |
| DEFAULT_AGENT_DESK_SETTINGS_ID_TAG | CONFIG_PERIPHERAL_EVENT | 272 |
| FLT_DESK_SETTINGS_MASK_TAG | CONFIG_AGENT_DESK_SETTINGS_EVENT | 273 |
| FLT_WRAP_UP_DATA_INCOMING_MODE_TAG | CONFIG_AGENT_DESK_SETTINGS_EVENT | 274 |
| FLT_WRAP_UP_DATA_OUTGOING_MODE_TAG | CONFIG_AGENT_DESK_SETTINGS_EVENT | 275 |
| FLT_LOGOUT_NON_ACTIVITY_TIME_TAG | CONFIG_AGENT_DESK_SETTINGS_EVENT | 276 |
| FLT_QUALITY_RECORDING_RATE_TAG | CONFIG_AGENT_DESK_SETTINGS_EVENT | 277 |
| FLT_RING_NO_ANSWER_TIME_TAG | CONFIG_AGENT_DESK_SETTINGS_EVENT | 278 |
| FLT_SILENT_MONITOR_WARNING_MESSAGE_TAG | CONFIG_AGENT_DESK_SETTINGS_EVENT | 279 |
| FLT_SILENT_MONITOR_AUDIBLE_INDICATION_TAG | CONFIG_AGENT_DESK_SETTINGS_EVENT | 280 |
| FLT_SUPERVISOR_ASSIST_CALL_METHOD_TAG | CONFIG_AGENT_DESK_SETTINGS_EVENT | 281 |
| FLT_EMERGENCY_CALL_METHOD_TAG | CONFIG_AGENT_DESK_SETTINGS_EVENT | 282 |
| FLT_AUTO_RECORD_ON_EMERGENCY_TAG | CONFIG_AGENT_DESK_SETTINGS_EVENT | 283 |
| FLT_RECORDING_MODE_TAG | CONFIG_AGENT_DESK_SETTINGS_EVENT | 284 |
| FLT_WORK_MODE_TIMER_TAG | CONFIG_AGENT_DESK_SETTINGS_EVENT | 285 |
| FLT_RING_NO_ANSWER_DN_ID_TAG | CONFIG_AGENT_DESK_SETTINGS_EVENT | 286 |
| FLT_DEFAULT_DEVICE_PORT_ADDRESS_TAG | CONFIG_AGENT_DESK_SETTINGS_EVENT | 287 |
| DESKTOP_CONNECTED_FLAG_TAG | AGENT_TASKS_REQUEST_EVENT | 288 |
| PLAY_TONE_DIRECTION_TAG | START_NETWORK_RECORDING_REQ | 289 |
| INVOCATION_TYPE_TAG | START_NETWORK_RECORDING_REQ, STOP_NETWORK_RECORDING_REQ | 290 |
| RECORDER_ADDRESS_TAG | NETWORK_RECORDING_TARGET_INFO_EVENT | 291 |
| TERMINAL_NAME_TAG | NETWORK_RECORDING_TARGET_INFO_EVENT | 292 |
| MEDIA_FORKING_DEVICE_NAME_TAG | NETWORK_RECORDING_TARGET_INFO_EVENT | 293 |
| PROTOCOL_REFERENCE_GUID_TAG | NETWORK_RECORDING_TARGET_INFO_EVENT AGENT_PRE_CALL_EVENT | 294 |
| MEDIA_FORKING_CLUSTER_ID_TAG | NETWORK_RECORDING_TARGET_INFO_EVENT | 295 |
| RECORDER_URI_TAG | NETWORK_RECORDING_TARGET_INFO_EVENT | 296 |
| RECORDER_ERROR_MSG_TAG | NETWORK_RECORDING_TARGET_INFO_EVENT | 297 |
| RECORDER_TYPE_TAG | NETWORK_RECORDING_TARGET_INFO_EVENT | 298 |
| RECORDER_STATUS_TAG | NETWORK_RECORDING_TARGET_INFO_EVENT | 299 |
| RECORDING_DEVICE_ID_TAG | NETWORK_RECORDING_STARTED_EVENT, NETWORK_RECORDING_ENDED_EVENT, NETWORK_RECORDING_FAILED_EVENT, NETWORK_RECORDING_TARGET_INFO_EVENT | 300 |
| FLT_TERM_TYPE | CONFIG_TERMINAL_EVENT | 302 |
| FLT_TERM_DEVICE_NAME | CONFIG_TERMINAL_EVENT,CONFIG_AGENT_EVENT, SET_AGENT_STATE_REQ, AGENT_STATE_EVENT | 303 |
| FLT__TERM_TYPE_NAME | CONFIG_TERMINAL_EVENT | 304 |
| FLT_NUM_INSTRUMENTS | CONFIG_TERMINAL_EVENT | 305 |
| ACD_SHARED_LINE_USAGE | AGENT_DESK_SETTINGS_CONF CONFIG_AGENT_DESK_SETTINGS_EVENT | 306 |
| PLAY_ZIP_TONE | AGENT_DESK_SETTINGS_CONF CONFIG_AGENT_DESK_SETTINGS_EVENT | 307 |
|  |  |  |
| FLT_ENABLED_SERVICES | CONFIG_AGENT_SERVICE_EVENT SET_AGENT_SERVICE_DATA_REQ | 309 |
| NUM_OF_ENABLED_SERVICES | CONFIG_AGENT_SERVICE_EVENT SET_AGENT_SERVICE_DATA_REQ | 310 |
| CCAI_CONFIG_ID | AGENT_PRE_CALL_EVENT | 311 |
| MEDIA_TYPE_TAG | MEDIA_LOGIN_REQ | 312 |
| MEDIA_PROVIDER_TAG | MEDIA_LOGIN_REQ | 313 |

| State Name | Description | Value |
|---|---|---|
| AGENT_STATE_ LOGIN | The agent
                                          					 has logged on to the ACD. It does not necessarily indicate that the agent is
                                          					 ready to accept calls. | 0 |
| AGENT_STATE_ LOGOUT | The agent
                                          					 has logged out of the ACD and cannot accept any additional calls. | 1 |
| AGENT_STATE_ NOT_ READY | The agent
                                          					 is unavailable for any call work. | 2 |
| AGENT_STATE_ AVAILABLE | The agent
                                          					 is ready to accept a call. | 3 |
| AGENT_STATE_ TALKING | The agent
                                          					 is currently talking on a call (inbound, outbound, or inside). | 4 |
| AGENT_STATE_ WORK_NOT_READY | The agent
                                          					 is performing after call work, but will not be ready to receive a call when
                                          					 completed. | 5 |
| AGENT_STATE_ WORK_ READY | The agent
                                          					 is performing after call work, and will be ready to receive a call when
                                          					 completed. | 6 |
| AGENT_STATE_ BUSY_ OTHER | The agent
                                          					 is busy performing a task associated with another active SkillGroup. | 7 |
| AGENT_STATE_ RESERVED | The agent
                                          					 is reserved for a call that will arrive at the ACD shortly. | 8 |
| AGENT_STATE_ UNKNOWN | The agent
                                          					 state is currently unknown. | 9 |
| AGENT_STATE_ HOLD | The agent
                                          					 currently has all calls on hold. | 10 |
| AGENT_STATE_ ACTIVE | The agent
                                          					 state is currently active. | 11 |
| AGENT_STATE_ PAUSED | The agent
                                          					 state is currently paused. | 12 |
| AGENT_STATE_ INTERRUPTED | The agent
                                          					 state is currently interrupted. | 13 |
| AGENT_STATE_NOT_ACTIVE | The agent
                                          					 state is currently not active. | 14 |

| PGStatus | Description | Mask Value |
|---|---|---|
| PGS_OPC_DOWN | Communication lost between the CTI Server and the PG’s Open
                                          					 Peripheral Controller (OPC) process. No call or agent state event messages can
                                          					 be sent due to this condition. | 0x00000001 |
| PGS_CC_DOWN | Communication lost between the PG and the Unified CCE Central
                                          					 Controller. Primarily affects translation routing and post-routing, other call
                                          					 and agent event messages can still be sent. | 0x00000002 |
| PGS_PERIPHERAL_OFFLINE | One or
                                          					 more of the peripherals monitored by the PG are offline. | 0x00000004 |
| PGS_CTI_SERVER_OFFLINE | Loss of
                                          					 communication between the CTI Server and the CTI Client. This status code is
                                          					 not reported by a software layer between the CTI Server and the client
                                          					 application. | 0x00000008 |
| PGS_LIMITED_FUNCTION | This
                                          					 status code may be reported by a software layer between the CTI Server and the
                                          					 client application when PGS_CTI_SERVER_ OFFLINE is true to indicate that
                                          					 limited local call control is possible. | 0x00000010 |

| Peripheral
                                          					 Type | Description | Value |
|---|---|---|
| PT_NONE | Not
                                          					 Applicable | 0xffff |
| PT_MERIDIAN | Northern
                                          					 Telecom Meridian ACD | 2 |
| PT_G2 | Lucent G2 | 3 |
| PT_DEFINITY_ECS_ NON_EAS | Lucent
                                          					 DEFINITY ECS (without Expert Agent Selection) | 4 |
| PT_DEFINITY_ECS_ EAS | Lucent
                                          					 DEFINITY ECS (with Expert Agent Selection) | 5 |
| PT_GALAXY | Obsolete | 6 |
| PT_SPECTRUM | Obsolete | 7 |
| PT_VRU | VRU (event
                                          					 type interface) | 8 |
| PT_VRU_POLLED | VRU
                                          					 (polled type interface) | 9 |
| PT_DMS100 | Obsolete | 10 |
| PT_SIEMENS_9006 | Siemens
                                          					 Hicom ACD (9006) | 11 |
| PT_SIEMENS_9005 | Siemens
                                          					 9751 CBX Release 9005 (Rolm 9005) | 12 |
| PT_ALCATEL | Alcatel
                                          					 4400 ACD | 13 |
| PT_NEC_NEAX_2x00 | Obsolete | 14 |
| PT_
                                          					 ACP_1000 | Ericsson
                                          					 ACP1000 | 15 |
| PT_ENTERPRISE_ AGENT | Unified
                                          					 CCE Manager | 17 |
| PT_MD110 | Ericsson
                                          					 MD-110 | 18 |
| PT_MEDIA_ROUTING | Media
                                          					 Routing | 19 |
| PT_GENERIC | Generic | 20 |
| PT_ACMI_CRS | A
                                          					 Gateway PG over Unified CCX | 21 |
| PT_ACMI_IPCC | A
                                          					 Gateway PG over Unified CCE or Unified CCX | 22 |
| PT_ARS | A system
                                          					 using the ARS PG | 24 |
| PT_ACMI_ERS | A system
                                          					 using the ERS PG | 25 |
| PT_ACMI_EXPERT_ADVISOR | Obsolete | 26 |
| {reserved} |  | 27 |

| LocalConnectionState | Description | Value |
|---|---|---|
| LCS_NONE | Not
                                          					 applicable | 0xffff |
| LCS_NULL | No
                                          					 relationship between call and device. | 0 |
| LCS_INITIATE | Device
                                          					 requesting service (“dialing”). | 1 |
| LCS_ALERTING | Device is
                                          					 alerting (“ringing”). | 2 |
| LCS_CONNECT | Device is
                                          					 actively participating in the call. | 3 |
| LCS_HOLD | Device is
                                          					 inactively participating in the call. | 4 |
| LCS_QUEUED | Device is
                                          					 stalled attempting to connect to a call, or a call is stalled attempting to
                                          					 connect to a device. | 5 |
| LCS_FAIL | A
                                          					 device-to-call or call-to-device connection attempt has been aborted. | 6 |

| EventCause | Value |
|---|---|
| CEC_NONE | 0xffff |
| CEC_ACTIVE_MONITOR | 1 |
| CEC_ALTERNATE | 2 |
| CEC_BUSY | 3 |
| CEC_CALL_BACK | 4 |
| CEC_CALL_CANCELLED | 5 |
| CEC_CALL_FORWARD_ALWAYS | 6 |
| CEC_CALL_FORWARD_BUSY | 7 |
| CEC_CALL_FORWARD_NO_ANSWER | 8 |
| CEC_CALL_FORWARD | 9 |
| CEC_CALL_NOT_ANSWERED | 10 |
| CEC_CALL_PICKUP | 11 |
| CEC_CAMP_ON | 12 |
| CEC_DEST_NOT_OBTAINABLE | 13 |
| CEC_DO_NOT_DISTURB | 14 |
| CEC_INCOMPATIBLE_DESTINATION | 15 |
| CEC_INVALID_ACCOUNT_CODE | 16 |
| CEC_KEY_CONFERENCE | 17 |
| CEC_LOCKOUT | 18 |
| CEC_MAINTENANCE | 19 |
| CEC_NETWORK_CONGESTION | 20 |
| CEC_NETWORK_NOT_OBTAINABLE | 21 |
| CEC_NEW_CALL | 22 |
| CEC_NO_AVAILABLE_AGENTS | 23 |
| CEC_OVERRIDE | 24 |
| CEC_PARK | 25 |
| CEC_OVERFLOW | 26 |
| CEC_RECALL | 27 |
| CEC_REDIRECTED | 28 |
| CEC_REORDER_TONE | 29 |
| CEC_RESOURCES_NOT_AVAILABLE | 30 |
| CEC_SILENT_MONITOR | 31 |
| CEC_TRANSFER | 32 |
| CEC_TRUNKS_BUSY | 33 |
| CEC_VOICE_UNIT_INITIATOR | 34 |
| CEC_TIME_OUT | 35 |
| CEC_NEW_CALL_INTERFLOW | 36 |
| CEC_SIMULATION_INIT_REQUEST | 37 |
| CEC_SIMULATION_RESET_REQUEST | 38 |
| CEC_CTI_LINK_DOWN | 39 |
| CEC_PERIPHERAL_RESET_REQUEST | 40 |
| CEC_MD110_CONFERENCE_TRANSFER | 41 |
| CEC_REMAINS_IN_Q | 42 |
| CEC_SUPERVISOR_ASSIST | 43 |
| CEC_EMERGENCY_CALL | 44 |
| CEC_SUPERVISOR_CLEAR | 45 |
| CEC_SUPERVISOR_MONITOR | 46 |
| CEC_SUPERVISOR_WHISPER | 47 |
| CEC_SUPERVISOR_BARGE_IN | 48 |
| CEC_SUPERVISOR_INTERCEPT | 49 |
| CEC_CALL_PARTY_UPDATE_IND | 50 |
| CEC_CONSULT | 51 |
| CEC_NIC_CALL_CLEAR | 52 |
| CEC_DNP | 53 |
| CEC_ ROUTER_REQUERY_BEFORE_ANSWER | 54 |
| CEC_ROUTER_REQUERY_AFTER_ANSWER | 55 |
| CEC_ NETWORK_ERROR | 56 |
| CEC_ NETWORK_ERROR_BEFORE_ANSWER | 57 |
| CEC_NETWORK_ERROR_AFTER_ANSWER | 58 |
| CEC_ GREETING | 59 |
| CEC_ RECORD_AGENT_GREETING | 60 |
| CEC_SNAPSHOT | 61 |
| CEC_ MAX_QUEUE_EXCEEDED | 62 |

| EventCause | Value |
|---|---|
| CECX_ABAND_NETWORK | 1001 |
| CECX_ABAND_LOCAL_QUEUE | 1002 |
| CECX_ABAND_RING | 1003 |
| CECX_ABAND_DELAY | 1004 |
| CECX_ABAND_INTERFLOW | 1005 |
| CECX_ABAND_AGENT_TERMINAL | 1006 |
| CECX_SHORT | 1007 |
| CECX_BUSY | 1008 |
| CECX_FORCED_BUSY | 1009 |
| CECX_DROP_NO_ANSWER | 1010 |
| CECX_DROP_BUSY | 1011 |
| CECX_DROP_REORDER | 1012 |
| CECX_DROP_HANDLED_PRIMARY_ROUTE | 1013 |
| CECX_DROP_HANDLED_OTHER | 1014 |
| CECX_REDIRECTED | 1015 |
| CECX_CUT_THROUGH | 1016 |
| CECX_INTRAFLOW | 1017 |
| CECX_INTERFLOW | 1018 |
| CECX_RING_NO_ANSWER | 1019 |
| CECX_INTERCEPT_REORDER | 1020 |
| CECX_INTERCEPT_DENIAL | 1021 |
| CECX_TIME_OUT | 1022 |
| CECX_VOICE_ENERGY | 1023 |
| CECX_NONCLASSIFIED_ENERGY_DETECT | 1024 |
| CECX_NO_CUT_THROUGH | 1025 |
| CECX_UABORT | 1026 |
| CECX_FAILED_SOFTWARE | 1027 |
| CECX_BLIND_TRANSFER | 1028 |
| CECX_ANNOUNCED_TRANSFER | 1029 |
| CECX_CONFERENCED | 1030 |
| CECX_DUPLICATE_TRANSFER | 1031 |
| CECX_UNMONITORED_DEVICE | 1032 |
| CECX_ANSWERING_MACHINE | 1033 |
| CECX_NETWORK_BLIND_TRANSFER | 1034 |
| CECX_TASK_ABANDONED_IN_ROUTER | 1035 |
| CECX_TASK_ABANDONED_BEFORE_OFFERED | 1036 |
| CECX_TASK_ABANDONED_WHILE_OFFERED | 1037 |
| CECX_NORMAL_END_TASK | 1038 |
| CECX_CANT_OBTAIN_TASK_ID | 1039 |
| CECX_AGENT_LOGGED_OUT_DURING_TASK | 1040 |
| CECX_MAX_TASK_LIFETIME_EXCEEDED | 1041 |
| CECX_APPLICATION_PATH_WENT_DOWN | 1042 |
| CECX_ICM_ROUTING_COMPLETE | 1043 |
| CECX_ICM_ROUTING_DISABLED | 1044 |
| CECX_APPL_INVALID_MRD_ID | 1045 |
| CECX_APPL_INVALID_DIALOGUE_ID | 1056 |
| CECX_APPL_DUPLICATE_DIALOGUE_ID | 1047 |
| CECX_APPL_INVALID_INVOKE_ID | 1048 |
| CECX_APPL_INVALID_SCRIPT_SELECTOR | 1049 |
| CECX_APPL_TERMINATE_DIALOGUE | 1050 |
| CECX_TASK_ENDED_DURING_APP_INIT | 1051 |
| CECX_CALLED_PARTY_DISCONNECTED | 1052 |
| CECX_PARTIAL_CALL | 1053 |
| CECX_DROP_NETWORK_CONSULT | 1054 |
| CECX_NETWORK_CONSULT_TRANSFER | 1055 |
| CECX_NETWORK_CONFERENCE | 1056 |
| CECX_ABAND_NETWORK_CONSULT | 1057 |

| Device ID
                                          					 Type | Description | Value |
|---|---|---|
| DEVID_NONE | No device
                                          					 ID is provided. | 0xffff |
| DEVID_DEVICE_IDENTIFIER | The
                                          					 provided device ID identifies a peripheral teleset (extension). | 0 |
| DEVID_TRUNK_IDENTIFIER | The
                                          					 provided device ID identifies a peripheral Trunk. | 70 |
| DEVID_TRUNK_GROUP_ IDENTIFIER | The
                                          					 provided device ID identifies a peripheral Trunk Group. | 71 |
| DEVID_IP_PHONE_MAC_ IDENTIFIER | The
                                          					 provided device ID identifiers the MAC address of an IP phone (Unified CCX
                                          					 ONLY). | 72 |
| DEVID_CTI_PORT | The
                                          					 provided device ID identifiers a CTI PORT (Unified CCX ONLY). | 73 |
| DEVID_ROUTE_POINT | The
                                          					 provided device ID identifies a ROUTE POINT. | 74 |
| DEVID_EXTERNAL | The
                                          					 provided device ID is an ANI number or some other external identifier. | 75 |
| DEVID_AGENT_DEVICE | The
                                          					 provided device ID is the ID of an AGENT Device (phone). | 76 |
| DEVID_QUEUE | The
                                          					 provided device ID is the ID of a QUEUE. | 77 |
| DEVID_NON_ACD_DEVICE_ IDENTIFIER | The
                                          					 provided device ID identifies a peripheral telset (extension) that is
                                          					 classified as being a non-ACD extension. | 78 |
| DEVID_SHARED_DEVICE_ IDENTIFIER | The
                                          					 provided device ID identifies a peripheral telset (extension) that is
                                          					 classified as being a shared line (0 or more telsets share this extension). | 79 |

| CallType | Description | Value |
|---|---|---|
| CALLTYPE_ACD_IN | Inbound ACD call. In Unified CCE, it indicates that this is a post route request. | 1 |
| CALLTYPE
                                          					 _PREROUTE_ ACD_IN | Translation routed inbound ACD call. | 2 |
| CALLTYPE
                                          					 _PREROUTE_ DIRECT_AGENT | Translation routed call to a specific agent. | 3 |
| CALLTYPE
                                          					 _TRANSFER_IN | Transferred inbound call. | 4 |
| CALLTYPE
                                          					 _OVERFLOW_IN | Overflowed
                                          					 inbound call. | 5 |
| CALLTYPE
                                          					 _OTHER_IN | Inbound
                                          					 call. | 6 |
| CALLTYPE
                                          					 _AUTO_OUT | Automatic
                                          					 out call. | 7 |
| CALLTYPE
                                          					 _AGENT_OUT | Agent out
                                          					 call. | 8 |
| CALLTYPE
                                          					 _OUT | Outbound
                                          					 call. | 9 |
| CALLTYPE
                                          					 _AGENT_INSIDE | Agent
                                          					 inside call. | 10 |
| CALLTYPE
                                          					 _OFFERED | Blind
                                          					 transferred call. | 11 |
| CALLTYPE
                                          					 _CONSULT | Consult
                                          					 call. | 12 |
| CALLTYPE
                                          					 _CONSULT_ OFFERRED | Announced
                                          					 transferred call. | 13 |
| CALLTYPE
                                          					 _CONSULT_ CONFERENCE | Conferenced consult call. | 14 |
| CALLTYPE
                                          					 _CONFERENCE | Conference
                                          					 call. | 15 |
| CALLTYPE_UNMONITORED | Inside or
                                          					 outbound call for which no call events will be received. | 16 |
| CALLTYPE_PREVIEW | Automatic
                                          					 out call in which the agent is given the option to proceed to dial a contact. | 17 |
| CALLTYPE_RESERVATION | Call made
                                          					 to reserve an agent for some other function. | 18 |
| CALLTYPE_ASSIST | Call to
                                          					 supervisor for assistance. | 19 |
| CALLTYPE_EMERGENCY | Emergency
                                          					 call. | 20 |
| CALLTYPE_SUPERVISOR_ MONITOR | Supervisor
                                          					 silently monitoring call. | 21 |
| CALLTYPE_SUPERVISOR_ WHISPER | Supervisor monitoring call, agent can hear supervisor. | 22 |
| CALLTYPE_SUPERVISOR_ BARGEIN | Supervisor conferenced into call. | 23 |
| CALLTYPE_SUPERVISOR_ INTERCEPT | Supervisor replaces agent on call. | 24 |
| CALLTYPE_TASK_ROUTED_BY_ICM | Task
                                          					 routed by Unified CCE | 25 |
| CALLTYPE_TASK_ROUTED_BY_APPLICATION | Task
                                          					 routed by application | 26 |
| CALLTYPE_NON_ACD | Agent
                                          					 call that is a non-ACD routed call. | 27 |
| RESERVATION_PREVIEW | Call
                                          					 type for Outbound Option Reservation calls for Preview mode. | 27 |
| RESERVATION_PREVIEW_DIRECT | Call
                                          					 type for Outbound Option Reservation calls for Direct Preview mode. | 28 |
| RESERVATION_PREDICTIVE | Call
                                          					 type for Outbound Option Reservation calls for Predictive mode and Progressive
                                          					 mode. | 29 |
| RESERVATION_CALLBACK | Call
                                          					 type for Outbound Option Reservation calls for Callback calls. | 30 |
| RESERVATION_PERSONAL_CALLBACK | Call
                                          					 type for Outbound Option Reservation calls for Personal Callback calls. | 31 |
| CUSTOMER_PREVIEW | Call
                                          					 type for Outbound Option Customer calls for Preview mode. | 32 |
| CUSTOMER_PREVIEW_DIRECT | Call
                                          					 type for Outbound Option Customer
                                          					 calls for Direct Preview | 33 |
| CUSTOMER_PREDICTIVE | Call
                                          					 type for Outbound Option Customer calls for Predictive mode and Progreassive
                                          					 modefor agentbased campaigns. | 34 |
| CUSTOMER_CALLBACK | Call
                                          					 type for Outbound Option Customer calls for callback calls. | 35 |
| CUSTOMER_PERSONAL | Call
                                          					 type for Outbound Option Customer calls for personal callback calls. | 36 |
| CUSTOMER_IVR | Call
                                          					 type for Outbound Option Customer calls for Transfer to IVR campaigns. | 37 |
| CALLTYPE_NON_ACD | Agent
                                          					 call that is a non-ACD call. | 38 |
| CALLTYPE_PLAY_AGENT_GREETING | An agent
                                          					 greeting route request. | 39 |
| CALLTYPE_RECORD_AGENT_GREETING | Record
                                          					 agent greeting call initiated by AGENT_GREETING_CONTROL_REQ. | 40 |
| CALLTYPE_VOICE_CALL_BACK | Voice
                                          					 callback using the Agent Request API. | 41 |

| ConnectionDevice IDType | Description | Value |
|---|---|---|
| CONNECTION_ID_ NONE | No
                                          					 ConnectionDeviceID is provided. | 0xffff |
| CONNECTION_ID_ STATIC | The
                                          					 ConnectionDeviceID value is stable over time (between calls). | 0 |
| CONNECTION_ID_ DYNAMIC | The
                                          					 ConnectionDeviceID value is dynamic and may change between calls. | 1 |

| LineType | Description | Value |
|---|---|---|
| LINETYPE_INBOUND_ ACD | Line used
                                          					 for inbound ACD calls. | 0 |
| LINETYPE_OUTBOUND_ACD | Line used
                                          					 for outbound ACD calls. | 1 |
| LINETYPE_INSIDE | Line used
                                          					 for inside calls. | 2 |
| LINETYPE_UNKNOWN | Line used
                                          					 for any purpose. | 3 |
| LINETYPE_SUPERVISOR | Line used
                                          					 for supervisor calls. | 4 |
| LINETYPE_MESSAGE | Line used
                                          					 for voice messages. | 5 |
| LINETYPE_HELP | Line used
                                          					 for assistance. | 6 |
| LINETYPE_OUTBOUND | Line used
                                          					 for outbound non-ACD calls. | 7 |
| LINETYPE_DID | Line used
                                          					 for direct inward dialed calls. | 8 |
| LINETYPE_SILENT_ MONITOR | Line used
                                          					 for silent monitor. | 9 |
| LINETYPE_NON_ACD_IN | Line used
                                          					 for inbound non-ACD calls. | 10 |
| LINETYPE_NON_ACD_OUT | Line used
                                          					 for outbound non-ACD calls. | 11 |

| FailureCode | Description | Value |
|---|---|---|
| CF_GENERIC_UNSPECIFIED | An error
                                          					 has occurred that is not one of the following error types. | 0 |
| CF_GENERIC_OPERATION | An
                                          					 operation error occurred (no specific details available). | 1 |
| CF_REQUEST_ INCOMPATIBLE_WITH_ OBJECT | The
                                          					 request is not compatible with the object. | 2 |
| CF_VALUE_OUT_OF_ RANGE | The
                                          					 parameter has a value that is not in the range defined for the server. | 3 |
| CF_OBJECT_NOT_KNOWN | The
                                          					 parameter has a value that is not known to the server. | 4 |
| CF_INVALID_CALLING_ DEVICE | The
                                          					 calling device is invalid. | 5 |
| CF_INVALID_CALLED_ DEVICE | The called
                                          					 device is invalid | 6 |
| CF_INVALID_FORWARDING_ DESTINATION | The
                                          					 forwarding destination device is invalid. | 7 |
| CF_PRIVILEGE_VIOLATION_ ON_SPECIFIED_DEVICE | The
                                          					 specified device is not authorized for the service. | 8 |
| CF_PRIVILEGE_VIOLATION_ ON_CALLED_DEVICE | The called
                                          					 device is not authorized for the service. | 9 |
| CF_PRIVILEGE_VIOLATION_ ON_CALLING_DEVICE | The
                                          					 calling device is not authorized for the service. | 10 |
| CF_INVALID_CSTA_CALL_ IDENTIFIER | The call
                                          					 identifier is invalid. | 11 |
| CF_INVALID_CSTA_DEVICE_ IDENTIFIER | The device
                                          					 identifier is invalid. | 12 |
| CF_INVALID_CSTA_ CONNECTION_IDENTIFIER | The
                                          					 connection identifier is invalid. | 13 |
| CF_INVALID_DESTINATION | The
                                          					 request specified a destination that is invalid. | 14 |
| CF_INVALID_FEATURE | The
                                          					 request specified a feature that is invalid. | 15 |
| CF_INVALID_ALLOCATION_ STATE | The
                                          					 request specified an allocation state that is invalid. | 16 |
| CF_INVALID_CROSS_REF_ID | The
                                          					 request specified a cross- reference ID that is not in use at this time. | 17 |
| CF_INVALID_OBJECT_TYPE | The
                                          					 request specified an invalid object type. | 18 |
| CF_SECURITY_VIOLATION | Security
                                          					 error (no specific details available). | 19 |
| CF_GENERIC_STATE_ INCOMPATIBILITY | The
                                          					 request is not compatible with the condition of a related device. | 21 |
| CF_INVALID_OBJECT_STATE | The
                                          					 object is in the incorrect state for the request. | 22 |
| CF_INVALID_CONNECTION_ ID_FOR_ACTIVE_CALL | The
                                          					 active connection ID in the request is invalid. | 23 |
| CF_NO_ACTIVE_CALL | There is
                                          					 no active call for the request. | 24 |
| CF_NO_HELD_CALL | There is
                                          					 no held call for the request. | 25 |
| CF_NO_CALL_TO_CLEAR | There is
                                          					 no call associated with the given connection ID. | 26 |
| CF_NO_CONNECTION_TO_ CLEAR | There is
                                          					 no call connection for the given connection ID. | 27 |
| CF_NO_CALL_TO_ANSWER | There is
                                          					 no alerting call to be answered. | 28 |
| CF_NO_CALL_TO_ COMPLETE | There is
                                          					 no active call to be completed. | 29 |
| CF_GENERIC_SYSTEM_ RESOURCE_AVAILABILITY | The
                                          					 request failed due to lack of system resources (no specific details available). | 31 |
| CF_SERVICE_BUSY | The
                                          					 service is temporarily unavailable. | 32 |
| CF_RESOURCE_BUSY | An
                                          					 internal resource is busy. | 33 |
| CF_RESOURCE_OUT_OF_ SERVICE | The
                                          					 service requires a resource that is out of service. | 34 |
| CF_NETWORK_BUSY | The
                                          					 server sub-domain is busy. | 35 |
| CF_NETWORK_OUT_OF_ SERVICE | The
                                          					 server sub-domain is out of service. | 36 |
| CF_
                                          					 OVERALL_MONITOR_ LIMIT_EXCEEDED | The
                                          					 request would exceed the server’s overall resource limits. | 37 |
| CF_CONFERENCE_MEMBER_ LIMIT_EXCEEDED | The
                                          					 request would exceed the server’s limit on the number of conference members. | 38 |
| CF_
                                          					 GENERIC_SUBSCRIBED_ RESOURCE_AVAILABILITY | The
                                          					 request failed due to lack of purchased or contracted resources (no specific
                                          					 details available). | 41 |
| CF_
                                          					 OBJECT_MONITOR_ LIMIT_EXCEEDED | The
                                          					 request would exceed the server’s specific resource limits. | 42 |
| CF_
                                          					 EXTERNAL_TRUNK_ LIMIT_EXCEEDED | The
                                          					 request would exceed the limit of external trunks. | 43 |
| CF_
                                          					 OUTSTANDING_ REQUEST_LIMIT_EXCEEDED | The
                                          					 request would exceed the limit of outstanding requests. | 44 |
| CF_GENERIC_ PERFORMANCE_ MANAGEMENT | The
                                          					 request failed as a performance management mechanism (no specific details
                                          					 available). | 51 |
| CF_PERFORMANCE_LIMIT_ EXCEEDED | The
                                          					 request failed because a performance management limit was exceeded. | 52 |
| CF_
                                          					 SEQUENCE_NUMBER_ VIOLATED | The
                                          					 server has detected an error in the sequence number of the operation. | 61 |
| CF_
                                          					 TIME_STAMP_ VIOLATED | The
                                          					 server has detected an error in the time stamp of the operation. | 62 |
| CF_
                                          					 PAC_VIOLATED | The
                                          					 server has detected an error in the PAC of the operation. | 63 |
| CF_
                                          					 SEAL_VIOLATED | The
                                          					 server has detected an error in the Seal of the operation. | 64 |
| CF_
                                          					 GENERIC_UNSPECIFIED_ REJECTION | The
                                          					 request has been rejected (no specific details available). | 70 |
| CF_
                                          					 GENERIC_OPERATION_ REJECTION | The
                                          					 requested operation has been rejected (no specific details available). | 71 |
| CF_
                                          					 DUPLICATE_ INVOCATION_REJECTION | The
                                          					 request duplicated another request for the same service. | 72 |
| CF_
                                          					 UNRECOGNIZED_ OPERATION_REJECTION | The
                                          					 request specified an unrecognized operation. | 73 |
| CF_MISTYPED_ARGUMENT_ REJECTION | The
                                          					 request contained a parameter of the wrong type for the requested operation. | 74 |
| CF_
                                          					 RESOURCE_LIMITATION_ REJECTION | The
                                          					 request would have exceeded a resource limitation. | 75 |
| CF_
                                          					 ACS_HANDLE_ TERMINATION_REJECTION | The
                                          					 request specified an ACS handle that is no longer in use. | 76 |
| CF_
                                          					 SERVICE_ TERMINATION_REJECTION | The
                                          					 request failed because the required service has been terminated. | 77 |
| CF_
                                          					 REQUEST_TIMEOUT_ REJECTION | The
                                          					 request failed because a timeout limit was exceeded. | 78 |
| CF_REQUESTS_ON_DEVICE_ EXCEEDED_REJECTION | The
                                          					 request would have exceeded the limits of the device. | 79 |

| FailureCode | Description | Value |
|---|---|---|
| CF_INVALID_AGENT_ID_ SPECIFIED | The
                                          						request specified an invalid AgentID. | 256 |
| CF_INVALID_PASSWORD_ SPECIFIED | The
                                          						request specified an invalid agent password. | 257 |
| CF_INVALID_AGENT_ID_ OR_PASSWORD_SPECIFIED | The
                                          						request specified an invalid AgentID and/or invalid agent password. | 258 |
| CF_SPECIFIED_AGENT_ ALREADY_SIGNED_ON | The
                                          						request failed because the specified agent is already logged in. | 259 |
| CF_INVALID_LOGON_ DEVICE_SPECIFIED | The
                                          						request specified an invalid logon device. | 260 |
| CF_INVALID_ANSWERING_ DEVICE_SPECIFIED | The
                                          						request specified an invalid answering device. | 261 |
| CF_INVALID_SKILL_ GROUP_SPECIFIED | The
                                          						request specified an invalid agent skill group. | 262 |
| CF_INVALID_CLASS_OF_ SERVICE_SPECIFIED | The
                                          						request specified an invalid class of service. | 263 |
| CF_INVALID_TEAM_ SPECIFIED | The
                                          						request specified an invalid team. | 264 |
| CF_INVALID_AGENT_ WORKMODE | The
                                          						request specified an invalid agent work mode. | 265 |
| CF_INVALID_AGENT_ REASON_CODE | The
                                          						request specified an invalid agent reason code. | 266 |
| CF_ADJUNCT_SWITCH_ COMM_ERROR | A
                                          						communication error occurred on the datalink between the Unified CCE and the
                                          						ACD. | 267 |
| CF_AGENT_NOT_PARTY_ ON_CALL | The
                                          						specified agent is not a party on the indicated call. | 268 |
| CF_INTERNAL_ PROCESSING_ERROR | An
                                          						internal error occurred in the ACD while processing the request. | 269 |
| CF_TAKE_CALL_CONTROL_ REJECTION | The
                                          						ACD refused an Unified CCE request to take control of a call. | 270 |
| CF_TAKE_DOMAIN_ CONTROL_REJECTION | The
                                          						ACD refused an Unified CCE request to take control of a domain. | 271 |
| CF_REQUESTED_SERVICE_ NOT_REGISTERED | The
                                          						Unified CCE is not registered on the ACD for the requested service. | 272 |
| CF_INVALID_CONSULT_ TYPE | The
                                          						consult type is invalid. | 273 |
| CF_ANSMAP_OR_ ADPARAM_FIELD_NOT_VALID | The
                                          						Ansmap or Asparam field are not valid. | 274 |
| CF_INVALID_CALL_ CONTROL_TABLE_ SPECIFIED | The
                                          						call control table is invalid. | 275 |
| CF_INVALID_DIGITS_ RNATIMEOUT_AMSDELAY_ OR_COUNTRY |  | 276 |
| CF_ANSWER_DETECT_ PORT_UNAVAILABLE |  | 277 |
| CF_VIRTUAL_AGENT_ UNAVAILABLE |  | 278 |
| CF_TAKEBACK_N_XFER_ ROUTE_END |  | 279 |
| CF_WRAPUP_DATA_ REQUIRED |  | 280 |
| CF_REASON_CODE_ REQUIRED |  | 281 |
| CF_INVALID_TRUNK_ID_ SPECIFIED |  | 282 |
| CF_SPECIFIED_EXTENSION_ ALREADY_IN_USE |  | 283 |
| CF_ARBITRARY_CONF_OR_ XFER_NOT_SUPPORTED |  | 284 |
| CF_NETWORK_TRANSFER_OR_ CONSULT |  | 285 |
| CF_NETWORK_TRANSFER_OR_ CONSULT_FAILED |  | 286 |
| CF_DEVICE_RESTRICTED |  | 287 |
| CF_LINE_RESTRICTED |  | 288 |
| CF_AGENT_ACCOUNT_ LOCKED_OUT |  | 289 |
| CF_DROP_ANY_PARTY_NOT_ ENABLED_CTI |  | 290 |
| CF_MAXIMUM_LINE_LIMIT_ EXCEEDED |  | 291 |
| CF_SHARED_LINES_NOT_ SUPPORTED |  | 292 |
| CF_EXTENSION_NOT_UNIQUE |  | 293 |
| CF_UNKNOWN_ INTERFACE_ CTRLR_ID | The
                                          						Interface Controller ID is unknown. | 1001 |
| CF_INVALID_INTERFACE_ CTRLR_TYPE | The
                                          						Interface Controller type is invalid. | 1002 |
| CF_SOFTWARE_REV_NO_ SUPPORTED | The
                                          						current software revision is not supported. | 1003 |
| CF_UNKNOWN_PID | The
                                          						PeripheralID is unknown. | 1004 |
| CF_INVALID_TABLE_ SPECIFIED | An
                                          						invalid table was specified. | 1005 |
| CF_PD_SERVICE_INACTIVE | The
                                          						peripheral data service is not active. | 1006 |
| CF_UNKNOWN_ROUTING_ CLIENT_ID | The
                                          						RoutingClientID is unknown. | 1007 |
| CF_RC_SERVICE_ INACTIVATE | The
                                          						routing client service is not active. | 1008 |
| CF_INVALID_DIALED_ NUMBER | The
                                          						dialed number is invalid. | 1009 |
| CF_INVALID_PARAMETER | A
                                          						parameter in the request is invalid. | 1010 |
| CF_UNKNOWN_ROUTING_ PROBLEM | An
                                          						unspecified error occurred during routing. | 1011 |
| CF_UNSUPPORTED_PD_ MESSAGE_REVISION | The
                                          						requested peripheral data service protocol version is not supported. | 1012 |
| CF_UNSUPPORTED_RC_ MESSAGE_REVISION | The
                                          						requested routing client service protocol version is not supported. | 1013 |
| CF_UNSUPPORTED_IC_ MESSAGE_REVISION | The
                                          						requested interface controller service protocol version is not supported. | 1014 |
| CF_RC_SERVICE_ INACTIVATE_PIM | The
                                          						peripheral interface is not active. | 1015 |
| CF_AGENT_GREETING_CONTROL_OPERATION_FAILURE | This
                                          						error occurs if AGENT_GREETING_CONTROL_REQ request fails. Notes:
                                          						All detailed errors are defined as Peripheral Error Codes. | 1016 |

| AllocationState | Description | Value |
|---|---|---|
| ALLOC_CALL_ DELIVERED | Connect
                                          					 call to originating device when call is delivered (alerting). | 0 |
| ALLOC_CALL_ ESTABLISHED | Connect
                                          					 call to originating device when call is established (answered). | 1 |

| ForwardType | Description | Value |
|---|---|---|
| FWT_IMMEDIATE | Forward
                                          					 all calls. | 0 |
| FWT_BUSY | Forward
                                          					 only when busy. | 1 |
| FWT_NO_ANS | Forward
                                          					 after no answer. | 2 |
| FWT_BUSY_INT | Forward on
                                          					 busy for internal calls. | 3 |
| FWT_BUSY_EXT | Forward on
                                          					 busy for external calls. | 4 |
| FWT_NO_ANS_INT | Forward
                                          					 after no answer for internal calls. | 5 |
| FWT_NO_ANS_EXT | Forward
                                          					 after no answer for external calls. | 6 |

| TypeOfDevice | Description | Value |
|---|---|---|
| DEVT_STATION | A
                                          					 traditional telephone device, consisting of one or more buttons and one or more
                                          					 lines. | 0 |
| DEVT_LINE | A
                                          					 communications interface to one or more stations. | 1 |
| DEVT_BUTTON | An
                                          					 instance of a call manipulation point at an individual station. | 2 |
| DEVT_ACD | A
                                          					 mechanism that distributes calls. | 3 |
| DEVT_TRUNK | A device
                                          					 used to access other switching domains. | 4 |
| DEVT_OPERATOR | A device
                                          					 that interacts with a call party to assist in call setup or provide other
                                          					 telecommunications service. | 5 |
| DEVT_STATION_ GROUP | Two or
                                          					 more stations used interchangeably or addressed identically. | 16 |
| DEVT_LINE_GROUP | A set of
                                          					 communications interfaces to one or more stations. | 17 |
| DEVT_BUTTON_ GROUP | Two or
                                          					 more instances of a call manipulation point at an individual station. | 18 |
| DEVT_ACD_GROUP | A call
                                          					 distributor device as well as the devices to which it distributes calls. | 19 |
| DEVT_TRUNK_ GROUP | A set of
                                          					 trunks providing connectivity to the same place. Individual trunks within the
                                          					 group may be used interchangeably. | 20 |
| DEVT_OPERATOR_ GROUP | Two or
                                          					 more operator devices used interchangeably or addressed identically. | 21 |
| DEVT_CTI_PORT_ SCCP | A CTI port
                                          					 on a Unified CM device. | 22 |
| DEVT_CTI_PORT_SIP | A CTI port
                                          					 on a SIP device. | 23 |
| DEVT_OTHER | A device
                                          					 that does not fall into any of the preceding categories. | 255 |

| ClassOfDevice | Description | Value |
|---|---|---|
| DEVC_OTHER | A class of
                                          					 device not covered by the following image, data, or voice classes. | 10x |
| DEVC_IMAGE | A device
                                          					 that is used to make digital data calls involving imaging or high speed circuit
                                          					 switched data in general. | 20x |
| DEVC_DATA | A device
                                          					 that is used to make digital data calls (both circuit switched and packet
                                          					 switched). | 40x |
| DEVC_VOICE | A device
                                          					 that is used to make audio calls. | 80x |

| CallPlacementType | Description | Value |
|---|---|---|
| CPT_UNSPECIFIED | Use
                                          					 default call placement. | 0 |
| CPT_LINE_CALL | An inside
                                          					 line call. | 1 |
| CPT_OUTBOUND | An
                                          					 outbound call. | 2 |
| CPT_OUTBOUND_NO_ ACCESS_CODE | An
                                          					 outbound call that will not require an access code. | 3 |
| CPT_DIRECT_POSITION | A call
                                          					 placed directly to a specific position. | 4 |
| CPT_DIRECT_AGENT | A call
                                          					 placed directly to a specific agent. | 5 |
| CPT_SUPERVISOR_ASSIST | A call
                                          					 placed to a supervisor for call handling assistance. | 6 |

| CallMannerType | Description | Value |
|---|---|---|
| CMT_UNSPECIFIED | Use
                                          					 default call manner. | 0 |
| CMT_POLITE | Attempt
                                          					 the call only if the originating device is idle. | 1 |
| CMT_BELLIGERENT | This CallManner type is only used with the MAKE_CALL_REQUEST. When an agent in Available state places an outbound call, the
                                          Unified CCE system forcibly changes the agent's state to NotReady with the 50006 reason code. The system changes the agent's
                                          state back to Available after the call ends or if the call fails to connect. For more details on the reason code, see the
                                          the Database Schema Handbook for Cisco Unified ICM/Contact Center Enterprise, Release 12.5(1) at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-technical-reference-list.html | 2 |
| CMT_SEMI_POLITE | Attempt
                                          					 the call only if the originating device is idle or is receiving dial tone. | 3 |
| CMT_RESERVED | Reserved | 4 |

| CallOption | Description | Value |
|---|---|---|
| COPT_UNSPECIFIED | No call
                                          					 options specified, use defaults. | 0 |
| COPT_CALLING_ AGENT_ONLINE | Attempt
                                          					 the call only if the calling agent is “online” (available to interact with the
                                          					 destination party). | 1 |
| COPT_CALLING_ AGENT_RESERVED | Obsolete
                                          					 with DMS-100. | 2 |
| COPT_CALLING_ AGENT_NOT_ RESERVED | Obsolete
                                          					 with DMS-100. | 3 |
| COPT_CALLING_ AGENT_BUZZ_BASE | Obsolete
                                          					 with DMS-100. | 4 |
| COPT_CALLING_ AGENT_BEEP_HSET | Obsolete
                                          					 with DMS-100. | 5 |
| COPT_SERVICE_ CIRCUIT_ON | Causes a
                                          					 call classifier to be applied to the call (ACM ECS). | 6 |

| ConsultType | Description | Value |
|---|---|---|
| CT_UNSPECIFIED | Default
                                          					 (consult call). | 0 |
| CT_TRANSFER | Consult
                                          					 call prior to transfer. | 1 |
| CT_CONFERENCE | Consult
                                          					 call prior to conference. | 2 |

| FacilityType | Description | Value |
|---|---|---|
| FT_UNSPECIFIED | Use
                                          					 default facility type. | 0 |
| FT_TRUNK_GROUP | Facility
                                          					 is a trunk group. | 1 |
| FT_SKILL_GROUP | Facility
                                          					 is a skill group or split. | 2 |

| AnsweringMachine | Description | Value |
|---|---|---|
| AM_UNSPECIFIED | Use
                                          					 default behavior. | 0 |
| AM_CONNECT | Connect
                                          					 call to agent when call is answered by an answering machine. | 1 |
| AM_DISCONNECT | Disconnect
                                          					 call when call is answered by an answering machine. | 2 |
| AM_NONE | Do not use
                                          					 answering machine detection. | 3 |
| AM_NONE_NO_ MODEM | Do not use
                                          					 answering machine detection, but disconnect call if answered by a modem. | 4 |
| AM_CONNECT_NO_MODEM | Connect
                                          					 call when call is answered by an answering machine, disconnect call if answered
                                          					 by a modem. | 5 |

| AnswerDetectMode | Description | Value |
|---|---|---|
| ADM_UNSPECIFIED | Use
                                          					 default behavior. | 0 |
| ADM_VOICE_
                                          					 THRESHOLD | Report
                                          					 call answered by an answering machine when initial voice duration exceeds time
                                          					 threshold. | 1 |
| ADM_VOICE_END | Report
                                          					 call answered by an answering machine when initial voice segment ends. | 2 |
| ADM_VOICE_END_ DELAY | Report
                                          					 call answered by an answering machine after a fixed delay following the end of
                                          					 the initial voice segment. | 3 |
| ADM_VOICE_AND_ BEEP | Report
                                          					 call answered by an answering machine after a beep tone following the end of
                                          					 the initial voice segment (excluding beep tone without any preceding voice). | 4 |
| ADM_BEEP | Report
                                          					 call answered by an answering machine after a beep tone following the end of
                                          					 the initial voice segment (including beep tone without any preceding voice). | 5 |

| AgentWorkMode | Description | Value |
|---|---|---|
| AWM_UNSPECIFIED | Use
                                          					 default behavior. | 0 |
| AWM_AUTO_IN | Agent
                                          					 automatically becomes available after handling a call. | 1 |
| AWM_MANUAL_IN | Agent must
                                          					 explicitly indicate availability after handling a call. | 2 |
| RA_CALL_BY_CALL | Remote
                                          					 agent Call by Call mode. | 3 |
| RA_NAILED_
                                          					 CONNECTION | Remote
                                          					 agent NailedUp mode. | 4 |

| DestinationCountry | Description | Value |
|---|---|---|
| DEST_UNSPECIFIED | Unspecified or unknown, use default behavior. | 0 |
| DEST_US_AND_ CANADA | Call
                                          					 destination is in the United States or Canada. | 1 |

| MaskName | Description | Value |
|---|---|---|
| CTI_SERVICE_ DEBUG | Causes all
                                          					 messages exchanged during the current session to be captured to a file for
                                          					 later analysis. | 0x80000000 |
| CTI_SERVICE_ CLIENT_ EVENTS | Client
                                          					 receives call and agent state change events associated with a specific ACD
                                          					 phone. | 0x00000001 |
| CTI_SERVICE_CALL_ DATA_UPDATE | Client may
                                          					 modify call context data. | 0x00000002 |
| CTI_SERVICE_ CLIENT_CONTROL | Client may
                                          					 control calls and agent states associated with a specific ACD phone. | 0x00000004 |
| CTI_SERVICE_ CONNECTION_ MONITOR | Establishment and termination of this session cause
                                          					 corresponding Unified CCE Alarm events to be generated. | 0x00000008 |
| CTI_SERVICE_ALL_ EVENTS | Client
                                          					 receives all call and agent state change events (associated with any ACD
                                          					 phone). | 0x00000010 |
| CTI_SERVICE_ PERIPHERAL_ MONITOR | Client may
                                          					 dynamically add and remove devices and/or calls that it wishes to receive call
                                          					 and agent state events for. | 0x00000020 |
| CTI_SERVICE_ CLIENT_MONITOR | Client
                                          					 receives notification when all other CTI client sessions are opened and closed,
                                          					 and may monitor the activity of other CTI client sessions. | 0x00000040 |
| CTI_SERVICE_ SUPERVISOR | Client may
                                          					 request supervisor services. | 0x00000080 |
| CTI_SERVICE_ SERVER | Client
                                          					 identify itself as server application. | 0x00000100 |
| CTI_SERVICE_ AGENT_REPORTING | Client may
                                          					 reporting/routing ARM(Agent Reporting And Management) messages. | 0x00000400 |
| CTI_SERVICE_ALL_ TASK_EVENTS | Client
                                          					 receives all task events. | 0x00000800 |
| CTI_SERVICE_ TASK_MONITOR | Client
                                          					 receives monitored task events. | 0x00001000 |
| CTI_AGENT_STATE_CONTROL_ONLY | Client can
                                          					 change agent state only. Call control is not allowed. If a client requests for
                                          					 CTI_SERVICE_ CLIENT_CONTROL, the server may grant this flag to indicate that
                                          					 only agent state change is allowed. | 0x00002000 |
| Unused |  | 0x00004000 |
| CTI_DEVICE_STATE_CONTROL | The
                                          					 client/server wishes to register and get resource state change requests. | 0x00008000 |
| CTI_SERVICE_ UPDATE_EVENTS | Requests
                                          					 that this client receive update notification events. (No data) | 0x00080000 |
| CTI_SERVICE_ IGNORE_ DUPLICATE_ AGENT_EVENTS | Request to
                                          					 suppress duplicate agent state events. | 0x00100000 |
| CTI_SERVICE_ IGNORE_CONF | Do not
                                          					 send confirmations for third party requests. | 0x00200000 |
| CTI_SERVICE_ACD_ LINE_ONLY | Request
                                          					 that events for non-ACD lines not be sent. (Unified CCE only) | 0x00400000 |

| Disposition Code | Meaning |
|---|---|
| 1 | Abandoned
                                          					 in Network |
| 2 | Abandoned
                                          					 in Local Queue |
| 3 | Abandoned
                                          					 Ring |
| 4 | Abandoned
                                          					 Delay |
| 5 | Abandoned
                                          					 Interflow |
| 6 | Abandoned
                                          					 Agent Terminal |
| 7 | Short |
| 8 | Busy |
| 9 | Forced
                                          					 Busy |
| 10 | Disconnect/drop no answer |
| 11 | Disconnect/drop busy |
| 12 | Disconnect/drop reorder |
| 13 | Disconnect/drop handled primary route |
| 14 | Disconnect/drop handled other |
| 15 | Redirected |
| 16 | Cut
                                          					 Through |
| 17 | Intraflow |
| 18 | Interflow |
| 19 | Ring No
                                          					 Answer |
| 20 | Intercept
                                          					 reorder |
| 21 | Intercept
                                          					 denial |
| 22 | Time Out |
| 23 | Voice
                                          					 Energy |
| 24 | Non-classified Energy Detected |
| 25 | No Cut
                                          					 Through |
| 26 | U-Abort |
| 27 | Failed
                                          					 Software |
| 28 | Blind
                                          					 Transfer |
| 29 | Announced
                                          					 Transfer |
| 30 | Conferenced |
| 31 | Duplicate Transfer |
| 32 | Unmonitored Device |
| 33 | Answering Machine |
| 34 | Network
                                          					 Blind Transfer |
| 35 | Task
                                          					 Abandoned in Router |
| 36 | Task
                                          					 Abandoned Before Offered |
| 37 | Task
                                          					 Abandoned While Offered |
| 38 | Normal
                                          					 End Task |
| 39 | Can't
                                          					 Obtain Task ID |
| 40 | Agent
                                          					 Logged Out During Task |
| 41 | Maximum
                                          					 Task Lifetime Exceeded |
| 42 | Application Path Went Down |
| 43 | Unified
                                          					 CCE Routing Complete |
| 44 | Unified
                                          					 CCE Routing Disabled |
| 45 | Application Invalid MRD ID |
| 46 | Application Invalid Dialogue ID |
| 47 | Application Duplicate Dialogue ID |
| 48 | Application Invalid Invoke ID |
| 49 | Application Invalid Script Selector |
| 50 | Application Terminate Dialogue |
| 51 | Task
                                          					 Ended During Application Init |
| 52 | Called
                                          					 Party Disconnected |
| 53 | Partial
                                          					 Call |
| 54 | Drop
                                          					 Network Consult |
| 55 | Network
                                          					 Consult Transfer |
| 57 | Abandon
                                          					 Network Consult |
| 58 | Router
                                          					 Requery Before Answer |
| 59 | Router
                                          					 Requery After Answer |
| 60 | Network
                                          					 Error |
| 61 | Network
                                          					 Error Before Answer |
| 62 | Network
                                          					 Error After Answer |
| 63 | Task
                                          					 Transfer |
| 64 | Application Disconnected |
| 65 | Task
                                          					 Transferred on Agent Logout |

| DestinationCountry | Description | Value |
|---|---|---|
| OUTBOUND_SUPPORT | The agent
                                          					 login can support outbound feature. | 0x1 |

| DestinationCountry | Description | Value |
|---|---|---|
| SILENT_MONITOR_ NONE | Normal
                                          					 call (non-silent monitor call). | 0 |
| SILENT_MONITOR_ INITIATOR | Initiator
                                          					 of silent monitor call. | 1 |
| SILENT_MONITOR_ TARGET | Monitor
                                          					 target of silent monitor call. | 2 |

| State Name | Description | Value |
|---|---|---|
| AGENT_STATE_LOGIN | The agent
                                          					 has logged on to the ACD. It does not necessarily indicate that the agent is
                                          					 ready to accept calls. | 0 |
| AGENT_STATE_LOGOUT | The agent
                                          					 has logged out of the ACD and cannot accept any additional calls. | 1 |
| AGENT_STATE_NOT_READY | The agent
                                          					 is unavailable for any call work. | 2 |
| AGENT_STATE_AVAILABLE | The agent
                                          					 is ready to accept a call. | 3 |
| AGENT_STATE_TALKING | The agent
                                          					 is currently talking on a call (inbound, outbound, or inside). | 4 |
| AGENT_STATE_WORK_NOT_READY | The agent
                                          					 is performing after call work, but will not be ready to receive a call when
                                          					 completed. | 5 |
| AGENT_STATE_WORK_READY | The agent
                                          					 is performing after call work, but will be ready to receive a call when
                                          					 completed. | 6 |
| AGENT_STATE_BUSY_OTHER | The agent
                                          					 is busy performing a task associated with another active SkillGroup. | 7 |
| AGENT_STATE_ACTIVE | The agent
                                          					 state is currently active. | 11 |

| State Name | Description | Value |
|---|---|---|
| TASK_STATE_PRE_CALL | Pre Call
                                          					 Message has been sent to client. | 0 |
| TASK_STATE_ACTIVE | Task is
                                          					 actively being worked on; Start Task has been received for this task. | 1 |
| TASK_STATE_WRAPUP | Wrap up
                                          					 task has been received for this task. | 2 |
| TASK_STATE_PAUSED | Task is
                                          					 paused; Pause Task has been received for this task. | 3 |
| TASK_STATE_OFFERED | Offer Task
                                          					 has been received for this task. | 4 |
| ASK_STATE_INTERRUPTED | Task is
                                          					 interrupted; Agent Interrupt Accepted Ind is received. | 5 |
| TASK_STATE_NOT_READY | Not used. | 6 |
| TASK_STATE_LOGGED_OUT | Task is
                                          					 terminated. | 7 |

| Status Code | Description | Value |
|---|---|---|
| E_CTI_NO_ERROR | No error occurred. | 0 |
| E_CTI_INVALID_ VERSION | The CTI Server does not support the protocol version number requested by the CTI client. | 1 |
| E_CTI_INVALID_MESSAGE_LENGTH | A message with an invalid message length field was received. | 2 |
| E_CTI_INVALID_ FIELD_TAG | A message with an invalid floating field tag was received. | 3 |
| E_CTI_SESSION_ NOT_OPEN | No session is currently open on the connection. | 4 |
| E_CTI_SESSION_ ALREADY_ OPEN | A session is already open on the connection. | 5 |
| E_CTI_REQUIRED_ DATA_ MISSING | The request did not include one or more floating items that are required. | 6 |
| E_CTI_INVALID_ PERIPHERAL_ID | A message with an invalid PeripheralID value was received. | 7 |
| E_CTI_INVALID_ AGENT_ DATA | The provided agent data item(s) are invalid. | 8 |
| E_CTI_AGENT_NOT_ LOGGED_ON | The indicated agent is not currently logged on. | 9 |
| E_CTI_DEVICE_IN_ USE | The indicated agent teleset is already associated with a different CTI client. | 10 |
| E_CTI_NEW_ SESSION_ OPENED | This session is being terminated due to a new session open request from the client. | 11 |
| E_CTI_FUNCTION_ NOT_ AVAILABLE | A request message was received for a function or service that was not granted to the client. | 12 |
| E_CTI_INVALID_ CALLID | A request message was received with an invalid CallID value. | 13 |
| E_CTI_PROTECTED_ VARIABLE | The CTI client may not update the requested variable. | 14 |
| E_CTI_CTI_SERVER_ OFFLINE | The CTI Server is not able to function normally. The CTI client should close the session upon receipt of this error. If a client using a CTI protocol version less than 24 tries to connect to a standby CTI Server, the client does not support
                                          active-standby functionality and will instead connect to the active side. | 15 |
| E_CTI_TIMEOUT | The CTI Server failed to respond to a request message within the time-out period, or no messages have been received from the
                                          CTI client within the IdleTimeout period. | 16 |
| E_CTI_UNSPECIFIED_FAILURE | An unspecified error occurred. | 17 |
| E_CTI_INVALID_ TIMEOUT | The IdleTimeout field contains a value that is less than 20 seconds (4 times the minimum heartbeat interval of 5 seconds). | 18 |
| E_CTI_INVALID_ SERVICE_MASK | The ServicesRequested field has unused bits set. All unused bit positions must be zero. | 19 |
| E_CTI_INVALID_ CALL_MSG_MASK | The CallMsgMask field has unused bits set. All unused bit positions must be zero. | 20 |
| E_CTI_INVALID_ AGENT_ STATE_ MASK | The AgentStateMask field has unused bits set. All unused bit positions must be zero. | 21 |
| E_CTI_INVALID_ RESERVED_ FIELD | A Reserved field has a non-zero value. | 22 |
| E_CTI_INVALID_ FIELD_ LENGTH | A floating field exceeds the allowable length for that field type. | 23 |
| E_CTI_INVALID_ DIGITS | A STRING field contains characters that are not digits (“0” through “9”). | 24 |
| E_CTI_BAD_ MESSAGE_ FORMAT | The message is improperly constructed. This may be caused by omitted or incorrectly sized fixed message fields. | 25 |
| E_CTI_INVALID_ TAG_FOR_MSG_ TYPE | A floating field tag is present that specifies a field that does not belong in this message type. | 26 |
| E_CTI_INVALID_ DEVICE_ID_ TYPE | A DeviceIDType field contains a value that is not in DeviceIDType Values . | 27 |
| E_CTI_INVALID_ LCL_CONN_ STATE | A LocalConnectionState field contains a value that is not in LocalConnectionState Values . | 28 |
| E_CTI_INVALID_ EVENT_ CAUSE | An EventCause field contains a value that is not in EventCause Values . | 29 |
| E_CTI_INVALID_ NUM_ PARTIES | The NumParties field contains a value that exceeds the maximum (16). | 30 |
| E_CTI_INVALID_ SYS_ EVENT_ID | The SystemEventID field contains a value that is not in SystemEventID Values . | 31 |
| E_CTI_ INCONSISTENT_ AGENT_DATA | The provided agent extension, agent id, and/or agent instrument values are inconsistent with each other. | 32 |
| E_CTI_INVALID_ CONNECTION_ID_ TYPE | A ConnectionDeviceIDType field contains a value that is not in ConnectionDeviceIDType Values . | 33 |
| E_CTI_INVALID_ CALL_TYPE | The CallType field contains a value that is not in CallType Values . | 34 |
| E_CTI_NOT_CALL_ PARTY | A CallDataUpdate or Release Call request specified a call that the client is not a party to. | 35 |
| E_CTI_INVALID_ PASSWORD | The ClientID and Client Password provided in an OPEN_REQ message is incorrect. | 36 |
| E_CTI_CLIENT_ DISCONNECTED | The client TCP/IP connection was disconnected without a CLOSE_REQ. | 37 |
| E_CTI_INVALID_ OBJECT_ STATE | An invalid object state value was provided. | 38 |
| E_CTI_INVALID_ NUM_ SKILL_GROUPS | An invalid NumSkillGroups value was provided. | 39 |
| E_CTI_INVALID_ NUM_LINES | An invalid NumLines value was provided. | 40 |
| E_CTI_INVALID_ LINE_TYPE | An invalid LineType value was provided. | 41 |
| E_CTI_INVALID_ ALLOCATION_STATE | An invalid AllocationState value was provided. | 42 |
| E_CTI_INVALID_ ANSWERING_ MACHINE | An invalid AnsweringMachine value was provided. | 43 |
| E_CTI_INVALID_ CALL_MANNER_ TYPE | An invalid CallMannerType value was provided. | 44 |
| E_CTI_INVALID_ CALL_PLACEMENT_ TYPE | An invalid CallPlacementType value was provided. | 45 |
| E_CTI_INVALID_ CONSULT_ TYPE | An invalid ConsultType value was provided. | 46 |
| E_CTI_INVALID_ FACILITY_ TYPE | An invalid FacilityType value was provided. | 47 |
| E_CTI_INVALID_ MSG_TYPE_ FOR_ VERSION | The provided MessageType is invalid for the opened protocol version. | 48 |
| E_CTI_INVALID_ TAG_FOR_ VERSION | A floating field tag value is invalid for the opened protocol version. | 49 |
| E_CTI_INVALID_ AGENT_WORK_ MODE | An invalid AgentWorkMode value was provided. | 50 |
| E_CTI_INVALID_ CALL_OPTION | An invalid call option value was provided. | 51 |
| E_CTI_INVALID_ DESTINATION_ COUNTRY | An invalid destination country value was provided. | 52 |
| E_CTI_INVALID_ ANSWER_DETECT_ MODE | An invalid answer detect mode value was provided. | 53 |
| E_CTI_MUTUALLY_ EXCLUS_DEVICEID_ TYPES | A peripheral monitor request may not specify both a call and a device. | 54 |
| E_CTI_INVALID_ MONITORID | An invalid monitorID value was provided. | 55 |
| E_CTI_SESSION_ MONITOR_ ALREADY_EXISTS | A requested session monitor was already created. | 56 |
| E_CTI_SESSION_ MONITOR_IS_ CLIENTS | A client may not monitor its own session. | 57 |
| E_CTI_INVALID_ CALL_CONTROL_ MASK | An invalid call control mask value was provided. | 58 |
| E_CTI_INVALID_ FEATURE_MASK | An invalid feature mask value was provided. | 59 |
| E_CTI_INVALID_ TRANSFER_ CONFERENCE_ SETUP_MASK | An invalid transfer conference setup mask value was provided. | 60 |
| E_CTI_INVALID_ ARRAY_INDEX | An invalid named array index value was provided. | 61 |
| E_CTI_INVALID_ CHARACTER | An invalid character value was provided. | 62 |
| E_CTI_CLIENT_NOT_FOUND | There is no open session with a matching ClientID. | 63 |
| E_CTI_SUPERVISOR_NOT_FOUND | The agent’s supervisor is unknown or does not have an open CTI session. | 64 |
| E_CTI_TEAM_NOT_ FOUND | The agent is not a member of an agent team. | 65 |
| E_CTI_NO_CALL_ ACTIVE | The specified agent does not have an active call. | 66 |
| E_CTI_NAMED_ VARIABLE_NOT_ CONFIGURED | The specified named variable is not configured in the Unified CCE. | 67 |
| E_CTI_NAMED_ ARRAY_NOT_ CONFIGURED | The specified named array is not configured in the Unified CCE. | 68 |
| E_CTI_INVALID_ CALL_VARIABLE_ MASK | The specified call variable mask in not valid. | 69 |
| E_CTI_ELEMENT_ NOT_FOUND | An internal error occurred manipulating a named variable or named array element. | 70 |
| E_CTI_INVALID_ DISTRIBUTION_TYPE | The specified distribution type is invalid. | 71 |
| E_CTI_INVALID_ SKILL_GROUP | The specified skill group is invalid. | 72 |
| E_CTI_TOO_MUCH_ DATA | The total combined size of named variables and named arrays may not exceed the limit of 2000 bytes. | 73 |
| E_CTI_VALUE_TOO_LONG | The value of the specified named variable or named array element exceeds the maximum permissible length. | 74 |
| E_CTI_SCALAR_ FUNCTION_ON_ ARRAY | A NamedArray was specified with a NamedVariable tag. | 75 |
| E_CTI_ARRAY_ FUNCTION_ON_ SCALAR | A NamedVariable was specified with a NamedArray tag. | 76 |
| E_CTI_INVALID_ NUM_NAMED_ VARIABLES | The value in the NumNamedVariables field is different than the number of NamedVariable floating fields in the message. | 77 |
| E_CTI_INVALID_ NUM_NAMED_ ARRAYS | The value in the NumNamedArrays field is different than the number of NamedArray floating fields in the message. | 78 |
| E_CTI_INVALID_RTP_DIRECTION | The RTP direction value is invalid. | 79 |
| E_CTI_INVALID_RTP_TYPE | The RTP type value is invalid. | 80 |
| E_CTI_CALLED_ PARTY_DISPOSITION | The called party disposition is invalid. | 81 |
| E_CTI_INVALID_ SUPERVISORY_ ACTION | The supervisory action is invalid. | 82 |
| E_CTI_AGENT_ TEAM_MONITOR_ ALREADY_EXISTS | The agent team monitor already exists. | 83 |
| E_CTI_INVALID_ SERVICE | The ServiceNumber or ServiceID value is invalid. | 84 |
| E_CTI_SERVICE_ CONFLICT | The ServiceNumber and ServiceID values given represent different services. | 85 |
| E_CTI_SKILL_ GROUP_CONFLICT | The SkillGroupNumber/SkillGroupPriority and SkillGroupID values given represent different skill groups. | 86 |
| E_CTI_INVALID_ DEVICE | The specified device is invalid. | 87 |
| E_CTI_INVALID_MR_DOMAIN | Media Routing Domain is invalid. | 88 |
| E_CTI_MONITOR_ ALREADY_EXISTS | Monitor already exists. | 89 |
| E_CTI_MONITOR_ TERMINATED | Monitor has terminated. | 90 |
| E_CTI_INVALID_ TASK_MSG_MASK | The task msg mask is invalid. | 91 |
| E_CTI_SERVER_NOT_MASTER | The server is a standby server. | 92 |
| E_CTI_INVALID_CSD | The CSD Specified is invalid (Unified CCX Only). | 93 |
| E_CTI_JTAPI_CCM_ PROBLEM | Indicates a JTAPI or Unified CM problem. | 94 |
| E_INVALID_CONFIG_ MSG_MASK | Indicates a bad config mask in OPEN_REQ. | 95 |
| E_CTI_AUTO_ CONFIG_RESET | Indicates a configuration change (Unified CCX only). | 96 |
| E_CTI_INVALID_ MONITOR_STATUS | Indicates an invalid monitor. | 97 |
| E_CTI_INVALID_ REQUEST_TYPE | Indicates an invalid request ID type. | 98 |
| E_CTI_INVALID_CLIENT_ FOR_STANDBY | Standby CTIServer returns this error code when: The clients without ServiceMask CTI_SERVICE_ACTIVE_STANDBY (0x02000000) connects. | 107 |
| E_CTI_INVALID_UNIQUE_ INSTANCE_ID | This status code is returned as a failure response for the OPEN_REQ message when the UniqueInstanceID element is present in
                                          the message but its value is empty (0 length). | 108 |
| E_CTI_DUPLICATE_UNIQUE_ INSTANCE_ID | This status code is returned as a failure response for the OPEN_REQ message when there is an existing Client Instance found
                                          with same UniqueInstanceID in the OPEN_REQ message. | 109 |
| E_CTI_SERVER_IN_ MAINTENANCE_MODE | This status code is returned as a failure response for the OPEN_REQ message a client is trying to open a session with CTI
                                          Server when Maintenance Mode is in progress. The code is used to close the client session when the active CTI Server stops for Maintenance Mode. | 110 |

| SystemEventID | Description | Value |
|---|---|---|
| SYS_CENTRAL_ CONTROLLER_ONLINE | The PG has
                                          					 resumed communication with the Unified CCE Central Controller. | 1 |
| SYS_CENTRAL_ CONTROLLER_OFFLINE | The PG is
                                          					 unable to communicate with the Unified CCE Central Controller. | 2 |
| SYS_PERIPHERAL_ ONLINE | A
                                          					 peripheral monitored by the PG has gone online. SystemEventArg1 contains the
                                          					 PeripheralID of the peripheral. | 3 |
| SYS_PERIPHERAL_ OFFLINE | A
                                          					 peripheral monitored by the PG has gone offline. SystemEventArg1 contains the
                                          					 PeripheralID of the peripheral. | 4 |
| SYS_TEXT_FYI | Broadcast
                                          					 of informational “text” floating field. | 5 |
| SYS_PERIPHERAL_ GATEWAY_OFFLINE | The CTI
                                          					 Server is unable to communicate with the Unified CCE Peripheral Gateway. | 6 |
| SYS_CTI_SERVER_ OFFLINE | The local
                                          					 software component is unable to communicate with the CTI Server. | 7 |
| SYS_CTI_SERVER_ ONLINE | The local
                                          					 software component has resumed communication with the CTI Server. | 8 |
| SYS_HALF_HOUR_ CHANGE | The
                                          					 Unified CCE Central Controller time has changed to a new half hour. | 9 |
| SYS_INSTRUMENT_ OUT_OF_SERVICE | An
                                          					 Enterprise Agent device target has been removed from service. SystemEventArg1
                                          					 contains the PeripheralID of the peripheral, and SystemEventText contains the
                                          					 AgentInstrument that was removed from service. | 10 |
| SYS_INSTRUMENT_ BACK_IN_SERVICE | An
                                          					 Enterprise Agent device target has been returned to service. SystemEventArg1
                                          					 contains the PeripheralID of the peripheral, and SystemEventText contains the
                                          					 AgentInstrument that was returned to service. | 11 |

| Constant | Description | Value |
|---|---|---|
| MAX_NUM_CTI_ CLIENTS | The
                                          					 maximum number of CTI clients that can be in a message list. | 16 |
| MAX_NUM_
                                          					 PARTIES | The
                                          					 maximum number of conference call parties that can be in a message list. | 16 |
| MAX_NUM_
                                          					 DEVICES | The
                                          					 maximum number of call devices that can be in a message list. | 16 |
| MAX_NUM_
                                          					 CALLS | The
                                          					 maximum number of calls that can be in a message list. | 16 |
| MAX_NUM_
                                          					 SKILL_GROUPS | The
                                          					 maximum number of skill group fields that can be in a message list. | 20 |
| MAX_NUM_LINES | The
                                          					 maximum number of teleset line fields that can be in a message list. | 10 |
| NULL_
                                          					 CALL_ID | No call ID
                                          					 is supplied. | 0xFFFFFFFF |
| NULL_
                                          					 PERIPHERAL_ID | No
                                          					 peripheral ID is supplied. | 0xFFFFFFFF |
| NULL_SERVICE | No service
                                          					 is supplied. | 0xFFFFFFFF |
| NULL_SKILL_ GROUP | No skill
                                          					 group is supplied. | 0xFFFFFFFF |
| NULL_CALLTYPE | Indicates
                                          					 that no CallType is supplied. | 0xFFFF |

| Floating
                                          					 Field Tag | Using
                                          					 Messages | Value |
|---|---|---|
| CLIENT_ID_TAG | OPEN_REQ | 1 |
| CLIENT_PASSWORD_ TAG | OPEN_REQ | 2 |
| CLIENT_SIGNATURE_ TAG | OPEN_REQ,
                                          					 AGENT_STATE_EVENT | 3 |
| AGENT_EXTENSION_ TAG | OPEN_REQ,
                                          					 OPEN_CONF, AGENT_STATE_EVENT | 4 |
| AGENT_ID_TAG | OPEN_REQ,
                                          					 OPEN_CONF, AGENT_STATE_EVENT, SET_AGENT_STATE_EVENT | 5 |
| AGENT_
                                          					 INSTRUMENT_ TAG | OPEN_REQ,
                                          					 OPEN_CONF, AGENT_STATE_EVENT, QUERY_AGENT_STATE_REQ, SET_AGENT_STATE_REQ,
                                          					 MAKE_CALL_REQ | 6 |
| TEXT_TAG | SYSTEM_EVENT, CLIENT_EVENT_REPORT_REQ, AGENT_TASKS_END_EVENT | 7 |
| ANI_TAG | BEGIN_CALL_EVENT, CALL_ DATA_UPDATE_EVENT, CALL_
                                          					 TRANSLATION_ROUTE_EVENT, SNAPSHOT_CALL_ CONF | 8 |
| UUI_TAG | BEGIN_CALL_EVENT, CALL_DATA_UPDATE_EVENT,
                                          					 CALL_TRANSLATION_ROUTE_ EVENT, CONSULTATION_ CALL_REQ, MAKE_CALL_REQ,
                                          					 TRANSFER_CALL_REQ, SNAPSHOT_CALL_CONF | 9 |
| DNIS_TAG | BEGIN_CALL_EVENT, CALL_ DATA_UPDATE_EVENT, CALL_
                                          					 TRANSLATION_ROUTE_ EVENT, SNAPSHOT_CALL_ CONF | 10 |
| DIALED_NUMBER_ TAG | BEGIN_CALL_EVENT, CALL_DATA_UPDATE_EVENT,
                                          					 CALL_TRANSLATION_ROUTE_ EVENT, CONSULTATION_ CALL_ REQ, MAKE_CALL_REQ,
                                          					 TRANSFER_CALL_REQ, SNAPSHOT_CALL_CONF | 11 |
| CED_TAG | BEGIN_CALL_EVENT, CALL_ DATA_UPDATE_EVENT, CALL_
                                          					 TRANSLATION_ROUTE_ EVENT, SNAPSHOT_CALL_ CONF | 12 |
| CALL_VAR_1_TAG through CALL_VAR_10_TAG | BEGIN_CALL_EVENT, CALL_DATA_UPDATE_EVENT, CALL_TRANSLATION_ROUTE_ EVENT, CONSULTATION_ CALL_REQ, MAKE_CALL_REQ, TRANSFER_CALL_REQ,
                                          SNAPSHOT_CALL_CONF, SNAPSHOT_TASK_RESP , SNAPSHOT_TASK_EVENT | 13-22 |
| CTI_CLIENT_ SIGNATURE_TAG | BEGIN_CALL_EVENT, CALL_DATA_UPDATE_EVENT, SNAPSHOT_CALL_CONF | 23 |
| CTI_CLIENT_ TIMESTAMP_TAG | BEGIN_CALL_EVENT, CALL_DATA_UPDATE_EVENT, SNAPSHOT_CALL_CONF | 24 |
| CONNECTION_ DEVID_ TAG | Any CALL
                                          					 EVENT message, most CLIENT CONTROL messages. | 25 |
| ALERTING_DEVID_ TAG | CALL_DELIVERED_EVENT | 26 |
| CALLING_DEVID_TAG | CALL_DELIVERED_EVENT, CALL_ESTABLISHED_EVENT,
                                          					 CALL_ORIGINATED_EVENT, CALL_SERVICE_INITIATED_EVENT, CALL_QUEUED_EVENT,
                                          					 SET_DEVICE_ATTRIBUTES_REQ | 27 |
| CALLED_DEVID_TAG | CALL_DELIVERED_EVENT, CALL_ESTABLISHED_EVENT,
                                          					 CALL_ORIGINATED_EVENT, CALL_QUEUED_EVENT, | 28 |
| LAST_REDIRECT_ DEVID_TAG | CALL_DELIVERED_EVENT, CALL_ESTABLISHED_EVENT, CALL_QUEUED_EVENT | 29 |
| ANSWERING_DEVID_ TAG | CALL_ESTABLISHED_EVENT | 30 |
| HOLDING_DEVID_ TAG | CALL_HELD_EVENT | 31 |
| RETRIEVING_DEVID_ TAG | CALL_RETRIEVED_EVENT | 32 |
| RELEASING_DEVID_ TAG | CALL_CONNECTION_ CLEARED_EVENT | 33 |
| FAILING_DEVID_TAG | CALL_FAILED_EVENT | 34 |
| PRIMARY_DEVID_ TAG | CALL_CONFERENCED_EVENT, CALL_TRANSFERRED_EVENT | 35 |
| SECONDARY_DEVID_ TAG | CALL_CONFERENCED_EVENT, CALL_TRANSFERRED_EVENT | 36 |
| CONTROLLER_ DEVID_ TAG | CALL_CONFERENCED_EVENT | 37 |
| ADDED_PARTY_ DEVID_TAG | CALL_CONFERENCED_EVENT | 38 |
| PARTY_CALLID_TAG | CALL_CONFERENCED_EVENT, CALL_TRANSFERRED_EVENT,
                                          					 CONFERENCE_CALL_CONF, TRANSFER_CALL_CONF | 39 |
| PARTY_DEVID_TYPE_ TAG | CALL_CONFERENCED_EVENT, CALL_TRANSFERRED_EVENT,
                                          					 CONFERENCE_CALL_CONF, TRANSFER_CALL_CONF | 40 |
| PARTY_DEVID_TAG | CALL_CONFERENCED_EVENT, CALL_TRANSFERRED_EVENT,
                                          					 CONFERENCE_CALL_CONF, TRANSFER_CALL_CONF | 41 |
| TRANSFERRING_ DEVID_TAG | CALL_TRANSFERRED_EVENT | 42 |
| TRANSFERRED_ DEVID_TAG | CALL_TRANSFERRED_EVENT | 43 |
| DIVERTING_DEVID_ TAG | CALL_DIVERTED_EVENT | 44 |
| QUEUE_DEVID_TAG | CALL_QUEUED_EVENT | 45 |
| CALL_WRAPUP_ DATA_ TAG | BEGIN_CALL_EVENT, CALL_DATA_UPDATE_EVENT, SET_CALL_DATA_REQ,
                                          					 CONSULTATION_CALL_REQ, MAKE_CALL_REQ, TRANSFER_CALL_REQ, SNAPSHOT_CALL_CONF | 46 |
| NEW_CONNECTION_ DEVID_TAG | CALL_DATA_UPDATE_EVENT, CONFERENCE_CALL_CONF,
                                          					 CONSULTATION_CALL_CONF, MAKE_CALL_CONF, TRANSFER_CALL_CONF | 47 |
| TRUNK_USED_ DEVID_ TAG | CALL_REACHED_NETWORK_ EVENT | 48 |
| AGENT_PASSWORD_ TAG | SET_AGENT_STATE_REQ | 49 |
| ACTIVE_CONN_ DEVID_ TAG | ALTERNATE_CALL_REQ, CONFERENCE_CALL_REQ, CONSULTATION_CALL_REQ,
                                          					 RECONNECT_CALL_REQ, TRANSFER_CALL_REQ | 50 |
| FACILITY_CODE_TAG | CONSULTATION_CALL_REQ, MAKE_CALL_REQ, TRANSFER_CALL_REQ | 51 |
| OTHER_CONN_ DEVID_ TAG | ALTERNATE_CALL_REQ | 52 |
| HELD_CONN_DEVID_ TAG | CONFERENCE_CALL_REQ, RECONNECT_CALL_REQ, RETRIEVE_CALL_REQ,
                                          					 TRANSFER_CALL_REQ | 53 |
| (reserved) |  | 54-55 |
| CALL_CONN_ CALLID_ TAG | SNAPSHOT_CALL_CONF, SNAPSHOT_DEVICE_CONF | 56 |
| CALL_CONN_DEVID_ TYPE_TAG | SNAPSHOT_CALL_CONF, SNAPSHOT_DEVICE_CONF | 57 |
| CALL_CONN_DEVID_ TAG | SNAPSHOT_CALL_CONF, SNAPSHOT_DEVICE_CONF | 58 |
| CALL_DEVID_TYPE_ TAG | SNAPSHOT_CALL_CONF | 59 |
| CALL_DEVID_TAG | SNAPSHOT_CALL_CONF | 60 |
| CALL_DEV_CONN_ STATE_TAG | SNAPSHOT_CALL_CONF | 61 |
| SKILL_GROUP_ NUMBER_TAG | CALL_QUEUED_EVENT, CALL_DEQUEUED_EVENT, QUERY_AGENT_STATE_CONF | 62 |
| SKILL_GROUP_ID_ TAG | CALL_QUEUED_EVENT, CALL_DEQUEUED_EVENT, QUERY_AGENT_STATE_CONF | 63 |
| SKILL_GROUP_ PRIORITY_TAG | CALL_QUEUED_EVENT, CALL_DEQUEUED_EVENT, QUERY_AGENT_STATE_CONF | 64 |
| SKILL_GROUP_ STATE_ TAG | QUERY_AGENT_STATE_CONF | 65 |
| OBJECT_NAME_TAG | CLIENT_EVENT_REPORT | 66 |
| DTMF_STRING_TAG | SEND_DTMF_SIGNAL_REQ | 67 |
| POSITION_ID_TAG | SET_AGENT_STATE_REQ | 68 |
| SUPERVISOR_ID_TAG | SET_AGENT_STATE_REQ | 69 |
| LINE_HANDLE_TAG | QUERY_DEVICE_INFO_CONF | 70 |
| LINE_TYPE_TAG | QUERY_DEVICE_INFO_CONF | 71 |
| ROUTER_CALL_KEY_ DAY_TAG | BEGIN_CALL_EVENT, CALL_ DATA_UPDATE_EVENT, CALL_
                                          					 TRANSLATION_ROUTE_EVENT, SNAPSHOT_CALL_ CONF | 72 |
| ROUTER_CALL_KEY_ CALLID_TAG | BEGIN_CALL_EVENT, CALL_ DATA_UPDATE_EVENT, CALL_
                                          					 TRANSLATION_ROUTE_EVENT, SNAPSHOT_CALL_ CONF | 73 |
| ROUTER_CALL_KEY_SEQUENCE_NUM_TAG | AGENT_LEGACY_PRE_CALL_EVENT, BEGIN_CALL_EVENT,
                                          					 CALL_DATA_UPDATE_EVENT, CALL_TRANSLATION_ROUTE_EVENT, AGENT_PRE_CALL_EVENT,
                                          					 AGENT_PRE_CALL_ABORT_EVENT | 110 |
| (reserved) |  | 74 |
| CALL_STATE_TAG | SNAPSHOT_DEVICE_CONF | 75 |
| MONITORED_DEVID_TAG | MONITOR_START_REQ | 76 |
| AUTHORIZATION_ CODE_TAG | CONFERENCE_CALL_REQ, CONSULTATION_CALL_REQ, MAKE_CALL_REQ,
                                          					 MAKE_PREDICTIVE_CALL_REQ, TRANSFER_CALL_REQ | 77 |
| ACCOUNT_CODE_TAG | CONFERENCE_CALL_REQ, CONSULTATION_CALL_REQ, MAKE_CALL_REQ,
                                          					 MAKE_PREDICTIVE_CALL_REQ, TRANSFER_CALL_REQ | 78 |
| ORIGINATING_DEVID_TAG | MAKE_PREDICTIVE_CALL_REQ | 79 |
| ORIGINATING_LINE _ID_TAG | MAKE_PREDICTIVE_CALL_REQ | 80 |
| CLIENT_ADDRESS_ TAG | CLIENT_SESSION_OPENED_EVENT, CLIENT_SESSION_CLOSED_EVENT | 81 |
| NAMED_VARIABLE_ TAG | BEGIN_CALL_EVENT, CALL_DATA_UPDATE_EVENT, AGENT_PRE_CALL_EVENT, CALL_TRANSLATION_ROUTE_ EVENT, SET_CALL_DATA_REQ, CONFERENCE_CALL_REQ,
                                          CONSULTATION_CALL_REQ, MAKE_CALL_REQ, MAKE_PREDICTIVE_CALL_REQ, TRANSFER_CALL_REQ, SNAPSHOT_CALL_CONF, REGISTER_VARIABLES_REQ,
                                          SNAPSHOT_TASK_RESP, SNAPSHOT_TASK_EVENT | 82 |
| NAMED_ARRAY_TAG | BEGIN_CALL_EVENT, CALL_DATA_UPDATE_EVENT, AGENT_PRE_CALL_EVENT, CALL_TRANSLATION_ROUTE_ EVENT, SET_CALL_DATA_REQ, CONFERENCE_CALL_REQ,
                                          CONSULTATION_CALL_REQ, MAKE_CALL_REQ, MAKE_PREDICTIVE_CALL_REQ, TRANSFER_CALL_REQ, SNAPSHOT_CALL_CONF, REGISTER_VARIABLES_REQ,
                                          SNAPSHOT_TASK_RESP, SNAPSHOT_TASK_EVENT | 83 |
| CALL_CONTROL_ TABLE_TAG | MAKE_CALL_REQ, MAKE_PREDICTIVE_CALL_REQ, | 84 |
| SUPERVISOR_ INSTRUMENT_TAG | SUPERVISE_CALL_REQ | 85 |
| ATC_AGENT_ID_TAG | AGENT_TEAM_CONFIG_EVENT | 86 |
| AGENT_FLAGS_TAG | AGENT_TEAM_CONFIG_EVENT | 87 |
| ATC_AGENT_STATE_ TAG | AGENT_TEAM_CONFIG_EVENT | 88 |
| ATC_STATE_ DURATION_TAG | AGENT_TEAM_CONFIG_EVENT | 89 |
| AGENT_
                                          					 CONNECTION_DEVID_ TAG | SUPERVISE_CALL_REQ | 90 |
| SUPERVISOR_ CONNECTION_ DEVID_TAG | SUPERVISE_CALL_REQ, | 91 |
| LIST_TEAM_ID_TAG | LIST_AGENT_TEAM_CONF | 92 |
| DEFAULT_DEVICE_ PORT_ADDRESS_TAG | AGENT_DESK_SETTINGS_CONF | 93 |
| SERVICE_NAME_TAG | REGISTER_SERVICE_REQ | 94 |
| CUSTOMER_PHONE_ NUMBER_TAG | SET_CALL_DATA_REQ, CALL_DATA_UPDATE_EVENT | 95 |
| CUSTOMER_ ACCOUNT_NUMBER_TAG | SET_CALL_DATA_REQ, CALL_DATA_UPDATE_EVENT | 96 |
| APP_PATH_ID_TAG | OPEN_REQ | 97 |
| SCRIPT_SELECTOR_TAG | SNAPSHOT_TASK_RESP, SNAPSHOT_TASK_EVENT | 99 |
| APPLICATION_STRING1_TAG | SNAPSHOT_TASK_RESP, SNAPSHOT_TASK_EVENT | 100 |
| APPLICATION_STRING2_TAG | SNAPSHOT_TASK_RESP, SNAPSHOT_TASK_EVENT | 101 |
| ROUTER_CALL_KEY_SEQUENCE_NUM_TAG | AGENT_LEGACY_PRE_CALL_EVENT, BEGIN_CALL_EVENT,
                                          					 CALL_DATA_UPDATE_EVENT, CALL_TRANSLATION_ROUTE_EVENT, AGENT_PRE_CALL_EVENT,
                                          					 AGENT_PRE_CALL_ABORT_EVENT | 110 |
| TRUNK_NUMBER_ TAG | CALL_DELIVERED_EVENT, CALL_ESTABLISHED_EVENT,
                                          					 CALL_REACHED_NETWORK_ EVENT | 121 |
| TRUNK_GROUP_ NUMBER_TAG | CALL_DELIVERED_EVENT, CALL_ESTABLISHED_EVENT,
                                          					 CALL_REACHED_NETWORK_EVENT | 122 |
| EXT_AGENT_STATE_ TAG | AGENT_STATE_EVENT | 123 |
| DEQUEUE_TYPE_TAG | CALL_DEQUEUED_EVENT | 124 |
| SENDING_ADDRESS_ TAG | RTP_STARTED_EVENT, RTP_STOPPED_EVENT | 125 |
| SENDING_PORT_TAG | RTP_STARTED_EVENT RTP_STOPPED_EVENT | 126 |
| Unused |  | 127-128 |
| MAX_QUEUED_TAG | CONFIG_SERVICE_EVENT, CONFIG_DEVICE_EVENT | 129 |
| QUEUE_ID_TAG | QUEUE_UPDATED_EVENT | 130 |
| CUSTOMER_ID_TAG | CONFIG_REQUEST_EVENT | 131 |
| SERVICE_SKILL_ TARGET_ID_TAG | CONFIG_SERVICE_EVENT | 132 |
| PERIPHERAL_NAME_ TAG | CONFIG_SERVICE_EVENT, CONFIG_SKILL_GROUP_EVENT,
                                          					 CONFIG_AGENT_EVENT, CONFIG_DIALED_NUMBER_ EVENT | 133 |
| DESCRIPTION_TAG | CONFIG_SERVICE_EVENT, CONFIG_SKILL_GROUP_EVENT,
                                          					 CONFIG_AGENT_EVENT, CONFIG_DIALED_NUMBER_EVENT CONFIG_MRD_EVENT | 134 |
| SERVICE_MEMBER_ ID_TAG | CONFIG_SKILL_GROUP_EVENT | 135 |
| SERVICE_MEMBER_ PRIORITY_TAG | CONFIG_SKILL_GROUP_EVENT | 136 |
| FIRST_NAME_TAG | CONFIG_AGENT_EVENT | 137 |
| LAST_NAME_TAG | CONFIG_AGENT_EVENT | 138 |
| SKILL_GROUP_TAG | CONFIG_AGENT_EVENT | 139 |
| AGENT_SKILL_ TARGET_ID_TAG | CONFIG_AGENT_EVENT | 141 |
| SERVICE_TAG | CONFIG_DIALED_NUMBER_ EVENT | 142 |
| Reserved |  | 143-149 |
| DURATION_TAG | AGENT_STATE_EVENT | 150 |
| Reserved |  | 151-172 |
| EXTENSION_TAG | CONFIG_SKILL_GROUP_EVENT, CONFIG_SERVICE_EVENT,
                                          					 CONFIG_AGENT_EVENT,CONFIG_DEVICE_EVENT | 173 |
| SERVICE_LEVEL_ THRESHOLD_TAG | CONFIG_SERVICE_EVENT | 174 |
| SERVICE_LEVEL_ TYPE_TAG | CONFIG_SERVICE_EVENT | 175 |
| CONFIG_PARAM_TAG | CONFIG_SKILL_GROUP_EVENT, CONFIG_SERVICE_EVENT | 176 |
| SERVICE_CONFIG_ KEY_TAG | CONFIG_KEY_EVENT, CONFIG_BEGIN_EVENT | 177 |
| SKILL_GROUP_ CONFIG_KEY_TAG | CONFIG_KEY_EVENT, CONFIG_BEGIN_EVENT | 178 |
| AGENT_CONFIG_ KEY_TAG | CONFIG_KEY_EVENT, CONFIG_BEGIN_EVENT | 179 |
| DEVICE_CONFIG_ KEY_TAG | CONFIG_KEY_EVENT, CONFIG_BEGIN_EVENT | 180 |
| Unused |  | 181-182 |
| RECORD_TYPE_TAG | CONFIG_AGENT_EVENT, CONFIG_DEVICE_EVENT, CONFIG_SERVICE_EVENT,
                                          					 CONFIG_SKILL_GROUP_EVENT | 183 |
| PERIPHERAL_ NUMBER_TAG | CONFIG_AGENT_EVENT, CONFIG_DEVICE_EVENT, CONFIG_SERVICE_EVENT,
                                          					 CONFIG_SKILL_GROUP_EVENT | 184 |
| AGENT_SKILL_ TARGET_ID_TAG | CONFIG_AGENT_EVENT | 185 |
| NUM_SERVICE_ MEMBERS_TAG | CONFIG_SERVICE_EVENT | 186 |
| SERVICE_MEMBER_ TAG | CONFIG_SERVICE_EVENT | 187 |
| SERVICE_PRIORITY_ TAG | CONFIG_SERVICE_EVENT | 188 |
| AGENT_TYPE_TAG | CONFIG_AGENT_EVENT | 189 |
| LOGIN_ID_TAG | CONFIG_AGENT_EVENT | 190 |
| NUM_SKILLS_TAG | CONFIG_AGENT_EVENT | 191 |
| SKILL_GROUP_SKILL_TARGET_ID_TAG | CONFIG_SKILL_GROUP_EVENT | 192 |
| SERVICE_ID_TAG | CONFIG_DEVICE_EVENT | 193 |
| AGENT_ID_LONG_ TAG | OPEN_REQ, OPEN_REQ, OPEN_REQ_CONF, AGENT_STATE_EVENT,
                                          					 RTP_STARTED_EVENT, RTP_STOPPED_EVENT, SUPERVISE_CALL_REQ, EMERGENCY_CALL_EVENT,
                                          					 USER_MESSAGE_REQ, SET_AGENT_STATE_REQ, SET_AGENT_STATE_CONF,
                                          					 QUERY_AGENT_STATE_REQ, QUERY_AGENT_STATE_CONF, AGENT_UPDATED_EVENT | 194 |
| DEVICE_TYPE_TAG | CONFIG_DEVICE_EVENT | 195 |
| Unused |  | 196-197 |
| ENABLE_TAG | ROUTE_REGISTER_EVENT | 198 |
| DEVICEID_TAG | ROUTE_REQUEST_EVENT | 199 |
| TIMEOUT_TAG | ROUTE_REQUEST_EVENT | 200 |
| CURRENT_ROUTE_ TAG | ROUTE_REQUEST_EVENT | 201 |
| SECONDARY_ CONNECTION_CALL_ ID | CALL_DELIVERED_EVENT | 202 |
| PRIORITY_QUEUE_ NUMBER_TAG | CALL_QUEUED_EVENT | 203 |
| TEAM_NAME_TAG | TEAM_CONFIG_EVENT | 204 |
| MEMBER_TYPE_TAG | TEAM_CONFIG_EVENT | 205 |
| EVENT_DEVICE_ID_ TAG | SYSTEM_EVENT | 206 |
| LOGIN_NAME_TAG (V11) | CONFIG_AGENT_EVENT | 207 |
| PERIPHERAL_ID_TAG (V11) | CONFIG_AGENT_EVENT, CONFIG_SERVICE_EVENT,
                                          					 CONFIG_SKILL_GROUP_EVENT, CONFIG_DEVICE_EVENT | 208 |
| CALL_TYPE_KEY_ CONFIG_TAG (V11) | CONFIG_KEY_EVENT | 209 |
| CALL_TYPE_ID_TAG (V11) | AGENT_PRE_CALL_EVENT, CONFIG_CALL_TYPE_EVENT, SET_APP_DATA | 210 |
| CUSTOMER_ DEFINITION_ID_TAG (V11) | CONFIG_CALL_TYPE_EVENT | 211 |
| ENTERPRISE_NAME_ TAG (V11) | CONFIG_CALL_TYPE_EVENT CONFIG_MRD_EVENT | 212 |
| OLD_PERIPHERAL_ NUMBER_TAG | CONFIG_SKILL_GROUP_EVENT, CONFIG_CALL_TYPE_EVENT | 213 |
| CUR_LOGIN_ID | CONFIG_AGENT_EVENT | 214 |
| ANI_II_TAG | BEGIN_CALL_EVENT, CALL_TRANSLATION_ROUTE_ EVENT,
                                          					 CALL_DATA_UPDATE, CALL_DELIVERED_EVENT, AGENT_PRE_CALL_EVENT,
                                          					 SET_CALL_DATA_REQ, SNAPSHOT_CALL_REQ, ROUTE_REQUEST_EVENT | 215 |
| MR_DOMAIN_ID_TAG | CONFIG_SKILL_GROUP_EVENT, CONFIG_SERVICE_EVENT CONFIG_MRD_EVENT | 216 |
| CTIOS_CIL_CLIENT_ ID_TAG | SET_CALL_DATA_REQ, ALTERNATE_CALL_REQ, ANSWER_CALL_REQ,
                                          					 CLEAR_CALL_REQ, CLEAR_CONNECTION_REQ, DEFLECT_CALL_REQ, HOLD_CALL_REQ,
                                          					 RECONNECT_CALL_REQ, RETRIEVE_CALL_REQ, SEND_DTMF_SIGNAL_REQ,
                                          					 CHANGE_MONITOR_MASK_REQ, USER_MESSAGE_REQ, SESSION_MONITOR_START_REQ,
                                          					 SESSION_MONITOR_STOP_REQ, MONITOR_AGENT_TEAM_START_REQ, MONITOR_AGENT_TEAM_
                                          					 STOP_REQ, FAILURE_CONF, CONTROL_FAILURE_CONF | 217 |
| SILENT_MONITOR_ STATUS_TAG | SNAPSHOT_DEVICE_CONF | 218 |
| REQUESTING_ DEVICE_ID_TAG | CALL_CLEAR_CONNECTION_REQ | 219 |
| REQUESTING_ DEVICE_ID_ TYPE_TAG | CALL_CLEAR_CONNECTION_REQ | 220 |
| PRE_CALL_INVOKE_ ID_TAG | AGENT_PRE_CALL_EVENT, SET_APP_DATA | 221 |
| ENTERPRISE_ QUEUE_TIME |  | 222 |
| CALL_REFERENCE_ ID_TAG | BEGIN_CALL_EVENT, CALL_DATA_UPDATE_EVENT, CALL_TERMINATION_EVNT,
                                          					 SNAPSHOT_CALL_CONF | 223 |
| MULTI_LINE_AGENT_ CONTROL_TAG | OPEN_CONF | 224 |
| NETWORK_
                                          					 CONTROLLED_TAG | ROUTE_SELECT_EVENT | 225 |
| Used |  | 226-227 |
| NUM_PERIPHERALS_ TAG | OPEN_CONF | 228 |
| COC_CONNECTION_ CALL_ID_TAG | CALL_SERVICE_INITIATED_ EVENT, ROUTE_REQUEST_EVENT, SNAPSHOT
                                          					 _CALL_CONF | 229 |
| COC_CONNECTION_ DEVICE_ID_TYPE_ TAG | CALL_SERVICE_INITIATED_ EVENT, ROUTE_REQUEST_EVENT, SNAPSHOT
                                          					 _CALL_CONF | 230 |
| COC_CONNECTION_ DEVICE_ID_TAG | CALL_SERVICE_INITIATED_ EVENT, ROUTE_REQUEST_EVENT, SNAPSHOT
                                          					 _CALL_CONF | 231 |
| CALL_ORIGINATED_ FROM_TAG | SET_CALL_DATA_REQ | 232 |
| SET_APPDATA_CALLID_TAG |  | 233 |
| CLIENT_SHARE_KEY_TAG |  | 234 |
| AGENT_TEAM_NAME_TAG | AGENT_TEAM_CONFIG_EVENT | 243 |
| DIRECTION_TAG | AGENT_STATE_EVENT | 244 |
| OPTIONS_TAG | ROUTE_REQUEST_EVENT (internal use only for ACMI PIM) | 245 |
| FLT_MRD_ID_TAG | CONFIG_MEDIA_ROUTING_DOMAIN_EVENT (Internal Cisco Use Only) | 246 |
| MEDIA_CLASS_ID_TAG | CONFIG_MEDIA_ROUTING_DOMAIN_EVENT and CONFIG_MEDIA_CLASS_EVENT (Internal Cisco Use Only) | 247 |
| TASK_LIFE_TAG | CONFIG_MEDIA_ROUTING_DOMAIN_EVENT and CONFIG_MEDIA_CLASS_EVENT (Internal Cisco Use Only) | 248 |
| TASK_START_TIMEOUT_TAG | CONFIG_MEDIA_ROUTING_DOMAIN_EVENT and CONFIG_MEDIA_CLASS_EVENT (Internal Cisco Use Only) | 249 |
| MAX_TASK_DURATION_TAG | CONFIG_MEDIA_ROUTING_DOMAIN_EVENT and CONFIG_MEDIA_CLASS_EVENT (Internal Cisco Use Only) CONFIG_MRD_EVENT | 250 |
| INTERRUPTIBLE_TAG | CONFIG_MEDIA_ROUTING_DOMAIN_EVENT (Internal Cisco Use Only) CONFIG_MRD_EVENT | 251 |
| MAX_CALLS_IN_QUEUE_TAG | CONFIG_MEDIA_ROUTING_DOMAIN_EVENT (Internal Cisco Use Only) | 252 |
| MAX_CALLS_IN_QUEUE_PER_CALL_TYPE_TAG | CONFIG_MEDIA_ROUTING_DOMAIN_EVENT (Internal Cisco Use Only) | 253 |
| MAX_TIME_IN_QUEUE_TAG | CONFIG_MEDIA_ROUTING_DOMAIN_EVENT (Internal Cisco Use Only) | 254 |
| INTERNAL_AGENT_STATE_TAG | QUERY_AGENT_STATE_CONF (internal use only for CCX) | 255 |
| Unused |  | 256 |
| SSO_ENABLED_TAG | CONFIG_AGENT_EVENT, SET_AGENT_STATE_REQ | 257 |
| FLT_TASK_ID_TAG | AGENT_TASKS_RESP, AGENT_TASKS_EVENT | 258 |
| FLT_ICM_DISP_TAG | MEDIA_LOGOUT_IND | 259 |
| FLT_APP_DISP_TAG | MEDIA_LOGOUT_IND | 260 |
| NUM_MRDS_TAG | CONFIG_AGENT_EVENT, DESKTOP_CONNECTED_IND | 261 |
| FLT_AGENT_MRD_ID_TAG | CONFIG_AGENT_EVENT, DESKTOP_CONNECTED_IND | 262 |
| FLT_AGENT_MRD_STATE_TAG | CONFIG_AGENT_EVENT | 263 |
| FLT_PRECISION_QUEUE_ID_TAG | CONFIG_SKILL_GROUP_EVENT | 264 |
| FLT_PRECISION_QUEUE_NAME_TAG | CONFIG_SKILL_GROUP_EVENT | 265 |
| MAX_BEYOND_TASK_LIMIT_TAG | AGENT_STATE_EVENT, QUERY_AGENT_STATE_CONF, MEDIA_LOGIN_REQ, AGENT_INIT_REQ | 266 |
| AGENT_DESK_SETTINGS_ID_TAG | CONFIG_AGENT_EVENT | 267 |
| XFER_IN_WHILE_LOGGED_OUT_TAG | OFFER_APPLICATION_TASK_REQ START_APPLICATION_TASK_REQ | 268 |
| PERIPHERAL_CONFIG_KEY_TAG | CONFIG_KEY_EVENT | 269 |
| AGENT_DESK_SETTINGS_CONFIG_KEY_TAG | CONFIG_AGENT_EVENT | 270 |
| CONFIG_PERIPHERAL_ID_TAG | CONFIG_PERIPHERAL_EVENT | 271 |
| DEFAULT_AGENT_DESK_SETTINGS_ID_TAG | CONFIG_PERIPHERAL_EVENT | 272 |
| FLT_DESK_SETTINGS_MASK_TAG | CONFIG_AGENT_DESK_SETTINGS_EVENT | 273 |
| FLT_WRAP_UP_DATA_INCOMING_MODE_TAG | CONFIG_AGENT_DESK_SETTINGS_EVENT | 274 |
| FLT_WRAP_UP_DATA_OUTGOING_MODE_TAG | CONFIG_AGENT_DESK_SETTINGS_EVENT | 275 |
| FLT_LOGOUT_NON_ACTIVITY_TIME_TAG | CONFIG_AGENT_DESK_SETTINGS_EVENT | 276 |
| FLT_QUALITY_RECORDING_RATE_TAG | CONFIG_AGENT_DESK_SETTINGS_EVENT | 277 |
| FLT_RING_NO_ANSWER_TIME_TAG | CONFIG_AGENT_DESK_SETTINGS_EVENT | 278 |
| FLT_SILENT_MONITOR_WARNING_MESSAGE_TAG | CONFIG_AGENT_DESK_SETTINGS_EVENT | 279 |
| FLT_SILENT_MONITOR_AUDIBLE_INDICATION_TAG | CONFIG_AGENT_DESK_SETTINGS_EVENT | 280 |
| FLT_SUPERVISOR_ASSIST_CALL_METHOD_TAG | CONFIG_AGENT_DESK_SETTINGS_EVENT | 281 |
| FLT_EMERGENCY_CALL_METHOD_TAG | CONFIG_AGENT_DESK_SETTINGS_EVENT | 282 |
| FLT_AUTO_RECORD_ON_EMERGENCY_TAG | CONFIG_AGENT_DESK_SETTINGS_EVENT | 283 |
| FLT_RECORDING_MODE_TAG | CONFIG_AGENT_DESK_SETTINGS_EVENT | 284 |
| FLT_WORK_MODE_TIMER_TAG | CONFIG_AGENT_DESK_SETTINGS_EVENT | 285 |
| FLT_RING_NO_ANSWER_DN_ID_TAG | CONFIG_AGENT_DESK_SETTINGS_EVENT | 286 |
| FLT_DEFAULT_DEVICE_PORT_ADDRESS_TAG | CONFIG_AGENT_DESK_SETTINGS_EVENT | 287 |
| DESKTOP_CONNECTED_FLAG_TAG | AGENT_TASKS_REQUEST_EVENT | 288 |
| PLAY_TONE_DIRECTION_TAG | START_NETWORK_RECORDING_REQ | 289 |
| INVOCATION_TYPE_TAG | START_NETWORK_RECORDING_REQ, STOP_NETWORK_RECORDING_REQ | 290 |
| RECORDER_ADDRESS_TAG | NETWORK_RECORDING_TARGET_INFO_EVENT | 291 |
| TERMINAL_NAME_TAG | NETWORK_RECORDING_TARGET_INFO_EVENT | 292 |
| MEDIA_FORKING_DEVICE_NAME_TAG | NETWORK_RECORDING_TARGET_INFO_EVENT | 293 |
| PROTOCOL_REFERENCE_GUID_TAG | NETWORK_RECORDING_TARGET_INFO_EVENT AGENT_PRE_CALL_EVENT | 294 |
| MEDIA_FORKING_CLUSTER_ID_TAG | NETWORK_RECORDING_TARGET_INFO_EVENT | 295 |
| RECORDER_URI_TAG | NETWORK_RECORDING_TARGET_INFO_EVENT | 296 |
| RECORDER_ERROR_MSG_TAG | NETWORK_RECORDING_TARGET_INFO_EVENT | 297 |
| RECORDER_TYPE_TAG | NETWORK_RECORDING_TARGET_INFO_EVENT | 298 |
| RECORDER_STATUS_TAG | NETWORK_RECORDING_TARGET_INFO_EVENT | 299 |
| RECORDING_DEVICE_ID_TAG | NETWORK_RECORDING_STARTED_EVENT, NETWORK_RECORDING_ENDED_EVENT, NETWORK_RECORDING_FAILED_EVENT, NETWORK_RECORDING_TARGET_INFO_EVENT | 300 |
| FLT_TERM_TYPE | CONFIG_TERMINAL_EVENT | 302 |
| FLT_TERM_DEVICE_NAME | CONFIG_TERMINAL_EVENT,CONFIG_AGENT_EVENT, SET_AGENT_STATE_REQ, AGENT_STATE_EVENT | 303 |
| FLT__TERM_TYPE_NAME | CONFIG_TERMINAL_EVENT | 304 |
| FLT_NUM_INSTRUMENTS | CONFIG_TERMINAL_EVENT | 305 |
| ACD_SHARED_LINE_USAGE | AGENT_DESK_SETTINGS_CONF CONFIG_AGENT_DESK_SETTINGS_EVENT | 306 |
| PLAY_ZIP_TONE | AGENT_DESK_SETTINGS_CONF CONFIG_AGENT_DESK_SETTINGS_EVENT | 307 |
|  |  |  |
| FLT_ENABLED_SERVICES | CONFIG_AGENT_SERVICE_EVENT SET_AGENT_SERVICE_DATA_REQ | 309 |
| NUM_OF_ENABLED_SERVICES | CONFIG_AGENT_SERVICE_EVENT SET_AGENT_SERVICE_DATA_REQ | 310 |
| CCAI_CONFIG_ID | AGENT_PRE_CALL_EVENT | 311 |
| MEDIA_TYPE_TAG | MEDIA_LOGIN_REQ | 312 |
| MEDIA_PROVIDER_TAG | MEDIA_LOGIN_REQ | 313 |

| State Name | Description | Value |
|---|---|---|
| AGENT_STATE_ LOGIN | The agent
                                          					 has logged on to the ACD. It does not necessarily indicate that the agent is
                                          					 ready to accept calls. | 0 |
| AGENT_STATE_ LOGOUT | The agent
                                          					 has logged out of the ACD and cannot accept any additional calls. | 1 |
| AGENT_STATE_ NOT_ READY | The agent
                                          					 is unavailable for any call work. | 2 |
| AGENT_STATE_ AVAILABLE | The agent
                                          					 is ready to accept a call. | 3 |
| AGENT_STATE_ TALKING | The agent
                                          					 is currently talking on a call (inbound, outbound, or inside). | 4 |
| AGENT_STATE_ WORK_NOT_READY | The agent
                                          					 is performing after call work, but will not be ready to receive a call when
                                          					 completed. | 5 |
| AGENT_STATE_ WORK_ READY | The agent
                                          					 is performing after call work, and will be ready to receive a call when
                                          					 completed. | 6 |
| AGENT_STATE_ BUSY_ OTHER | The agent
                                          					 is busy performing a task associated with another active SkillGroup. | 7 |
| AGENT_STATE_ RESERVED | The agent
                                          					 is reserved for a call that will arrive at the ACD shortly. | 8 |
| AGENT_STATE_ UNKNOWN | The agent
                                          					 state is currently unknown. | 9 |
| AGENT_STATE_ HOLD | The agent
                                          					 currently has all calls on hold. | 10 |
| AGENT_STATE_ ACTIVE | The agent
                                          					 state is currently active. | 11 |
| AGENT_STATE_ PAUSED | The agent
                                          					 state is currently paused. | 12 |
| AGENT_STATE_ INTERRUPTED | The agent
                                          					 state is currently interrupted. | 13 |
| AGENT_STATE_NOT_ACTIVE | The agent
                                          					 state is currently not active. | 14 |

| PGStatus | Description | Mask Value |
|---|---|---|
| PGS_OPC_DOWN | Communication lost between the CTI Server and the PG’s Open
                                          					 Peripheral Controller (OPC) process. No call or agent state event messages can
                                          					 be sent due to this condition. | 0x00000001 |
| PGS_CC_DOWN | Communication lost between the PG and the Unified CCE Central
                                          					 Controller. Primarily affects translation routing and post-routing, other call
                                          					 and agent event messages can still be sent. | 0x00000002 |
| PGS_PERIPHERAL_OFFLINE | One or
                                          					 more of the peripherals monitored by the PG are offline. | 0x00000004 |
| PGS_CTI_SERVER_OFFLINE | Loss of
                                          					 communication between the CTI Server and the CTI Client. This status code is
                                          					 not reported by a software layer between the CTI Server and the client
                                          					 application. | 0x00000008 |
| PGS_LIMITED_FUNCTION | This
                                          					 status code may be reported by a software layer between the CTI Server and the
                                          					 client application when PGS_CTI_SERVER_ OFFLINE is true to indicate that
                                          					 limited local call control is possible. | 0x00000010 |

| Peripheral
                                          					 Type | Description | Value |
|---|---|---|
| PT_NONE | Not
                                          					 Applicable | 0xffff |
| PT_MERIDIAN | Northern
                                          					 Telecom Meridian ACD | 2 |
| PT_G2 | Lucent G2 | 3 |
| PT_DEFINITY_ECS_ NON_EAS | Lucent
                                          					 DEFINITY ECS (without Expert Agent Selection) | 4 |
| PT_DEFINITY_ECS_ EAS | Lucent
                                          					 DEFINITY ECS (with Expert Agent Selection) | 5 |
| PT_GALAXY | Obsolete | 6 |
| PT_SPECTRUM | Obsolete | 7 |
| PT_VRU | VRU (event
                                          					 type interface) | 8 |
| PT_VRU_POLLED | VRU
                                          					 (polled type interface) | 9 |
| PT_DMS100 | Obsolete | 10 |
| PT_SIEMENS_9006 | Siemens
                                          					 Hicom ACD (9006) | 11 |
| PT_SIEMENS_9005 | Siemens
                                          					 9751 CBX Release 9005 (Rolm 9005) | 12 |
| PT_ALCATEL | Alcatel
                                          					 4400 ACD | 13 |
| PT_NEC_NEAX_2x00 | Obsolete | 14 |
| PT_
                                          					 ACP_1000 | Ericsson
                                          					 ACP1000 | 15 |
| PT_ENTERPRISE_ AGENT | Unified
                                          					 CCE Manager | 17 |
| PT_MD110 | Ericsson
                                          					 MD-110 | 18 |
| PT_MEDIA_ROUTING | Media
                                          					 Routing | 19 |
| PT_GENERIC | Generic | 20 |
| PT_ACMI_CRS | A
                                          					 Gateway PG over Unified CCX | 21 |
| PT_ACMI_IPCC | A
                                          					 Gateway PG over Unified CCE or Unified CCX | 22 |
| PT_ARS | A system
                                          					 using the ARS PG | 24 |
| PT_ACMI_ERS | A system
                                          					 using the ERS PG | 25 |
| PT_ACMI_EXPERT_ADVISOR | Obsolete | 26 |
| {reserved} |  | 27 |

| LocalConnectionState | Description | Value |
|---|---|---|
| LCS_NONE | Not
                                          					 applicable | 0xffff |
| LCS_NULL | No
                                          					 relationship between call and device. | 0 |
| LCS_INITIATE | Device
                                          					 requesting service (“dialing”). | 1 |
| LCS_ALERTING | Device is
                                          					 alerting (“ringing”). | 2 |
| LCS_CONNECT | Device is
                                          					 actively participating in the call. | 3 |
| LCS_HOLD | Device is
                                          					 inactively participating in the call. | 4 |
| LCS_QUEUED | Device is
                                          					 stalled attempting to connect to a call, or a call is stalled attempting to
                                          					 connect to a device. | 5 |
| LCS_FAIL | A
                                          					 device-to-call or call-to-device connection attempt has been aborted. | 6 |

| EventCause | Value |
|---|---|
| CEC_NONE | 0xffff |
| CEC_ACTIVE_MONITOR | 1 |
| CEC_ALTERNATE | 2 |
| CEC_BUSY | 3 |
| CEC_CALL_BACK | 4 |
| CEC_CALL_CANCELLED | 5 |
| CEC_CALL_FORWARD_ALWAYS | 6 |
| CEC_CALL_FORWARD_BUSY | 7 |
| CEC_CALL_FORWARD_NO_ANSWER | 8 |
| CEC_CALL_FORWARD | 9 |
| CEC_CALL_NOT_ANSWERED | 10 |
| CEC_CALL_PICKUP | 11 |
| CEC_CAMP_ON | 12 |
| CEC_DEST_NOT_OBTAINABLE | 13 |
| CEC_DO_NOT_DISTURB | 14 |
| CEC_INCOMPATIBLE_DESTINATION | 15 |
| CEC_INVALID_ACCOUNT_CODE | 16 |
| CEC_KEY_CONFERENCE | 17 |
| CEC_LOCKOUT | 18 |
| CEC_MAINTENANCE | 19 |
| CEC_NETWORK_CONGESTION | 20 |
| CEC_NETWORK_NOT_OBTAINABLE | 21 |
| CEC_NEW_CALL | 22 |
| CEC_NO_AVAILABLE_AGENTS | 23 |
| CEC_OVERRIDE | 24 |
| CEC_PARK | 25 |
| CEC_OVERFLOW | 26 |
| CEC_RECALL | 27 |
| CEC_REDIRECTED | 28 |
| CEC_REORDER_TONE | 29 |
| CEC_RESOURCES_NOT_AVAILABLE | 30 |
| CEC_SILENT_MONITOR | 31 |
| CEC_TRANSFER | 32 |
| CEC_TRUNKS_BUSY | 33 |
| CEC_VOICE_UNIT_INITIATOR | 34 |
| CEC_TIME_OUT | 35 |
| CEC_NEW_CALL_INTERFLOW | 36 |
| CEC_SIMULATION_INIT_REQUEST | 37 |
| CEC_SIMULATION_RESET_REQUEST | 38 |
| CEC_CTI_LINK_DOWN | 39 |
| CEC_PERIPHERAL_RESET_REQUEST | 40 |
| CEC_MD110_CONFERENCE_TRANSFER | 41 |
| CEC_REMAINS_IN_Q | 42 |
| CEC_SUPERVISOR_ASSIST | 43 |
| CEC_EMERGENCY_CALL | 44 |
| CEC_SUPERVISOR_CLEAR | 45 |
| CEC_SUPERVISOR_MONITOR | 46 |
| CEC_SUPERVISOR_WHISPER | 47 |
| CEC_SUPERVISOR_BARGE_IN | 48 |
| CEC_SUPERVISOR_INTERCEPT | 49 |
| CEC_CALL_PARTY_UPDATE_IND | 50 |
| CEC_CONSULT | 51 |
| CEC_NIC_CALL_CLEAR | 52 |
| CEC_DNP | 53 |
| CEC_ ROUTER_REQUERY_BEFORE_ANSWER | 54 |
| CEC_ROUTER_REQUERY_AFTER_ANSWER | 55 |
| CEC_ NETWORK_ERROR | 56 |
| CEC_ NETWORK_ERROR_BEFORE_ANSWER | 57 |
| CEC_NETWORK_ERROR_AFTER_ANSWER | 58 |
| CEC_ GREETING | 59 |
| CEC_ RECORD_AGENT_GREETING | 60 |
| CEC_SNAPSHOT | 61 |
| CEC_ MAX_QUEUE_EXCEEDED | 62 |

| EventCause | Value |
|---|---|
| CECX_ABAND_NETWORK | 1001 |
| CECX_ABAND_LOCAL_QUEUE | 1002 |
| CECX_ABAND_RING | 1003 |
| CECX_ABAND_DELAY | 1004 |
| CECX_ABAND_INTERFLOW | 1005 |
| CECX_ABAND_AGENT_TERMINAL | 1006 |
| CECX_SHORT | 1007 |
| CECX_BUSY | 1008 |
| CECX_FORCED_BUSY | 1009 |
| CECX_DROP_NO_ANSWER | 1010 |
| CECX_DROP_BUSY | 1011 |
| CECX_DROP_REORDER | 1012 |
| CECX_DROP_HANDLED_PRIMARY_ROUTE | 1013 |
| CECX_DROP_HANDLED_OTHER | 1014 |
| CECX_REDIRECTED | 1015 |
| CECX_CUT_THROUGH | 1016 |
| CECX_INTRAFLOW | 1017 |
| CECX_INTERFLOW | 1018 |
| CECX_RING_NO_ANSWER | 1019 |
| CECX_INTERCEPT_REORDER | 1020 |
| CECX_INTERCEPT_DENIAL | 1021 |
| CECX_TIME_OUT | 1022 |
| CECX_VOICE_ENERGY | 1023 |
| CECX_NONCLASSIFIED_ENERGY_DETECT | 1024 |
| CECX_NO_CUT_THROUGH | 1025 |
| CECX_UABORT | 1026 |
| CECX_FAILED_SOFTWARE | 1027 |
| CECX_BLIND_TRANSFER | 1028 |
| CECX_ANNOUNCED_TRANSFER | 1029 |
| CECX_CONFERENCED | 1030 |
| CECX_DUPLICATE_TRANSFER | 1031 |
| CECX_UNMONITORED_DEVICE | 1032 |
| CECX_ANSWERING_MACHINE | 1033 |
| CECX_NETWORK_BLIND_TRANSFER | 1034 |
| CECX_TASK_ABANDONED_IN_ROUTER | 1035 |
| CECX_TASK_ABANDONED_BEFORE_OFFERED | 1036 |
| CECX_TASK_ABANDONED_WHILE_OFFERED | 1037 |
| CECX_NORMAL_END_TASK | 1038 |
| CECX_CANT_OBTAIN_TASK_ID | 1039 |
| CECX_AGENT_LOGGED_OUT_DURING_TASK | 1040 |
| CECX_MAX_TASK_LIFETIME_EXCEEDED | 1041 |
| CECX_APPLICATION_PATH_WENT_DOWN | 1042 |
| CECX_ICM_ROUTING_COMPLETE | 1043 |
| CECX_ICM_ROUTING_DISABLED | 1044 |
| CECX_APPL_INVALID_MRD_ID | 1045 |
| CECX_APPL_INVALID_DIALOGUE_ID | 1056 |
| CECX_APPL_DUPLICATE_DIALOGUE_ID | 1047 |
| CECX_APPL_INVALID_INVOKE_ID | 1048 |
| CECX_APPL_INVALID_SCRIPT_SELECTOR | 1049 |
| CECX_APPL_TERMINATE_DIALOGUE | 1050 |
| CECX_TASK_ENDED_DURING_APP_INIT | 1051 |
| CECX_CALLED_PARTY_DISCONNECTED | 1052 |
| CECX_PARTIAL_CALL | 1053 |
| CECX_DROP_NETWORK_CONSULT | 1054 |
| CECX_NETWORK_CONSULT_TRANSFER | 1055 |
| CECX_NETWORK_CONFERENCE | 1056 |
| CECX_ABAND_NETWORK_CONSULT | 1057 |

| Device ID
                                          					 Type | Description | Value |
|---|---|---|
| DEVID_NONE | No device
                                          					 ID is provided. | 0xffff |
| DEVID_DEVICE_IDENTIFIER | The
                                          					 provided device ID identifies a peripheral teleset (extension). | 0 |
| DEVID_TRUNK_IDENTIFIER | The
                                          					 provided device ID identifies a peripheral Trunk. | 70 |
| DEVID_TRUNK_GROUP_ IDENTIFIER | The
                                          					 provided device ID identifies a peripheral Trunk Group. | 71 |
| DEVID_IP_PHONE_MAC_ IDENTIFIER | The
                                          					 provided device ID identifiers the MAC address of an IP phone (Unified CCX
                                          					 ONLY). | 72 |
| DEVID_CTI_PORT | The
                                          					 provided device ID identifiers a CTI PORT (Unified CCX ONLY). | 73 |
| DEVID_ROUTE_POINT | The
                                          					 provided device ID identifies a ROUTE POINT. | 74 |
| DEVID_EXTERNAL | The
                                          					 provided device ID is an ANI number or some other external identifier. | 75 |
| DEVID_AGENT_DEVICE | The
                                          					 provided device ID is the ID of an AGENT Device (phone). | 76 |
| DEVID_QUEUE | The
                                          					 provided device ID is the ID of a QUEUE. | 77 |
| DEVID_NON_ACD_DEVICE_ IDENTIFIER | The
                                          					 provided device ID identifies a peripheral telset (extension) that is
                                          					 classified as being a non-ACD extension. | 78 |
| DEVID_SHARED_DEVICE_ IDENTIFIER | The
                                          					 provided device ID identifies a peripheral telset (extension) that is
                                          					 classified as being a shared line (0 or more telsets share this extension). | 79 |

| CallType | Description | Value |
|---|---|---|
| CALLTYPE_ACD_IN | Inbound ACD call. In Unified CCE, it indicates that this is a post route request. | 1 |
| CALLTYPE
                                          					 _PREROUTE_ ACD_IN | Translation routed inbound ACD call. | 2 |
| CALLTYPE
                                          					 _PREROUTE_ DIRECT_AGENT | Translation routed call to a specific agent. | 3 |
| CALLTYPE
                                          					 _TRANSFER_IN | Transferred inbound call. | 4 |
| CALLTYPE
                                          					 _OVERFLOW_IN | Overflowed
                                          					 inbound call. | 5 |
| CALLTYPE
                                          					 _OTHER_IN | Inbound
                                          					 call. | 6 |
| CALLTYPE
                                          					 _AUTO_OUT | Automatic
                                          					 out call. | 7 |
| CALLTYPE
                                          					 _AGENT_OUT | Agent out
                                          					 call. | 8 |
| CALLTYPE
                                          					 _OUT | Outbound
                                          					 call. | 9 |
| CALLTYPE
                                          					 _AGENT_INSIDE | Agent
                                          					 inside call. | 10 |
| CALLTYPE
                                          					 _OFFERED | Blind
                                          					 transferred call. | 11 |
| CALLTYPE
                                          					 _CONSULT | Consult
                                          					 call. | 12 |
| CALLTYPE
                                          					 _CONSULT_ OFFERRED | Announced
                                          					 transferred call. | 13 |
| CALLTYPE
                                          					 _CONSULT_ CONFERENCE | Conferenced consult call. | 14 |
| CALLTYPE
                                          					 _CONFERENCE | Conference
                                          					 call. | 15 |
| CALLTYPE_UNMONITORED | Inside or
                                          					 outbound call for which no call events will be received. | 16 |
| CALLTYPE_PREVIEW | Automatic
                                          					 out call in which the agent is given the option to proceed to dial a contact. | 17 |
| CALLTYPE_RESERVATION | Call made
                                          					 to reserve an agent for some other function. | 18 |
| CALLTYPE_ASSIST | Call to
                                          					 supervisor for assistance. | 19 |
| CALLTYPE_EMERGENCY | Emergency
                                          					 call. | 20 |
| CALLTYPE_SUPERVISOR_ MONITOR | Supervisor
                                          					 silently monitoring call. | 21 |
| CALLTYPE_SUPERVISOR_ WHISPER | Supervisor monitoring call, agent can hear supervisor. | 22 |
| CALLTYPE_SUPERVISOR_ BARGEIN | Supervisor conferenced into call. | 23 |
| CALLTYPE_SUPERVISOR_ INTERCEPT | Supervisor replaces agent on call. | 24 |
| CALLTYPE_TASK_ROUTED_BY_ICM | Task
                                          					 routed by Unified CCE | 25 |
| CALLTYPE_TASK_ROUTED_BY_APPLICATION | Task
                                          					 routed by application | 26 |
| CALLTYPE_NON_ACD | Agent
                                          					 call that is a non-ACD routed call. | 27 |
| RESERVATION_PREVIEW | Call
                                          					 type for Outbound Option Reservation calls for Preview mode. | 27 |
| RESERVATION_PREVIEW_DIRECT | Call
                                          					 type for Outbound Option Reservation calls for Direct Preview mode. | 28 |
| RESERVATION_PREDICTIVE | Call
                                          					 type for Outbound Option Reservation calls for Predictive mode and Progressive
                                          					 mode. | 29 |
| RESERVATION_CALLBACK | Call
                                          					 type for Outbound Option Reservation calls for Callback calls. | 30 |
| RESERVATION_PERSONAL_CALLBACK | Call
                                          					 type for Outbound Option Reservation calls for Personal Callback calls. | 31 |
| CUSTOMER_PREVIEW | Call
                                          					 type for Outbound Option Customer calls for Preview mode. | 32 |
| CUSTOMER_PREVIEW_DIRECT | Call
                                          					 type for Outbound Option Customer
                                          					 calls for Direct Preview | 33 |
| CUSTOMER_PREDICTIVE | Call
                                          					 type for Outbound Option Customer calls for Predictive mode and Progreassive
                                          					 modefor agentbased campaigns. | 34 |
| CUSTOMER_CALLBACK | Call
                                          					 type for Outbound Option Customer calls for callback calls. | 35 |
| CUSTOMER_PERSONAL | Call
                                          					 type for Outbound Option Customer calls for personal callback calls. | 36 |
| CUSTOMER_IVR | Call
                                          					 type for Outbound Option Customer calls for Transfer to IVR campaigns. | 37 |
| CALLTYPE_NON_ACD | Agent
                                          					 call that is a non-ACD call. | 38 |
| CALLTYPE_PLAY_AGENT_GREETING | An agent
                                          					 greeting route request. | 39 |
| CALLTYPE_RECORD_AGENT_GREETING | Record
                                          					 agent greeting call initiated by AGENT_GREETING_CONTROL_REQ. | 40 |
| CALLTYPE_VOICE_CALL_BACK | Voice
                                          					 callback using the Agent Request API. | 41 |

| ConnectionDevice IDType | Description | Value |
|---|---|---|
| CONNECTION_ID_ NONE | No
                                          					 ConnectionDeviceID is provided. | 0xffff |
| CONNECTION_ID_ STATIC | The
                                          					 ConnectionDeviceID value is stable over time (between calls). | 0 |
| CONNECTION_ID_ DYNAMIC | The
                                          					 ConnectionDeviceID value is dynamic and may change between calls. | 1 |

| LineType | Description | Value |
|---|---|---|
| LINETYPE_INBOUND_ ACD | Line used
                                          					 for inbound ACD calls. | 0 |
| LINETYPE_OUTBOUND_ACD | Line used
                                          					 for outbound ACD calls. | 1 |
| LINETYPE_INSIDE | Line used
                                          					 for inside calls. | 2 |
| LINETYPE_UNKNOWN | Line used
                                          					 for any purpose. | 3 |
| LINETYPE_SUPERVISOR | Line used
                                          					 for supervisor calls. | 4 |
| LINETYPE_MESSAGE | Line used
                                          					 for voice messages. | 5 |
| LINETYPE_HELP | Line used
                                          					 for assistance. | 6 |
| LINETYPE_OUTBOUND | Line used
                                          					 for outbound non-ACD calls. | 7 |
| LINETYPE_DID | Line used
                                          					 for direct inward dialed calls. | 8 |
| LINETYPE_SILENT_ MONITOR | Line used
                                          					 for silent monitor. | 9 |
| LINETYPE_NON_ACD_IN | Line used
                                          					 for inbound non-ACD calls. | 10 |
| LINETYPE_NON_ACD_OUT | Line used
                                          					 for outbound non-ACD calls. | 11 |

| FailureCode | Description | Value |
|---|---|---|
| CF_GENERIC_UNSPECIFIED | An error
                                          					 has occurred that is not one of the following error types. | 0 |
| CF_GENERIC_OPERATION | An
                                          					 operation error occurred (no specific details available). | 1 |
| CF_REQUEST_ INCOMPATIBLE_WITH_ OBJECT | The
                                          					 request is not compatible with the object. | 2 |
| CF_VALUE_OUT_OF_ RANGE | The
                                          					 parameter has a value that is not in the range defined for the server. | 3 |
| CF_OBJECT_NOT_KNOWN | The
                                          					 parameter has a value that is not known to the server. | 4 |
| CF_INVALID_CALLING_ DEVICE | The
                                          					 calling device is invalid. | 5 |
| CF_INVALID_CALLED_ DEVICE | The called
                                          					 device is invalid | 6 |
| CF_INVALID_FORWARDING_ DESTINATION | The
                                          					 forwarding destination device is invalid. | 7 |
| CF_PRIVILEGE_VIOLATION_ ON_SPECIFIED_DEVICE | The
                                          					 specified device is not authorized for the service. | 8 |
| CF_PRIVILEGE_VIOLATION_ ON_CALLED_DEVICE | The called
                                          					 device is not authorized for the service. | 9 |
| CF_PRIVILEGE_VIOLATION_ ON_CALLING_DEVICE | The
                                          					 calling device is not authorized for the service. | 10 |
| CF_INVALID_CSTA_CALL_ IDENTIFIER | The call
                                          					 identifier is invalid. | 11 |
| CF_INVALID_CSTA_DEVICE_ IDENTIFIER | The device
                                          					 identifier is invalid. | 12 |
| CF_INVALID_CSTA_ CONNECTION_IDENTIFIER | The
                                          					 connection identifier is invalid. | 13 |
| CF_INVALID_DESTINATION | The
                                          					 request specified a destination that is invalid. | 14 |
| CF_INVALID_FEATURE | The
                                          					 request specified a feature that is invalid. | 15 |
| CF_INVALID_ALLOCATION_ STATE | The
                                          					 request specified an allocation state that is invalid. | 16 |
| CF_INVALID_CROSS_REF_ID | The
                                          					 request specified a cross- reference ID that is not in use at this time. | 17 |
| CF_INVALID_OBJECT_TYPE | The
                                          					 request specified an invalid object type. | 18 |
| CF_SECURITY_VIOLATION | Security
                                          					 error (no specific details available). | 19 |
| CF_GENERIC_STATE_ INCOMPATIBILITY | The
                                          					 request is not compatible with the condition of a related device. | 21 |
| CF_INVALID_OBJECT_STATE | The
                                          					 object is in the incorrect state for the request. | 22 |
| CF_INVALID_CONNECTION_ ID_FOR_ACTIVE_CALL | The
                                          					 active connection ID in the request is invalid. | 23 |
| CF_NO_ACTIVE_CALL | There is
                                          					 no active call for the request. | 24 |
| CF_NO_HELD_CALL | There is
                                          					 no held call for the request. | 25 |
| CF_NO_CALL_TO_CLEAR | There is
                                          					 no call associated with the given connection ID. | 26 |
| CF_NO_CONNECTION_TO_ CLEAR | There is
                                          					 no call connection for the given connection ID. | 27 |
| CF_NO_CALL_TO_ANSWER | There is
                                          					 no alerting call to be answered. | 28 |
| CF_NO_CALL_TO_ COMPLETE | There is
                                          					 no active call to be completed. | 29 |
| CF_GENERIC_SYSTEM_ RESOURCE_AVAILABILITY | The
                                          					 request failed due to lack of system resources (no specific details available). | 31 |
| CF_SERVICE_BUSY | The
                                          					 service is temporarily unavailable. | 32 |
| CF_RESOURCE_BUSY | An
                                          					 internal resource is busy. | 33 |
| CF_RESOURCE_OUT_OF_ SERVICE | The
                                          					 service requires a resource that is out of service. | 34 |
| CF_NETWORK_BUSY | The
                                          					 server sub-domain is busy. | 35 |
| CF_NETWORK_OUT_OF_ SERVICE | The
                                          					 server sub-domain is out of service. | 36 |
| CF_
                                          					 OVERALL_MONITOR_ LIMIT_EXCEEDED | The
                                          					 request would exceed the server’s overall resource limits. | 37 |
| CF_CONFERENCE_MEMBER_ LIMIT_EXCEEDED | The
                                          					 request would exceed the server’s limit on the number of conference members. | 38 |
| CF_
                                          					 GENERIC_SUBSCRIBED_ RESOURCE_AVAILABILITY | The
                                          					 request failed due to lack of purchased or contracted resources (no specific
                                          					 details available). | 41 |
| CF_
                                          					 OBJECT_MONITOR_ LIMIT_EXCEEDED | The
                                          					 request would exceed the server’s specific resource limits. | 42 |
| CF_
                                          					 EXTERNAL_TRUNK_ LIMIT_EXCEEDED | The
                                          					 request would exceed the limit of external trunks. | 43 |
| CF_
                                          					 OUTSTANDING_ REQUEST_LIMIT_EXCEEDED | The
                                          					 request would exceed the limit of outstanding requests. | 44 |
| CF_GENERIC_ PERFORMANCE_ MANAGEMENT | The
                                          					 request failed as a performance management mechanism (no specific details
                                          					 available). | 51 |
| CF_PERFORMANCE_LIMIT_ EXCEEDED | The
                                          					 request failed because a performance management limit was exceeded. | 52 |
| CF_
                                          					 SEQUENCE_NUMBER_ VIOLATED | The
                                          					 server has detected an error in the sequence number of the operation. | 61 |
| CF_
                                          					 TIME_STAMP_ VIOLATED | The
                                          					 server has detected an error in the time stamp of the operation. | 62 |
| CF_
                                          					 PAC_VIOLATED | The
                                          					 server has detected an error in the PAC of the operation. | 63 |
| CF_
                                          					 SEAL_VIOLATED | The
                                          					 server has detected an error in the Seal of the operation. | 64 |
| CF_
                                          					 GENERIC_UNSPECIFIED_ REJECTION | The
                                          					 request has been rejected (no specific details available). | 70 |
| CF_
                                          					 GENERIC_OPERATION_ REJECTION | The
                                          					 requested operation has been rejected (no specific details available). | 71 |
| CF_
                                          					 DUPLICATE_ INVOCATION_REJECTION | The
                                          					 request duplicated another request for the same service. | 72 |
| CF_
                                          					 UNRECOGNIZED_ OPERATION_REJECTION | The
                                          					 request specified an unrecognized operation. | 73 |
| CF_MISTYPED_ARGUMENT_ REJECTION | The
                                          					 request contained a parameter of the wrong type for the requested operation. | 74 |
| CF_
                                          					 RESOURCE_LIMITATION_ REJECTION | The
                                          					 request would have exceeded a resource limitation. | 75 |
| CF_
                                          					 ACS_HANDLE_ TERMINATION_REJECTION | The
                                          					 request specified an ACS handle that is no longer in use. | 76 |
| CF_
                                          					 SERVICE_ TERMINATION_REJECTION | The
                                          					 request failed because the required service has been terminated. | 77 |
| CF_
                                          					 REQUEST_TIMEOUT_ REJECTION | The
                                          					 request failed because a timeout limit was exceeded. | 78 |
| CF_REQUESTS_ON_DEVICE_ EXCEEDED_REJECTION | The
                                          					 request would have exceeded the limits of the device. | 79 |

| FailureCode | Description | Value |
|---|---|---|
| CF_INVALID_AGENT_ID_ SPECIFIED | The
                                          						request specified an invalid AgentID. | 256 |
| CF_INVALID_PASSWORD_ SPECIFIED | The
                                          						request specified an invalid agent password. | 257 |
| CF_INVALID_AGENT_ID_ OR_PASSWORD_SPECIFIED | The
                                          						request specified an invalid AgentID and/or invalid agent password. | 258 |
| CF_SPECIFIED_AGENT_ ALREADY_SIGNED_ON | The
                                          						request failed because the specified agent is already logged in. | 259 |
| CF_INVALID_LOGON_ DEVICE_SPECIFIED | The
                                          						request specified an invalid logon device. | 260 |
| CF_INVALID_ANSWERING_ DEVICE_SPECIFIED | The
                                          						request specified an invalid answering device. | 261 |
| CF_INVALID_SKILL_ GROUP_SPECIFIED | The
                                          						request specified an invalid agent skill group. | 262 |
| CF_INVALID_CLASS_OF_ SERVICE_SPECIFIED | The
                                          						request specified an invalid class of service. | 263 |
| CF_INVALID_TEAM_ SPECIFIED | The
                                          						request specified an invalid team. | 264 |
| CF_INVALID_AGENT_ WORKMODE | The
                                          						request specified an invalid agent work mode. | 265 |
| CF_INVALID_AGENT_ REASON_CODE | The
                                          						request specified an invalid agent reason code. | 266 |
| CF_ADJUNCT_SWITCH_ COMM_ERROR | A
                                          						communication error occurred on the datalink between the Unified CCE and the
                                          						ACD. | 267 |
| CF_AGENT_NOT_PARTY_ ON_CALL | The
                                          						specified agent is not a party on the indicated call. | 268 |
| CF_INTERNAL_ PROCESSING_ERROR | An
                                          						internal error occurred in the ACD while processing the request. | 269 |
| CF_TAKE_CALL_CONTROL_ REJECTION | The
                                          						ACD refused an Unified CCE request to take control of a call. | 270 |
| CF_TAKE_DOMAIN_ CONTROL_REJECTION | The
                                          						ACD refused an Unified CCE request to take control of a domain. | 271 |
| CF_REQUESTED_SERVICE_ NOT_REGISTERED | The
                                          						Unified CCE is not registered on the ACD for the requested service. | 272 |
| CF_INVALID_CONSULT_ TYPE | The
                                          						consult type is invalid. | 273 |
| CF_ANSMAP_OR_ ADPARAM_FIELD_NOT_VALID | The
                                          						Ansmap or Asparam field are not valid. | 274 |
| CF_INVALID_CALL_ CONTROL_TABLE_ SPECIFIED | The
                                          						call control table is invalid. | 275 |
| CF_INVALID_DIGITS_ RNATIMEOUT_AMSDELAY_ OR_COUNTRY |  | 276 |
| CF_ANSWER_DETECT_ PORT_UNAVAILABLE |  | 277 |
| CF_VIRTUAL_AGENT_ UNAVAILABLE |  | 278 |
| CF_TAKEBACK_N_XFER_ ROUTE_END |  | 279 |
| CF_WRAPUP_DATA_ REQUIRED |  | 280 |
| CF_REASON_CODE_ REQUIRED |  | 281 |
| CF_INVALID_TRUNK_ID_ SPECIFIED |  | 282 |
| CF_SPECIFIED_EXTENSION_ ALREADY_IN_USE |  | 283 |
| CF_ARBITRARY_CONF_OR_ XFER_NOT_SUPPORTED |  | 284 |
| CF_NETWORK_TRANSFER_OR_ CONSULT |  | 285 |
| CF_NETWORK_TRANSFER_OR_ CONSULT_FAILED |  | 286 |
| CF_DEVICE_RESTRICTED |  | 287 |
| CF_LINE_RESTRICTED |  | 288 |
| CF_AGENT_ACCOUNT_ LOCKED_OUT |  | 289 |
| CF_DROP_ANY_PARTY_NOT_ ENABLED_CTI |  | 290 |
| CF_MAXIMUM_LINE_LIMIT_ EXCEEDED |  | 291 |
| CF_SHARED_LINES_NOT_ SUPPORTED |  | 292 |
| CF_EXTENSION_NOT_UNIQUE |  | 293 |
| CF_UNKNOWN_ INTERFACE_ CTRLR_ID | The
                                          						Interface Controller ID is unknown. | 1001 |
| CF_INVALID_INTERFACE_ CTRLR_TYPE | The
                                          						Interface Controller type is invalid. | 1002 |
| CF_SOFTWARE_REV_NO_ SUPPORTED | The
                                          						current software revision is not supported. | 1003 |
| CF_UNKNOWN_PID | The
                                          						PeripheralID is unknown. | 1004 |
| CF_INVALID_TABLE_ SPECIFIED | An
                                          						invalid table was specified. | 1005 |
| CF_PD_SERVICE_INACTIVE | The
                                          						peripheral data service is not active. | 1006 |
| CF_UNKNOWN_ROUTING_ CLIENT_ID | The
                                          						RoutingClientID is unknown. | 1007 |
| CF_RC_SERVICE_ INACTIVATE | The
                                          						routing client service is not active. | 1008 |
| CF_INVALID_DIALED_ NUMBER | The
                                          						dialed number is invalid. | 1009 |
| CF_INVALID_PARAMETER | A
                                          						parameter in the request is invalid. | 1010 |
| CF_UNKNOWN_ROUTING_ PROBLEM | An
                                          						unspecified error occurred during routing. | 1011 |
| CF_UNSUPPORTED_PD_ MESSAGE_REVISION | The
                                          						requested peripheral data service protocol version is not supported. | 1012 |
| CF_UNSUPPORTED_RC_ MESSAGE_REVISION | The
                                          						requested routing client service protocol version is not supported. | 1013 |
| CF_UNSUPPORTED_IC_ MESSAGE_REVISION | The
                                          						requested interface controller service protocol version is not supported. | 1014 |
| CF_RC_SERVICE_ INACTIVATE_PIM | The
                                          						peripheral interface is not active. | 1015 |
| CF_AGENT_GREETING_CONTROL_OPERATION_FAILURE | This
                                          						error occurs if AGENT_GREETING_CONTROL_REQ request fails. Notes:
                                          						All detailed errors are defined as Peripheral Error Codes. | 1016 |

| AllocationState | Description | Value |
|---|---|---|
| ALLOC_CALL_ DELIVERED | Connect
                                          					 call to originating device when call is delivered (alerting). | 0 |
| ALLOC_CALL_ ESTABLISHED | Connect
                                          					 call to originating device when call is established (answered). | 1 |

| ForwardType | Description | Value |
|---|---|---|
| FWT_IMMEDIATE | Forward
                                          					 all calls. | 0 |
| FWT_BUSY | Forward
                                          					 only when busy. | 1 |
| FWT_NO_ANS | Forward
                                          					 after no answer. | 2 |
| FWT_BUSY_INT | Forward on
                                          					 busy for internal calls. | 3 |
| FWT_BUSY_EXT | Forward on
                                          					 busy for external calls. | 4 |
| FWT_NO_ANS_INT | Forward
                                          					 after no answer for internal calls. | 5 |
| FWT_NO_ANS_EXT | Forward
                                          					 after no answer for external calls. | 6 |

| TypeOfDevice | Description | Value |
|---|---|---|
| DEVT_STATION | A
                                          					 traditional telephone device, consisting of one or more buttons and one or more
                                          					 lines. | 0 |
| DEVT_LINE | A
                                          					 communications interface to one or more stations. | 1 |
| DEVT_BUTTON | An
                                          					 instance of a call manipulation point at an individual station. | 2 |
| DEVT_ACD | A
                                          					 mechanism that distributes calls. | 3 |
| DEVT_TRUNK | A device
                                          					 used to access other switching domains. | 4 |
| DEVT_OPERATOR | A device
                                          					 that interacts with a call party to assist in call setup or provide other
                                          					 telecommunications service. | 5 |
| DEVT_STATION_ GROUP | Two or
                                          					 more stations used interchangeably or addressed identically. | 16 |
| DEVT_LINE_GROUP | A set of
                                          					 communications interfaces to one or more stations. | 17 |
| DEVT_BUTTON_ GROUP | Two or
                                          					 more instances of a call manipulation point at an individual station. | 18 |
| DEVT_ACD_GROUP | A call
                                          					 distributor device as well as the devices to which it distributes calls. | 19 |
| DEVT_TRUNK_ GROUP | A set of
                                          					 trunks providing connectivity to the same place. Individual trunks within the
                                          					 group may be used interchangeably. | 20 |
| DEVT_OPERATOR_ GROUP | Two or
                                          					 more operator devices used interchangeably or addressed identically. | 21 |
| DEVT_CTI_PORT_ SCCP | A CTI port
                                          					 on a Unified CM device. | 22 |
| DEVT_CTI_PORT_SIP | A CTI port
                                          					 on a SIP device. | 23 |
| DEVT_OTHER | A device
                                          					 that does not fall into any of the preceding categories. | 255 |

| ClassOfDevice | Description | Value |
|---|---|---|
| DEVC_OTHER | A class of
                                          					 device not covered by the following image, data, or voice classes. | 10x |
| DEVC_IMAGE | A device
                                          					 that is used to make digital data calls involving imaging or high speed circuit
                                          					 switched data in general. | 20x |
| DEVC_DATA | A device
                                          					 that is used to make digital data calls (both circuit switched and packet
                                          					 switched). | 40x |
| DEVC_VOICE | A device
                                          					 that is used to make audio calls. | 80x |

| CallPlacementType | Description | Value |
|---|---|---|
| CPT_UNSPECIFIED | Use
                                          					 default call placement. | 0 |
| CPT_LINE_CALL | An inside
                                          					 line call. | 1 |
| CPT_OUTBOUND | An
                                          					 outbound call. | 2 |
| CPT_OUTBOUND_NO_ ACCESS_CODE | An
                                          					 outbound call that will not require an access code. | 3 |
| CPT_DIRECT_POSITION | A call
                                          					 placed directly to a specific position. | 4 |
| CPT_DIRECT_AGENT | A call
                                          					 placed directly to a specific agent. | 5 |
| CPT_SUPERVISOR_ASSIST | A call
                                          					 placed to a supervisor for call handling assistance. | 6 |

| CallMannerType | Description | Value |
|---|---|---|
| CMT_UNSPECIFIED | Use
                                          					 default call manner. | 0 |
| CMT_POLITE | Attempt
                                          					 the call only if the originating device is idle. | 1 |
| CMT_BELLIGERENT | This CallManner type is only used with the MAKE_CALL_REQUEST. When an agent in Available state places an outbound call, the
                                          Unified CCE system forcibly changes the agent's state to NotReady with the 50006 reason code. The system changes the agent's
                                          state back to Available after the call ends or if the call fails to connect. For more details on the reason code, see the
                                          the Database Schema Handbook for Cisco Unified ICM/Contact Center Enterprise, Release 12.5(1) at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-technical-reference-list.html | 2 |
| CMT_SEMI_POLITE | Attempt
                                          					 the call only if the originating device is idle or is receiving dial tone. | 3 |
| CMT_RESERVED | Reserved | 4 |

| CallOption | Description | Value |
|---|---|---|
| COPT_UNSPECIFIED | No call
                                          					 options specified, use defaults. | 0 |
| COPT_CALLING_ AGENT_ONLINE | Attempt
                                          					 the call only if the calling agent is “online” (available to interact with the
                                          					 destination party). | 1 |
| COPT_CALLING_ AGENT_RESERVED | Obsolete
                                          					 with DMS-100. | 2 |
| COPT_CALLING_ AGENT_NOT_ RESERVED | Obsolete
                                          					 with DMS-100. | 3 |
| COPT_CALLING_ AGENT_BUZZ_BASE | Obsolete
                                          					 with DMS-100. | 4 |
| COPT_CALLING_ AGENT_BEEP_HSET | Obsolete
                                          					 with DMS-100. | 5 |
| COPT_SERVICE_ CIRCUIT_ON | Causes a
                                          					 call classifier to be applied to the call (ACM ECS). | 6 |

| ConsultType | Description | Value |
|---|---|---|
| CT_UNSPECIFIED | Default
                                          					 (consult call). | 0 |
| CT_TRANSFER | Consult
                                          					 call prior to transfer. | 1 |
| CT_CONFERENCE | Consult
                                          					 call prior to conference. | 2 |

| FacilityType | Description | Value |
|---|---|---|
| FT_UNSPECIFIED | Use
                                          					 default facility type. | 0 |
| FT_TRUNK_GROUP | Facility
                                          					 is a trunk group. | 1 |
| FT_SKILL_GROUP | Facility
                                          					 is a skill group or split. | 2 |

| AnsweringMachine | Description | Value |
|---|---|---|
| AM_UNSPECIFIED | Use
                                          					 default behavior. | 0 |
| AM_CONNECT | Connect
                                          					 call to agent when call is answered by an answering machine. | 1 |
| AM_DISCONNECT | Disconnect
                                          					 call when call is answered by an answering machine. | 2 |
| AM_NONE | Do not use
                                          					 answering machine detection. | 3 |
| AM_NONE_NO_ MODEM | Do not use
                                          					 answering machine detection, but disconnect call if answered by a modem. | 4 |
| AM_CONNECT_NO_MODEM | Connect
                                          					 call when call is answered by an answering machine, disconnect call if answered
                                          					 by a modem. | 5 |

| AnswerDetectMode | Description | Value |
|---|---|---|
| ADM_UNSPECIFIED | Use
                                          					 default behavior. | 0 |
| ADM_VOICE_
                                          					 THRESHOLD | Report
                                          					 call answered by an answering machine when initial voice duration exceeds time
                                          					 threshold. | 1 |
| ADM_VOICE_END | Report
                                          					 call answered by an answering machine when initial voice segment ends. | 2 |
| ADM_VOICE_END_ DELAY | Report
                                          					 call answered by an answering machine after a fixed delay following the end of
                                          					 the initial voice segment. | 3 |
| ADM_VOICE_AND_ BEEP | Report
                                          					 call answered by an answering machine after a beep tone following the end of
                                          					 the initial voice segment (excluding beep tone without any preceding voice). | 4 |
| ADM_BEEP | Report
                                          					 call answered by an answering machine after a beep tone following the end of
                                          					 the initial voice segment (including beep tone without any preceding voice). | 5 |

| AgentWorkMode | Description | Value |
|---|---|---|
| AWM_UNSPECIFIED | Use
                                          					 default behavior. | 0 |
| AWM_AUTO_IN | Agent
                                          					 automatically becomes available after handling a call. | 1 |
| AWM_MANUAL_IN | Agent must
                                          					 explicitly indicate availability after handling a call. | 2 |
| RA_CALL_BY_CALL | Remote
                                          					 agent Call by Call mode. | 3 |
| RA_NAILED_
                                          					 CONNECTION | Remote
                                          					 agent NailedUp mode. | 4 |

| DestinationCountry | Description | Value |
|---|---|---|
| DEST_UNSPECIFIED | Unspecified or unknown, use default behavior. | 0 |
| DEST_US_AND_ CANADA | Call
                                          					 destination is in the United States or Canada. | 1 |

| MaskName | Description | Value |
|---|---|---|
| CTI_SERVICE_ DEBUG | Causes all
                                          					 messages exchanged during the current session to be captured to a file for
                                          					 later analysis. | 0x80000000 |
| CTI_SERVICE_ CLIENT_ EVENTS | Client
                                          					 receives call and agent state change events associated with a specific ACD
                                          					 phone. | 0x00000001 |
| CTI_SERVICE_CALL_ DATA_UPDATE | Client may
                                          					 modify call context data. | 0x00000002 |
| CTI_SERVICE_ CLIENT_CONTROL | Client may
                                          					 control calls and agent states associated with a specific ACD phone. | 0x00000004 |
| CTI_SERVICE_ CONNECTION_ MONITOR | Establishment and termination of this session cause
                                          					 corresponding Unified CCE Alarm events to be generated. | 0x00000008 |
| CTI_SERVICE_ALL_ EVENTS | Client
                                          					 receives all call and agent state change events (associated with any ACD
                                          					 phone). | 0x00000010 |
| CTI_SERVICE_ PERIPHERAL_ MONITOR | Client may
                                          					 dynamically add and remove devices and/or calls that it wishes to receive call
                                          					 and agent state events for. | 0x00000020 |
| CTI_SERVICE_ CLIENT_MONITOR | Client
                                          					 receives notification when all other CTI client sessions are opened and closed,
                                          					 and may monitor the activity of other CTI client sessions. | 0x00000040 |
| CTI_SERVICE_ SUPERVISOR | Client may
                                          					 request supervisor services. | 0x00000080 |
| CTI_SERVICE_ SERVER | Client
                                          					 identify itself as server application. | 0x00000100 |
| CTI_SERVICE_ AGENT_REPORTING | Client may
                                          					 reporting/routing ARM(Agent Reporting And Management) messages. | 0x00000400 |
| CTI_SERVICE_ALL_ TASK_EVENTS | Client
                                          					 receives all task events. | 0x00000800 |
| CTI_SERVICE_ TASK_MONITOR | Client
                                          					 receives monitored task events. | 0x00001000 |
| CTI_AGENT_STATE_CONTROL_ONLY | Client can
                                          					 change agent state only. Call control is not allowed. If a client requests for
                                          					 CTI_SERVICE_ CLIENT_CONTROL, the server may grant this flag to indicate that
                                          					 only agent state change is allowed. | 0x00002000 |
| Unused |  | 0x00004000 |
| CTI_DEVICE_STATE_CONTROL | The
                                          					 client/server wishes to register and get resource state change requests. | 0x00008000 |
| CTI_SERVICE_ UPDATE_EVENTS | Requests
                                          					 that this client receive update notification events. (No data) | 0x00080000 |
| CTI_SERVICE_ IGNORE_ DUPLICATE_ AGENT_EVENTS | Request to
                                          					 suppress duplicate agent state events. | 0x00100000 |
| CTI_SERVICE_ IGNORE_CONF | Do not
                                          					 send confirmations for third party requests. | 0x00200000 |
| CTI_SERVICE_ACD_ LINE_ONLY | Request
                                          					 that events for non-ACD lines not be sent. (Unified CCE only) | 0x00400000 |

| Disposition Code | Meaning |
|---|---|
| 1 | Abandoned
                                          					 in Network |
| 2 | Abandoned
                                          					 in Local Queue |
| 3 | Abandoned
                                          					 Ring |
| 4 | Abandoned
                                          					 Delay |
| 5 | Abandoned
                                          					 Interflow |
| 6 | Abandoned
                                          					 Agent Terminal |
| 7 | Short |
| 8 | Busy |
| 9 | Forced
                                          					 Busy |
| 10 | Disconnect/drop no answer |
| 11 | Disconnect/drop busy |
| 12 | Disconnect/drop reorder |
| 13 | Disconnect/drop handled primary route |
| 14 | Disconnect/drop handled other |
| 15 | Redirected |
| 16 | Cut
                                          					 Through |
| 17 | Intraflow |
| 18 | Interflow |
| 19 | Ring No
                                          					 Answer |
| 20 | Intercept
                                          					 reorder |
| 21 | Intercept
                                          					 denial |
| 22 | Time Out |
| 23 | Voice
                                          					 Energy |
| 24 | Non-classified Energy Detected |
| 25 | No Cut
                                          					 Through |
| 26 | U-Abort |
| 27 | Failed
                                          					 Software |
| 28 | Blind
                                          					 Transfer |
| 29 | Announced
                                          					 Transfer |
| 30 | Conferenced |
| 31 | Duplicate Transfer |
| 32 | Unmonitored Device |
| 33 | Answering Machine |
| 34 | Network
                                          					 Blind Transfer |
| 35 | Task
                                          					 Abandoned in Router |
| 36 | Task
                                          					 Abandoned Before Offered |
| 37 | Task
                                          					 Abandoned While Offered |
| 38 | Normal
                                          					 End Task |
| 39 | Can't
                                          					 Obtain Task ID |
| 40 | Agent
                                          					 Logged Out During Task |
| 41 | Maximum
                                          					 Task Lifetime Exceeded |
| 42 | Application Path Went Down |
| 43 | Unified
                                          					 CCE Routing Complete |
| 44 | Unified
                                          					 CCE Routing Disabled |
| 45 | Application Invalid MRD ID |
| 46 | Application Invalid Dialogue ID |
| 47 | Application Duplicate Dialogue ID |
| 48 | Application Invalid Invoke ID |
| 49 | Application Invalid Script Selector |
| 50 | Application Terminate Dialogue |
| 51 | Task
                                          					 Ended During Application Init |
| 52 | Called
                                          					 Party Disconnected |
| 53 | Partial
                                          					 Call |
| 54 | Drop
                                          					 Network Consult |
| 55 | Network
                                          					 Consult Transfer |
| 57 | Abandon
                                          					 Network Consult |
| 58 | Router
                                          					 Requery Before Answer |
| 59 | Router
                                          					 Requery After Answer |
| 60 | Network
                                          					 Error |
| 61 | Network
                                          					 Error Before Answer |
| 62 | Network
                                          					 Error After Answer |
| 63 | Task
                                          					 Transfer |
| 64 | Application Disconnected |
| 65 | Task
                                          					 Transferred on Agent Logout |

| DestinationCountry | Description | Value |
|---|---|---|
| OUTBOUND_SUPPORT | The agent
                                          					 login can support outbound feature. | 0x1 |

| DestinationCountry | Description | Value |
|---|---|---|
| SILENT_MONITOR_ NONE | Normal
                                          					 call (non-silent monitor call). | 0 |
| SILENT_MONITOR_ INITIATOR | Initiator
                                          					 of silent monitor call. | 1 |
| SILENT_MONITOR_ TARGET | Monitor
                                          					 target of silent monitor call. | 2 |

| State Name | Description | Value |
|---|---|---|
| AGENT_STATE_LOGIN | The agent
                                          					 has logged on to the ACD. It does not necessarily indicate that the agent is
                                          					 ready to accept calls. | 0 |
| AGENT_STATE_LOGOUT | The agent
                                          					 has logged out of the ACD and cannot accept any additional calls. | 1 |
| AGENT_STATE_NOT_READY | The agent
                                          					 is unavailable for any call work. | 2 |
| AGENT_STATE_AVAILABLE | The agent
                                          					 is ready to accept a call. | 3 |
| AGENT_STATE_TALKING | The agent
                                          					 is currently talking on a call (inbound, outbound, or inside). | 4 |
| AGENT_STATE_WORK_NOT_READY | The agent
                                          					 is performing after call work, but will not be ready to receive a call when
                                          					 completed. | 5 |
| AGENT_STATE_WORK_READY | The agent
                                          					 is performing after call work, but will be ready to receive a call when
                                          					 completed. | 6 |
| AGENT_STATE_BUSY_OTHER | The agent
                                          					 is busy performing a task associated with another active SkillGroup. | 7 |
| AGENT_STATE_ACTIVE | The agent
                                          					 state is currently active. | 11 |

| State Name | Description | Value |
|---|---|---|
| TASK_STATE_PRE_CALL | Pre Call
                                          					 Message has been sent to client. | 0 |
| TASK_STATE_ACTIVE | Task is
                                          					 actively being worked on; Start Task has been received for this task. | 1 |
| TASK_STATE_WRAPUP | Wrap up
                                          					 task has been received for this task. | 2 |
| TASK_STATE_PAUSED | Task is
                                          					 paused; Pause Task has been received for this task. | 3 |
| TASK_STATE_OFFERED | Offer Task
                                          					 has been received for this task. | 4 |
| ASK_STATE_INTERRUPTED | Task is
                                          					 interrupted; Agent Interrupt Accepted Ind is received. | 5 |
| TASK_STATE_NOT_READY | Not used. | 6 |
| TASK_STATE_LOGGED_OUT | Task is
                                          					 terminated. | 7 |