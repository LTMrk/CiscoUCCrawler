---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-crs-express-12-5-user-guide-uccx-b-unified-ccx-r-220ad2426d
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/crs/express_12_5/user/guide/uccx_b_unified-ccx-reporting-user-guide-125/uccx_b_unified-ccx-reporting-user-guide-125_chapter_01001.html
retrieved_at: 2026-08-16T21:26:48.866327+00:00
---

Cisco Unified Contact Center Express Reporting User Guide, Release 12.5(1)

# Cisco Unified Contact Center Express Reporting User Guide, Release 12.5(1)

Updated: January 31, 2020

Chapter: FAQs

## Chapter: FAQs

# FAQs

## Overview

This chapter presents reporting-related Frequently Asked Questions
                              		  (FAQs).

ACDR—AgentConnectionDetail record in the AgentConnectionDetail
                                       				table

ASDR—AgentStateDetail record in the AgentStateDetail table

CCDR—ContactCallDetail record in the ContactCallDetail table

CQDR—ContactQueueDetail record in the ContactQueueDetail table

CRDR—ContactRoutingDetail record in the ContactRoutingDetail table

## General

Q.

A.

The number of days is
                                          				  calculated by an SQL function that counts the number of calendar days.
                                          				  Fractions of a day are counted as an entire day. This table provides an
                                          				  example.

Time Range

Number of Days

10
                                                      								a.m. (1000) on 5/15 to 10 a.m. (1000) on 5/16

Two days

12:00:00 a.m. (0000) on 5/15 to 11:59:59 p.m. (1159:59) on 5/15

One day

12:00:00 a.m. (0000) on 5/15 to 12:00:00 a.m. (0000) on 5/16

Two days

Q.

A.

When reason
                                          				  codes are configured, agents enter the reason codes when explicitly
                                          				  transitioning to Logout state or to Not Ready state. These reason codes are
                                          				  stored in the ASDR.

Agent Login Logout Activity Report —Presents the
                                                   						logout reason code in detail.

Agent Not Ready Reason Code Summary Report —Presents
                                                   						summary information for the Not Ready reason code.

Agent State Detail Report —Presents Logout reason code
                                                   						and Not Ready reason code in detail.

Not
                                                         						Ready codes are systemwide and cannot be configured to be hidden from certain
                                                         						agents.

In the
                                          				  following cases, reason codes are not stored. In these cases, the reasonCode
                                          				  field in the ASDR contains a value of –1.

Case

Agent State in ASDR

Browser crashes

Logout

Agent logs out when logged in to another computer or phone

Logout

Normal agent login

Not Ready

Agent receives an IVR call on the ICD extension, fails to
                                                         								answer, and that results in RNA

Not Ready

Agent goes off-hook on ICD extension to place a call

Not Ready

Agent fails to answer an ACD call within the specified timeout
                                                         								period

Not Ready

Agent does not answer an ICD call

Not Ready

Agent’s phone goes down

Not Ready or Logout

Supervisor changes the agent’s state from the Cisco Finesse
                                                         								Supervisor Desktop

Not Ready or Logout

Q.

A.

Unified CCX
                                          				  uses IBM Informix Dynamic Server (IDS) database.

Q.

A.

The
                                          				  information that was in this report is distributed among the Contact
                                             					 Service Queue Service Level Priority Summary Report , the Contact
                                             					 Service Queue Activity Report , and the Contact
                                             					 Service Queue Call Distribution Summary Report .

Q.

A.

The
                                          				  information that was in this report is available in the Contact
                                             					 Service Queue Activity Report or in the Contact
                                             					 Service Queue Activity Report when filtered to show Skill Groups only.

Q.

A.

A call
                                                   						is conferenced to a CTI route point.

A call
                                                   						rings at an agent's phone, but the agent does not pick up. The call is
                                                   						categorized as Ring No Answer (RNA) to the agent.

Q.

A.

The length
                                          				  of each parameter to the report must not exceed 800 characters. If the selected
                                          				  parameters exceed this value, then the database server truncates the parameter
                                          				  to the first 800 characters.

The stored
                                          				  procedure receives only the first 800 characters of the chosen parameters; the
                                          				  rest are not included in the generated report.

Q.

A.

Use
                                          				  third-party database administration tools such as SQuirreL SQL Client or AGS
                                          				  Server Studio to export Unified CCX historical data to your own data warehouse.
                                          				  Use uccxhruser as the username to connect to db_cra
                                          				  database.

Q.

A.

No, it is
                                          				  not supported with embedded Unified Intelligence Center but is supported with
                                          				  standalone Unified Intelligence Center.

Q.

A.

Yes, but
                                          				  it should be used with discretion keeping in mind the impact on the system.

## Availability of
                        	 Reporting Data

Q.

A.

The Contact Service Queue Activity Report by Interval shows this information. To generate this report for one-hour intervals, set its
                                          				  Interval Length filter parameter to sixty (60) minute intervals.

Q.

A.

The Call ANI
                                          				  fields on the Abandoned Call Detail Activity Report and the Agent Detail Report show this information.

Q.

A.

The scenario appears in the following reports:

The Agent Detail Report shows two lines:

For the agent who did not answer the call—Ring time is greater than 0; talk time, hold time, and work time are each zero.

For the agent who answered the call—Talk time is greater than 0.

The Agent Summary Report shows the following:

The call was presented to the agent who did not answer the call, but was not handled by that agent.

The call was presented to and handled by the agent who answered the call.

The CSQ Agent Summary Report shows the call as Ring No Answer (RNA) for the first agent.

Q.

A.

The
                                          				  following fields identify the various legs of a call:

The sessionID fields in the Unified CCX database tables contain the same value for a particular call. These fields identify
                                                all the database records that relate to a call.

The sessionSeqNum fields in the Unified CCX database tables start at 0 and increment by 1 for each leg of a call.

The startDateTime field of the CCDR stores the start time of a call. The sessionSeqNum is equal to 0, and the sessionID value
                                                identifies the call.

The endDateTime field of the CCDR with the highest sessionSeqNum and the same sessionID value stores the end time of a call.

Q.

A.

You can
                                          				  create a custom report to show menu choices. Use the Set Session Info step in a workflow to store the
                                          				  custom variables entered by the callers. The contents of such custom variables
                                          				  are stored in the customVariable fields in the CCDR. Use the information in the
                                          				  CCDR customVariable fields when you create custom reports.

The
                                          				  following is an example of how to prepare a report to show information for a
                                          				  menu with three choices (1, 2, and 3):

For a workflow, define a variable of type session and name it this_session .

Place a Get Contact Info step at the beginning of the workflow.

Set the Session attribute to variable this_session .

Define a Menu step that has three branches and place a Set Enterprise Call Info step in each branch.

In the General tab of the Set Enterprise Call Info step, click Add .

In the branch for caller-choice 1, enter 1 in the Value field, and choose Call.PeripheralVariable1 from the Name drop-down list.

In the branch for caller-choice 2, enter 2 in the Value field, and choose Call.PeripheralVariable2 from the Name drop-down list.

In the branch for caller-choice 3, enter 3 in the Value field, and choose Call.PeripheralVariable3 from the Name drop-down list.

Create a custom report that will show the values of the customVariable1, customVariable2, and customVariable3 fields in the
                                                CCDR.

If calls
                                          				  are to be transferred between workflows and multiple menu choices can be made
                                          				  for a single session, take care to preserve previously entered menu choices.
                                          				  For example, place a Get Session Info step at the beginning of the
                                          				  workflow. If the _ccdrVar1 variable is null, there were no previous entries. If
                                          				  it is not null, when you add a new choice, determine a format for associating a
                                          				  menu choice to a sequence number. In this way, you will be able to prepare
                                          				  accurate reports.

Q.

A.

Yes.

Q.

A.

There are
                                          				  no reports available, but the Unified CCX databases store this data. You can
                                          				  create a custom report to show this information.

Q.

A.

The Detailed Call CSQ Agent Report has information about
                                          				  transferred calls. The session ID remains the same for a transferred call, but
                                          				  the session sequence number increments by 1. This report also shows the agent
                                          				  who handled each call, and the CSQ to which the call was routed.

Q.

A.

Call records (CCDR, CRDR, CQDR) are written after each call is completed.

Agent state records (ASDR) are written after agents change state.

Agent connection records (ACDR) are written when an agent leaves Work state or after the call completes if the agent does
                                                not go to Work state.

Q.

A.

The system
                                          				  stores detailed data. It does not summarize detailed tables to create daily,
                                          				  weekly, or monthly tables.

Q.

A.

The Contact Service Queue Activity by CSQ or Contact Service Queue Activity by Interval shows
                                          				  information about service levels provided to handled calls. Schedule the Contact Service Queue Activity by CSQ or Contact Service Queue Activity by Interval to run
                                          				  monthly.

Q.

A.

Yes. For
                                          				  more information about creating custom reports, see the "Create Custom Reports"
                                          				  section of Cisco Unified Contact
                                                   				  Center Express Report Developer Guide ,
                                          				  located at:

https://www.cisco.com/en/US/products/sw/custcosw/ps1846/products_installation_and_configuration_guides_list.html .

## Data
                        	 Reconciliation Among Reports

Q.

A.

The CSQ
                                          				  reports show calls that are handled by agents after the calls are queued for a
                                          				  CSQ. The Detailed Call by Call CCDR Report shows these calls
                                          				  and also the calls that are marked as handled by a workflow script before they
                                          				  are queued for a CSQ.

Q.

A.

An
                                                   						incoming call can invoke multiple applications because each leg of the call
                                                   						invokes a different application. The call is counted once for each application.

Calls
                                                   						that are hung up before being queued for any CSQ are marked as handled or
                                                   						abandoned depending on the workflow, and also depending on when they are hung
                                                   						up. Such calls do not have CRDRs or ACDRs and will not be counted for CSQ
                                                   						reports or agent reports. These calls will be counted for the Application Performance Analysis Report because the
                                                   						calls entered an application.

Q.

A.

Conference
                                          				  calls to agents result in one CRDR that has multiple ACDRs. The Agent Summary Report counts the number of ACDRs, but
                                          				  the CSQ reports count the number of CRDRs.

Q.

A.

To identify
                                          				  conference calls, search for ACDRs with the same session ID and sequence
                                          				  number, with different agent IDs, and with talk time greater than 0.

Q.

A.

To identify calls that were
                                          				  not answered by an agent, search for ACDRs with talk time equal to zero. The CSQ Agent Summary Report shows the total number of
                                          				  Ring No Answer (RNA) calls for each agent and for each CSQ. In the Agent Summary Report , the number of Ring No Answer
                                          				  calls = Calls Presented – Calls Handled.

Q.

A.

The CSQ reports, including
                                          				  the Contact Service Queue Activity Report show activity
                                          				  at the CSQ level. The agent reports, including the Agent Summary Report , show activity at the agent
                                          				  level.

For handled calls, the Agent Summary Report counts the ACDRs with non-zero
                                          				  talk time (to exclude unanswered calls), and the Contact Service Queue Activity Report counts CQDRs
                                          				  with disposition equal to 2 (handled).

The number of such ACDRs may be larger than the number of such
                                          				  CQDRs for any of the following reasons:

If you
                                                						choose all the agents for the Agent Summary Report , but choose only one CSQ for the Contact Service Queue Activity Report , the Agent Summary Report will show more handled calls.

There
                                                						may be conference calls that involve multiple agents. In such cases, one CQDR
                                                						has multiple associated ACDRs. An associated ACDR has the same sessionID and
                                                						sessionSeqNum as the CQDR.

Agent-to-Agent transfers will result in more ACDRs than CQDRs.
                                                						If Agent1 picks up a call from CSQ1, one CQDR and one ACDR are created. When
                                                						Agent1 transfers the call to Agent2, another ACDR is created, but no CQDR is
                                                						created.

Q.

A.

The Application Performance Analysis Report shows the
                                          				  highest number of presented calls for the following reasons:

An
                                                						incoming call can invoke multiple applications, because each leg of the call
                                                						can invoke a different application. The same call is counted once for each
                                                						application.

Some
                                                						calls are terminated before they are queued. Such calls do not have CRDRs
                                                						(because they are not queued) and are not counted for the Contact Service Queue Activity Report . These calls do
                                                						not have ACDRs as well and are not counted on the Agent Summary Report .

The Agent Summary Report shows more presented calls than
                                          				  the Contact Service Queue Activity Report for either of
                                          				  the following reasons:

The same
                                                						call is queued to a certain CSQ, but is presented to multiple agents within the
                                                						CSQ (because an agent did not answer). Such calls are counted once for the Contact Service Queue Activity Report , but counted
                                                						once for each agent involved for the Agent Summary Report .

There
                                                						are conference calls that involved multiple agents.

Q.

A.

Some calls shown in the Abandoned Call Detail Activity Report are abandoned
                                          				  before they are routed to a CSQ (these calls have a blank Call Routed CSQ
                                          				  field), so they are not counted for any CSQ. The Contact Service Queue Activity Report shows calls
                                          				  that are abandoned while they are queued for a CSQ.

Q.

A.

Consider this example: An
                                          				  agent from another CSQ handled the call, in conference with Agent1, and then
                                          				  dropped out. In addition, Agent1 continued the call for longer than the longest
                                          				  talk time of the any call that the agent handled for CSQ1. In this case, the
                                          				  maximum Handle Time appears for Agent1 on the Agent Summary Report . It does not appear for CSQ1 on
                                          				  the Contact Service Queue Activity Report because Agent1
                                          				  was conferenced in to the call, but the call was initially handled by another
                                          				  CSQ.

Q.

A.

CQDR
                                                   						for CSQ1—With a disposition of Handled_by_other (5) (or of 4 if there is a
                                                   						dequeue step).

CQDR
                                                   						for CSQ2—With a disposition of Handled_by_other (5) (or of 4 if there is a
                                                   						dequeue step).

CQDR
                                                   						for agent—Who handled call through agent-based routing, with a disposition of
                                                   						Handled (2).

The Contact Service Queue Activity Report shows
                                          				  dispositions 4 and 5 as Calls Handled by Other, so it shows one call as handled
                                          				  by other for both CSQ1 and CSQ2. Calls Dequeued is 0 for both the CSQs
                                          				  (disposition 3 is reported as dequeued on the report).

The CSQ
                                          				  Unified CCX Stats real-time report counts calls marked as Handled_by_other as
                                          				  dequeued calls. In this report, Contacts Dequeued includes calls that were
                                          				  dequeued and handled by another CSQ, by an agent, or by a script.

Q.

A.

In the Contact Service Queue Activity Report by Interval and Contact Service Queue Activity by CSQ Report :

Calls Dequeued = Calls dequeued via the dequeue step + calls
                                                   						handled by workflow script + calls handled by another CSQ.

In the Contact Service Queue Activity Report :

Calls Dequeued = Calls dequeued via dequeue step

Calls handled by other = calls handled by workflow script +
                                                            							 calls handled by another CSQ

Q.

A.

The Agent Summary Report shows ACD calls only, but the Agent Detail Report shows Unified CCX and Cisco
                                          				  Unified IP IVR calls. The calls in question are IVR calls, so they do not
                                          				  appear on Agent Summary Report .

Q.

A.

If the agent does not spend
                                          				  the entire duration of time in Not Ready state with the unique reason code
                                          				  making outbound calls, then the sum of the duration of outbound calls will be
                                          				  less than the duration that is spent in Not Ready state with the unique reason
                                          				  code.

## Abandoned Call
                        	 Detail Activity Report

Q.

A.

Match the call start time
                                          				  in the Abandoned Call Detail Activity Report with
                                          				  the call start time in the Detailed Call by Call CCDR Report , and look
                                          				  up the session ID and session sequence number in the Detailed Call by Call CCDR Report . Different
                                          				  call legs that belong to the same call have the same session ID, but different
                                          				  session sequence numbers.

Q.

A.

The call was abandoned
                                          				  before it was assigned a priority.

Q.

A.

The call was abandoned
                                          				  before it was routed to an agent.

Q.

A.

The call was routed to an
                                          				  agent, the agent did not answer, and the caller hung up.

Q.

A.

The values can differ
                                          				  because the Contact Service Queue Activity Report may
                                          				  mark a call as dequeued, while a Contact Call Detail record marks the call as
                                          				  abandoned. For example, consider the following workflow:

```
StartAccept
Prompt
Select Resource
-Connect
-Queue
--Play Prompt (Prompt2)
--Dequeue
--Play Prompt (Prompt3)
End
```

Scenario

Contact Service Queue Activity Report

Abandoned Call Detail Activity Report

Call is abandoned during Prompt2 or Prompt3

The Contact Queue Detail record marks the call as dequeued, but not as
                                                         								abandoned from any queue. So, the Contact Service Queue Activity
                                                            								  Report shows the call as dequeued from all CSQs to which the call
                                                         								was routed.

The Contact Call Detail
                                                         								record marks the call as abandoned. So, the Abandoned Call Detail Activity
                                                            								  Report shows the call as abandoned from all CSQs to which the call
                                                         								was routed.

Call gets aborted after being in the queue

Call is marked as aborted in the Contact Call Detail record. So,
                                                         								the CSQ reports display more abandoned calls than the Abandoned Call Detail Activity
                                                            								  Report .

Call is marked as dequeued (if the call was dequeued before
                                                         								aborting) or abandoned in Contact Queue Detail record.

Q.

A.

When an agent transfers a
                                          				  call to another agent, and the caller abandons the call before the call is
                                          				  answered by the second agent, then the first phase of the call is marked as
                                          				  handled. The abandonment of the second phase is not displayed in the Abandoned Detail Call Activity Report . This
                                          				  information cannot be seen in any other report.

## Agent Call Summary
                        	 Report

Q.

A.

Yes, these calls are
                                          				  included for calculating the Inbound ACD—Total field.

Q.

A.

The number of calls can
                                          				  differ for the following reasons:

The
                                                						Agent Call Summary Report shows calls that are presented to the agents, and the Contact Service Queue Activity by CSQ shows calls that are presented to the CSQs. If there are agents included in the
                                                						Agent Call Summary Report who do not belong to the CSQs in the Contact Service Queue Activity by CSQ ,
                                                						then the Agent Call Summary Report shows more
                                                						calls.

If
                                                						agent-based routing is configured, calls can go to agents directly, without
                                                						going through a CSQ. In this case, the Agent Call Summary Report shows more
                                                						calls.

The Agent Call Summary Report can include
                                                						transferred ACD calls. For example, if a call is queued for CSQ1, handled by
                                                						Agent1, and transferred by Agent1 to Agent2 (without going through a CSQ), then
                                                						one call is shown as handled on the Contact Service Queue Activity Report (through CSQ1 by Agent1). The same is shown twice on the Agent Call Summary Report —one as handled
                                                						by Agent1 (through CSQ1), another as handled by Agent2 (not through a CSQ but
                                                						as a direct transfer from Agent2).

## Agent Detail
                        	 Report

Q.

A.

The call was not an ACD
                                          				  call. (IVR calls include Agent-to-Agent calls and external calls made by an
                                          				  agent.) The Unified CCX database does not record hold time and work time for
                                          				  IVR calls.

Q.

A.

The value in the duration
                                          				  field is calculated as follows:

call end time – call start time

The
                                          				  call start time is when the call rings at the agent extension. The call end
                                          				  time is when the agent leaves Work state. Therefore, the call duration is equal
                                          				  to ring time + talk time + hold time + work time.

Q.

A.

The Hold Time and the Work
                                          				  Time fields are blank in the Agent Detail Report for IVR calls.

## Agent Login Logout
                        	 Activity Report

Q.

A.

A less-than sign (<)
                                          				  indicates that the agent logged in before the report start time. A greater-than
                                          				  sign (>) indicates that the agent logged out after the report end time.

The
                                                   						agent logged in at 7:45 a.m. (0745), the Login Time field will show < 8am
                                                   						(or < 0800).

If the
                                                   						agent logged out at 6:30 p.m. (1830), the Logout Time field will show > 6pm
                                                   						(or > 1800).

## Agent State Summary by Agent Report

Q.

A.

The report template defines the view of the report. There are two kinds of  summary rows (darker background)   that are defined
                                             in the template. The summary row that follows after each agent summarizes  details of the agent. The summary row that appears
                                             at the end of the report summarizes details of all the agents.

If there is a single row for the agent, then the summary row of the agent will have the same details as the above row.

## Agent Summary
                        	 Report

Q.

A.

This value is calculated as
                                          				  the total logged-in time divided by the number of login sessions.

For
                                          				  example, if an agent logs in at 8:00 a.m. (0800) and logs out at 8:30a.m.
                                          				  (0830), logs in again at 9:15 a.m. (0915) and logs out at 10:00 a.m. (1000),
                                          				  then there are two login sessions. The first session lasts 30 minutes and the
                                          				  second session lasts 45 minutes. The average logged-in time is (30+45)/2 = 37.5
                                          				  minutes.

Q.

A.

Handle time = Talk time +
                                          				  Hold time + Work time.

Q.

A.

This value is calculated as
                                          				  the total idle time divided by the number of idle sessions.

For
                                          				  example, if an agent goes to Not Ready state at 10:00 a.m. (1000) and goes to
                                          				  Ready state at 10:15 a.m. (1015), goes to Not Ready state at 11:00 a.m. (1100)
                                          				  and goes to Ready state at 11:05 a.m (1105), then there are two idle sessions.
                                          				  The first session lasts 15 minutes and the second session lasts 5 minutes. The
                                          				  average idle time is (15+5)/2 = 10 minutes.

Q.

A.

The talk time information
                                          				  in the Agent Summary Report comes from the talkTime
                                          				  field in the AgentConnectionDetail table. This value is the time that an agent
                                          				  spent on an incoming ACD call. The talk time information in the Agent State Summary by Agent Report or the Agent State Summary by Interval Report comes
                                          				  from AgentStateDetail table. These values show the time that an agent spent in
                                          				  the Talk state. These values will be different if the agent placed ACD calls on
                                          				  hold during the reporting period.

Q.

A.

The Agent Summary Report shows information for
                                          				  ACD calls only. The Agent Detail Report shows information for
                                          				  Unified CCX and Cisco Unified IP IVR calls.

## Application
                        	 Performance Analysis Report

Q.

A.

The Application ID field is
                                          				  –1, and the Application Name field is empty for Agent-to-Agent calls, IVR
                                          				  calls, Agent-to-Agent transfer/conference consult legs, or any other call that
                                          				  is not placed to a Unified CCX Route Point or associated with an application.

Q.

A.

The Application Performance Analysis Report counts only incoming calls. The Detailed Call by Call CCDR Report counts
                                          				  incoming calls, outgoing calls (for example, outbound calls made by agents),
                                          				  and internal calls (for example, Agent-to-Agent consult calls).

Q.

A.

The Contact Service Queue Activity Report includes only abandoned ACD calls. This report counts an ACD call as abandoned
                                          				  if the caller hangs up while queued for a CSQ or CSQs.

The Application Performance Analysis Report includes abandoned ACD calls and abandoned IVR calls. This report counts a call
                                          				  as abandoned if the call ends before it is answered by an agent or before it is
                                          				  marked as handled by a workflow.

## Call Custom
                        	 Variables Report

Q.

A.

These fields show the
                                          				  values of the custom variables that are specified in a workflow.

For example, a workflow may designate variable1 as the menu
                                          				  option that the caller chooses, and designate variable2 as the account number
                                          				  that the caller enters. In this case, Custom Variable 1 would show the option
                                          				  value (such as 2) that the caller entered, and Custom Variable 2 would show the
                                          				  account number that was entered.

## Common Skill CSQ
                        	 Activity Report

Q.

A.

This report provides
                                          				  additional information for multiple CSQs that are configured with the same call
                                          				  skill, but with different competence levels. An incoming call may be queued for
                                          				  the CSQ with the lowest-competence level. If no agent is available for a
                                          				  certain period, the call is queued for the next higher-competence level.

The summary
                                          				  line in the report displays the summarized statistics for the group of CSQs
                                          				  configured with common skills. A group of CSQs that is configured in this
                                          				  manner is called a logical CSQ.

## Contact Service
                        	 Queue Activity Report

Q.

A.

The average queue time for
                                          				  a CSQ is calculated as the sum of the queue times for all the calls presented
                                          				  divided by the number of calls presented. The maximum queue time for a CSQ is
                                          				  the longest queue time for a single call among the calls presented.

The individual queue time for each CSQ is stored in the CQDR
                                          				  table. For example, assume that an incoming call is queued for CSQ1 for 5
                                          				  minutes, queued for CSQ2 for 10 minutes, and then it is handled by CSQ1. The
                                          				  queue time recorded for CSQ1 in the CQDR table is 5 minutes, and for CSQ2 is 10
                                          				  minutes.

Q.

A.

Average calls abandoned for
                                          				  a CSQ is an average value per day. It is calculated as the total number of
                                          				  calls abandoned for the CSQ divided by the number of days in the report period.

Maximum
                                          				  calls abandoned for a CSQ is calculated by determining the number of calls
                                          				  abandoned for each day in the report period and selecting the largest of these
                                          				  values.

Q.

A.

By default, the call is
                                          				  counted as abandoned instead of handled, because it did not connect to an
                                          				  agent. However, if the workflow is designed to mark a call as handled after a
                                          				  caller leaves a message, the call will be counted as handled.

Q.

A.

You can design a workflow
                                          				  to store a caller’s key input in one of the custom variables in the
                                          				  ContactCallDetail table. You can either generate the Call Custom Variables Report and manually
                                          				  count the rows that contain the desired information or you can create a custom
                                          				  report to provide this information.

Q.

A.

No. Calls presented = calls
                                          				  handled + calls abandoned + calls dequeued + calls handled by others.

"Calls handled" are the
                                          				  calls that were connected to an agent in a particular CSQ. "Calls
                                             					 handled by others" are the calls that were handled by some workflow in a
                                          				  script, and the calls that were queued for multiple CSQs and then handled by
                                          				  one of the other CSQs.

Q.

A.

To show hourly data for
                                          				  each day, schedule daily reports either for Contact Service Queue Activity by CSQ Report or for Contact Service Queue Activity Report by
                                             					 Interval . Set the Interval Length to 60 minutes. This setting will
                                          				  provide one report each day, divided into one-hour intervals.

Separate hourly reports are not available, but with the interval
                                          				  length set to 60 minutes, a daily report will display 24 intervals, one for
                                          				  each hour of the day.

## Contact Service
                        	 Queue Activity by CSQ Report

Q.

A.

A CSQ has many attributes,
                                          				  including CSQ name, service level, resource selection criterion, and auto work.
                                          				  Some attributes, such as CSQ name and service level, are displayed in the
                                          				  report. Other attributes are not displayed in the report. However, changing any
                                          				  attribute of the CSQ causes a new line to show in the report. For example:

If the
                                                   						service level is changed from 10 to 25, two lines of the same CSQ will show in
                                                   						the report. One line will show the old service level value and another line
                                                   						will show the new service level value.

If Auto
                                                   						Work is changed from 1 to 0, two lines of the same CSQ will be shown in the
                                                   						report. As the Auto Work setting does not appear in the report, the same CSQ
                                                   						will appear twice.

Q.

A.

Handled
                                                   						within service level

Handled
                                                   						after service level

Abandoned within service level

Abandoned after service level

Field

Description

Calculation

Percentage of Service Level Met—Only Handled

This field shows only handled calls. It does not include
                                                      								abandoned calls. This field shows the percentage of handled calls that were
                                                      								handled within the service level.

The remaining fields differ in how they account for abandoned
                                                      								calls: not counted, meeting service level, or not meeting service level.

(Number of calls handled within service level / Number of calls
                                                      								handled) * 100%

Percentage of Service Level Met—With No Abandoned Calls

This field shows the percentage of presented calls (calls routed
                                                      								to a CSQ), not counting abandoned calls, that were handled within the service
                                                      								level. It does not include calls that were abandoned within the service level.

This value is always less than or equal to the value in the
                                                      								Percentage of Service Level Met—Only Handled field

(Number of calls handled within service level / (Number of calls
                                                      								presented – Number of calls abandoned within service level)) * 100%

Percentage of Service Level Met—With Abandoned Calls Counted
                                                      								Positively

The field shows the calls that are abandoned within the service
                                                      								level as meeting the service level. It shows the percentage of presented calls
                                                      								that were handled or abandoned within the service level.

((Number of calls handled within service level + Number of calls
                                                      								abandoned within service level) / Number of calls presented) * 100%

Percentage of Service Level Met—With Abandoned Calls Counted
                                                      								Negatively

The field shows the calls that are abandoned within the service
                                                      								level as not meeting the service level. It shows the percentage of presented
                                                      								calls that were handled within the service level. This value is less than or
                                                      								equal to the Percentage of Service Level Met—With Abandoned Calls Counted
                                                      								Positively field.

(Number of calls handled within service level / Number of calls
                                                      								presented) * 100%

Q.

A.

If a call is queued for
                                          				  multiple CSQs and is abandoned, it is counted as abandoned from all the CSQs
                                          				  for which it is queued.

For example, if a call is queued for CSQ1 and CSQ2 and the
                                          				  caller hangs up before being routed to an agent, then an abandoned call is
                                          				  counted for CSQ1 and for CSQ2.

Q.

A.

If a call is queued for
                                          				  multiple CSQs and is handled by one of them, then the call is counted as
                                          				  dequeued from each of the other CSQs.

For example, if an incoming call is queued for CSQ1, CSQ2, and
                                          				  CSQ3 and is handled by an agent from CSQ2, then a dequeued call is counted for
                                          				  CSQ1 and for CSQ3.

Q.

A.

The Unified CCX database
                                          				  maintains records of old and new service levels. When a new service level is
                                          				  configured, the old record is marked as inactive. The dateInactive field in the
                                          				  ContactServiceQueue table shows the date and time that the new service level
                                          				  was configured. If the value in the dateInactive field is in the report period,
                                          				  the report shows the active (new) and inactive (old) CSQs.

## Detailed Call by
                        	 Call CCDR Report

Q.

A.

A session ID is a unique
                                          				  identification number that the system assigns to a call. This number remains
                                          				  the same for the entire call. The system also assigns a sequence number to each
                                          				  leg of a call. Sequence numbers start at 0 and increment by 1 each time the
                                          				  call is transferred or redirected.

Q.

A.

Yes. You can design a
                                          				  workflow to mark such a call as handled.

Q.

A.

The call was an IVR call.
                                          				  (IVR calls include Agent-to-Agent calls and external calls that are made by an
                                          				  agent.) The Unified CCX database does not record hold time and work time for
                                          				  IVR calls.

Q.

A.

The calls in the CCDR
                                          				  Report are not duplicates. They are conference calls, which have the same
                                          				  SessionID and Session Sequence Number, but different talk time because
                                          				  different agents participated in the same call. (The Detailed Call by Call CCDR Report shows the
                                          				  names of agents who participated in a conference call.)

Q.

A.

When the system removes
                                          				  stuck calls, which may have remained in the system because of missing events,
                                          				  the system writes a CCDR with the contact disposition dont_care (value = 3).

## License
                        	 Utilization Hourly Report

Q.

A.

Data is
                                          				  sampled per minute. The report aggregates the data over an hour (maximum of all
                                          				  samples within the hour).

Q.

A.

If a call
                                          				  duration is less than a minute and its start and end times fall between two
                                          				  sampling points, then this call will not be considered for the statistics.

## Traffic Analysis
                        	 Report

Q.

A.

An incoming call can have
                                          				  multiple call legs. The Traffic Analysis Report counts a call with
                                          				  multiple legs as a single call. However, each call leg may invoke a different
                                          				  application, so the Application Performance Analysis Report counts each call leg as a call.

Session ID = 1, sequence number = 0, application = "auto
                                                      						  attendant"

Session ID = 1, sequence number = 1, application = "musician demonstration"

This call is counted once for the Traffic Analysis Report . It is counted twice
                                          				  for the Application Performance Analysis Report —once
                                          				  for the "auto
                                             					 attendant" application and once for the "musician
                                             					 demonstration" application.

| Q. | How is the
                                       				number of days calculated in Historical reports? |
|---|---|
| A. | The number of days is
                                          				  calculated by an SQL function that counts the number of calendar days.
                                          				  Fractions of a day are counted as an entire day. This table provides an
                                          				  example. Time Range Number of Days 10
                                                      								a.m. (1000) on 5/15 to 10 a.m. (1000) on 5/16 Two days 12:00:00 a.m. (0000) on 5/15 to 11:59:59 p.m. (1159:59) on 5/15 One day 12:00:00 a.m. (0000) on 5/15 to 12:00:00 a.m. (0000) on 5/16 Two days | Time Range | Number of Days | 10
                                                      								a.m. (1000) on 5/15 to 10 a.m. (1000) on 5/16 | Two days | 12:00:00 a.m. (0000) on 5/15 to 11:59:59 p.m. (1159:59) on 5/15 | One day | 12:00:00 a.m. (0000) on 5/15 to 12:00:00 a.m. (0000) on 5/16 | Two days |
| Time Range | Number of Days |
| 10
                                                      								a.m. (1000) on 5/15 to 10 a.m. (1000) on 5/16 | Two days |
| 12:00:00 a.m. (0000) on 5/15 to 11:59:59 p.m. (1159:59) on 5/15 | One day |
| 12:00:00 a.m. (0000) on 5/15 to 12:00:00 a.m. (0000) on 5/16 | Two days |
| Q. | Which reason
                                       				codes are supported for reports? |
| A. | When reason
                                          				  codes are configured, agents enter the reason codes when explicitly
                                          				  transitioning to Logout state or to Not Ready state. These reason codes are
                                          				  stored in the ASDR. The
                                          				  following reports provide the details: Agent Login Logout Activity Report —Presents the
                                                   						logout reason code in detail. Agent Not Ready Reason Code Summary Report —Presents
                                                   						summary information for the Not Ready reason code. Agent State Detail Report —Presents Logout reason code
                                                   						and Not Ready reason code in detail. Note Not
                                                         						Ready codes are systemwide and cannot be configured to be hidden from certain
                                                         						agents. In the
                                          				  following cases, reason codes are not stored. In these cases, the reasonCode
                                          				  field in the ASDR contains a value of –1. Case Agent State in ASDR Browser crashes Logout Agent logs out when logged in to another computer or phone Logout Normal agent login Not Ready Agent receives an IVR call on the ICD extension, fails to
                                                         								answer, and that results in RNA Not Ready Agent goes off-hook on ICD extension to place a call Not Ready Agent fails to answer an ACD call within the specified timeout
                                                         								period Not Ready Agent does not answer an ICD call Not Ready Agent’s phone goes down Not Ready or Logout Supervisor changes the agent’s state from the Cisco Finesse
                                                         								Supervisor Desktop Not Ready or Logout | Note | Not
                                                         						Ready codes are systemwide and cannot be configured to be hidden from certain
                                                         						agents. | Case | Agent State in ASDR | Browser crashes | Logout | Agent logs out when logged in to another computer or phone | Logout | Normal agent login | Not Ready | Agent receives an IVR call on the ICD extension, fails to
                                                         								answer, and that results in RNA | Not Ready | Agent goes off-hook on ICD extension to place a call | Not Ready | Agent fails to answer an ACD call within the specified timeout
                                                         								period | Not Ready | Agent does not answer an ICD call | Not Ready | Agent’s phone goes down | Not Ready or Logout | Supervisor changes the agent’s state from the Cisco Finesse
                                                         								Supervisor Desktop | Not Ready or Logout |
| Note | Not
                                                         						Ready codes are systemwide and cannot be configured to be hidden from certain
                                                         						agents. |
| Case | Agent State in ASDR |
| Browser crashes | Logout |
| Agent logs out when logged in to another computer or phone | Logout |
| Normal agent login | Not Ready |
| Agent receives an IVR call on the ICD extension, fails to
                                                         								answer, and that results in RNA | Not Ready |
| Agent goes off-hook on ICD extension to place a call | Not Ready |
| Agent fails to answer an ACD call within the specified timeout
                                                         								period | Not Ready |
| Agent does not answer an ICD call | Not Ready |
| Agent’s phone goes down | Not Ready or Logout |
| Supervisor changes the agent’s state from the Cisco Finesse
                                                         								Supervisor Desktop | Not Ready or Logout |
| Q. | Which
                                       				database is used for Unified CCX? |
| A. | Unified CCX
                                          				  uses IBM Informix Dynamic Server (IDS) database. |
| Q. | Why is the Contact Service Queue Service Level Report , which is
                                       				available in previous versions of Unified CCX, no longer available in the
                                       				current version? |
| A. | The
                                          				  information that was in this report is distributed among the Contact
                                             					 Service Queue Service Level Priority Summary Report , the Contact
                                             					 Service Queue Activity Report , and the Contact
                                             					 Service Queue Call Distribution Summary Report . |
| Q. | Why is the Skill Routing Activity Report , which is available in
                                       				previous versions of Unified CCX, no longer available in the current version? |
| A. | The
                                          				  information that was in this report is available in the Contact
                                             					 Service Queue Activity Report or in the Contact
                                             					 Service Queue Activity Report when filtered to show Skill Groups only. |
| Q. | What can
                                       				cause more than one record to have the same node ID, session ID, and sequence
                                       				number? |
| A. | In the
                                          				  following scenarios, more than one record can have the same node ID, session
                                          				  ID, and sequence number: A call
                                                   						is conferenced to a CTI route point. A call
                                                   						rings at an agent's phone, but the agent does not pick up. The call is
                                                   						categorized as Ring No Answer (RNA) to the agent. |
| Q. | Why are some
                                       				of the selected filter parameters not included in the generated report? |
| A. | The length
                                          				  of each parameter to the report must not exceed 800 characters. If the selected
                                          				  parameters exceed this value, then the database server truncates the parameter
                                          				  to the first 800 characters. The stored
                                          				  procedure receives only the first 800 characters of the chosen parameters; the
                                          				  rest are not included in the generated report. |
| Q. | How can I
                                       				export historical data to my own data warehouse? |
| A. | Use
                                          				  third-party database administration tools such as SQuirreL SQL Client or AGS
                                          				  Server Studio to export Unified CCX historical data to your own data warehouse.
                                          				  Use uccxhruser as the username to connect to db_cra
                                          				  database. |
| Q. | Can I
                                       				connect the embedded Unified Intelligence Center to 3 rd party databases
                                       				or a different Unified CCX / Unified IP-IVR deployment for reporting purpose? |
| A. | No, it is
                                          				  not supported with embedded Unified Intelligence Center but is supported with
                                          				  standalone Unified Intelligence Center. |
| Q. | Can I use
                                       				3 rd party
                                       				software to access Unified CCX IBM Informix Dynamic Server (IDS) database for
                                       				reporting purpose? |
| A. | Yes, but
                                          				  it should be used with discretion keeping in mind the impact on the system. |

| Time Range | Number of Days |
|---|---|
| 10
                                                      								a.m. (1000) on 5/15 to 10 a.m. (1000) on 5/16 | Two days |
| 12:00:00 a.m. (0000) on 5/15 to 11:59:59 p.m. (1159:59) on 5/15 | One day |
| 12:00:00 a.m. (0000) on 5/15 to 12:00:00 a.m. (0000) on 5/16 | Two days |

| Note | Not
                                                         						Ready codes are systemwide and cannot be configured to be hidden from certain
                                                         						agents. |
|---|---|

| Case | Agent State in ASDR |
|---|---|
| Browser crashes | Logout |
| Agent logs out when logged in to another computer or phone | Logout |
| Normal agent login | Not Ready |
| Agent receives an IVR call on the ICD extension, fails to
                                                         								answer, and that results in RNA | Not Ready |
| Agent goes off-hook on ICD extension to place a call | Not Ready |
| Agent fails to answer an ACD call within the specified timeout
                                                         								period | Not Ready |
| Agent does not answer an ICD call | Not Ready |
| Agent’s phone goes down | Not Ready or Logout |
| Supervisor changes the agent’s state from the Cisco Finesse
                                                         								Supervisor Desktop | Not Ready or Logout |

| Q. | Which report
                                       				shows calls per hour per CSQ? For example: 7:00
                                          				  a.m. to 8:00 a.m., 25 calls; 8:00 a.m. to 9:00 a.m., 35 calls; and 9:00 a.m. to
                                          				  10:00 a.m., 34 calls. |
|---|---|
| A. | The Contact Service Queue Activity Report by Interval shows this information. To generate this report for one-hour intervals, set its
                                          				  Interval Length filter parameter to sixty (60) minute intervals. |
| Q. | How can I
                                       				determine telephone numbers of calling parties? |
| A. | The Call ANI
                                          				  fields on the Abandoned Call Detail Activity Report and the Agent Detail Report show this information. |
| Q. | How is the
                                       				following scenario reported? A call is in queue and it is routed to an
                                       				available agent who does not answer the call, so the call is redirected to
                                       				another agent. |
| A. | The scenario appears in the following reports: The Agent Detail Report shows two lines: For the agent who did not answer the call—Ring time is greater than 0; talk time, hold time, and work time are each zero. For the agent who answered the call—Talk time is greater than 0. The Agent Summary Report shows the following: The call was presented to the agent who did not answer the call, but was not handled by that agent. The call was presented to and handled by the agent who answered the call. The CSQ Agent Summary Report shows the call as Ring No Answer (RNA) for the first agent. |
| Q. | How can I
                                       				determine the start time and the end time for a call with multiple legs? |
| A. | The
                                          				  following fields identify the various legs of a call: The sessionID fields in the Unified CCX database tables contain the same value for a particular call. These fields identify
                                                all the database records that relate to a call. The sessionSeqNum fields in the Unified CCX database tables start at 0 and increment by 1 for each leg of a call. The startDateTime field of the CCDR stores the start time of a call. The sessionSeqNum is equal to 0, and the sessionID value
                                                identifies the call. The endDateTime field of the CCDR with the highest sessionSeqNum and the same sessionID value stores the end time of a call. Note The way in which sessionID and sessionSeqNum values are written to the database depend on the call scenario. For more information
                                                   and examples, see the "Interpret Database Records" section of Cisco Unified Contact
                                                            				  Center Express Report Developer Guide , located at: https://www.cisco.com/en/US/products/sw/custcosw/ps1846/products_installation_and_configuration_guides_list.html . | Note | The way in which sessionID and sessionSeqNum values are written to the database depend on the call scenario. For more information
                                                   and examples, see the "Interpret Database Records" section of Cisco Unified Contact
                                                            				  Center Express Report Developer Guide , located at: https://www.cisco.com/en/US/products/sw/custcosw/ps1846/products_installation_and_configuration_guides_list.html . |
| Note | The way in which sessionID and sessionSeqNum values are written to the database depend on the call scenario. For more information
                                                   and examples, see the "Interpret Database Records" section of Cisco Unified Contact
                                                            				  Center Express Report Developer Guide , located at: https://www.cisco.com/en/US/products/sw/custcosw/ps1846/products_installation_and_configuration_guides_list.html . |
| Q. | Which
                                       				report displays information on menu choices? |
| A. | You can
                                          				  create a custom report to show menu choices. Use the Set Session Info step in a workflow to store the
                                          				  custom variables entered by the callers. The contents of such custom variables
                                          				  are stored in the customVariable fields in the CCDR. Use the information in the
                                          				  CCDR customVariable fields when you create custom reports. The
                                          				  following is an example of how to prepare a report to show information for a
                                          				  menu with three choices (1, 2, and 3): For a workflow, define a variable of type session and name it this_session . Place a Get Contact Info step at the beginning of the workflow. Set the Session attribute to variable this_session . Define a Menu step that has three branches and place a Set Enterprise Call Info step in each branch. In the General tab of the Set Enterprise Call Info step, click Add . In the branch for caller-choice 1, enter 1 in the Value field, and choose Call.PeripheralVariable1 from the Name drop-down list. In the branch for caller-choice 2, enter 2 in the Value field, and choose Call.PeripheralVariable2 from the Name drop-down list. In the branch for caller-choice 3, enter 3 in the Value field, and choose Call.PeripheralVariable3 from the Name drop-down list. Create a custom report that will show the values of the customVariable1, customVariable2, and customVariable3 fields in the
                                                CCDR. If calls
                                          				  are to be transferred between workflows and multiple menu choices can be made
                                          				  for a single session, take care to preserve previously entered menu choices.
                                          				  For example, place a Get Session Info step at the beginning of the
                                          				  workflow. If the _ccdrVar1 variable is null, there were no previous entries. If
                                          				  it is not null, when you add a new choice, determine a format for associating a
                                          				  menu choice to a sequence number. In this way, you will be able to prepare
                                          				  accurate reports. |
| Q. | If a
                                       				Unified CCX system does not include a license for Historical reports, is data
                                       				still written to the Unified CCX databases? |
| A. | Yes. |
| Q. | Which
                                       				report has information on agent Service Level Agreements (SLAs), such as 
                                       				queue time threshold (caution, warning) and agent talk time
                                       				SLA (caution, warning)? |
| A. | There are
                                          				  no reports available, but the Unified CCX databases store this data. You can
                                          				  create a custom report to show this information. |
| Q. | Which
                                       				report has information about calls that were transferred by agents to another
                                       				Contact Service Queue? |
| A. | The Detailed Call CSQ Agent Report has information about
                                          				  transferred calls. The session ID remains the same for a transferred call, but
                                          				  the session sequence number increments by 1. This report also shows the agent
                                          				  who handled each call, and the CSQ to which the call was routed. |
| Q. | A record
                                       				that contains data is stored in memory and is ready to be written to the
                                       				Unified CCX database, when is it written to the database? |
| A. | Call records (CCDR, CRDR, CQDR) are written after each call is completed. Note CCDRs are written after the agent leaves Work state, when applicable. Otherwise, they are written after the call ends. Agent state records (ASDR) are written after agents change state. Agent connection records (ACDR) are written when an agent leaves Work state or after the call completes if the agent does
                                                not go to Work state. | Note | CCDRs are written after the agent leaves Work state, when applicable. Otherwise, they are written after the call ends. |
| Note | CCDRs are written after the agent leaves Work state, when applicable. Otherwise, they are written after the call ends. |
| Q. | Are there
                                       				summary tables for daily data that contain the data for a specific day? Are
                                       				these tables used to create weekly data tables? Are weekly data tables used to
                                       				create monthly data tables? |
| A. | The system
                                          				  stores detailed data. It does not summarize detailed tables to create daily,
                                          				  weekly, or monthly tables. |
| Q. | Which
                                       				monthly report shows statistics for service levels? |
| A. | The Contact Service Queue Activity by CSQ or Contact Service Queue Activity by Interval shows
                                          				  information about service levels provided to handled calls. Schedule the Contact Service Queue Activity by CSQ or Contact Service Queue Activity by Interval to run
                                          				  monthly. |
| Q. | Can I
                                       				create custom Historical reports? |
| A. | Yes. For
                                          				  more information about creating custom reports, see the "Create Custom Reports"
                                          				  section of Cisco Unified Contact
                                                   				  Center Express Report Developer Guide ,
                                          				  located at: https://www.cisco.com/en/US/products/sw/custcosw/ps1846/products_installation_and_configuration_guides_list.html . |

| Note | The way in which sessionID and sessionSeqNum values are written to the database depend on the call scenario. For more information
                                                   and examples, see the "Interpret Database Records" section of Cisco Unified Contact
                                                            				  Center Express Report Developer Guide , located at: https://www.cisco.com/en/US/products/sw/custcosw/ps1846/products_installation_and_configuration_guides_list.html . |
|---|---|

| Note | CCDRs are written after the agent leaves Work state, when applicable. Otherwise, they are written after the call ends. |
|---|---|

| Q. | Why does the Detailed Call by Call CCDR Report show more handled
                                       				calls than the CSQ reports? |
|---|---|
| A. | The CSQ
                                          				  reports show calls that are handled by agents after the calls are queued for a
                                          				  CSQ. The Detailed Call by Call CCDR Report shows these calls
                                          				  and also the calls that are marked as handled by a workflow script before they
                                          				  are queued for a CSQ. |
| Q. | Why does the Application Performance Analysis Report show more
                                       				presented, handled, and abandoned calls than the CSQ Reports? |
| A. | The
                                          				  following are the two reasons: An
                                                   						incoming call can invoke multiple applications because each leg of the call
                                                   						invokes a different application. The call is counted once for each application. Calls
                                                   						that are hung up before being queued for any CSQ are marked as handled or
                                                   						abandoned depending on the workflow, and also depending on when they are hung
                                                   						up. Such calls do not have CRDRs or ACDRs and will not be counted for CSQ
                                                   						reports or agent reports. These calls will be counted for the Application Performance Analysis Report because the
                                                   						calls entered an application. |
| Q. | Why does the Agent Summary Report show more handled calls than the
                                       				CSQ reports? |
| A. | Conference
                                          				  calls to agents result in one CRDR that has multiple ACDRs. The Agent Summary Report counts the number of ACDRs, but
                                          				  the CSQ reports count the number of CRDRs. |
| Q. | How can I
                                       				identify conference calls? |
| A. | To identify
                                          				  conference calls, search for ACDRs with the same session ID and sequence
                                          				  number, with different agent IDs, and with talk time greater than 0. |
| Q. | How to
                                       				identify calls that were presented to an agent, but were not answered? |
| A. | To identify calls that were
                                          				  not answered by an agent, search for ACDRs with talk time equal to zero. The CSQ Agent Summary Report shows the total number of
                                          				  Ring No Answer (RNA) calls for each agent and for each CSQ. In the Agent Summary Report , the number of Ring No Answer
                                          				  calls = Calls Presented – Calls Handled. |
| Q. | Why is the
                                       				total number of calls in the Calls Handled field in the Contact Service Queue Activity Report lower than the
                                       				number in the Calls Handled Field in the Agent Summary Report ? |
| A. | The CSQ reports, including
                                          				  the Contact Service Queue Activity Report show activity
                                          				  at the CSQ level. The agent reports, including the Agent Summary Report , show activity at the agent
                                          				  level. For handled calls, the Agent Summary Report counts the ACDRs with non-zero
                                          				  talk time (to exclude unanswered calls), and the Contact Service Queue Activity Report counts CQDRs
                                          				  with disposition equal to 2 (handled). The number of such ACDRs may be larger than the number of such
                                          				  CQDRs for any of the following reasons: If you
                                                						choose all the agents for the Agent Summary Report , but choose only one CSQ for the Contact Service Queue Activity Report , the Agent Summary Report will show more handled calls. There
                                                						may be conference calls that involve multiple agents. In such cases, one CQDR
                                                						has multiple associated ACDRs. An associated ACDR has the same sessionID and
                                                						sessionSeqNum as the CQDR. Agent-to-Agent transfers will result in more ACDRs than CQDRs.
                                                						If Agent1 picks up a call from CSQ1, one CQDR and one ACDR are created. When
                                                						Agent1 transfers the call to Agent2, another ACDR is created, but no CQDR is
                                                						created. |
| Q. | Why do the Agent Summary Report , Contact Service Queue Activity Report , and Application Performance Analysis Report show
                                       				different values for Calls Presented field? |
| A. | The Application Performance Analysis Report shows the
                                          				  highest number of presented calls for the following reasons: An
                                                						incoming call can invoke multiple applications, because each leg of the call
                                                						can invoke a different application. The same call is counted once for each
                                                						application. Some
                                                						calls are terminated before they are queued. Such calls do not have CRDRs
                                                						(because they are not queued) and are not counted for the Contact Service Queue Activity Report . These calls do
                                                						not have ACDRs as well and are not counted on the Agent Summary Report . The Agent Summary Report shows more presented calls than
                                          				  the Contact Service Queue Activity Report for either of
                                          				  the following reasons: The same
                                                						call is queued to a certain CSQ, but is presented to multiple agents within the
                                                						CSQ (because an agent did not answer). Such calls are counted once for the Contact Service Queue Activity Report , but counted
                                                						once for each agent involved for the Agent Summary Report . There
                                                						are conference calls that involved multiple agents. |
| Q. | Why is the
                                       				number of abandoned calls in the Abandoned Call Detail Activity Report higher than the
                                       				number of abandoned calls in the Contact Service Queue Activity Report ? |
| A. | Some calls shown in the Abandoned Call Detail Activity Report are abandoned
                                          				  before they are routed to a CSQ (these calls have a blank Call Routed CSQ
                                          				  field), so they are not counted for any CSQ. The Contact Service Queue Activity Report shows calls
                                          				  that are abandoned while they are queued for a CSQ. |
| Q. | Why is there
                                       				a difference in maximum handle time between the Contact Service Queue Activity Report and the Agent Summary Report ? For example, if Agent1 belongs
                                       				only to CSQ1 and CSQ1 does not include any other agent. Why is the Max Handle
                                       				Time field for Agent1 on the Contact Service Queue Activity Report different than
                                       				the Handle Time—Max field for Agent1 on the Agent Summary Report ? |
| A. | Consider this example: An
                                          				  agent from another CSQ handled the call, in conference with Agent1, and then
                                          				  dropped out. In addition, Agent1 continued the call for longer than the longest
                                          				  talk time of the any call that the agent handled for CSQ1. In this case, the
                                          				  maximum Handle Time appears for Agent1 on the Agent Summary Report . It does not appear for CSQ1 on
                                          				  the Contact Service Queue Activity Report because Agent1
                                          				  was conferenced in to the call, but the call was initially handled by another
                                          				  CSQ. |
| Q. | If a call is
                                       				queued in CSQ1 and CSQ2, and handled by an agent-based routing agent, the CSQ
                                       				Unified CCX Stats real-time report shows a value of 1 for Contacts Dequeued for
                                       				both CSQ1 and CSQ2, but the Contact Service Queue Activity Report shows a value
                                       				of 0 for Calls dequeued for both CSQ1 and CSQ2, why is this so? |
| A. | In this scenario, there are
                                          				  three CQDRs: CQDR
                                                   						for CSQ1—With a disposition of Handled_by_other (5) (or of 4 if there is a
                                                   						dequeue step). CQDR
                                                   						for CSQ2—With a disposition of Handled_by_other (5) (or of 4 if there is a
                                                   						dequeue step). CQDR
                                                   						for agent—Who handled call through agent-based routing, with a disposition of
                                                   						Handled (2). The Contact Service Queue Activity Report shows
                                          				  dispositions 4 and 5 as Calls Handled by Other, so it shows one call as handled
                                          				  by other for both CSQ1 and CSQ2. Calls Dequeued is 0 for both the CSQs
                                          				  (disposition 3 is reported as dequeued on the report). The CSQ
                                          				  Unified CCX Stats real-time report counts calls marked as Handled_by_other as
                                          				  dequeued calls. In this report, Contacts Dequeued includes calls that were
                                          				  dequeued and handled by another CSQ, by an agent, or by a script. |
| Q. | Why are the
                                       				Calls Dequeued field values different in the Contact Service Queue Activity Report by Interval or Contact Service Queue Activity by CSQ Report and the Contact Service Queue Activity Report ? |
| A. | In the Contact Service Queue Activity Report by Interval and Contact Service Queue Activity by CSQ Report : Calls Dequeued = Calls dequeued via the dequeue step + calls
                                                   						handled by workflow script + calls handled by another CSQ. In the Contact Service Queue Activity Report : Calls Dequeued = Calls dequeued via dequeue step Calls handled by other = calls handled by workflow script +
                                                            							 calls handled by another CSQ |
| Q. | Why does the
                                       				Talk Time field in the Agent Summary Report show 0, but the Talk Time field
                                       				in the Agent Detail Report shows another value? |
| A. | The Agent Summary Report shows ACD calls only, but the Agent Detail Report shows Unified CCX and Cisco
                                          				  Unified IP IVR calls. The calls in question are IVR calls, so they do not
                                          				  appear on Agent Summary Report . |
| Q. | If an agent
                                       				uses a unique reason code when going to Not Ready state to make outbound calls,
                                       				why does the Agent Not Ready Reason Code Summary Report show a
                                       				different duration for that reason code compared with the Agent Detail Report that shows the duration of
                                       				outbound calls for the agent? |
| A. | If the agent does not spend
                                          				  the entire duration of time in Not Ready state with the unique reason code
                                          				  making outbound calls, then the sum of the duration of outbound calls will be
                                          				  less than the duration that is spent in Not Ready state with the unique reason
                                          				  code. |

| Q. | How can I
                                       				correlate multiple abandoned call legs that belong to the same call? |
|---|---|
| A. | Match the call start time
                                          				  in the Abandoned Call Detail Activity Report with
                                          				  the call start time in the Detailed Call by Call CCDR Report , and look
                                          				  up the session ID and session sequence number in the Detailed Call by Call CCDR Report . Different
                                          				  call legs that belong to the same call have the same session ID, but different
                                          				  session sequence numbers. |
| Q. | Why do the
                                       				Initial Call Priority field or the Final Call Priority field show n/a for a
                                       				call? |
| A. | The call was abandoned
                                          				  before it was assigned a priority. |
| Q. | What does it
                                       				mean when the Agent Name field is blank? |
| A. | The call was abandoned
                                          				  before it was routed to an agent. |
| Q. | What does it
                                       				mean when the Agent Name field contains a value? |
| A. | The call was routed to an
                                          				  agent, the agent did not answer, and the caller hung up. |
| Q. | Why is there
                                       				a mismatch between the number of abandoned calls that are shown on the Abandoned Call Detail Activity Report and the
                                       				number of calls that are shown on the Contact Service Queue Activity Report ? |
| A. | The values can differ
                                          				  because the Contact Service Queue Activity Report may
                                          				  mark a call as dequeued, while a Contact Call Detail record marks the call as
                                          				  abandoned. For example, consider the following workflow: StartAccept
Prompt
Select Resource
-Connect
-Queue
--Play Prompt (Prompt2)
--Dequeue
--Play Prompt (Prompt3)
End Scenario Contact Service Queue Activity Report Abandoned Call Detail Activity Report Call is abandoned during Prompt2 or Prompt3 The Contact Queue Detail record marks the call as dequeued, but not as
                                                         								abandoned from any queue. So, the Contact Service Queue Activity
                                                            								  Report shows the call as dequeued from all CSQs to which the call
                                                         								was routed. The Contact Call Detail
                                                         								record marks the call as abandoned. So, the Abandoned Call Detail Activity
                                                            								  Report shows the call as abandoned from all CSQs to which the call
                                                         								was routed. Call gets aborted after being in the queue Call is marked as aborted in the Contact Call Detail record. So,
                                                         								the CSQ reports display more abandoned calls than the Abandoned Call Detail Activity
                                                            								  Report . Call is marked as dequeued (if the call was dequeued before
                                                         								aborting) or abandoned in Contact Queue Detail record. | Scenario | Contact Service Queue Activity Report | Abandoned Call Detail Activity Report | Call is abandoned during Prompt2 or Prompt3 | The Contact Queue Detail record marks the call as dequeued, but not as
                                                         								abandoned from any queue. So, the Contact Service Queue Activity
                                                            								  Report shows the call as dequeued from all CSQs to which the call
                                                         								was routed. | The Contact Call Detail
                                                         								record marks the call as abandoned. So, the Abandoned Call Detail Activity
                                                            								  Report shows the call as abandoned from all CSQs to which the call
                                                         								was routed. | Call gets aborted after being in the queue | Call is marked as aborted in the Contact Call Detail record. So,
                                                         								the CSQ reports display more abandoned calls than the Abandoned Call Detail Activity
                                                            								  Report . | Call is marked as dequeued (if the call was dequeued before
                                                         								aborting) or abandoned in Contact Queue Detail record. |
| Scenario | Contact Service Queue Activity Report | Abandoned Call Detail Activity Report |
| Call is abandoned during Prompt2 or Prompt3 | The Contact Queue Detail record marks the call as dequeued, but not as
                                                         								abandoned from any queue. So, the Contact Service Queue Activity
                                                            								  Report shows the call as dequeued from all CSQs to which the call
                                                         								was routed. | The Contact Call Detail
                                                         								record marks the call as abandoned. So, the Abandoned Call Detail Activity
                                                            								  Report shows the call as abandoned from all CSQs to which the call
                                                         								was routed. |
| Call gets aborted after being in the queue | Call is marked as aborted in the Contact Call Detail record. So,
                                                         								the CSQ reports display more abandoned calls than the Abandoned Call Detail Activity
                                                            								  Report . | Call is marked as dequeued (if the call was dequeued before
                                                         								aborting) or abandoned in Contact Queue Detail record. |
| Q. | When an agent
                                       				transfers a call to another agent and the caller abandons the call, why is the
                                       				call not displayed in the Abandoned Call Detail Activity Report ? |
| A. | When an agent transfers a
                                          				  call to another agent, and the caller abandons the call before the call is
                                          				  answered by the second agent, then the first phase of the call is marked as
                                          				  handled. The abandonment of the second phase is not displayed in the Abandoned Detail Call Activity Report . This
                                          				  information cannot be seen in any other report. |

| Scenario | Contact Service Queue Activity Report | Abandoned Call Detail Activity Report |
|---|---|---|
| Call is abandoned during Prompt2 or Prompt3 | The Contact Queue Detail record marks the call as dequeued, but not as
                                                         								abandoned from any queue. So, the Contact Service Queue Activity
                                                            								  Report shows the call as dequeued from all CSQs to which the call
                                                         								was routed. | The Contact Call Detail
                                                         								record marks the call as abandoned. So, the Abandoned Call Detail Activity
                                                            								  Report shows the call as abandoned from all CSQs to which the call
                                                         								was routed. |
| Call gets aborted after being in the queue | Call is marked as aborted in the Contact Call Detail record. So,
                                                         								the CSQ reports display more abandoned calls than the Abandoned Call Detail Activity
                                                            								  Report . | Call is marked as dequeued (if the call was dequeued before
                                                         								aborting) or abandoned in Contact Queue Detail record. |

| Q. | Are the
                                       				ACD—Transfer In and ACD—Transfer Out calls included for calculating Inbound
                                       				ACD—Total field? |
|---|---|
| A. | Yes, these calls are
                                          				  included for calculating the Inbound ACD—Total field. |
| Q. | Why is the
                                       				total number of inbound calls different than the number of calls handled on the Contact Service Queue Activity by CSQ ? |
| A. | The number of calls can
                                          				  differ for the following reasons: The
                                                						Agent Call Summary Report shows calls that are presented to the agents, and the Contact Service Queue Activity by CSQ shows calls that are presented to the CSQs. If there are agents included in the
                                                						Agent Call Summary Report who do not belong to the CSQs in the Contact Service Queue Activity by CSQ ,
                                                						then the Agent Call Summary Report shows more
                                                						calls. If
                                                						agent-based routing is configured, calls can go to agents directly, without
                                                						going through a CSQ. In this case, the Agent Call Summary Report shows more
                                                						calls. The Agent Call Summary Report can include
                                                						transferred ACD calls. For example, if a call is queued for CSQ1, handled by
                                                						Agent1, and transferred by Agent1 to Agent2 (without going through a CSQ), then
                                                						one call is shown as handled on the Contact Service Queue Activity Report (through CSQ1 by Agent1). The same is shown twice on the Agent Call Summary Report —one as handled
                                                						by Agent1 (through CSQ1), another as handled by Agent2 (not through a CSQ but
                                                						as a direct transfer from Agent2). |

| Q. | Why are the
                                       				Hold Time and the Work Time fields blank for a call? |
|---|---|
| A. | The call was not an ACD
                                          				  call. (IVR calls include Agent-to-Agent calls and external calls made by an
                                          				  agent.) The Unified CCX database does not record hold time and work time for
                                          				  IVR calls. |
| Q. | Why is
                                       				Duration not equal to Talk Time + Hold Time + Work Time? |
| A. | The value in the duration
                                          				  field is calculated as follows: call end time – call start time The
                                          				  call start time is when the call rings at the agent extension. The call end
                                          				  time is when the agent leaves Work state. Therefore, the call duration is equal
                                          				  to ring time + talk time + hold time + work time. |
| Q. | How can I
                                       				identify IVR calls? |
| A. | The Hold Time and the Work
                                          				  Time fields are blank in the Agent Detail Report for IVR calls. |

| Q. | Why does a
                                       				less-than sign (<) precede the value in the Login Time field or a
                                       				greater-than sign (>) precede the value in the Logout Time field? |
|---|---|
| A. | A less-than sign (<)
                                          				  indicates that the agent logged in before the report start time. A greater-than
                                          				  sign (>) indicates that the agent logged out after the report end time. For
                                          				  example, if the report start time is 8:00 a.m. (0800) and the report end time
                                          				  is 6:00 p.m. (1800): The
                                                   						agent logged in at 7:45 a.m. (0745), the Login Time field will show < 8am
                                                   						(or < 0800). If the
                                                   						agent logged out at 6:30 p.m. (1830), the Logout Time field will show > 6pm
                                                   						(or > 1800). |

| Q. | Why do I see two rows for the agent with the same values? |
|---|---|
| A. | The report template defines the view of the report. There are two kinds of  summary rows (darker background)   that are defined
                                             in the template. The summary row that follows after each agent summarizes  details of the agent. The summary row that appears
                                             at the end of the report summarizes details of all the agents. If there is a single row for the agent, then the summary row of the agent will have the same details as the above row. |

| Q. | How is the
                                       				Average Logged In Time field calculated? |
|---|---|
| A. | This value is calculated as
                                          				  the total logged-in time divided by the number of login sessions. For
                                          				  example, if an agent logs in at 8:00 a.m. (0800) and logs out at 8:30a.m.
                                          				  (0830), logs in again at 9:15 a.m. (0915) and logs out at 10:00 a.m. (1000),
                                          				  then there are two login sessions. The first session lasts 30 minutes and the
                                          				  second session lasts 45 minutes. The average logged-in time is (30+45)/2 = 37.5
                                          				  minutes. |
| Q. | How is the
                                       				Handle Time field calculated? |
| A. | Handle time = Talk time +
                                          				  Hold time + Work time. |
| Q. | How is the
                                       				Idle Time—Avg field calculated? |
| A. | This value is calculated as
                                          				  the total idle time divided by the number of idle sessions. For
                                          				  example, if an agent goes to Not Ready state at 10:00 a.m. (1000) and goes to
                                          				  Ready state at 10:15 a.m. (1015), goes to Not Ready state at 11:00 a.m. (1100)
                                          				  and goes to Ready state at 11:05 a.m (1105), then there are two idle sessions.
                                          				  The first session lasts 15 minutes and the second session lasts 5 minutes. The
                                          				  average idle time is (15+5)/2 = 10 minutes. |
| Q. | Why do not
                                       				the values of Talk Time—Avg and Talk Time—Max fields in the Agent Summary Report match the values of Talk
                                       				Time field in the Agent State Summary by Agent Report or the Agent State Summary by Interval Report ? |
| A. | The talk time information
                                          				  in the Agent Summary Report comes from the talkTime
                                          				  field in the AgentConnectionDetail table. This value is the time that an agent
                                          				  spent on an incoming ACD call. The talk time information in the Agent State Summary by Agent Report or the Agent State Summary by Interval Report comes
                                          				  from AgentStateDetail table. These values show the time that an agent spent in
                                          				  the Talk state. These values will be different if the agent placed ACD calls on
                                          				  hold during the reporting period. |
| Q. | Does the Agent Summary Report show information for IVR
                                       				calls? |
| A. | The Agent Summary Report shows information for
                                          				  ACD calls only. The Agent Detail Report shows information for
                                          				  Unified CCX and Cisco Unified IP IVR calls. |

| Q. | What does it
                                       				mean when the Application ID field shows the value –1 and the Application Name
                                       				field is empty? |
|---|---|
| A. | The Application ID field is
                                          				  –1, and the Application Name field is empty for Agent-to-Agent calls, IVR
                                          				  calls, Agent-to-Agent transfer/conference consult legs, or any other call that
                                          				  is not placed to a Unified CCX Route Point or associated with an application. |
| Q. | Why is the
                                       				value in the Calls Presented field lower than the total number of calls on the Detailed Call by Call CCDR Report for the same
                                       				report period? |
| A. | The Application Performance Analysis Report counts only incoming calls. The Detailed Call by Call CCDR Report counts
                                          				  incoming calls, outgoing calls (for example, outbound calls made by agents),
                                          				  and internal calls (for example, Agent-to-Agent consult calls). |
| Q. | Why does the Application Performance Analysis Report show
                                       				more abandoned calls than the Contact Service Queue Activity Report for the
                                       				same report period? |
| A. | The Contact Service Queue Activity Report includes only abandoned ACD calls. This report counts an ACD call as abandoned
                                          				  if the caller hangs up while queued for a CSQ or CSQs. The Application Performance Analysis Report includes abandoned ACD calls and abandoned IVR calls. This report counts a call
                                          				  as abandoned if the call ends before it is answered by an agent or before it is
                                          				  marked as handled by a workflow. |

| Q. | What are the
                                       				values from Custom Variable 1 through Custom Variable 10 fields? |
|---|---|
| A. | These fields show the
                                          				  values of the custom variables that are specified in a workflow. For example, a workflow may designate variable1 as the menu
                                          				  option that the caller chooses, and designate variable2 as the account number
                                          				  that the caller enters. In this case, Custom Variable 1 would show the option
                                          				  value (such as 2) that the caller entered, and Custom Variable 2 would show the
                                          				  account number that was entered. |

| Q. | Common Skill CSQ Activity Report is similar
                                       				to other CSQ reports—how is it useful? |
|---|---|
| A. | This report provides
                                          				  additional information for multiple CSQs that are configured with the same call
                                          				  skill, but with different competence levels. An incoming call may be queued for
                                          				  the CSQ with the lowest-competence level. If no agent is available for a
                                          				  certain period, the call is queued for the next higher-competence level. The summary
                                          				  line in the report displays the summarized statistics for the group of CSQs
                                          				  configured with common skills. A group of CSQs that is configured in this
                                          				  manner is called a logical CSQ. |

| Q. | How are
                                       				average queue time and maximum queue time calculated? |
|---|---|
| A. | The average queue time for
                                          				  a CSQ is calculated as the sum of the queue times for all the calls presented
                                          				  divided by the number of calls presented. The maximum queue time for a CSQ is
                                          				  the longest queue time for a single call among the calls presented. The individual queue time for each CSQ is stored in the CQDR
                                          				  table. For example, assume that an incoming call is queued for CSQ1 for 5
                                          				  minutes, queued for CSQ2 for 10 minutes, and then it is handled by CSQ1. The
                                          				  queue time recorded for CSQ1 in the CQDR table is 5 minutes, and for CSQ2 is 10
                                          				  minutes. |
| Q. | How are
                                       				average calls abandoned (Avg Abandon Per Day field) and maximum calls abandoned
                                       				(Max Abandon Per Day field) calculated? |
| A. | Average calls abandoned for
                                          				  a CSQ is an average value per day. It is calculated as the total number of
                                          				  calls abandoned for the CSQ divided by the number of days in the report period. Maximum
                                          				  calls abandoned for a CSQ is calculated by determining the number of calls
                                          				  abandoned for each day in the report period and selecting the largest of these
                                          				  values. |
| Q. | The system
                                       				receives a call, queues it, and plays a prompt giving the caller the option to
                                       				press 1 to leave a message. The caller presses 1 and leaves a message. In this
                                       				scenario, is the call counted as abandoned or as handled? |
| A. | By default, the call is
                                          				  counted as abandoned instead of handled, because it did not connect to an
                                          				  agent. However, if the workflow is designed to mark a call as handled after a
                                          				  caller leaves a message, the call will be counted as handled. |
| Q. | If a workflow
                                       				gives callers the option to transfer to a voice messaging system, is there a
                                       				way to track the number of callers that make this transfer and leave a message? |
| A. | You can design a workflow
                                          				  to store a caller’s key input in one of the custom variables in the
                                          				  ContactCallDetail table. You can either generate the Call Custom Variables Report and manually
                                          				  count the rows that contain the desired information or you can create a custom
                                          				  report to provide this information. |
| Q. | Will calls
                                       				presented always equal calls handled + calls abandoned? |
| A. | No. Calls presented = calls
                                          				  handled + calls abandoned + calls dequeued + calls handled by others. "Calls handled" are the
                                          				  calls that were connected to an agent in a particular CSQ. "Calls
                                             					 handled by others" are the calls that were handled by some workflow in a
                                          				  script, and the calls that were queued for multiple CSQs and then handled by
                                          				  one of the other CSQs. |
| Q. | Can the Contact Service Queue Activity Report show
                                       				hourly data? And can hourly reports be generated automatically for each hour of
                                       				each day? |
| A. | To show hourly data for
                                          				  each day, schedule daily reports either for Contact Service Queue Activity by CSQ Report or for Contact Service Queue Activity Report by
                                             					 Interval . Set the Interval Length to 60 minutes. This setting will
                                          				  provide one report each day, divided into one-hour intervals. Separate hourly reports are not available, but with the interval
                                          				  length set to 60 minutes, a daily report will display 24 intervals, one for
                                          				  each hour of the day. |

| Q. | Why does the
                                       				same CSQ appear twice in the Contact Service Queue Activity by CSQ Report (and other CSQ reports)? |
|---|---|
| A. | A CSQ has many attributes,
                                          				  including CSQ name, service level, resource selection criterion, and auto work.
                                          				  Some attributes, such as CSQ name and service level, are displayed in the
                                          				  report. Other attributes are not displayed in the report. However, changing any
                                          				  attribute of the CSQ causes a new line to show in the report. For example: If the
                                                   						service level is changed from 10 to 25, two lines of the same CSQ will show in
                                                   						the report. One line will show the old service level value and another line
                                                   						will show the new service level value. If Auto
                                                   						Work is changed from 1 to 0, two lines of the same CSQ will be shown in the
                                                   						report. As the Auto Work setting does not appear in the report, the same CSQ
                                                   						will appear twice. |
| Q. | How do these
                                       				four fields differ—Percentage of Service Level Met—Only Handled, Percentage of
                                       				Service Level Met—With No Abandoned Calls, Percentage of Service Level Met—With
                                       				Abandoned Calls Counted Positively, and Percentage of Service Level Met—With
                                       				Abandoned Calls Counted Negatively? |
| A. | A call is categorized as
                                          				  handled if it is either answered by an agent or marked as handled by a
                                          				  workflow. Handled calls can be divided into the following categories: Handled
                                                   						within service level Handled
                                                   						after service level A call is
                                          				  categorized as abandoned if the call disconnects before an agent answers.
                                          				  Abandoned calls can be divided into the following categories: Abandoned within service level Abandoned after service level Field Description Calculation Percentage of Service Level Met—Only Handled This field shows only handled calls. It does not include
                                                      								abandoned calls. This field shows the percentage of handled calls that were
                                                      								handled within the service level. The remaining fields differ in how they account for abandoned
                                                      								calls: not counted, meeting service level, or not meeting service level. (Number of calls handled within service level / Number of calls
                                                      								handled) * 100% Percentage of Service Level Met—With No Abandoned Calls This field shows the percentage of presented calls (calls routed
                                                      								to a CSQ), not counting abandoned calls, that were handled within the service
                                                      								level. It does not include calls that were abandoned within the service level. This value is always less than or equal to the value in the
                                                      								Percentage of Service Level Met—Only Handled field (Number of calls handled within service level / (Number of calls
                                                      								presented – Number of calls abandoned within service level)) * 100% Percentage of Service Level Met—With Abandoned Calls Counted
                                                      								Positively The field shows the calls that are abandoned within the service
                                                      								level as meeting the service level. It shows the percentage of presented calls
                                                      								that were handled or abandoned within the service level. ((Number of calls handled within service level + Number of calls
                                                      								abandoned within service level) / Number of calls presented) * 100% Percentage of Service Level Met—With Abandoned Calls Counted
                                                      								Negatively The field shows the calls that are abandoned within the service
                                                      								level as not meeting the service level. It shows the percentage of presented
                                                      								calls that were handled within the service level. This value is less than or
                                                      								equal to the Percentage of Service Level Met—With Abandoned Calls Counted
                                                      								Positively field. (Number of calls handled within service level / Number of calls
                                                      								presented) * 100% | Field | Description | Calculation | Percentage of Service Level Met—Only Handled | This field shows only handled calls. It does not include
                                                      								abandoned calls. This field shows the percentage of handled calls that were
                                                      								handled within the service level. The remaining fields differ in how they account for abandoned
                                                      								calls: not counted, meeting service level, or not meeting service level. | (Number of calls handled within service level / Number of calls
                                                      								handled) * 100% | Percentage of Service Level Met—With No Abandoned Calls | This field shows the percentage of presented calls (calls routed
                                                      								to a CSQ), not counting abandoned calls, that were handled within the service
                                                      								level. It does not include calls that were abandoned within the service level. This value is always less than or equal to the value in the
                                                      								Percentage of Service Level Met—Only Handled field | (Number of calls handled within service level / (Number of calls
                                                      								presented – Number of calls abandoned within service level)) * 100% | Percentage of Service Level Met—With Abandoned Calls Counted
                                                      								Positively | The field shows the calls that are abandoned within the service
                                                      								level as meeting the service level. It shows the percentage of presented calls
                                                      								that were handled or abandoned within the service level. | ((Number of calls handled within service level + Number of calls
                                                      								abandoned within service level) / Number of calls presented) * 100% | Percentage of Service Level Met—With Abandoned Calls Counted
                                                      								Negatively | The field shows the calls that are abandoned within the service
                                                      								level as not meeting the service level. It shows the percentage of presented
                                                      								calls that were handled within the service level. This value is less than or
                                                      								equal to the Percentage of Service Level Met—With Abandoned Calls Counted
                                                      								Positively field. | (Number of calls handled within service level / Number of calls
                                                      								presented) * 100% |
| Field | Description | Calculation |
| Percentage of Service Level Met—Only Handled | This field shows only handled calls. It does not include
                                                      								abandoned calls. This field shows the percentage of handled calls that were
                                                      								handled within the service level. The remaining fields differ in how they account for abandoned
                                                      								calls: not counted, meeting service level, or not meeting service level. | (Number of calls handled within service level / Number of calls
                                                      								handled) * 100% |
| Percentage of Service Level Met—With No Abandoned Calls | This field shows the percentage of presented calls (calls routed
                                                      								to a CSQ), not counting abandoned calls, that were handled within the service
                                                      								level. It does not include calls that were abandoned within the service level. This value is always less than or equal to the value in the
                                                      								Percentage of Service Level Met—Only Handled field | (Number of calls handled within service level / (Number of calls
                                                      								presented – Number of calls abandoned within service level)) * 100% |
| Percentage of Service Level Met—With Abandoned Calls Counted
                                                      								Positively | The field shows the calls that are abandoned within the service
                                                      								level as meeting the service level. It shows the percentage of presented calls
                                                      								that were handled or abandoned within the service level. | ((Number of calls handled within service level + Number of calls
                                                      								abandoned within service level) / Number of calls presented) * 100% |
| Percentage of Service Level Met—With Abandoned Calls Counted
                                                      								Negatively | The field shows the calls that are abandoned within the service
                                                      								level as not meeting the service level. It shows the percentage of presented
                                                      								calls that were handled within the service level. This value is less than or
                                                      								equal to the Percentage of Service Level Met—With Abandoned Calls Counted
                                                      								Positively field. | (Number of calls handled within service level / Number of calls
                                                      								presented) * 100% |
| Q. | How is an
                                       				abandoned call counted if it is queued for multiple CSQs? |
| A. | If a call is queued for
                                          				  multiple CSQs and is abandoned, it is counted as abandoned from all the CSQs
                                          				  for which it is queued. For example, if a call is queued for CSQ1 and CSQ2 and the
                                          				  caller hangs up before being routed to an agent, then an abandoned call is
                                          				  counted for CSQ1 and for CSQ2. |
| Q. | How is a
                                       				dequeued call counted if it is queued for multiple CSQs? |
| A. | If a call is queued for
                                          				  multiple CSQs and is handled by one of them, then the call is counted as
                                          				  dequeued from each of the other CSQs. For example, if an incoming call is queued for CSQ1, CSQ2, and
                                          				  CSQ3 and is handled by an agent from CSQ2, then a dequeued call is counted for
                                          				  CSQ1 and for CSQ3. |
| Q. | After the
                                       				service level for a CSQ changes, why does the CSQ appear in the report
                                       				twice—once with the old service level and again with the new service level? |
| A. | The Unified CCX database
                                          				  maintains records of old and new service levels. When a new service level is
                                          				  configured, the old record is marked as inactive. The dateInactive field in the
                                          				  ContactServiceQueue table shows the date and time that the new service level
                                          				  was configured. If the value in the dateInactive field is in the report period,
                                          				  the report shows the active (new) and inactive (old) CSQs. |

| Field | Description | Calculation |
|---|---|---|
| Percentage of Service Level Met—Only Handled | This field shows only handled calls. It does not include
                                                      								abandoned calls. This field shows the percentage of handled calls that were
                                                      								handled within the service level. The remaining fields differ in how they account for abandoned
                                                      								calls: not counted, meeting service level, or not meeting service level. | (Number of calls handled within service level / Number of calls
                                                      								handled) * 100% |
| Percentage of Service Level Met—With No Abandoned Calls | This field shows the percentage of presented calls (calls routed
                                                      								to a CSQ), not counting abandoned calls, that were handled within the service
                                                      								level. It does not include calls that were abandoned within the service level. This value is always less than or equal to the value in the
                                                      								Percentage of Service Level Met—Only Handled field | (Number of calls handled within service level / (Number of calls
                                                      								presented – Number of calls abandoned within service level)) * 100% |
| Percentage of Service Level Met—With Abandoned Calls Counted
                                                      								Positively | The field shows the calls that are abandoned within the service
                                                      								level as meeting the service level. It shows the percentage of presented calls
                                                      								that were handled or abandoned within the service level. | ((Number of calls handled within service level + Number of calls
                                                      								abandoned within service level) / Number of calls presented) * 100% |
| Percentage of Service Level Met—With Abandoned Calls Counted
                                                      								Negatively | The field shows the calls that are abandoned within the service
                                                      								level as not meeting the service level. It shows the percentage of presented
                                                      								calls that were handled within the service level. This value is less than or
                                                      								equal to the Percentage of Service Level Met—With Abandoned Calls Counted
                                                      								Positively field. | (Number of calls handled within service level / Number of calls
                                                      								presented) * 100% |

| Q. | What are a
                                       				session ID and a session sequence number? |
|---|---|
| A. | A session ID is a unique
                                          				  identification number that the system assigns to a call. This number remains
                                          				  the same for the entire call. The system also assigns a sequence number to each
                                          				  leg of a call. Sequence numbers start at 0 and increment by 1 each time the
                                          				  call is transferred or redirected. |
| Q. | Can a call be
                                       				marked as handled if it is never queued for a CSQ? |
| A. | Yes. You can design a
                                          				  workflow to mark such a call as handled. |
| Q. | Why are the
                                       				Hold Time and the Work Time fields blank? |
| A. | The call was an IVR call.
                                          				  (IVR calls include Agent-to-Agent calls and external calls that are made by an
                                          				  agent.) The Unified CCX database does not record hold time and work time for
                                          				  IVR calls. |
| Q. | Why does the
                                       				report show duplicate calls? |
| A. | The calls in the CCDR
                                          				  Report are not duplicates. They are conference calls, which have the same
                                          				  SessionID and Session Sequence Number, but different talk time because
                                          				  different agents participated in the same call. (The Detailed Call by Call CCDR Report shows the
                                          				  names of agents who participated in a conference call.) |
| Q. | What does it
                                       				mean when the Contact—Disposition is 3? |
| A. | When the system removes
                                          				  stuck calls, which may have remained in the system because of missing events,
                                          				  the system writes a CCDR with the contact disposition dont_care (value = 3). |

| Q. | What is the
                                       				sampling frequency for the report? |
|---|---|
| A. | Data is
                                          				  sampled per minute. The report aggregates the data over an hour (maximum of all
                                          				  samples within the hour). |
| Q. | How are
                                       				calls that are less than a minute treated? |
| A. | If a call
                                          				  duration is less than a minute and its start and end times fall between two
                                          				  sampling points, then this call will not be considered for the statistics. |

| Q. | Why is there
                                       				a difference between the Total Incoming Calls field in the Traffic Analysis Report and the Total Incoming
                                       				Calls field in the Application Performance Analysis Report ? |
|---|---|
| A. | An incoming call can have
                                          				  multiple call legs. The Traffic Analysis Report counts a call with
                                          				  multiple legs as a single call. However, each call leg may invoke a different
                                          				  application, so the Application Performance Analysis Report counts each call leg as a call. For example, if a call comes into an Auto Attendant and the
                                          				  caller selects a menu option for Musician Demonstration, then the call will
                                          				  have two call legs: Session ID = 1, sequence number = 0, application = "auto
                                                      						  attendant" Session ID = 1, sequence number = 1, application = "musician demonstration" This call is counted once for the Traffic Analysis Report . It is counted twice
                                          				  for the Application Performance Analysis Report —once
                                          				  for the "auto
                                             					 attendant" application and once for the "musician
                                             					 demonstration" application. |