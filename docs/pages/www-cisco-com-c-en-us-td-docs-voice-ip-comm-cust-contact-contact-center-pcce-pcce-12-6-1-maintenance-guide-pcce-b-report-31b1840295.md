---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-pcce-pcce-12-6-1-maintenance-guide-pcce-b-report-31b1840295
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/pcce/pcce_12_6_1/maintenance/guide/pcce_b_Reporting-User-Guide-12_6_1/pcce_b_cisco-packaged-contact-center-enterprise_chapter_01101.html
retrieved_at: 2026-08-21T16:56:23.814611+00:00
---

Cisco Packaged Contact Center Enterprise Reporting User Guide, Release 12.6(1)

# Cisco Packaged Contact Center Enterprise Reporting User Guide, Release 12.6(1)

Updated: May 10, 2021

Chapter: Call Type Reporting

## Chapter: Call Type Reporting

# Call Type Reporting

## Call Type
                        	 Activity

Call type is the
                           		highest level reporting entity. Call type reports provide the most insight into
                           		call treatment and a caller's overall experience with the system.

A call type is a
                           		category of incoming call, and is used to select a routing script for a call.
                           		Administrators can create call types that correlate to the type of service the
                           		caller wants, and can change the call type during a routing script to direct the
                           		call to a new routing script or to gather report metrics for different legs or
                           		transactions. For example, your system may have call types configured for the
                           		following situations:

Transfers and
                                 			 conferences, to direct the call to a different routing script and gather call
                                 			 type report metrics for transfers and conferences.

Individual
                                 			 transactions in CVP Self-Service and Information Gathering applications, to be
                                 			 able to report on those transactions.

Queuing, to
                                 			 separate Information Gathering and queue metrics. For example, you might change
                                 			 the call type when a call completes an Information Gathering script and enters
                                 			 a queue.

CVP Ring No
                                 			 Answer (RONA), to direct calls to a routing script designed for this situation,
                                 			 and to use call type reports to see how calls that experience CVP RONA are
                                 			 eventually handled.

Supervisor and
                                 			 Emergency Assist, to direct the assistance request to a routing script that
                                 			 assigns the request to the team's primary or secondary supervisor, and to use
                                 			 call type reports to view data about supervisor assistance requests.

Key call type
                           		metrics include the following:

Average speed of
                                 			 answer.

Number of calls
                                 			 received and handled.

Number of calls
                                 			 that abandoned while en-route to CVP, at CVP, while en-route to an agent, or
                                 			 while being offered to an agent.

How long callers
                                 			 waited in queue.

Number of calls
                                 			 queued for an available agent.

Whether service
                                 			 level objectives are being met.

Number of
                                 			 transfers and conferences.

Number of calls
                                 			 that were given the busy, ring, default-routed, or network-routed treatment.

Number of calls
                                 			 that encountered an error.

Number of calls
                                 			 that have a bad label.

Number of calls
                                 			 that re-routed on no answer from the agent's phone.

## How Call Errors Affect Call Type Reporting

The way call errors increment the database depends on
                              the following conditions:

Calls that abandon en route to the Packaged CCE/CVP scripts are calls that abandon in the network while they are being sent to the VRU. An example of this condition is if a
                                    call abandons while it is sent to the VRU from a CTI Route point in Unified Communications Manager. These calls increment
                                    the ErrorCount column in the Call_Type tables.

If the caller abandons within the Abandon Wait Time,
                                    calls that abandon en route to CVP might be counted as short calls, instead
                                    of as errors.

Calls that
                                    abandon en route to agents are calls that encounter an error when the call is
                                    at the agent desktop. This call is counted as part of the AgentErrorCount in
                                    the Call_Type tables.

The Calls Error field in call
                              type reports is a calculated field that combines both error columns. For
                              example, the Calls Error field in the Call Type Historical All Fields report is
                              derived from Call_Type_Interval.IncompleteCalls +
                              Call_Type_Interval.AgentErrorCount.

## How Calls That Experience CVP Ring No Answer Affect Call Type Reporting

The CVP Ring No Answer feature ensures that when an agent does
                           not answer a call after a specified number of seconds, the call is taken away from the agent and re-assigned to another agent
                           or requeued. The original agent is made Not Ready.

You can configure the routing script to handle
                           CVP Ring  No Answer situations in two ways: the script can change the call
                           type when the calls is requeried, or the script can continue to use the same
                           call type. The manner in which you script for
                           CVP Ring No Answer affects the report data that you see, as follows:

If you change the call type, then CallsOffered,
                                 CallsRequeried, and OverflowOut are updated for the initial call type.
                                 CallsOffered and fields related to the completion of the call, such as
                                 CallsHandled, are incremented for the second call type.

Using two
                                 call types enables you to identify CVP Ring No Answer occurrences in call
                                 type reports. For example, if you create a specific call type for use in
                                 Ring No Answer situations, then you can see whether calls are
                                 redirecting by monitoring the calls offered to that call type. You can also see
                                 whether the FlowOut field is incremented for other call types.

If you do not change the call type, CallsOffered and fields related
                                 to the completion of the call, such as CallsHandled, are incremented. FlowOut
                                 is not incremented. You need to use agent or skill group reports to view a count of  CVP Ring No Answer calls; you cannot
                                 tell from  call type reports whether calls are experiencing CVP Ring No Answer.

Because the Unified CVP application performs a requery to redirect the
                                       call to a different agent or skill group instead of branching to another
                                       script, the CallsRONA field is not incremented for the call type.

| Note | Because the Unified CVP application performs a requery to redirect the
                                       call to a different agent or skill group instead of branching to another
                                       script, the CallsRONA field is not incremented for the call type. |
|---|---|