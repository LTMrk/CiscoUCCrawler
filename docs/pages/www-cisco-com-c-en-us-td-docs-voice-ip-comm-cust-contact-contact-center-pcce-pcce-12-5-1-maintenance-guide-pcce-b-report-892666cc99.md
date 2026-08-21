---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-pcce-pcce-12-5-1-maintenance-guide-pcce-b-report-892666cc99
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/pcce/pcce_12_5_1/maintenance/guide/pcce_b_Reporting-User-Guide-12-5/pcce_b_cisco-packaged-contact-center-enterprise_chapter_01111.html
retrieved_at: 2026-08-21T16:58:18.268755+00:00
---

Cisco Packaged Contact Center Enterprise Reporting User Guide, Release 12.5(1)

# Cisco Packaged Contact Center Enterprise Reporting User Guide, Release 12.5(1)

Updated: February 4, 2020

Chapter: Cisco Unified CVP
	 Reporting

## Chapter: Cisco Unified CVP
	 Reporting

- Cisco Unified CVP                              	 Reporting

- Cisco Unified CVP                              	 Application Reporting

- Trunks and Trunk Groups

# Cisco Unified CVP
                     	 Reporting

## Cisco Unified CVP
                        	 Application Reporting

Cisco Unified
                           		Customer Voice Portal (CVP) is a Voice Response Unit (VRU) that is used for
                           		customer self-service, information gathering, and queuing. Self-service
                           		applications allow customers to handle their own needs, such as looking up an
                           		account balance or entering payment information, without having to talk with an
                           		agent. Information gathering applications are used to decide what skill group
                           		to queue the call to by walking the caller through a series of voice prompts.
                           		The Caller Entered Digits (CED) are passed back from the Unified CVP to be used
                           		within the routing script, to decide the optimal skill group to answer the
                           		call.

The manner in which
                           		your enterprise uses Unified CVP determines what report data you should
                           		monitor:

If Unified CVP
                                 			 performs queuing ,
                                 			 you might want to see how long callers waited in queue and the number of
                                 			 callers who abandoned while queued.

If Unified CVP
                                 			 is used for self-service , you might want to see the following metrics:

How many
                                       				  calls traversed the application.

How many
                                       				  successful transactions occurred in the self-service application. For example,
                                       				  in a banking application a customer might have the ability to perform multiple
                                       				  transactions, such as account lookup, obtaining balance information, and
                                       				  learning about recent payments. You might want to see which of these
                                       				  transactions was used, and whether the caller successfully completed the
                                       				  transaction.

Whether
                                       				  callers handled their needs through the self-service application or were
                                       				  transferred to an agent.

If a system
                                       				  error, such as a failed database lookup, caused a caller to be transferred by
                                       				  an agent instead of continuing through the self-service application.

If Unified CVP
                                 			 is used for information
                                    				gathering , you might want to see the following metrics:

How many
                                       				  calls traversed the application.

How long
                                       				  each call remained in the application.

How many
                                       				  calls disconnected before being routed to an agent.

How many
                                       				  calls were eventually routed to agents.

How many
                                       				  callers opted out of the digit collection to be transferred directly to an
                                       				  agent.

If a system
                                       				  error, such as a failed database lookup, caused the caller to be transferred to
                                       				  an agent instead of continuing through the digit collection prompts for more
                                       				  appropriate routing.

If a self-service or
                           		information gathering application is used before the call is queued, change the
                           		call type just before Queue node. Changing the call type resets the service
                           		level timer; time spent in the self-service or information gathering
                           		application does not count against the service level for the second call type.
                           		If you do not change call types prior to the Queue node, the self-service or
                           		information gathering time is included in the calculation of service level,
                           		having a negative impact on your service level. See the following figure.

The following
                           		illustration shows how a call moves from the information gathering application
                           		to the queuing applications.

In this example, 20
                           		seconds will be used to calculate ASA and decide the service level instead of
                           		50 seconds (30 + 20 seconds).

The following table
                           		illustrates how some basic metrics are defined at the call type and skill
                           		group.

Report
                                       				  metric

Call type

Skill group

Abandon Wait
                                       				  Time

Starts when
                                       				  a call first enters a call type and ends when it abandons.

Not
                                       				  Applicable

Average
                                       				  Speed of Answer (ASA)

Starts at
                                       				  the first Queue to Skill Group node in the routing script.

Starts at
                                       				  the first Queue to Skill Group node in the routing script.

Service
                                       				  Level

Starts as
                                       				  soon as the call enters the call type that has the service level defined.

Not
                                       				  Applicable

## Trunks and Trunk Groups

Every peripheral has one or more associated trunk groups, with
                              each trunk group containing one, or more physical trunks.

You can
                              report on data such as the number of trunks in service, number of trunks idle,
                              and the time during which all trunks in a trunk group were simultaneously busy
                              (All Trunks Busy).

| Note | If the call
                                    		abandons before being changed to the call type that handles queuing, the Call
                                    		Abandon Wait time is not reset. Therefore, the Abandon Wait time for the
                                    		information gathering call type starts when the call enters the first call
                                    		type, and ends when the call abandons, as illustrated below: |
|---|---|

| Report
                                       				  metric | Call type | Skill group |
|---|---|---|
| Abandon Wait
                                       				  Time | Starts when
                                       				  a call first enters a call type and ends when it abandons. | Not
                                       				  Applicable |
| Average
                                       				  Speed of Answer (ASA) | Starts at
                                       				  the first Queue to Skill Group node in the routing script. | Starts at
                                       				  the first Queue to Skill Group node in the routing script. |
| Service
                                       				  Level | Starts as
                                       				  soon as the call enters the call type that has the service level defined. | Not
                                       				  Applicable |