---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-icm-enterprise-icm-enterprise-15-0-1-user-guide--c1ffa15fc1
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/icm_enterprise/icm_enterprise_15_0_1/user/guide/ucce_b_cisco-unified-contact-center-enterprise-reporting-user-guide-release1501/ucce_b_cisco-unified-contact-center-enterprise-1261_chapter_01100.html
retrieved_at: 2026-08-16T20:34:36.321909+00:00
---

Cisco Unified Contact Center Enterprise Reporting User Guide, Release 15.0(1)

# Cisco Unified Contact Center Enterprise Reporting User Guide, Release 15.0(1)

Updated: April 30, 2025

Chapter: Outbound Real Time Reports

## Chapter: Outbound Real Time Reports

# Outbound Real Time Reports

## Call Summary Count
                        	 Per Campaign Real Time

The Call Summary
                              		  Count per Campaign Real Time report displays the status of each query rule
                              		  within a campaign, the current status of all campaign records, and the
                              		  currently valid campaign dialing times.

Views: This report has the following grid views and chart view:

Call Summary Count per Campaign Real Time (the default)

Valid Campaign Dialing Times Real Time

Summary of Call Counts Per Campaign Real Time

Select the view you want to see from the report drop-down list that is located on the top left corner.

Query: This report data
                              		  is built from an Anonymous Block query.

Value List: Campaigns

Database Schema Tables from which data is retrieved:

Campaign

Campaign_Query_Rule_Real_Time

### Current Fields
                              		  in the Call Summary Count Per Campaign Real Time View

Current fields are those fields that appear by default in a report generated from the stock template. Current fields are listed in
                              the order (left to right) in which they appear by default in the stock template.

Columns
                                          						(Fields)

Description

Campaign

The name
                                          						of the campaign.

Derived from: Campaign.CampaignName

Total
                                          						Records

The
                                          						total number of records.

Derived from: Campaign_Query_Rule_Real_Time.TotalCount

Available

The number of available records.

Derived from:
                                          									Campaign_Query_Rule_Real_Time.TotalCount-Campaign_Query_Rule_Real_Time.
                                          									FutureUseInt1-Campaign_Query_Rule_Real_Time.ClosedCount

Closed

The number of contacts closed.

Derived from: Campaign_Query_Rule_Real_Time.ClosedCount

Voice

The number of calls for the day that ended in successful customer contact.

Derived from: Campaign_Query_Rule_Real_Time.VoiceCount

### Current
                              		  Fields in the Summary of Call Counts Per Campaign Real Time Report View

Current fields are those fields that appear by default in a report generated from the stock template. Current fields are listed in
                              the order (left to right) in which they appear by default in the stock template.

Columns (Fields)

Description

Campaign

The
                                          						name of the campaign.

Derived from: Campaign.CampaignName

Attempts

Summary total of the number of calls attempted.

Derived from: Campaign_Query_Rule_Real_Time.AttemptedCount

Requested Personal Callback

The
                                          						number of callback contacts scheduled.

Derived from:
                                          						Campaign_Query_Rule_Real_Time.PersonalCallBackCount

Requested Callback

The
                                          						number of callback contacts.

Derived from: Campaign_Query_Rule_Real_Time.CallBackCount

Voice

The
                                          						number of calls for the day that ended in successful customer contact.

Derived from: Campaign_Query_Rule_Real_Time.VoiceCount

Busy

The
                                          						number of calls that detected a busy signal.

Derived from: Campaign_Query_Rule_Real_Time.BusyCount

No
                                          						Answer

The
                                          						number of calls that were not answered.

Derived from: Campaign_Query_Rule_Real_Time.NoAnswerDetectCount

No
                                          						Ringback

The
                                          						number of calls that did not detect a ring back. The Calls with CallResults 4,
                                          						27 and 28 are mentioned in this column.

Derived from:
                                          						Campaign_Query_Rule_Real_Time.NoRingBackDetectCount

No
                                          						Dialtone

The
                                          						number of calls that did not detect a dial tone.

Derived from:
                                          						Campaign_Query_Rule_Real_Time.NoDialToneDetectCount

Fax

The
                                          						number of calls that detected a fax.

Derived from: Campaign_Query_Rule_Real_Time.FaxDetectCount

Network IVR

The
                                          						number of calls that detected a network answering machine.

Derived from:
                                          						Campaign_Query_Rule_Real_Time.NetworkAnsMachinesCount

Answering Machine

The
                                          						number of calls that detected an answering machine.

Derived from:
                                          						Campaign_Query_Rule_Real_Time.AnsweringMachineCount

SIT
                                          						Tone

The
                                          						number of calls that detected a special information tone (SIT).

Derived from: Campaign_Query_Rule_Real_Time.SITToneDetectCount

Agent
                                          						Rejected

The
                                          						number of preview or callback calls that were rejected by the agent.

Derived from: Campaign_Query_Rule_Real_Time.AgentRejectedCount

Agent
                                          						Closed

The
                                          						number of preview or callback calls that were rejected by the agent. The agent
                                          						did not call these customers.

Derived from: Campaign_Query_Rule_Real_Time.AgentClosedCount

Customer Not Home

The
                                          						number of contacts where the party answering the phone was not the customer.

Derived from: Campaign_Query_Rule_Real_Time.CustomerNotHomeCount

Wrong
                                          						Number

The
                                          						number of contacts where the party answering the phone indicated that the customer
                                          						did not live there.

Derived from: Campaign_Query_Rule_Real_Time.WrongNumberCount

Canceled

The
                                          						number of calls where the dialer canceled a ringing customer call.

Derived from: Campaign_Query_Rule_Real_Time.CancelledDetectCount

Dialer
                                          						Abandon

The
                                          						number of calls abandoned by the dialer.

Derived from: Campaign_Query_Rule_Real_Time.AbandonDetectCount

Abandon to IVR

The
                                          						number of calls that were abandoned by the dialer and transferred to IVR, which
                                          						plays a message.

Derived from: Campaign_Query_Rule_Real_Time.AbandonToIVRCount

Customer Abandon

The number of calls where the customer ended the call immediately after picking up the phone.

Derived from:
                                          						Campaign_Query_Rule_Real_Time.CustomerAbandonDetectCount

Talk
                                          						Time

The
                                          						total time in HH:MM:SS (hours, minutes, seconds) that agents spent talking on
                                          						the phone today.

Derived from: Campaign_Query_Rule_Real_Time.TalkTimeCount

Wrap Up
                                          						Time

The
                                          						length of time the agents spent in wrap-up work.

Derived from: Campaign_Query_Rule_Real_Time.WrapupTimeCount

### Current Fields
                              		  in the Valid Campaign Dialing Times Real Time Report View

Current fields are those fields that appear by default in a report generated from the stock template. Current fields are listed in
                              the order (left to right) in which they appear by default in the stock template.

Columns
                                          						(Fields)

Description

Campaign

The name
                                          						of the campaign.

Derived from: Campaign.CampaignName

Start
                                          						Zone 1 Time

Campaign
                                          						Start Zone 1 time measured in HH:MM format. Campaign Start Zone 1 time is the
                                          						start time that a customer can be phoned at Zone 1. Zone 1 time and Zone 2 time
                                          						cannot overlap.

Derived from: Campaign.HomeStartHours ':'
                                          						Campaign.HomeStartMinutes

End Zone
                                          						1 Time

Campaign
                                          						End Zone 1 time measured in HH:MM format. Campaign End Zone 1 time is the time
                                          						beyond which a customer can no longer be phoned at Zone 1.

Derived from: Campaign.HomeEndHours ':' Campaign.HomeEndMinutes

Zone 1
                                          						Duration

The
                                          						total Zone 1 time. Zone 1 Duration = End Zone 1 Time-Start Zone 1 Time

Derived
                                          						from: Campaign.HomeDuration

Start
                                          						Zone 2 Time

Campaign Start Zone 2 time measured in HH:MM:SS format. Campaign Start Zone 2 time is the start time that a customer can be
                                          phoned at Zone 2. Campaign time is set to the customer's time zone. For example, if the campaign runs from 3 to 6 p.m. Eastern
                                          Standard time and it is past 6 p.m. on the East coast, you can still dial someone in Chicago because it is not yet 6 p.m.
                                          there.

Derived from: Campaign.WorkStartHours :
                                          						Campaign.WorkStartMinutes

End
                                          						Zone 2 Time

Campaign End Zone 2 time measured n HH:MM:SS format. Campaign
                                          						End Zone 2 time is the time beyond which a customer can no longer be phoned at
                                          						Zone 2.

Derived from: Campaign.WorkEndHours : Campaign.WorkEndMinutes

Zone 2
                                          						Duration

The
                                          						total Zone 2 time. Zone 2 Duration = End Zone 2 Time - Start Zone 2 Time

Derived from: Campaign.WorkDuration

## Dialer Real Time

The Dialer Real Time report provides the current status of each dialer.

This report is based on the Outbound Option Dialer: contacts, busy, voice, answering machine, SIT Tone detects, no answer,
                              and abandoned calls for each dialer.

Views: This report has one grid view, Dialer Real Time.

Query: This report data is built from an Anonymous Block Query.

Grouping: This report is grouped by Dialer.

Value List: Dialers

Database Schema Tables from which data is retrieved:

Dialer

Dialer_Real_Time

### Current Fields in the Dialer Real Time Report

Current fields are those fields that appear by default in a report generated from the stock template.

Current fields are listed in the order (left to right) in which they appear by default in the stock template.

Columns (Fields)

Description

Dialer

The name of the dialer.

Derived from: Dialer.DialerName

Attempts

The summary total of the number of contacts dialed today.

Derived from: Dialer_Real_Time.ContactsDialedToday

Requested Personal Callback

The number of callback contacts scheduled.

Derived from: Dialer_Real_Time.PersonalCallBackCount

Requested Callback

The number of callback contacts.

Derived from: Dialer_Real_Time.CallBackCount

Voice

The number of contacts for which a voice was detected today.

Derived from: Dialer_Real_Time.VoiceDetectToday

Busy

The number of contacts for which busy signals were detected today.

Derived from: Dialer_Real_Time.BusyDetectToday

No Answer

The number of contacts that were not answered today.

Derived from: Dialer_Real_Time.NoAnswerDetectToday

No Ringback

The number of contacts today that did not detect a ring back. The Calls with CallResults 4, 27, and 28 are mentioned in this
                                          column.

Derived from: Dialer_Real_Time.NoRingBackDetectHalf

No Dialtone

The number of contacts today that did not detect a dial tone.

Derived from: Dialer_Real_Time.NoDialToneDetectHalf

Fax

The number of contacts today that detected a fax.

Derived from: Dialer_Real_Time.FaxDetectHalf

Network IVR

The number of contacts today that detected a network answering machine.

Derived from: Dialer_Real_Time.NetworkAnsMachineDetectHalf

Answering Machine

The number of contacts today that detected an answering machine.

Derived from: Dialer_Real_Time.AnsweringMachineDetectToday

SIT Tone

The number of contacts today that detected a special information tone (SIT).

Derived from: Dialer_Real_Time.SITToneDetectToday

Agent Rejected

The number of preview or callback contacts that were rejected by the agent. (The agent did not call these customers.)

Derived from: Dialer_Real_Time.AgentRejectedDetectHalf

Agent Closed

The number of preview or callback contacts that were closed by the agent. (The agent did not call these customers.)

Derived from: Dialer_Real_Time.AgentClosedDetectHalf

Customer Not Home

The number of contacts today where the party answering the phone was not the customer.

Derived from: Dialer_Real_Time.CustomerNotHomeCount

Wrong Number

The number of contacts today where the party answering the phone indicated that the customer did not call.

Derived from: Dialer_Real_Time.WrongNumberCount

Canceled

The number of contacts today where the dialer canceled a ringing customer call.

Derived from: Dialer_Real_Time.CancelledDetectHalf

Dialer Abandon

The number of contacts in the half-hour interval abandoned by the dialer.

Derived from: Dialer_Real_Time.AbandonDetectToday

Abandon to IVR

The number of contacts today that were abandoned by the dialer and transferred to an IVR, which plays a message.

Derived from: Dialer_Real_Time.AbandonToIVRHalf

Customer Abandon

The number of contacts today where the customer ended the call immediately after picking up the phone.

Derived from: Dialer_Real_Time.CustomerAbandonDetectHalf

## Import Status Real Time

The Import Status Real Time report provides the status of Outbound Option import records.

This report is based on the Import Rule. It provides the number of good, bad, and total records imported, or to be imported.

Views: This report has one grid view, Import Rule.

Query: This report data is built from an Anonymous Block Query.

Grouping: There is no grouping for this report. The report is sorted by Import.

Value List: Import Rule

Database Schema Tables from which data is retrieved:

Import_Rule

Import_Rule_Real_Time

### Current Fields in the Import Status Real Time Report View

Current fields are those fields that appear by default in a report generated from the stock template.

Columns (Fields)

Description

Import

The name of the import rule.

Derived from: Import_Rule.ImportRuleName

Start Date

The time the import rule is scheduled to start.

Derived from: Import_Rule_Real_Time.DateTimeStart

Status

The status of the import rule. These are the codes:

380 = "IMPORT_BEGIN"

385 = "IMPORT_UPDATE"

390 = "BUILD_BEGIN"

410 = "BUILD_END"

420 = "IMPORT_END"

430 = "DNC_BEGIN"

450 = "DNC_END"

455 = "IMPORT_FAILED"

All other values = "IDLE"

Derived from: Import_Rule_Real_Time.Status

Good Records

The number of good records imported or to be imported.

Derived from: Import_Rule_Real_Time.GoodRecords

Bad Records

The number of bad records imported.

Derived from: Import_Rule_Real_Time.BadRecords

Total Records

The total number of records imported or to be imported.

Derived from: Import_Rule_Real_Time.TotalRecords

## Query Rule Within
                        	 Campaign Real Time

The Query Rule
                              		  Within Campaign Real Time report displays the current status of all campaign
                              		  records, dialing times, and query rule within a campaign.

Views: This report has the following grid views and chart view:

Call Counts of Query Rule within Campaign (the default)

Call Summary Count Of Query Rule Within Campaign

Query Rule Dialing Times

Select the view you want to see from the report drop-down list that is located on the top left corner.

Query: This report data
                              		  is built from an Anonymous Block.

Grouping: This report
                              		  is grouped by Campaign and Query Rule. The report is sorted by Campaign.

Value List: Campaigns

Database Schema Tables from which data is retrieved:

Campaign

Query_Rule

Campaign_Query_Rule_Real_Time

Campaign_Query_Rule

### Current Fields
                              		  in the Call Counts of Query Rule Within Campaign View

Current fields are those fields that appear by default in a report generated from the stock template. Current fields are listed in
                              the order (left to right) in which they appear by default in the stock template.

Columns
                                          						(Fields)

Description

Campaign

The name
                                          						of the campaign.

Derived from: Campaign.CampaignName

Query
                                          						Rule

The name
                                          						of the query rule.

Derived from: Query_Rule.QueryRuleName

DateTime

The date
                                          						and time in MM/DD/YYYY (month, day, year) and HH:MM (hours, minutes, seconds)
                                          						format.

Derived from: Campaign_Query_Rule_Real_Time.DateTime

Attempts

The
                                          						summary total of the number of calls attempted.

Derived from: Campaign_Query_Rule_Real_Time.AttemptedCount

Requested Personal Callback

The
                                          						number of callback contacts scheduled.

Derived from: Dialer_Real_Time.PersonalCallBackCount

Requested Callback

The
                                          						number of callback contacts.

Derived from: Dialer_Real_Time.CallBackCount

Voice

The
                                          						number of contacts for which a voice was detected today.

Derived from: Dialer_Real_Time.VoiceDetectToday

Busy

The
                                          						number of contacts for which busy signals were detected today.

Derived from: Dialer_Real_Time.BusyDetectToday

No
                                          						Answer

The
                                          						number of contacts that were not answered today.

Derived from: Dialer_Real_Time.NoAnswerDetectToday

No
                                          						Ringback

The
                                          						number of contacts today that did not detect a ring back. The Calls with
                                          						CallResults 4, 27 and 28 are mentioned in this column.

Derived from: Dialer_Real_Time.NoRingBackDetectHalf

No
                                          						Dialtone

The
                                          						number of contacts today that did not detect a dial tone.

Derived from: Dialer_Real_Time.NoDialToneDetectHalf

Fax

The
                                          						number of contacts today that detected a fax.

Derived from: Dialer_Real_Time.FaxDetectHalf

Network IVR

The
                                          						number of contacts today that detected a network answering machine.

Derived from: Dialer_Real_Time.NetworkAnsMachineDetectHalf

Answering Machine

The
                                          						number of contacts today that detected an answering machine.

Derived from: Dialer_Real_Time.AnsweringMachineDetectToday

SIT
                                          						Tone

The
                                          						number of contacts today that detected a special information tone (SIT).

Derived from: Dialer_Real_Time.SITToneDetectToday

Agent
                                          						Rejected

The
                                          						number of preview or callback contacts today that were rejected by the agent.
                                          						(The agent did not call these customers.)

Derived from: Dialer_Real_Time.AgentRejectedDetectHalf

Agent
                                          						Closed

The
                                          						number of preview or callback contacts that were closed by the agent. (The
                                          						agent did not call these customers.)

Derived from: Dialer_Real_Time.AgentClosedDetectHalf

Customer Not Home

The
                                          						number of contacts today where the party answering the phone was not the
                                          						customer.

Derived from: Dialer_Real_Time.CustomerNotHomeCount

Wrong
                                          						Number

The
                                          						number of contacts today where the party answering the phone indicated that the
                                          						customer did not live there.

Derived from: Dialer_Real_Time.WrongNumberCount

Canceled

The
                                          						number of contacts today where the dialer canceled a ringing customer call.

Derived from: Dialer_Real_Time.CancelledDetectHalf

Dialer
                                          						Abandon

The
                                          						number of contacts in the half-hour interval abandoned by the dialer.

Derived from: Dialer_Real_Time.AbandonDetectToday

Abandon to IVR

The
                                          						number of contacts today that were abandoned by the dialer and transferred to
                                          						an IVR, which plays a message.

Derived from: Dialer_Real_Time.AbandonToIVRHalf

Customer Abandon

The number of contacts today where the customer ended the call immediately after picking up the phone.

Derived from: Dialer_Real_Time.CustomerAbandonDetectHalf

Talk
                                          						Time

The
                                          						total time in HH:MM (hours, minutes, seconds) that agents spent talking on the
                                          						phone today.

Derived from: Campaign_Query_Rule_Real_Time.TalkTimeCount

Wrap
                                          						Up Time

The
                                          						length of time the agents spent in wrap-up work.

Derived from: Campaign_Query_Rule_Real_Time.WrapupTimeCount

### Current
                              		  Fields in the Call Summary Count of Query Rule Within Campaign View

Current fields are those fields that appear by default in a report generated from the stock template. Current fields are listed in
                              the order (left to right) in which they appear by default in the stock template.

Columns (Fields)

Description

Campaign

The
                                          						name of the campaign.

Derived from: Campaign.CampaignName

Query
                                          						Rule

The
                                          						name of the query rule.

Derived from: Query_Rule.QueryRuleName

Total
                                          						Records

The
                                          						total number of records.

Derived from: Campaign_Query_Rule_Real_Time.TotalCount

Available

The number of available records.

Derived from: Campaign_Query_Rule_Real_Time.TotalCount - Campaign_Query_Rule_Real_Time.VoiceCount - Campaign_Query_Rule_Real_Time.ClosedCount

Closed

The
                                          						number of contacts attempted.

Derived from: Campaign_Query_Rule_Real_Time.ClosedCount

Voice

The
                                          						number of contacts for which a voice was detected today.

Derived from: Dialer_Real_Time.VoiceDetectToday

### Current
                              		  Fields in the Query Rule Dialing Times View

Current fields are those fields that appear by default in a report generated from the stock template. Current fields are listed in
                              the order (left to right) in which they appear by default in the stock template.

Columns (Fields)

Description

Campaign

The name of the campaign.

Derived from: Campaign.CampaignName

Query Rule

The name of the query rule.

Derived from: Query_Rule.QueryRuleName

CAMPAIGN DATA

Start Zone 1 Time

Campaign Start Zone 1 time measured in HH:MM format. Campaign Start Zone 1 time is the start time that a customer can be phoned
                                          at Zone1. Zone 1 time and Zone 2 time cannot overlap.

Derived from: Campaign.HomeStartHours ':' Campaign.HomeStartMinutes

End Zone 1 Time

Campaign End Zone 1 time measured in HH:MM format. Campaign End Zone 1 time is the time beyond which a customer can no longer
                                          be phoned at Zone1.

Derived from: Campaign.WorkEndHours ':' Campaign.WorkEndMinutes

Zone 1 Duration

The total Zone 1 time. Home Duration = End Home Time - Start Home Time.

Derived from: (((Campaign.HomeEndHours * 60) + (Campaign.HomeEndMinutes)) - ((Campaign.HomeStartHours * 60) + (Campaign.HomeStartMinutes)))

Start Zone 2 Time

Campaign Start Zone 2 time measured in HH:MM format. Campaign Start Zone 2 time is the start time that a customer can be phoned
                                          at Zone2. Campaign time is set to the customer's time zone. For example, if the campaign runs from 3 to 6 p.m. Eastern Standard
                                          time and it is past 6 p.m. on the East coast, you can still dial someone in Chicago because it is not yet 6 p.m. there.

Derived from: Campaign.WorkStartHours ':' Campaign.WorkStartMinutes

End Zone 2 Time

The Zone 2 time in HH:MM format at which the campaign ends.

Derived from: Campaign.WorkEndHours ':' Campaign.WorkEndMinutes

Zone 2 Duration

The total Zone 2 time. Work Duration = End Work Time - Start Work Time.

Derived from: (((Campaign.WorkEndHours * 60) + (Campaign.WorkEndMinutes)) - ((Campaign.WorkStartHours * 60) + (Campaign.WorkStartMinutes)))

QUERY RULE DATA

Query Rule Start Time

The time in HH:MM format that the query rule starts. Query rule time is based on the Central Controller's time zone. Typically,
                                          the Administration and Data Server from which a query is run is in the Central Controller's time zone.

Derived from: Campaign_Query_Rule.StartHours ":" Campaign_Query_Rule.StartMinutes

Query Rule End Time

The time in HH:MM format that the query rule ends.

Derived from: Campaign_Query_Rule.EndHours ':' Campaign_Query_Rule.EndMinutes

Query Rule Duration

The total query rule time. Work Duration = End Query Rule Time - Start Query Rule Time.

Derived from: (((Campaign_Query_Rule.EndHours * 60) + (Campaign_Query_Rule.EndMinutes)) - ((Campaign_Query_Rule.StartHours
                                          * 60) + (Campaign_Query_Rule.StartMinutes)))

| Columns
                                          						(Fields) | Description |
|---|---|
| Campaign | The name
                                          						of the campaign. Derived from: Campaign.CampaignName |
| Total
                                          						Records | The
                                          						total number of records. Derived from: Campaign_Query_Rule_Real_Time.TotalCount |
| Available | The number of available records. Derived from:
                                          									Campaign_Query_Rule_Real_Time.TotalCount-Campaign_Query_Rule_Real_Time.
                                          									FutureUseInt1-Campaign_Query_Rule_Real_Time.ClosedCount |
| Closed | The number of contacts closed. Derived from: Campaign_Query_Rule_Real_Time.ClosedCount |
| Voice | The number of calls for the day that ended in successful customer contact. Derived from: Campaign_Query_Rule_Real_Time.VoiceCount |

| Columns (Fields) | Description |
|---|---|
| Campaign | The
                                          						name of the campaign. Derived from: Campaign.CampaignName |
| Attempts | Summary total of the number of calls attempted. Derived from: Campaign_Query_Rule_Real_Time.AttemptedCount |
| Requested Personal Callback | The
                                          						number of callback contacts scheduled. Derived from:
                                          						Campaign_Query_Rule_Real_Time.PersonalCallBackCount |
| Requested Callback | The
                                          						number of callback contacts. Derived from: Campaign_Query_Rule_Real_Time.CallBackCount |
| Voice | The
                                          						number of calls for the day that ended in successful customer contact. Derived from: Campaign_Query_Rule_Real_Time.VoiceCount |
| Busy | The
                                          						number of calls that detected a busy signal. Derived from: Campaign_Query_Rule_Real_Time.BusyCount |
| No
                                          						Answer | The
                                          						number of calls that were not answered. Derived from: Campaign_Query_Rule_Real_Time.NoAnswerDetectCount |
| No
                                          						Ringback | The
                                          						number of calls that did not detect a ring back. The Calls with CallResults 4,
                                          						27 and 28 are mentioned in this column. Derived from:
                                          						Campaign_Query_Rule_Real_Time.NoRingBackDetectCount |
| No
                                          						Dialtone | The
                                          						number of calls that did not detect a dial tone. Derived from:
                                          						Campaign_Query_Rule_Real_Time.NoDialToneDetectCount |
| Fax | The
                                          						number of calls that detected a fax. Derived from: Campaign_Query_Rule_Real_Time.FaxDetectCount |
| Network IVR | The
                                          						number of calls that detected a network answering machine. Derived from:
                                          						Campaign_Query_Rule_Real_Time.NetworkAnsMachinesCount |
| Answering Machine | The
                                          						number of calls that detected an answering machine. Derived from:
                                          						Campaign_Query_Rule_Real_Time.AnsweringMachineCount |
| SIT
                                          						Tone | The
                                          						number of calls that detected a special information tone (SIT). Derived from: Campaign_Query_Rule_Real_Time.SITToneDetectCount |
| Agent
                                          						Rejected | The
                                          						number of preview or callback calls that were rejected by the agent. Derived from: Campaign_Query_Rule_Real_Time.AgentRejectedCount |
| Agent
                                          						Closed | The
                                          						number of preview or callback calls that were rejected by the agent. The agent
                                          						did not call these customers. Derived from: Campaign_Query_Rule_Real_Time.AgentClosedCount |
| Customer Not Home | The
                                          						number of contacts where the party answering the phone was not the customer. Derived from: Campaign_Query_Rule_Real_Time.CustomerNotHomeCount |
| Wrong
                                          						Number | The
                                          						number of contacts where the party answering the phone indicated that the customer
                                          						did not live there. Derived from: Campaign_Query_Rule_Real_Time.WrongNumberCount |
| Canceled | The
                                          						number of calls where the dialer canceled a ringing customer call. Derived from: Campaign_Query_Rule_Real_Time.CancelledDetectCount |
| Dialer
                                          						Abandon | The
                                          						number of calls abandoned by the dialer. Derived from: Campaign_Query_Rule_Real_Time.AbandonDetectCount |
| Abandon to IVR | The
                                          						number of calls that were abandoned by the dialer and transferred to IVR, which
                                          						plays a message. Derived from: Campaign_Query_Rule_Real_Time.AbandonToIVRCount |
| Customer Abandon | The number of calls where the customer ended the call immediately after picking up the phone. Derived from:
                                          						Campaign_Query_Rule_Real_Time.CustomerAbandonDetectCount |
| Talk
                                          						Time | The
                                          						total time in HH:MM:SS (hours, minutes, seconds) that agents spent talking on
                                          						the phone today. Derived from: Campaign_Query_Rule_Real_Time.TalkTimeCount |
| Wrap Up
                                          						Time | The
                                          						length of time the agents spent in wrap-up work. Derived from: Campaign_Query_Rule_Real_Time.WrapupTimeCount |

| Columns
                                          						(Fields) | Description |
|---|---|
| Campaign | The name
                                          						of the campaign. Derived from: Campaign.CampaignName |
| Start
                                          						Zone 1 Time | Campaign
                                          						Start Zone 1 time measured in HH:MM format. Campaign Start Zone 1 time is the
                                          						start time that a customer can be phoned at Zone 1. Zone 1 time and Zone 2 time
                                          						cannot overlap. Derived from: Campaign.HomeStartHours ':'
                                          						Campaign.HomeStartMinutes |
| End Zone
                                          						1 Time | Campaign
                                          						End Zone 1 time measured in HH:MM format. Campaign End Zone 1 time is the time
                                          						beyond which a customer can no longer be phoned at Zone 1. Derived from: Campaign.HomeEndHours ':' Campaign.HomeEndMinutes |
| Zone 1
                                          						Duration | The
                                          						total Zone 1 time. Zone 1 Duration = End Zone 1 Time-Start Zone 1 Time Derived
                                          						from: Campaign.HomeDuration |
| Start
                                          						Zone 2 Time | Campaign Start Zone 2 time measured in HH:MM:SS format. Campaign Start Zone 2 time is the start time that a customer can be
                                          phoned at Zone 2. Campaign time is set to the customer's time zone. For example, if the campaign runs from 3 to 6 p.m. Eastern
                                          Standard time and it is past 6 p.m. on the East coast, you can still dial someone in Chicago because it is not yet 6 p.m.
                                          there. Derived from: Campaign.WorkStartHours :
                                          						Campaign.WorkStartMinutes |
| End
                                          						Zone 2 Time | Campaign End Zone 2 time measured n HH:MM:SS format. Campaign
                                          						End Zone 2 time is the time beyond which a customer can no longer be phoned at
                                          						Zone 2. Derived from: Campaign.WorkEndHours : Campaign.WorkEndMinutes |
| Zone 2
                                          						Duration | The
                                          						total Zone 2 time. Zone 2 Duration = End Zone 2 Time - Start Zone 2 Time Derived from: Campaign.WorkDuration |

| Columns (Fields) | Description |
|---|---|
| Dialer | The name of the dialer. Derived from: Dialer.DialerName |
| Attempts | The summary total of the number of contacts dialed today. Derived from: Dialer_Real_Time.ContactsDialedToday |
| Requested Personal Callback | The number of callback contacts scheduled. Derived from: Dialer_Real_Time.PersonalCallBackCount |
| Requested Callback | The number of callback contacts. Derived from: Dialer_Real_Time.CallBackCount |
| Voice | The number of contacts for which a voice was detected today. Derived from: Dialer_Real_Time.VoiceDetectToday |
| Busy | The number of contacts for which busy signals were detected today. Derived from: Dialer_Real_Time.BusyDetectToday |
| No Answer | The number of contacts that were not answered today. Derived from: Dialer_Real_Time.NoAnswerDetectToday |
| No Ringback | The number of contacts today that did not detect a ring back. The Calls with CallResults 4, 27, and 28 are mentioned in this
                                          column. Derived from: Dialer_Real_Time.NoRingBackDetectHalf |
| No Dialtone | The number of contacts today that did not detect a dial tone. Derived from: Dialer_Real_Time.NoDialToneDetectHalf |
| Fax | The number of contacts today that detected a fax. Derived from: Dialer_Real_Time.FaxDetectHalf |
| Network IVR | The number of contacts today that detected a network answering machine. Derived from: Dialer_Real_Time.NetworkAnsMachineDetectHalf |
| Answering Machine | The number of contacts today that detected an answering machine. Derived from: Dialer_Real_Time.AnsweringMachineDetectToday |
| SIT Tone | The number of contacts today that detected a special information tone (SIT). Derived from: Dialer_Real_Time.SITToneDetectToday |
| Agent Rejected | The number of preview or callback contacts that were rejected by the agent. (The agent did not call these customers.) Derived from: Dialer_Real_Time.AgentRejectedDetectHalf |
| Agent Closed | The number of preview or callback contacts that were closed by the agent. (The agent did not call these customers.) Derived from: Dialer_Real_Time.AgentClosedDetectHalf |
| Customer Not Home | The number of contacts today where the party answering the phone was not the customer. Derived from: Dialer_Real_Time.CustomerNotHomeCount |
| Wrong Number | The number of contacts today where the party answering the phone indicated that the customer did not call. Derived from: Dialer_Real_Time.WrongNumberCount |
| Canceled | The number of contacts today where the dialer canceled a ringing customer call. Derived from: Dialer_Real_Time.CancelledDetectHalf |
| Dialer Abandon | The number of contacts in the half-hour interval abandoned by the dialer. Derived from: Dialer_Real_Time.AbandonDetectToday |
| Abandon to IVR | The number of contacts today that were abandoned by the dialer and transferred to an IVR, which plays a message. Derived from: Dialer_Real_Time.AbandonToIVRHalf |
| Customer Abandon | The number of contacts today where the customer ended the call immediately after picking up the phone. Derived from: Dialer_Real_Time.CustomerAbandonDetectHalf |

| Columns (Fields) | Description |
|---|---|
| Import | The name of the import rule. Derived from: Import_Rule.ImportRuleName |
| Start Date | The time the import rule is scheduled to start. Derived from: Import_Rule_Real_Time.DateTimeStart |
| Status | The status of the import rule. These are the codes: 380 = "IMPORT_BEGIN" 385 = "IMPORT_UPDATE" 390 = "BUILD_BEGIN" 410 = "BUILD_END" 420 = "IMPORT_END" 430 = "DNC_BEGIN" 450 = "DNC_END" 455 = "IMPORT_FAILED" All other values = "IDLE" Derived from: Import_Rule_Real_Time.Status |
| Good Records | The number of good records imported or to be imported. Derived from: Import_Rule_Real_Time.GoodRecords |
| Bad Records | The number of bad records imported. Derived from: Import_Rule_Real_Time.BadRecords |
| Total Records | The total number of records imported or to be imported. Derived from: Import_Rule_Real_Time.TotalRecords |

| Columns
                                          						(Fields) | Description |
|---|---|
| Campaign | The name
                                          						of the campaign. Derived from: Campaign.CampaignName |
| Query
                                          						Rule | The name
                                          						of the query rule. Derived from: Query_Rule.QueryRuleName |
| DateTime | The date
                                          						and time in MM/DD/YYYY (month, day, year) and HH:MM (hours, minutes, seconds)
                                          						format. Derived from: Campaign_Query_Rule_Real_Time.DateTime |
| Attempts | The
                                          						summary total of the number of calls attempted. Derived from: Campaign_Query_Rule_Real_Time.AttemptedCount |
| Requested Personal Callback | The
                                          						number of callback contacts scheduled. Derived from: Dialer_Real_Time.PersonalCallBackCount |
| Requested Callback | The
                                          						number of callback contacts. Derived from: Dialer_Real_Time.CallBackCount |
| Voice | The
                                          						number of contacts for which a voice was detected today. Derived from: Dialer_Real_Time.VoiceDetectToday |
| Busy | The
                                          						number of contacts for which busy signals were detected today. Derived from: Dialer_Real_Time.BusyDetectToday |
| No
                                          						Answer | The
                                          						number of contacts that were not answered today. Derived from: Dialer_Real_Time.NoAnswerDetectToday |
| No
                                          						Ringback | The
                                          						number of contacts today that did not detect a ring back. The Calls with
                                          						CallResults 4, 27 and 28 are mentioned in this column. Derived from: Dialer_Real_Time.NoRingBackDetectHalf |
| No
                                          						Dialtone | The
                                          						number of contacts today that did not detect a dial tone. Derived from: Dialer_Real_Time.NoDialToneDetectHalf |
| Fax | The
                                          						number of contacts today that detected a fax. Derived from: Dialer_Real_Time.FaxDetectHalf |
| Network IVR | The
                                          						number of contacts today that detected a network answering machine. Derived from: Dialer_Real_Time.NetworkAnsMachineDetectHalf |
| Answering Machine | The
                                          						number of contacts today that detected an answering machine. Derived from: Dialer_Real_Time.AnsweringMachineDetectToday |
| SIT
                                          						Tone | The
                                          						number of contacts today that detected a special information tone (SIT). Derived from: Dialer_Real_Time.SITToneDetectToday |
| Agent
                                          						Rejected | The
                                          						number of preview or callback contacts today that were rejected by the agent.
                                          						(The agent did not call these customers.) Derived from: Dialer_Real_Time.AgentRejectedDetectHalf |
| Agent
                                          						Closed | The
                                          						number of preview or callback contacts that were closed by the agent. (The
                                          						agent did not call these customers.) Derived from: Dialer_Real_Time.AgentClosedDetectHalf |
| Customer Not Home | The
                                          						number of contacts today where the party answering the phone was not the
                                          						customer. Derived from: Dialer_Real_Time.CustomerNotHomeCount |
| Wrong
                                          						Number | The
                                          						number of contacts today where the party answering the phone indicated that the
                                          						customer did not live there. Derived from: Dialer_Real_Time.WrongNumberCount |
| Canceled | The
                                          						number of contacts today where the dialer canceled a ringing customer call. Derived from: Dialer_Real_Time.CancelledDetectHalf |
| Dialer
                                          						Abandon | The
                                          						number of contacts in the half-hour interval abandoned by the dialer. Derived from: Dialer_Real_Time.AbandonDetectToday |
| Abandon to IVR | The
                                          						number of contacts today that were abandoned by the dialer and transferred to
                                          						an IVR, which plays a message. Derived from: Dialer_Real_Time.AbandonToIVRHalf |
| Customer Abandon | The number of contacts today where the customer ended the call immediately after picking up the phone. Derived from: Dialer_Real_Time.CustomerAbandonDetectHalf |
| Talk
                                          						Time | The
                                          						total time in HH:MM (hours, minutes, seconds) that agents spent talking on the
                                          						phone today. Derived from: Campaign_Query_Rule_Real_Time.TalkTimeCount |
| Wrap
                                          						Up Time | The
                                          						length of time the agents spent in wrap-up work. Derived from: Campaign_Query_Rule_Real_Time.WrapupTimeCount |

| Columns (Fields) | Description |
|---|---|
| Campaign | The
                                          						name of the campaign. Derived from: Campaign.CampaignName |
| Query
                                          						Rule | The
                                          						name of the query rule. Derived from: Query_Rule.QueryRuleName |
| Total
                                          						Records | The
                                          						total number of records. Derived from: Campaign_Query_Rule_Real_Time.TotalCount |
| Available | The number of available records. Derived from: Campaign_Query_Rule_Real_Time.TotalCount - Campaign_Query_Rule_Real_Time.VoiceCount - Campaign_Query_Rule_Real_Time.ClosedCount |
| Closed | The
                                          						number of contacts attempted. Derived from: Campaign_Query_Rule_Real_Time.ClosedCount |
| Voice | The
                                          						number of contacts for which a voice was detected today. Derived from: Dialer_Real_Time.VoiceDetectToday |

| Columns (Fields) | Description |
|---|---|
| Campaign | The name of the campaign. Derived from: Campaign.CampaignName |
| Query Rule | The name of the query rule. Derived from: Query_Rule.QueryRuleName |
| CAMPAIGN DATA |
| Start Zone 1 Time | Campaign Start Zone 1 time measured in HH:MM format. Campaign Start Zone 1 time is the start time that a customer can be phoned
                                          at Zone1. Zone 1 time and Zone 2 time cannot overlap. Derived from: Campaign.HomeStartHours ':' Campaign.HomeStartMinutes |
| End Zone 1 Time | Campaign End Zone 1 time measured in HH:MM format. Campaign End Zone 1 time is the time beyond which a customer can no longer
                                          be phoned at Zone1. Derived from: Campaign.WorkEndHours ':' Campaign.WorkEndMinutes |
| Zone 1 Duration | The total Zone 1 time. Home Duration = End Home Time - Start Home Time. Derived from: (((Campaign.HomeEndHours * 60) + (Campaign.HomeEndMinutes)) - ((Campaign.HomeStartHours * 60) + (Campaign.HomeStartMinutes))) |
| Start Zone 2 Time | Campaign Start Zone 2 time measured in HH:MM format. Campaign Start Zone 2 time is the start time that a customer can be phoned
                                          at Zone2. Campaign time is set to the customer's time zone. For example, if the campaign runs from 3 to 6 p.m. Eastern Standard
                                          time and it is past 6 p.m. on the East coast, you can still dial someone in Chicago because it is not yet 6 p.m. there. Derived from: Campaign.WorkStartHours ':' Campaign.WorkStartMinutes |
| End Zone 2 Time | The Zone 2 time in HH:MM format at which the campaign ends. Derived from: Campaign.WorkEndHours ':' Campaign.WorkEndMinutes |
| Zone 2 Duration | The total Zone 2 time. Work Duration = End Work Time - Start Work Time. Derived from: (((Campaign.WorkEndHours * 60) + (Campaign.WorkEndMinutes)) - ((Campaign.WorkStartHours * 60) + (Campaign.WorkStartMinutes))) |
| QUERY RULE DATA |
| Query Rule Start Time | The time in HH:MM format that the query rule starts. Query rule time is based on the Central Controller's time zone. Typically,
                                          the Administration and Data Server from which a query is run is in the Central Controller's time zone. Derived from: Campaign_Query_Rule.StartHours ":" Campaign_Query_Rule.StartMinutes |
| Query Rule End Time | The time in HH:MM format that the query rule ends. Derived from: Campaign_Query_Rule.EndHours ':' Campaign_Query_Rule.EndMinutes |
| Query Rule Duration | The total query rule time. Work Duration = End Query Rule Time - Start Query Rule Time. Derived from: (((Campaign_Query_Rule.EndHours * 60) + (Campaign_Query_Rule.EndMinutes)) - ((Campaign_Query_Rule.StartHours
                                          * 60) + (Campaign_Query_Rule.StartMinutes))) |

| Note | Campaign_Query_Rule_Real_Time report is not applicable for API campaign. |
|---|---|