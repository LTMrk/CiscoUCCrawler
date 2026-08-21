---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-pcce-pcce-12-5-1-maintenance-guide-pcce-b-report-d750459d6c
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/pcce/pcce_12_5_1/maintenance/guide/pcce_b_Reporting-User-Guide-12-5/pcce_b_cisco-packaged-contact-center-enterprise_chapter_010101.html
retrieved_at: 2026-08-21T16:58:46.526616+00:00
---

Cisco Packaged Contact Center Enterprise Reporting User Guide, Release 12.5(1)

# Cisco Packaged Contact Center Enterprise Reporting User Guide, Release 12.5(1)

Updated: February 4, 2020

Chapter: Historical Outbound Option Report Templates

## Chapter: Historical Outbound Option Report Templates

# Historical Outbound Option Report Templates

## Attempts Per Campaign
                        		Daily

The Attempts per Campaign Daily report shows the status (summary and percentage) of each campaign for the selected time period
                              and the breakdown of attempts (in percentage) of each campaign for the selected time period.

Views: This report has the following grid views:

Breakdown of Attempts per Campaign Daily (the default)

Summary of Attempts per Campaign Daily

Select the view you want to see from the report drop-down list that is located on the top left corner.

Query: This report data is built from an Anonymous type query.

Value List: Campaigns

Database Schema Tables from which data is retrieved:

Campaign

Campaign_Query_Rule_Interval

### Breakdown of
                              		  Attempts Per Campaign Daily Report View

Current fields are those fields that appear by default in a report generated from the stock template.

Columns (Fields)

Description

Campaign

The
                                          						name of the campaign.

Derived from: Campaign.CampaignName

Date

The date for the record in MM/DD/YYYY (month, day, year) format.

Derived from: Campaign_Query_Rule_Interval.DateTime

Attempts

The total number of outbound calls attempted.

Derived from: Campaign_Query_Rule_Interval.ContactsAttempted

Customer Answered

Right Party Connect

The percentage of calls attempted when the
                                          						actual customer was contacted and handled, as indicated by agents using their desktop.

Derived from: Campaign_Query_Rule_Interval. VoiceDetect/ Campaign_Query_Rule_Interval.ContactsAttempted

Dialer Abandon

The percentage of contacts or attempts abandoned by the dialer
                                          						because the agent was not available and "Abandon to IVR" was not
                                          						configured.

Derived from: Campaign_Query_Rule_Interval. AbandonDetect/ Campaign_Query_Rule_Interval.ContactsAttempted

Abandon to IVR

The percentage of contacts or attempts that were abandoned by
                                          						the dialer but transferred to an IVR. That is, the percentage of attempts that
                                          						were sent to IVR (or another dialed number) for treatment after the dialer
                                          						reached a contact and no agent was available to take the call. 
                                          					 Instead of hanging up on the customer, the customer was
                                          						transferred to an IVR, which plays a message.

Derived from: Campaign_Query_Rule_Interval. AbandonToIVR/ Campaign_Query_Rule_Interval.ContactsAttempted

Callback

When the campaign is not
                                          						configured for personal callback, the percentage of customers contacted that  request a callback.

Derived from: Campaign_Query_Rule_Interval. CallbackCount/Campaign_Query_Rule_Interval.ContactsAttempted

Personal Callback

When the campaign
                                          						is configured for personal callback, the percentage of contacts in which the customer requested a callback and was scheduled.

Derived from: Campaign_Query_Rule_Interval. PersonalCallbackCount/Campaign_Query_Rule_Interval.ContactsAttempted

Customer Not Home

The percentage of contacts where the party answering the
                                          						phone was not the customer.

Derived from: Campaign_Query_Rule_Interval. CustomerNotHomeCount/Campaign_Query_Rule_Interval.ContactsAttempted

Wrong Number

The percentage of contacts where the party answering the
                                          						phone indicated that the customer was not available.

Derived from: Campaign_Query_Rule_Interval. WrongNumberCount/Campaign_Query_Rule_Interval.ContactsAttempted

Customer Abandon

The percentage of contacts where the customer ended the call immediately after being connected to an agent.

Derived from: Campaign_Query_Rule_Interval. CustomerAbandonDetect/Campaign_Query_Rule_Interval.ContactsAttempted

Customer Did Not Answer

Answering Machine

The percentage of contacts that detected an answering
                                          						machine.

Derived from: Campaign_Query_Rule_Interval. AnsweringMachineDetectToHal/Campaign_Query_Rule_Interval.ContactsAttempted

No Answer

The percentage of contacts that were not answered.

Derived from: Campaign_Query_Rule_Interval. NoAnswerDetect/Campaign_Query_Rule_Interval.ContactsAttempted

Busy

The percentage of contacts that detected a busy signal.

Derived from: Campaign_Query_Rule_Interval. BusyDetect/Campaign_Query_Rule_Interval.ContactsAttempted

Canceled

The percentage of contacts where the dialer canceled a
                                          						ringing customer call.

Derived from: Campaign_Query_Rule_Interval. CanceledDetect/Campaign_Query_Rule_Interval.ContactsAttempted

Problem

SIT Tone

The number of contacts in the half-hour interval that detected a Special
                                          						Information Tone (SIT).

Derived from: Campaign_Query_Rule_Interval.SITToneDetect

No Dial tone

The
                                          						number of contacts in the half-hour interval that did not detect a dial tone.

Derived from:
                                          						Campaign_Query_Rule_Interval.NoDialToneDetect

Fax

The
                                          						number of contacts in the half-hour interval that detected a fax.

Campaign_Query_Rule_Interval.FaxDetect

Network Error

The number of contacts that encountered one of the following problems:

No Ringback from network when dial attempted

Network disconnected while alerting

Low Energy ("or dead air") call detected by the dialer.

Derived from:
                                          						Campaign_Query_Rule_Interval.NoRingBackDetect

### Current Fields
                              		  in the Summary of Attempts Per Campaign Daily Report View

Current fields are those fields that appear by default in a report generated from the stock template.

Columns
                                          						(Fields)

Description

Campaign

The name
                                          						of the campaign.

Derived
                                          						from: Campaign.CampaignName

Date

The date for the record in MM/DD/YYYY (month, day, year) format.

Derived from: Campaign_Query_Rule_Interval.DateTime

Key
                                             						Statistics

Customer Answered

The
                                          						number of outbound calls (attempts) that reached a live voice.

Derived
                                          						from: Campaign_Query_Rule_Interval.VoiceDetect +
                                          						Campaign_Query_Rule_Interval.WrongNumberCount +
                                          						Campaign_Query_Rule_Interval.CustomerNotHomeCount +
                                          						Campaign_Query_Rule_Interval.CustomerAbandonDetect +
                                          						Campaign_Query_Rule_Interval.CallbackCount +
                                          						Campaign_Query_Rule_Interval.PersonalCallbackCount +
                                          						Campaign_Query_Rule_Interval.AbandonDetect +
                                          						Campaign_Query_Rule_Interval.AbandonToIVR

Right Party  
                                          					 Connect

The
                                          						number of call attempts, as indicated by agents using their desktop, when
                                          						the actual customer was contacted and handled.

Derived
                                          						from: Campaign_Query_Rule_Interval.VoiceDetect

Dialer Abandon & Abandon to IVR

The
                                          						number of calls that were abandoned by the dialer or abandoned to IVR because
                                          						an agent was not available to take the call. Campaign configuration
                                          						determines whether these calls are abandoned at the dialer or transferred to IVR.

Derived
                                          						from: Campaign_Query_Rule_Interval. AbandonToIVR +
                                          						Campaign_Query_Rule_Interval. AbandonDetect

Attempts

Total

The
                                          						total number of outbound calls attempted.

Derived
                                          						from: Campaign_Query_Rule_Interval.ContactsAttempted

Customer Answered

The
                                          						percentage of attempted calls that reached a live voice.

Derived
                                          						from: (Campaign_Query_Rule_Interval.VoiceDetect +
                                          						Campaign_Query_Rule_Interval.WrongNumberCount +
                                          						Campaign_Query_Rule_Interval.CustomerNotHomeCount +
                                          						Campaign_Query_Rule_Interval.CustomerAbandonDetect +
                                          						Campaign_Query_Rule_Interval.CallbackCount +
                                          						Campaign_Query_Rule_Interval.PersonalCallbackCount +
                                          						Campaign_Query_Rule_Interval.AbandonDetect +
                                          						Campaign_Query_Rule_Interval.AbandonToIVR)/
                                          						Campaign_Query_Rule_Interval.ContactsAttempted

Did not Answer

The
                                          						percentage of calls attempted when the number was dialed but the customer was
                                          						not reached and there were no problems with the call ("Ring No Answer").

Derived
                                          						from: (Campaign_Query_Rule_Interval.AnsweringMachineDetect +
                                          						Campaign_Query_Rule_Interval.BusyDetect +
                                          						Campaign_Query_Rule_Interval.NoAnswerDetect +
                                          						Campaign_Query_Rule_Interval.CancelledDetect)/
                                          						Campaign_Query_Rule_Interval.ContactsAttempted

Problem

The percentage of calls attempted where the contact was dialed and one of the following problems was encountered:

Fax machine detected

No dial tone when dialer port went off hook

No Ringback from network when dial attempted

Network disconnected while alerting.

Low Energy ("or dead air") call detected by the dialer

Operator intercept (SIT Tone) was returned from network when dial attempted.

Derived
                                          						from: (Campaign_Query_Rule_Interval.FaxDetect +
                                          						Campaign_Query_Rule_Interval.NoDialToneDetect +
                                          						Campaign_Query_Rule_Interval.NoRingBackDetect +
                                          						Campaign_Query_Rule_Interval.SITToneDetect)/
                                          						Campaign_Query_Rule_Interval.ContactsAttempted

Did Not
                                             						Dial

Agent Rejected

The
                                          						number of preview or callback calls that were rejected
                                          						by the agent. (An attempt should be made to contact these customers again.)

Derived
                                          						from: Campaign_Query_Rule_Interval.AgentRejectedDetect

These
                                          						calls are not counted as attempted.

Agent Closed

The
                                          						number of preview or callback calls that were rejected by the agent. (The agent did not call these customers.)

Derived
                                          						from: Campaign_Query_Rule_Interval.AgentClosedDetect

These
                                          						calls are not counted as attempted.

## Campaign
                        	 Consolidated Daily

This report shows
                              		  the daily activity and performance of the selected campaigns and their skill
                              		  groups for the selected time period and provides analysis of the actual
                              		  customer calls (outbound calls which reached live voice, inbound calls, or
                              		  calls transferred to the campaign's skill group) for the selected campaigns and
                              		  their skill groups for the selected time period.

Views: This report has the following grid views:

Campaign Consolidated Daily (the default)

Campaign Consolidated Detailed Daily

Select the view you want to see from the report drop-down list that is located on the top left corner.

Query: This report data
                              		  is built from an Anonymous type query.

Value List: Campaigns

Database Schema Tables from which data is retrieved:

Campaign

Campaign_Query_Rule_Interval

Skill_Group_Interval

### Current Fields
                              		  in the Campaign Consolidated Daily Report View

Current fields are those fields that appear by default in a report that is generated from the stock template.

Columns
                                          						(Fields)

Description

Campaign

The name
                                          						of the campaign.

Derived
                                          						from: Campaign.CampaignName

Date

The date for the record in MM/DD/YYYY (month, day, year) format.

Derived from: Campaign_Query_Rule_Interval.DateTime

Agent
                                             						Time In Campaign

FTE

The FTE
                                          						value for the agents logged in and skilled for the campaign and not working in
                                          						other skill groups (or not ready). If all agents spend full-time on the
                                          						campaign's skill, the FTE is the number of agents.

Derived
                                          						from: (Skill_Group_Interval.LoggedOnTime - Skill_Group_Interval.BusyOtherTime -
                                          						Skill_Group_Interval.NotReadyTime)/ Skill_Group_Interval.ReportingInterval

Talk

The
                                          						percentage of time that agents spent talking in one of the campaign's skill
                                          						groups.

Derived
                                          						from: (Skill_Group_Interval.TalkTime - Skill_Group_Interval.TalkReserveTime)/
                                          						(Skill_Group_Interval.LoggedOnTime - Skill_Group_Interval. BusyOtherTime -
                                          						Skill_Group_Interval.NotReadyTime)

Wrap Up

The
                                          						percentage of time that agents have spent in Wrap-up state after incoming or
                                          						outgoing calls in one of the campaign's skill groups.

Derived
                                          						from: (Skill_Group_Interval.WorkReadyTime +
                                          						Skill_Group_Interval.WorkNotReadyTime)/ (Skill_Group_Interval.LoggedOnTime-
                                          						Skill_Group_Interval. BusyOtherTime - Skill_Group_Interval.NotReadyTime)

Idle

The
                                          						percentage of time the agents were available in one of the campaign's skill groups; but not working.

Derived
                                          						from: (Skill_Group_Interval.ReservedStateTime +
                                          						Skill_Group_Interval.TalkReserveTime + Skill_Group_Interval.AvailTime)/
                                          						(Skill_Group_Interval.LoggedOnTime- Skill_Group_Interval. BusyOtherTime -
                                          						Skill_Group_Interval.NotReadyTime)

Account Statistics

Connects/ FTE Agent Hour

The FTE
                                          						value for the number of calls of agents for the campaign's skill groups.

Derived
                                          						from: (Skill_Group_Interval.AutoOutCalls + Skill_Group_Interval.CallsHandled +
                                          						Skill_Group_Interval. PreviewCalls) * Skill_Group_Interval.ReportingInterval/
                                          						(Skill_Group_Interval.LoggedOnTime - Skill_Group_Interval.BusyOtherTime -
                                          						Skill_Group_Interval.NotReadyTime, 0)

Time between Agent Connects

The
                                          						average time in seconds between the connecting customer calls to the agents.

Derived
                                          						from: (Skill_Group_Interval.ReservedStateTime +
                                          						Skill_Group_Interval.TalkReserveTime + Skill_Group_Interval.AvailTime)/
                                          						(Skill_Group_Interval.AutoOutCalls + Skill_Group_Interval.CallsHandled +
                                          						Skill_Group_Interval. PreviewCalls)

The Summary Avg for Time between Agent Connects is calculated using the following formula: Summary Avg for a selected campaign
                                          = idle time/ agent connects.

Completed

Agent Connects

The
                                          						number of calls (outbound and inbound) handled per agent for the campaign's
                                          						skill groups.

Derived
                                          						from: (Skill_Group_Interval.AutoOutCalls + Skill_Group_Interval.CallsHandled +
                                          						Skill_Group_Interval. PreviewCalls)

Not Connected

The number of customer calls that were not connected to any agent or device. This includes calls which were abandoned by the
                                          dialer or abandoned to IVR (includes inbound and outbound calls) and resulted in customer abandon in queue or routing script
                                          error.

Derived
                                          						from: Skill_Group_Interval.RouterCallsAbandQ + Skill_Group_Interval.RouterError
                                          						+ Campaign_Query_Rule_Interval.CustomerAbandonDetect +
                                          						Campaign_Query_Rule_Interval.AbandonDetect

Note:
                                          						This column is invalid if the Outbound Reservation Script does not use
                                          						ReleaseCall when not reserving an agent. This results in extraneous Router Error call reports, which inflate the value
                                          in this column.

Dialer Abandon To Other

The number of calls which are in "abandon to IVR" state and have completed in a way that is not associated with a skill group
                                          in this campaign. This value only applies to Campaigns where the skill groups associated with the campaign are not used for
                                          inbound.

Derived
                                          						from: Campaign_Query_Rule_Interval.AbandonToIVR -
                                          						(Skill_Group_Interval.RouterCallsAbandQ + Skill_Group_Interval.CallsHandled +
                                          						Skill_Group_Interval.RouterError)

Note:
                                          						This column is approximate because the abandon to IVR can occur in one half
                                          						hour interval and the call completion occurs in another.

This column is invalid if the Outbound Reservation Script does not use ReleaseCall when not reserving an agent, which results
                                          in undercounting in this column.

This
                                          						column is invalid if the skill group is used for anything other than outbound
                                          						agent campaigns, for example inbound or transferred calls, as this results in
                                          						undercounting in this column.

This
                                          						column is invalid if the abandon to IVR script queues to multiple skill groups
                                          						in this campaign because RouterErrors and RouterCallsAbandQ are counted once in
                                          						each skill group the call was queued to, which results in undercounting in this
                                          						column.

Outbound
                                             						Statistics

Average Handle Time

The
                                          						average length of calls (Inbound and Outbound) handled by the agent during the
                                          						campaign's skill group selected interval.

Derived
                                          						from: (Skill_Group_Interval.TalkTime - Skill_Group_Interval.TalkReserveTime +
                                          						Skill_Group_Interval.WorkReadyTime + Skill_Group_Interval.WorkNotReadyTime)/
                                          						(Skill_Group_Interval.AutoOutCalls + Skill_Group_Interval.CallsHandled +
                                          						Skill_Group_Interval. PreviewCalls)

% Abandon

The
                                          						percentage of calls that reached a live voice and were abandoned by the dialer
                                          						or abandon to IVR because no agent was available.

Derived from: (Campaign_Query_Rule_Interval.AbandonDetect +
                                          						Campaign_Query_Rule_Interval.AbandonToIVR)/
                                          						(Campaign_Query_Rule_Interval.VoiceDetect +
                                          						Campaign_Query_Rule_Interval.WrongNumberCount +
                                          						Campaign_Query_Rule_Interval.CustomerNotHomeCount +
                                          						Campaign_Query_Rule_Interval.CustomerAbandonDetect +
                                          						Campaign_Query_Rule_Interval.CallbackCount +
                                          						Campaign_Query_Rule_Interval.PersonalCallbackCount +
                                          						Campaign_Query_Rule_Interval.AbandonDetect +
                                          						Campaign_Query_Rule_Interval.AbandonToIVR)

Hit Rate

The
                                          						percentage % of the outbound calls (attempts) that reached a live voice.

Derived
                                          						from: (Campaign_Query_Rule_Interval.VoiceDetect +
                                          						Campaign_Query_Rule_Interval.WrongNumberCount +
                                          						Campaign_Query_Rule_Interval.CustomerNotHomeCount +
                                          						Campaign_Query_Rule_Interval.CustomerAbandonDetect +
                                          						Campaign_Query_Rule_Interval.CallbackCount +
                                          						Campaign_Query_Rule_Interval.PersonalCallbackCount +
                                          						Campaign_Query_Rule_Interval.AbandonDetect +
                                          						Campaign_Query_Rule_Interval.AbandonToIVR)/
                                          						Campaign_Query_Rule_Interval.ContactsAttempted

Attempts

The
                                          						Total number of outbound calls attempted.

Derived
                                          						from: Campaign_Query_Rule_Interval.ContactsAttempted

### Current
                              		  Fields in the Campaign Consolidated Detailed Daily Report View

Current fields are those fields that appear by default in a report that is generated from the stock template.

Campaign

The
                                          						name of the campaign.

Derived from: Campaign.CampaignName

Date

The
                                          						date for the row's data in MM/DD/YYYY (month, day, year) format.

Derived from: Campaign_Query_Rule_Interval.DateTime

Agent
                                             						Connects

Outbound Immediate

The number of outbound calls where the customer was connected to an agent immediately (without waiting in the queue).

Derived from: Skill_Group_Interval.AutoOutCalls +
                                          						Skill_Group_Interval.PreviewCalls

After Abandon To IVR & Inbound

This field includes the following calls:

Outbound calls that were handled by an agent in this skill group after Abandon To IVR.

Outbound calls from a Transfer to IVR campaign that were queued back to agents.

Inbound and transferred calls that were routed to agents in this skill group.

Derived from: Skill_Group_Interval. CallsHandled

Not
                                             						Connected

Customer Abandon

The number of contacts when the customer ended the call immediately after picking up the phone.

Derived from: Campaign_Query_Rule_Interval.CustomerAbandonDetect

Dialer Abandon

The
                                          						number of contacts abandoned by the dialer.

Derived from:Campaign_Query_Rule_Interval.AbandonDetect

Customer Abandon in Queue

The number of contacts when the customer ended the call while in queue.

Derived from:Skill_Group_Interval.RouterCallsAbandQ

Script Error

The
                                          						number of calls that resulted in an error condition in the call routing script.

Derived from:Skill_Group_Interval.RouterError

Dialer
                                             						Abandon To Other

Script Dequeued

The
                                          						number of calls that were initially abandoned to IVR because no agent was
                                          						available and then queued to a skill group for this campaign and again removed
                                          						from the queue during the interval.

Derived from: Skill_Group_Interval.RouterCallsDequeued

The
                                          						number of calls that were routed to another skill group or never made it to the
                                          						skill group. This column is approximate because the abandon to IVR can occur
                                          						in one half hour interval and the call completion occurs in another interval.

This
                                          						column is approximate because the abandon to IVR can occur in one interval
                                          						and the call completion occurs in another interval.

## Campaign
                        	 Consolidated Half Hour

The Campaign Consolidated Half Hour report shows the list of Consolidated Calls and Agent Statistics per Campaign by Half
                              Hour and Breakdown of completed calls.

Views: This report has the following grid views:

Campaign Consolidated Half Hour (the default)

Campaign Consolidated Detailed Half Hour

Select the view you want to see from the report drop-down list that is located on the top left corner.

Query: This report data
                              		  is built from an Anonymous type query.

Value List: Campaigns

Database Schema Tables from which data is retrieved:

Campaign

Campaign_Query_Rule_Interval

Skill_Group_Interval

### Current Fields
                              		  in the Campaign Consolidated Half Hour Report View

Current fields are those fields that appear by default in a report generated from the stock template.

Columns
                                          						(Fields)

Description

Campaign

The name
                                          						of the campaign.

Derived
                                          						from: Campaign.CampaignName

DateTime

The date
                                          						and time at the start of the half-hour interval for the row's data in
                                          						MM/DD/YYYY (month, day, year) and HH:MM:SS (hours, minutes, seconds) format.

Derived
                                          						from: Campaign_Query_Rule_Interval.DateTime

Agent
                                             						Time In Campaign

FTE

The Full Time Equivalent (FTE)
                                          						value for the agents logged in and skilled for the campaign and not working in
                                          						other skill groups (or not ready) in the half-hour interval. If all agents
                                          						spend full-time on the campaign's skill during the half hour interval, the FTE
                                          						is the number of agents.

Derived
                                          						from: (Skill_Group_Interval.LoggedOnTime -
                                          						Skill_Group_Interval.BusyOtherTime -
                                          						Skill_Group_Interval.NotReadyTime)/ Skill_Group_Interval.ReportingInterval

Talk

The percentage of time that agents spent talking in one of the campaign's skill groups.

(Skill_Group_Interval.TalkTime - Skill_Group_Interval.TalkReserveTime)/ (Skill_Group_Interval.LoggedOnTime - Skill_Group_Interval.
                                          BusyOtherTime - Skill_Group_Interval.NotReadyTime)

Wrap Up

The
                                          						percentage of time that agents have spent in Wrap-up state after incoming or
                                          						outgoing calls in one of the campaign's skill groups.

Derived
                                          						from: (Skill_Group_Interval.WorkReadyTime +
                                          						Skill_Group_Interval.WorkNotReadyTime)/
                                          						(Skill_Group_Interval.LoggedOnTime- Skill_Group_Interval.
                                          						BusyOtherTime - Skill_Group_Interval.NotReadyTime)

Idle

The
                                          						percentage of time the agents were available in one of the Campaign's skill
                                          						groups but not working.

Derived
                                          						from: (Skill_Group_Interval.ReservedStateTime +
                                          						Skill_Group_Interval.TalkReserveTime +
                                          						Skill_Group_Interval.AvailTime)/
                                          						(Skill_Group_Interval.LoggedOnTime- Skill_Group_Interval.
                                          						BusyOtherTime - Skill_Group_Interval.NotReadyTime)

Agent Statistics

Connects/ FTE Agent Hour

The FTE value for the number of calls of agents in the interval for the campaign's skill groups.

Derived
                                          						from: (Skill_Group_Interval.AutoOutCalls +
                                          						Skill_Group_Interval.CallsHandled + Skill_Group_Interval.
                                          						PreviewCalls) *  Skill_Group_Interval.ReportingInterval/ (Skill_Group_Interval.LoggedOnTime -
                                          						Skill_Group_Interval.BusyOtherTime -
                                          						Skill_Group_Interval.NotReadyTime, 0)

Time between Agent Connects

The
                                          						average time in seconds between the connecting customer calls to the agents.

Derived
                                          						from: (Skill_Group_Interval.ReservedStateTime +
                                          						Skill_Group_Interval.TalkReserveTime +
                                          						Skill_Group_Interval.AvailTime)/
                                          						(Skill_Group_Interval.AutoOutCalls +
                                          						Skill_Group_Interval.CallsHandled + Skill_Group_Interval.
                                          						PreviewCalls)

The
                                          						Summary Avg for Time between Agent Connects is calculated using the following
                                          						formula: Summary Avg for a selected campaign = idle time/ agent connects

Completed

Agent Connects

The
                                          						number of calls (outbound and inbound) handled per agent for the campaign's
                                          						skill groups.

Derived
                                          						from: (Skill_Group_Interval.AutoOutCalls +
                                          						Skill_Group_Interval.CallsHandled + Skill_Group_Interval.
                                          						PreviewCalls)

Not Connected

The
                                          						number of customer calls that were not connected to any agent or device. This
                                          						includes calls which were abandoned by the dialer or abandoned to IVR (includes
                                          						inbound and outbound calls) and resulted in customer abandon in queue or
                                          						routing script error.

Derived from: Skill_Group_Interval.RouterCallsAbandQ +
                                          						Skill_Group_Interval.RouterError +
                                          						Campaign_Query_Rule_Interval.CustomerAbandonDetect +
                                          						Campaign_Query_Rule_Interval.AbandonDetect

Note:
                                          						This column is invalid if the Outbound Reservation Script does not use
                                          						ReleaseCall when not reserving an agent, which results in extraneous Router
                                          						Error call reports that inflates the value in this column.

Dialer Abandon To Other

The
                                          						number of calls that are in "abandon to IVR" state and have completed in a way
                                          						not associated with a skill group in this campaign. This value applies only to
                                          						Campaigns where the skill groups associated with the campaign are not used for
                                          						inbound.

Derived
                                          						from: Campaign_Query_Rule_Interval.AbandonToIVR -
                                          						(Skill_Group_Interval.RouterCallsAbandQ +
                                          						Skill_Group_Interval.CallsHandled +
                                          						Skill_Group_Interval.RouterError)

Note:
                                          						This column is approximate because the abandon to IVR can occur in one half-hour interval and the call completion occurs
                                          in another.

This
                                          						column is invalid if the Outbound Reservation Script does not use ReleaseCall
                                          						when not reserving an agent, which results in under counting in this column.

This
                                          						column is invalid if the skill group is used for anything other than outbound
                                          						agent campaigns, for example, inbound or transferred calls, as this results in
                                          						undercounting in this column.

This
                                          						column is invalid if the abandon to IVR script queues to multiple skill groups
                                          						in this campaign because RouterErrors and RouterCallsAbandQ are
                                          						counted once in each skill group the call was queued to, which results in
                                          						undercounting in this column.

Outbound Statistics

Avg Handle Time

The
                                          						average length of calls (Inbound and Outbound) handled by the agent during the
                                          						campaign's skill group selected interval.

Derived
                                          						from: (Skill_Group_Interval.TalkTime -
                                          						Skill_Group_Interval.TalkReserveTime +
                                          						Skill_Group_Interval.WorkReadyTime +
                                          						Skill_Group_Interval.WorkNotReadyTime)/
                                          						(Skill_Group_Interval.AutoOutCalls +
                                          						Skill_Group_Interval.CallsHandled + Skill_Group_Interval.
                                          						PreviewCalls)

% Abandon

The
                                          						percentage of calls that reached a live voice and were abandoned by the dialer
                                          						or abandon to IVR because no agent was available.

Derived
                                          						from: (Campaign_Query_Rule_Interval.AbandonDetect +
                                          						Campaign_Query_Rule_Interval.AbandonToIVR)/
                                          						(Campaign_Query_Rule_Interval.VoiceDetect +
                                          						Campaign_Query_Rule_Interval.WrongNumberCount +
                                          						Campaign_Query_Rule_Interval.CustomerNotHomeCount +
                                          						Campaign_Query_Rule_Interval.CustomerAbandonDetect +
                                          						Campaign_Query_Rule_Interval.CallbackCount +
                                          						Campaign_Query_Rule_Interval.PersonalCallbackCount +
                                          						Campaign_Query_Rule_Interval.AbandonDetect +
                                          						Campaign_Query_Rule_Interval.AbandonToIVR)

Hit Rate

The
                                          						percentage of the outbound calls (attempts) that reached a live voice.

Derived
                                          						from: (Campaign_Query_Rule_Interval.VoiceDetect +
                                          						Campaign_Query_Rule_Interval.WrongNumberCount +
                                          						Campaign_Query_Rule_Interval.CustomerNotHomeCount +
                                          						Campaign_Query_Rule_Interval.CustomerAbandonDetect +
                                          						Campaign_Query_Rule_Interval.CallbackCount +
                                          						Campaign_Query_Rule_Interval.PersonalCallbackCount +
                                          						Campaign_Query_Rule_Interval.AbandonDetect +
                                          						Campaign_Query_Rule_Interval.AbandonToIVR)/
                                          						Campaign_Query_Rule_Interval.ContactsAttempted

Attempts

The
                                          						total number of outbound calls attempted.

Derived
                                          						from: Campaign_Query_Rule_Interval.ContactsAttempted

### Current Fields
                              		  in the Campaign Consolidated Detailed Half Hour Report View

Current fields are those fields that appear by default in a report generated from the stock template.

Columns
                                          						(Fields)

Description

Campaign

The name
                                          						of the campaign.

Derived
                                          						from: Campaign.CampaignName

DateTime

The date
                                          						and time at the start of the half-hour interval for the row's data in
                                          						MM/DD/YYYY (month, day, year) and HH:MM:SS (hours, minutes, seconds) format.

Derived
                                          						from: Campaign_Query_Rule_Interval.DateTime

Agent
                                             						Connects

Outbound Immediate

The
                                          						number of outbound calls where the customer was connected to an agent
                                          						immediately (without waiting in queue).

Derived from: Skill_Group_Interval.AutoOutCalls +
                                          						Skill_Group_Interval.PreviewCalls

After Abandon To IVR & Inbound

This
                                          						includes the following calls:

Outbound calls that were handled by an agent in this skill group after Abandon To IVR.

Inbound and transferred calls that were routed to agents in this skill group.

Outbound calls from a Transfer to IVR campaign that were queued back to agents.

Derived from: Skill_Group_Interval. CallsHandled

Not
                                             						Connected

Customer Abandon

The number of contacts in the half-hour interval where the customer ended the call immediately after picking up the phone.

Derived from:
                                          						Campaign_Query_Rule_Interval.CustomerAbandonDetect

Dialer Abandon

The
                                          						number of contacts in the half-hour interval abandoned by the dialer.

Derived from:Campaign_Query_Rule_Interval.AbandonDetect

Customer Abandon in Queue

The number of contacts in the half-hour interval where the customer ended the call while in queue.

Derived from:Skill_Group_Interval.RouterCallsAbandQ

Script Error

The
                                          						number of calls that resulted in an error condition in the call routing script.

Derived from:Skill_Group_Interval.RouterError

Dialer
                                             						Abandon To Other

Script Dequeued

The
                                          						number of calls that were initially abandoned to IVR because no agent was
                                          						available and then queued to a skill group for this campaign and again removed
                                          						from the queue during the half-hour interval.

Derived from: Skill_Group_Interval.RouterCallsDequeued

Other

The
                                          						number of calls that were routed to another skill group or never made to the
                                          						skill group.

Derived from:Campaign_Query_Rule_Interval.AbandonToIVR -
                                          						(Skill_Group_Interval.RouterCallsAbandQ +
                                          						Skill_Group_Interval.CallsHandled +
                                          						Skill_Group_Interval.RouterError + Skill_Group_Interval.
                                          						RouterCallsDequeued)

This
                                          						column is approximate because the abandon to IVR can occur in one half-hour
                                          						interval and the call completion occurs in another interval.

## Campaign Half Hour
                        	 Summary

The Campaign Half Hour Summary report shows
                              		  the status for all campaigns for the selected time period, the status (summary
                              		  and percentage) of each campaign for the selected time period, and the breakdown
                              		  of attempts (in percentage) of each campaign for the selected time period.

Views: This report has the following grid views:

Breakdown of Attempts per Campaign Half Hour (the default)

Summary of Attempts per Campaign Half Hour

Summary of Call Counts per Campaign Half Hour

Select the view you want to see from the report drop-down list that is located on the top left corner.

Query: This report data
                              		  is built from an Anonymous type query.

Value List: Campaigns

Database Schema Tables from which data is retrieved:

Campaign

Campaign_Query_Rule_Interval

### Current Fields
                              		  in the Breakdown of Attempts (%) Per Campaign Half Hour Report View

Current fields are those fields that appear by default in a report generated from the stock template.

Columns
                                          						(Fields)

Description

Campaign

The name
                                          						of the campaign.

Derived
                                          						from: Campaign.CampaignName

DateTime

The date
                                          						and time at the start of a half-hour interval for the row's data in MM/DD/YYYY
                                          						(month, day, year) and HH:MM:SS (hours, minutes, seconds) format.

Derived
                                          						from: Campaign_Query_Rule_Interval.DateTime

Attempts

The total number of outbound calls attempted.

Derived from: Campaign_Query_Rule_Interval.ContactsAttempted

Customer
                                             						Answered

Right Party Connect

The percentage of call attempts when the
                                          						actual customer was contacted and handled,  as indicated by agents using their desktop.

Derived from: Campaign_Query_Rule_Interval. VoiceDetect/Campaign_Query_Rule_Interval.ContactsAttempted

Dialer Abandon

The percentage of contacts or attempts in the half-hour interval abandoned by the dialer because agents were not available
                                          and there was no configuration in place for "Abandon to IVR".

Derived
                                          						from: Campaign_Query_Rule_Interval. AbandonDetect/
                                          						Campaign_Query_Rule_Interval.ContactsAttempted

Abandon to IVR

The percentage of attempts that reached a customer and were abandoned to IVR because no agents were available to handle the
                                          call.

Derived
                                          						from: Campaign_Query_Rule_Interval.AbandonToIVR/
                                          						Campaign_Query_Rule_Interval.ContactsAttempted

Callback

The percentage of call backs requested by the customer when the campaign is not
                                          						configured for personal callback.

Derived
                                          						from: Campaign_Query_Rule_Interval.CallbackCount/
                                          						Campaign_Query_Rule_Interval.ContactsAttempted

Personal Callback

The percentage of call backs scheduled and requested by the customer when the campaign
                                          						is configured for personal callback.

Derived
                                          						from: Campaign_Query_Rule_Interval.PersonalCallbackCount/
                                          						Campaign_Query_Rule_Interval.ContactsAttempted

Customer Not Home

The percentage of contacts in the half-hour interval when the party answering the phone was not the customer.

Derived
                                          						from: Campaign_Query_Rule_Interval.CustomerNotHomeCount/
                                          						Campaign_Query_Rule_Interval.ContactsAttempted

Wrong Number

The percentage of contacts in the half-hour interval when the party answering the phone indicated that the customer did not
                                          live there.

Derived
                                          						from: Campaign_Query_Rule_Interval.WrongNumberCount/
                                          						Campaign_Query_Rule_Interval.ContactsAttempted

Customer Abandon

The percentage of contacts in the half-hour interval where the customer ended the call immediately after being connected to
                                          an agent.

Derived
                                          						from: Campaign_Query_Rule_Interval.
                                          						CustomerAbandonDetect/Campaign_Query_Rule_Interval.ContactsAttempted

Customer
                                             						Did Not Answer

Answering Machine

The percentage of contacts in the half-hour interval that detected an answering
                                          						machine.

Derived
                                          						from: Campaign_Query_Rule_Interval.
                                          						AnsweringMachineDetect/Campaign_Query_Rule_Interval.ContactsAttempted

No Answer

The percentage of contacts in the half-hour interval that were not answered.

Derived
                                          						from: Campaign_Query_Rule_Interval.
                                          						NoAnswerDetect/Campaign_Query_Rule_Interval.ContactsAttempted

Busy

The percentage of contacts in the half-hour interval that detected a busy signal.

Derived from: Campaign_Query_Rule_Interval. BusyDetect/
                                          						Campaign_Query_Rule_Interval.ContactsAttempted

Canceled

The percentage of contacts in the half-hour interval where the dialer canceled a
                                          						ringing customer call.

Derived from: Campaign_Query_Rule_Interval.CanceledDetect /Campaign_Query_Rule_Interval.ContactsAttempted

Problem

SIT Tone

The
                                          						number of contacts in the half-hour interval that detected a Special
                                          						Information Tone (SIT).

Derived from: Campaign_Query_Rule_Interval.SITToneDetect

No Dial tone

The
                                          						number of contacts in the half-hour interval that did not detect a dial tone.

Derived from:
                                          						Campaign_Query_Rule_Interval.NoDialToneDetect

Fax

The
                                          						number of contacts in the half-hour interval that detected a fax.

Derived from: Campaign_Query_Rule_Interval.FaxDetect

Network Error

The number of contacts that encountered one of the following problems:

No Ringback from network when dial attempted.

Network disconnected while alerting.

Low Energy ("or dead air") call detected by the dialer.

Derived from:
                                          						Campaign_Query_Rule_Interval.NoRingBackDetect

### Current
                              		  Fields in the Summary of Attempts Per Campaign Half Hour Report View

Columns (Fields)

Description

Campaign

The
                                          						name of the campaign.

Derived from: Campaign.CampaignName

DateTime

The
                                          						date and time of the start half hour interval for the row's data in MM/DD/YYYY
                                          						(month, day, year) and HH:MM:SS (hours, minutes, seconds) format.

Derived from: Campaign_Query_Rule_Interval.DateTime

Key
                                             						Statistics

Customer Answered

The
                                          						number of the outbound calls (attempts) that reached a live voice.

Derived from: Cam paign_Query_Rule_Interval.VoiceDetect +
                                          						Campaign_Query_Rule_Interval.WrongNumberCount +
                                          						Campaign_Query_Rule_Interval.CustomerNotHomeCount +
                                          						Campaign_Query_Rule_Interval.CustomerAbandonDetect +
                                          						Campaign_Query_Rule_Interval.CallbackCount +
                                          						Campaign_Query_Rule_Interval.PersonalCallbackCount +
                                          						Campaign_Query_Rule_Interval.AbandonDetect +
                                          						Campaign_Query_Rule_Interval.AbandonToIVR

Right Party Connect

The
                                          						number of call attempts as indicated by agents using their desktop, when
                                          						the actual customer was contacted and handled.

Derived from: Campaign_Query_Rule_Interval.VoiceDetect

Dialer Abandon & Abandon to IVR

The
                                          						number of calls that were abandoned by the dialer or abandoned to IVR because
                                          						of there were no agents available to take the call. Campaign configuration
                                          						determines whether these calls are abandoned at the dialer or to IVR.

Derived from: Campaign_Query_Rule_Interval. AbandonToIVR
                                          						+ Campaign_Query_Rule_Interval. AbandonDetect

Attempts

Total

The
                                          						total number of outbound calls attempted.

Derived from:
                                          						Campaign_Query_Rule_Interval.ContactsAttempted

Customer Answered

The
                                          						percentage of attempted calls that reached a live voice.

Derived from: (Campaign_Query_Rule_Interval.VoiceDetect +
                                          						Campaign_Query_Rule_Interval.WrongNumberCount +
                                          						Campaign_Query_Rule_Interval.CustomerNotHomeCount +
                                          						Campaign_Query_Rule_Interval.CustomerAbandonDetect +
                                          						Campaign_Query_Rule_Interval.CallbackCount +
                                          						Campaign_Query_Rule_Interval.PersonalCallbackCount +
                                          						Campaign_Query_Rule_Interval.AbandonDetect +
                                          						Campaign_Query_Rule_Interval.AbandonToIVR)/
                                          						Campaign_Query_Rule_Interval.ContactsAttempted

Did Not Answer

The
                                          						percentage of calls attempted when the number was dialed but the customer was
                                          						not reached and there were no problems with the call ("Ring No Answer").

Derived from:
                                          						(Campaign_Query_Rule_Interval.AnsweringMachineDetect +
                                          						Campaign_Query_Rule_Interval.BusyDetect +
                                          						Campaign_Query_Rule_Interval.NoAnswerDetect +
                                          						Campaign_Query_Rule_Interval.CancelledDetect/
                                          						Campaign_Query_Rule_Interval.ContactsAttempted

Problem

The percentage of calls attempted where the contact was dialed and one of the following problems was encountered:

Fax machine detected.

No dial tone when dialer port went off hook.

No Ringback from network when dial attempted.

Network disconnected while alerting.

Low Energy ("or dead air") call detected by the dialer.

Operator intercept (SIT Tone) was returned from network when dial attempted.

Derived from: (Campaign_Query_Rule_Interval.FaxDetect +
                                          						Campaign_Query_Rule_Interval.NoDialToneDetect +
                                          						Campaign_Query_Rule_Interval.NoRingBackDetect +
                                          						Campaign_Query_Rule_Interval.SITToneDetect)/
                                          						Campaign_Query_Rule_Interval.ContactsAttempted

Did
                                             						Not Dial

Agent Rejected

The number of preview or callback calls in the half-hour interval rejected by the agent.

Derived from:
                                          						Campaign_Query_Rule_Interval.AgentRejectedDetect

Note: These calls are not counted as attempted.

Agent Closed

The number of preview or callback calls rejected by the agent. These customers are not dialed.

Derived from:
                                          						Campaign_Query_Rule_Interval.AgentClosedDetect

Note:
                                          						These calls are not counted as attempted.

### Current
                              		  Fields in the Summary of Call Counts Per Campaign Half Hour Report View

Current fields are those fields that appear by default in a report that is generated from the stock template.

Columns (Fields)

Description

Campaign

The
                                          						name of the campaign.

Derived from: Campaign.CampaignName

DateTime

The
                                          						central controller date and time at the start of the half-hour interval.

Derived from: Campaign_Query_Rule_Interval.DateTime

Attempts

Summary total of the number of calls attempted in the half-hour
                                          						interval.

Derived from:
                                          						Campaign_Query_Rule_Interval.ContactsAttempted

Requested Callback

The
                                          						number of callback contacts.

Derived from: Campaign_Query_Rule_Interval.CallBackCount

Requested Personal Callback

The
                                          						number of callback contacts scheduled.

Derived from:
                                          						Campaign_Query_Rule_Interval.PersonalCallBackCount

Voice

The
                                          						number of contacts for which a voice was detected in the half hour interval.

Derived from: Campaign_Query_Rule_Interval.VoiceDetect

Busy

The
                                          						number of contacts in the half hour interval that detected a busy signal.

Derived from: Campaign_Query_Rule_Interval.BusyDetect

No
                                          						Answer

The
                                          						number of contacts in the half hour interval that were not answered.

Derived from: Campaign_Query_Rule_Interval.NoAnswerDetect

No
                                          						Ringback

The
                                          						number of contacts in the half hour interval that did not detect a ring back.
                                          						The Calls with CallResults 4, 27 and 28 are mentioned in this column.

Derived from:
                                          						Campaign_Query_Rule_Interval.NoRingBackDetect

No
                                          						Dialtone

The
                                          						number of contacts in the half hour interval that did not detect a dial tone.

Derived from:
                                          						Campaign_Query_Rule_Interval.NoDialToneDetect

Fax

The
                                          						number of contacts in the half hour interval that detected a fax.

Derived from: Campaign_Query_Rule_Interval.FaxDetect

Network IVR

The
                                          						number of contacts in the half hour interval that detected a network answering
                                          						machine.

Derived from:
                                          						Campaign_Query_Rule_Interval.NetworkAnsMachineDetect

Answering Machine

The
                                          						number of contacts in the half hour interval that detected an answering
                                          						machine.

Derived from:
                                          						Campaign_Query_Rule_Interval.AnsweringMachineDetect

SIT
                                          						Tone

The
                                          						number of contacts in the half hour interval that detected a special
                                          						information tone (SIT).

Derived from: Campaign_Query_Rule_Interval.SITToneDetect

Agent
                                          						Rejected

The
                                          						number of preview or callback contacts in the half hour interval that were
                                          						rejected by the agent.

Derived from:
                                          						Campaign_Query_Rule_Interval.AgentRejectedDetect

Agent
                                          						Closed

The
                                          						number of preview or callback contacts that were rejected by the agent. These
                                          						customers are not dialed.

Derived from:
                                          						Campaign_Query_Rule_Interval.AgentClosedDetect

Customer Not Home

The number of contacts in the half hour interval when the party answering the phone was not the customer.

Derived from:
                                          						Campaign_Query_Rule_Interval.CustomerNotHomeCount

Wrong
                                          						Number

The number of contacts in the half hour interval when the party answering the phone indicated that the customer did not live
                                          there.

Derived from:
                                          						Campaign_Query_Rule_Interval.WrongNumberCount

Canceled

The
                                          						number of contacts in the half hour interval where the dialer canceled a
                                          						ringing customer call.

Derived from: Campaign_Query_Rule_Interval.CanceledDetect

Dialer
                                          						Abandon

The
                                          						number of contacts in the half hour interval abandoned by the dialer.

Derived from: Campaign_Query_Rule_Interval.AbandonDetect

Abandon to IVR

The
                                          						number of contacts in the half hour interval that were abandoned by the dialer.
                                          						However, instead of hanging up on the customer, the customer was transferred to
                                          						an IVR which plays a message.

Derived from: Campaign_Query_Rule_Interval.AbandonToIVR

Customer Abandon

The number of contacts in the half hour interval where the customer ended the call immediately after picking up the phone.

Derived from:
                                          						Campaign_Query_Rule_Interval.CustomerAbandonDetect

Talk
                                          						Time

The
                                          						total time in HH:MM:SS (hours, minutes, seconds) that  agents spent talking on the phone in the half hour interval.

Derived from: Campaign_Query_Rule_Interval.TalkTime

Wrap Up
                                          						Time

The
                                          						length of time the agents spent in wrap-up work.

Derived from: Campaign_Query_Rule_Interval.WrapupTime

## Dialer Call Result Summary Half Hour

The Dialer Call Result Summary Half Hour report displays the status of each dialer for the selected time period.

Views: This report has one grid view, Dialer Call Result Summary Half Hour.

Query: This report data is built from an Anonymous type query.

Value List: Dialers

Database Schema Tables from which data is retrieved:

Dialer

Dialer_Interval

### Current Fields in the Dialer Call Result Summary Half Hour Report View

Current fields are those fields that appear by default in a report generated from the stock template.

Columns (Fields)

Description

Dialer

The name of the dialer.

Derived from: Dialer.DialerName

DateTime

The central controller date and time at the start of the half-hour interval.

Derived from: Dialer_Interval.DateTime

Attempts

Summary total of the number of contacts dialed in the half-hour interval.

Derived from: Dialer_Interval.ContactsDialed

Requested Callback

The number of callback contacts.

Derived from: Dialer_Interval.CallBackCount

Requested Personal Callback

The number of callback contacts scheduled.

Derived from: Dialer_Interval.PersonalCallBackCount

Voice

The number of contacts for which a voice was detected in the half-hour interval.

Derived from: Dialer_Interval.VoiceDetect

Busy

The number of contacts for which busy signals were detected in the half-hour interval.

Derived from: Dialer_Interval.BusyDetect

No Answer

The number of contacts which were not answered in the half hour-interval.

Derived from: Dialer_Interval.NoAnswerDetect

No Ringback

The number of contacts in the half-hour interval that did not detect a ring back.

Derived from: Dialer_Interval.NoRingBackDetect

No Dialtone

The number of contacts in the half-hour interval that did not detect a dial tone.

Derived from: Dialer_Interval.NoDialToneDetect

Fax

The number of contacts in the half-hour interval that detected a fax.

Derived from: Dialer_Interval.FaxDetect

Network IVR

The number of contacts in the half-hour interval that detected a network answering machine.

Derived from: Dialer_Interval.NetworkAnsMachineDetect

Answering Machine

The number of contacts in the half-hour interval that detected an answering machine.

Derived from: Dialer_Interval.AnsweringMachineDetect

SIT Tone

The number of contacts in the half-hour interval that detected a special information tone (SIT).

Derived from: Dialer_Interval.SITToneDetect

Agent Rejected

The number of preview or callback contacts in the half-hour interval that were rejected by the agent.

Derived from: Dialer_Interval.AgentRejectedDetect

Agent Closed

The number of preview or callback contacts that were rejected by the agent. The agent did not call these customers.

Derived from: Dialer_Interval.AgentClosedDetect

Customer Not Home

The number of contacts in a half-hour interval where the party answering the phone was not the customer.

Derived from: Dialer_Interval.CustomerNotHomeCount

Wrong Number

The number of contacts in a half-hour interval where the party answering the phone indicated that the customer did not live
                                          there.

Derived from: Dialer_Interval.WrongNumberCount

Canceled

The number of contacts in the half-hour interval where the dialer canceled a ringing customer call.

Derived from: Dialer_Interval.CancelledDetect

Dialer Abandon

The number of contacts in the half-hour interval abandoned by the dialer.

Derived from: Dialer_Interval.AbandonDetect

Abandon to IVR

The number of contacts in the half-hour interval that were abandoned by the dialer and transferred to IVR, which plays a message.

Derived from: Dialer_Interval.AbandonToIVR

Customer Abandon

The number of contacts in the half-hour interval where the customer ended the call immediately after picking up the phone.

Derived from: Dialer_Interval.CustomerAbandonDetect

## Dialer Capacity Daily

The Dialer Capacity Daily report displays the status of each dialer for the selected time period.

Views: This report has one grid view, Dialer Capacity Daily Report.

Query: This report data is built from an Anonymous type query.

Value List: Dialers

Database Schema Tables from which data is retrieved:

Dialer

Dialer_Interval

### Current Fields in the Dialer Capacity Daily Report View

Current fields are those fields that appear by default in a report generated from the stock template.

Columns (Fields)

Description

Dialer

The name of the dialer.

Derived from: Dialer.DialerName

Date

The date for the row's data in MM/DD/YYYY (month, day, year) format.

Derived from: Dialer_Interval.DateTime

Port Status

Ports in Service

The full-time equivalent value of registered dialer ports during the  interval. If this is less than the full number of ports
                                          allocated, then it describes a system issue where ports were offline for some time.

Derived from: (Dialer_Interval.IdlePortTime+Dialer_Interval.ReservePortTime + Dialer_Interval.DialingTime)/ Dialer_Interval.ReportingInterval

Idle

The percentage of nonbusy ports in the current interval.

Derived from: Dialer_Interval.IdlePortTime/ (Dialer_Interval.IdlePortTime + Dialer_Interval.ReservePortTime + Dialer_Interval.DialingTime)

Contacting Customers

The percentage of time spent by the dialer ports for calling customers during the current  interval.

Derived from: Dialer_Interval.DialingTime /(Dialer_Interval.IdlePortTime + Dialer_Interval.ReservePortTime + Dialer_Interval.DialingTime)

Reserved Agents

The percentage of time spent by the dialer ports for reserving agents during the current  interval for an agent campaign.

Derived from: Dialer_Interval.ReservePortTime/ (Dialer_Interval.IdlePortTime + Dialer_Interval.ReservePortTime + Dialer_Interval.DialingTime)

Out of Ports

The percentage of time maxed out by the dialer during the current interval.

Derived from: Dialer_Interval.AllPortsBusyTime/(Dialer_Interval.IdlePortTime + Dialer_Interval.ReservePortTime + Dialer_Interval.DialingTime)

Dialer Statistics

Attempts

The number of customer contact calls attempted by the dialer during the current  interval. This includes all attempts, whether
                                          customers were reached or not.

Derived from: Dialer_Interval.ContactsDialed

Avg Attempt Time

The average time length in seconds of a customer attempt.

Derived from: Dialer_Interval.DialingTime/Dialer_Interval.ContactsDialed

Reservation Calls

The total number of reservation calls placed. This includes dialer requests to reserve agents that were rejected in the routing
                                          script because no agents were available or otherwise.

Derived from: Dialer_Interval.ReservationCallAttempts

Avg Reservation Time

The average length of a reservation call in seconds.

Derived from: Dialer_Interval.ReservePortTime/ Dialer_Interval.ReservationCallAttempts

## Dialer Capacity Half Hour

The Dialer Capacity Half Hour report displays the status of each dialer for the selected time period.

Views: This report has one grid view, Dialer Capacity Half Hour Report.

Query: This report data is built from an Anonymous type query.

Value List: Dialers

Database Schema Tables from which data is retrieved:

Dialer

Dialer_Interval

### Current Fields in the Dialer Capacity Half Hour Report View

Current fields are those fields that appear by default in a report generated from the stock template.

Columns (Fields)

Description

Dialer

The name of the dialer.

Derived from: Dialer.DialerName

DateTime

The date and time of the start of the half-hour interval for the row's data in MM/DD/YYYY (month, day, year) and HH:MM:SS
                                          (hour, minute, second) format.

Derived from: Dialer_Interval.DateTime

Port Status

Ports in Service

The full-time equivalent value of registered dialer ports during the half-hour interval. If this value is less than the full
                                          number of ports allocated, then it describes a system issue where ports were offline for some time.

Derived from: (Dialer_Interval.IdlePortTime+Dialer_Interval.ReservePortTime + Dialer_Interval.DialingTime)/ Dialer_Interval.ReportingInterval

Idle

The percentage of nonbusy ports in the current half-hour interval.

Derived from: Dialer_Interval.IdlePortTime/ (Dialer_Interval.IdlePortTime + Dialer_Interval.ReservePortTime + Dialer_Interval.DialingTime)

Contacting Customers

The percentage of time spent by the dialer ports for calling customers during the current half-hour interval.

Derived from: Dialer_Interval.DialingTime /(Dialer_Interval.IdlePortTime + Dialer_Interval.ReservePortTime + Dialer_Interval.DialingTime)

Reserved Agents

The percentage of time spent by the dialer ports for reserved agents during the current half-hour interval for an agent campaign.

Derived from: Dialer_Interval.ReservePortTime/ (Dialer_Interval.IdlePortTime + Dialer_Interval.ReservePortTime + Dialer_Interval.DialingTime)

Out of Ports

The percentage of time maxed out by the dialer during the current half-hour interval.

Derived from: Dialer_Interval.AllPortsBusyTime/(Dialer_Interval.IdlePortTime + Dialer_Interval.ReservePortTime + Dialer_Interval.DialingTime)

Dialer Statistics: Attempts

The number of customer contact calls attempted by the dialer during the current half-hour interval. This number includes all
                                          attempts, whether customers were reached or not.

Derived from: Dialer_Interval.ContactsDialed

Dialer Statistics

Attempts

The number of customer contact calls attempted by the dialer during the current  half-hour interval. This includes all attempts,
                                          whether customers were reached or not.

Derived from: Dialer_Interval.ContactsDialed

Avg Attempt Time

The average time length of a customer attempt in seconds.

Derived from: Dialer_Interval.DialingTime/Dialer_Interval.ContactsDialed

Reservation Calls

The total number of reservation calls placed the current half-hour interval. This number includes dialer requests to reserve
                                          agents that were rejected in the routing script because no agents were available or otherwise.

Derived from: Dialer_Interval.ReservationCallAttempts

Avg Reservation Calls

The average length of a reservation call in seconds.

Derived from: Dialer_Interval.ReservePortTime / Dialer_Interval.ReservationCallAttempts

## Import Rule

The Import Rule report displays the status of imported records for the selected time period.

Views: This report has one grid view, Import Rule Report.

Query: This report data is built from an Anonymous type query.

Value List: Import Rule

Database Schema Tables from which data is retrieved:

Import_Rule

Import_Rule_History

### Current Fields in the Import Rule Report View

Current fields are those fields that appear by default in a report generated from the stock template. You can change them.

Columns (Fields)

Description

Import

The name of the import rule.

Derived from: Import_Rule.ImportRuleName

Start Date

The date and time the import rule is scheduled to start.

Derived from: Import_Rule_History.StartDateTime

End Date

The date and time the import rule finished.

Derived from: Import_Rule_History.EndDateTime

Duration

The total time duration.

Derived from: DateDiff(ss,Import_Rule_History.StartDateTime, Import_Rule_History.EndDateTime)

Records Status

Total Records

The total number of records present in the import list.

Derived from: Import_Rule_History.TotalRecords

Imported

The total number of records imported into the Do Not Call List.

Derived from: Import_Rule_History.GoodRecords

Failed

The total number of import records that did not meet format criteria. These records are captured in an import error file.

Derived from: Import_Rule_History.BadRecords

Records To Dial

The total number of records imported to dialing lists based on existing query rules.

Derived from: Import_Rule_History. ImportedToDialingListCount

Records With Unknown Prefix

The total number of records that did not match the prefixes in the region prefix table and were assigned with the default
                                          time zone for the campaign.

Derived from: Import_Rule_History.UnmatchedRegionPrefixCount

## Query Rule Within
                        	 Campaign Daily

The Query Rule Within Campaign Daily report shows
                              		  the breakdown of attempts (in percentage) of each campaign for the selected
                              		  time period and the status (summary and percentage) of each campaign
                              		  for the selected time period.

Views: This report has the following grid views:

Breakdown of Attempts per Query Rule Daily (the default)

Attempts per Query Rule Within Campaign Daily.

Select the view you want to see from the report drop-down list that is located on the top left corner.

Query: This report data
                              		  is built from an Anonymous type query.

Value List: Campaigns

Database Schema Tables from which data is retrieved:

Campaign

Campaign_Query_Rule_Interval

Query_Rule

### Breakdown of Attempts  Per Query Rule Within Campaign Daily Report

Current fields are those fields that appear by default in a report generated from the stock template.

Columns
                                          						(Fields)

Description

Campaign

The name
                                          						of the campaign.

Derived
                                          						from: Campaign.CampaignName

Query
                                          						Rule

The name
                                          						of the query rule.

Derived
                                          						from: Query_Rule.QueryRuleName

Date

The date for the record in MM/DD/YYYY (month, day, year) format.

Derived from: Campaign_Query_Rule_Interval.DateTime

Attempts

The
                                          						total number of outbound calls attempted.

Derived
                                          						from: Campaign_Query_Rule_Interval.ContactsAttempted

Customer
                                             						Answered

Right Party Connect

The percentage of call attempts as indicated by agents using their desktop, when the
                                          						actual customer was contacted and handled.

Derived
                                          						from: Campaign_Query_Rule_Interval.VoiceDetect/
                                          						Campaign_Query_Rule_Interval.ContactsAttempted

Dialer Abandon

The percentage of contacts or attempts abandoned by the dialer
                                          						because of no agent was available to take the call and "Abandon to IVR" was not
                                          						configured.

Derived
                                          						from: Campaign_Query_Rule_Interval. AbandonDetect/
                                          						Campaign_Query_Rule_Interval.ContactsAttempted

Abandon to IVR

The
                                          						percentage of attempts that were sent to IVR (or another dialed number) for
                                          						treatment after the dialer reached a contact and no agent was available to take
                                          						the call.

Derived from: Campaign_Query_Rule_Interval. AbandonToIVR/
                                          						Campaign_Query_Rule_Interval.ContactsAttempted

Callback

The percentage of callbacks requested by the customer when the campaign is not
                                          						configured for personal callback.

Derived from: Campaign_Query_Rule_Interval.CallbackCount/
                                          						Campaign_Query_Rule_Interval.ContactsAttempted

Personal Callback

The percentage of callback scheduled and requested by the customer when the campaign
                                          						was configured for personal callback.

Derived from:
                                          						Campaign_Query_Rule_Interval.PersonalCallbackCount/
                                          						Campaign_Query_Rule_Interval.ContactsAttempted

Customer Not Home

The percentage of contacts where the party answering the
                                          						phone was not the customer.

Derived from:
                                          						Campaign_Query_Rule_Interval.CustomerNotHomeCount/
                                          						Campaign_Query_Rule_Interval.ContactsAttempted

Wrong Number

The percentage of contacts where the party answering the
                                          						phone indicated that the customer did not live there.

Derived from:
                                          						Campaign_Query_Rule_Interval.WrongNumberCount/
                                          						Campaign_Query_Rule_Interval.ContactsAttempted

Customer Abandon

The percentage of contacts where the customer ended the call immediately after being connected to an agent.

Derived from:
                                          						Campaign_Query_Rule_Interval.CustomerAbandonDetect/
                                          						Campaign_Query_Rule_Interval.ContactsAttempted

Customer Did Not Answer

Answering Machine

The percentage of contacts that detected an answering machine.

Derived from: Campaign_Query_Rule_Interval.AnsweringMachineDetect

No Answer

The percentage of contacts that were not answered.

Derived from: Campaign_Query_Rule_Interval.
                                          						NoAnswerDetect/ Campaign_Query_Rule_Interval.ContactsAttempted

Busy

The percentage of contacts that detected a busy signal.

Derived from: Campaign_Query_Rule_Interval. BusyDetect/
                                          						Campaign_Query_Rule_Interval.ContactsAttempted

Canceled

The percentage of contacts where the dialer canceled a
                                          						ringing customer call.

Derived from:
                                          						Campaign_Query_Rule_Interval.CanceledDetect/
                                          						Campaign_Query_Rule_Interval.ContactsAttempted

Problem

SIT Tone

The percentage of contacts that detected a Special
                                          						Information Tone (SIT).

Derived from: Campaign_Query_Rule_Interval.SITToneDetect

No Dial tone

The percentage of contacts that did not detect a dial tone.

Derived from:
                                          						Campaign_Query_Rule_Interval.NoDialToneDetect

Fax

The percentage of contacts that detected a fax machine.

Derived from: Campaign_Query_Rule_Interval.FaxDetect

Network Error

The number of contacts that encountered one of the following problems:

No Ringback from network when dial attempted.

Network disconnected while alerting.

Low Energy ("or dead air") call detected by the dialer.

Derived from:
                                          						Campaign_Query_Rule_Interval.NoRingBackDetect

### Attempts Per Query Rule Within Campaign Daily Report

Current fields are those fields that appear by default in a report generated from the stock template.

Columns
                                          						(Fields)

Description

Campaign

The name
                                          						of the campaign.

Derived
                                          						from: Campaign.CampaignName

Query
                                          						Rule

The name
                                          						of the query rule.

Derived
                                          						from: Query_Rule.QueryRuleName

Date

The date for the row's data in MM/DD/YYYY (month, day, year) format.

Derived
                                          						from: Campaign_Query_Rule_Interval.DateTime

Key
                                             						Statistics

Customer Answered

The
                                          						number of the outbound calls (attempts) that reached a live voice.

Derived
                                          						from: Campaign_Query_Rule_Interval.VoiceDetect +
                                          						Campaign_Query_Rule_Interval.WrongNumberCount +
                                          						Campaign_Query_Rule_Interval.CustomerNotHomeCount +
                                          						Campaign_Query_Rule_Interval.CustomerAbandonDetect +
                                          						Campaign_Query_Rule_Interval.CallbackCount +
                                          						Campaign_Query_Rule_Interval.PersonalCallbackCount +
                                          						Campaign_Query_Rule_Interval.AbandonDetect +
                                          						Campaign_Query_Rule_Interval.AbandonToIVR

Right Party Connect

The
                                          						number of call attempts as indicated by agents using their desktop, when
                                          						the actual customer was contacted and handled.

Derived
                                          						from: Campaign_Query_Rule_Interval.VoiceDetect

Dialer Abandon & Abandon to IVR

The
                                          						number of calls that were abandoned by the dialer or abandoned to IVR because
                                          						there were no agents available to take the call. Campaign configuration
                                          						determines whether these calls are abandoned at the dialer or to IVR.

Dialer
                                          						Abandon is derived from: Campaign_Query_Rule_Interval.AbandonDetect

Abandon to
                                          						IVR is derived from: Campaign_Query_Rule_Interval.AbandonToIVR

Attempts

Total

The total number of outbound calls attempted.

Derived from: Campaign_Query_Rule_Interval.ContactsAttempted

Customer Answered

The
                                          						percentage of attempted calls that reached a live voice.

Derived
                                          						from: (Campaign_Query_Rule_Interval.VoiceDetect +
                                          						Campaign_Query_Rule_Interval.WrongNumberCount +
                                          						Campaign_Query_Rule_Interval.CustomerNotHomeCount +
                                          						Campaign_Query_Rule_Interval.CustomerAbandonDetect +
                                          						Campaign_Query_Rule_Interval.CallbackCount +
                                          						Campaign_Query_Rule_Interval.PersonalCallbackCount +
                                          						Campaign_Query_Rule_Interval.AbandonDetect +
                                          						Campaign_Query_Rule_Interval.AbandonToIVR)/
                                          						Campaign_Query_Rule_Interval.ContactsAttempted

Did Not Answer

The
                                          						percentage of calls attempted when the number was dialed but the customer (live
                                          						voice) was not reached and there were no problems with the call ("Ring No
                                          						Answer").

Derived
                                          						from: (Campaign_Query_Rule_Interval. AnsweringMachineDetect +
                                          						Campaign_Query_Rule_Interval.BusyDetect +
                                          						Campaign_Query_Rule_Interval.NoAnswerDetect +
                                          						Campaign_Query_Rule_Interval.CancelledDetect)/
                                          						Campaign_Query_Rule_Interval.ContactsAttempted

Problem

The percentage of calls attempted where the contact was dialed and one of the following problems was encountered:

Fax machine detected.

No dial tone when dialer port went off hook.

No Ringback from network when dial attempted.

Network disconnected while alerting.

Low Energy ("or dead air") call detected by the dialer.

Operator intercept (SIT Tone) was returned from network when dial attempted.

Derived
                                          						from: (Campaign_Query_Rule_Interval.FaxDetect +
                                          						Campaign_Query_Rule_Interval.NoDialToneDetect +
                                          						Campaign_Query_Rule_Interval.NoRingBackDetect +
                                          						Campaign_Query_Rule_Interval.SITToneDetect)/
                                          						Campaign_Query_Rule_Interval.ContactsAttempted

Did Not
                                             						Dial

Agent Rejected

The
                                          						number of preview or callback calls that were rejected
                                          						by the agent.

Derived
                                          						from: Campaign_Query_Rule_Interval.AgentRejectedDetect

Agent Closed

The
                                          						number of preview or callback calls that were rejected by the agent. 
                                          					 The agent did not call these customers.

Derived
                                          						from: Campaign_Query_Rule_Interval.AgentClosedDetect

Note
                                          						that these calls were not counted as attempted.

## Query Rule Within
                        	 Campaign Half Hour

The Query Rule Within Campaign Half Hour report shows
                              		  the breakdown of attempts (in percentage) of each campaign for the selected
                              		  time period, the status (summary and percentage) of each campaign for the
                              		  selected time period, and the status for each Query rule within a campaign for
                              		  the selected time interval.

Views: This report has the following grid views:

Breakdown of Attempts per Query Rule within Campaign Half Hour (the default)

Call Counts per Query Rule within Campaign Half Hour

Summary of Attempts per Query Rule Within Campaign Half Hour

Select the view you want to see from the report drop-down list that is located on the top left corner.

Query: This report data
                              		  is built from an Anonymous type query.

Value List: Campaigns

Database Schema Tables from which data is retrieved:

Campaign

Campaign_Query_Rule_Interval

Query_Rule

### Current
                              		  Fields in the Breakdown of Attempts (%) Per Query Rule Within Campaign Half
                              		  Hour Report View

Current fields are those fields that appear by default in a report generated from the stock template.

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

DateTime

The date and time of the start of the half-hour interval for the row's data in MM/DD/YYYY (month, day, year) and HH:MM:SS
                                          (hour, minute, second) format.

Derived from: Campaign_Query_Rule_Interval.DateTime

Attempts

The
                                          						total number of outbound calls attempted.

Derived from:
                                          						Campaign_Query_Rule_Interval.ContactsAttempted

Customers Answered

Right Party Connect

The percentage of call attempts as indicated by agents using their desktop, when the
                                          						actual customer was contacted and handled.

Derived from: Campaign_Query_Rule_Interval.VoiceDetect /Campaign_Query_Rule_Interval.ContactsAttempted

Dialer Abandon

The percentage of contacts or attempts in the half-hour interval abandoned by the dialer
                                          						because no agents were available and "Abandon to IVR" was not
                                          						configured.

Derived from: Campaign_Query_Rule_Interval.
                                          						AbandonDetect/Campaign_Query_Rule_Interval.ContactsAttempted

Note: This column is calculated as a percentage of all attempts because all the
                                          						remaining numbers are represented in percentage only. These columns always add
                                          						up to 100%.

Abandon to IVR

The percentage of attempts that
                                          						were sent to IVR (or another dialed number) for treatment after the dialer
                                          						reached a contact and no agent was available to take the call.

Derived from: Campaign_Query_Rule_Interval.
                                          						AbandonToIVR/Campaign_Query_Rule_Interval.ContactsAttempted

Callback

The percentage of callbacks requested by the customer when the campaign is not
                                          						configured for personal callback.

Derived from: Campaign_Query_Rule_Interval.CallbackCount/
                                          						Campaign_Query_Rule_Interval.ContactsAttempted

Personal Callback

The percentage of callbacks scheduled and requested by the customer when the campaign
                                          						was configured for personal callback.

Derived from:
                                          						Campaign_Query_Rule_Interval.PersonalCallbackCount/
                                          						Campaign_Query_Rule_Interval.ContactsAttempted

Customers Not Home

The percentage of contacts in the half-hour interval where the party answering the
                                          						phone was not the customer.

Derived from:
                                          						Campaign_Query_Rule_Interval.CustomersNotHomeCount/
                                          						Campaign_Query_Rule_Interval.ContactsAttempted

Wrong Number

The percentage of contacts in the half-hour interval where the party answering the
                                          						phone indicated that the customer did not live there.

Derived from:
                                          						Campaign_Query_Rule_Interval.WrongNumberCount/
                                          						Campaign_Query_Rule_Interval.ContactsAttempted

Customer Abandon

The percentage of contacts in the half-hour interval where the customer ended the call immediately after being connected to
                                          an agent.

Derived from:
                                          						Campaign_Query_Rule_Interval.CustomerAbandonDetect/
                                          						Campaign_Query_Rule_Interval.ContactsAttempted

Customers Did Not Answer

Answering Machine

The percentage of contacts in the half-hour interval that detected an answering
                                          						machine.

Derived from: Campaign_Query_Rule_Interval.
                                          						AnsweringMachineDetectToHal/
                                          						Campaign_Query_Rule_Interval.ContactsAttempted

No Answer

The percentage of contacts in the half-hour interval that were not answered.

Derived from: Campaign_Query_Rule_Interval.
                                          						NoAnswerDetect/ Campaign_Query_Rule_Interval.ContactsAttempted

Busy

The percentage of contacts in the half-hour interval that detected a busy signal.

Derived from: Campaign_Query_Rule_Interval. BusyDetect/
                                          						Campaign_Query_Rule_Interval.ContactsAttempted

Canceled

The percentage of contacts in the half-hour interval where the dialer canceled a
                                          						ringing customer call.

Derived from:
                                          						Campaign_Query_Rule_Interval.CanceledDetect/
                                          						Campaign_Query_Rule_Interval.ContactsAttempted

Problem

SIT Tone

The
                                          						number of contacts in the half-hour interval that detected a Special
                                          						Information Tone (SIT).

Derived from: Campaign_Query_Rule_Interval.SITToneDetect

No Dialtone

The
                                          						number of contacts in the half-hour interval that did not detect a dial tone.

Derived from:
                                          						Campaign_Query_Rule_Interval.NoDialToneDetect

Fax

The
                                          						number of contacts in the half-hour interval that detected a fax machine.

Derived from: Campaign_Query_Rule_Interval.FaxDetect

Network Error

The number of contacts that encountered one of the following problems:

No Ringback from network when dial attempted

Network disconnected while alerting

Low Energy ("or dead air") call detected by the dialer.

Derived from:
                                          						Campaign_Query_Rule_Interval.NoRingBackDetect

### Current Fields
                              		  in the Call Counts Per Query Rule Within Campaign Half Hour Report View

Current fields are those fields that appear by default in a report generated from the stock template.

Columns
                                          						(Fields)

Description

Campaign

The name
                                          						of the campaign.

Derived
                                          						from: Campaign.CampaignName

Query
                                          						Rule

The name
                                          						of the query rule.

Derived
                                          						from: Query_Rule.QueryRuleName

DateTime

The
                                          						central controller date and time at the start of the half-hour interval.

Derived
                                          						from: Campaign_Query_Rule_Interval.DateTime

Attempts

Summary
                                          						total of the number of calls attempted in the half-hour interval.

Derived
                                          						from: Campaign_Query_Rule_Interval.ContactsAttempted

Requested Callback

The
                                          						number of callback contacts.

Derived
                                          						from: Campaign_Query_Rule_Interval.CallBackCount

Requested Personal Callback

The
                                          						number of callback contacts scheduled.

Derived
                                          						from: Campaign_Query_Rule_Interval.PersonalCallbackCount

Voice

The
                                          						number of contacts for which a voice was detected during the half-hour
                                          						interval.

Derived
                                          						from: Campaign_Query_Rule_Interval.VoiceDetect

Busy

The
                                          						number of contacts in the half-hour interval that detected a busy signal.

Derived
                                          						from: Campaign_Query_Rule_Interval.BusyDetect

No
                                          						Answer

The
                                          						number of contacts in the half-hour interval that were not answered.

Derived
                                          						from: Campaign_Query_Rule_Interval.NoAnswerDetect

No
                                          						Ringback

The
                                          						number of contacts in the half-hour interval that did not detect a ring back.
                                          						The Calls with CallResults 4, 27 and 28 are mentioned in this column.

Derived
                                          						from: Campaign_Query_Rule_Interval.NoRingBackDetect

No
                                          						Dialtone

The
                                          						number of contacts in the half-hour interval that did not detect a dial tone.

Derived
                                          						from: Campaign_Query_Rule_Interval.NoDialToneDetect

Fax

The
                                          						number of contacts in the half-hour interval that detected a fax.

Derived
                                          						from: Campaign_Query_Rule_Interval.FaxDetect

Network
                                          						IVR

The
                                          						number of contacts in the half-hour interval that detected a network answering
                                          						machine.

Derived from:
                                          						Campaign_Query_Rule_Interval.NetworkAnsMachineDetect

Answering Machine

The
                                          						number of contacts in the half-hour interval that detected an answering
                                          						machine.

Derived from:
                                          						Campaign_Query_Rule_Interval.AnsweringMachineDetect

SIT
                                          						Tone

The
                                          						number of contacts in the half-hour interval that detected a special
                                          						information tone (SIT).

Derived from: Campaign_Query_Rule_Interval.SITToneDetect

Agent
                                          						Rejected

The
                                          						number of preview or callback contacts in the half-hour interval that were
                                          						rejected by the agent.

Derived from:
                                          						Campaign_Query_Rule_Interval.AgentRejectedDetect

Agent
                                          						Closed

The
                                          						number of preview or callback contacts that were rejected by the agent. (The agent did not call these customers.)

Derived from:
                                          						Campaign_Query_Rule_Interval.AgentClosedDetect

Customer Not Home

The
                                          						number of contacts in the half-hour interval where the party answering the
                                          						phone was not the customer.

Derived from:
                                          						Campaign_Query_Rule_Interval.CustomerNotHomeCount

Wrong
                                          						Number

The
                                          						number of contacts in the half-hour interval where the party answering the
                                          						phone indicated the customer didn't live there.

Derived from:
                                          						Campaign_Query_Rule_Interval.WrongNumberCount

Canceled

The
                                          						number of contacts in the half-hour interval where the dialer canceled a
                                          						ringing customer call.

Derived from: Campaign_Query_Rule_Interval.CanceledDetect

Dialer
                                          						Abandon

The
                                          						number of contacts in the half-hour interval abandoned by the dialer.

Derived from: Campaign_Query_Rule_Interval.AbandonDetect

Abandon to IVR

The
                                          						number of contacts in the half-hour interval that were abandoned by the dialer and  transferred to IVR, which plays
                                          a message.

Derived from: Campaign_Query_Rule_Interval.AbandonToIVR

Customer Abandon

The number of contacts in the half-hour interval where the customer ended the call immediately after picking up the phone.

Derived from:
                                          						Campaign_Query_Rule_Interval.CustomerAbandonDetect

Talk
                                          						Time

The
                                          						total time in HH:MM:SS (hours, minutes, seconds) that agents spent talking on
                                          						the phone in the half-hour interval.

Derived from: Campaign_Query_Rule_Interval.TalkTime

Wrap Up
                                          						Time

The
                                          						length of time the agents spent in wrap-up work.

Derived from: Campaign_Query_Rule_Interval.WrapupTime

### Current
                              		  Fields in the Summary of Attempts Per Query Rule Within Campaign Half Hour
                              		  Report View

Current fields are those fields that appear by default in a report generated from the stock template.

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

DateTime

The
                                          						date and time at the start of the half-hour interval for the row's data in
                                          						MM/DD/YYYY (month, day, year) and HH:MM:SS (hours, minutes, seconds) format.

Derived from: Campaign_Query_Rule_Interval.DateTime

Key
                                             						Statistics

Customer Answered

The
                                          						number of the outbound calls (attempts) that reached a live voice.

Derived from: Campaign_Query_Rule_Interval.VoiceDetect +
                                          						Campaign_Query_Rule_Interval.WrongNumberCount +
                                          						Campaign_Query_Rule_Interval.CustomerNotHomeCount +
                                          						Campaign_Query_Rule_Interval.CustomerAbandonDetect +
                                          						Campaign_Query_Rule_Interval.CallbackCount
                                          						+Campaign_Query_Rule_Interval.PersonalCallbackCount +
                                          						Campaign_Query_Rule_Interval.AbandonDetect +
                                          						Campaign_Query_Rule_Interval.AbandonToIVR

Right Party Connect

The
                                          						number of call attempts as indicated by agents using their desktop, when
                                          						the actual customer was contacted and handled.

Derived from: Derived from:
                                          						Campaign_Query_Rule_Interval.VoiceDetect

Dialer Abandon & Abandon to IVR

The
                                          						number of calls that were abandoned by the dialer or abandoned to IVR because
                                          						there were no agents available to take the call. Campaign configuration
                                          						determines whether these calls are abandoned at the dialer or to IVR.

Dialer
                                          						Abandon is derived from: Campaign_Query_Rule_Interval.AbandonDetect

AbandtoIVR is derived from: Campaign_Query_Rule_Interval.AbandonToIVR

Attempts

Total

The
                                          						total number of outbound calls attempted.

Derived from:
                                          						Campaign_Query_Rule_Interval.ContactsAttempted

Customer Answered

The
                                          						percentage of attempted calls that reached a live voice.

Derived from: (Campaign_Query_Rule_Interval.VoiceDetect +
                                          						Campaign_Query_Rule_Interval.WrongNumberCount +
                                          						Campaign_Query_Rule_Interval.CustomerNotHomeCount +
                                          						Campaign_Query_Rule_Interval.CustomerAbandonDetect +
                                          						Campaign_Query_Rule_Interval.CallbackCount +
                                          						Campaign_Query_Rule_Interval.PersonalCallbackCount +
                                          						Campaign_Query_Rule_Interval.AbandonDetect +
                                          						Campaign_Query_Rule_Interval.AbandonToIVR)/
                                          						Campaign_Query_Rule_Interval.ContactsAttempted

Did Not Answer

The
                                          						percentage of calls attempted when the number was dialed but the customer (live
                                          						voice) was not reached and there were no problems with the call ("Ring No
                                          						Answer").

Derived from: (Campaign_Query_Rule_Interval.
                                          						AnsweringMachineDetect + Campaign_Query_Rule_Interval.BusyDetect +
                                          						Campaign_Query_Rule_Interval.NoAnswerDetect +
                                          						Campaign_Query_Rule_Interval.CancelledDetect)/
                                          						Campaign_Query_Rule_Interval.ContactsAttempted

Problem

The percentage of calls attempted where the contact was dialed and one of the following problems was encountered:

Fax machine detected.

No dial tone when dialer port went off hook.

No Ringback from network when dial attempted.

Network disconnected while alerting.

Low Energy ("or dead air") call detected by the dialer.

Operator intercept (SIT Tone) was returned from network when dial attempted.

Derived from: (Campaign_Query_Rule_Interval.FaxDetect +
                                          						Campaign_Query_Rule_Interval.NoDialToneDetect +
                                          						Campaign_Query_Rule_Interval.NoRingBackDetect +
                                          						Campaign_Query_Rule_Interval.SITToneDetect)/
                                          						Campaign_Query_Rule_Interval.ContactsAttempted

Did
                                             						Not Dial

Agent Rejected

The
                                          						number of preview or callback calls in the half-hour interval that were rejected
                                          						by the agent.

Derived from:
                                          						Campaign_Query_Rule_Interval.AgentRejectedDetect

Note:
                                          						These calls are not counted as attempted.

Agent Closed

The
                                          						number of preview or callback calls that were rejected by the agent (these
                                          						customers are not dialed).

Derived from:
                                          						Campaign_Query_Rule_Interval.AgentClosedDetect

Note: These calls are not counted as attempted.

| Columns (Fields) | Description |
|---|---|
| Campaign | The
                                          						name of the campaign. Derived from: Campaign.CampaignName |
| Date | The date for the record in MM/DD/YYYY (month, day, year) format. Derived from: Campaign_Query_Rule_Interval.DateTime |
| Attempts | The total number of outbound calls attempted. Derived from: Campaign_Query_Rule_Interval.ContactsAttempted |
| Customer Answered |
| Right Party Connect | The percentage of calls attempted when the
                                          						actual customer was contacted and handled, as indicated by agents using their desktop. Derived from: Campaign_Query_Rule_Interval. VoiceDetect/ Campaign_Query_Rule_Interval.ContactsAttempted |
| Dialer Abandon | The percentage of contacts or attempts abandoned by the dialer
                                          						because the agent was not available and "Abandon to IVR" was not
                                          						configured. Derived from: Campaign_Query_Rule_Interval. AbandonDetect/ Campaign_Query_Rule_Interval.ContactsAttempted |
| Abandon to IVR | The percentage of contacts or attempts that were abandoned by
                                          						the dialer but transferred to an IVR. That is, the percentage of attempts that
                                          						were sent to IVR (or another dialed number) for treatment after the dialer
                                          						reached a contact and no agent was available to take the call. 
                                          					 Instead of hanging up on the customer, the customer was
                                          						transferred to an IVR, which plays a message. Derived from: Campaign_Query_Rule_Interval. AbandonToIVR/ Campaign_Query_Rule_Interval.ContactsAttempted |
| Callback | When the campaign is not
                                          						configured for personal callback, the percentage of customers contacted that  request a callback. Derived from: Campaign_Query_Rule_Interval. CallbackCount/Campaign_Query_Rule_Interval.ContactsAttempted |
| Personal Callback | When the campaign
                                          						is configured for personal callback, the percentage of contacts in which the customer requested a callback and was scheduled. Derived from: Campaign_Query_Rule_Interval. PersonalCallbackCount/Campaign_Query_Rule_Interval.ContactsAttempted |
| Customer Not Home | The percentage of contacts where the party answering the
                                          						phone was not the customer. Derived from: Campaign_Query_Rule_Interval. CustomerNotHomeCount/Campaign_Query_Rule_Interval.ContactsAttempted |
| Wrong Number | The percentage of contacts where the party answering the
                                          						phone indicated that the customer was not available. Derived from: Campaign_Query_Rule_Interval. WrongNumberCount/Campaign_Query_Rule_Interval.ContactsAttempted |
| Customer Abandon | The percentage of contacts where the customer ended the call immediately after being connected to an agent. Derived from: Campaign_Query_Rule_Interval. CustomerAbandonDetect/Campaign_Query_Rule_Interval.ContactsAttempted |
| Customer Did Not Answer |
| Answering Machine | The percentage of contacts that detected an answering
                                          						machine. Derived from: Campaign_Query_Rule_Interval. AnsweringMachineDetectToHal/Campaign_Query_Rule_Interval.ContactsAttempted |
| No Answer | The percentage of contacts that were not answered. Derived from: Campaign_Query_Rule_Interval. NoAnswerDetect/Campaign_Query_Rule_Interval.ContactsAttempted |
| Busy | The percentage of contacts that detected a busy signal. Derived from: Campaign_Query_Rule_Interval. BusyDetect/Campaign_Query_Rule_Interval.ContactsAttempted |
| Canceled | The percentage of contacts where the dialer canceled a
                                          						ringing customer call. Derived from: Campaign_Query_Rule_Interval. CanceledDetect/Campaign_Query_Rule_Interval.ContactsAttempted |
| Problem |
| SIT Tone | The number of contacts in the half-hour interval that detected a Special
                                          						Information Tone (SIT). Derived from: Campaign_Query_Rule_Interval.SITToneDetect |
| No Dial tone | The
                                          						number of contacts in the half-hour interval that did not detect a dial tone. Derived from:
                                          						Campaign_Query_Rule_Interval.NoDialToneDetect |
| Fax | The
                                          						number of contacts in the half-hour interval that detected a fax. Campaign_Query_Rule_Interval.FaxDetect |
| Network Error | The number of contacts that encountered one of the following problems: No Ringback from network when dial attempted Network disconnected while alerting Low Energy ("or dead air") call detected by the dialer. Derived from:
                                          						Campaign_Query_Rule_Interval.NoRingBackDetect |

| Columns
                                          						(Fields) | Description |
|---|---|
| Campaign | The name
                                          						of the campaign. Derived
                                          						from: Campaign.CampaignName |
| Date | The date for the record in MM/DD/YYYY (month, day, year) format. Derived from: Campaign_Query_Rule_Interval.DateTime |
| Key
                                             						Statistics |
| Customer Answered | The
                                          						number of outbound calls (attempts) that reached a live voice. Derived
                                          						from: Campaign_Query_Rule_Interval.VoiceDetect +
                                          						Campaign_Query_Rule_Interval.WrongNumberCount +
                                          						Campaign_Query_Rule_Interval.CustomerNotHomeCount +
                                          						Campaign_Query_Rule_Interval.CustomerAbandonDetect +
                                          						Campaign_Query_Rule_Interval.CallbackCount +
                                          						Campaign_Query_Rule_Interval.PersonalCallbackCount +
                                          						Campaign_Query_Rule_Interval.AbandonDetect +
                                          						Campaign_Query_Rule_Interval.AbandonToIVR |
| Right Party  
                                          					 Connect | The
                                          						number of call attempts, as indicated by agents using their desktop, when
                                          						the actual customer was contacted and handled. Derived
                                          						from: Campaign_Query_Rule_Interval.VoiceDetect |
| Dialer Abandon & Abandon to IVR | The
                                          						number of calls that were abandoned by the dialer or abandoned to IVR because
                                          						an agent was not available to take the call. Campaign configuration
                                          						determines whether these calls are abandoned at the dialer or transferred to IVR. Derived
                                          						from: Campaign_Query_Rule_Interval. AbandonToIVR +
                                          						Campaign_Query_Rule_Interval. AbandonDetect |
| Attempts |
| Total | The
                                          						total number of outbound calls attempted. Derived
                                          						from: Campaign_Query_Rule_Interval.ContactsAttempted |
| Customer Answered | The
                                          						percentage of attempted calls that reached a live voice. Derived
                                          						from: (Campaign_Query_Rule_Interval.VoiceDetect +
                                          						Campaign_Query_Rule_Interval.WrongNumberCount +
                                          						Campaign_Query_Rule_Interval.CustomerNotHomeCount +
                                          						Campaign_Query_Rule_Interval.CustomerAbandonDetect +
                                          						Campaign_Query_Rule_Interval.CallbackCount +
                                          						Campaign_Query_Rule_Interval.PersonalCallbackCount +
                                          						Campaign_Query_Rule_Interval.AbandonDetect +
                                          						Campaign_Query_Rule_Interval.AbandonToIVR)/
                                          						Campaign_Query_Rule_Interval.ContactsAttempted |
| Did not Answer | The
                                          						percentage of calls attempted when the number was dialed but the customer was
                                          						not reached and there were no problems with the call ("Ring No Answer"). Derived
                                          						from: (Campaign_Query_Rule_Interval.AnsweringMachineDetect +
                                          						Campaign_Query_Rule_Interval.BusyDetect +
                                          						Campaign_Query_Rule_Interval.NoAnswerDetect +
                                          						Campaign_Query_Rule_Interval.CancelledDetect)/
                                          						Campaign_Query_Rule_Interval.ContactsAttempted |
| Problem | The percentage of calls attempted where the contact was dialed and one of the following problems was encountered: Fax machine detected No dial tone when dialer port went off hook No Ringback from network when dial attempted Network disconnected while alerting. Low Energy ("or dead air") call detected by the dialer Operator intercept (SIT Tone) was returned from network when dial attempted. Derived
                                          						from: (Campaign_Query_Rule_Interval.FaxDetect +
                                          						Campaign_Query_Rule_Interval.NoDialToneDetect +
                                          						Campaign_Query_Rule_Interval.NoRingBackDetect +
                                          						Campaign_Query_Rule_Interval.SITToneDetect)/
                                          						Campaign_Query_Rule_Interval.ContactsAttempted |
| Did Not
                                             						Dial |
| Agent Rejected | The
                                          						number of preview or callback calls that were rejected
                                          						by the agent. (An attempt should be made to contact these customers again.) Derived
                                          						from: Campaign_Query_Rule_Interval.AgentRejectedDetect These
                                          						calls are not counted as attempted. |
| Agent Closed | The
                                          						number of preview or callback calls that were rejected by the agent. (The agent did not call these customers.) Derived
                                          						from: Campaign_Query_Rule_Interval.AgentClosedDetect These
                                          						calls are not counted as attempted. |

| Columns
                                          						(Fields) | Description |
|---|---|
| Campaign | The name
                                          						of the campaign. Derived
                                          						from: Campaign.CampaignName |
| Date | The date for the record in MM/DD/YYYY (month, day, year) format. Derived from: Campaign_Query_Rule_Interval.DateTime |
| Agent
                                             						Time In Campaign |
| FTE | The FTE
                                          						value for the agents logged in and skilled for the campaign and not working in
                                          						other skill groups (or not ready). If all agents spend full-time on the
                                          						campaign's skill, the FTE is the number of agents. Derived
                                          						from: (Skill_Group_Interval.LoggedOnTime - Skill_Group_Interval.BusyOtherTime -
                                          						Skill_Group_Interval.NotReadyTime)/ Skill_Group_Interval.ReportingInterval |
| Talk | The
                                          						percentage of time that agents spent talking in one of the campaign's skill
                                          						groups. Derived
                                          						from: (Skill_Group_Interval.TalkTime - Skill_Group_Interval.TalkReserveTime)/
                                          						(Skill_Group_Interval.LoggedOnTime - Skill_Group_Interval. BusyOtherTime -
                                          						Skill_Group_Interval.NotReadyTime) |
| Wrap Up | The
                                          						percentage of time that agents have spent in Wrap-up state after incoming or
                                          						outgoing calls in one of the campaign's skill groups. Derived
                                          						from: (Skill_Group_Interval.WorkReadyTime +
                                          						Skill_Group_Interval.WorkNotReadyTime)/ (Skill_Group_Interval.LoggedOnTime-
                                          						Skill_Group_Interval. BusyOtherTime - Skill_Group_Interval.NotReadyTime) |
| Idle | The
                                          						percentage of time the agents were available in one of the campaign's skill groups; but not working. Derived
                                          						from: (Skill_Group_Interval.ReservedStateTime +
                                          						Skill_Group_Interval.TalkReserveTime + Skill_Group_Interval.AvailTime)/
                                          						(Skill_Group_Interval.LoggedOnTime- Skill_Group_Interval. BusyOtherTime -
                                          						Skill_Group_Interval.NotReadyTime) |
| Account Statistics |
| Connects/ FTE Agent Hour | The FTE
                                          						value for the number of calls of agents for the campaign's skill groups. Derived
                                          						from: (Skill_Group_Interval.AutoOutCalls + Skill_Group_Interval.CallsHandled +
                                          						Skill_Group_Interval. PreviewCalls) * Skill_Group_Interval.ReportingInterval/
                                          						(Skill_Group_Interval.LoggedOnTime - Skill_Group_Interval.BusyOtherTime -
                                          						Skill_Group_Interval.NotReadyTime, 0) |
| Time between Agent Connects | The
                                          						average time in seconds between the connecting customer calls to the agents. Derived
                                          						from: (Skill_Group_Interval.ReservedStateTime +
                                          						Skill_Group_Interval.TalkReserveTime + Skill_Group_Interval.AvailTime)/
                                          						(Skill_Group_Interval.AutoOutCalls + Skill_Group_Interval.CallsHandled +
                                          						Skill_Group_Interval. PreviewCalls) The Summary Avg for Time between Agent Connects is calculated using the following formula: Summary Avg for a selected campaign
                                          = idle time/ agent connects. |
| Completed |
| Agent Connects | The
                                          						number of calls (outbound and inbound) handled per agent for the campaign's
                                          						skill groups. Derived
                                          						from: (Skill_Group_Interval.AutoOutCalls + Skill_Group_Interval.CallsHandled +
                                          						Skill_Group_Interval. PreviewCalls) |
| Not Connected | The number of customer calls that were not connected to any agent or device. This includes calls which were abandoned by the
                                          dialer or abandoned to IVR (includes inbound and outbound calls) and resulted in customer abandon in queue or routing script
                                          error. Derived
                                          						from: Skill_Group_Interval.RouterCallsAbandQ + Skill_Group_Interval.RouterError
                                          						+ Campaign_Query_Rule_Interval.CustomerAbandonDetect +
                                          						Campaign_Query_Rule_Interval.AbandonDetect Note:
                                          						This column is invalid if the Outbound Reservation Script does not use
                                          						ReleaseCall when not reserving an agent. This results in extraneous Router Error call reports, which inflate the value
                                          in this column. |
| Dialer Abandon To Other | The number of calls which are in "abandon to IVR" state and have completed in a way that is not associated with a skill group
                                          in this campaign. This value only applies to Campaigns where the skill groups associated with the campaign are not used for
                                          inbound. Derived
                                          						from: Campaign_Query_Rule_Interval.AbandonToIVR -
                                          						(Skill_Group_Interval.RouterCallsAbandQ + Skill_Group_Interval.CallsHandled +
                                          						Skill_Group_Interval.RouterError) Note:
                                          						This column is approximate because the abandon to IVR can occur in one half
                                          						hour interval and the call completion occurs in another. This column is invalid if the Outbound Reservation Script does not use ReleaseCall when not reserving an agent, which results
                                          in undercounting in this column. This
                                          						column is invalid if the skill group is used for anything other than outbound
                                          						agent campaigns, for example inbound or transferred calls, as this results in
                                          						undercounting in this column. This
                                          						column is invalid if the abandon to IVR script queues to multiple skill groups
                                          						in this campaign because RouterErrors and RouterCallsAbandQ are counted once in
                                          						each skill group the call was queued to, which results in undercounting in this
                                          						column. |
| Outbound
                                             						Statistics |
| Average Handle Time | The
                                          						average length of calls (Inbound and Outbound) handled by the agent during the
                                          						campaign's skill group selected interval. Derived
                                          						from: (Skill_Group_Interval.TalkTime - Skill_Group_Interval.TalkReserveTime +
                                          						Skill_Group_Interval.WorkReadyTime + Skill_Group_Interval.WorkNotReadyTime)/
                                          						(Skill_Group_Interval.AutoOutCalls + Skill_Group_Interval.CallsHandled +
                                          						Skill_Group_Interval. PreviewCalls) |
| % Abandon | The
                                          						percentage of calls that reached a live voice and were abandoned by the dialer
                                          						or abandon to IVR because no agent was available. Derived from: (Campaign_Query_Rule_Interval.AbandonDetect +
                                          						Campaign_Query_Rule_Interval.AbandonToIVR)/
                                          						(Campaign_Query_Rule_Interval.VoiceDetect +
                                          						Campaign_Query_Rule_Interval.WrongNumberCount +
                                          						Campaign_Query_Rule_Interval.CustomerNotHomeCount +
                                          						Campaign_Query_Rule_Interval.CustomerAbandonDetect +
                                          						Campaign_Query_Rule_Interval.CallbackCount +
                                          						Campaign_Query_Rule_Interval.PersonalCallbackCount +
                                          						Campaign_Query_Rule_Interval.AbandonDetect +
                                          						Campaign_Query_Rule_Interval.AbandonToIVR) |
| Hit Rate | The
                                          						percentage % of the outbound calls (attempts) that reached a live voice. Derived
                                          						from: (Campaign_Query_Rule_Interval.VoiceDetect +
                                          						Campaign_Query_Rule_Interval.WrongNumberCount +
                                          						Campaign_Query_Rule_Interval.CustomerNotHomeCount +
                                          						Campaign_Query_Rule_Interval.CustomerAbandonDetect +
                                          						Campaign_Query_Rule_Interval.CallbackCount +
                                          						Campaign_Query_Rule_Interval.PersonalCallbackCount +
                                          						Campaign_Query_Rule_Interval.AbandonDetect +
                                          						Campaign_Query_Rule_Interval.AbandonToIVR)/
                                          						Campaign_Query_Rule_Interval.ContactsAttempted |
| Attempts | The
                                          						Total number of outbound calls attempted. Derived
                                          						from: Campaign_Query_Rule_Interval.ContactsAttempted |

| Columns (Fields) | Description |
|---|---|
| Campaign | The
                                          						name of the campaign. Derived from: Campaign.CampaignName |
| Date | The
                                          						date for the row's data in MM/DD/YYYY (month, day, year) format. Derived from: Campaign_Query_Rule_Interval.DateTime |
| Agent
                                             						Connects |
| Outbound Immediate | The number of outbound calls where the customer was connected to an agent immediately (without waiting in the queue). Derived from: Skill_Group_Interval.AutoOutCalls +
                                          						Skill_Group_Interval.PreviewCalls |
| After Abandon To IVR & Inbound | This field includes the following calls: Outbound calls that were handled by an agent in this skill group after Abandon To IVR. Outbound calls from a Transfer to IVR campaign that were queued back to agents. Inbound and transferred calls that were routed to agents in this skill group. Derived from: Skill_Group_Interval. CallsHandled |
| Not
                                             						Connected |
| Customer Abandon | The number of contacts when the customer ended the call immediately after picking up the phone. Derived from: Campaign_Query_Rule_Interval.CustomerAbandonDetect |
| Dialer Abandon | The
                                          						number of contacts abandoned by the dialer. Derived from:Campaign_Query_Rule_Interval.AbandonDetect |
| Customer Abandon in Queue | The number of contacts when the customer ended the call while in queue. Derived from:Skill_Group_Interval.RouterCallsAbandQ |
| Script Error | The
                                          						number of calls that resulted in an error condition in the call routing script. Derived from:Skill_Group_Interval.RouterError |
| Dialer
                                             						Abandon To Other |
| Script Dequeued | The
                                          						number of calls that were initially abandoned to IVR because no agent was
                                          						available and then queued to a skill group for this campaign and again removed
                                          						from the queue during the interval. Derived from: Skill_Group_Interval.RouterCallsDequeued |
| Other | The
                                          						number of calls that were routed to another skill group or never made it to the
                                          						skill group. This column is approximate because the abandon to IVR can occur
                                          						in one half hour interval and the call completion occurs in another interval. Derived from:Campaign_Query_Rule_Interval.AbandonToIVR -
                                       					 (Skill_Group_Interval.RouterCallsAbandQ + Skill_Group_Interval.CallsHandled +
                                       					 Skill_Group_Interval.RouterError + Skill_Group_Interval. RouterCallsDequeued) This
                                          						column is approximate because the abandon to IVR can occur in one interval
                                          						and the call completion occurs in another interval. |

| Columns
                                          						(Fields) | Description |
|---|---|
| Campaign | The name
                                          						of the campaign. Derived
                                          						from: Campaign.CampaignName |
| DateTime | The date
                                          						and time at the start of the half-hour interval for the row's data in
                                          						MM/DD/YYYY (month, day, year) and HH:MM:SS (hours, minutes, seconds) format. Derived
                                          						from: Campaign_Query_Rule_Interval.DateTime |
| Agent
                                             						Time In Campaign |
| FTE | The Full Time Equivalent (FTE)
                                          						value for the agents logged in and skilled for the campaign and not working in
                                          						other skill groups (or not ready) in the half-hour interval. If all agents
                                          						spend full-time on the campaign's skill during the half hour interval, the FTE
                                          						is the number of agents. Derived
                                          						from: (Skill_Group_Interval.LoggedOnTime -
                                          						Skill_Group_Interval.BusyOtherTime -
                                          						Skill_Group_Interval.NotReadyTime)/ Skill_Group_Interval.ReportingInterval |
| Talk | The percentage of time that agents spent talking in one of the campaign's skill groups. (Skill_Group_Interval.TalkTime - Skill_Group_Interval.TalkReserveTime)/ (Skill_Group_Interval.LoggedOnTime - Skill_Group_Interval.
                                          BusyOtherTime - Skill_Group_Interval.NotReadyTime) |
| Wrap Up | The
                                          						percentage of time that agents have spent in Wrap-up state after incoming or
                                          						outgoing calls in one of the campaign's skill groups. Derived
                                          						from: (Skill_Group_Interval.WorkReadyTime +
                                          						Skill_Group_Interval.WorkNotReadyTime)/
                                          						(Skill_Group_Interval.LoggedOnTime- Skill_Group_Interval.
                                          						BusyOtherTime - Skill_Group_Interval.NotReadyTime) |
| Idle | The
                                          						percentage of time the agents were available in one of the Campaign's skill
                                          						groups but not working. Derived
                                          						from: (Skill_Group_Interval.ReservedStateTime +
                                          						Skill_Group_Interval.TalkReserveTime +
                                          						Skill_Group_Interval.AvailTime)/
                                          						(Skill_Group_Interval.LoggedOnTime- Skill_Group_Interval.
                                          						BusyOtherTime - Skill_Group_Interval.NotReadyTime) |
| Agent Statistics |
| Connects/ FTE Agent Hour | The FTE value for the number of calls of agents in the interval for the campaign's skill groups. Derived
                                          						from: (Skill_Group_Interval.AutoOutCalls +
                                          						Skill_Group_Interval.CallsHandled + Skill_Group_Interval.
                                          						PreviewCalls) *  Skill_Group_Interval.ReportingInterval/ (Skill_Group_Interval.LoggedOnTime -
                                          						Skill_Group_Interval.BusyOtherTime -
                                          						Skill_Group_Interval.NotReadyTime, 0) |
| Time between Agent Connects | The
                                          						average time in seconds between the connecting customer calls to the agents. Derived
                                          						from: (Skill_Group_Interval.ReservedStateTime +
                                          						Skill_Group_Interval.TalkReserveTime +
                                          						Skill_Group_Interval.AvailTime)/
                                          						(Skill_Group_Interval.AutoOutCalls +
                                          						Skill_Group_Interval.CallsHandled + Skill_Group_Interval.
                                          						PreviewCalls) The
                                          						Summary Avg for Time between Agent Connects is calculated using the following
                                          						formula: Summary Avg for a selected campaign = idle time/ agent connects |
| Completed |
| Agent Connects | The
                                          						number of calls (outbound and inbound) handled per agent for the campaign's
                                          						skill groups. Derived
                                          						from: (Skill_Group_Interval.AutoOutCalls +
                                          						Skill_Group_Interval.CallsHandled + Skill_Group_Interval.
                                          						PreviewCalls) |
| Not Connected | The
                                          						number of customer calls that were not connected to any agent or device. This
                                          						includes calls which were abandoned by the dialer or abandoned to IVR (includes
                                          						inbound and outbound calls) and resulted in customer abandon in queue or
                                          						routing script error. Derived from: Skill_Group_Interval.RouterCallsAbandQ +
                                          						Skill_Group_Interval.RouterError +
                                          						Campaign_Query_Rule_Interval.CustomerAbandonDetect +
                                          						Campaign_Query_Rule_Interval.AbandonDetect Note:
                                          						This column is invalid if the Outbound Reservation Script does not use
                                          						ReleaseCall when not reserving an agent, which results in extraneous Router
                                          						Error call reports that inflates the value in this column. |
| Dialer Abandon To Other | The
                                          						number of calls that are in "abandon to IVR" state and have completed in a way
                                          						not associated with a skill group in this campaign. This value applies only to
                                          						Campaigns where the skill groups associated with the campaign are not used for
                                          						inbound. Derived
                                          						from: Campaign_Query_Rule_Interval.AbandonToIVR -
                                          						(Skill_Group_Interval.RouterCallsAbandQ +
                                          						Skill_Group_Interval.CallsHandled +
                                          						Skill_Group_Interval.RouterError) Note:
                                          						This column is approximate because the abandon to IVR can occur in one half-hour interval and the call completion occurs
                                          in another. This
                                          						column is invalid if the Outbound Reservation Script does not use ReleaseCall
                                          						when not reserving an agent, which results in under counting in this column. This
                                          						column is invalid if the skill group is used for anything other than outbound
                                          						agent campaigns, for example, inbound or transferred calls, as this results in
                                          						undercounting in this column. This
                                          						column is invalid if the abandon to IVR script queues to multiple skill groups
                                          						in this campaign because RouterErrors and RouterCallsAbandQ are
                                          						counted once in each skill group the call was queued to, which results in
                                          						undercounting in this column. |
| Outbound Statistics |
| Avg Handle Time | The
                                          						average length of calls (Inbound and Outbound) handled by the agent during the
                                          						campaign's skill group selected interval. Derived
                                          						from: (Skill_Group_Interval.TalkTime -
                                          						Skill_Group_Interval.TalkReserveTime +
                                          						Skill_Group_Interval.WorkReadyTime +
                                          						Skill_Group_Interval.WorkNotReadyTime)/
                                          						(Skill_Group_Interval.AutoOutCalls +
                                          						Skill_Group_Interval.CallsHandled + Skill_Group_Interval.
                                          						PreviewCalls) |
| % Abandon | The
                                          						percentage of calls that reached a live voice and were abandoned by the dialer
                                          						or abandon to IVR because no agent was available. Derived
                                          						from: (Campaign_Query_Rule_Interval.AbandonDetect +
                                          						Campaign_Query_Rule_Interval.AbandonToIVR)/
                                          						(Campaign_Query_Rule_Interval.VoiceDetect +
                                          						Campaign_Query_Rule_Interval.WrongNumberCount +
                                          						Campaign_Query_Rule_Interval.CustomerNotHomeCount +
                                          						Campaign_Query_Rule_Interval.CustomerAbandonDetect +
                                          						Campaign_Query_Rule_Interval.CallbackCount +
                                          						Campaign_Query_Rule_Interval.PersonalCallbackCount +
                                          						Campaign_Query_Rule_Interval.AbandonDetect +
                                          						Campaign_Query_Rule_Interval.AbandonToIVR) |
| Hit Rate | The
                                          						percentage of the outbound calls (attempts) that reached a live voice. Derived
                                          						from: (Campaign_Query_Rule_Interval.VoiceDetect +
                                          						Campaign_Query_Rule_Interval.WrongNumberCount +
                                          						Campaign_Query_Rule_Interval.CustomerNotHomeCount +
                                          						Campaign_Query_Rule_Interval.CustomerAbandonDetect +
                                          						Campaign_Query_Rule_Interval.CallbackCount +
                                          						Campaign_Query_Rule_Interval.PersonalCallbackCount +
                                          						Campaign_Query_Rule_Interval.AbandonDetect +
                                          						Campaign_Query_Rule_Interval.AbandonToIVR)/
                                          						Campaign_Query_Rule_Interval.ContactsAttempted |
| Attempts | The
                                          						total number of outbound calls attempted. Derived
                                          						from: Campaign_Query_Rule_Interval.ContactsAttempted |

| Columns
                                          						(Fields) | Description |
|---|---|
| Campaign | The name
                                          						of the campaign. Derived
                                          						from: Campaign.CampaignName |
| DateTime | The date
                                          						and time at the start of the half-hour interval for the row's data in
                                          						MM/DD/YYYY (month, day, year) and HH:MM:SS (hours, minutes, seconds) format. Derived
                                          						from: Campaign_Query_Rule_Interval.DateTime |
| Agent
                                             						Connects |
| Outbound Immediate | The
                                          						number of outbound calls where the customer was connected to an agent
                                          						immediately (without waiting in queue). Derived from: Skill_Group_Interval.AutoOutCalls +
                                          						Skill_Group_Interval.PreviewCalls |
| After Abandon To IVR & Inbound | This
                                          						includes the following calls: Outbound calls that were handled by an agent in this skill group after Abandon To IVR. Inbound and transferred calls that were routed to agents in this skill group. Outbound calls from a Transfer to IVR campaign that were queued back to agents. Derived from: Skill_Group_Interval. CallsHandled |
| Not
                                             						Connected |
| Customer Abandon | The number of contacts in the half-hour interval where the customer ended the call immediately after picking up the phone. Derived from:
                                          						Campaign_Query_Rule_Interval.CustomerAbandonDetect |
| Dialer Abandon | The
                                          						number of contacts in the half-hour interval abandoned by the dialer. Derived from:Campaign_Query_Rule_Interval.AbandonDetect |
| Customer Abandon in Queue | The number of contacts in the half-hour interval where the customer ended the call while in queue. Derived from:Skill_Group_Interval.RouterCallsAbandQ |
| Script Error | The
                                          						number of calls that resulted in an error condition in the call routing script. Derived from:Skill_Group_Interval.RouterError |
| Dialer
                                             						Abandon To Other |
| Script Dequeued | The
                                          						number of calls that were initially abandoned to IVR because no agent was
                                          						available and then queued to a skill group for this campaign and again removed
                                          						from the queue during the half-hour interval. Derived from: Skill_Group_Interval.RouterCallsDequeued |
| Other | The
                                          						number of calls that were routed to another skill group or never made to the
                                          						skill group. Derived from:Campaign_Query_Rule_Interval.AbandonToIVR -
                                          						(Skill_Group_Interval.RouterCallsAbandQ +
                                          						Skill_Group_Interval.CallsHandled +
                                          						Skill_Group_Interval.RouterError + Skill_Group_Interval.
                                          						RouterCallsDequeued) This
                                          						column is approximate because the abandon to IVR can occur in one half-hour
                                          						interval and the call completion occurs in another interval. |

| Columns
                                          						(Fields) | Description |
|---|---|
| Campaign | The name
                                          						of the campaign. Derived
                                          						from: Campaign.CampaignName |
| DateTime | The date
                                          						and time at the start of a half-hour interval for the row's data in MM/DD/YYYY
                                          						(month, day, year) and HH:MM:SS (hours, minutes, seconds) format. Derived
                                          						from: Campaign_Query_Rule_Interval.DateTime |
| Attempts | The total number of outbound calls attempted. Derived from: Campaign_Query_Rule_Interval.ContactsAttempted |
| Customer
                                             						Answered |
| Right Party Connect | The percentage of call attempts when the
                                          						actual customer was contacted and handled,  as indicated by agents using their desktop. Derived from: Campaign_Query_Rule_Interval. VoiceDetect/Campaign_Query_Rule_Interval.ContactsAttempted |
| Dialer Abandon | The percentage of contacts or attempts in the half-hour interval abandoned by the dialer because agents were not available
                                          and there was no configuration in place for "Abandon to IVR". Derived
                                          						from: Campaign_Query_Rule_Interval. AbandonDetect/
                                          						Campaign_Query_Rule_Interval.ContactsAttempted |
| Abandon to IVR | The percentage of attempts that reached a customer and were abandoned to IVR because no agents were available to handle the
                                          call. Derived
                                          						from: Campaign_Query_Rule_Interval.AbandonToIVR/
                                          						Campaign_Query_Rule_Interval.ContactsAttempted |
| Callback | The percentage of call backs requested by the customer when the campaign is not
                                          						configured for personal callback. Derived
                                          						from: Campaign_Query_Rule_Interval.CallbackCount/
                                          						Campaign_Query_Rule_Interval.ContactsAttempted |
| Personal Callback | The percentage of call backs scheduled and requested by the customer when the campaign
                                          						is configured for personal callback. Derived
                                          						from: Campaign_Query_Rule_Interval.PersonalCallbackCount/
                                          						Campaign_Query_Rule_Interval.ContactsAttempted |
| Customer Not Home | The percentage of contacts in the half-hour interval when the party answering the phone was not the customer. Derived
                                          						from: Campaign_Query_Rule_Interval.CustomerNotHomeCount/
                                          						Campaign_Query_Rule_Interval.ContactsAttempted |
| Wrong Number | The percentage of contacts in the half-hour interval when the party answering the phone indicated that the customer did not
                                          live there. Derived
                                          						from: Campaign_Query_Rule_Interval.WrongNumberCount/
                                          						Campaign_Query_Rule_Interval.ContactsAttempted |
| Customer Abandon | The percentage of contacts in the half-hour interval where the customer ended the call immediately after being connected to
                                          an agent. Derived
                                          						from: Campaign_Query_Rule_Interval.
                                          						CustomerAbandonDetect/Campaign_Query_Rule_Interval.ContactsAttempted |
| Customer
                                             						Did Not Answer |
| Answering Machine | The percentage of contacts in the half-hour interval that detected an answering
                                          						machine. Derived
                                          						from: Campaign_Query_Rule_Interval.
                                          						AnsweringMachineDetect/Campaign_Query_Rule_Interval.ContactsAttempted |
| No Answer | The percentage of contacts in the half-hour interval that were not answered. Derived
                                          						from: Campaign_Query_Rule_Interval.
                                          						NoAnswerDetect/Campaign_Query_Rule_Interval.ContactsAttempted |
| Busy | The percentage of contacts in the half-hour interval that detected a busy signal. Derived from: Campaign_Query_Rule_Interval. BusyDetect/
                                          						Campaign_Query_Rule_Interval.ContactsAttempted |
| Canceled | The percentage of contacts in the half-hour interval where the dialer canceled a
                                          						ringing customer call. Derived from: Campaign_Query_Rule_Interval.CanceledDetect /Campaign_Query_Rule_Interval.ContactsAttempted |
| Problem |
| SIT Tone | The
                                          						number of contacts in the half-hour interval that detected a Special
                                          						Information Tone (SIT). Derived from: Campaign_Query_Rule_Interval.SITToneDetect |
| No Dial tone | The
                                          						number of contacts in the half-hour interval that did not detect a dial tone. Derived from:
                                          						Campaign_Query_Rule_Interval.NoDialToneDetect |
| Fax | The
                                          						number of contacts in the half-hour interval that detected a fax. Derived from: Campaign_Query_Rule_Interval.FaxDetect |
| Network Error | The number of contacts that encountered one of the following problems: No Ringback from network when dial attempted. Network disconnected while alerting. Low Energy ("or dead air") call detected by the dialer. Derived from:
                                          						Campaign_Query_Rule_Interval.NoRingBackDetect |

| Columns (Fields) | Description |
|---|---|
| Campaign | The
                                          						name of the campaign. Derived from: Campaign.CampaignName |
| DateTime | The
                                          						date and time of the start half hour interval for the row's data in MM/DD/YYYY
                                          						(month, day, year) and HH:MM:SS (hours, minutes, seconds) format. Derived from: Campaign_Query_Rule_Interval.DateTime |
| Key
                                             						Statistics |
| Customer Answered | The
                                          						number of the outbound calls (attempts) that reached a live voice. Derived from: Cam paign_Query_Rule_Interval.VoiceDetect +
                                          						Campaign_Query_Rule_Interval.WrongNumberCount +
                                          						Campaign_Query_Rule_Interval.CustomerNotHomeCount +
                                          						Campaign_Query_Rule_Interval.CustomerAbandonDetect +
                                          						Campaign_Query_Rule_Interval.CallbackCount +
                                          						Campaign_Query_Rule_Interval.PersonalCallbackCount +
                                          						Campaign_Query_Rule_Interval.AbandonDetect +
                                          						Campaign_Query_Rule_Interval.AbandonToIVR |
| Right Party Connect | The
                                          						number of call attempts as indicated by agents using their desktop, when
                                          						the actual customer was contacted and handled. Derived from: Campaign_Query_Rule_Interval.VoiceDetect |
| Dialer Abandon & Abandon to IVR | The
                                          						number of calls that were abandoned by the dialer or abandoned to IVR because
                                          						of there were no agents available to take the call. Campaign configuration
                                          						determines whether these calls are abandoned at the dialer or to IVR. Derived from: Campaign_Query_Rule_Interval. AbandonToIVR
                                          						+ Campaign_Query_Rule_Interval. AbandonDetect |
| Attempts |
| Total | The
                                          						total number of outbound calls attempted. Derived from:
                                          						Campaign_Query_Rule_Interval.ContactsAttempted |
| Customer Answered | The
                                          						percentage of attempted calls that reached a live voice. Derived from: (Campaign_Query_Rule_Interval.VoiceDetect +
                                          						Campaign_Query_Rule_Interval.WrongNumberCount +
                                          						Campaign_Query_Rule_Interval.CustomerNotHomeCount +
                                          						Campaign_Query_Rule_Interval.CustomerAbandonDetect +
                                          						Campaign_Query_Rule_Interval.CallbackCount +
                                          						Campaign_Query_Rule_Interval.PersonalCallbackCount +
                                          						Campaign_Query_Rule_Interval.AbandonDetect +
                                          						Campaign_Query_Rule_Interval.AbandonToIVR)/
                                          						Campaign_Query_Rule_Interval.ContactsAttempted |
| Did Not Answer | The
                                          						percentage of calls attempted when the number was dialed but the customer was
                                          						not reached and there were no problems with the call ("Ring No Answer"). Derived from:
                                          						(Campaign_Query_Rule_Interval.AnsweringMachineDetect +
                                          						Campaign_Query_Rule_Interval.BusyDetect +
                                          						Campaign_Query_Rule_Interval.NoAnswerDetect +
                                          						Campaign_Query_Rule_Interval.CancelledDetect/
                                          						Campaign_Query_Rule_Interval.ContactsAttempted |
| Problem | The percentage of calls attempted where the contact was dialed and one of the following problems was encountered: Fax machine detected. No dial tone when dialer port went off hook. No Ringback from network when dial attempted. Network disconnected while alerting. Low Energy ("or dead air") call detected by the dialer. Operator intercept (SIT Tone) was returned from network when dial attempted. Derived from: (Campaign_Query_Rule_Interval.FaxDetect +
                                          						Campaign_Query_Rule_Interval.NoDialToneDetect +
                                          						Campaign_Query_Rule_Interval.NoRingBackDetect +
                                          						Campaign_Query_Rule_Interval.SITToneDetect)/
                                          						Campaign_Query_Rule_Interval.ContactsAttempted |
| Did
                                             						Not Dial |
| Agent Rejected | The number of preview or callback calls in the half-hour interval rejected by the agent. Derived from:
                                          						Campaign_Query_Rule_Interval.AgentRejectedDetect Note: These calls are not counted as attempted. |
| Agent Closed | The number of preview or callback calls rejected by the agent. These customers are not dialed. Derived from:
                                          						Campaign_Query_Rule_Interval.AgentClosedDetect Note:
                                          						These calls are not counted as attempted. |

| Columns (Fields) | Description |
|---|---|
| Campaign | The
                                          						name of the campaign. Derived from: Campaign.CampaignName |
| DateTime | The
                                          						central controller date and time at the start of the half-hour interval. Derived from: Campaign_Query_Rule_Interval.DateTime |
| Attempts | Summary total of the number of calls attempted in the half-hour
                                          						interval. Derived from:
                                          						Campaign_Query_Rule_Interval.ContactsAttempted |
| Requested Callback | The
                                          						number of callback contacts. Derived from: Campaign_Query_Rule_Interval.CallBackCount |
| Requested Personal Callback | The
                                          						number of callback contacts scheduled. Derived from:
                                          						Campaign_Query_Rule_Interval.PersonalCallBackCount |
| Voice | The
                                          						number of contacts for which a voice was detected in the half hour interval. Derived from: Campaign_Query_Rule_Interval.VoiceDetect |
| Busy | The
                                          						number of contacts in the half hour interval that detected a busy signal. Derived from: Campaign_Query_Rule_Interval.BusyDetect |
| No
                                          						Answer | The
                                          						number of contacts in the half hour interval that were not answered. Derived from: Campaign_Query_Rule_Interval.NoAnswerDetect |
| No
                                          						Ringback | The
                                          						number of contacts in the half hour interval that did not detect a ring back.
                                          						The Calls with CallResults 4, 27 and 28 are mentioned in this column. Derived from:
                                          						Campaign_Query_Rule_Interval.NoRingBackDetect |
| No
                                          						Dialtone | The
                                          						number of contacts in the half hour interval that did not detect a dial tone. Derived from:
                                          						Campaign_Query_Rule_Interval.NoDialToneDetect |
| Fax | The
                                          						number of contacts in the half hour interval that detected a fax. Derived from: Campaign_Query_Rule_Interval.FaxDetect |
| Network IVR | The
                                          						number of contacts in the half hour interval that detected a network answering
                                          						machine. Derived from:
                                          						Campaign_Query_Rule_Interval.NetworkAnsMachineDetect |
| Answering Machine | The
                                          						number of contacts in the half hour interval that detected an answering
                                          						machine. Derived from:
                                          						Campaign_Query_Rule_Interval.AnsweringMachineDetect |
| SIT
                                          						Tone | The
                                          						number of contacts in the half hour interval that detected a special
                                          						information tone (SIT). Derived from: Campaign_Query_Rule_Interval.SITToneDetect |
| Agent
                                          						Rejected | The
                                          						number of preview or callback contacts in the half hour interval that were
                                          						rejected by the agent. Derived from:
                                          						Campaign_Query_Rule_Interval.AgentRejectedDetect |
| Agent
                                          						Closed | The
                                          						number of preview or callback contacts that were rejected by the agent. These
                                          						customers are not dialed. Derived from:
                                          						Campaign_Query_Rule_Interval.AgentClosedDetect |
| Customer Not Home | The number of contacts in the half hour interval when the party answering the phone was not the customer. Derived from:
                                          						Campaign_Query_Rule_Interval.CustomerNotHomeCount |
| Wrong
                                          						Number | The number of contacts in the half hour interval when the party answering the phone indicated that the customer did not live
                                          there. Derived from:
                                          						Campaign_Query_Rule_Interval.WrongNumberCount |
| Canceled | The
                                          						number of contacts in the half hour interval where the dialer canceled a
                                          						ringing customer call. Derived from: Campaign_Query_Rule_Interval.CanceledDetect |
| Dialer
                                          						Abandon | The
                                          						number of contacts in the half hour interval abandoned by the dialer. Derived from: Campaign_Query_Rule_Interval.AbandonDetect |
| Abandon to IVR | The
                                          						number of contacts in the half hour interval that were abandoned by the dialer.
                                          						However, instead of hanging up on the customer, the customer was transferred to
                                          						an IVR which plays a message. Derived from: Campaign_Query_Rule_Interval.AbandonToIVR |
| Customer Abandon | The number of contacts in the half hour interval where the customer ended the call immediately after picking up the phone. Derived from:
                                          						Campaign_Query_Rule_Interval.CustomerAbandonDetect |
| Talk
                                          						Time | The
                                          						total time in HH:MM:SS (hours, minutes, seconds) that  agents spent talking on the phone in the half hour interval. Derived from: Campaign_Query_Rule_Interval.TalkTime |
| Wrap Up
                                          						Time | The
                                          						length of time the agents spent in wrap-up work. Derived from: Campaign_Query_Rule_Interval.WrapupTime |

| Columns (Fields) | Description |
|---|---|
| Dialer | The name of the dialer. Derived from: Dialer.DialerName |
| DateTime | The central controller date and time at the start of the half-hour interval. Derived from: Dialer_Interval.DateTime |
| Attempts | Summary total of the number of contacts dialed in the half-hour interval. Derived from: Dialer_Interval.ContactsDialed |
| Requested Callback | The number of callback contacts. Derived from: Dialer_Interval.CallBackCount |
| Requested Personal Callback | The number of callback contacts scheduled. Derived from: Dialer_Interval.PersonalCallBackCount |
| Voice | The number of contacts for which a voice was detected in the half-hour interval. Derived from: Dialer_Interval.VoiceDetect |
| Busy | The number of contacts for which busy signals were detected in the half-hour interval. Derived from: Dialer_Interval.BusyDetect |
| No Answer | The number of contacts which were not answered in the half hour-interval. Derived from: Dialer_Interval.NoAnswerDetect |
| No Ringback | The number of contacts in the half-hour interval that did not detect a ring back. Derived from: Dialer_Interval.NoRingBackDetect |
| No Dialtone | The number of contacts in the half-hour interval that did not detect a dial tone. Derived from: Dialer_Interval.NoDialToneDetect |
| Fax | The number of contacts in the half-hour interval that detected a fax. Derived from: Dialer_Interval.FaxDetect |
| Network IVR | The number of contacts in the half-hour interval that detected a network answering machine. Derived from: Dialer_Interval.NetworkAnsMachineDetect |
| Answering Machine | The number of contacts in the half-hour interval that detected an answering machine. Derived from: Dialer_Interval.AnsweringMachineDetect |
| SIT Tone | The number of contacts in the half-hour interval that detected a special information tone (SIT). Derived from: Dialer_Interval.SITToneDetect |
| Agent Rejected | The number of preview or callback contacts in the half-hour interval that were rejected by the agent. Derived from: Dialer_Interval.AgentRejectedDetect |
| Agent Closed | The number of preview or callback contacts that were rejected by the agent. The agent did not call these customers. Derived from: Dialer_Interval.AgentClosedDetect |
| Customer Not Home | The number of contacts in a half-hour interval where the party answering the phone was not the customer. Derived from: Dialer_Interval.CustomerNotHomeCount |
| Wrong Number | The number of contacts in a half-hour interval where the party answering the phone indicated that the customer did not live
                                          there. Derived from: Dialer_Interval.WrongNumberCount |
| Canceled | The number of contacts in the half-hour interval where the dialer canceled a ringing customer call. Derived from: Dialer_Interval.CancelledDetect |
| Dialer Abandon | The number of contacts in the half-hour interval abandoned by the dialer. Derived from: Dialer_Interval.AbandonDetect |
| Abandon to IVR | The number of contacts in the half-hour interval that were abandoned by the dialer and transferred to IVR, which plays a message. Derived from: Dialer_Interval.AbandonToIVR |
| Customer Abandon | The number of contacts in the half-hour interval where the customer ended the call immediately after picking up the phone. Derived from: Dialer_Interval.CustomerAbandonDetect |

| Columns (Fields) | Description |
|---|---|
| Dialer | The name of the dialer. Derived from: Dialer.DialerName |
| Date | The date for the row's data in MM/DD/YYYY (month, day, year) format. Derived from: Dialer_Interval.DateTime |
| Port Status |
| Ports in Service | The full-time equivalent value of registered dialer ports during the  interval. If this is less than the full number of ports
                                          allocated, then it describes a system issue where ports were offline for some time. Derived from: (Dialer_Interval.IdlePortTime+Dialer_Interval.ReservePortTime + Dialer_Interval.DialingTime)/ Dialer_Interval.ReportingInterval |
| Idle | The percentage of nonbusy ports in the current interval. Derived from: Dialer_Interval.IdlePortTime/ (Dialer_Interval.IdlePortTime + Dialer_Interval.ReservePortTime + Dialer_Interval.DialingTime) |
| Contacting Customers | The percentage of time spent by the dialer ports for calling customers during the current  interval. Derived from: Dialer_Interval.DialingTime /(Dialer_Interval.IdlePortTime + Dialer_Interval.ReservePortTime + Dialer_Interval.DialingTime) |
| Reserved Agents | The percentage of time spent by the dialer ports for reserving agents during the current  interval for an agent campaign. Derived from: Dialer_Interval.ReservePortTime/ (Dialer_Interval.IdlePortTime + Dialer_Interval.ReservePortTime + Dialer_Interval.DialingTime) |
| Out of Ports | The percentage of time maxed out by the dialer during the current interval. Derived from: Dialer_Interval.AllPortsBusyTime/(Dialer_Interval.IdlePortTime + Dialer_Interval.ReservePortTime + Dialer_Interval.DialingTime) |
| Dialer Statistics |
| Attempts | The number of customer contact calls attempted by the dialer during the current  interval. This includes all attempts, whether
                                          customers were reached or not. Derived from: Dialer_Interval.ContactsDialed |
| Avg Attempt Time | The average time length in seconds of a customer attempt. Derived from: Dialer_Interval.DialingTime/Dialer_Interval.ContactsDialed |
| Reservation Calls | The total number of reservation calls placed. This includes dialer requests to reserve agents that were rejected in the routing
                                          script because no agents were available or otherwise. Derived from: Dialer_Interval.ReservationCallAttempts |
| Avg Reservation Time | The average length of a reservation call in seconds. Derived from: Dialer_Interval.ReservePortTime/ Dialer_Interval.ReservationCallAttempts |

| Columns (Fields) | Description |
|---|---|
| Dialer | The name of the dialer. Derived from: Dialer.DialerName |
| DateTime | The date and time of the start of the half-hour interval for the row's data in MM/DD/YYYY (month, day, year) and HH:MM:SS
                                          (hour, minute, second) format. Derived from: Dialer_Interval.DateTime |
| Port Status |
| Ports in Service | The full-time equivalent value of registered dialer ports during the half-hour interval. If this value is less than the full
                                          number of ports allocated, then it describes a system issue where ports were offline for some time. Derived from: (Dialer_Interval.IdlePortTime+Dialer_Interval.ReservePortTime + Dialer_Interval.DialingTime)/ Dialer_Interval.ReportingInterval |
| Idle | The percentage of nonbusy ports in the current half-hour interval. Derived from: Dialer_Interval.IdlePortTime/ (Dialer_Interval.IdlePortTime + Dialer_Interval.ReservePortTime + Dialer_Interval.DialingTime) |
| Contacting Customers | The percentage of time spent by the dialer ports for calling customers during the current half-hour interval. Derived from: Dialer_Interval.DialingTime /(Dialer_Interval.IdlePortTime + Dialer_Interval.ReservePortTime + Dialer_Interval.DialingTime) |
| Reserved Agents | The percentage of time spent by the dialer ports for reserved agents during the current half-hour interval for an agent campaign. Derived from: Dialer_Interval.ReservePortTime/ (Dialer_Interval.IdlePortTime + Dialer_Interval.ReservePortTime + Dialer_Interval.DialingTime) |
| Out of Ports | The percentage of time maxed out by the dialer during the current half-hour interval. Derived from: Dialer_Interval.AllPortsBusyTime/(Dialer_Interval.IdlePortTime + Dialer_Interval.ReservePortTime + Dialer_Interval.DialingTime) |
| Dialer Statistics: Attempts | The number of customer contact calls attempted by the dialer during the current half-hour interval. This number includes all
                                          attempts, whether customers were reached or not. Derived from: Dialer_Interval.ContactsDialed |
| Dialer Statistics |
| Attempts | The number of customer contact calls attempted by the dialer during the current  half-hour interval. This includes all attempts,
                                          whether customers were reached or not. Derived from: Dialer_Interval.ContactsDialed |
| Avg Attempt Time | The average time length of a customer attempt in seconds. Derived from: Dialer_Interval.DialingTime/Dialer_Interval.ContactsDialed |
| Reservation Calls | The total number of reservation calls placed the current half-hour interval. This number includes dialer requests to reserve
                                          agents that were rejected in the routing script because no agents were available or otherwise. Derived from: Dialer_Interval.ReservationCallAttempts |
| Avg Reservation Calls | The average length of a reservation call in seconds. Derived from: Dialer_Interval.ReservePortTime / Dialer_Interval.ReservationCallAttempts |

| Columns (Fields) | Description |
|---|---|
| Import | The name of the import rule. Derived from: Import_Rule.ImportRuleName |
| Start Date | The date and time the import rule is scheduled to start. Derived from: Import_Rule_History.StartDateTime |
| End Date | The date and time the import rule finished. Derived from: Import_Rule_History.EndDateTime |
| Duration | The total time duration. Derived from: DateDiff(ss,Import_Rule_History.StartDateTime, Import_Rule_History.EndDateTime) |
| Records Status |
| Total Records | The total number of records present in the import list. Derived from: Import_Rule_History.TotalRecords |
| Imported | The total number of records imported into the Do Not Call List. Derived from: Import_Rule_History.GoodRecords |
| Failed | The total number of import records that did not meet format criteria. These records are captured in an import error file. Derived from: Import_Rule_History.BadRecords |
|  |
| Records To Dial | The total number of records imported to dialing lists based on existing query rules. Derived from: Import_Rule_History. ImportedToDialingListCount |
| Records With Unknown Prefix | The total number of records that did not match the prefixes in the region prefix table and were assigned with the default
                                          time zone for the campaign. Derived from: Import_Rule_History.UnmatchedRegionPrefixCount |

| Columns
                                          						(Fields) | Description |
|---|---|
| Campaign | The name
                                          						of the campaign. Derived
                                          						from: Campaign.CampaignName |
| Query
                                          						Rule | The name
                                          						of the query rule. Derived
                                          						from: Query_Rule.QueryRuleName |
| Date | The date for the record in MM/DD/YYYY (month, day, year) format. Derived from: Campaign_Query_Rule_Interval.DateTime |
| Attempts | The
                                          						total number of outbound calls attempted. Derived
                                          						from: Campaign_Query_Rule_Interval.ContactsAttempted |
| Customer
                                             						Answered |
| Right Party Connect | The percentage of call attempts as indicated by agents using their desktop, when the
                                          						actual customer was contacted and handled. Derived
                                          						from: Campaign_Query_Rule_Interval.VoiceDetect/
                                          						Campaign_Query_Rule_Interval.ContactsAttempted |
| Dialer Abandon | The percentage of contacts or attempts abandoned by the dialer
                                          						because of no agent was available to take the call and "Abandon to IVR" was not
                                          						configured. Derived
                                          						from: Campaign_Query_Rule_Interval. AbandonDetect/
                                          						Campaign_Query_Rule_Interval.ContactsAttempted |
| Abandon to IVR | The
                                          						percentage of attempts that were sent to IVR (or another dialed number) for
                                          						treatment after the dialer reached a contact and no agent was available to take
                                          						the call. Derived from: Campaign_Query_Rule_Interval. AbandonToIVR/
                                          						Campaign_Query_Rule_Interval.ContactsAttempted |
| Callback | The percentage of callbacks requested by the customer when the campaign is not
                                          						configured for personal callback. Derived from: Campaign_Query_Rule_Interval.CallbackCount/
                                          						Campaign_Query_Rule_Interval.ContactsAttempted |
| Personal Callback | The percentage of callback scheduled and requested by the customer when the campaign
                                          						was configured for personal callback. Derived from:
                                          						Campaign_Query_Rule_Interval.PersonalCallbackCount/
                                          						Campaign_Query_Rule_Interval.ContactsAttempted |
| Customer Not Home | The percentage of contacts where the party answering the
                                          						phone was not the customer. Derived from:
                                          						Campaign_Query_Rule_Interval.CustomerNotHomeCount/
                                          						Campaign_Query_Rule_Interval.ContactsAttempted |
| Wrong Number | The percentage of contacts where the party answering the
                                          						phone indicated that the customer did not live there. Derived from:
                                          						Campaign_Query_Rule_Interval.WrongNumberCount/
                                          						Campaign_Query_Rule_Interval.ContactsAttempted |
| Customer Abandon | The percentage of contacts where the customer ended the call immediately after being connected to an agent. Derived from:
                                          						Campaign_Query_Rule_Interval.CustomerAbandonDetect/
                                          						Campaign_Query_Rule_Interval.ContactsAttempted |
| Customer Did Not Answer |
| Answering Machine | The percentage of contacts that detected an answering machine. Derived from: Campaign_Query_Rule_Interval.AnsweringMachineDetect |
| No Answer | The percentage of contacts that were not answered. Derived from: Campaign_Query_Rule_Interval.
                                          						NoAnswerDetect/ Campaign_Query_Rule_Interval.ContactsAttempted |
| Busy | The percentage of contacts that detected a busy signal. Derived from: Campaign_Query_Rule_Interval. BusyDetect/
                                          						Campaign_Query_Rule_Interval.ContactsAttempted |
| Canceled | The percentage of contacts where the dialer canceled a
                                          						ringing customer call. Derived from:
                                          						Campaign_Query_Rule_Interval.CanceledDetect/
                                          						Campaign_Query_Rule_Interval.ContactsAttempted |
| Problem |
| SIT Tone | The percentage of contacts that detected a Special
                                          						Information Tone (SIT). Derived from: Campaign_Query_Rule_Interval.SITToneDetect |
| No Dial tone | The percentage of contacts that did not detect a dial tone. Derived from:
                                          						Campaign_Query_Rule_Interval.NoDialToneDetect |
| Fax | The percentage of contacts that detected a fax machine. Derived from: Campaign_Query_Rule_Interval.FaxDetect |
| Network Error | The number of contacts that encountered one of the following problems: No Ringback from network when dial attempted. Network disconnected while alerting. Low Energy ("or dead air") call detected by the dialer. Derived from:
                                          						Campaign_Query_Rule_Interval.NoRingBackDetect |

| Columns
                                          						(Fields) | Description |
|---|---|
| Campaign | The name
                                          						of the campaign. Derived
                                          						from: Campaign.CampaignName |
| Query
                                          						Rule | The name
                                          						of the query rule. Derived
                                          						from: Query_Rule.QueryRuleName |
| Date | The date for the row's data in MM/DD/YYYY (month, day, year) format. Derived
                                          						from: Campaign_Query_Rule_Interval.DateTime |
| Key
                                             						Statistics |
| Customer Answered | The
                                          						number of the outbound calls (attempts) that reached a live voice. Derived
                                          						from: Campaign_Query_Rule_Interval.VoiceDetect +
                                          						Campaign_Query_Rule_Interval.WrongNumberCount +
                                          						Campaign_Query_Rule_Interval.CustomerNotHomeCount +
                                          						Campaign_Query_Rule_Interval.CustomerAbandonDetect +
                                          						Campaign_Query_Rule_Interval.CallbackCount +
                                          						Campaign_Query_Rule_Interval.PersonalCallbackCount +
                                          						Campaign_Query_Rule_Interval.AbandonDetect +
                                          						Campaign_Query_Rule_Interval.AbandonToIVR |
| Right Party Connect | The
                                          						number of call attempts as indicated by agents using their desktop, when
                                          						the actual customer was contacted and handled. Derived
                                          						from: Campaign_Query_Rule_Interval.VoiceDetect |
| Dialer Abandon & Abandon to IVR | The
                                          						number of calls that were abandoned by the dialer or abandoned to IVR because
                                          						there were no agents available to take the call. Campaign configuration
                                          						determines whether these calls are abandoned at the dialer or to IVR. Dialer
                                          						Abandon is derived from: Campaign_Query_Rule_Interval.AbandonDetect Abandon to
                                          						IVR is derived from: Campaign_Query_Rule_Interval.AbandonToIVR |
| Attempts |
| Total | The total number of outbound calls attempted. Derived from: Campaign_Query_Rule_Interval.ContactsAttempted |
| Customer Answered | The
                                          						percentage of attempted calls that reached a live voice. Derived
                                          						from: (Campaign_Query_Rule_Interval.VoiceDetect +
                                          						Campaign_Query_Rule_Interval.WrongNumberCount +
                                          						Campaign_Query_Rule_Interval.CustomerNotHomeCount +
                                          						Campaign_Query_Rule_Interval.CustomerAbandonDetect +
                                          						Campaign_Query_Rule_Interval.CallbackCount +
                                          						Campaign_Query_Rule_Interval.PersonalCallbackCount +
                                          						Campaign_Query_Rule_Interval.AbandonDetect +
                                          						Campaign_Query_Rule_Interval.AbandonToIVR)/
                                          						Campaign_Query_Rule_Interval.ContactsAttempted |
| Did Not Answer | The
                                          						percentage of calls attempted when the number was dialed but the customer (live
                                          						voice) was not reached and there were no problems with the call ("Ring No
                                          						Answer"). Derived
                                          						from: (Campaign_Query_Rule_Interval. AnsweringMachineDetect +
                                          						Campaign_Query_Rule_Interval.BusyDetect +
                                          						Campaign_Query_Rule_Interval.NoAnswerDetect +
                                          						Campaign_Query_Rule_Interval.CancelledDetect)/
                                          						Campaign_Query_Rule_Interval.ContactsAttempted |
| Problem | The percentage of calls attempted where the contact was dialed and one of the following problems was encountered: Fax machine detected. No dial tone when dialer port went off hook. No Ringback from network when dial attempted. Network disconnected while alerting. Low Energy ("or dead air") call detected by the dialer. Operator intercept (SIT Tone) was returned from network when dial attempted. Derived
                                          						from: (Campaign_Query_Rule_Interval.FaxDetect +
                                          						Campaign_Query_Rule_Interval.NoDialToneDetect +
                                          						Campaign_Query_Rule_Interval.NoRingBackDetect +
                                          						Campaign_Query_Rule_Interval.SITToneDetect)/
                                          						Campaign_Query_Rule_Interval.ContactsAttempted |
| Did Not
                                             						Dial |  |
| Agent Rejected | The
                                          						number of preview or callback calls that were rejected
                                          						by the agent. Derived
                                          						from: Campaign_Query_Rule_Interval.AgentRejectedDetect |
| Agent Closed | The
                                          						number of preview or callback calls that were rejected by the agent. 
                                          					 The agent did not call these customers. Derived
                                          						from: Campaign_Query_Rule_Interval.AgentClosedDetect Note
                                          						that these calls were not counted as attempted. |

| Columns (Fields) | Description |
|---|---|
| Campaign | The
                                          						name of the campaign. Derived from: Campaign.CampaignName |
| Query
                                          						Rule | The
                                          						name of the query rule. Derived from: Query_Rule.QueryRuleName |
| DateTime | The date and time of the start of the half-hour interval for the row's data in MM/DD/YYYY (month, day, year) and HH:MM:SS
                                          (hour, minute, second) format. Derived from: Campaign_Query_Rule_Interval.DateTime |
| Attempts | The
                                          						total number of outbound calls attempted. Derived from:
                                          						Campaign_Query_Rule_Interval.ContactsAttempted |
| Customers Answered |
| Right Party Connect | The percentage of call attempts as indicated by agents using their desktop, when the
                                          						actual customer was contacted and handled. Derived from: Campaign_Query_Rule_Interval.VoiceDetect /Campaign_Query_Rule_Interval.ContactsAttempted |
| Dialer Abandon | The percentage of contacts or attempts in the half-hour interval abandoned by the dialer
                                          						because no agents were available and "Abandon to IVR" was not
                                          						configured. Derived from: Campaign_Query_Rule_Interval.
                                          						AbandonDetect/Campaign_Query_Rule_Interval.ContactsAttempted Note: This column is calculated as a percentage of all attempts because all the
                                          						remaining numbers are represented in percentage only. These columns always add
                                          						up to 100%. |
| Abandon to IVR | The percentage of attempts that
                                          						were sent to IVR (or another dialed number) for treatment after the dialer
                                          						reached a contact and no agent was available to take the call. Derived from: Campaign_Query_Rule_Interval.
                                          						AbandonToIVR/Campaign_Query_Rule_Interval.ContactsAttempted |
| Callback | The percentage of callbacks requested by the customer when the campaign is not
                                          						configured for personal callback. Derived from: Campaign_Query_Rule_Interval.CallbackCount/
                                          						Campaign_Query_Rule_Interval.ContactsAttempted |
| Personal Callback | The percentage of callbacks scheduled and requested by the customer when the campaign
                                          						was configured for personal callback. Derived from:
                                          						Campaign_Query_Rule_Interval.PersonalCallbackCount/
                                          						Campaign_Query_Rule_Interval.ContactsAttempted |
| Customers Not Home | The percentage of contacts in the half-hour interval where the party answering the
                                          						phone was not the customer. Derived from:
                                          						Campaign_Query_Rule_Interval.CustomersNotHomeCount/
                                          						Campaign_Query_Rule_Interval.ContactsAttempted |
| Wrong Number | The percentage of contacts in the half-hour interval where the party answering the
                                          						phone indicated that the customer did not live there. Derived from:
                                          						Campaign_Query_Rule_Interval.WrongNumberCount/
                                          						Campaign_Query_Rule_Interval.ContactsAttempted |
| Customer Abandon | The percentage of contacts in the half-hour interval where the customer ended the call immediately after being connected to
                                          an agent. Derived from:
                                          						Campaign_Query_Rule_Interval.CustomerAbandonDetect/
                                          						Campaign_Query_Rule_Interval.ContactsAttempted |
| Customers Did Not Answer |
| Answering Machine | The percentage of contacts in the half-hour interval that detected an answering
                                          						machine. Derived from: Campaign_Query_Rule_Interval.
                                          						AnsweringMachineDetectToHal/
                                          						Campaign_Query_Rule_Interval.ContactsAttempted |
| No Answer | The percentage of contacts in the half-hour interval that were not answered. Derived from: Campaign_Query_Rule_Interval.
                                          						NoAnswerDetect/ Campaign_Query_Rule_Interval.ContactsAttempted |
| Busy | The percentage of contacts in the half-hour interval that detected a busy signal. Derived from: Campaign_Query_Rule_Interval. BusyDetect/
                                          						Campaign_Query_Rule_Interval.ContactsAttempted |
| Canceled | The percentage of contacts in the half-hour interval where the dialer canceled a
                                          						ringing customer call. Derived from:
                                          						Campaign_Query_Rule_Interval.CanceledDetect/
                                          						Campaign_Query_Rule_Interval.ContactsAttempted |
| Problem |
| SIT Tone | The
                                          						number of contacts in the half-hour interval that detected a Special
                                          						Information Tone (SIT). Derived from: Campaign_Query_Rule_Interval.SITToneDetect |
| No Dialtone | The
                                          						number of contacts in the half-hour interval that did not detect a dial tone. Derived from:
                                          						Campaign_Query_Rule_Interval.NoDialToneDetect |
| Fax | The
                                          						number of contacts in the half-hour interval that detected a fax machine. Derived from: Campaign_Query_Rule_Interval.FaxDetect |
| Network Error | The number of contacts that encountered one of the following problems: No Ringback from network when dial attempted Network disconnected while alerting Low Energy ("or dead air") call detected by the dialer. Derived from:
                                          						Campaign_Query_Rule_Interval.NoRingBackDetect |

| Columns
                                          						(Fields) | Description |
|---|---|
| Campaign | The name
                                          						of the campaign. Derived
                                          						from: Campaign.CampaignName |
| Query
                                          						Rule | The name
                                          						of the query rule. Derived
                                          						from: Query_Rule.QueryRuleName |
| DateTime | The
                                          						central controller date and time at the start of the half-hour interval. Derived
                                          						from: Campaign_Query_Rule_Interval.DateTime |
| Attempts | Summary
                                          						total of the number of calls attempted in the half-hour interval. Derived
                                          						from: Campaign_Query_Rule_Interval.ContactsAttempted |
| Requested Callback | The
                                          						number of callback contacts. Derived
                                          						from: Campaign_Query_Rule_Interval.CallBackCount |
| Requested Personal Callback | The
                                          						number of callback contacts scheduled. Derived
                                          						from: Campaign_Query_Rule_Interval.PersonalCallbackCount |
| Voice | The
                                          						number of contacts for which a voice was detected during the half-hour
                                          						interval. Derived
                                          						from: Campaign_Query_Rule_Interval.VoiceDetect |
| Busy | The
                                          						number of contacts in the half-hour interval that detected a busy signal. Derived
                                          						from: Campaign_Query_Rule_Interval.BusyDetect |
| No
                                          						Answer | The
                                          						number of contacts in the half-hour interval that were not answered. Derived
                                          						from: Campaign_Query_Rule_Interval.NoAnswerDetect |
| No
                                          						Ringback | The
                                          						number of contacts in the half-hour interval that did not detect a ring back.
                                          						The Calls with CallResults 4, 27 and 28 are mentioned in this column. Derived
                                          						from: Campaign_Query_Rule_Interval.NoRingBackDetect |
| No
                                          						Dialtone | The
                                          						number of contacts in the half-hour interval that did not detect a dial tone. Derived
                                          						from: Campaign_Query_Rule_Interval.NoDialToneDetect |
| Fax | The
                                          						number of contacts in the half-hour interval that detected a fax. Derived
                                          						from: Campaign_Query_Rule_Interval.FaxDetect |
| Network
                                          						IVR | The
                                          						number of contacts in the half-hour interval that detected a network answering
                                          						machine. Derived from:
                                          						Campaign_Query_Rule_Interval.NetworkAnsMachineDetect |
| Answering Machine | The
                                          						number of contacts in the half-hour interval that detected an answering
                                          						machine. Derived from:
                                          						Campaign_Query_Rule_Interval.AnsweringMachineDetect |
| SIT
                                          						Tone | The
                                          						number of contacts in the half-hour interval that detected a special
                                          						information tone (SIT). Derived from: Campaign_Query_Rule_Interval.SITToneDetect |
| Agent
                                          						Rejected | The
                                          						number of preview or callback contacts in the half-hour interval that were
                                          						rejected by the agent. Derived from:
                                          						Campaign_Query_Rule_Interval.AgentRejectedDetect |
| Agent
                                          						Closed | The
                                          						number of preview or callback contacts that were rejected by the agent. (The agent did not call these customers.) Derived from:
                                          						Campaign_Query_Rule_Interval.AgentClosedDetect |
| Customer Not Home | The
                                          						number of contacts in the half-hour interval where the party answering the
                                          						phone was not the customer. Derived from:
                                          						Campaign_Query_Rule_Interval.CustomerNotHomeCount |
| Wrong
                                          						Number | The
                                          						number of contacts in the half-hour interval where the party answering the
                                          						phone indicated the customer didn't live there. Derived from:
                                          						Campaign_Query_Rule_Interval.WrongNumberCount |
| Canceled | The
                                          						number of contacts in the half-hour interval where the dialer canceled a
                                          						ringing customer call. Derived from: Campaign_Query_Rule_Interval.CanceledDetect |
| Dialer
                                          						Abandon | The
                                          						number of contacts in the half-hour interval abandoned by the dialer. Derived from: Campaign_Query_Rule_Interval.AbandonDetect |
| Abandon to IVR | The
                                          						number of contacts in the half-hour interval that were abandoned by the dialer and  transferred to IVR, which plays
                                          a message. Derived from: Campaign_Query_Rule_Interval.AbandonToIVR |
| Customer Abandon | The number of contacts in the half-hour interval where the customer ended the call immediately after picking up the phone. Derived from:
                                          						Campaign_Query_Rule_Interval.CustomerAbandonDetect |
| Talk
                                          						Time | The
                                          						total time in HH:MM:SS (hours, minutes, seconds) that agents spent talking on
                                          						the phone in the half-hour interval. Derived from: Campaign_Query_Rule_Interval.TalkTime |
| Wrap Up
                                          						Time | The
                                          						length of time the agents spent in wrap-up work. Derived from: Campaign_Query_Rule_Interval.WrapupTime |

| Columns (Fields) | Description |
|---|---|
| Campaign | The
                                          						name of the campaign. Derived from: Campaign.CampaignName |
| Query
                                          						Rule | The
                                          						name of the query rule. Derived from: Query_Rule.QueryRuleName |
| DateTime | The
                                          						date and time at the start of the half-hour interval for the row's data in
                                          						MM/DD/YYYY (month, day, year) and HH:MM:SS (hours, minutes, seconds) format. Derived from: Campaign_Query_Rule_Interval.DateTime |
| Key
                                             						Statistics |
| Customer Answered | The
                                          						number of the outbound calls (attempts) that reached a live voice. Derived from: Campaign_Query_Rule_Interval.VoiceDetect +
                                          						Campaign_Query_Rule_Interval.WrongNumberCount +
                                          						Campaign_Query_Rule_Interval.CustomerNotHomeCount +
                                          						Campaign_Query_Rule_Interval.CustomerAbandonDetect +
                                          						Campaign_Query_Rule_Interval.CallbackCount
                                          						+Campaign_Query_Rule_Interval.PersonalCallbackCount +
                                          						Campaign_Query_Rule_Interval.AbandonDetect +
                                          						Campaign_Query_Rule_Interval.AbandonToIVR |
| Right Party Connect | The
                                          						number of call attempts as indicated by agents using their desktop, when
                                          						the actual customer was contacted and handled. Derived from: Derived from:
                                          						Campaign_Query_Rule_Interval.VoiceDetect |
| Dialer Abandon & Abandon to IVR | The
                                          						number of calls that were abandoned by the dialer or abandoned to IVR because
                                          						there were no agents available to take the call. Campaign configuration
                                          						determines whether these calls are abandoned at the dialer or to IVR. Dialer
                                          						Abandon is derived from: Campaign_Query_Rule_Interval.AbandonDetect AbandtoIVR is derived from: Campaign_Query_Rule_Interval.AbandonToIVR |
| Attempts |
| Total | The
                                          						total number of outbound calls attempted. Derived from:
                                          						Campaign_Query_Rule_Interval.ContactsAttempted |
| Customer Answered | The
                                          						percentage of attempted calls that reached a live voice. Derived from: (Campaign_Query_Rule_Interval.VoiceDetect +
                                          						Campaign_Query_Rule_Interval.WrongNumberCount +
                                          						Campaign_Query_Rule_Interval.CustomerNotHomeCount +
                                          						Campaign_Query_Rule_Interval.CustomerAbandonDetect +
                                          						Campaign_Query_Rule_Interval.CallbackCount +
                                          						Campaign_Query_Rule_Interval.PersonalCallbackCount +
                                          						Campaign_Query_Rule_Interval.AbandonDetect +
                                          						Campaign_Query_Rule_Interval.AbandonToIVR)/
                                          						Campaign_Query_Rule_Interval.ContactsAttempted |
| Did Not Answer | The
                                          						percentage of calls attempted when the number was dialed but the customer (live
                                          						voice) was not reached and there were no problems with the call ("Ring No
                                          						Answer"). Derived from: (Campaign_Query_Rule_Interval.
                                          						AnsweringMachineDetect + Campaign_Query_Rule_Interval.BusyDetect +
                                          						Campaign_Query_Rule_Interval.NoAnswerDetect +
                                          						Campaign_Query_Rule_Interval.CancelledDetect)/
                                          						Campaign_Query_Rule_Interval.ContactsAttempted |
| Problem | The percentage of calls attempted where the contact was dialed and one of the following problems was encountered: Fax machine detected. No dial tone when dialer port went off hook. No Ringback from network when dial attempted. Network disconnected while alerting. Low Energy ("or dead air") call detected by the dialer. Operator intercept (SIT Tone) was returned from network when dial attempted. Derived from: (Campaign_Query_Rule_Interval.FaxDetect +
                                          						Campaign_Query_Rule_Interval.NoDialToneDetect +
                                          						Campaign_Query_Rule_Interval.NoRingBackDetect +
                                          						Campaign_Query_Rule_Interval.SITToneDetect)/
                                          						Campaign_Query_Rule_Interval.ContactsAttempted |
| Did
                                             						Not Dial |
| Agent Rejected | The
                                          						number of preview or callback calls in the half-hour interval that were rejected
                                          						by the agent. Derived from:
                                          						Campaign_Query_Rule_Interval.AgentRejectedDetect Note:
                                          						These calls are not counted as attempted. |
| Agent Closed | The
                                          						number of preview or callback calls that were rejected by the agent (these
                                          						customers are not dialed). Derived from:
                                          						Campaign_Query_Rule_Interval.AgentClosedDetect Note: These calls are not counted as attempted. |