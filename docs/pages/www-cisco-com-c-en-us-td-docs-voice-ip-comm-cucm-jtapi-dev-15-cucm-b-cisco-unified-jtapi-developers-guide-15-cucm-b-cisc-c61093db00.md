---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-jtapi-dev-15-cucm-b-cisco-unified-jtapi-developers-guide-15-cucm-b-cisc-c61093db00
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/jtapi_dev/15/cucm_b_cisco-unified-jtapi-developers-guide-15/cucm_b_cisco-unified-jtapi-developers-guide-1251_appendix_01010.html
retrieved_at: 2026-08-16T18:04:18.178852+00:00
---

Cisco Unified JTAPI Developers Guide for Cisco Unified Communications Manager, Release 15 and SUs

# Cisco Unified JTAPI Developers Guide for Cisco Unified Communications Manager, Release 15 and SUs

Updated: July 31, 2025

Chapter: Troubleshooting Cisco Unified JTAPI

## Chapter: Troubleshooting Cisco Unified JTAPI

# Troubleshooting Cisco Unified JTAPI

This
                           		  appendix contains CTI Error Codes,  CiscoEvent IDs,  and other information to
                           		  assist with troubleshooting efforts.

## CTI Error Codes

Error code

Description

ASSOCIATED_LINE_NOT_OPEN

This error indicates that the request is issued on
                                          						a line, which is not open

CALL_ALREADY_EXISTS

This error indicates that another call already
                                          						exists on the line

CALL_DROPPED

The call dropped after the feature request (hold,
                                          						unhold, transfer, or conference) but before the request was completed.

CALLHANDLE_NOTINCOMINGCALL

This error indicates that an attempt is made to
                                          						answer a call that either does not exist or is not in the correct state

CALLHANDLE_UNKNOWN_TO_LINECONTROL

This error indicates that attempt to redirect call
                                          						that was unknown to line control

CANNOT_OPEN_DEVICE

This error indicates that device open failed
                                          						because the associated device is unregistering

CANNOT_TERMINATE_MEDIA_ON_PHONE

This error indicates that media cannot be
                                          						terminated by an application when the device is a physical phone (the phone
                                          						always terminates the media)

CFWDALL_ALREADY_SET

This error indicates that attempt to set CFWALL
                                          						while it is already set

CFWDALL_DESTN_INVALID

This error indicates that attempt to CFWALL to an
                                          						invalid destination

CLUSTER_LINK_FAILURE

This error indicates that link to one of the cisco
                                          						unified communications managers failed in the cluster (network error)

COMMAND_NOT_IMPLEMENTED_ON_DEVICE

This error indicates that device does not support
                                          						the command.

CONFERENCE_ALREADY_PRESENT

This error indicates that attempt to conference a
                                          						party that is already in conference

CONFERENCE_FAILED

This error indicates that conference completion was
                                          						not successful.

CONFERENCE_FULL

This error indicates that all conference bridges
                                          						are busy.

CONFERENCE_INACTIVE

This error indicates that attempt to complete
                                          						conference while consult conference is not active

CONFERENCE_INVALID_PARTICIPANT

This error indicates that an attempt to conference
                                          						to self or an invalid participant

CTIERR_ACCESS_TO_DEVICE_DENIED

This error indicates that the access to device is
                                          						denied.

CTIERR_APP_SOFTKEYS_ALREADY_CONTROLLED

This error indicates that the application softkeys
                                          						are already controlled by another application

CTIERR_APPLICATION_DATA_SIZE_EXCEEDED

This error indicates that application data size has
                                          						exceeded limit

CTIERR_BIB_NOT_CONFIGURED

This error indicates built in bridge is not
                                          						configured

CTIERR_BIB_RESOURCE_NOT_AVAILABLE

This error indicates that built in bridge resource
                                          						not available

CTIERR_CALL_MANAGER_NOT_AVAILABLE

This error indicates that Communications Manager is
                                          						not available currently

CTIERR_CALL_NOT_EXISTED

This error indicates that call does not exist

CTIERR_CALL_PARK_NO_DN

This error indicates no call park DN

CTIERR_CALL_REQUEST_ALREADY_OUTSTANDING

This error indicates call request already
                                          						outstanding

CTIERR_CALL_UNPARK_FAILED

This error indicates that call unpark did not
                                          						succeed

CTIERR_CAPABILITIES_DO_NOT_MATCH

This error indicates that capabilities do not match

CTIERR_CLOSE_DELAY_NOT_SUPPORTED_WITH_REG_TYPE

This error indicates that the close delay is not
                                          						supported with this registration type

CTIERR_CONFERENCE_ALREADY_EXISTED

This error indicates that conference already exists

CTIERR_CONFERENCE_NOT_EXISTED

This error indicates that conference does not exist

CTIERR_CONNECTION_ON_INVALID_PORT

This error indicates application is trying to
                                          						connect to invalid port

CTIERR_CONSULT_CALL_FAILURE

This error indicates consult call failure

CTIERR_CONSULTCALL_ALREADY_OUTSTANDING

This error indicates that consult call already
                                          						outstanding

CTIERR_CREATE_PERSISTENT_CALL_FAILED

This error indicates that there is an issue with creating a
                                          						persistent call.

CTIERR_CRYPTO_CAPABILITY_MISMATCH

This error indicates that device registration
                                          						failed as device crypto algorithms does not match with current device
                                          						registration

CTIERR_CTIHANDLER_PROCESS_CREATION_FAILED

This error indicates that CTIHandler process
                                          						creation failed

CTIERR_DB_INITIALIZATION_ERROR

This error indicates DB initialization error

CTIERR_DEVICE_ALREADY_OPENED

This error indicates that device is already opened

CTIERR_DEVICE_ALREADY_REGISTERED_NONEXTEND

Device registration failed as device is already
                                          						registered in Non-Extend mode.

CTIERR_DEVICE_NOT_OPENED_YET

This error indicates that device is not yet opened

CTIERR_DEVICE_OWNER_ALIVE_TIMER_STARTED

This error indicates that there is a device
                                          						registration failure

CTIERR_DEVICE_REGISTRATION_FAILED_ NOT_SUPPORTED_MEDIATYPE

This error indicates an invalid media type, CTIPort
                                          						need to be registered with Dynamic media port registation if it has an intercom
                                          						line

CTIERR_DEVICE_RESTRICTED

This error indicates that the device is restricted

CTIERR_DEVICE_SHUTTING_DOWN

This error indicates that device is shutting down

CTIERR_DIRECTORY_LOGIN_TIMEOUT

This error indicates that there is a directory
                                          						login time out

CTIERR_DISCONNECT_PERSISTENT_CALL_FAILED_ CALL_ACTIVE

This error indicates that the request to disconnect the
                                          						persistent call failed because there is an active customer call. Only when
                                          						there are no active calls present, can the persistent call be disconnected.

CTIERR_DUPLICATE_CALL_REFERENCE

This error indicates duplicate call reference

CTIERR_DUPLICATE_REMOTE_DESTINATION_NUMBER

Duplicated Remote Destination Number with an
                                          						existing Remote Destination Number.

CTIERR_DYNREG_IPADDRMODE_MISMATCH

This indicates registration failure when Cisco
                                          						Media/Route Tterminal is already registered with different Addressing mode

CTIERR_ENDUSER_NOT_ASSOCIATED_WITH_DEVICE

Enduser is not associated with the device.

CTIERR_FAC_CMC_REASON_CMC_INVALID

Client Matter Code (CMC) entered is invalid

CTIERR_FAC_CMC_REASON_CMC_NEEDED

CMC is required to offer the call

CTIERR_FAC_CMC_REASON_FAC_CMC_NEEDED

Forced Authorization Code (FAC) and CMC are
                                          						required to offer call

CTIERR_FAC_CMC_REASON_FAC_INVALID

FAC entered is invalid

CTIERR_FAC_CMC_REASON_FAC_NEEDED

FAC is required to offer the call

CTIERR_FEATURE_ALREADY_REGISTERED

This error indicates feature already registered

CTIERR_FEATURE_DATA_REJECT

This error indicates feature data reject

CTIERR_FEATURE_SELECT_FAILED

This error indicates that feature select failed

CTIERR_ILLEGAL_DEVICE_TYPE

This error indicates that the device type is
                                          						illegal

CTIERR_INCOMPATIBLE_AUTOINSTALL_PROTOCOL_ VERSION

This error indicates that auto install protocol
                                          						version is incompatible

CTIERR_INCORRECT_MEDIA_CAPABILITY

This error indicates that device registration
                                          						failed due to incorrect media capability

CTIERR_INFORMATION_NOT_AVAILABLE

This error indicates that information is not
                                          						available

CTIERR_INTERCOM_SPEEDDIAL_ALREADY_CONFIGURED

This error indicates that intercom target value is
                                          						already configured, application is trying to make call with Intercom target DN

CTIERR_INTERCOM_SPEEDDIAL_ALREADY_SET

This error indicates that intercom request failed
                                          						as intercom target value is already set, application is trying to set again

CTIERR_INTERCOM_SPEEDDIAL_DESTN_INVALID

This error indicates that intercomm request failed
                                          						as intercom target value in not in the intercom group

CTIERR_INTERCOM_TALKBACK_ALREADY_PENDING

This error indicates that intercom talk back
                                          						request is already pending

CTIERR_INTERCOM_TALKBACK_FAILURE

This error indicates that talkback request failed
                                          						for some reason

CTIERR_INTERNAL_FAILURE

This error indicates there is a CTI internal
                                          						failure

CTIERR_INVALID_CALLID

This error indicates the call ID is invalid

CTIERR_INVALID_DEVICE_NAME

This error indicates that the device name is not
                                          						valid

CTIERR_INVALID_DTMFDIGITS

Play DTMF request failed because it is an invalid
                                          						DTMF digit

CTIERR_INVALID_FILTER_SIZE

This error indicates that filter size is invalid

CTIERR_INVALID_MEDIA_DEVICE

This error indicates that the media device is not
                                          						valid

CTIERR_INVALID_MEDIA_PARAMETER

This error indicates media parameter is invalid

CTIERR_INVALID_MEDIA_PROCESS

This error indicates that there is an invalid
                                          						media process

CTIERR_INVALID_MEDIA_RESOURCE_ID

This error indicates media resource ID is not
                                          						valid

CTIERR_INVALID_MESSAGE_HEADER_INFO

This error indicates that the header info is not
                                          						valid

CTIERR_INVALID_MESSAGE_LENGTH

This error indicates that message length is
                                          						invalid

CTIERR_INVALID_MONITOR_DESTN

This error indicates monitoring request failed due
                                          						to invalid monitoring destination

CTIERR_INVALID_MONITOR_DN_TYPE

This error indicates an invalid monitor DN type

CTIERR_INVALID_MONITORMODE

This error indicates monitor request failed due to
                                          						an invalid monitor mode

CTIERR_INVALID_PARAMETER

This error indicates that the parameter is not
                                          						valid

CTIERR_INVALID_PARK_DN

This error indicates that the DN is an invalid
                                          						park DN

CTIERR_INVALID_PARK_REGISTRATION_HANDLE

This error indicates that the handle is an invalid
                                          						park registration handle

CTIERR_PERSISTENT_CALL_EXISTS

This error indicates that a persistent call already exists.

CTIERR_INVALID_REMOTE_DESTINATION_NAME

This error indicates an Invalid Remote Destination
                                          						Name.

CTIERR_INVALID_REMOTE_DESTINATION_NUMBER

This error indicates an Invalid Remote Destination
                                          						Number.

CTIERR_INVALID_RESOURCE_TYPE

This error indicates an invalid resource type

CTIERR_IPADDRMODE_MISMATCH

This indicates the registration failure due to IP
                                          						Addressing Mode mismatch.

CTIERR_LINE_OUT_OF_SERVICE

This error indicates that line is out of service.

CTIERR_LINE_RESTRICTED

This er ror indicates that the line is restricted

CTIERR_MAXCALL_LIMIT_REACHED

This error indicates that maximum call limit has
                                          						reached

CTIERR_MEDIA_ALREADY_TERMINATED_DYNAMIC

This error indicates that device registration
                                          						failed as device is registered with Dynamic media termination

CTIERR_MEDIA_ALREADY_TERMINATED_EXTEND

Device registration failed as device is already
                                          						registered in Extend mode.

CTIERR_MEDIA_ALREADY_TERMINATED_NONE

This error indicates that device registration
                                          						failed as device is already registered with media termination none

CTIERR_MEDIA_ALREADY_TERMINATED_STATIC

This error indicates that device registration
                                          						failed as device is registered with Static media termination

CTIERR_MEDIA_CAPABILITY_MISMATCH

This error indicates that device registration
                                          						failed as media capability of device does not match with current device
                                          						registration

CTIERR_MEDIA_RESOURCE_NAME_SIZE_EXCEEDED

This error indicates that media resource name size
                                          						has exceeded limit

CTIERR_MEDIAREGISTRATIONTYPE_DO_NOT_MATCH

This error indicates that media registration types
                                          						do not match

CTIERR_MESSAGE_TOO_BIG

This error indicates that message is too big

CTIERR_MORE_ACTIVE_CALLS_THAN_RESERVED

This error indicates that there are more active
                                          						calls than reserved

CTIERR_NO_EXISTING_CALLS

This error indicates there are no existing calls

CTIERR_NO_EXISTING_CONFERENCE

This error indicates that there is no existing
                                          						conference

CTIERR_NO_RECORDING_SESSION

This error indicates recording request failed as
                                          						there is no recording session

CTIERR_NO_RESPONSE_FROM_MP

This error indicates no response from media
                                          						resource

CTIERR_NOT_PRESERVED_CALL

This error indicates that the call is not
                                          						preserved

CTIERR_OPERATION_FAILED_QUIETCLEAR

This error indicates that feature unavailable for
                                          						this call due to temporary failure

CTIERR_OPERATION_NOT_ALLOWED

This error indicates that this operation is not
                                          						allowed

CTIERR_OPERATION_NOT_ALLOWED_ON_ PERSISTENT_CALL

This indicates that the specified operation is not allowed
                                          						on a persistent call.

CTIERR_OUT_OF_BANDWIDTH

This error indicates out of bandwidth error

CTIERR_OWNER_NOT_ALIVE

This error indicates a failure during registering
                                          						the device

CTIERR_PENDING_ACCEPT_OR_ANSWER_REQUEST

This error indicates that there is a pending
                                          						accept or answer request

CTIERR_PENDING_START_MONITORING_REQUEST

This error indicates there is a pending start
                                          						monitoring request

CTIERR_PENDING_START_RECORDING_REQUEST

This error indicates there is a pending start
                                          						recording request

CTIERR_PENDING_STOP_RECORDING_REQUEST

This error indicates there is a pending stop
                                          						recording request

CTIERR_PERSISTENT_CALL_BEING_SETUP

This error indicates that the request failed because a
                                          						persistent call is already being set up.

CTIERR_PRIMARY_CALL_INVALID

This error indicates that primary call in
                                          						monitoring request in invalid or gone idle

CTIERR_PRIMARY_CALL_STATE_INVALID

This error indicates that primary call in
                                          						monitoring request is in invalid state

CTIERR_RECORDING_ALREADY_INPROGRESS

This error indicates recording request failed that
                                          						recording is already in progress

CTIERR_RECORDING_CONFIG_NOT_MATCHING

This error indicates recording configuration does
                                          						not match

CTIERR_RECORDING_INVOCATION_TYPE_NOT_MATCHING

Stop recording failed because the recording
                                          						invocation type did not match.

CTIERR_RECORDING_SESSION_INACTIVE

This error indicates recording request failed
                                          						because recording session is inactive

CTIERR_REDIRECT_UNAUTHORIZED_COMMAND_USAGE

This error indicates a redirect unauthorized
                                          						command usage

CTIERR_REGISTER_FEATURE_ACTIVATION_FAILED

This error indicates that register feature
                                          						activation failed

CTIERR_REGISTER_FEATURE_APP_ALREADY_REGISTERED

Register feature application was already
                                          						registered

CTIERR_REGISTER_FEATURE_PROVIDER_NOT_REGISTERED

Register feature provider was not registered.

CTIERR_REMOTE_DEVICE_REQUEST_FAILED_ ACTIVE_RD_NOT_SET

The active remote destination is not set.

CTIERR_REMOTEDESTINATION_LIMIT_EXCEEDED

The number of Remote Destinations has exceeded the
                                          						max number limit.

CTIERR_RESOURCE_NOT_AVAILABLE

This error indicates that resource is not
                                          						available to fulfill the request

CTIERR_START_MONITORING_FAILED

This error indicates that start monitoring request
                                          						failed

CTIERR_START_RECORDING_FAILED

This error indicates that start recording request
                                          						failed

CTIERR_STATION_SHUT_DOWN

This error indicates that there is a station
                                          						shutdown

CTIERR_SYSTEM_ERROR

This error indicates CTI system error

CTIERR_UDP_PASS_THROUGH_NOT_SUPPORTED

This error indicates UDP data passthrough not
                                          						supported

CTIERR_UNKNOWN_EXCEPTION

This error indicates an unknown exception occured

CTIERR_UNSUPPORTED_CALL_PARK_TYPE

This error indicates that call park type is not
                                          						supported

CTIERR_UNSUPPORTED_CFWD_TYPE

This error indicates that the call forward type is
                                          						unsupported

CTIERR_USER_NOT_AUTH_FOR_SECURITY

This error indicates user is not authorized for
                                          						secure connection

DARES_INVALID_REQ_TYPE

This error indicates that there is an internal
                                          						call processing error: DaRes invalid request type

DATA_SIZE_LIMIT_EXCEEDED

This error indicates that XML data object size is
                                          						bigger than allowed.

DB_ERROR

This error indicates that the device query
                                          						contained an illegal device type

DB_ILLEGAL_DEVICE_TYPE

This error indicates illegal device type in DB

DB_NO_MORE_DEVICES

This error is no longer used.

DESTINATION_BUSY

This error indicates that destination is busy

DESTINATION_UNKNOWN

This error indicates that destination is not found

DEVICE_ALREADY_REGISTERED

This error indicates that device registration
                                          						attempt failed, because the device is already registered

DEVICE_NOT_OPEN

This error indicates that an attempt to open a
                                          						line failed, as the device is not opened or the device is not registered.

DEVICE_OUT_OF_SERVICE

This error indicates that device is out of
                                          						service.

DIGIT_GENERATION_ALREADY_IN_PROGRESS

This error indicates that digit generation is
                                          						already in progress.

DIGIT_GENERATION_CALLSTATE_CHANGED

This error indicates that call state is invalid to
                                          						continue.

DIGIT_GENERATION_WRONG_CALL_HANDLE

This error indicates that call handle is invalid
                                          						and call may be gone.

DIGIT_GENERATION_WRONG_CALL_STATE

This error indicates that call state is not valid
                                          						to generate digits.

DIRECTORY_LOGIN_FAILED

This error indicates that directory login failed:
                                          						directory not initialized

DIRECTORY_LOGIN_NOT_ALLOWED

This error indicates that directory login failed

DIRECTORY_TEMPORARY_UNAVAILABLE

This error indicates that directory is temporarily
                                          						unavailable.

EXISTING_FIRSTPARTY

This error indicates that there is already a
                                          						device controlling media.

HOLDFAILED

This error indicates that the hold was rejected by
                                          						line control or call control layers

ILLEGAL_CALLINGPARTY

This error indicates that an attempt was made to
                                          						originate call using a calling party that is not on the device

ILLEGAL_CALLSTATE

This error indicates line is not in a legal state
                                          						to invoke the request

ILLEGAL_HANDLE

This error indicates the handle is not valid

ILLEGAL_MESSAGE_FORMAT

This error indicates that there is a QBE protocol
                                          						error

INCOMPATIBLE_PROTOCOL_VERSION

This error indicates that JTAPI and CTI versions
                                          						are not compatible : CTI Error Protocol version not supported

INVALID_LINE_HANDLE

This error indicates that attempt to perform a
                                          						line operation on an invalid line handle.

INVALID_RING_OPTION

This error indicates that the ring option is
                                          						invalid

LINE_GREATER_THAN_MAX_LINE

This error indicates that line is greater than the
                                          						maximum available lines on this device

LINE_INFO_DOES_NOT_EXIST

This error indicates that line information does
                                          						not exist in the database.

LINE_NOT_PRIMARY

This error indicates that internal error returned
                                          						from call control.

LINECONTROL_FAILURE

This error indicates line control refuses to allow
                                          						a new call to be initiated because of its current state.

MAX_NUMBER_OF_CTI_CONNECTIONS_REACHED

The maximum number of CTI connections was reached.

MSGWAITING_DESTN_INVALID

This error indicates that attempt to set message
                                          						waiting lamp for an invalid DN; Message Waiting Destination not found.

NO_ACTIVE_DEVICE_FOR_THIRDPARTY

This error indicates there is no active device for
                                          						thirdparty

NO_CONFERENCE_BRIDGE

This error indicates that no conference bridge
                                          						available

NOT_INITIALIZED

This error indicates that attempt is made to open
                                          						a provider before CTI initialization completes

PROTOCOL_TIMEOUT

Internal error returned from call control

PROVIDER_ALREADY_OPEN

This error indicates that an attempt is made to
                                          						reopen provider

PROVIDER_CLOSED

This error indicates an attempt to close provider
                                          						while it is already closed

PROVIDER_NOT_OPEN

This error indicates that device list incomplete
                                          						or device list query timeout or query aborted

REDIRECT_CALL_CALL_TABLE_FULL

This error indicates that internal error is
                                          						returned from call control

REDIRECT_CALL_DESTINATION_BUSY

This error indicates that the redirect destination
                                          						is busy

REDIRECT_CALL_DESTINATION_OUT_OF_ORDER

This error indicates that redirect destination is
                                          						out of order

REDIRECT_CALL_DIGIT_ANALYSIS_TIMEOUT

This error indicates a digit analyss time out,
                                          						this is an internal error returned from call control

REDIRECT_CALL_DOES_NOT_EXIST

This error indicates that an attempt is made to
                                          						redirect a call that does not exist or is not longer active

REDIRECT_CALL_INCOMPATIBLE_STATE

This error indicates that internal error is
                                          						returned from call control

REDIRECT_CALL_MEDIA_CONNECTION_FAILED

This error indicates media connection failure,
                                          						this is an internal error returned from call control

REDIRECT_CALL_NORMAL_CLEARING

This error indicates that redirect failed because
                                          						of normal call clearing

REDIRECT_CALL_ORIGINATOR_ABANDONED

This error indicates that far end hung up on the
                                          						call being redirected

REDIRECT_CALL_PARTY_TABLE_FULL

This error indicates that internal error is
                                          						returned from call control

REDIRECT_CALL_PENDING_REDIRECT_TRANSACTION

This error indicates that internal error is
                                          						returned from call control

REDIRECT_CALL_PROTOCOL_ERROR

This error indicates a protocol error, this is an
                                          						internal error returned from call control

REDIRECT_CALL_UNKNOWN_DESTINATION

This error indicates that an attempt is made to
                                          						redirect to an unknown destination

REDIRECT_CALL_UNKNOWN_ERROR

This error indicates that internal error is
                                          						returned from call control

REDIRECT_CALL_UNKNOWN_PARTY

This error indicates an unknown party is detected,
                                          						this is an internal error returned from call control

REDIRECT_CALL_UNRECOGNIZED_MANAGER

This error indicates that internal error is
                                          						returned from call control

REDIRECT_CALLINFO_ERR

This error indicates that internal error is
                                          						returned from call control

REDIRECT_ERR

This error indicates that internal error is
                                          						returned from call control

RETRIEVEFAILED

This error indicates that retrieval of call was
                                          						rejected by line control or call control

RETRIEVEFAILED_ACTIVE_CALL_ON_LINE

This error indicates that error occurred in
                                          						retrieving held call; because there is already another active call on the line

SSAPI_NOT_REGISTERED

This error indicates that the redirect command was
                                          						issued when the internal supporting interface was not initialized; either CTI
                                          						has not yet finished its initialization or an internal error occurred

TIMEOUT

This error indicates that the request has timed
                                          						out.

TRANSFER_INACTIVE

This error indicates that attempt to complete
                                          						transfer, while consult tranfer is not there

TRANSFERFAILED

This error indicates that the transfer failed
                                          						probably because one of the call legs was hung up or disconnected from the far
                                          						end

TRANSFERFAILED_CALLCONTROL_TIMEOUT

This error indicates that expected response from
                                          						call control not received during a transfer

TRANSFERFAILED_DESTINATION_BUSY

This error indicates that an attempt is made to
                                          						transfer call to a busy destination

TRANSFERFAILED_DESTINATION_UNALLOCATED

This error indicates an attempt is made to to
                                          						transfer call to a directory number that is not registered

TRANSFERFAILED_OUTSTANDING_TRANSFER

This error indicates that existing transfer is
                                          						still in progress

UNDEFINED_LINE

This error indicates that the line that was
                                          						specified, is not found on the device

UNKNOWN_GLOBAL_CALL_HANDLE

This error indicates that the global call handle
                                          						is unknown

UNRECOGNIZABLE_PDU

This error indicates that there is a QBE protocol
                                          						error

UNSPECIFIED

This error indicates that an unspecified error has
                                          						occurred.

## CiscoEventIDs

### Provider Events

Event name

Event number

CiscoProvFeatureUnRegisteredEv

0x40000008

CiscoRestrictedEv

0x40000009

CiscoAddrRestrictedEv

0x40000010

CiscoTermRestrictedEv

0x40000011

CiscoAddrActivatedEv

0x40000012

CiscoTermActivatedEv

0x40000013

CiscoAddrActivatedOnTerminalEv

0x40000014

CiscoAddrRestrictedOnTerminalEv

0x40000015

CiscoProviderCapabilityChangedEv

0x40000016

CiscoProvTerminalCapabilityChangedEv

0x40000017

CiscoProvTerminalRegisteredEv

0x40000018

CiscoProvTerminalUnRegisteredEv

0x40000019

CiscoProvTerminalRemoteDestinationChangedEv

0x40000020

CiscoProvTerminalIPAddressChangedEv

0x40000021

CiscoProvTerminalMultiMediaCapabilityChangedEv

0x40000022

### Terminal Events

Event name

Event number

CiscoTermCreatedEv

0x40001001

CiscoTermDataEv

0x40001002

CiscoTermInServiceEv

0x40001003

CiscoTermOutOfServiceEv

0x40001004

CiscoTermRemovedEv

0x40001005

CiscoTermDeviceActiveStatusEv

0x40001006

CiscoTermDeviceAlertingStatusEv

0x40001007

CiscoTermDeviceHoldStatusEv

0x40001008

CiscoTermDeviceIdleStatusEv

0x40001009

CiscoTermButtonPressedEv

0x40001010

CiscoTermRegistraionFailedEv

0x40001011

CiscoTermDNDStatusChangedEv

0x40001014

CiscoTermDeviceStateWhisperEv

0x40001015

CiscoTermDNDOptionChangedEv

0x40001016

CiscoMultiMediaStreamsInfoEv

0x40001017

### Address
                           	 Events

Event name

Event number

CiscoAddrCreatedEv

0x40002001

CiscoAddrInServiceEv

0x40002002

CiscoAddrOutOfServiceEv

0x40002003

CiscoAddrRemovedEv

0x40002004

CiscoOutOfServiceEv

0x40002005

CiscoAddrAddedToTerminalEv

0x40002006

CiscoAddrRemovedFromTerminalEv

0x40002007

CiscoAddrAutoAcceptStatusChangedEv

0x40002008

CiscoAddrIntercomInfoChangedEv

0x40002009

CiscoAddrIntercomInfoRestorationFailedEv

0x40002010

CiscoAddrRecordingConfigChangedEv

0x40002011

CiscoAddrParkStatusEv

0x40002012

CiscoAddrVoiceMailPilotChangedEv

0x40002013

CiscoAddrPickupGroupChangedEv

0x40002014

CiscoAddrMonitoringTerminatedEv

0x4000200A

### Call
                           	 Events

Event name

Event number

CiscoProvCallParkEv

0x40003001

CiscoConferenceEndEv

0x40003002

CiscoConferenceStartEv

0x40003003

CiscoConsultCallActiveEv

0x40003004

CiscoTransferEndEv

0x40003005

CiscoTransferStartEv

0x40003006

CiscoToneChangedEv

0x40003007

CiscoCallChangedEv

0x40003008

CiscoConferenceChainAddedEv

0x40003009

CiscoConferenceChainRemovedEv

0x40003010

CiscoCallSecurityStatusChangedEv

0x40003011

CiscoCallFeatureCancelledEv

0x40003012

CiscoProvPickupCallAlertEv

0x40003013

CiscoProvPickupNotificationRegistrationClosedEv

0x40003014

CiscoCallInfoChangedEv

0x40003015

CiscoProvAuthenticationInfoEv

0x40003016

### RTP Events

Event name

Event number

CiscoRTPInputStartedEv

0x40004001

CiscoRTPInputStoppedEv

0x40004002

CiscoRTPOutputStartedEv

0x40004003

CiscoRTPOutputStoppedEv

0x40004004

CiscoMediaOpenLogicalChannelEv

0x40004005

CiscoRTPInputKeyEv

0x40004006

CiscoRTPOutputKeyEv

0x40004007

CiscoMediaOpenIPPortEv

0x40004008

### TermConn
                           	 Events

Event name

Event number

CiscoTermConnPrivacyChangedEv

0x40005001

CiscoCallCtlTermConnHeldReversionEv

0x40005002

CiscoTermConnSelectChangedEv

0x40005003

CiscoTermConnRecordingStartEv

0x40005004

CiscoTermConnRecordingEndEv

0x40005005

CiscoTermConnRecordingFailedEv

0x4000500E

CiscoTermConnMonitoringStartEv

0x40005006

CiscoTermConnMonitoringEndEv

0x40005007

CiscoTermConnRecordingTargetInfoEv

0x40005008

CiscoTermConnMonitorInitiatorInfoEv

0x40005009

CiscoTermConnMonitorTargetInfoEv

0x4000500A

CiscoTermConnMonitorUpdatedEv

0x4000500B

CiscoMediaStreamStartedEv

0x4000500C

CiscoMediaStreamEndedEv

0x4000500D

### Conn
                           	 Events

Event name

Event number

CiscoConnectionUniqueIDChangedEv

0x40006001

CiscoHuntConnCreatedEv

0x40006002

## Reason
                        	 Codes

The
                              		  following codes are defined in CiscoFeatureReason interface.

Reason code name

Reason code

REASON_TRANSFER

2

REASON_FORWARDNOANWSER

3

REASON_FORWARDBUSY

4

REASON_FORWARDALL

5

REASON_REDIRECT

6

REASON_BLINDTRANSFER

7

REASON_CONFERENCE

9

REASON_PARK

10

REASON_CALLPICKUP

11

REASON_NORMAL

12

REASON_PARKREMINDER

15

REASON_UNPARK

16

REASON_BARGE

20

REASON_IMMDIVERT

21

REASON_FAC_CMC

22

REASON_QSIG_PR

23

REASON_REFER

24

REASON_REPLACE

25

REASON_CCM_REDIRECTION

26

REASON_DPARK_CALLPARK

27

REASON_DPARK_REVERSION

28

REASON_DPARK_UNPARK

29

REASON_SILENTMONITORING

31

REASON_MOBILITY

33

REASON_MOBILITY_IVR

34

REASON_MOBILITY_CELLPICKUP

35

REASON_MOBILITY_HANDIN

36

REASON_MOBILITY_HANDOUT

37

REASON_MOBILITY_FOLLOWME

38

REASON_CLICK_TO_CONFERENCE

39

REASON_FORWARD_NO_RETRIEVE

40

REASON_EXTERNALCALLCONTROL

42

REASON_SAF_CCD_PSTN_FAILOVER

43

REASON_MEDIA_STREAMING

44

## Cause
                        	 Codes

Cause code name

Cause code

CAUSE_NOERROR

0X00 (0)

CAUSE_UNALLOCATEDNUMBER

0X01 (1)

CAUSE_NOROUTETOTRANSITNET

0X02 (2)

CAUSE_NOROUTETODDESTINATION

0X03 (3)

CAUSE_CHANUNACCEPTABLE

0X06 (6)

CAUSE_CALLBEINGDELIVERED

0X07 (7)

CAUSE_CTIPREEMPTNOREUSE

0X08 (8)

CAUSE_CTIPREEMPTFORREUSE

0X09 (9)

CAUSE_NORMALCALLCLEARING

0X10 (16)

CAUSE_USERBUSY

0X11 (17)

CAUSE_NOUSERRESPONDING

0X12 (18)

CAUSE_NOANSWERFROMUSER

0X13 (19)

CAUSE_SUBSCRIBERABSENT

0X14 (20)

CAUSE_CALLREJECTED

0X15 (21)

CAUSE_NUMBERCHANGED

0X16 (22)

CAUSE_EXCHANGEROUTINGERROR

0X19 (25)

CAUSE_NONSELECTEDUSERCLEARING

0X1A (26)

CAUSE_DDESTINATIONOUTOFORDER

0X1B (27)

CAUSE_INVALIDNUMBERFORMAT

0X1C (28)

CAUSE_FACILITYREJECTED

0X1D (29)

CAUSE_RESPONSETOSTATUSENQUIRY

0X1E (30)

CAUSE_NORMALUNSPECIFIED

0X1F (31)

CAUSE_NOCIRCAVAIL

0X22 (34)

CAUSE_NETOUTOFORDER

0X26 (38)

CAUSE_TEMPORARYFAILURE

0X29 (41)

CAUSE_SWITCHINGEQUIPMENTCONGESTION

0X2A (42)

CAUSE_ACCESSINFORMATIONDISCARDED

0X2B (43)

CAUSE_REQCIRCNAVIL

0X2C (44)

CAUSE_CTIPRECEDENCECALLBLOCKED

0X2E (46)

CAUSE_RESOURCESNAVAIL

0X2F (47)

CAUSE_QUALOFSERVNAVAIL

0X31 (49)

CAUSE_REQFACILITYNOTSUBSCRIBED

0X32 (50)

CAUSE_SERVOPERATIONVIOLATED

0X35 (53)

CAUSE_INCOMINGCALLBARRED

0X36 (54)

CAUSE_BCNAUTHORIZED

0X39 (57)

CAUSE_BCBPRESENTLYAVAIL

0X3A (58)

CAUSE_SERVNOTAVAILUNSPECIFIED

0X3F (63)

CAUSE_BEARERCAPNIMPL

0X41 (65)

CAUSE_CHANTYPENIMPL

0X42 (66)

CAUSE_REQFACILITYNIMPL

0X45 (69)

CAUSE_ONLYRDIVEARERCAPAVAIL

0X46 (70)

CAUSE_SERVOROPTNAVAILORIMPL

0X4F (79)

CAUSE_INVALIDCALLREFVALUE

0X51 (81 )

CAUSE_IDENTIFIEDCHANDOESNOTEXIST

0X52 (82)

CAUSE_SUSPCALLBUTNOTTHISONE

0X53 (83)

CAUSE_CALLIDINUSE

0X54 (84)

CAUSE_NOCALLSUSPENDED

0X55 (85)

CAUSE_REQCALLIDHASBEENCLEARED

0X56 (86)

CAUSE_INCOMPATABLEDDESTINATION

0X58 (88)

CAUSE_DESTNUMMISSANDDCNOTSUB

0X5A (90)

CAUSE_INVALIDTRANSITNETSEL

0X5B (91)

CAUSE_INVALIDMESSAGEUNSPECIFIED

0X5F (95)

CAUSE_MANDATORYIEMISSING

0X60 (96)

CAUSE_MSGTYPENIMPL

0X61 (97)

CAUSE_MSGTYPENCOMPATWCS

0X62 (98)

CAUSE_IENIMPL

0X63 (99)

CAUSE_INVALIDIECONTENTS

0X64 (100)

CAUSE_MSGNCOMPATABLEWCS

0X65 (101)

CAUSE_RECOVERYONTIMEREXPIRY

0X66 (102)

CAUSE_PROTOCOLERRORUNSPECIFIED

0X6F (111)

CAUSE_CTIPRECEDENCELEVELEXCEEDED

0X7A (122)

CAUSE_CTIDEVICENOTPREEMPTABLE

0X7B (123)

CAUSE_OUTOFBANDWIDTH

0X7D (125)

CAUSE_INTERWORKINGUNSPECIFIED

0X7F (127)

CAUSE_CTIPRECEDENCEOUTOFBANDWIDTH

0X81 (129)

CAUSE_REDIRECTED

0XC9 (200)

CAUSE_INTERNALCAUSE

0X1F4 (500)

CAUSE_OUTBOUND_TRANSFER

0X1F5 (501)

CAUSE_OUTBOUND_CONFERENCE

0X1F6 (502)

CAUSE_INBOUND_TRANSFER

0X1F7 (503)

CAUSE_INBOUND_CONFERENCE

0X1F8 (504)

CAUSE_INBOUND_BLINDTRANSFER

0X1F9 (505)

CAUSE_CTIMANAGER_FAILURE

0x1FB (507)

CAUSE_CALLMANAGER_FAILURE

0x1FC (508)

CAUSE_BARGE

0x1FD(509)

CAUSE_FAC_CMC

0x1FE (510)

CAUSE_QSIG_PR

0x1FF (511)

CAUSE_DPARK

0x200 (512)

CAUSE_DPARK_UNPARK

0x201 (513)

CAUSE_DPARK_REMINDER

0x202 (514)

CAUSE_QUIET_CLEAR

0x203 (515)

CAUSE_CTICONFERENCEFULL

0X40000 + CAUSE_NOERROR

CAUSE_CALLSPLIT

0X60000 + CAUSE_NOERROR

CAUSE_CTIDROPCONFEREE

0X70000 + CAUSE_NOERROR

CAUSE_CTICCMSIP400BADREQUEST

0X1000000 + CAUSE_TEMPORARYFAILURE

CAUSE_CTICCMSIP401UNAUTHORIZED

0X2000000 + CAUSE_CALLREJECTED

CAUSE_CTICCMSIP402PAYMENTREQUIRED

0X3000000 + CAUSE_CALLREJECTED

CAUSE_CTICCMSIP403FORBIDDEN

0X4000000 + CAUSE_CALLREJECTED

CAUSE_CTICCMSIP404NOTFOUND

0X5000000 + CAUSE_UNALLOCATEDNUMBER

CAUSE_CTICCMSIP405METHODNOTALLOWED

0X6000000 + CAUSE_SERVNOTAVAILUNSPECIFIED

CAUSE_CTICCMSIP406NOTACCEPTABLE

0X7000000 + CAUSE_SERVOROPTNAVAILORIMPL

CAUSE_CTICCMSIP407PROXYAUTHENTICATIONREQUIRED

0X8000000 + CAUSE_CALLREJECTED

CAUSE_CTICCMSIP408REQUESTTIMEOUT

0X9000000 + CAUSE_RECOVERYONTIMEREXPIRY

CAUSE_CTICCMSIP410GONE

0XB000000 + CAUSE_NUMBERCHANGED

CAUSE_CTICCMSIP411LENGTHREQUIRED

0XC000000 + CAUSE_INTERWORKINGUNSPECIFIED

CAUSE_CTICCMSIP413REQUESTENTITYTOOLONG

0XE000000 + CAUSE_INTERWORKINGUNSPECIFIED

CAUSE_CTICCMSIP414REQUESTURITOOLONG

0XF000000 + CAUSE_INTERWORKINGUNSPECIFIED

CAUSE_CTICCMSIP415UNSUPPORTEDMEDIATYPE

0X10000000 + CAUSE_SERVOROPTNAVAILORIMPL

CAUSE_CTICCMSIP416UNSUPPORTEDURISCHEME

0X11000000 + CAUSE_INTERWORKINGUNSPECIFIED

CAUSE_CTICCMSIP420BADEXTENSION

0X15000000 + CAUSE_INTERWORKINGUNSPECIFIED

CAUSE_CTICCMSIP421EXTENSTIONREQUIRED

0X16000000 + CAUSE_INTERWORKINGUNSPECIFIED

CAUSE_CTICCMSIP423INTERVALTOOBRIEF

0X18000000 + CAUSE_INTERWORKINGUNSPECIFIED

CAUSE_CTICCMSIP480TEMPORARILYUNAVAILABLE

0X40000000 + CAUSE_NOUSERRESPONDING

CAUSE_CTICCMSIP481CALLLEGDOESNOTEXIST

0X41000000 + CAUSE_TEMPORARYFAILURE

CAUSE_CTICCMSIP482LOOPDETECTED

0X42000000 + CAUSE_EXCHANGEROUTINGERROR

CAUSE_CTICCMSIP483TOOMANYHOOPS

0X43000000 + CAUSE_EXCHANGEROUTINGERROR

CAUSE_CTICCMSIP484ADDRESSINCOMPLETE

0X44000000 + CAUSE_INVALIDNUMBERFORMAT

CAUSE_CTICCMSIP485AMBIGUOUS

0X45000000 + CAUSE_UNALLOCATEDNUMBER

CAUSE_CTICCMSIP486BUSYHERE

0X46000000 + CAUSE_USERBUSY

CAUSE_CTICCMSIP487REQUESTTERMINATED

0X47000000 + CAUSE_NORMALUNSPECIFIED

CAUSE_CTICCMSIP488NOTACCEPTABLEHERE

0X48000000 + CAUSE_NORMALUNSPECIFIED

CAUSE_CTICCMSIP491REQUESTPENDING

0X4B000000 + CAUSE_USERBUSY

CAUSE_CTICCMSIP493UNDECIPHERABLE

0X4D000000 + CAUSE_USERBUSY

CAUSE_CTICCMSIP500SERVERINTERNALERROR

0X54000000 + CAUSE_TEMPORARYFAILURE

CAUSE_CTICCMSIP501NOTIMPLEMENTED

0X55000000 + CAUSE_SERVOROPTNAVAILORIMPL

CAUSE_CTICCMSIP502BADGATEWAY

0X56000000 + CAUSE_NETOUTOFORDER

CAUSE_CTICCMSIP503SERVICEUNAVAILABLE

0X57000000 + CAUSE_TEMPORARYFAILURE

CAUSE_CTICCMSIP504SERVERTIMEOUT

0X58000000 + CAUSE_RECOVERYONTIMEREXPIRY

CAUSE_CTICCMSIP505SIPVERSIONNOTSUPPORTED

0X59000000 + CAUSE_INTERWORKINGUNSPECIFIED

CAUSE_CTICCMSIP513MESSAGETOOLARGE

0X5A000000 + CAUSE_INTERWORKINGUNSPECIFIED

CAUSE_CTICCMSIP600BUSYEVERYWHERE

0XA1000000 + CAUSE_USERBUSY

CAUSE_CTICCMSIP603DECLINE

0XA2000000 + CAUSE_CALLREJECTED

CAUSE_CTICCMSIP604DOESNOTEXISTANYWHERE

0XA3000000 + CAUSE_UNALLOCATEDNUMBER

CAUSE_CTICCMSIP606NOTACCEPTABLE

0XA4000000 + CAUSE_NORMALUNSPECIFIED

CAUSE_CTICCMSIP200CALLCOMPLETEDELSEWHERE

0xA5000000 + NORMALUNSPECIFIED

CAUSE_CTICCMSIP503SERVICENOTAVAILABLE

0xA7000000 + SERVNOTAVAILUNSPECIFIED

## Additional Troubleshooting Information

### Viewing JTAPI
                           	 Debug Output

To view
                              		JTAPI debug output,  use the JTPREFS application to change the trace settings.
                              		The JTPREFS application allows you to enable or disable various kinds of
                              		tracing.

JTPREFS is
                              		installed in the %SystemRoot%\java\lib directory along with the JTAPI
                              		classes. Cisco JTAPI Preferences is installed by default in Program
                                 		  Files\JTAPITools .

To open
                              		the Cisco JTAPI Preferences utility,  choose Start >
                                 		  Programs > Cisco JTAPI > JTAPI Preferences.

The
                              		following trace levels are defined:

WARNING -
                                    			 warning events

INFORMATIONAL -
                                    			 status events

DEBUG -
                                    			 debugging events

If DEBUG
                              		is enabled,  JTPREFS allows you to enable or disable various debugging levels.

The
                              		following debugging levels are defined:

TAPI_DEBUGGING -
                                    			 to trace JTAPI methods and events

TAPI_IMPLDEBUGGING - internal JTAPI implementation trace

CTI_DEBUGGING -
                                    			 to trace Cisco Unified
                                       				Communications Manager events that are sent to the JTAPI
                                    			 implementation

CTIIMPL_DEBUGGING - internal CTICLIENT implementation trace

PROTOCOL_DEBUGGING - full CTI protocol decoding

MISC_DEBUGGING -
                                    			 miscellaneous low-level debug trace

Traces can
                              		be directed to a specific path and folder rather than to the application
                              		directory by default. The same trace folder could be used for successive or
                              		more than one simultaneous launch of JTAPI. Different launches of JTAPI would
                              		also send the traces to different folders. This allows simultaneous JTAPI
                              		instances to maintain independent trace destinations

Traces can be directed to a specific path and folder rather than to the application directory by default. The same trace folder
                                          could be used for successive or more than one simultaneous launch of JTAPI. Different launches of JTAPI would also send traces
                                          to different folders. This allows simultaneous JTAPI instances to maintain independent trace destinations. The application
                                          directory in this case is not that of the JTAPI client itself, but of the application that is integrating/using the JTAPI
                                          client.

### Log Files for JTAPI Client Installer

In order
                              		to detect the error which might occur during the installation and
                              		uninstallation process,  two log files will be generated. These files will be in
                              		the same location from which the installer is executed.

ismpInstall.log
                                    			 – to track events during installation.

ismpUninstall.log – to track events during uninstallation.

The error
                              		messages will contain the information about the wizard beans that were executed
                              		as a part of the install procedure and if there were any exceptions.

### Troubleshooting
                           	 Tips for ISMP Installer

SN

Problem Description

Cause

Solution

1

ISMP Uninstall does not remove the target directories
                                          					 installed.

Directory from which uninstaller is invoked.

The uninstaller needs to be invoked from at least one level
                                          					 above the install directory.

2

Proper language details are not displayed during installation

Locale Files not proper.

Please report this problem immediately to the support
                                          					 personnel to suggest the change or error in message.

3

Uninstaller/Installer throws error.

The JVM has been either removed or replaced with an
                                          					 incompatible version

The installer comes with a built in JVM which also gets
                                          					 installed if the target machine does not have a JVM. In case you face this
                                          					 error - manual removal of the files needs to be done.

4

Installer goes through fine,  but the files have not been
                                          					 copied.

Permissions

Ensure that proper write permissions are there for the
                                          					 destination folder. This problem can occur on UNIX platforms.

5

Installer/Uninstaller throws exception or crashes during the
                                          					 installation process.

version name problem / folder name problem.

Refer to the log files generated to get an idea of which step
                                          					 caused the error.

6

Upgrade does not show "upgrade" message during installation of an upgrade
                                          					 version.

.jtapiver.ini missing.

This file is where the current jtapi install details are
                                          					 located. If this is accidently removed then,  upgrade/reinstall will have
                                          					 display issues. In the case of an upgrade/reinstall or downgrade failure,  the
                                          					 user will have to manually remove the files from the .jtapi/bin and .jtapi/lib
                                          					 folders and then try the installer in order to ensure proper installation
                                          					 during the next time.

### Unable to Create
                           	 Provider Directory Login Timeout

This
                              		error occurs when there is no authentication response from CTI for the
                              		ProviderOpenRequest. It could fail because of:

LDAP
                                    			 connectivity problems

Database delays

The CTIManager
                                    			 being busy for some other reason and therefore unable to honor the request

The
                              		solution is that the application must try again. If the ProviderOpenRequest
                              		fails on repeated attempts,  modify the ProviderOpenRequest.

| Error code | Description |
|---|---|
| ASSOCIATED_LINE_NOT_OPEN | This error indicates that the request is issued on
                                          						a line, which is not open |
| CALL_ALREADY_EXISTS | This error indicates that another call already
                                          						exists on the line |
| CALL_DROPPED | The call dropped after the feature request (hold,
                                          						unhold, transfer, or conference) but before the request was completed. |
| CALLHANDLE_NOTINCOMINGCALL | This error indicates that an attempt is made to
                                          						answer a call that either does not exist or is not in the correct state |
| CALLHANDLE_UNKNOWN_TO_LINECONTROL | This error indicates that attempt to redirect call
                                          						that was unknown to line control |
| CANNOT_OPEN_DEVICE | This error indicates that device open failed
                                          						because the associated device is unregistering |
| CANNOT_TERMINATE_MEDIA_ON_PHONE | This error indicates that media cannot be
                                          						terminated by an application when the device is a physical phone (the phone
                                          						always terminates the media) |
| CFWDALL_ALREADY_SET | This error indicates that attempt to set CFWALL
                                          						while it is already set |
| CFWDALL_DESTN_INVALID | This error indicates that attempt to CFWALL to an
                                          						invalid destination |
| CLUSTER_LINK_FAILURE | This error indicates that link to one of the cisco
                                          						unified communications managers failed in the cluster (network error) |
| COMMAND_NOT_IMPLEMENTED_ON_DEVICE | This error indicates that device does not support
                                          						the command. |
| CONFERENCE_ALREADY_PRESENT | This error indicates that attempt to conference a
                                          						party that is already in conference |
| CONFERENCE_FAILED | This error indicates that conference completion was
                                          						not successful. |
| CONFERENCE_FULL | This error indicates that all conference bridges
                                          						are busy. |
| CONFERENCE_INACTIVE | This error indicates that attempt to complete
                                          						conference while consult conference is not active |
| CONFERENCE_INVALID_PARTICIPANT | This error indicates that an attempt to conference
                                          						to self or an invalid participant |
| CTIERR_ACCESS_TO_DEVICE_DENIED | This error indicates that the access to device is
                                          						denied. |
| CTIERR_APP_SOFTKEYS_ALREADY_CONTROLLED | This error indicates that the application softkeys
                                          						are already controlled by another application |
| CTIERR_APPLICATION_DATA_SIZE_EXCEEDED | This error indicates that application data size has
                                          						exceeded limit |
| CTIERR_BIB_NOT_CONFIGURED | This error indicates built in bridge is not
                                          						configured |
| CTIERR_BIB_RESOURCE_NOT_AVAILABLE | This error indicates that built in bridge resource
                                          						not available |
| CTIERR_CALL_MANAGER_NOT_AVAILABLE | This error indicates that Communications Manager is
                                          						not available currently |
| CTIERR_CALL_NOT_EXISTED | This error indicates that call does not exist |
| CTIERR_CALL_PARK_NO_DN | This error indicates no call park DN |
| CTIERR_CALL_REQUEST_ALREADY_OUTSTANDING | This error indicates call request already
                                          						outstanding |
| CTIERR_CALL_UNPARK_FAILED | This error indicates that call unpark did not
                                          						succeed |
| CTIERR_CAPABILITIES_DO_NOT_MATCH | This error indicates that capabilities do not match |
| CTIERR_CLOSE_DELAY_NOT_SUPPORTED_WITH_REG_TYPE | This error indicates that the close delay is not
                                          						supported with this registration type |
| CTIERR_CONFERENCE_ALREADY_EXISTED | This error indicates that conference already exists |
| CTIERR_CONFERENCE_NOT_EXISTED | This error indicates that conference does not exist |
| CTIERR_CONNECTION_ON_INVALID_PORT | This error indicates application is trying to
                                          						connect to invalid port |
| CTIERR_CONSULT_CALL_FAILURE | This error indicates consult call failure |
| CTIERR_CONSULTCALL_ALREADY_OUTSTANDING | This error indicates that consult call already
                                          						outstanding |
| CTIERR_CREATE_PERSISTENT_CALL_FAILED | This error indicates that there is an issue with creating a
                                          						persistent call. |
| CTIERR_CRYPTO_CAPABILITY_MISMATCH | This error indicates that device registration
                                          						failed as device crypto algorithms does not match with current device
                                          						registration |
| CTIERR_CTIHANDLER_PROCESS_CREATION_FAILED | This error indicates that CTIHandler process
                                          						creation failed |
| CTIERR_DB_INITIALIZATION_ERROR | This error indicates DB initialization error |
| CTIERR_DEVICE_ALREADY_OPENED | This error indicates that device is already opened |
| CTIERR_DEVICE_ALREADY_REGISTERED_NONEXTEND | Device registration failed as device is already
                                          						registered in Non-Extend mode. |
| CTIERR_DEVICE_NOT_OPENED_YET | This error indicates that device is not yet opened |
| CTIERR_DEVICE_OWNER_ALIVE_TIMER_STARTED | This error indicates that there is a device
                                          						registration failure |
| CTIERR_DEVICE_REGISTRATION_FAILED_ NOT_SUPPORTED_MEDIATYPE | This error indicates an invalid media type, CTIPort
                                          						need to be registered with Dynamic media port registation if it has an intercom
                                          						line |
| CTIERR_DEVICE_RESTRICTED | This error indicates that the device is restricted |
| CTIERR_DEVICE_SHUTTING_DOWN | This error indicates that device is shutting down |
| CTIERR_DIRECTORY_LOGIN_TIMEOUT | This error indicates that there is a directory
                                          						login time out |
| CTIERR_DISCONNECT_PERSISTENT_CALL_FAILED_ CALL_ACTIVE | This error indicates that the request to disconnect the
                                          						persistent call failed because there is an active customer call. Only when
                                          						there are no active calls present, can the persistent call be disconnected. |
| CTIERR_DUPLICATE_CALL_REFERENCE | This error indicates duplicate call reference |
| CTIERR_DUPLICATE_REMOTE_DESTINATION_NUMBER | Duplicated Remote Destination Number with an
                                          						existing Remote Destination Number. |
| CTIERR_DYNREG_IPADDRMODE_MISMATCH | This indicates registration failure when Cisco
                                          						Media/Route Tterminal is already registered with different Addressing mode |
| CTIERR_ENDUSER_NOT_ASSOCIATED_WITH_DEVICE | Enduser is not associated with the device. |
| CTIERR_FAC_CMC_REASON_CMC_INVALID | Client Matter Code (CMC) entered is invalid |
| CTIERR_FAC_CMC_REASON_CMC_NEEDED | CMC is required to offer the call |
| CTIERR_FAC_CMC_REASON_FAC_CMC_NEEDED | Forced Authorization Code (FAC) and CMC are
                                          						required to offer call |
| CTIERR_FAC_CMC_REASON_FAC_INVALID | FAC entered is invalid |
| CTIERR_FAC_CMC_REASON_FAC_NEEDED | FAC is required to offer the call |
| CTIERR_FEATURE_ALREADY_REGISTERED | This error indicates feature already registered |
| CTIERR_FEATURE_DATA_REJECT | This error indicates feature data reject |
| CTIERR_FEATURE_SELECT_FAILED | This error indicates that feature select failed |
| CTIERR_ILLEGAL_DEVICE_TYPE | This error indicates that the device type is
                                          						illegal |
| CTIERR_INCOMPATIBLE_AUTOINSTALL_PROTOCOL_ VERSION | This error indicates that auto install protocol
                                          						version is incompatible |
| CTIERR_INCORRECT_MEDIA_CAPABILITY | This error indicates that device registration
                                          						failed due to incorrect media capability |
| CTIERR_INFORMATION_NOT_AVAILABLE | This error indicates that information is not
                                          						available |
| CTIERR_INTERCOM_SPEEDDIAL_ALREADY_CONFIGURED | This error indicates that intercom target value is
                                          						already configured, application is trying to make call with Intercom target DN |
| CTIERR_INTERCOM_SPEEDDIAL_ALREADY_SET | This error indicates that intercom request failed
                                          						as intercom target value is already set, application is trying to set again |
| CTIERR_INTERCOM_SPEEDDIAL_DESTN_INVALID | This error indicates that intercomm request failed
                                          						as intercom target value in not in the intercom group |
| CTIERR_INTERCOM_TALKBACK_ALREADY_PENDING | This error indicates that intercom talk back
                                          						request is already pending |
| CTIERR_INTERCOM_TALKBACK_FAILURE | This error indicates that talkback request failed
                                          						for some reason |
| CTIERR_INTERNAL_FAILURE | This error indicates there is a CTI internal
                                          						failure |
| CTIERR_INVALID_CALLID | This error indicates the call ID is invalid |
| CTIERR_INVALID_DEVICE_NAME | This error indicates that the device name is not
                                          						valid |
| CTIERR_INVALID_DTMFDIGITS | Play DTMF request failed because it is an invalid
                                          						DTMF digit |
| CTIERR_INVALID_FILTER_SIZE | This error indicates that filter size is invalid |
| CTIERR_INVALID_MEDIA_DEVICE | This error indicates that the media device is not
                                          						valid |
| CTIERR_INVALID_MEDIA_PARAMETER | This error indicates media parameter is invalid |
| CTIERR_INVALID_MEDIA_PROCESS | This error indicates that there is an invalid
                                          						media process |
| CTIERR_INVALID_MEDIA_RESOURCE_ID | This error indicates media resource ID is not
                                          						valid |
| CTIERR_INVALID_MESSAGE_HEADER_INFO | This error indicates that the header info is not
                                          						valid |
| CTIERR_INVALID_MESSAGE_LENGTH | This error indicates that message length is
                                          						invalid |
| CTIERR_INVALID_MONITOR_DESTN | This error indicates monitoring request failed due
                                          						to invalid monitoring destination |
| CTIERR_INVALID_MONITOR_DN_TYPE | This error indicates an invalid monitor DN type |
| CTIERR_INVALID_MONITORMODE | This error indicates monitor request failed due to
                                          						an invalid monitor mode |
| CTIERR_INVALID_PARAMETER | This error indicates that the parameter is not
                                          						valid |
| CTIERR_INVALID_PARK_DN | This error indicates that the DN is an invalid
                                          						park DN |
| CTIERR_INVALID_PARK_REGISTRATION_HANDLE | This error indicates that the handle is an invalid
                                          						park registration handle |
| CTIERR_PERSISTENT_CALL_EXISTS | This error indicates that a persistent call already exists. |
| CTIERR_INVALID_REMOTE_DESTINATION_NAME | This error indicates an Invalid Remote Destination
                                          						Name. |
| CTIERR_INVALID_REMOTE_DESTINATION_NUMBER | This error indicates an Invalid Remote Destination
                                          						Number. |
| CTIERR_INVALID_RESOURCE_TYPE | This error indicates an invalid resource type |
| CTIERR_IPADDRMODE_MISMATCH | This indicates the registration failure due to IP
                                          						Addressing Mode mismatch. |
| CTIERR_LINE_OUT_OF_SERVICE | This error indicates that line is out of service. |
| CTIERR_LINE_RESTRICTED | This er ror indicates that the line is restricted |
| CTIERR_MAXCALL_LIMIT_REACHED | This error indicates that maximum call limit has
                                          						reached |
| CTIERR_MEDIA_ALREADY_TERMINATED_DYNAMIC | This error indicates that device registration
                                          						failed as device is registered with Dynamic media termination |
| CTIERR_MEDIA_ALREADY_TERMINATED_EXTEND | Device registration failed as device is already
                                          						registered in Extend mode. |
| CTIERR_MEDIA_ALREADY_TERMINATED_NONE | This error indicates that device registration
                                          						failed as device is already registered with media termination none |
| CTIERR_MEDIA_ALREADY_TERMINATED_STATIC | This error indicates that device registration
                                          						failed as device is registered with Static media termination |
| CTIERR_MEDIA_CAPABILITY_MISMATCH | This error indicates that device registration
                                          						failed as media capability of device does not match with current device
                                          						registration |
| CTIERR_MEDIA_RESOURCE_NAME_SIZE_EXCEEDED | This error indicates that media resource name size
                                          						has exceeded limit |
| CTIERR_MEDIAREGISTRATIONTYPE_DO_NOT_MATCH | This error indicates that media registration types
                                          						do not match |
| CTIERR_MESSAGE_TOO_BIG | This error indicates that message is too big |
| CTIERR_MORE_ACTIVE_CALLS_THAN_RESERVED | This error indicates that there are more active
                                          						calls than reserved |
| CTIERR_NO_EXISTING_CALLS | This error indicates there are no existing calls |
| CTIERR_NO_EXISTING_CONFERENCE | This error indicates that there is no existing
                                          						conference |
| CTIERR_NO_RECORDING_SESSION | This error indicates recording request failed as
                                          						there is no recording session |
| CTIERR_NO_RESPONSE_FROM_MP | This error indicates no response from media
                                          						resource |
| CTIERR_NOT_PRESERVED_CALL | This error indicates that the call is not
                                          						preserved |
| CTIERR_OPERATION_FAILED_QUIETCLEAR | This error indicates that feature unavailable for
                                          						this call due to temporary failure |
| CTIERR_OPERATION_NOT_ALLOWED | This error indicates that this operation is not
                                          						allowed |
| CTIERR_OPERATION_NOT_ALLOWED_ON_ PERSISTENT_CALL | This indicates that the specified operation is not allowed
                                          						on a persistent call. |
| CTIERR_OUT_OF_BANDWIDTH | This error indicates out of bandwidth error |
| CTIERR_OWNER_NOT_ALIVE | This error indicates a failure during registering
                                          						the device |
| CTIERR_PENDING_ACCEPT_OR_ANSWER_REQUEST | This error indicates that there is a pending
                                          						accept or answer request |
| CTIERR_PENDING_START_MONITORING_REQUEST | This error indicates there is a pending start
                                          						monitoring request |
| CTIERR_PENDING_START_RECORDING_REQUEST | This error indicates there is a pending start
                                          						recording request |
| CTIERR_PENDING_STOP_RECORDING_REQUEST | This error indicates there is a pending stop
                                          						recording request |
| CTIERR_PERSISTENT_CALL_BEING_SETUP | This error indicates that the request failed because a
                                          						persistent call is already being set up. |
| CTIERR_PRIMARY_CALL_INVALID | This error indicates that primary call in
                                          						monitoring request in invalid or gone idle |
| CTIERR_PRIMARY_CALL_STATE_INVALID | This error indicates that primary call in
                                          						monitoring request is in invalid state |
| CTIERR_RECORDING_ALREADY_INPROGRESS | This error indicates recording request failed that
                                          						recording is already in progress |
| CTIERR_RECORDING_CONFIG_NOT_MATCHING | This error indicates recording configuration does
                                          						not match |
| CTIERR_RECORDING_INVOCATION_TYPE_NOT_MATCHING | Stop recording failed because the recording
                                          						invocation type did not match. |
| CTIERR_RECORDING_SESSION_INACTIVE | This error indicates recording request failed
                                          						because recording session is inactive |
| CTIERR_REDIRECT_UNAUTHORIZED_COMMAND_USAGE | This error indicates a redirect unauthorized
                                          						command usage |
| CTIERR_REGISTER_FEATURE_ACTIVATION_FAILED | This error indicates that register feature
                                          						activation failed |
| CTIERR_REGISTER_FEATURE_APP_ALREADY_REGISTERED | Register feature application was already
                                          						registered |
| CTIERR_REGISTER_FEATURE_PROVIDER_NOT_REGISTERED | Register feature provider was not registered. |
| CTIERR_REMOTE_DEVICE_REQUEST_FAILED_ ACTIVE_RD_NOT_SET | The active remote destination is not set. |
| CTIERR_REMOTEDESTINATION_LIMIT_EXCEEDED | The number of Remote Destinations has exceeded the
                                          						max number limit. |
| CTIERR_RESOURCE_NOT_AVAILABLE | This error indicates that resource is not
                                          						available to fulfill the request |
| CTIERR_START_MONITORING_FAILED | This error indicates that start monitoring request
                                          						failed |
| CTIERR_START_RECORDING_FAILED | This error indicates that start recording request
                                          						failed |
| CTIERR_STATION_SHUT_DOWN | This error indicates that there is a station
                                          						shutdown |
| CTIERR_SYSTEM_ERROR | This error indicates CTI system error |
| CTIERR_UDP_PASS_THROUGH_NOT_SUPPORTED | This error indicates UDP data passthrough not
                                          						supported |
| CTIERR_UNKNOWN_EXCEPTION | This error indicates an unknown exception occured |
| CTIERR_UNSUPPORTED_CALL_PARK_TYPE | This error indicates that call park type is not
                                          						supported |
| CTIERR_UNSUPPORTED_CFWD_TYPE | This error indicates that the call forward type is
                                          						unsupported |
| CTIERR_USER_NOT_AUTH_FOR_SECURITY | This error indicates user is not authorized for
                                          						secure connection |
| DARES_INVALID_REQ_TYPE | This error indicates that there is an internal
                                          						call processing error: DaRes invalid request type |
| DATA_SIZE_LIMIT_EXCEEDED | This error indicates that XML data object size is
                                          						bigger than allowed. |
| DB_ERROR | This error indicates that the device query
                                          						contained an illegal device type |
| DB_ILLEGAL_DEVICE_TYPE | This error indicates illegal device type in DB |
| DB_NO_MORE_DEVICES | This error is no longer used. |
| DESTINATION_BUSY | This error indicates that destination is busy |
| DESTINATION_UNKNOWN | This error indicates that destination is not found |
| DEVICE_ALREADY_REGISTERED | This error indicates that device registration
                                          						attempt failed, because the device is already registered |
| DEVICE_NOT_OPEN | This error indicates that an attempt to open a
                                          						line failed, as the device is not opened or the device is not registered. |
| DEVICE_OUT_OF_SERVICE | This error indicates that device is out of
                                          						service. |
| DIGIT_GENERATION_ALREADY_IN_PROGRESS | This error indicates that digit generation is
                                          						already in progress. |
| DIGIT_GENERATION_CALLSTATE_CHANGED | This error indicates that call state is invalid to
                                          						continue. |
| DIGIT_GENERATION_WRONG_CALL_HANDLE | This error indicates that call handle is invalid
                                          						and call may be gone. |
| DIGIT_GENERATION_WRONG_CALL_STATE | This error indicates that call state is not valid
                                          						to generate digits. |
| DIRECTORY_LOGIN_FAILED | This error indicates that directory login failed:
                                          						directory not initialized |
| DIRECTORY_LOGIN_NOT_ALLOWED | This error indicates that directory login failed |
| DIRECTORY_TEMPORARY_UNAVAILABLE | This error indicates that directory is temporarily
                                          						unavailable. |
| EXISTING_FIRSTPARTY | This error indicates that there is already a
                                          						device controlling media. |
| HOLDFAILED | This error indicates that the hold was rejected by
                                          						line control or call control layers |
| ILLEGAL_CALLINGPARTY | This error indicates that an attempt was made to
                                          						originate call using a calling party that is not on the device |
| ILLEGAL_CALLSTATE | This error indicates line is not in a legal state
                                          						to invoke the request |
| ILLEGAL_HANDLE | This error indicates the handle is not valid |
| ILLEGAL_MESSAGE_FORMAT | This error indicates that there is a QBE protocol
                                          						error |
| INCOMPATIBLE_PROTOCOL_VERSION | This error indicates that JTAPI and CTI versions
                                          						are not compatible : CTI Error Protocol version not supported |
| INVALID_LINE_HANDLE | This error indicates that attempt to perform a
                                          						line operation on an invalid line handle. |
| INVALID_RING_OPTION | This error indicates that the ring option is
                                          						invalid |
| LINE_GREATER_THAN_MAX_LINE | This error indicates that line is greater than the
                                          						maximum available lines on this device |
| LINE_INFO_DOES_NOT_EXIST | This error indicates that line information does
                                          						not exist in the database. |
| LINE_NOT_PRIMARY | This error indicates that internal error returned
                                          						from call control. |
| LINECONTROL_FAILURE | This error indicates line control refuses to allow
                                          						a new call to be initiated because of its current state. |
| MAX_NUMBER_OF_CTI_CONNECTIONS_REACHED | The maximum number of CTI connections was reached. |
| MSGWAITING_DESTN_INVALID | This error indicates that attempt to set message
                                          						waiting lamp for an invalid DN; Message Waiting Destination not found. |
| NO_ACTIVE_DEVICE_FOR_THIRDPARTY | This error indicates there is no active device for
                                          						thirdparty |
| NO_CONFERENCE_BRIDGE | This error indicates that no conference bridge
                                          						available |
| NOT_INITIALIZED | This error indicates that attempt is made to open
                                          						a provider before CTI initialization completes |
| PROTOCOL_TIMEOUT | Internal error returned from call control |
| PROVIDER_ALREADY_OPEN | This error indicates that an attempt is made to
                                          						reopen provider |
| PROVIDER_CLOSED | This error indicates an attempt to close provider
                                          						while it is already closed |
| PROVIDER_NOT_OPEN | This error indicates that device list incomplete
                                          						or device list query timeout or query aborted |
| REDIRECT_CALL_CALL_TABLE_FULL | This error indicates that internal error is
                                          						returned from call control |
| REDIRECT_CALL_DESTINATION_BUSY | This error indicates that the redirect destination
                                          						is busy |
| REDIRECT_CALL_DESTINATION_OUT_OF_ORDER | This error indicates that redirect destination is
                                          						out of order |
| REDIRECT_CALL_DIGIT_ANALYSIS_TIMEOUT | This error indicates a digit analyss time out,
                                          						this is an internal error returned from call control |
| REDIRECT_CALL_DOES_NOT_EXIST | This error indicates that an attempt is made to
                                          						redirect a call that does not exist or is not longer active |
| REDIRECT_CALL_INCOMPATIBLE_STATE | This error indicates that internal error is
                                          						returned from call control |
| REDIRECT_CALL_MEDIA_CONNECTION_FAILED | This error indicates media connection failure,
                                          						this is an internal error returned from call control |
| REDIRECT_CALL_NORMAL_CLEARING | This error indicates that redirect failed because
                                          						of normal call clearing |
| REDIRECT_CALL_ORIGINATOR_ABANDONED | This error indicates that far end hung up on the
                                          						call being redirected |
| REDIRECT_CALL_PARTY_TABLE_FULL | This error indicates that internal error is
                                          						returned from call control |
| REDIRECT_CALL_PENDING_REDIRECT_TRANSACTION | This error indicates that internal error is
                                          						returned from call control |
| REDIRECT_CALL_PROTOCOL_ERROR | This error indicates a protocol error, this is an
                                          						internal error returned from call control |
| REDIRECT_CALL_UNKNOWN_DESTINATION | This error indicates that an attempt is made to
                                          						redirect to an unknown destination |
| REDIRECT_CALL_UNKNOWN_ERROR | This error indicates that internal error is
                                          						returned from call control |
| REDIRECT_CALL_UNKNOWN_PARTY | This error indicates an unknown party is detected,
                                          						this is an internal error returned from call control |
| REDIRECT_CALL_UNRECOGNIZED_MANAGER | This error indicates that internal error is
                                          						returned from call control |
| REDIRECT_CALLINFO_ERR | This error indicates that internal error is
                                          						returned from call control |
| REDIRECT_ERR | This error indicates that internal error is
                                          						returned from call control |
| RETRIEVEFAILED | This error indicates that retrieval of call was
                                          						rejected by line control or call control |
| RETRIEVEFAILED_ACTIVE_CALL_ON_LINE | This error indicates that error occurred in
                                          						retrieving held call; because there is already another active call on the line |
| SSAPI_NOT_REGISTERED | This error indicates that the redirect command was
                                          						issued when the internal supporting interface was not initialized; either CTI
                                          						has not yet finished its initialization or an internal error occurred |
| TIMEOUT | This error indicates that the request has timed
                                          						out. |
| TRANSFER_INACTIVE | This error indicates that attempt to complete
                                          						transfer, while consult tranfer is not there |
| TRANSFERFAILED | This error indicates that the transfer failed
                                          						probably because one of the call legs was hung up or disconnected from the far
                                          						end |
| TRANSFERFAILED_CALLCONTROL_TIMEOUT | This error indicates that expected response from
                                          						call control not received during a transfer |
| TRANSFERFAILED_DESTINATION_BUSY | This error indicates that an attempt is made to
                                          						transfer call to a busy destination |
| TRANSFERFAILED_DESTINATION_UNALLOCATED | This error indicates an attempt is made to to
                                          						transfer call to a directory number that is not registered |
| TRANSFERFAILED_OUTSTANDING_TRANSFER | This error indicates that existing transfer is
                                          						still in progress |
| UNDEFINED_LINE | This error indicates that the line that was
                                          						specified, is not found on the device |
| UNKNOWN_GLOBAL_CALL_HANDLE | This error indicates that the global call handle
                                          						is unknown |
| UNRECOGNIZABLE_PDU | This error indicates that there is a QBE protocol
                                          						error |
| UNSPECIFIED | This error indicates that an unspecified error has
                                          						occurred. |

| Event name | Event number |
|---|---|
| CiscoProvFeatureUnRegisteredEv | 0x40000008 |
| CiscoRestrictedEv | 0x40000009 |
| CiscoAddrRestrictedEv | 0x40000010 |
| CiscoTermRestrictedEv | 0x40000011 |
| CiscoAddrActivatedEv | 0x40000012 |
| CiscoTermActivatedEv | 0x40000013 |
| CiscoAddrActivatedOnTerminalEv | 0x40000014 |
| CiscoAddrRestrictedOnTerminalEv | 0x40000015 |
| CiscoProviderCapabilityChangedEv | 0x40000016 |
| CiscoProvTerminalCapabilityChangedEv | 0x40000017 |
| CiscoProvTerminalRegisteredEv | 0x40000018 |
| CiscoProvTerminalUnRegisteredEv | 0x40000019 |
| CiscoProvTerminalRemoteDestinationChangedEv | 0x40000020 |
| CiscoProvTerminalIPAddressChangedEv | 0x40000021 |
| CiscoProvTerminalMultiMediaCapabilityChangedEv | 0x40000022 |

| Event name | Event number |
|---|---|
| CiscoTermCreatedEv | 0x40001001 |
| CiscoTermDataEv | 0x40001002 |
| CiscoTermInServiceEv | 0x40001003 |
| CiscoTermOutOfServiceEv | 0x40001004 |
| CiscoTermRemovedEv | 0x40001005 |
| CiscoTermDeviceActiveStatusEv | 0x40001006 |
| CiscoTermDeviceAlertingStatusEv | 0x40001007 |
| CiscoTermDeviceHoldStatusEv | 0x40001008 |
| CiscoTermDeviceIdleStatusEv | 0x40001009 |
| CiscoTermButtonPressedEv | 0x40001010 |
| CiscoTermRegistraionFailedEv | 0x40001011 |
| CiscoTermDNDStatusChangedEv | 0x40001014 |
| CiscoTermDeviceStateWhisperEv | 0x40001015 |
| CiscoTermDNDOptionChangedEv | 0x40001016 |
| CiscoMultiMediaStreamsInfoEv | 0x40001017 |

| Event name | Event number |
|---|---|
| CiscoAddrCreatedEv | 0x40002001 |
| CiscoAddrInServiceEv | 0x40002002 |
| CiscoAddrOutOfServiceEv | 0x40002003 |
| CiscoAddrRemovedEv | 0x40002004 |
| CiscoOutOfServiceEv | 0x40002005 |
| CiscoAddrAddedToTerminalEv | 0x40002006 |
| CiscoAddrRemovedFromTerminalEv | 0x40002007 |
| CiscoAddrAutoAcceptStatusChangedEv | 0x40002008 |
| CiscoAddrIntercomInfoChangedEv | 0x40002009 |
| CiscoAddrIntercomInfoRestorationFailedEv | 0x40002010 |
| CiscoAddrRecordingConfigChangedEv | 0x40002011 |
| CiscoAddrParkStatusEv | 0x40002012 |
| CiscoAddrVoiceMailPilotChangedEv | 0x40002013 |
| CiscoAddrPickupGroupChangedEv | 0x40002014 |
| CiscoAddrMonitoringTerminatedEv | 0x4000200A |

| Event name | Event number |
|---|---|
| CiscoProvCallParkEv | 0x40003001 |
| CiscoConferenceEndEv | 0x40003002 |
| CiscoConferenceStartEv | 0x40003003 |
| CiscoConsultCallActiveEv | 0x40003004 |
| CiscoTransferEndEv | 0x40003005 |
| CiscoTransferStartEv | 0x40003006 |
| CiscoToneChangedEv | 0x40003007 |
| CiscoCallChangedEv | 0x40003008 |
| CiscoConferenceChainAddedEv | 0x40003009 |
| CiscoConferenceChainRemovedEv | 0x40003010 |
| CiscoCallSecurityStatusChangedEv | 0x40003011 |
| CiscoCallFeatureCancelledEv | 0x40003012 |
| CiscoProvPickupCallAlertEv | 0x40003013 |
| CiscoProvPickupNotificationRegistrationClosedEv | 0x40003014 |
| CiscoCallInfoChangedEv | 0x40003015 |
| CiscoProvAuthenticationInfoEv | 0x40003016 |

| Event name | Event number |
|---|---|
| CiscoRTPInputStartedEv | 0x40004001 |
| CiscoRTPInputStoppedEv | 0x40004002 |
| CiscoRTPOutputStartedEv | 0x40004003 |
| CiscoRTPOutputStoppedEv | 0x40004004 |
| CiscoMediaOpenLogicalChannelEv | 0x40004005 |
| CiscoRTPInputKeyEv | 0x40004006 |
| CiscoRTPOutputKeyEv | 0x40004007 |
| CiscoMediaOpenIPPortEv | 0x40004008 |

| Event name | Event number |
|---|---|
| CiscoTermConnPrivacyChangedEv | 0x40005001 |
| CiscoCallCtlTermConnHeldReversionEv | 0x40005002 |
| CiscoTermConnSelectChangedEv | 0x40005003 |
| CiscoTermConnRecordingStartEv | 0x40005004 |
| CiscoTermConnRecordingEndEv | 0x40005005 |
| CiscoTermConnRecordingFailedEv | 0x4000500E |
| CiscoTermConnMonitoringStartEv | 0x40005006 |
| CiscoTermConnMonitoringEndEv | 0x40005007 |
| CiscoTermConnRecordingTargetInfoEv | 0x40005008 |
| CiscoTermConnMonitorInitiatorInfoEv | 0x40005009 |
| CiscoTermConnMonitorTargetInfoEv | 0x4000500A |
| CiscoTermConnMonitorUpdatedEv | 0x4000500B |
| CiscoMediaStreamStartedEv | 0x4000500C |
| CiscoMediaStreamEndedEv | 0x4000500D |

| Event name | Event number |
|---|---|
| CiscoConnectionUniqueIDChangedEv | 0x40006001 |
| CiscoHuntConnCreatedEv | 0x40006002 |

| Reason code name | Reason code |
|---|---|
| REASON_TRANSFER | 2 |
| REASON_FORWARDNOANWSER | 3 |
| REASON_FORWARDBUSY | 4 |
| REASON_FORWARDALL | 5 |
| REASON_REDIRECT | 6 |
| REASON_BLINDTRANSFER | 7 |
| REASON_CONFERENCE | 9 |
| REASON_PARK | 10 |
| REASON_CALLPICKUP | 11 |
| REASON_NORMAL | 12 |
| REASON_PARKREMINDER | 15 |
| REASON_UNPARK | 16 |
| REASON_BARGE | 20 |
| REASON_IMMDIVERT | 21 |
| REASON_FAC_CMC | 22 |
| REASON_QSIG_PR | 23 |
| REASON_REFER | 24 |
| REASON_REPLACE | 25 |
| REASON_CCM_REDIRECTION | 26 |
| REASON_DPARK_CALLPARK | 27 |
| REASON_DPARK_REVERSION | 28 |
| REASON_DPARK_UNPARK | 29 |
| REASON_SILENTMONITORING | 31 |
| REASON_MOBILITY | 33 |
| REASON_MOBILITY_IVR | 34 |
| REASON_MOBILITY_CELLPICKUP | 35 |
| REASON_MOBILITY_HANDIN | 36 |
| REASON_MOBILITY_HANDOUT | 37 |
| REASON_MOBILITY_FOLLOWME | 38 |
| REASON_CLICK_TO_CONFERENCE | 39 |
| REASON_FORWARD_NO_RETRIEVE | 40 |
| REASON_EXTERNALCALLCONTROL | 42 |
| REASON_SAF_CCD_PSTN_FAILOVER | 43 |
| REASON_MEDIA_STREAMING | 44 |

| Cause code name | Cause code |
|---|---|
| CAUSE_NOERROR | 0X00 (0) |
| CAUSE_UNALLOCATEDNUMBER | 0X01 (1) |
| CAUSE_NOROUTETOTRANSITNET | 0X02 (2) |
| CAUSE_NOROUTETODDESTINATION | 0X03 (3) |
| CAUSE_CHANUNACCEPTABLE | 0X06 (6) |
| CAUSE_CALLBEINGDELIVERED | 0X07 (7) |
| CAUSE_CTIPREEMPTNOREUSE | 0X08 (8) |
| CAUSE_CTIPREEMPTFORREUSE | 0X09 (9) |
| CAUSE_NORMALCALLCLEARING | 0X10 (16) |
| CAUSE_USERBUSY | 0X11 (17) |
| CAUSE_NOUSERRESPONDING | 0X12 (18) |
| CAUSE_NOANSWERFROMUSER | 0X13 (19) |
| CAUSE_SUBSCRIBERABSENT | 0X14 (20) |
| CAUSE_CALLREJECTED | 0X15 (21) |
| CAUSE_NUMBERCHANGED | 0X16 (22) |
| CAUSE_EXCHANGEROUTINGERROR | 0X19 (25) |
| CAUSE_NONSELECTEDUSERCLEARING | 0X1A (26) |
| CAUSE_DDESTINATIONOUTOFORDER | 0X1B (27) |
| CAUSE_INVALIDNUMBERFORMAT | 0X1C (28) |
| CAUSE_FACILITYREJECTED | 0X1D (29) |
| CAUSE_RESPONSETOSTATUSENQUIRY | 0X1E (30) |
| CAUSE_NORMALUNSPECIFIED | 0X1F (31) |
| CAUSE_NOCIRCAVAIL | 0X22 (34) |
| CAUSE_NETOUTOFORDER | 0X26 (38) |
| CAUSE_TEMPORARYFAILURE | 0X29 (41) |
| CAUSE_SWITCHINGEQUIPMENTCONGESTION | 0X2A (42) |
| CAUSE_ACCESSINFORMATIONDISCARDED | 0X2B (43) |
| CAUSE_REQCIRCNAVIL | 0X2C (44) |
| CAUSE_CTIPRECEDENCECALLBLOCKED | 0X2E (46) |
| CAUSE_RESOURCESNAVAIL | 0X2F (47) |
| CAUSE_QUALOFSERVNAVAIL | 0X31 (49) |
| CAUSE_REQFACILITYNOTSUBSCRIBED | 0X32 (50) |
| CAUSE_SERVOPERATIONVIOLATED | 0X35 (53) |
| CAUSE_INCOMINGCALLBARRED | 0X36 (54) |
| CAUSE_BCNAUTHORIZED | 0X39 (57) |
| CAUSE_BCBPRESENTLYAVAIL | 0X3A (58) |
| CAUSE_SERVNOTAVAILUNSPECIFIED | 0X3F (63) |
| CAUSE_BEARERCAPNIMPL | 0X41 (65) |
| CAUSE_CHANTYPENIMPL | 0X42 (66) |
| CAUSE_REQFACILITYNIMPL | 0X45 (69) |
| CAUSE_ONLYRDIVEARERCAPAVAIL | 0X46 (70) |
| CAUSE_SERVOROPTNAVAILORIMPL | 0X4F (79) |
| CAUSE_INVALIDCALLREFVALUE | 0X51 (81 ) |
| CAUSE_IDENTIFIEDCHANDOESNOTEXIST | 0X52 (82) |
| CAUSE_SUSPCALLBUTNOTTHISONE | 0X53 (83) |
| CAUSE_CALLIDINUSE | 0X54 (84) |
| CAUSE_NOCALLSUSPENDED | 0X55 (85) |
| CAUSE_REQCALLIDHASBEENCLEARED | 0X56 (86) |
| CAUSE_INCOMPATABLEDDESTINATION | 0X58 (88) |
| CAUSE_DESTNUMMISSANDDCNOTSUB | 0X5A (90) |
| CAUSE_INVALIDTRANSITNETSEL | 0X5B (91) |
| CAUSE_INVALIDMESSAGEUNSPECIFIED | 0X5F (95) |
| CAUSE_MANDATORYIEMISSING | 0X60 (96) |
| CAUSE_MSGTYPENIMPL | 0X61 (97) |
| CAUSE_MSGTYPENCOMPATWCS | 0X62 (98) |
| CAUSE_IENIMPL | 0X63 (99) |
| CAUSE_INVALIDIECONTENTS | 0X64 (100) |
| CAUSE_MSGNCOMPATABLEWCS | 0X65 (101) |
| CAUSE_RECOVERYONTIMEREXPIRY | 0X66 (102) |
| CAUSE_PROTOCOLERRORUNSPECIFIED | 0X6F (111) |
| CAUSE_CTIPRECEDENCELEVELEXCEEDED | 0X7A (122) |
| CAUSE_CTIDEVICENOTPREEMPTABLE | 0X7B (123) |
| CAUSE_OUTOFBANDWIDTH | 0X7D (125) |
| CAUSE_INTERWORKINGUNSPECIFIED | 0X7F (127) |
| CAUSE_CTIPRECEDENCEOUTOFBANDWIDTH | 0X81 (129) |
| CAUSE_REDIRECTED | 0XC9 (200) |
| CAUSE_INTERNALCAUSE | 0X1F4 (500) |
| CAUSE_OUTBOUND_TRANSFER | 0X1F5 (501) |
| CAUSE_OUTBOUND_CONFERENCE | 0X1F6 (502) |
| CAUSE_INBOUND_TRANSFER | 0X1F7 (503) |
| CAUSE_INBOUND_CONFERENCE | 0X1F8 (504) |
| CAUSE_INBOUND_BLINDTRANSFER | 0X1F9 (505) |
| CAUSE_CTIMANAGER_FAILURE | 0x1FB (507) |
| CAUSE_CALLMANAGER_FAILURE | 0x1FC (508) |
| CAUSE_BARGE | 0x1FD(509) |
| CAUSE_FAC_CMC | 0x1FE (510) |
| CAUSE_QSIG_PR | 0x1FF (511) |
| CAUSE_DPARK | 0x200 (512) |
| CAUSE_DPARK_UNPARK | 0x201 (513) |
| CAUSE_DPARK_REMINDER | 0x202 (514) |
| CAUSE_QUIET_CLEAR | 0x203 (515) |
| CAUSE_CTICONFERENCEFULL | 0X40000 + CAUSE_NOERROR |
| CAUSE_CALLSPLIT | 0X60000 + CAUSE_NOERROR |
| CAUSE_CTIDROPCONFEREE | 0X70000 + CAUSE_NOERROR |
| CAUSE_CTICCMSIP400BADREQUEST | 0X1000000 + CAUSE_TEMPORARYFAILURE |
| CAUSE_CTICCMSIP401UNAUTHORIZED | 0X2000000 + CAUSE_CALLREJECTED |
| CAUSE_CTICCMSIP402PAYMENTREQUIRED | 0X3000000 + CAUSE_CALLREJECTED |
| CAUSE_CTICCMSIP403FORBIDDEN | 0X4000000 + CAUSE_CALLREJECTED |
| CAUSE_CTICCMSIP404NOTFOUND | 0X5000000 + CAUSE_UNALLOCATEDNUMBER |
| CAUSE_CTICCMSIP405METHODNOTALLOWED | 0X6000000 + CAUSE_SERVNOTAVAILUNSPECIFIED |
| CAUSE_CTICCMSIP406NOTACCEPTABLE | 0X7000000 + CAUSE_SERVOROPTNAVAILORIMPL |
| CAUSE_CTICCMSIP407PROXYAUTHENTICATIONREQUIRED | 0X8000000 + CAUSE_CALLREJECTED |
| CAUSE_CTICCMSIP408REQUESTTIMEOUT | 0X9000000 + CAUSE_RECOVERYONTIMEREXPIRY |
| CAUSE_CTICCMSIP410GONE | 0XB000000 + CAUSE_NUMBERCHANGED |
| CAUSE_CTICCMSIP411LENGTHREQUIRED | 0XC000000 + CAUSE_INTERWORKINGUNSPECIFIED |
| CAUSE_CTICCMSIP413REQUESTENTITYTOOLONG | 0XE000000 + CAUSE_INTERWORKINGUNSPECIFIED |
| CAUSE_CTICCMSIP414REQUESTURITOOLONG | 0XF000000 + CAUSE_INTERWORKINGUNSPECIFIED |
| CAUSE_CTICCMSIP415UNSUPPORTEDMEDIATYPE | 0X10000000 + CAUSE_SERVOROPTNAVAILORIMPL |
| CAUSE_CTICCMSIP416UNSUPPORTEDURISCHEME | 0X11000000 + CAUSE_INTERWORKINGUNSPECIFIED |
| CAUSE_CTICCMSIP420BADEXTENSION | 0X15000000 + CAUSE_INTERWORKINGUNSPECIFIED |
| CAUSE_CTICCMSIP421EXTENSTIONREQUIRED | 0X16000000 + CAUSE_INTERWORKINGUNSPECIFIED |
| CAUSE_CTICCMSIP423INTERVALTOOBRIEF | 0X18000000 + CAUSE_INTERWORKINGUNSPECIFIED |
| CAUSE_CTICCMSIP480TEMPORARILYUNAVAILABLE | 0X40000000 + CAUSE_NOUSERRESPONDING |
| CAUSE_CTICCMSIP481CALLLEGDOESNOTEXIST | 0X41000000 + CAUSE_TEMPORARYFAILURE |
| CAUSE_CTICCMSIP482LOOPDETECTED | 0X42000000 + CAUSE_EXCHANGEROUTINGERROR |
| CAUSE_CTICCMSIP483TOOMANYHOOPS | 0X43000000 + CAUSE_EXCHANGEROUTINGERROR |
| CAUSE_CTICCMSIP484ADDRESSINCOMPLETE | 0X44000000 + CAUSE_INVALIDNUMBERFORMAT |
| CAUSE_CTICCMSIP485AMBIGUOUS | 0X45000000 + CAUSE_UNALLOCATEDNUMBER |
| CAUSE_CTICCMSIP486BUSYHERE | 0X46000000 + CAUSE_USERBUSY |
| CAUSE_CTICCMSIP487REQUESTTERMINATED | 0X47000000 + CAUSE_NORMALUNSPECIFIED |
| CAUSE_CTICCMSIP488NOTACCEPTABLEHERE | 0X48000000 + CAUSE_NORMALUNSPECIFIED |
| CAUSE_CTICCMSIP491REQUESTPENDING | 0X4B000000 + CAUSE_USERBUSY |
| CAUSE_CTICCMSIP493UNDECIPHERABLE | 0X4D000000 + CAUSE_USERBUSY |
| CAUSE_CTICCMSIP500SERVERINTERNALERROR | 0X54000000 + CAUSE_TEMPORARYFAILURE |
| CAUSE_CTICCMSIP501NOTIMPLEMENTED | 0X55000000 + CAUSE_SERVOROPTNAVAILORIMPL |
| CAUSE_CTICCMSIP502BADGATEWAY | 0X56000000 + CAUSE_NETOUTOFORDER |
| CAUSE_CTICCMSIP503SERVICEUNAVAILABLE | 0X57000000 + CAUSE_TEMPORARYFAILURE |
| CAUSE_CTICCMSIP504SERVERTIMEOUT | 0X58000000 + CAUSE_RECOVERYONTIMEREXPIRY |
| CAUSE_CTICCMSIP505SIPVERSIONNOTSUPPORTED | 0X59000000 + CAUSE_INTERWORKINGUNSPECIFIED |
| CAUSE_CTICCMSIP513MESSAGETOOLARGE | 0X5A000000 + CAUSE_INTERWORKINGUNSPECIFIED |
| CAUSE_CTICCMSIP600BUSYEVERYWHERE | 0XA1000000 + CAUSE_USERBUSY |
| CAUSE_CTICCMSIP603DECLINE | 0XA2000000 + CAUSE_CALLREJECTED |
| CAUSE_CTICCMSIP604DOESNOTEXISTANYWHERE | 0XA3000000 + CAUSE_UNALLOCATEDNUMBER |
| CAUSE_CTICCMSIP606NOTACCEPTABLE | 0XA4000000 + CAUSE_NORMALUNSPECIFIED |
| CAUSE_CTICCMSIP200CALLCOMPLETEDELSEWHERE | 0xA5000000 + NORMALUNSPECIFIED |
| CAUSE_CTICCMSIP503SERVICENOTAVAILABLE | 0xA7000000 + SERVNOTAVAILUNSPECIFIED |

| Note | Traces can be directed to a specific path and folder rather than to the application directory by default. The same trace folder
                                          could be used for successive or more than one simultaneous launch of JTAPI. Different launches of JTAPI would also send traces
                                          to different folders. This allows simultaneous JTAPI instances to maintain independent trace destinations. The application
                                          directory in this case is not that of the JTAPI client itself, but of the application that is integrating/using the JTAPI
                                          client. |
|---|---|

| SN | Problem Description | Cause | Solution |
|---|---|---|---|
| 1 | ISMP Uninstall does not remove the target directories
                                          					 installed. | Directory from which uninstaller is invoked. | The uninstaller needs to be invoked from at least one level
                                          					 above the install directory. |
| 2 | Proper language details are not displayed during installation | Locale Files not proper. | Please report this problem immediately to the support
                                          					 personnel to suggest the change or error in message. |
| 3 | Uninstaller/Installer throws error. | The JVM has been either removed or replaced with an
                                          					 incompatible version | The installer comes with a built in JVM which also gets
                                          					 installed if the target machine does not have a JVM. In case you face this
                                          					 error - manual removal of the files needs to be done. |
| 4 | Installer goes through fine,  but the files have not been
                                          					 copied. | Permissions | Ensure that proper write permissions are there for the
                                          					 destination folder. This problem can occur on UNIX platforms. |
| 5 | Installer/Uninstaller throws exception or crashes during the
                                          					 installation process. | version name problem / folder name problem. | Refer to the log files generated to get an idea of which step
                                          					 caused the error. |
| 6 | Upgrade does not show "upgrade" message during installation of an upgrade
                                          					 version. | .jtapiver.ini missing. | This file is where the current jtapi install details are
                                          					 located. If this is accidently removed then,  upgrade/reinstall will have
                                          					 display issues. In the case of an upgrade/reinstall or downgrade failure,  the
                                          					 user will have to manually remove the files from the .jtapi/bin and .jtapi/lib
                                          					 folders and then try the installer in order to ensure proper installation
                                          					 during the next time. |