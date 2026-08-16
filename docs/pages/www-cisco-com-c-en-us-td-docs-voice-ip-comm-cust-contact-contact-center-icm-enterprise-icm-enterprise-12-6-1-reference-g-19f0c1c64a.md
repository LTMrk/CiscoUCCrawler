---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-icm-enterprise-icm-enterprise-12-6-1-reference-g-19f0c1c64a
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/icm_enterprise/icm_enterprise_12_6_1/reference/guide/ucce_b_cti-servermessage-reference-guide-for-1261/ucce_b_cti-servermessagereferenceguideprotocolversion24-for-1261_chapter_0111.html
retrieved_at: 2026-08-16T19:47:20.624088+00:00
---

CTI Server Message Reference Guide(Protocol Version 24) for Cisco Unified Contact Center Enterprise, Release 12.6(1)

# CTI Server Message Reference Guide(Protocol Version 24) for Cisco Unified Contact Center Enterprise, Release 12.6(1)

Updated: May 14, 2021

Chapter: Changes and Additions

## Chapter: Changes and Additions

# Changes and Additions

## Protocol Version 24

Following is a list of changes made in Protocol Version 24:

Added STANDBY_ACTIVE_EVENT_MSG, ACTIVE_MAINTENANCE_REQ_MSG, ACTIVE_MAINTENANCE_RESP_MSG, ACTIVE_MAINTENANCE_EVENT_MSG,  and
                                    STOPPING_REQUESTS_TO_THIS_SIDE_IND to Message Types .

Updated OPEN_REQ and OPEN_CONF in Message Types

Updated CONFIG_AGENT_SERVICE_EVENT, SET_AGENT_SERVICE_DATA_REQ and
                                    SET_AGENT_SERVICE_DATA_CONF

Added E_CTI_INVALID_CLIENT_FOR_STANDBY to the Failure Indication Message Status Codes table.

Added the following new messages:

CONFIG_AGENT_SERVICE_EVENT

SET_AGENT_SERVICE_DATA_REQ

SET_AGENT_SERVICE_DATA_CONF

Modified the existing messages:

AGENT_PRE_CALL_EVENT

SNAPSHOT_CALL_CONF

Added the following values to the Tag Values table:

FLT_ENABLED_SERVICES for the messages CONFIG_AGENT_SERVICE_EVENT and
                                          SET_AGENT_SERVICE_DATA_REQ.

NUM_OF_ENABLED_SERVICES for the messages CONFIG_AGENT_SERVICE_EVENT
                                          and

SET_AGENT_SERVICE_DATA_REQ.

CCAI_CONFIG_ID for the message AGENT_PRE_CALL_EVENT

NUM_POSITIVE_ANSWERS_SUGGESTIONS for the message
                                          SET_AGENT_SERVICE_DATA_REQ

NUM_NEGATIVE_ANSWERS_SUGGESTIONS for the message

SET_AGENT_SERVICE_DATA_REQ

Add a new row for the CONFIG_MSG_AGENT_SERVICE_MASK to Table 11: CTI Service
                                    Masks.

## Protocol Version 23

Following is a list of changes made in Protocol Version 23:

Added START_NETWORK_RECORDING_REQ and STOP_NETWORK_RECORDING_REQ to Client Control Service.

Added the following values to the Tag Values table:

FLT_TASK_ID_TAG for the AGENT_TASKS_EVENT message

CALL_VAR_1_TAG through CALL_VAR_10_TAG for the SNAPSHOT_TASK_EVENT message

DESKTOP_CONNECTED_FLAG_TAG for the AGENT_TASKS_REQUEST_EVENT message

TEXT_TAG for the AGENT_TASKS_END_EVENT message

NUM_MRDS_TAG for the DESKTOP_CONNECTED_IND message

Modified the existing message: MEDIA_LOGIN_REQ.

Added the following new messages:

NETWORK_RECORDING_STARTED_EVENT

NETWORK_RECORDING_ENDED_EVENT

NETWORK_RECORDING_FAILED_EVENT

NETWORK_RECORDING_TARGET_INFO_EVENT

## Protocol Version 22

Following is a list of changes made in Protocol Version 22:

Added MaxBeyondTaskLimit under AGENT_STATE_EVENT and QUERY_AGENT_STATE_CONF.

Added FltPrecisionQueueID and FltPrecisionQueueName under CONFIG_SKILL_GROUP_EVENT.

Added AgentDeskSettingsID in CONFIG_AGENT_EVENT.

Added CONFIG_AGENT_DESK_SETTINGS_EVENT and CONFIG_PERIPHERAL_EVENT.

Added PeripheralConfigKey and AgentDeskSettingsConfigKey under CONFIG_KEY_EVENT and CONFIG_BEGIN_EVENT.

Changed the behavior of CALL_DATA_UPDATE_EVENT for ECC variables.

## Protocol Version 21

Following is a list of changes made in Protocol Version 21:

Added NumMRDs, FLTAgentMRDID, and FltAgentMRDState under CONFIG_AGENT_EVENT.

Added a new Message with the type 259. This Message is reserved for internal use only.

Changed the behavior of the PeripheralType field in the OPEN_CONF message.

## Protocol Version
                        	 20

Following is a
                              		  list of additional changes made in Protocol Version 20 (Unified CCE
                              		  Release11.5(1)):

Important

In the CTI Server Protocol Version 20 the floating field tag and length size changed from 1 byte to 2 byte USHORT.

Added the
                                    				fixed AgentSkillTargetID and floating AgentID fields to the
                                    				AGENT_PRE_CALL_EVENT message.

Added the
                                    				CONFIG_MRD_EVENT message.

Added bit
                                          					 mask value 32=Media Routing Domain Information to the CONFIG_REQUEST_EVENT
                                          					 message ConfigInformation field. Added a cross-reference to this field from the
                                          					 OPEN_REQ message ConfigMsgMask field.

Added bit
                                          					 mask value 32=Media Routing Domain Information to the CONFIG_BEGIN_EVENT
                                          					 message ConfigInformation field.

Added the
                                          					 MR_DOMAIN_ID_TAG, DESCRIPTION_TAG, ENTERPRISE_NAME_TAG, MAX_TASK_DURATION_TAG,
                                          					 AND INTERRUPTIBLE_TAG to the event CONFIG_MRD_EVENT.

Added that the
                                    				AGENT_PRE_CALL_ABORT_ EVENT message is sent to the to ALL_EVENTS client.

Added the
                                    				following values to the Tag
                                       				  Values table:

SSO_ENABLED_TAG for the CONFIG_AGENT_EVENT and SET_AGENT_STATE_REQ

FLT_TASK_ID_TAG for the AGENT_TASKS_RESP message

FLT_ICM_DISP_TAG and FLT_APP_DISP_TAG for the MEDIA_LOGOUT_IND
                                          					 message

For the
                                    				CONFIG_AGENT_EVENT message, the length of the LoginName field is increased to
                                    				255 Bytes.

Floating field
                                    				subfields have changed:

The Tag
                                          					 subfield is a Data Type of USHORT and a Byte Size of 2.

The
                                          					 FieldLength subfield is a Data Type of USHORT and a Byte Size of 2.

Added or
                                    				modified these tags in the Tag Values table for the SNAPSHOT_TASKS_RESP
                                    				message: SCRIPT_SELECTOR_TAG , APPLICATION_STRING1_TAG,
                                    				APPLICATION_STRING2_TAG, CALL_VAR_1_TAG through CALL_VAR_10_TAG,
                                    				NAMED_VARIABLE_ TAG, NAMED_ARRAY_TAG.

Added new
                                    				TaskState Values that may appear in SNAPSHOT_TASK_RESP messages.

Added the
                                    				following values to the Disposition Codes table for nonvoice tasks:

63=Task
                                          					 Transferred

64=Application Disconnected

65=Task
                                          					 Transferred on Agent Logout

## Protocol Version
                        	 19

The following is a
                              		  list of changes made for CTI Server in Protocol Version 19:

Updated
                                    				Message Types in Messaging Conventions chapter.

Added
                                    				Configuration Acquisition Messages section in Application Level Interfaces
                                    				chapter.

Added row
                                    				containing INTERNAL_AGENT_STATE_TAG to Tag Values. Table Tag
                                       				  Values .

Added values
                                    				27 to 37 for outbound call types to CallType Values CallType Values .

Added row
                                    				containing InternalAgentState to QUERY_AGENT_STATE CONF Message Form to Table Message
                                       				  Types .

Added Agent’s
                                    				Internal States and their Status Values to Table Agent’s
                                       				  Internal States and their Status Values .

Removed the
                                    				ClientAddressIPV6 and SendingAddressIPV6 elements and the
                                    				CLIENT_ADDRESS_IPV6_TAG (226) and SENDING_ADDRESS_IPV6_TAG(227) tags due to a
                                    				change in the handling of IPv6 addresses.

Changed
                                    				ClientAddress and SendingAddress elements’ size from 16 byte to 64 byte to
                                    				support IPv6 addresses.

Added the
                                    				DepartmentID field to the following messages:

OPEN_CONF

AGENT_STATE_EVENT

AGENT_TEAM_CONFIG_EVENT

QUERY_AGENT_STATE_CONF

## Protocol Version
                        	 18

The following is a
                              		  list of changes made for CTI Server in Protocol Version 18 (Unified CCE version
                              		  10.0(1) - internal use only):

Added values
                                    				247 to 254 to Tag Values Table Tag
                                       				  Values .

## Protocol Version
                        	 17

The following is a
                              		  list of changes made for CTI Server in Protocol Version 17 (Unified CCE version
                              		  9.0(1) - internal use only):

Added row
                              		  containing OPTIONS_TAG to Tag Values Table Tag
                                 			 Values .

## Protocol Version
                        	 16

The following is a
                              		  list of changes made for CTI Server in Protocol Version 16 (Unified CCE verion
                              		  9.0(1)).

Added Agent
                                    				TeamName to AGENT_TEAM_CONFIG_EVENT Table Supervisor
                                       				  Service

Added
                                    				AGENT_TEAM_NAME_TAG(243) to Table Tag
                                       				  Values

Added
                                    				Direction to AGENT_STATE_EVENT Table Tag
                                       				  Values

Added
                                    				DIRECTION_TAG(244) to Table Tag
                                       				  Values

## Protocol Version
                        	 15

The following is a
                              		  list of additions and changes made to the CTI Server in Protocol Version 15
                              		  (Unified CCE Version 8.5(x)).

Added three
                                    				message types to Table Tag
                                       				  Values .

Added
                                    				CALL_AGENT_GREETING_MASK to Table Unsolicited
                                       				  Call Event Message Masks .

Added
                                    				CALL_AGENT_GREETING_EVENT in Table Unsolicited
                                       				  Call Event Message Masks .

Added
                                    				AGENT_GREETING_CONTROL_REQ in Table Message
                                       				  Types .

Added AGENT_GREETING_CONTROL_CONF in Table Message Types .

Added
                                    				CF_AGENT_GREETING_CONTROL_OPERATION_FAILURE Extended Control Failure Code to
                                    				Table ControlFailureCode
                                       				  Values .

## Protocol Version
                        	 14

The following is a
                              		  list of additions and changes made to the CTI Server in Protocol Version 14
                              		  (Unified CCE Version 8.0(x)).

Changed the
                                    				VersionNumber field in OPEN_REQ to 14 from 13.

Added new
                                    				floating field tags to Table Tag
                                       				  Values :

REQUESTING_DEVICE_ID_TAG (219)

REQUESTING_DEVICE_ID_TYPE_TAG (220)

PRE_CALL_INVOKE_ID_TAG (221)

ENTERPRISE_QUEUE_TIME (222)

CALL_REFERENCE_ID_TAG (223)

MULTI_LINE_AGENT_CONTROL_TAG (224)

NETWORK_CONTROLLED_TAG (225)

CLIENT_ADDRESS_IPV6_TAG (226)

SENDING_ADDRESS_IPV6_TAG(227)

NUM_PERIPHERALS_TAG(228)

COC_CONNECTION_CALL_ID_TAG(229)

COC_CALL_CONNECTION_DEVICE_ID_TYPE_TAG(230)

COC_CALL_CONNECTION_DEVICE_ID_TYPE_TAG(231)

CALL_ORIGINATED_FROM_TAG(232)

SET_APPDATA_CALLID_TAG(233)

CLIENT_SHARE_KEY_TAG(234)

Added
                                    				SkillGroupNumber field to MAKE_CALL_REQ.

Added
                                    				RouterCallKeyDay, RouterCallKeyCallID, and RouterCallKeySequenceNumber fields
                                    				to SET_CALL_DATA.

Added floating
                                    				CallTypeID field and floating PreCallInvokeID field to AGENT_PRE_CALL_EVENT and
                                    				SET_APP_DATA.

Added
                                    				CallReferenceIDfield (for solution call trace) to BEGIN_CALL_EVENT,
                                    				CALL_DATA_UPDATE_EVENT, and SNAPSHOT_CALL_CONF.

Added optional
                                    				parms RequestingDeviceID and RequestingDeviceIDType to CLEAR_CONNECTION_REQ.

Added
                                    				DEVID_NON_ACD_DEVICE_IDENTIFIER and DEVID_SHARED_DEVICE_IDENTIFIER to Table DeviceIDType
                                       				  Values .

Added non ACD
                                    				line types LINETYPE_NON_ACD_IN and LINETYPE_NON_ACD_OUT to Table LineType
                                       				  Values .

Added calltype
                                    				CALLTYPE_NON_ACD (27) to Table CallType
                                       				  Values .

Added the
                                    				NumPeripherals, FltPeripheralID, and MultilineAgentControl fields to OPEN_CONF.

Added the
                                    				following status codes to Table PGStatusCode Values :

E_CTI_INVALID_CONFIG_MSG_MASK

E_CTI_AUTO_CONFIG_RESET

E_CTI_INVALID_MONITOR_STATUS

E_CTI_INVALID_REQUEST_ID_TYPE

Added the
                                    				following ControlFailureCode values to Table ControlFailureCode
                                       				  Values :

CF_INVALID_TRUNK_ID_SPECIFIED

CF_SPECIFIED_EXTENSION_ALREADY_IN_USE

CF_ARBITRARY_CONF_OR_XFER_NOT_SUPPORTED

CF_NETWORK_TRANSFER_OR_CONSULT

CF_NETWORK_TRANSFER_OR_CONSULT_FAILED

CF_DEVICE_RESTRICTED

CF_LINE_RESTRICTED

CF_AGENT_ACCOUNT_LOCKED_OUT

CF_ARBITRARY_CONF_OR_XFER_NOT_SUPPORTED

CF_MAXIMUM_LINE_LIMIT_EXCEEDED

CF_SHARED_LINES_NOT_SUPPORTED

CF_EXTENSION_NOT_UNIQUE

Added
                                    				CTI_SERVICE_ACD_LINE_ONLY and CTI_SERVICE_IGNORE_CONF to Table CTI Service Masks .

Added the
                                    				ClientAddressIPV6 field to the following events:

RTP_STARTED_EVENT

RTP_STOPPED_EVENT

CLIENT_SESSION_OPENED_EVENT

CLIENT_SESSION_CLOSED_EVENT

EMERGENCY_CALL_EVENT

START_RECORDING_REQ

START_RECORDING_CONF

STOP_RECORDING_REQ

STOP_RECORDING_CONF

Added the
                                    				SendingAddressIPV6 field to RTP_STARTED_EVENT and RTP_STOPPED_EVENT.

Added the
                                    				COCConnectionCallID, COCCallConnectionDeviceIDType, and
                                    				COCCallConnectionDeviceID fields to CALL_SERVICE_INITIATED_EVENT and
                                    				SNAPSHOT_CALL_CONF.

Added device
                                    				types DEVT_CTI_PORT_SCCP, and DEVT_CTI_PORT_SIP to Table TypeOfDevice Values .

## Protocol Versions 10-13

The following is a list of additions and changes made to the CTI Server
                              in Protocol Versions 10-13 (ICM Version 7.0(x).

Added New Types to Existing Tables, New fields to existing Messages,
                                    New fields added to existing messages

Added following fields to AGENT_STATE_EVENT: Duration (optional),
                                    NextAgentState, FltSkillGroupNumber, FltSkillGroupID, FltSkillGroupPriority,
                                    FltSkillGroupState

Changed Version Number in OPEN_REQ to 13 from 6.

Added DeviceIDType to SNAPSHOT_CALL_REQ to allow for Queues and Agent
                                    extensions with the same number.

Added ForcedFlag and AgentServiceReq to SET_AGENT_STATE_REQ

Added CTI_AGENT_STATE_CONTROL_ONLY, CTI_DEVICE_STATE_CONTROL, CTI_ROUTING,
                                    CTI_SERVICE_MINIMIZE_EVENTS, CTI_SERVICE_CONFIG_EVENTS, CTI_SERVICE_UPDATE_EVENTS,
                                    and CTI_SERVICE_IGNORE_DUPLICATE_AGENT_EVENTS in the CTI Service Masks
                                    table.

Corrected CALL_QUEUED_EVENT scenarios to reflect a QueueDeviceIDType
                                    of DEVID_NONE and remove the QueueDeviceID floating field.

Added DEVID_QUEUE to the device ID type table.

Removed CallsInQueue from the QUERY_AGENT_STATISTICS_CONF message.

In CALL_DELIVERED_EVENT, changed AlertingDevice to required.

Removed Duplicate tag SKILL_GROUP_PRIORITY_TAG.

Added DEVICE_TYPE_TAG to the tag value table.

Removed OldestCallInQueue from the QUERY_AGENT_STATISTICS_CONF message.

Added AgentAvailabilityStatus to QUERY_AGENT_STATE_CONF and AGENT_STATE_EVENT.

Added AgentsICMAvailable, and AgentsApplicationAvailable to QUERY_SKILL_GROUP_STATISTICS_CONF.

Added ICMAvailableTimeSession, RoutableTimeSession, ICMAvailableTimeToday,
                                    and RoutableTimeToday to QUERY_AGENT_STATISTICS_CONF.

Added AGENT_UDPATED_EVENT and QUEUE_UPDATED_EVENT to the message type
                                    table. The individual messages were covered but they were missing from
                                    the table.

Corrected EMERGENCY_CALL_CONF table.

Changed PauseDuration in SEND_DTMF_SIGNAL_REQ from USHORT to UINT.
                                    The type was mistakenly changed and there is special code to cover the
                                    backward compatibility.

Added EventDeviceType and EventDeviceID in SYSTEM_EVENT to allow specifying
                                    a non-numeric device on the in and out of service events.

Corrected CustomerPhoneNumber, and CustomerAccountNumber to be optional
                                    in CALL_DATA_UPDATE_EVENT and SET_CALL_DATA_REQ

Added NumFltSkillGroups field and floating fields for FltSkillGroupNumber,
                                    FltSkillGroupID, FltSkilllGroupState, and FltSkillGroupPriority to allow
                                    specifying more than 1 skill group in the event to AGENT_STATE_EVENT

Added RA_CALL_BY_CALL and RA_NAILED_CONNECTION in AgentWorkMode table.

Updated following messages with new fields:

AGENT_STATE_EVENT: NextAgentState, Duration

CALL_DEQUEUED_EVENT: DeQueueType

OPEN_REQ: EventMsgMask

RTP_STARTED_EVENT: SendingAddress, SendingPort

RTP_STOPPED_EVENT: SendingAddress, SendingPort

SET_AGENT_STATE_REQ: ForcedFlag

Updated tables with various new values.

Updated tables with various new values.

## Protocol Version 9

The following is a list of additions and changes made to the CTI Server
                              in Protocol Version 9 (ICM Version 5.0).

Added Server Service. See the section “Server Service” in Chapter 5, “Application Level Interfaces.”

Added the CampaignID and QueryRuleID fields to the SET_CALL_DATA_REQ
                                    and CALL_DATA_UPDATE_EVENT messages.

During an OPEN_REQ of an ALL_EVENTS client session, additional SYSTEM_EVENTs
                                    are now sent to the ALL_EVENTS client to indicate the status of each
                                    peripheral associated with the PG.

Added AgentAvailabilityStatus and ICMAgentID fields to QUERY_AGENT_STATE_CONF
                                    and AGENT_STATE_EVENT.

Added field AgentsICMAvailable and AgentsApplicationAvailable to QUERY_SKILL_GROUP_STATISTICS_CONF.

Added fields ICMAvailableTimeSession, RoutableTimeSession, ICMAvailableTimeToday,
                                    and RoutableTimeToday to QUERY_AGENT_STATISTICS_CONF.

Added ICMAgentID, AgentExtension, AgentID, and AgentInstrument fields
                                    to QUERY_AGENT_STATE_REQ.

Updates to several tables in Chapter 6, “Constants and Status Codes.”

## Protocol Version
                        	 8

The following is a
                              		  list of additions and changes made to the CTI Server in Protocol Version 8 (ICM
                              		  Version 4.6).

Moved the
                                    				RTP_STARTED_EVENT and RTP_STOPPED_EVENT messages to the ClientEvents Service.

Added
                                    				AgentInstrument optional field to the following messages:

ALTERNATE_CALL_REQ

CLEAR_CALL_REQ

CONFERENCE_CALL_REQ

DEFLECT_CALL_REQ

HOLD_CALL_REQ

RECONNECT_CALL_REQ

RETRIEVE_CALL_REQ

TRANSFER_CALL_REQ

SEND_DTMF_SIGNAL_REQ

Added
                                    				CalledPartyDisposition field to the BEGIN_CALL_EVENT, CALL_DATA_UPDATE_EVENT,
                                    				and SNAPSHOT_CALL_CONF messages.

Added CallType
                                    				and CalledPartyDisposition fields to the SET_CALL_DATA_REQ message.

Added
                                    				BlendedAgent support.

Add
                                    				CALLTYPE_PREVIEW and CALLTYPE_RESERVATION call types (see table CallType Values ).

Add CallType
                                    				and/or CalledPartyDisposition fields to the set_call_data_req,
                                    				BEGIN_CALL_EVENT, CALL_DATA_ UPDATE_EVENT, and snapshot_call_conf messages.

Added
                                    				CampaignID and QueryRuleID fields to the SET_CALL_DATA_REQ and
                                    				CALL_DATA_UPDATE_EVENT messages.

Add real time
                                    				and 5 minutes fields to the query_skill_group_statistics_conf message.

Add new
                                    				AutoOut, Preview, and Reservation call metrics to the
                                    				query_AGENT_statistics_conf and query_skill_group_statistics_conf messages.

Added
                                    				SessionID field to the AGENT_STATE_EVENT message.

Add new
                                    				BargeIn, Intercept, Monitor, Whisper, and Emergency call metrics to the
                                    				query_AGENT_statistics_conf and query_skill_group_statistics_conf messages.

Added
                                    				Supervisor services. See Supervisor
                                       				  Service in Chapter 5, “Application Level Interfaces.”

Added the
                                    				following new messages:

SET_DEVICE_ATTRIBUTES_REQ / CONF

SUPERVISOR_ASSIST_REQ/CONF

EMERGENCY_CALL_REQ/CONF

SUPERVISE_CALL_REQ/CONF

AGENT_TEAM_CONFIG_REQ/CONF/EVENT

SET_APP_DATA_REQ/CONF

AGENT_DESK_SETTINGS_REQ/CONF

LIST_AGENT_TEAM_REQ/CONF

MONITOR_AGENT_TEAM_START_REQ/CONF

MONITOR_AGENT_TEAM_STOP_REQ/CONF

BAD_CALL_REQ/CONF

SET_DEVICE_ATTRIBUTES_REQ/CONF

REGISTER_SERVICE_REQ/CONF

UNREGISTER_SERVICE_REQ/CONF

START_RECORDING_REQ/CONF

STOP_RECORDING_REQ/CONF

Added the
                                    				CustomerPhoneNumber, and CustomerAccountNumber fields. Developers may receive
                                    				these fields in the CALL_DATA_UPDATE_EVENT messages.

## Protocol Version 7

The following is a list of additions and changes made to the CTI Server
                              in Protocol Version 7 (ICM Version 4.5).

Added the RTP_STARTED_EVENT and RTP_STOPPED_EVENT messages

Added skill group parameters to the CALL_DELIVERED_EVENT message.

Added LineHandle and LineType parameters to the CALL_REACHED_NETWORK_EVENT
                                    message.

## Protocol Version
                        	 6

The following is a
                              		  list of additions and changes made to the CTI Server in Protocol Version 6 (ICM
                              		  Version 4.1).

Added the
                                    				NAMEDVAR and NAMEDARRAY data types.

Added
                                    				ICRCentralControllerTime and SystemCapabilities fields to the OPEN_CONF and
                                    				SYSTEM_EVENT messages.

System Events
                                    				Service renamed to Miscellaneous Services.

NamedVariable
                                    				and NamedArray optional fields added to the following messages:

BEGIN_CALL_EVENT

CALL_DATA_UPDATE_EVENT

CALL_TRANSLATION_ROUTE_EVENT

SET_CALL_DATA_REQ

CONFERENCE_CALL_REQ

CONSULTATION_CALL_REQ

MAKE_CALL_REQ

MAKE_PREDICTIVE_CALL_REQ

TRANSFER_CALL_REQ

SNAPSHOT_CALL_CONF

EventReasonCode field added to the AGENT_STATE_EVENT message.

AGENT_PRE_CALL_EVENT and AGENT_PRE_CALL_ABORT_EVENT messages
                                    				added .

New messages
                                    				added to Miscellaneous Services:

USER_MESSAGE_REQ/CONF

USER_MESSAGE_EVENT

SUPERVISOR_ASSIST_REQ/CONF

EMERGENCY_CALL_REQ/CONF

QUERY_AGENT_STATISTICS_REQ/CONF

QUERY_SKILL_GROUP_STATISTICS_REQ/CONF

AgentExtension
                                    				and AgentID fields added tothe QUERY_AGENT_STATE_REQ message.

New values
                                    				SYS_CTI_SERVER_OFFLINE, SYS_CTI_SERVER_ONLINE, and SYS_HALF_HOUR_CHANGE added
                                    				to SystemEventID Values table (Table SystemEventID Values ).

Maximum length
                                    				of all instances of the AgentInstrument field increased from 12 to 64 bytes.

SystemCapabilities field removed from the OPEN_CONF and
                                    				SYSTEM_EVENT messages.

NumNamedVariables and NumNamedArrays fixed fields added to all
                                    				messages that contain the NamedVariable and NamedArray floating fields.

Supervisor
                                    				Service removed.

Queue
                                    				information added to the QUERY_SKILL_GROUP_STATISTICS_CONF message.

AgentInstrument field added to QUERY_AGENT_STATE_CONF message.

Added the
                                    				following fields to the QUERY_DEVICE_INFO_CONF message:

MaxActiveCalls

MaxHeldCalls

MaxDevicesInConference

MakeCallSetup

TransferConferenceSetup

CallEventsSupported

CallControlSupported

OtherFeaturesSupported

New PGStatus
                                    				code values PGS_CTI_SERVER_OFFLINE and PGS_LIMITED_FUNCTION added to the
                                    				PGStatusCode table (Table PGStatusCode Values ).

Added
                                    				HandledCallsAfterCallTimeSession and HandledCallsAfterCallTimeToday fields to
                                    				the QUERY_AGENT_STATISTICS_CONF message.

Added
                                    				HandledCallsAfterCallTimeToHalf and HandledCallsAfterCallTimeToday fields to
                                    				the QUERY_SKILL_GROUP_STATISTICS_CONF message.

New
                                    				Transfer/Conference Setup Mask values CONF_SETUP_SINGLE_ACD_CALL,
                                    				TRANS_SETUP_SINGLE_ACD_CALL, and TRANS_SETUP_ANY_SINGLE_CALL added to the
                                    				QUERY_DEVICE_INFO_CONF message.

New
                                    				SystemEventIDs SYS_INSTRUMENT_OUT_OF_SERVICE and SYS_INSTRUMENT_BACK_IN_SERVICE
                                    				added to the SystemEventID Values table (Table SystemEventID Values ).

Added
                                    				REGISTER_VARIABLES_REQ and REGISTER_VARIABLES_CONF messages.

Added
                                    				MonitorID field to AGENT_PRECALL_EVENT and AGENT_PRECALL_ABORT_EVENT messages.

PeripheralID
                                    				field added to the USER_MESSAGE_REQ message.

Updated
                                    				StatusCodes table (Table Failure Indication Message Status Codes ).

New LineTypes
                                    				LINETYPE_OUTBOUND and LINETYPE_DID added to the LineTypes table (Table 6-14
                                    				LineType Values).

Added
                                    				ServiceNumber, ServiceID, SkillGroupNumber, SkillGroupID, and
                                    				SkillGroupPriority fields to AGENT_PRECALL_EVENT message.

Added note for
                                    				CALL_ESTABLISHED_EVENT for Spectrum ACDs.

Added /CCT
                                    				(Call Control Table) optional field to the MAKE_CALL_REQ and
                                    				MAKE_PREDICTIVE_CALL_REQ messages.

## Protocol Version
                        	 5

The following is a
                              		  list of additions and changes made to the CTI Server in Protocol Version 5 (ICM
                              		  Version 4.0).

Added
                                    				Peripheral Monitor service and related messages.

Added a new
                                    				MonitorID field to all Call and Agent Event messages.

Added Client
                                    				Monitor service and related messages.

Added
                                    				CallingDeviceType and CallingDeviceID fields to the
                                    				CALL_SERVICE_INITIATED_EVENT message.

Increased the
                                    				maximum number of skill groups from 10 to 20.

Added
                                    				AlertRings, CallOption, AuthorizationCode, and AccountCode fields to the
                                    				CONSULTATION_CALL_REQ, MAKE_CALL_REQ, and TRANSFER_CALL_REQ messages.

Readded
                                    				MAKE_PREDICTIVE_CALL_REQ and MAKE_PREDICTIVE_CALL_CONF messages.

Added new
                                    				SYS_PERIPHERAL_GATEWAY_OFFLINE System Event ID to the SystemEventID Values
                                    				table (Table PeripheralType Values ).

Added new
                                    				AM_NONE, AM_NONE_NO_MODEM and AM_CONNECT_NO_MODEM AnsweringMachine values to
                                    				the AnsweringMachine Values table (Table AnsweringMachine Values ).

ANSWER_CALL_REQ message (Table SystemEventID Values )
                                    				revised for peripherals that do not provide alerting call identification.

Added fields
                                    				for single step conference to the CONFERENCE_CALL_REQ message:

CallPlacementType

CallMannerType

AlertRings

CallOption

FacilityType

Priority

PostRoute

DialedNumber

UserToUserInfo

CallVariable1 – CallVariable10

CallWrapupData

FacilityCode

AuthorizationCode

AccountCode

Replaced the
                                    				AgentInstrument field in the MAKE_PREDICTIVE_CALL_REQ message with the
                                    				OriginatingDevice field.

Added the
                                    				following new fields to the MAKE_PREDICTIVE_CALL_REQ message:

AnswerDetectMode

AnswerDetectTime

AnswerDetectControl1

AnswerDetectControl2

DestinationCountry

OriginatingLineID

PeripheralOnline field added to the OPEN_CONF message.

ClientPort
                                    				field added to the CLIENT_SESSION_OPENED_EVENT and CLIENT_SESSION_CLOSED_EVENT
                                    				messages.

Optional
                                    				AgentInstrument field added to the CLEAR_CONNECTION_REQ message.

AnsweringMachine field added to the CONFERENCE_CALL_REQ and
                                    				TRANSFER_CALL_REQ messages.

Optional
                                    				AgentInstrument field added to the CONSULTATION_CALL_REQ message.

Added the
                                    				symbolic constant NULL_CALL_ID to the Special Values table (Table Special
                                       				  Values Special Values).

New peripheral types PT_SIEMENS_9005 and PT_ALCATEL added to the PeripheralType Values table (Table PeripheralType Values ).

| Important | In the CTI Server Protocol Version 20 the floating field tag and length size changed from 1 byte to 2 byte USHORT. |
|---|---|