---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-icm-enterprise-icm-enterprise-15-0-1-user-ucce-b-a0249ecfdd
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/icm_enterprise/icm_enterprise_15_0_1/user/ucce_b_150_outbound-option-guide-for-unified/registry_settings.html
retrieved_at: 2026-08-16T20:35:40.186180+00:00
---

Outbound Option Guide for Unified Contact Center Enterprise, Release 15.0(1)

# Outbound Option Guide for Unified Contact Center Enterprise, Release 15.0(1)

Updated: April 30, 2025

Chapter: Registry Settings

## Chapter: Registry Settings

- Registry Settings

- Campaign Manager Registry Settings

- Dialer Registry                              	 Settings

# Registry Settings

## Campaign Manager Registry Settings

The following registry settings modify the behavior of the Campaign Manager:

Registry Setting

Default Setting

Description

BADBDriveFreeSpaceThreshold

20% free.

Indicates the percentage of free space left on the Microsoft SQL Server drive where the Outbound Option database is installed
                                          before an alarm is raised.

BADbFreeSpaceThresholdInPercent.

20% free.

Indicates the percentage of free space left on the Outbound Option database before an alarm is raised.

CallbackTimeLimit (Campaign Manager only)

15 minutes

Calculates the callback time range for each personal and regular callback in minutes. The Campaign Manager queries the Personal
                                          or Regular Callback List for callback records, where the CallbackDateTime database column value is between the current time
                                          and current time minus the CallbackTimeLimit. For example, if the current time is 3:00 PM and the CallbackTimeLimit is 15
                                          minutes, the query to retrieve Personal Callback records is "where CallbackDateTime >= 2:45 PM and CallbackDateTime <= 3:00 PM." This column is also used to control how long a Personal or Regular Callback is retried after it is sent to a dialer. If the
                                          CallbackTimeLimit is set to 15 minutes, the Dialer keeps reserving the agent and calling the customer for 15 minutes before
                                          giving up for that day. For Personal Callbacks, the Dialer re-reserves the agent based on the PersonalCallbackTimeToRetryReservation
                                          registry entry.

ContactTableImportThreshold

Default Value is 1 million, and if the value is set to 0 you will not receive the SNMP trap.

This is a threshold for number of records in a contact table. If number of records go beyond this threshold value, SNMP trap
                                          will be generated corresponding to that contact table after every successful import.

DialerDetailBufferSize

20

Describes how many dialer detail records should be buffered before sending to the Central Controller database.

DialerDetailBufferTimeout

5

Describes how long to wait before sending dialer detail records to the Central Controller database when the DialerDetailBufferSize
                                          is not reached.

DialerDetailEnabled

TRUE

When set to 0, dialer detail records are not sent from campaign manager. All Dialer Detail records are disabled.

DialingListCallStatusToPurge

If the registry entry is missing, the default values are C,M, and D.

A string containing the call status types of records in the Dialing_list table to be included in the automated purge. The
                                          types specified are compared with the value of CallStatusZone1. For example, if the string contains "C,M,F,L,I," any calls with these call statuses are purged from the database.

This registry setting is not added by default; it must be added manually.

To be purged, records must also be older than the number of days set in DialingListDaysToPurgeOldRecords.

DialingListDaysToPurgeOldRecords

Minimum value is 1; maximum value is 30; default is 5 days

The number of days after the record is imported before it is included in the automated purge of the Dialing_list table. This
                                          value is compared with ImportRuleDate.

To be purged, records must also have a call status that is set in DialingListCallStatusToPurge.

DNCDBPollingInSec

Minimum value is 10 seconds; maximum value is 600 seconds; default value is 60 seconds.

Do Not Call Records are loaded into the Campaign Manager by the Campaign Manager's periodic reading of the Do_Not_Call table.
                                          The polling frequency of this operation is determined by this registry key in seconds.

EMTClientTimeoutToFailover

Default value: 60 seconds

The interval time, in seconds, at which the active Campaign Manager sends the failover message to the router if the Dialer
                                          or BAImport do not connect with the Campaign Manager.

Set this registry value. If it is not set, the default value of 60 seconds is used.

EMTHeartBeat (Outbound Option Import only)

500 milliseconds

Outbound Option Import sends a heartbeat message to Campaign Manager every n milliseconds to indicate that it is still alive.

ImportAreaCodeProcDisable (Outbound Option Import only)

0, enabled

When set to 0, this setting performs standard region_prefix matching. When set to 1, the GMT time zones are always set to
                                          the local time zone of the ICM Logger.

If there is a prefix match, the GMT time zones for each customer record are retrieved from the Region_Prefix table.

ImportRegLocalNumberSize (Outbound Option Import only)

7 digits

The number of digits in a phone number must be greater than this registry entry to perform a search of the region_prefix table.

MinimumCallsForHitRate (Campaign Manager only)

30 calls

Specifies the minimum number of calls that have to be attempted before the hit-rate percentage calculation begins for a campaign
                                          query rule.

PendingOverRetryEnabled

0

When set to 1, pending records get priority over retry records for all campaigns.

PersonalCallbackNoAnswerRingLimit (Campaign Manager only)

Minimum value is 2; maximum value is 10; default is 4 rings

The number of times a customer phone rings before being classified as an unanswered call.

PersonalCallbackCallStatusToPurge (Campaign Manager only)

If the registry entry is missing, the default values are C,M,D.

A string containing the call status types of records in the Personal_Callback_List table to be included in the automated purge.
                                          For example, if the string contains "C,M,F,L,I," all calls with these call statuses are purged from the database.

This registry setting is not added by default; it must be added manually.

PersonalCallbackDaysToPurgeOldRecords (Campaign Manager only)

Minimum value is 1; maximum value is 30; default is 5 days

The number of days after the personal callback has been scheduled to keep the record before it is purged.

PersonalCallbackDisableViaQueryRule (Campaign Manager only)

0

This registry key determines if the Callback has to be enabled if the query rule is disabled.

PersonalCallbackMaxAttemptsDefault (Campaign Manager only)

5

Sets the maximum number of times a personal callback is attempted (minimum value is 1; maximum value is 20). When the number
                                          of maximum attempts reaches 0, the record is not tried again and the status is set to M (maxed out).

PersonalCallbackMode

1

Not used.

PersonalCallbackRecordsToCache (Campaign Manager only)

Minimum value is 5; maximum value is 200 ; default is 20

The number of personal callback records to send to the Outbound Option Dialer at one time.

PersonalCallbackReattempt

1

You can leverage the capabilities of this registry by installing the Unified CCE 15.0(1) ICM15.0.1_ES202508 .

To control the Campaign Manager from rescheduling the unreachable outbound personal callback calls, set any one of the following
                                          value to the PersonalCallbackReattempt registry:

Set to 1 (default): Campaign Manager automatically reschedules personal callback attempt based on campaign configuration until maximum
                                                attempt is reached. Once the maximum attempts is exhausted, the callback record is closed and record status as M (“maxed out”).

Set to 0 : Disables rescheduling of unreachable personal callback records with call results 2, 4, 6, 8, 9, or 16. These records are
                                                marked with status 'C' and the maximum attempt count remains unchanged.

Ensure you retain the same PersonalCallbackReattempt registry value in both Campaign Manager and Dialer Registry settings.

If this registry setting is changed, the ICM Logger must be restarted before the new values take effect.

PersonalCallbackReattemptNoRingBack

1

Indicates whether the personal callback should be counted as attempted or not.

Set any one of the following value to the PersonalCallbackReattemptNoRingBack registry:

Set to 1 (default): If no ringback is received when attempting to call the customer, the call attempt will not be counted, and it
                                                will be rescheduled for the next business day.

Set to 0 : The dialer reschedule the personal callback after NoAnswerRetryTime. If no ringback is received on the outbound customer
                                                call, the call attempt is counted and the callback is rescheduled to redial until it reaches the maximum number of attempts.

Ensure the PersonalCallbackReattempt registry is set to 1 to get the expected behavior. If PersonalCallbackReattempt is set
                                                            to 0, NoRingback is not reattempted.

You must retain the same PersonalCallbackReattemptNoRingBack registry value in both Campaign Manager and Dialer Registry settings.

If this registry setting is changed, the ICM Logger must be restarted before the new values take effect.

PersonalCallbackSaturdayAllowed (Campaign Manager only)

0

Indicates whether personal callbacks are allowed on Saturdays.

0: Personal callbacks are not allowed on Saturdays and are scheduled for the next allowable day. For example, a personal callback
                                                which fails to reach the customer on a Friday is rescheduled for the following Monday.

1: Personal callbacks are allowed on Saturdays.

PersonalCallbackSundayAllowed (Campaign Manager only)

0

Indicates whether personal callbacks are allowed on Sundays.

0: Personal callbacks are not allowed on Sundays and are scheduled for the next allowable day. For example, a personal callback
                                                which fails to reach the customer on a Friday or Saturday is rescheduled for the following Monday.

1: Personal callbacks are allowed on Sundays.

PersonalCallbackTimeToCheckForRecords (Campaign Manager only)

Minimum value is 1; maximum value is 30; default is 1 minute

The interval time, in minutes, at which the Outbound Option Dialer checks the Campaign Manager for personal callback records.

PersonalCallbackTimeToRetryBusy (Campaign Manager only)

Minimum value is 1; maximum value is 10; default is 1 minute

Sets the amount of time, in minutes, that the Outbound Option Dialer waits before retrying a personal callback when the customer’s
                                          phone is busy.

PersonalCallbackTimeToRetryNoAnswer (Campaign Manager only)

Minimum value is 5; maximum value is 60; default is 20 minutes

Sets the amount of time, in minutes, that the Outbound Option Dialer waits before retrying a personal callback when the customer
                                          does not answer the phone.

PersonalCallbackTimeToRetryReservation (Campaign Manager only)

Minimum value is 1; maximum value is 10; default is 1 minute

Sets the amount of time, in minutes, that the Outbound Option Dialer waits before retrying to reserve an agent if the agent
                                          is not available.

ReplicationExpirationThreshold

600 seconds

Controls the expiration threshold for replication.

If the data is not replicated within this threshold, an EMS Report Event is signaled periodically until the condition has
                                          improved.

RescheduleCallbacks (Campaign Manager only)

1

Boolean value.

Controls how to handle contacts that were requested to be called back at a particular time, but were left out in Pending call
                                          status 'P', for whatever reason.

0: Pending dialing records are not rescheduled or purged.

1: Pending dialing records are scheduled for retry at the next valid time.

SQLServer (Campaign Manager and Outbound Option Import)

null

Not used.

TCD_DBComputerName_A

""

Not used.

TCD_DBComputerName_B

""

Not used.

TCD_DBDatabaseName_A

""

Not used.

TCD_DBDatabaseName_B

""

Not used.

TCDCopyPendingEnabled

0

Not used.

TCDEnabled

0

Not used.

TCDKeepDays

30

Not used.

TimeToResetDailyStats (Campaign Manager only)

30 minutes after midnight ( "00:30" )

Specifies the time of day (in 24-hour format: hh:mm) when the real-time statistics for DialerRealTime and CampaignQueryRealTime
                                          are reset.

UnknownCallStatusResetTime (Campaign Manager only)

60 minutes

The interval time, in minutes, at which the Campaign Manager resets the contact records in Unknown status to Pending status
                                          (available for reuse).

EnableMaxAttemptsPerNumber

0

Enable the maximum attempts per phone number in a record.

For example: If every phone number has to be dialed only once then configure MaxAttempts to 1 and set EnableMaxAttemptsPerNumber to 1.

BAReplDriveFreeSpaceThreshold

15 Seconds

Represents the percentage of free Logger drive space allowed before outbound option replication stops and the databases are
                                          no longer in sync.

ReplicationFileSwitchDuration

15 Seconds

Represents the amount of time before temporary files are renamed to replication files. This registry also provides information
                                          to the standby Campaign Manager if it were to observe a temporary file remaining open for longer than this duration.

## Dialer Registry
                        	 Settings

The following
                              		  registry settings modify the behavior of the Outbound Option Dialer. To specify
                              		  the exact path, modify the registry path for the dialer to HKEY_LOCAL_MACHINE\SOFTWARE\Cisco Systems, Inc.\ICM\<instance
                                 			 name>\Dialer instead of HKEY_LOCAL_MACHINE\SOFTWARE\Cisco Systems, Inc.\\Dialer .

Registry
                                          						Setting

Default
                                          						Setting

Description

AnswerTransferUsingAgentPhone

1

When enabled (1), the dialer automatically answers customer calls transferred to agent phones.

AutoAnswerCall

1

This registry key is not created until the process starts up. It controls whether the Dialer auto-answers the call or not.
                                          The guideline is to disable this and uses the auto-answer in Unified CM, if you want zip tone.

Ca_cnosig

20 seconds

Amount of
                                          						silence before no ringback is returned, in seconds. If ringback is not detected
                                          						within this time limit, the call is dropped.

CancelDialingCalls

0

Controls behavior when started call attempts can be canceled once all agents are occupied and abandon to IVR is not configured.
                                          Setting to 0 never cancels calls after they have been started. Setting to 1 always cancels calls after they have been started
                                          once no agents are available. A value of 100 cancels all ringing calls that are less than 100 milliseconds after the dialing
                                          was started (that is,  the line went off hook.

When CancelDialingCalls = 0, it cancels calls not confirmed to reach the customer (which means SIP progress messages of 180,
                                                            181, 182, or 183 not yet received). The abandon to IVR configuration is ignored for canceling in this case.

When CancelDialingCalls > 0, and abandon to IVR configuration is enabled, the only calls that have not yet started while
                                                            waiting in the Port Throttle queue, are canceled.

CaptureEnabled

0

When set
                                          						to 0, packet capturing is disabled; when set to 1, packet capturing is enabled.

CaptureOptions

-i 2 -tt
                                          						-C 20 -s 0 -W 20 -w DialerCapture

Options
                                          						associated with packet capture:

-i
                                                							 <ifname>: Interface name to capture on

-tt :
                                                							 Print an unformatted time stamp on each dump line.

-w <filename>: Capture directly to file in pcap format, the file can be opened with Wireshark.

-C
                                                							 <file_size>: The maximum size of a capture file. The units of file_size
                                                							 are millions of bytes (1,000,000 bytes, not 1,048,576 bytes).

-W
                                                							 <filecount>: The number of files created. The capture files are
                                                							 overwritten from the beginning, thus creating a rotating buffer. Capture files
                                                							 after the first capture file have the name specified with the -w flag, with a
                                                							 number after it, starting at 1 and continuing upward.

-s : Snarf snaplen bytes of data from each packet rather than the default of 68 Setting snaplen to 0 means use the required length to catch whole packets.

CaptureType

1

When set
                                          						to 1, capture SIP packets only. When set to 2, capture the entire data payload
                                          						on the Dialer host machine.

CCMTransferDelay

0

Not used.

CMServerA

NA

The
                                          						hostname or IP address of the Campaign Manager on Side A.

CMServerB

NA

The
                                          						hostname or IP address of the Campaign Manager on Side B.

ConsecutiveNoDialToneEvents

3

Not used.

CPAActiveThreshold

32

Signal
                                          						must exceed CPAActiveThreshold*noiseThreshold to be considered active. For
                                          						example, 32 is 10 * log(32) = 15 dB.

CPAJitterBufferDelay

150

The
                                          						jitter buffer delay (in mS).

CPAMaxNoiseFloor

10000

Maximum
                                          						Noise floor possible. Used to restrict noise floor measurement.

CPAMinNoiseFloor

1000

Minimum
                                          						Noise floor possible. Used to restrict noise floor measurement.

CPAMaxToneSTDEV

0.600000

Standard
                                          						deviation of zero crossing rate per block. Values lower than this and
                                          						CPAMaxEnergySTDev are considered tones.

CPANoiseThresholdPeriod

100ms

The amount of time to wait for the initial voice. The CPAAnalysisPeriod starts once the system detects speech.

CPARecordWaveFile

0 (off)

Setting
                                          						this entry to 1 enables recording of the CPA period to assist in
                                          						troubleshooting. The key must be added to be enabled.

CTIServerA

""

The
                                          						machine name where CTI Server-Side A resides.

CTIServerB

""

The
                                          						machine name where CTI Server-Side B resides.

CTIServerPortA

""

The TCP
                                          						port number where CTI Server-Side A listens.

CTIServerPortB

""

The TCP
                                          						port number where CTI Server-Side B listens.

CustRecReadyRequestToServer

30
                                          						seconds

Describes the polling interval when the campaign is enabled,
                                          						agents are available, and the Dialer needs more records from the Campaign
                                          						Manager. The first request is sent when the Dialer notices that it is low on
                                          						records. Subsequent requests are sent after the TimeToWaitForRecord times out,
                                          						based on this polling interval until more records are received.

DirectAgentDial

0

Not
                                          						used.

DisableIPCPA

0

Disables
                                          						call progress analysis for this Dialer.

EMTHeartBeat

500
                                          						milliseconds

Dialer
                                          						sends a heartbeat message to the Campaign Manager every n millisecond to
                                          						indicate that it is still alive.

EnhancedPredictiveDialing

N/A ( Manual Registry)

If there is no registry value or if the registry value is set as
                                          									zero, Unified CCE uses the existing predictive algorithm.

If the registry value is set to 1, Unified CCE uses the Enhanced
                                          									Predictive Algorithm.

Enable this registry only when there is a low hit rate with long idle agent times. This change adjusts the dialing rate more
                                                      aggressively, so it may not respect the configured abandon limit.

EnableAutoAcceptFeature

0

Generally, an agent must respond to the Preview dialog when a reservation call is placed. With the implementation of the Auto
                                          Accept feature, the Outbound Option Dialer implements the Auto-Accept functionality. It causes the Dialer to Auto-ACCEPT the
                                          preview call in n seconds if the agent fails to respond to the preview dialog. The same applies to Personal Callback calls.

This
                                          						feature is disabled by default and the registry key must be set to one (1) to
                                          						enable the feature.

The
                                          						PreviewReservationTimeout registry key is used to configure the auto-accept
                                          						timer value.

EnableHeartbeat

1
                                          						(enabled)

EnableHeartbeat registry is used to enable heartbeats on the
                                          						dialer. When this flag is enabled, the dialer sends heartbeats (SIP OPTIONS
                                          						request message) to the SIP server - Proxy or Gateway.

If
                                          						there is no response from the SIP server, the dialer marks itself as not ready
                                          						and inform the same to the campaign manager.

If this
                                          						registry is disabled, there is no indication if the SIP server goes down.

HBInterval

5
                                          						seconds

The time
                                          						between heartbeats.

HBNumTries

1

The
                                          						number of times a timeout occurs before the SIP Dialer identifies the SIP
                                          						Gateway or SIP Proxy as down.

LongDistancePrefix

"1"

Not
                                          						used.

MaxAllRecordFiles

500,000,000

The
                                          						maximum recording file size (in bytes) per SIP Dialer.

MaxMediaTerminationSessions

200

The
                                          						maximum number of media termination sessions per SIP Dialer if recording is
                                          						enabled in the Campaign configuration.

MaxPortCapacityReachedCount

30

The number of failed attempts to reserve a port before the Dialer logs a
                                          									warning. The message states that the Dialer has reached maximum port
                                          									capacity. The counter resets to 0 after logging the message.

MaxPurgeRecordFiles

100,000,000

The
                                          						maximum recording file size (in bytes) that the SIP Dialer deletes when the
                                          						total recording file size, MaxAllRecordFiles, is reached.

MaxRecordingSessions

100

The
                                          						maximum number of recording sessions per SIP Dialer if recording is enabled in
                                          						the Campaign configuration.

MRPort

38001

The
                                          						connection port for the MR PIM.

OptimizeAgentAvailability

0

This
                                          						registry entry is reserved for future use. Leave the value of this parameter at
                                          						0.

OverrideNetworkTones

0

Not
                                          						used.

PersonalCallbackDN

"PersonalCallback"

Contains
                                          						a script name that the MR PIM receives as a dialed number when personal
                                          						callback calls require to reserve agents.

PersonalCallbackReattempt

1

You can leverage the capabilities of this registry by installing the Unified CCE 15.0(1) ICM15.0.1_ES202508 .

To control the Dialer from attempting to retry the unreachable outbound personal callback calls, set any one of the following
                                          value to the PersonalCallbackReattempt registry:

Set to 1 (default): The dialer immediately reattempts the unreachable personal callback calls or sends the record back to Campaign
                                                Manager for rescheduling.

Set to 0 : Disables redialing of personal callback records that were unreachable, with call results 2, 4, 6, 8, 9, or 16. These records
                                                are sent back to Campaign Manager and marked as closed.

Ensure you retain the same PersonalCallbackReattempt registry value in both Campaign Manager and Dialer Registry settings.

If this registry setting is changed, the Dialer must be restarted before the new values take effect.

PersonalCallbackReattemptNoRingBack

1

Indicates whether the Dialer must retry or redial outbound personal callbacks in case of the following scenarios:

Customer number is switched off or not reachable.

Customer disconnects the call.

Customer on a different call and the call is being dropped.

Set any one of the following value to the PersonalCallbackReattemptNoRingBack registry:

Set to 1 (default): Dialer retries the call every one minute until the CallbackTimeLimit is reached.

Set to 0 : Disables the Dialer from redialing personal callbacks within the duration set in CallbackTimeLimit, set the registry key
                                                value to 0.

Ensure the PersonalCallbackReattempt registry is set to 1 to get the expected behavior. If PersonalCallbackReattempt is set
                                                            to 0, NoRingback is not reattempted.

You must retain the same PersonalCallbackReattemptNoRingBack registry value in both Campaign Manager and Dialer Registry settings.

If this registry setting is changed, the Dialer must be restarted before the new values take effect.

PreviewReservationTimeout

600

Number of seconds to wait before canceling a preview agent’s reservation call. This key is automatically created when the
                                          Dialer starts. If a preview agent does not accept or reject a call within this time period, the agent’s reservation call is dropped and the record is marked as rejected.

ReclassifyTransferFailures

0

When set to 1, answering machine calls that
                                          									are abandoned due to lack of agent or IVR resources are not
                                          									counted as abandoned voice calls.

They will be counted as answering machine
                                          									calls. This registry is also enabled by default on fresh
                                          									installs, and disabled in upgraded systems.

RTPortFeedDisable

1

When
                                          						set, real-time dialer port messages are disabled for this dialer. Enabling the
                                          						Real-Time Port Feed by setting to 0 causes the dialpr01 report to populate, but
                                          						this can cause impacts to the Outbound Campaign in delays in getting records.

SetAgentsReadyOnResvDrop

1

When set
                                          						to 1, the Outbound Option Dialer automatically sets manual IN agents to the
                                          						Ready state, if the reservation call is dropped due to any reason other than
                                          						transfer of a live customer call.

If this value is set to 0, then manual IN agents
                                          									assume the After Call Work (ACW) state at the end of each reservation call
                                          									and manually become ready to receive another call.

SetAgentsReadyOnResvDrop is applicable only for TDM dialer.

SIPDialerPortBaseNumber

58800

SIPServerAddress

NULL

The IP
                                          						address or DNS hostname of the SIP Proxy or SIP Gateway that this Dialer
                                          						connects to, as specified during setup.

SIPServerPortNumber

5060

The port
                                          						number that the SIP Dialer uses to communicate with the server.

SIPServerTransportType

1

The transport type used to communicate with the gateway/ CCCSP .

A
                                          						setting of 1 indicates that the transport type is UDP, and a setting of 2
                                          						indicates that the transport type is TCP. Currently, only UDP is supported.

SkillGroupQueryDelay

1 second

The
                                          						amount of time, in seconds, to wait between CTI Server skill group query
                                          						requests.

SwitchPrefix

""

Dialing
                                          						prefix prepended to every phone number; for example, this entry could be used
                                          						to dial an outside line access number, such as 9.

TalkTimeAvg

60
                                          						seconds

The
                                          						amount of time an average customer call takes. (Seed value for talk time, which
                                          						is adjusted as a moving average as the system is used.)

TestNumberMaxDigits

5

Maximum
                                          						length for test phone numbers. Test phone numbers do not receive any prefixes
                                          						added by the Dialer.

TFTPServer

""

The name of the Unified CM TFTP server. This
                                          									server is usually located on the Publisher Unified CM.

TimeToCTIBeginCall

7
                                          						seconds

The amount of time, in seconds, to wait for the CTI begin call event before canceling the call.

TimeToFreeStuckCall

7200
                                          						seconds, which is 2 hours

The
                                          						amount of time, in seconds, before a customer call is declared stuck and
                                          						dropped.

TimeToFreeStuckPort

7200
                                          						seconds, which is 2 hours

The
                                          						amount of time, in seconds, to wait before releasing a stuck port.

TimeToHoldCustomer

1 second

The
                                          						amount of time, in seconds, to wait before abandoning a customer call due to
                                          						lack of agents. If abandon to IVR is enabled for campaigns, this value should
                                          						be set to 0 to reduce transfer delays.

TimeToReserve

10
                                          						seconds

The
                                          						amount of time, in seconds, to wait before dropping a reservation call.

TimeToRetryCustomerRequest

30
                                          						seconds

The
                                          						amount of time, in seconds, to wait before retrying a close customer record
                                          						request to the Campaign Manager.

When the
                                          						Outbound Option Dialer finishes with a customer record, it sends a close
                                          						customer record request message to the Campaign Manager. If this message is not
                                          						sent, the Outbound Option Dialer retries the call based on the configured
                                          						timeout.

TimeToRingCustomer

8
                                          						seconds

The
                                          						amount of time, in seconds, each customer ring takes. For example, if this
                                          						entry is set to 8 and the no-answer configuration in the campaign is set to 3
                                          						rings, then the Dialer classifies the call as no-answer within 3*8 (24)
                                          						seconds.

TimeToTransfer

7
                                          						seconds

The
                                          						amount of time, in seconds, to wait before dropping a call being transferred.

TimeToWaitForCTIResp

3
                                          						seconds

The
                                          						amount of time, in seconds, to wait for the CTI Server to respond to a request
                                          						before dropping the call.

TimeToWaitForIPDialTone

10 seconds

The amount of time, in seconds, to wait for the
                                          									Unified CM dial tone.

TimeToWaitForMRIResponse

600
                                          						seconds (10 minutes)

The
                                          						amount of time, in seconds, to wait for the MR PIM to respond to a new task
                                          						request before canceling the request.

TimeToWaitForRecord

5
                                          						seconds

The
                                          						amount of time, in seconds, to wait for customer records from the Campaign
                                          						Manager before declaring the skill group disabled.

Once a
                                          						skill group has been disabled, the Dialer begins polling the Campaign Manager
                                          						every <CustRecReadyRequestToServer> second for additional records.

| Registry Setting | Default Setting | Description |
|---|---|---|
| BADBDriveFreeSpaceThreshold | 20% free. | Indicates the percentage of free space left on the Microsoft SQL Server drive where the Outbound Option database is installed
                                          before an alarm is raised. |
| BADbFreeSpaceThresholdInPercent. | 20% free. | Indicates the percentage of free space left on the Outbound Option database before an alarm is raised. |
| CallbackTimeLimit (Campaign Manager only) | 15 minutes | Calculates the callback time range for each personal and regular callback in minutes. The Campaign Manager queries the Personal
                                          or Regular Callback List for callback records, where the CallbackDateTime database column value is between the current time
                                          and current time minus the CallbackTimeLimit. For example, if the current time is 3:00 PM and the CallbackTimeLimit is 15
                                          minutes, the query to retrieve Personal Callback records is "where CallbackDateTime >= 2:45 PM and CallbackDateTime <= 3:00 PM." This column is also used to control how long a Personal or Regular Callback is retried after it is sent to a dialer. If the
                                          CallbackTimeLimit is set to 15 minutes, the Dialer keeps reserving the agent and calling the customer for 15 minutes before
                                          giving up for that day. For Personal Callbacks, the Dialer re-reserves the agent based on the PersonalCallbackTimeToRetryReservation
                                          registry entry. |
| ContactTableImportThreshold | Default Value is 1 million, and if the value is set to 0 you will not receive the SNMP trap. | This is a threshold for number of records in a contact table. If number of records go beyond this threshold value, SNMP trap
                                          will be generated corresponding to that contact table after every successful import. |
| DialerDetailBufferSize | 20 | Describes how many dialer detail records should be buffered before sending to the Central Controller database. |
| DialerDetailBufferTimeout | 5 | Describes how long to wait before sending dialer detail records to the Central Controller database when the DialerDetailBufferSize
                                          is not reached. |
| DialerDetailEnabled | TRUE | When set to 0, dialer detail records are not sent from campaign manager. All Dialer Detail records are disabled. |
| DialingListCallStatusToPurge | If the registry entry is missing, the default values are C,M, and D. | A string containing the call status types of records in the Dialing_list table to be included in the automated purge. The
                                          types specified are compared with the value of CallStatusZone1. For example, if the string contains "C,M,F,L,I," any calls with these call statuses are purged from the database. This registry setting is not added by default; it must be added manually. To be purged, records must also be older than the number of days set in DialingListDaysToPurgeOldRecords. Note The call status values can optionally be delimited using a comma, a hyphen, a semi-colon, or a colon. | Note | The call status values can optionally be delimited using a comma, a hyphen, a semi-colon, or a colon. |
| Note | The call status values can optionally be delimited using a comma, a hyphen, a semi-colon, or a colon. |
| DialingListDaysToPurgeOldRecords | Minimum value is 1; maximum value is 30; default is 5 days | The number of days after the record is imported before it is included in the automated purge of the Dialing_list table. This
                                          value is compared with ImportRuleDate. To be purged, records must also have a call status that is set in DialingListCallStatusToPurge. |
| DNCDBPollingInSec | Minimum value is 10 seconds; maximum value is 600 seconds; default value is 60 seconds. | Do Not Call Records are loaded into the Campaign Manager by the Campaign Manager's periodic reading of the Do_Not_Call table.
                                          The polling frequency of this operation is determined by this registry key in seconds. |
| EMTClientTimeoutToFailover | Default value: 60 seconds | The interval time, in seconds, at which the active Campaign Manager sends the failover message to the router if the Dialer
                                          or BAImport do not connect with the Campaign Manager. Set this registry value. If it is not set, the default value of 60 seconds is used. |
| EMTHeartBeat (Outbound Option Import only) | 500 milliseconds | Outbound Option Import sends a heartbeat message to Campaign Manager every n milliseconds to indicate that it is still alive. |
| ImportAreaCodeProcDisable (Outbound Option Import only) | 0, enabled | When set to 0, this setting performs standard region_prefix matching. When set to 1, the GMT time zones are always set to
                                          the local time zone of the ICM Logger. If there is a prefix match, the GMT time zones for each customer record are retrieved from the Region_Prefix table. Note Time zones are selected based on the data in the Region_Prefix database. When contacts are imported, the phone number is assigned
                                                   a time zone based on the information in the region prefix table. Each prefix has settings for the time zone and daylight savings
                                                   observation. If the prefix of the contact number does not match any of the prefixes listed in the region prefix table, then
                                                   the contact number is assigned the time zone listed in the campaign configuration tool Call Target Tab. Note If this registry setting changes, the ICM Logger must be restarted before the new values take effect. Alternatively, restart
                                                   the Outbound Option Import process by closing its console window. | Note | Time zones are selected based on the data in the Region_Prefix database. When contacts are imported, the phone number is assigned
                                                   a time zone based on the information in the region prefix table. Each prefix has settings for the time zone and daylight savings
                                                   observation. If the prefix of the contact number does not match any of the prefixes listed in the region prefix table, then
                                                   the contact number is assigned the time zone listed in the campaign configuration tool Call Target Tab. | Note | If this registry setting changes, the ICM Logger must be restarted before the new values take effect. Alternatively, restart
                                                   the Outbound Option Import process by closing its console window. |
| Note | Time zones are selected based on the data in the Region_Prefix database. When contacts are imported, the phone number is assigned
                                                   a time zone based on the information in the region prefix table. Each prefix has settings for the time zone and daylight savings
                                                   observation. If the prefix of the contact number does not match any of the prefixes listed in the region prefix table, then
                                                   the contact number is assigned the time zone listed in the campaign configuration tool Call Target Tab. |
| Note | If this registry setting changes, the ICM Logger must be restarted before the new values take effect. Alternatively, restart
                                                   the Outbound Option Import process by closing its console window. |
| ImportRegLocalNumberSize (Outbound Option Import only) | 7 digits | The number of digits in a phone number must be greater than this registry entry to perform a search of the region_prefix table. Note If this registry setting changes, the ICM Logger must be restarted before the new values take effect. Alternatively, restart
                                                   the Outbound Option Import process by closing its console window. | Note | If this registry setting changes, the ICM Logger must be restarted before the new values take effect. Alternatively, restart
                                                   the Outbound Option Import process by closing its console window. |
| Note | If this registry setting changes, the ICM Logger must be restarted before the new values take effect. Alternatively, restart
                                                   the Outbound Option Import process by closing its console window. |
| MinimumCallsForHitRate (Campaign Manager only) | 30 calls | Specifies the minimum number of calls that have to be attempted before the hit-rate percentage calculation begins for a campaign
                                          query rule. |
| PendingOverRetryEnabled | 0 | When set to 1, pending records get priority over retry records for all campaigns. |
| PersonalCallbackNoAnswerRingLimit (Campaign Manager only) | Minimum value is 2; maximum value is 10; default is 4 rings | The number of times a customer phone rings before being classified as an unanswered call. |
| PersonalCallbackCallStatusToPurge (Campaign Manager only) | If the registry entry is missing, the default values are C,M,D. | A string containing the call status types of records in the Personal_Callback_List table to be included in the automated purge.
                                          For example, if the string contains "C,M,F,L,I," all calls with these call statuses are purged from the database. This registry setting is not added by default; it must be added manually. Note The call status values can optionally be delimited using a comma, a hyphen, a semi-colon, or a colon. | Note | The call status values can optionally be delimited using a comma, a hyphen, a semi-colon, or a colon. |
| Note | The call status values can optionally be delimited using a comma, a hyphen, a semi-colon, or a colon. |
| PersonalCallbackDaysToPurgeOldRecords (Campaign Manager only) | Minimum value is 1; maximum value is 30; default is 5 days | The number of days after the personal callback has been scheduled to keep the record before it is purged. |
| PersonalCallbackDisableViaQueryRule (Campaign Manager only) | 0 | This registry key determines if the Callback has to be enabled if the query rule is disabled. |
| PersonalCallbackMaxAttemptsDefault (Campaign Manager only) | 5 | Sets the maximum number of times a personal callback is attempted (minimum value is 1; maximum value is 20). When the number
                                          of maximum attempts reaches 0, the record is not tried again and the status is set to M (maxed out). |
| PersonalCallbackMode | 1 | Not used. |
| PersonalCallbackRecordsToCache (Campaign Manager only) | Minimum value is 5; maximum value is 200 ; default is 20 | The number of personal callback records to send to the Outbound Option Dialer at one time. |
| PersonalCallbackReattempt | 1 | You can leverage the capabilities of this registry by installing the Unified CCE 15.0(1) ICM15.0.1_ES202508 . To control the Campaign Manager from rescheduling the unreachable outbound personal callback calls, set any one of the following
                                          value to the PersonalCallbackReattempt registry: Set to 1 (default): Campaign Manager automatically reschedules personal callback attempt based on campaign configuration until maximum
                                                attempt is reached. Once the maximum attempts is exhausted, the callback record is closed and record status as M (“maxed out”). Set to 0 : Disables rescheduling of unreachable personal callback records with call results 2, 4, 6, 8, 9, or 16. These records are
                                                marked with status 'C' and the maximum attempt count remains unchanged. Note Ensure you retain the same PersonalCallbackReattempt registry value in both Campaign Manager and Dialer Registry settings. If this registry setting is changed, the ICM Logger must be restarted before the new values take effect. | Note | Ensure you retain the same PersonalCallbackReattempt registry value in both Campaign Manager and Dialer Registry settings. If this registry setting is changed, the ICM Logger must be restarted before the new values take effect. |
| Note | Ensure you retain the same PersonalCallbackReattempt registry value in both Campaign Manager and Dialer Registry settings. If this registry setting is changed, the ICM Logger must be restarted before the new values take effect. |
| PersonalCallbackReattemptNoRingBack | 1 | Indicates whether the personal callback should be counted as attempted or not. Set any one of the following value to the PersonalCallbackReattemptNoRingBack registry: Set to 1 (default): If no ringback is received when attempting to call the customer, the call attempt will not be counted, and it
                                                will be rescheduled for the next business day. Set to 0 : The dialer reschedule the personal callback after NoAnswerRetryTime. If no ringback is received on the outbound customer
                                                call, the call attempt is counted and the callback is rescheduled to redial until it reaches the maximum number of attempts. Note Ensure the PersonalCallbackReattempt registry is set to 1 to get the expected behavior. If PersonalCallbackReattempt is set
                                                            to 0, NoRingback is not reattempted. You must retain the same PersonalCallbackReattemptNoRingBack registry value in both Campaign Manager and Dialer Registry settings. If this registry setting is changed, the ICM Logger must be restarted before the new values take effect. | Note | Ensure the PersonalCallbackReattempt registry is set to 1 to get the expected behavior. If PersonalCallbackReattempt is set
                                                            to 0, NoRingback is not reattempted. You must retain the same PersonalCallbackReattemptNoRingBack registry value in both Campaign Manager and Dialer Registry settings. If this registry setting is changed, the ICM Logger must be restarted before the new values take effect. |
| Note | Ensure the PersonalCallbackReattempt registry is set to 1 to get the expected behavior. If PersonalCallbackReattempt is set
                                                            to 0, NoRingback is not reattempted. You must retain the same PersonalCallbackReattemptNoRingBack registry value in both Campaign Manager and Dialer Registry settings. If this registry setting is changed, the ICM Logger must be restarted before the new values take effect. |
| PersonalCallbackSaturdayAllowed (Campaign Manager only) | 0 | Indicates whether personal callbacks are allowed on Saturdays. 0: Personal callbacks are not allowed on Saturdays and are scheduled for the next allowable day. For example, a personal callback
                                                which fails to reach the customer on a Friday is rescheduled for the following Monday. 1: Personal callbacks are allowed on Saturdays. |
| PersonalCallbackSundayAllowed (Campaign Manager only) | 0 | Indicates whether personal callbacks are allowed on Sundays. 0: Personal callbacks are not allowed on Sundays and are scheduled for the next allowable day. For example, a personal callback
                                                which fails to reach the customer on a Friday or Saturday is rescheduled for the following Monday. 1: Personal callbacks are allowed on Sundays. |
| PersonalCallbackTimeToCheckForRecords (Campaign Manager only) | Minimum value is 1; maximum value is 30; default is 1 minute | The interval time, in minutes, at which the Outbound Option Dialer checks the Campaign Manager for personal callback records. |
| PersonalCallbackTimeToRetryBusy (Campaign Manager only) | Minimum value is 1; maximum value is 10; default is 1 minute | Sets the amount of time, in minutes, that the Outbound Option Dialer waits before retrying a personal callback when the customer’s
                                          phone is busy. |
| PersonalCallbackTimeToRetryNoAnswer (Campaign Manager only) | Minimum value is 5; maximum value is 60; default is 20 minutes | Sets the amount of time, in minutes, that the Outbound Option Dialer waits before retrying a personal callback when the customer
                                          does not answer the phone. |
| PersonalCallbackTimeToRetryReservation (Campaign Manager only) | Minimum value is 1; maximum value is 10; default is 1 minute | Sets the amount of time, in minutes, that the Outbound Option Dialer waits before retrying to reserve an agent if the agent
                                          is not available. |
| ReplicationExpirationThreshold | 600 seconds | Controls the expiration threshold for replication. If the data is not replicated within this threshold, an EMS Report Event is signaled periodically until the condition has
                                          improved. |
| RescheduleCallbacks (Campaign Manager only) | 1 | Boolean value. Controls how to handle contacts that were requested to be called back at a particular time, but were left out in Pending call
                                          status 'P', for whatever reason. 0: Pending dialing records are not rescheduled or purged. 1: Pending dialing records are scheduled for retry at the next valid time. |
| SQLServer (Campaign Manager and Outbound Option Import) | null | Not used. |
| TCD_DBComputerName_A | "" | Not used. |
| TCD_DBComputerName_B | "" | Not used. |
| TCD_DBDatabaseName_A | "" | Not used. |
| TCD_DBDatabaseName_B | "" | Not used. |
| TCDCopyPendingEnabled | 0 | Not used. |
| TCDEnabled | 0 | Not used. |
| TCDKeepDays | 30 | Not used. |
| TimeToResetDailyStats (Campaign Manager only) | 30 minutes after midnight ( "00:30" ) | Specifies the time of day (in 24-hour format: hh:mm) when the real-time statistics for DialerRealTime and CampaignQueryRealTime
                                          are reset. |
| UnknownCallStatusResetTime (Campaign Manager only) | 60 minutes | The interval time, in minutes, at which the Campaign Manager resets the contact records in Unknown status to Pending status
                                          (available for reuse). Note Contact records are marked Unknown if they are in the Active state when the Campaign Manager is initialized or if the Outbound
                                                   Option Dialer dialing those (Active) records disconnects from the Campaign Manager due to network or Outbound Option Dialer
                                                   failure. | Note | Contact records are marked Unknown if they are in the Active state when the Campaign Manager is initialized or if the Outbound
                                                   Option Dialer dialing those (Active) records disconnects from the Campaign Manager due to network or Outbound Option Dialer
                                                   failure. |
| Note | Contact records are marked Unknown if they are in the Active state when the Campaign Manager is initialized or if the Outbound
                                                   Option Dialer dialing those (Active) records disconnects from the Campaign Manager due to network or Outbound Option Dialer
                                                   failure. |
| EnableMaxAttemptsPerNumber | 0 | Enable the maximum attempts per phone number in a record. For example: If every phone number has to be dialed only once then configure MaxAttempts to 1 and set EnableMaxAttemptsPerNumber to 1. |
| BAReplDriveFreeSpaceThreshold | 15 Seconds | Represents the percentage of free Logger drive space allowed before outbound option replication stops and the databases are
                                          no longer in sync. |
| ReplicationFileSwitchDuration | 15 Seconds | Represents the amount of time before temporary files are renamed to replication files. This registry also provides information
                                          to the standby Campaign Manager if it were to observe a temporary file remaining open for longer than this duration. |

| Note | The call status values can optionally be delimited using a comma, a hyphen, a semi-colon, or a colon. |
|---|---|

| Note | Time zones are selected based on the data in the Region_Prefix database. When contacts are imported, the phone number is assigned
                                                   a time zone based on the information in the region prefix table. Each prefix has settings for the time zone and daylight savings
                                                   observation. If the prefix of the contact number does not match any of the prefixes listed in the region prefix table, then
                                                   the contact number is assigned the time zone listed in the campaign configuration tool Call Target Tab. |
|---|---|

| Note | If this registry setting changes, the ICM Logger must be restarted before the new values take effect. Alternatively, restart
                                                   the Outbound Option Import process by closing its console window. |
|---|---|

| Note | If this registry setting changes, the ICM Logger must be restarted before the new values take effect. Alternatively, restart
                                                   the Outbound Option Import process by closing its console window. |
|---|---|

| Note | The call status values can optionally be delimited using a comma, a hyphen, a semi-colon, or a colon. |
|---|---|

| Note | Ensure you retain the same PersonalCallbackReattempt registry value in both Campaign Manager and Dialer Registry settings. If this registry setting is changed, the ICM Logger must be restarted before the new values take effect. |
|---|---|

| Note | Ensure the PersonalCallbackReattempt registry is set to 1 to get the expected behavior. If PersonalCallbackReattempt is set
                                                            to 0, NoRingback is not reattempted. You must retain the same PersonalCallbackReattemptNoRingBack registry value in both Campaign Manager and Dialer Registry settings. If this registry setting is changed, the ICM Logger must be restarted before the new values take effect. |
|---|---|

| Note | Contact records are marked Unknown if they are in the Active state when the Campaign Manager is initialized or if the Outbound
                                                   Option Dialer dialing those (Active) records disconnects from the Campaign Manager due to network or Outbound Option Dialer
                                                   failure. |
|---|---|

| Registry
                                          						Setting | Default
                                          						Setting | Description |
|---|---|---|
| AnswerTransferUsingAgentPhone | 1 | When enabled (1), the dialer automatically answers customer calls transferred to agent phones. |
| AutoAnswerCall | 1 | This registry key is not created until the process starts up. It controls whether the Dialer auto-answers the call or not.
                                          The guideline is to disable this and uses the auto-answer in Unified CM, if you want zip tone. |
| Ca_cnosig | 20 seconds | Amount of
                                          						silence before no ringback is returned, in seconds. If ringback is not detected
                                          						within this time limit, the call is dropped. Note Changes
                                                   						made to this setting take effect after the Outbound Option Dialer is cycled. | Note | Changes
                                                   						made to this setting take effect after the Outbound Option Dialer is cycled. |
| Note | Changes
                                                   						made to this setting take effect after the Outbound Option Dialer is cycled. |
| CancelDialingCalls | 0 | Controls behavior when started call attempts can be canceled once all agents are occupied and abandon to IVR is not configured.
                                          Setting to 0 never cancels calls after they have been started. Setting to 1 always cancels calls after they have been started
                                          once no agents are available. A value of 100 cancels all ringing calls that are less than 100 milliseconds after the dialing
                                          was started (that is,  the line went off hook. Note When CancelDialingCalls = 0, it cancels calls not confirmed to reach the customer (which means SIP progress messages of 180,
                                                            181, 182, or 183 not yet received). The abandon to IVR configuration is ignored for canceling in this case. When CancelDialingCalls > 0, and abandon to IVR configuration is enabled, the only calls that have not yet started while
                                                            waiting in the Port Throttle queue, are canceled. | Note | When CancelDialingCalls = 0, it cancels calls not confirmed to reach the customer (which means SIP progress messages of 180,
                                                            181, 182, or 183 not yet received). The abandon to IVR configuration is ignored for canceling in this case. When CancelDialingCalls > 0, and abandon to IVR configuration is enabled, the only calls that have not yet started while
                                                            waiting in the Port Throttle queue, are canceled. |
| Note | When CancelDialingCalls = 0, it cancels calls not confirmed to reach the customer (which means SIP progress messages of 180,
                                                            181, 182, or 183 not yet received). The abandon to IVR configuration is ignored for canceling in this case. When CancelDialingCalls > 0, and abandon to IVR configuration is enabled, the only calls that have not yet started while
                                                            waiting in the Port Throttle queue, are canceled. |
| CaptureEnabled | 0 | When set
                                          						to 0, packet capturing is disabled; when set to 1, packet capturing is enabled. |
| CaptureOptions | -i 2 -tt
                                          						-C 20 -s 0 -W 20 -w DialerCapture | Options
                                          						associated with packet capture: -i
                                                							 <ifname>: Interface name to capture on -tt :
                                                							 Print an unformatted time stamp on each dump line. -w <filename>: Capture directly to file in pcap format, the file can be opened with Wireshark. -C
                                                							 <file_size>: The maximum size of a capture file. The units of file_size
                                                							 are millions of bytes (1,000,000 bytes, not 1,048,576 bytes). -W
                                                							 <filecount>: The number of files created. The capture files are
                                                							 overwritten from the beginning, thus creating a rotating buffer. Capture files
                                                							 after the first capture file have the name specified with the -w flag, with a
                                                							 number after it, starting at 1 and continuing upward. -s : Snarf snaplen bytes of data from each packet rather than the default of 68 Setting snaplen to 0 means use the required length to catch whole packets. |
| CaptureType | 1 | When set
                                          						to 1, capture SIP packets only. When set to 2, capture the entire data payload
                                          						on the Dialer host machine. |
| CCMTransferDelay | 0 | Not used. |
| CMServerA | NA | The
                                          						hostname or IP address of the Campaign Manager on Side A. |
| CMServerB | NA | The
                                          						hostname or IP address of the Campaign Manager on Side B. |
| ConsecutiveNoDialToneEvents | 3 | Not used. |
| CPAActiveThreshold | 32 | Signal
                                          						must exceed CPAActiveThreshold*noiseThreshold to be considered active. For
                                          						example, 32 is 10 * log(32) = 15 dB. |
| CPAJitterBufferDelay | 150 | The
                                          						jitter buffer delay (in mS). |
| CPAMaxNoiseFloor | 10000 | Maximum
                                          						Noise floor possible. Used to restrict noise floor measurement. |
| CPAMinNoiseFloor | 1000 | Minimum
                                          						Noise floor possible. Used to restrict noise floor measurement. |
| CPAMaxToneSTDEV | 0.600000 | Standard
                                          						deviation of zero crossing rate per block. Values lower than this and
                                          						CPAMaxEnergySTDev are considered tones. |
| CPANoiseThresholdPeriod | 100ms | The amount of time to wait for the initial voice. The CPAAnalysisPeriod starts once the system detects speech. |
| CPARecordWaveFile | 0 (off) | Setting
                                          						this entry to 1 enables recording of the CPA period to assist in
                                          						troubleshooting. The key must be added to be enabled. |
| CTIServerA | "" | The
                                          						machine name where CTI Server-Side A resides. |
| CTIServerB | "" | The
                                          						machine name where CTI Server-Side B resides. |
| CTIServerPortA | "" | The TCP
                                          						port number where CTI Server-Side A listens. |
| CTIServerPortB | "" | The TCP
                                          						port number where CTI Server-Side B listens. |
| CustRecReadyRequestToServer | 30
                                          						seconds | Describes the polling interval when the campaign is enabled,
                                          						agents are available, and the Dialer needs more records from the Campaign
                                          						Manager. The first request is sent when the Dialer notices that it is low on
                                          						records. Subsequent requests are sent after the TimeToWaitForRecord times out,
                                          						based on this polling interval until more records are received. |
| DirectAgentDial | 0 | Not
                                          						used. |
| DisableIPCPA | 0 | Disables
                                          						call progress analysis for this Dialer. |
| EMTHeartBeat | 500
                                          						milliseconds | Dialer
                                          						sends a heartbeat message to the Campaign Manager every n millisecond to
                                          						indicate that it is still alive. |
| EnhancedPredictiveDialing | N/A ( Manual Registry) | If there is no registry value or if the registry value is set as
                                          									zero, Unified CCE uses the existing predictive algorithm. If the registry value is set to 1, Unified CCE uses the Enhanced
                                          									Predictive Algorithm. Note Enable this registry only when there is a low hit rate with long idle agent times. This change adjusts the dialing rate more
                                                      aggressively, so it may not respect the configured abandon limit. | Note | Enable this registry only when there is a low hit rate with long idle agent times. This change adjusts the dialing rate more
                                                      aggressively, so it may not respect the configured abandon limit. |
| Note | Enable this registry only when there is a low hit rate with long idle agent times. This change adjusts the dialing rate more
                                                      aggressively, so it may not respect the configured abandon limit. |
| EnableAutoAcceptFeature | 0 | Generally, an agent must respond to the Preview dialog when a reservation call is placed. With the implementation of the Auto
                                          Accept feature, the Outbound Option Dialer implements the Auto-Accept functionality. It causes the Dialer to Auto-ACCEPT the
                                          preview call in n seconds if the agent fails to respond to the preview dialog. The same applies to Personal Callback calls. This
                                          						feature is disabled by default and the registry key must be set to one (1) to
                                          						enable the feature. The
                                          						PreviewReservationTimeout registry key is used to configure the auto-accept
                                          						timer value. |
| EnableHeartbeat | 1
                                          						(enabled) | EnableHeartbeat registry is used to enable heartbeats on the
                                          						dialer. When this flag is enabled, the dialer sends heartbeats (SIP OPTIONS
                                          						request message) to the SIP server - Proxy or Gateway. If
                                          						there is no response from the SIP server, the dialer marks itself as not ready
                                          						and inform the same to the campaign manager. If this
                                          						registry is disabled, there is no indication if the SIP server goes down. |
| HBInterval | 5
                                          						seconds | The time
                                          						between heartbeats. |
| HBNumTries | 1 | The
                                          						number of times a timeout occurs before the SIP Dialer identifies the SIP
                                          						Gateway or SIP Proxy as down. |
| LongDistancePrefix | "1" | Not
                                          						used. |
| MaxAllRecordFiles | 500,000,000 | The
                                          						maximum recording file size (in bytes) per SIP Dialer. |
| MaxMediaTerminationSessions | 200 | The
                                          						maximum number of media termination sessions per SIP Dialer if recording is
                                          						enabled in the Campaign configuration. |
| MaxPortCapacityReachedCount | 30 | The number of failed attempts to reserve a port before the Dialer logs a
                                          									warning. The message states that the Dialer has reached maximum port
                                          									capacity. The counter resets to 0 after logging the message. |
| MaxPurgeRecordFiles | 100,000,000 | The
                                          						maximum recording file size (in bytes) that the SIP Dialer deletes when the
                                          						total recording file size, MaxAllRecordFiles, is reached. |
| MaxRecordingSessions | 100 | The
                                          						maximum number of recording sessions per SIP Dialer if recording is enabled in
                                          						the Campaign configuration. |
| MRPort | 38001 | The
                                          						connection port for the MR PIM. |
| OptimizeAgentAvailability | 0 | This
                                          						registry entry is reserved for future use. Leave the value of this parameter at
                                          						0. |
| OverrideNetworkTones | 0 | Not
                                          						used. |
| PersonalCallbackDN | "PersonalCallback" | Contains
                                          						a script name that the MR PIM receives as a dialed number when personal
                                          						callback calls require to reserve agents. |
| PersonalCallbackReattempt | 1 | You can leverage the capabilities of this registry by installing the Unified CCE 15.0(1) ICM15.0.1_ES202508 . To control the Dialer from attempting to retry the unreachable outbound personal callback calls, set any one of the following
                                          value to the PersonalCallbackReattempt registry: Set to 1 (default): The dialer immediately reattempts the unreachable personal callback calls or sends the record back to Campaign
                                                Manager for rescheduling. Set to 0 : Disables redialing of personal callback records that were unreachable, with call results 2, 4, 6, 8, 9, or 16. These records
                                                are sent back to Campaign Manager and marked as closed. Note Ensure you retain the same PersonalCallbackReattempt registry value in both Campaign Manager and Dialer Registry settings. If this registry setting is changed, the Dialer must be restarted before the new values take effect. | Note | Ensure you retain the same PersonalCallbackReattempt registry value in both Campaign Manager and Dialer Registry settings. If this registry setting is changed, the Dialer must be restarted before the new values take effect. |
| Note | Ensure you retain the same PersonalCallbackReattempt registry value in both Campaign Manager and Dialer Registry settings. If this registry setting is changed, the Dialer must be restarted before the new values take effect. |
| PersonalCallbackReattemptNoRingBack | 1 | Indicates whether the Dialer must retry or redial outbound personal callbacks in case of the following scenarios: Customer number is switched off or not reachable. Customer disconnects the call. Customer on a different call and the call is being dropped. Set any one of the following value to the PersonalCallbackReattemptNoRingBack registry: Set to 1 (default): Dialer retries the call every one minute until the CallbackTimeLimit is reached. Set to 0 : Disables the Dialer from redialing personal callbacks within the duration set in CallbackTimeLimit, set the registry key
                                                value to 0. Note Ensure the PersonalCallbackReattempt registry is set to 1 to get the expected behavior. If PersonalCallbackReattempt is set
                                                            to 0, NoRingback is not reattempted. You must retain the same PersonalCallbackReattemptNoRingBack registry value in both Campaign Manager and Dialer Registry settings. If this registry setting is changed, the Dialer must be restarted before the new values take effect. | Note | Ensure the PersonalCallbackReattempt registry is set to 1 to get the expected behavior. If PersonalCallbackReattempt is set
                                                            to 0, NoRingback is not reattempted. You must retain the same PersonalCallbackReattemptNoRingBack registry value in both Campaign Manager and Dialer Registry settings. If this registry setting is changed, the Dialer must be restarted before the new values take effect. |
| Note | Ensure the PersonalCallbackReattempt registry is set to 1 to get the expected behavior. If PersonalCallbackReattempt is set
                                                            to 0, NoRingback is not reattempted. You must retain the same PersonalCallbackReattemptNoRingBack registry value in both Campaign Manager and Dialer Registry settings. If this registry setting is changed, the Dialer must be restarted before the new values take effect. |
| PreviewReservationTimeout | 600 | Number of seconds to wait before canceling a preview agent’s reservation call. This key is automatically created when the
                                          Dialer starts. If a preview agent does not accept or reject a call within this time period, the agent’s reservation call is dropped and the record is marked as rejected. Note This
                                                   						registry setting also works with Direct Preview mode, and applies to the
                                                   						regular callback calls in both Preview mode and Direct Preview mode. | Note | This
                                                   						registry setting also works with Direct Preview mode, and applies to the
                                                   						regular callback calls in both Preview mode and Direct Preview mode. |
| Note | This
                                                   						registry setting also works with Direct Preview mode, and applies to the
                                                   						regular callback calls in both Preview mode and Direct Preview mode. |
| ReclassifyTransferFailures | 0 | When set to 1, answering machine calls that
                                          									are abandoned due to lack of agent or IVR resources are not
                                          									counted as abandoned voice calls. They will be counted as answering machine
                                          									calls. This registry is also enabled by default on fresh
                                          									installs, and disabled in upgraded systems. |
| RTPortFeedDisable | 1 | When
                                          						set, real-time dialer port messages are disabled for this dialer. Enabling the
                                          						Real-Time Port Feed by setting to 0 causes the dialpr01 report to populate, but
                                          						this can cause impacts to the Outbound Campaign in delays in getting records. |
| SetAgentsReadyOnResvDrop | 1 | When set
                                          						to 1, the Outbound Option Dialer automatically sets manual IN agents to the
                                          						Ready state, if the reservation call is dropped due to any reason other than
                                          						transfer of a live customer call. If this value is set to 0, then manual IN agents
                                          									assume the After Call Work (ACW) state at the end of each reservation call
                                          									and manually become ready to receive another call. Note SetAgentsReadyOnResvDrop is applicable only for TDM dialer. | Note | SetAgentsReadyOnResvDrop is applicable only for TDM dialer. |
| Note | SetAgentsReadyOnResvDrop is applicable only for TDM dialer. |
| SIPDialerPortBaseNumber | 58800 | This key specifies the port
                                       					 number used by the dialer to communicate with the SIP server. This registry is
                                       					 created by default when the dialer machine is installed. |
| SIPServerAddress | NULL | The IP
                                          						address or DNS hostname of the SIP Proxy or SIP Gateway that this Dialer
                                          						connects to, as specified during setup. |
| SIPServerPortNumber | 5060 | The port
                                          						number that the SIP Dialer uses to communicate with the server. |
| SIPServerTransportType | 1 | The transport type used to communicate with the gateway/ CCCSP . A
                                          						setting of 1 indicates that the transport type is UDP, and a setting of 2
                                          						indicates that the transport type is TCP. Currently, only UDP is supported. Note Incoming transport time accepts TCP and UDP. The trunk accepts traffic from the Gateway in TCP or UDP. | Note | Incoming transport time accepts TCP and UDP. The trunk accepts traffic from the Gateway in TCP or UDP. |
| Note | Incoming transport time accepts TCP and UDP. The trunk accepts traffic from the Gateway in TCP or UDP. |
| SkillGroupQueryDelay | 1 second | The
                                          						amount of time, in seconds, to wait between CTI Server skill group query
                                          						requests. |
| SwitchPrefix | "" | Dialing
                                          						prefix prepended to every phone number; for example, this entry could be used
                                          						to dial an outside line access number, such as 9. |
| TalkTimeAvg | 60
                                          						seconds | The
                                          						amount of time an average customer call takes. (Seed value for talk time, which
                                          						is adjusted as a moving average as the system is used.) |
| TestNumberMaxDigits | 5 | Maximum
                                          						length for test phone numbers. Test phone numbers do not receive any prefixes
                                          						added by the Dialer. |
| TFTPServer | "" | The name of the Unified CM TFTP server. This
                                          									server is usually located on the Publisher Unified CM. |
| TimeToCTIBeginCall | 7
                                          						seconds | The amount of time, in seconds, to wait for the CTI begin call event before canceling the call. |
| TimeToFreeStuckCall | 7200
                                          						seconds, which is 2 hours | The
                                          						amount of time, in seconds, before a customer call is declared stuck and
                                          						dropped. |
| TimeToFreeStuckPort | 7200
                                          						seconds, which is 2 hours | The
                                          						amount of time, in seconds, to wait before releasing a stuck port. |
| TimeToHoldCustomer | 1 second | The
                                          						amount of time, in seconds, to wait before abandoning a customer call due to
                                          						lack of agents. If abandon to IVR is enabled for campaigns, this value should
                                          						be set to 0 to reduce transfer delays. |
| TimeToReserve | 10
                                          						seconds | The
                                          						amount of time, in seconds, to wait before dropping a reservation call. |
| TimeToRetryCustomerRequest | 30
                                          						seconds | The
                                          						amount of time, in seconds, to wait before retrying a close customer record
                                          						request to the Campaign Manager. When the
                                          						Outbound Option Dialer finishes with a customer record, it sends a close
                                          						customer record request message to the Campaign Manager. If this message is not
                                          						sent, the Outbound Option Dialer retries the call based on the configured
                                          						timeout. |
| TimeToRingCustomer | 8
                                          						seconds | The
                                          						amount of time, in seconds, each customer ring takes. For example, if this
                                          						entry is set to 8 and the no-answer configuration in the campaign is set to 3
                                          						rings, then the Dialer classifies the call as no-answer within 3*8 (24)
                                          						seconds. |
| TimeToTransfer | 7
                                          						seconds | The
                                          						amount of time, in seconds, to wait before dropping a call being transferred. |
| TimeToWaitForCTIResp | 3
                                          						seconds | The
                                          						amount of time, in seconds, to wait for the CTI Server to respond to a request
                                          						before dropping the call. |
| TimeToWaitForIPDialTone | 10 seconds | The amount of time, in seconds, to wait for the
                                          									Unified CM dial tone. |
| TimeToWaitForMRIResponse | 600
                                          						seconds (10 minutes) | The
                                          						amount of time, in seconds, to wait for the MR PIM to respond to a new task
                                          						request before canceling the request. |
| TimeToWaitForRecord | 5
                                          						seconds | The
                                          						amount of time, in seconds, to wait for customer records from the Campaign
                                          						Manager before declaring the skill group disabled. Once a
                                          						skill group has been disabled, the Dialer begins polling the Campaign Manager
                                          						every <CustRecReadyRequestToServer> second for additional records. |

| Note | Changes
                                                   						made to this setting take effect after the Outbound Option Dialer is cycled. |
|---|---|

| Note | When CancelDialingCalls = 0, it cancels calls not confirmed to reach the customer (which means SIP progress messages of 180,
                                                            181, 182, or 183 not yet received). The abandon to IVR configuration is ignored for canceling in this case. When CancelDialingCalls > 0, and abandon to IVR configuration is enabled, the only calls that have not yet started while
                                                            waiting in the Port Throttle queue, are canceled. |
|---|---|

| Note | Enable this registry only when there is a low hit rate with long idle agent times. This change adjusts the dialing rate more
                                                      aggressively, so it may not respect the configured abandon limit. |
|---|---|

| Note | Ensure you retain the same PersonalCallbackReattempt registry value in both Campaign Manager and Dialer Registry settings. If this registry setting is changed, the Dialer must be restarted before the new values take effect. |
|---|---|

| Note | Ensure the PersonalCallbackReattempt registry is set to 1 to get the expected behavior. If PersonalCallbackReattempt is set
                                                            to 0, NoRingback is not reattempted. You must retain the same PersonalCallbackReattemptNoRingBack registry value in both Campaign Manager and Dialer Registry settings. If this registry setting is changed, the Dialer must be restarted before the new values take effect. |
|---|---|

| Note | This
                                                   						registry setting also works with Direct Preview mode, and applies to the
                                                   						regular callback calls in both Preview mode and Direct Preview mode. |
|---|---|

| Note | SetAgentsReadyOnResvDrop is applicable only for TDM dialer. |
|---|---|

| Note | Incoming transport time accepts TCP and UDP. The trunk accepts traffic from the Gateway in TCP or UDP. |
|---|---|