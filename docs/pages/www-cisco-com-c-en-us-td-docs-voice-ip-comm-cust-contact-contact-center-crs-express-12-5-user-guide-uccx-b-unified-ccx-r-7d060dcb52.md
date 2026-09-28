---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-crs-express-12-5-user-guide-uccx-b-unified-ccx-r-7d060dcb52
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/crs/express_12_5/user/guide/uccx_b_unified-ccx-reporting-user-guide-125/uccx_b_unified-ccx-reporting-user-guide-125_appendix_01011.html
retrieved_at: 2026-08-16T21:26:56.685629+00:00
---

Cisco Unified Contact Center Express Reporting User Guide, Release 12.5(1)

# Cisco Unified Contact Center Express Reporting User Guide, Release 12.5(1)

Updated: January 31, 2020

Chapter: Glossary

## Chapter: Glossary

- Glossary

# Glossary

## A

For an agent-based call (Unified CCX call), a call is considered abandoned if it is not answered by an agent or the caller
                                          hangs up or the call is disconnected.

For Unified IP IVR call, a call is considered abandoned if it does not reach the workflow step that sets the Handled flag.

If a call has more than one leg that is abandoned, for example, a Unified IP IVR call that is processed by different applications,
                                          each abandoned leg is counted as an abandoned call.

An abandoned
                                    				  chat is a chat that is routed to the CSQ but not accepted by an agent, because
                                    				  the chat submitter ended the chat before an agent accepted.

The system
                                    				  abandons a call when a customer answers the phone if an IVR port is not
                                    				  available to play the prompts to the customer. So, Unified CCX fails to
                                    				  transfer the call to the IVR port.

A call is
                                    				  aborted if an exception occurs in the workflow that is processing a call, for
                                    				  example, UndefinedPromptException or ApplicationMaxSessionsException. In such
                                    				  cases, Unified CCX sets up media and plays the error message to the caller.

A call is
                                    				  considered accepted if the agent clicks Accept when presented with the call. A
                                    				  call that is routed to an agent, skipped or rejected by that agent, routed to
                                    				  another agent, and then accepted by that agent is counted once.

Automatic
                                    				  Call Distribution (ACD) or Incoming Call Distribution (ICD) calls are calls
                                    				  that are processed through a workflow and queued to the agent. Calls are dialed
                                    				  to an ICD route point number.

Agent
                                    				  enters reason codes when moving to Logout or Not Ready state. For more information, see
                                       					 the Cisco Finesse Administration Guide , located at:

https://www.cisco.com/c/en/us/support/customer-collaboration/finesse/products-user-guide-list.html .

A contact
                                    				  is considered attempted if the contact is dialed out by the IVR dialer. If the
                                    				  same contact is retried, the attempt does not fall under the Attempted
                                    				  category. Even though a contact is retried multiple times, the attempted
                                    				  contact is counted only once.

A contact is considered attempted when an outbound call is placed to the customer, regardless of the outcome. A call record
                                          is considered attempted if an agent clicks Accept for this contact.

A contact that is routed to and accepted by an agent is considered attempted by the system. If the contact is marked for
                                          callback and later called by the same or another agent, this call record is still attempted once.

## C

A call is
                                    				  considered closed if the agent clicks either Skip-Close or Reject-Close. These
                                    				  contacts are not dialed again.

## D

A call is dequeued from a particular CSQ for the following reasons:

The call is dequeued by a Dequeue step in a workflow.

The call is marked as handled by a workflow.

The call is queued for more than one CSQ and is handled by an agent in another CSQ.

## F

Dialer asks the gateway to cancel a call that is not yet placed.

Gateway declined the call.

Gateway is down or Gateway timed out while the call is being placed.

Gateway failure or configuration issues at the Gateway.

## H

A call is considered handled:

When the call state is one of these—Voice, Answering Machine, Invalid Number, or Fax/Modem.

Call reaches the workflow step that defines the call as handled.

Call is handled by an agent.

A chat is
                                    				  considered handled if an agent accepts the chat that is presented by the chat
                                    				  submitter while the chat submitter is queued for this CSQ.

## I

IP Phone Agent is an
                                    				  agent who has access to only a phone and not Cisco Finesse Agent Desktop.

## N

A call that
                                    				  is not dialed to an ICD route point number. For example, an internal call
                                    				  between agents or an outbound call.

A call that
                                    				  is dialed to the agent&apos;s non-Unified CCX extension.

## O

Outbound
                                    				  calls that are offered to the agent, including accepted, rejected, and closed
                                    				  calls.

A contact
                                    				  that is offered to an agent multiple times, possibly because the agent skipped
                                    				  the call and the call is looped back to the same agent, is counted once for
                                    				  each time the contact is presented.

## P

Calls sent
                                    				  to the agent irrespective of whether the agent answers the call. If a call is
                                    				  connected to an agent, transferred to another agent, and then transferred back
                                    				  to the original agent, the value for the original agent increases by two (once
                                    				  for each time the call was presented)

## R

A call is
                                    				  considered as rejected when Unified Communications Manager or Unified CCX
                                    				  resources are not sufficient for accepting incoming calls as system resources
                                    				  reach their maximum capacity, for example, insufficient number of CTI ports.

A call is
                                    				  considered rejected if the agent clicks either Reject or Skip or Cancel
                                    				  Reservation. These contacts are dialed again. If a contact is rejected by
                                    				  multiple agents, then the field is incremented each time the contact is
                                    				  rejected.

## S

The
                                    				  percentage of calls answered within the amount of time that is specified in the
                                    				  service level threshold for a CSQ.

The agent
                                    				  accepts the call, and selects a classification of Voice for this contact. The
                                    				  calls that are marked with this classification are a subset of accepted calls.

Built-in
                                    				  reason codes are generated when the Unified CCX server moves an agent to Logout
                                    				  state or Not Ready state. The Agent State Detail table includes a valid reason
                                    				  code for these two states. Reason code for other states is zero.

## T

Talk time
                                    				  is the elapsed time between the time that an agent connects to a call and the
                                    				  time the call is disconnected or transferred, not including hold time.

## U

A call that
                                    				  is dialed to the agent&apos;s Unified CCX extension.

## W

Wait time
                                    				  is the time that elapsed between the time a call entered the queue and the time
                                    				  the call was answered by an agent or was disconnected.