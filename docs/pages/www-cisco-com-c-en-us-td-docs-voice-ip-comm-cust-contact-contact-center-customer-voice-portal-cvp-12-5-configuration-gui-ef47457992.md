---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-customer-voice-portal-cvp-12-5-configuration-gui-ef47457992
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/customer_voice_portal/cvp_12_5/configuration/guide/ccvp_b_1251-reportingguide-cvp/ccvp_b_1251-reportingguide-cvp_chapter_010.html
retrieved_at: 2026-08-21T03:06:33.208088+00:00
---

Reporting Guide for Cisco Unified Customer Voice Portal, Release 12.5(1)

# Reporting Guide for Cisco Unified Customer Voice Portal, Release 12.5(1)

Updated: January 31, 2020

Chapter: Cisco Unified Customer Voice Portal Templates for Cisco Unified Intelligence Center

## Chapter: Cisco Unified Customer Voice Portal Templates for Cisco Unified Intelligence Center

# Cisco Unified Customer Voice Portal Templates for Cisco Unified Intelligence Center

This chapter presents the Cisco-designed reports for Cisco Unified Customer Voice Portal (Unified CVP). These
                        		templates are available to you once you import them and set their data source.

To become familiar with developing additional custom reports, run one
                        		of the stock reports, perform a Save As operation, and modify the Save As
                        		report.

This chapter contains the following topics:

## Application Summary Reports (15, Daily, and Weekly)

Unified CVP has three Application Summary Reports: Application Summary 15,
                              		  Application Summary Daily, and Application Summary Weekly.

These reports are useful for Dominant Path Analysis. They display which elements of the voice applications are being run
                              and the number of times they are run.

The three reports display the same data but aggregate the data for
                              		  different time periods. See Summary / Aggregate Tables

Fields in this report are populated from these tables:

Fields in this report:

Date and Time

The date and time when the period of data collection began. From the dbdatetime field of the appropriate Application
                                    				Summary table - 15, Daily, or Weekly.

Application Name

The name of the voice application. From the AppName field of the
                                    				appropriate Application Summary table - 15, Daily, or Weekly.

Source Application Name

The name of the source application that transferred the element.
                                    				This field typically shows null . From The SourceAppName field of the appropriate Application
                                    				Summary table - 15, Daily, or Weekly.

Element Name

The name of the element. From the ElementName field of of the
                                    				appropriate Application Summary table - 15, Daily, or Weekly.

Element Type

The element type. From the ElementTypeID field of the appropriate
                                    				Application Summary table - 15, Daily, or Weekly.

Exit State

The exit state of the element. From the ExitState field of the
                                    				appropriate Application Summary table - 15, Daily, or Weekly.

Result

Indicates how an element ended. From result, where ResultID =
                                    				ResultRef.resulttypeID.

Count

The number of calls to run a particular application. From the Count field of the appropriate Application Summary table -
                                    15, Daily, or Weekly.

Average Elapsed Time

The average number of seconds a call was in a particular element.
                                    				Calculated by subtracting the start time from the end time over all the
                                    				elements within the grouping.

## Call Report

The Call report shows the first 500 calls, starting at the date/time
                              		  you select in the Basic Filter.

For this report, you can take advantage of the Absolute Date feature of the Basic Filter and filter to a narrow range, for
                              example, to a one-minute time interval:

Fields in this report are populated from these tables:

Call

CallTypeRef

SubsystemTypeRef

Fields in this report:

Call Guid

The Global Unique ID (GUID) of a call. From Call.CallGuid.

ANI

The Automatic Number Identification (ANI) of the caller sent by the
                                    				telephony provider.

ANI does not need to be configured, and can therefore be a null
                                    				field. From Call.ANI.

DNIS

The Dialed Number Identification Service (DNIS) sent by the telephony
                                    				provider. From Call.DNIS.

UID

The external User Identifier (UID) of the originating caller, sent by
                                    				telephony provider. From Call.UID.

UUI

The User-To-User Information (UUI) of the originating caller, sent by
                                    				telephony provider. From Call.UUI.

IIDigits

The ANI II Digits of the originating caller, sent by the
                                    				telephony provider. From Call.IIDigits.

Sub Subsystem Type

The type of Unified CVP Service used for the call, such as SIP,
                                    				IVR,VXML, where Call.SubSystemTypeID = SubsystemTypeRef.SubsystemTypeRefID.

See SubsystemTypeRef for the list of sybsystem types.

Call Type

The type of call, where Call.CallTypeID = CallTypeRef.CallTypeID.
                                    				See CallTypeRef for the list of call types.

Call Started

The time when the call started. From Call.StartDateTime.

Call Ended

The time when the call ended. From Call.EndDateTime.

Time Persisted to Database

This is the timestamp when data is written to the database. If
                                    				the reporting server is in Boston, and the Callserver is in San Diego, then
                                    				calls placed in San Diego at 1 PM  have a  Coordinated Universal Time (UTC) startdatetime ( + 7 hours),
                                    				and the dbdatetime for this call is 4 PM (Boston time).

Time Zone Offset from UTC (Minutes)

The offset in minutes of the local timezone from the UTC timezone.
                                    				From Call.LocalTimeZoneOffset.

If the reporting server is in Boston, and the Callserver is in
                                    				San Diego, then calls placed in San Diego at 1 PM have a UTC startdatetime
                                    				( + 7 hours), and the dbdatetime for this call is 4 PM (Boston time).
                                    				The timezone offset is 240 minutes.

Applications Visited

The number of applications visited during the life of the call.
                                    				From Call.NumAppVisited.

Errors

The number of errors that occurred during the call. From
                                    				Call.NumError.

On Hold

The number of times the call was on hold due to unavailable
                                    				ports. From Call.NumOnHold.

Opted Out

This will always show 0. From Call.NumOptOut, deprecated field.

Timed Out

The number of times the call timed out because it exceeded a
                                    				processing time. From Call.NumTimedOut.

Transferred

The number of times the call was transferred out to an agent or
                                    				to a Voice Response Unit (VRU) leg. The VRU leg is the leg that talks to VoiceXML Gateways.

## Call Detail Report

This report displays robust detail for calls according to the filters
                              		  you set. This report is based on a Stored Procedure and uses the Filter Page for Stored Procedure and Anonymous Block Reports .

Note that this is a wide report. You might need to set the printer to
                              		  Landscape mode, use legal-sized paper, or Export to Excel.

Fields in this report include data from these tables:

Fields in this report are:

Call Start Date

The time when the call started. From Call.StartDateTime.

End Date and Time

The time when the call ended. From Call.EndDateTime.

Local Timezone Offset

The offset in minutes of the local timezone from UTC timezone.
                                    				From Call.LocalTimeZoneOffset.

If the reporting server is in Boston, and the Callserver is in
                                    				San Diego, then calls placed in San Diego at 1 PM will have a UTC startdatetime
                                    				( + 7 hours), and the dbdatetime for this call will be 4 PM (Boston time).
                                    				The timezone offset is 240 minutes.

Call Guid

The Global Unique ID (GUID) of a call. From Call.CallGuid.

Call Type

The type of call, where Call.CallTypeID = CallTypeRef.CallTypeID.

ANI

The Automatic Number Identification  (ANI) of the caller sent by the
                                    				telephony provider. From Call.CallGuid.

ANI does not need to be configured, and can therefore be a null
                                    				field. From Call.ANI.

DNIS

The Dialed Number Identification Service (DNIS) sent by the telephony
                                    				provider. From Call.DNIS.

IIDigits

The ANI II Digits of the originating caller, sent by the
                                    				telephony provider. From Call.IIDigits.

UID

The external User Identifier (UID) of the originating caller, sent by
                                    				telephony provider. From Call.UID.

UUI

The User-To-User Information (UUI) of the originating caller, sent by
                                    				telephony provider. From Call.UUI.

Number of Applications Visited

The number of applications visited during the life of the call.
                                    				From Call.NumAppVisited.

Number of Interactions

The number of applications visited during the life of the call.
                                    				From VXMLElement.NumberofInteractions.

Number of Errors

The number of errors that occurred during the call. From
                                    				Call.NumError.

Number of Times On Hold

The number of times the call was on hold due to unavailable
                                    				ports. From Call.NumOnHold.

Number of Timeouts

The number of times the call timed out because it exceeded a
                                    				processing time. From Call.NumTimedOut.

Total Number of Transfers

The number of times the call was transferred out to an agent or
                                    				to a VRU leg. ( VRU leg is the leg that talks to VoiceXML Gateways.) From
                                    				Call.TotalTransfer.

Event Date and Time

The date and time of the event. From CallEvent.EventDateTime.

Event Type

The name of the event type, from Callback.eventtypeID, where
                                    				Callback.eventtypeID = EventTypeRef.eventtypeid.

Subsystem

The Subsystem Name. From SubsystemTypeRef.Subsystem.

Subsystem Type ID

The ID of the Unified CVP Service used for the call, such as "2" for
                                    				VXML. From SubsystemTypeRef.SubsystemTypeRefID.

CallLegId

This is an ID assigned by the service. From CallEvent.CallLegID.

Cause

The reason that the call event was generated. From
                                    				CallEvent.CauseID.

Result

Indicates how an element ended. From result, where ResultID =
                                    				ResultRef.resulttypeID.

Media Filename

This field is always null in this release. From CallEvent.MediaFileName.

Transfer Label

The destination to which Unified CVP transfers the call. From
                                    				CallEvent.TransferLabel.

Transfer Type

The unique id of the transfer type. From
                                    				CallEvent.TransferTypeID.

Messagebus

The name of the Call Server (its message adapter name) with which
                                    				the Call Event is associated. From CallEvent.MessageBusName.

RouterCallKey

The Unified ICM router call key. From CallICMInfo.RouterCallKey.

RouterCallKeyDay

The Unified ICM router call key day. From
                                    				CallICMInfo.RouterCallKeyDay.

RouterCallKeySeqenceNumber

The Unified ICM router call key sequence number. From
                                    				CallICMInfo.RouterCallKeySequenceNumber.

Application Name

The name of the VXML application. From VXMLSession.AppName.

Enter Date and Time

The  date and time when the element was entered. From
                                    				VXMLElement.EnterDateTime.

Exit Date and Time

The date and time when the element was exited. From
                                    				VXML.ExitDateTime.

Duration

The length of the session. From VXMLSession.Duration.

Element Name

The name of the element. From VXMLElement.ElementName.

Element Type

The type of element. From VXMLElement.ElementTypeID.

Exit State

The exit state of the element. From VXMLElement.ExitState.

Session ID

The unique id of a VXML application session. From
                                    				VXMLSession.SessionID.

Session Name

The name of the session assigned by VXML Server. From
                                    				VXMLSession.SessionName.

Source Application Name

The name of the application that transferred to this one. From
                                    				VXMLSession.SourceAppName.

VXML Cause

The reason that the application visit ended. From
                                    				VXMLSession.CauseID.

VXML End Date and Time

The end date and time of the session. From
                                    				VXMLSession.EndDateTime.

VXML Event Type

The mechanism used to end the application visit. From
                                    				VXMLSession.EventTypeID.

VXML Start Date and Time

Date and time when session began. From VXMLSession.StartDateTime.

## Call Traffic Reports (15, Daily, and Weekly)

Unified CVP has three Call Traffic Reports: Call Traffic 15, Call Traffic
                              		  Daily, and Call Traffic Weekly.

These reports indicate the CallServer/VXML Server load during the
                              		  course of the day. Call center administrators can monitor peak call volume
                              		  times and monitor load levels on various call servers and VXML servers.

The three reports display the same data and aggregate the data for
                              		  different time periods. See Summary / Aggregate Tables

Fields in this report are populated from these tables:

Fields in this report:

Date and Time

The date and time of the call, from the start of the increment.
                                    				From the datetime field of the appropriate Call Traffic table (15, Daily, or
                                    				Weekly).

SubSystem Type

The type of Unified CVP Service used for the call, such as SIP,
                                    				IVR,VXML, where the Call Summary table SubSystemTypeID =
                                    				SubsystemTypeRef.SubsystemTypeRefID.

See SubSystemTypeRef Table for the list of subsystem types.

Call Type

The type of call, where the Call Summary Table CallTypeID =
                                    				CallTypeRef.CallTypeID. See CallTypeRef Table for the list of call types.

Number of Calls

Total number of calls in this period. From the NumCalls field of
                                    				the appropriate Call Traffic table (15, Daily, or Weekly).

Average Call Length

The average call length. From the AvgCallLength field of the
                                    				appropriate Call Traffic table (15, Daily, or Weekly).

Applications Visited

The total number of applications visited in this period. From the
                                    				TotalAppVisited field of the appropriate Call Traffic table (15, Daily, or
                                    				Weekly).

Errors

The total number of errors in this period. From the TotalError
                                    				field of the appropriate Call Traffic table (15, Daily, or Weekly).

On Hold

The total number of times that calls were placed on hold in this
                                    				period. From the TotalOnHold field of the appropriate Call Traffic table (15,
                                    				Daily, or Weekly).

Opted Out

This field is deprecated. From the TotalOptOut field of the appropriate Call
                                    				Traffic table (15, Daily, or Weekly).

Timed Out

The total number of calls that timed out in this period. From the
                                    				TotalTimeOut field of the appropriate Call Traffic table (15, Daily, or
                                    				Weekly).

Transfers

The total number of calls were transferred in this period. From
                                    				the TotalTransfer field of the appropriate Call Traffic table (15, Daily, or
                                    				Weekly).

## Call Traffic
                        	 Charts

All three Call Traffic reports have chart views. To display the report data in the chart view, click the View drop-down and
                              select Columns.

Call Traffic charts
                              		  are columns that show the total Applications Visited, Errors, Number of Calls,
                              		  On Hold calls, Timed Out calls, and Transfers for the 15 minute, Daily, or
                              		  Weekly time interval.

## Current and
                        	 Historical Callback Reports

Unified CVP has two
                              		  callback reports: Pending Callbacks and Historical Callbacks.

They both pull data
                              		  from the CallBack
                                 			 table .

The Pending
                              		  Callbacks report takes data from calls that have occurred in the past 30
                              		  minutes. The Historical Callbacks report shows calls that occurred prior to 30
                              		  minutes ago.

The CallBack
                                 			 table is used to generate the report.

Fields in this report
                                 			 are:

ANI

This field
                                    				specifies the Automatic Number Identification (ANI) for the call.

Callguid

This field
                                    				specifies the call's unique identifier.

Cause

This field
                                    				specifies the cause of the event (no answer, no response etc).

CVP estimated
                                       				  wait time

This specifies
                                    				the estimated wait time by CVP.

Database
                                       				  date and time

This field
                                    				specifies the name of the queue.

Date and Time

This field
                                    				specifies the database update date and time.

Event date
                                       				  and time

This field
                                    				specifies the several events that are generated during a Courtesy Call Back
                                    				(CCB) call. It's the time of latest event.

Event
                                       				  type

This field
                                    				specifies the type of the latest event.

Gateway

The
                                    				identifier for the gateway, can be an IP address or a string identifier.

ICM
                                       				  estimated wait time

This field
                                    				specifies the estimated wait time for ICM to start sending to CVP (at the time
                                    				call comes into ICM scripts for the first time).

Location

This field
                                    				specifies the location that is assigned to the ingress gate way.

ICM
                                       				  estimated wait time

This field
                                    				specifies the estimated wait time for ICM to start sending to CVP (at the time
                                    				call comes into ICM scripts for the first time).

Number of
                                       				  attempts

This field
                                    				specifies the number of callback retries that have been made so far (in case
                                    				the callback was not accepted earlier).

Queue enter
                                       				  time

This field
                                    				specifies the time at which the call entered the queue.

Queue

This field
                                    				specifies the name of the queue.

Queue leave
                                       				  time

This field
                                    				specifies the time at which the call left the queue.

Queue
                                       				  status

This field
                                    				specifies the current call back status of the call.

Recording
                                       				  URL

This field
                                    				specifies the URL of the media file for caller's name.

Validation
                                       				  Status

This field
                                    				specifies whether each call that gets into reporting server gets validated for
                                    				CCB and the result is captured in a bit mask.

## Trunk Group Utilization Report

This report shows a summary of trunk group utilization. It is a grid (a tabular display).

This report is populated by data from the Usage Table ,
                              		  the Resource
                                 			 Table , and the Device Table .

Fields in this report are:

Date and Time

The date for the event. From Usage.eventdatetime.

Device

The IP address of the device. From Usage.DeviceID, where
                                    				Usage.DeviceID = Device.DeviceID.

Resource

The unique identifier of the resource being measured. From
                                    				Usage.ResourceID, where Usage.ResourceID = Resource.ResourceID. See the Resource for
                                    				the resource descriptors.

Average Resource Used

The average resource used, from Usage.ResourceUsed.

Max Threshold Reached

Was the maximum threshold reached (Yes | No), from
                                    				Usage.ThresholdReached.

Max Resource Used

The maximum resource used, from Usage.ResourceMax.

| Note | Callbacks reports
                                       		  must use the callback database as the data source or an error occurs
                                       		  when you attempt to access the report. The error message received is "Import could not be
                                          			 completed: Query validation failed against the selected data source." |
|---|---|