---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-crs-express-12-5-reference-guide-uccx-b-125repor-6b7c515c6d
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/crs/express_12_5/reference/guide/uccx_b_125report-developers-guide/uccx_b_125report-developers-guide_chapter_011.html
retrieved_at: 2026-08-16T21:04:17.857016+00:00
---

Cisco Unified Contact Center Express Report Developer Guide, Release 12.5(1)

# Cisco Unified Contact Center Express Report Developer Guide, Release 12.5(1)

## Results

Updated: February 7, 2020

Chapter: Interpret Database Records

## Chapter: Interpret Database Records

# Interpret Database Records

## Overview

The following abbreviations are used for database records:

ACDR—AgentConnectionDetail record in the AgentConnectionDetail table.

ASDR—AgentStateDetail record in the AgentStateDetail table.

CCDR—ContactCallDetail record in the ContactCallDetail table.

CQDR—ContactQueueDetail record in the ContactQueueDetail table.

CRDR—ContactRoutingDetail record in the ContactRoutingDetail table.

TACDR—TextAgentConnectionDetail record in the TextAgentConnectionDetail table.

TCDR—TextContactDetail records in the TextContactDetail table.

TASDR—TextAgentStateDetail records in the TextAgentStateDetail table.

TCQDR—TextContactQueueDetail record in the TextContactQueueDetail table.

## Call
                        	 Scenarios

The following assumptions are made for the call scenarios:

Auto-work is disabled for incoming Automatic Call Distribution (ACD) calls.

Auto-available is enabled for agents.

### Call-Related
                           	 Detail Records Flow

The
                                 		  following table presents an example of the general flow of detail records for
                                 		  incoming ACD calls.

Assumptions

Contact Service Queue (CSQ) is configured for auto-work.

Agent is configured for auto-available.

Call activity

Detail record activity

Call reaches the CTI port

Allocates session.

Begins CCDR in memory.

Call executes the first Select Resource step

Begins CRDR and CQDR in memory.

System selects agent and rings the phone

Begins ACDR in memory, writes ASDR to change state to Reserved.

Agent answers

Writes ASDR (Talking).

Call disconnects

Writes CRDR, CQDRs, ASDR (Work).

Agent leaves Work state

Writes ACDR, CCDR, ASDR (Ready).

If the
                                 		  agent does not enter Work state after the call, the system writes the ACDR and
                                 		  the ASDR (Ready) when the call disconnects. If the agent is not configured to
                                 		  be auto-available, the ASDR relates to the Not Ready state.

### Basic ACD Call
                           	 Queues for One CSQ

Call reaches a
                                          				Unified CCX route point, executes a script, and queues for one CSQ.

System
                                          				allocates agent A for the call and rings agent A’s phone, and agent A answers
                                          				the call.

Record

Session ID

Session sequence number

qIndex

Remarks

CCDR1

100

0

—

—

CRDR1

100

0

1

Overall queue information.

CQDR1

100

0

1

Detailed queue information for CSQ1 (targetType = 0; indicates
                                             					 CSQ-based routing).

ACDR1

100

0

1

Agent A and original call information.

Record

Reason

Remarks

ASDR1

4 (Reserved)

Agent A is selected for call.

ASDR2

5 (Talking)

Agent A answers call.

ASDR3

3 (Ready)

Call ends.

### Basic ACD Call
                           	 Queues for Two CSQs

Call reaches a Unified CCX route point, executes a script, and queues for two CSQs.

System allocates agent A for the call and rings agent A’s phone, and agent A answers the call.

Record

Session ID

Session sequence number

qIndex

Remarks

CCDR1

100

0

—

—

CRDR1

100

0

1

Overall queue information.

CQDR1

100

0

1

Overall queue information for CSQ1 (targetType = 0, targetID =
                                             					 ID of CSQ1).

CQDR2

100

0

1

Overall queue information for CSQ2 (targetType = 0, targetID =
                                             					 ID of CSQ2).

ACDR1

100

0

1

Agent A and original call information.

### Basic ACD Call
                           	 Wrap-Up

Call reaches a Unified CCX route point, executes a script, and queues for one CSQ.

System allocates agent A for the call and rings agent A’s phone, and agent A answers the call.

After completing the call, agent A goes to Work state, and chooses a wrap-up code.

Record

Session ID

Session sequence number

qIndex

Remarks

CCDR1

100

0

—

—

CRDR1

100

0

1

Overall queue information.

CQDR1

100

0

1

Detailed queue information for CSQ1 (targetType = 0; indicates
                                             					 CSQ-based routing).

ACDR1

100

0

1

Agent A and original call information with wrap-up code.

Record

Reason

Remarks

ASDR1

4 (Reserved)

Agent A is selected for call.

ASDR2

5 (Talking)

Agent A answers call.

ASDR3

6 (Work)

Call ends.

ASDR4

3 (Ready)

Agent A goes to Ready state.

### Basic Agent-Based
                           	 Routing Call

Call reaches a Unified CCX route point, executes a script, and selects agent A.

System allocates agent A for the call and rings agent A’s phone, and agent A answers the call.

Record

Reason

Remarks

ASDR1

4 (Reserved)

Agent A is selected for call.

ASDR2

5 (Talking)

Agent A answers call.

ASDR3

3 (Ready)

Call ends.

Record

Session ID

Session sequence number

qIndex

Remarks

CCDR1

100

0

—

—

CRDR1

100

0

1

Overall queue information.

CQDR1

100

0

1

Detailed information for the routing attempt (targetType = 1;
                                             					 indicates agent-based routing).

ACDR1

100

0

1

Agent A and original call information.

Record

Reason

Remarks

ASDR1

4 (Reserved)

Agent A is selected for call.

ASDR2

5 (Talking)

Agent A answers call.

ASDR3

3 (Ready)

Call ends.

### Transfer to Route
                           	 Point

Call reaches a Unified CCX route point, executes a script, and queues for one CSQ.

System allocates agent A for the call and rings agent A’s phone, and agent A answers the call.

Agent A transfers the call to a Unified CCX route point.

Call executes a script, queues for one or more CSQs, and connects to agent B.

Server begins a new session and CCDR as soon as agent A starts the consult call.

Server writes the CCDR for the consult call either when agent A completes the transfer or when agent A or the script terminates
                                       that call.

Record

Session ID

Session sequence number

qIndex

Remarks

CCDR1

100

0

—

Transfer field will be 1.

CRDR1

100

0

1

Overall queue information for the first segment of the call
                                             					 (before the transfer).

ACDR1

100

0

1

Agent A and original call information.

CQDR1

100

0

1

Detailed queue information for the CSQ that is selected by the
                                             					 first route point’s script.

CCDR2

101

0

—

Consult call from agent A to route point.

CCDR3

100

1

—

Second leg of original call to new route point.

CRDR3

100

1

—

Overall queue information for the second segment of the call
                                             					 (after the transfer).

CQDR3

100

1

1

Queue information for second leg of call.

ACDR3

100

1

1

Agent B and original call information.

### Conference to
                           	 Agent

Call reaches a Unified CCX route point, executes a script, and queues for one CSQ.

System allocates agent A for the call and rings agent A’s phone, and agent A answers the call.

Agent A calls another logged-in agent (agent B), and conferences agent B into the original call.

Server begins a new session and CCDR as soon as agent A starts the consult call.

Server writes the CCDR for the consult call either when agent A completes the conference or when agent A or agent B terminates
                                       the consult call.

The server does not create a new CCDR or CRDR after the conference is completed.

An asterisk (*) indicates that another record has the same name, but the record is for a different agent.

Record

Session ID

Session sequence number

qIndex

Remarks

CCDR1

100

0

—

Conference field will be 1.

CRDR1

100

0

1

Overall queue information.

ACDR1

100

0

1

Agent A and original call information.

CQDR1

100

0

1

Detailed queue information for CSQ1 (targetType = 0; indicates
                                             					 CSQ-based routing).

CCDR2

101

0

—

Consult call from agent A to agent B.

ACDR1*

100

0

0

Agent B and original call information.

### Workflow Redirect
                           	 to Route Point

Call reaches a Unified CCX route point.

Workflow for that route point redirects the call to a second route point.

Record

Session ID

Session sequence number

Remarks

CCDR1

100

0

Caller to first route point (redirect field will be 1).

CCDR2

100

1

Caller to second route point.

### ACD Call
                           	 Unanswered

Call reaches a Unified CCX route point, executes a script, and queues for one or more CSQs.

System allocates agent A for the call and rings agent A’s phone, but agent A does not answer the call within the timeout specified
                                       in the Select Resource or Connect step.

Call goes into queue and is presented to agent B, who answers the call.

Record

Session ID

Session sequence number

qIndex

Remarks

CCDR1

100

0

—

—

CRDR1

100

0

1

Overall queue information.

CQDR1

100

0

1

Detailed queue information for the CSQ selected by the route
                                             					 point script.

ACDR1

100

0

1

Agent A information, ring time > 0 and talk time = 0.

ACDR1*

100

0

1

Agent B information, talk time > 0.

Record

Agent

State

Reason Code

Remarks

ASDR1

A

4 (Reserved)

—

Agent A is selected for call.

ASDR2

A

2 (Not Ready)

32763

Server retrieves call from the agent's phone.

ASDR3

B

4 (Reserved)

—

Agent B is selected for call.

ASDR4

B

5 (Talking)

—

Agent B answers call.

### Agent-to-Agent
                           	 Non-ACD Call

Agent A goes off-hook and calls agent B.

Agent B answers, the two agents talk for a while, and agent B hangs up.

Record

Session ID

Session sequence number

Remarks

CCDR1

100

0

Agent A to agent B information.

Record

Agent

State

Reason Code

Remarks

ASDR1

A

2 (Not Ready)

32762

Agent A goes off-hook.

ASDR2

B

2 (Not Ready)

32761

Call rings at agent B’s phone.

ASDR3

B

3 (Ready)

—

Agent B hangs up.

ASDR4

A

3 (Ready)

—

—

### Agent-to-Agent
                           	 Non-ACD Call Transfer

Agent A receives a non-ACD call from an unknown party.

Agent A places a consult call to agent B, agent B answers the call, and agent A completes the transfer.

Agent B then hangs up.

Record

Session ID

Session sequence number

Remarks

CCDR1

100

0

Unknown party to agent A information (transfer field will be 1).

CCDR2

101

0

Agent A to agent B information.

CCDR3

100

1

Unknown party to agent B information.

Record

Agent

State

Reason Code

Remarks

ASDR1

A

2 (Not Ready)

32761

First call rings at agent A’s phone.

ASDR2

B

2 (Not Ready)

32761

Consult call rings at agent B’s phone.

ASDR3

A

3 (Ready)

—

Agent A completes transfer.

ASDR4

B

3 (Ready)

—

Agent B hangs up.

### Agent-to-Agent
                           	 Non-ACD Call Conference

Agent A receives a non-ACD call from an unknown party.

Agent A places a consult call to agent B, and agent B answers the call.

Agent A establishes a conference; agent A, agent B, and the caller are in conversation.

Agent A hangs up.

Agent B hangs up.

Record

Session ID

Session sequence number

Remarks

CCDR1

100

0

Unknown party to agent A information (conference field will be
                                             					 1).

CCDR2

101

0

Agent A to agent B information.

Record

Agent

State

Reason Code

Remarks

ASDR1

A

2 (Not Ready)

32761

First call rings at agent A's phone.

ASDR2

B

2 (Not Ready)

32761

Consult call rings at agent B's phone.

ASDR3

A

3 (Ready)

—

Agent A hangs up.

ASDR4

B

3 (Ready)

—

Agent B hangs up.

### ACD Call Consult
                           	 Transfer

Agent A is connected and talking to an incoming ACD call.

Agent A puts the call on hold and places a consult transfer to agent B.

Agent A completes the transfer and then agent B answers.

Record

Session ID

Session sequence number

qIndex

Remarks

CCDR1

100

0

—

Original call and agent A information (transfer
                                             					 field will be 1).

CRDR1

100

0

1

Overall queue information.

ACDR1

100

0

1

Agent A information.

CQDR1

100

0

1

Queue information.

CCDR2

101

0

—

Agent A and agent B information.

CCDR3

100

1

—

Original call and agent B information.

ACDR3

100

1

0

Agent B information.

Record

Agent

Reason

Remarks

ASDR1

A

4 (Reserved)

Agent A is selected for original call.

ASDR2

A

5 (Talking)

Agent A answers.

ASDR3

B

4 (Reserved)

Agent A calls agent B, agent B’s phone rings.

ASDR4

A

3 (Ready)

Agent A competes the transfer.

ASDR5

B

5 (Talking)

Agent B answers.

ASDR6

B

3 (Ready)

Caller hangs up.

### ACD Call Blind
                           	 Transfer to Agent Extension(ACD/Non-ACD)

Agent A is
                                          				connected and talking to an incoming ACD call.

Agent A
                                          				places a blind transfer to agent B's extension.

Agent B
                                          				answers, Agent A moves to Ready state.

Record

Session ID

Session sequence number

qIndex

Remarks

CCDR

100

0

-

Contact and agent information.

CRDR

100

0

1

Overall queue information of CSQ of incoming ICD call.

ACDR1

100

0

1

Agent A information.

CQDR

100

0

1

Queue information.

ACDR2

100

0

0

Agent B information.

Record

Agent

Reason

Remarks

ASDR1

A

4 (Reserved)

Agent A is selected for original call.

ASDR2

A

5 (Talking)

Agent A answers.

ASDR3

B

4 (Reserved)

Agent A
                                             					 initiates blind transfer to agent B, agent B's phone rings.

ASDR4

A

3 (Ready)

Agent A after blind transfer.

ASDR5

B

5 (Talking)

Agent B answers.

ASDR6

B

3 (Ready)

Caller hangs up.

### ACD Call Blind
                           	 Transfer to Route Point

Agent A is
                                          				connected and talking to an incoming ACD call.

Agent A
                                          				initiates a blind transfer to a route point.

Agent B
                                          				answers, Agent A moves to Ready state.

Record

Session ID

Session
                                             					 sequence number

qIndex

Remarks

CCDR

100

0

—

Contact
                                             					 and agent information.

CRDR1

100

0

1

Overall
                                             					 queue information of CSQ of incoming ICD call.

ACDR1

100

0

1

Agent A
                                             					 information.

CQDR1

100

0

1

Queue
                                             					 information.

ACDR2

100

0

0

Agent B
                                             					 information.

CQDR2

100

0

1

Queue
                                             					 information.

CRDR2

100

0

1

Overall
                                             					 queue information for CSQ after blind transfer is initiated.

Record

Agent

Reason

Remarks

ASDR1

A

4
                                             					 (Reserved)

Agent A
                                             					 is selected for original call.

ASDR2

A

5
                                             					 (Talking)

Agent A
                                             					 answers.

ASDR3

B

4
                                             					 (Reserved)

Agent A
                                             					 initiates blind transfer to agent B, agent B's phone rings.

ASDR4

A

3
                                             					 (Ready)

Agent A
                                             					 after blind transfer.

ASDR5

B

5
                                             					 (Talking)

Agent B
                                             					 answers.

ASDR6

B

3
                                             					 (Ready)

Caller
                                             					 hangs up.

### Agent Places
                           	 Consult Call and Resumes Call

Agent A is connected to an incoming ACD call.

Agent A presses the Transfer button on the phone to initiate a consult call with agent B.

Agent A receives a dial tone, drops the consult call, and resumes the incoming call.

Record

Session ID

Session sequence number

qIndex

Remarks

CCDR1

100

0

—

Original call and agent A information.

CRDR1

100

0

1

Overall queue information.

CQDR1

100

0

1

Detailed queue information for CSQ1 (targetType = 0; indicates
                                             					 CSQ-based routing).

ACDR1

100

0

1

Includes talk time both before and after the canceled consult
                                             					 call, and contains hold time for the duration of the canceled consult call.

CCDR2

101

0

—

Agent A information, no called-party information.

Record

Agent

Reason

Remarks

ASDR1

A

4 (Reserved)

Agent A is selected for original call.

ASDR2

A

5 (Talking)

Agent A answers.

ASDR3

A

3 (Ready)

Caller hangs up.

### Agent Consults
                           	 Agent and Resumes Call

Agent A is connected to an incoming ACD call.

Agent A puts that call on hold and initiates a consult transfer to agent B.

Agent B answers, talks to agent A for some time, and then hangs up without agent A completing the transfer.

Agent A resumes the original call.

Record

Session ID

Session sequence number

qIndex

Remarks

CCDR1

100

0

—

Original call and agent A information.

CRDR1

100

0

1

Overall queue information.

CQDR1

100

0

1

Detailed queue information for CSQ1 (targetType = 0; indicates
                                             					 CSQ-based routing).

CCDR2

101

0

—

Agent A to agent B.

ACDR1

100

0

1

Includes talk time both before and after the consult call, and
                                             					 contains hold time for the duration of the canceled consult call.

Record

Agent

Reason

Remarks

ASDR1

A

4 (Reserved)

Agent A is selected for original call.

ASDR2

A

5 (Talking)

Agent A answers.

ASDR3

B

4 (Reserved)

Agent A calls agent B, agent B’s phone rings.

ASDR4

B

5 (Talking)

Agent B answers.

ASDR5

B

3 (Ready)

Agent B disconnects from consult call.

ASDR6

A

3 (Ready)

Caller disconnects original call.

### Basic Outbound
                           	 Call Accepted

Call is presented to agent A, and agent A accepts the call.

System places the call from agent A to the customer.

Record

Session ID

Session sequence number

Remarks

CCDR1

100

0

—

ACDR1

100

0

Call result is 1 (voice).

Record

Reason

Remarks

ASDR1

4 (Reserved)

Agent A is presented with outbound call.

ASDR2

5 (Talking)

Agent A accepts call.

ASDR3

3 (Ready)

Call ends.

### Basic Outbound
                           	 Call Rejected and Later Accepted

Call is presented to agent A, and agent A rejects the call.

Call is then presented to agent B, and agent B accepts the call.

System places the call from agent B to the customer.

Record

Session ID

Session sequence number

Remarks

CCDR1

100

0

—

ACDR1

100

0

Call result is 9 (reject).

ACDR2

100

0

Call result is 1 (voice).

Record

Reason

Remarks

ASDR1

4 (Reserved)

Agent A is presented with outbound call.

ASDR1

3 (Ready)

Agent A rejects call.

ASDR1

4 (Reserved)

Agent B is presented with outbound call.

ASDR2

5 (Talking)

Agent B accepts call.

ASDR3

3 (Ready)

Call ends.

### Basic Outbound
                           	 Call Accepted and Transferred to Another Agent

Call is presented to agent A, and agent A accepts the call.

System places the call from agent A to the customer.

Agent A transfers the call to agent B.

Record

Session ID

Session sequence number

Remarks

CCDR1

100

0

—

ACDR1

100

0

Call result is 1 (voice).

CCDR2

200

0

Consult call from agent A to agent B information.

CCDR3

100

1

Outbound call at agent B information.

ACDR2

100

1

Call result is 20 (transfer).

Record

Reason

Remarks

ASDR1

4 (Reserved)

Agent A is presented with outbound call.

ASDR2

5 (Talking)

Agent A accepts call.

ASDR3

3 (Ready)

Agent A transfers call to agent B.

ASDR1

4 (Reserved)

Agent B is presented with outbound call.

ASDR2

5 (Talking)

Agent B on outbound call.

ASDR3

3 (Ready)

Call ends.

### Basic Outbound
                           	 Call Accepted and Transferred to Route Point

Call is presented to agent A, and agent A accepts the call.

System places the call from agent A to the customer.

Agent A transfers the call to a route point.

Call reaches a Unified CCX route point, executes a script, and queues for one CSQ.

System allocates agent B for the call and rings agent B’s phone, and agent B answers the call.

Record

Session ID

Session sequence number

qIndex

Remarks

CCDR1

100

0

—

—

ACDR1

100

0

—

Call result is 1 (voice).

CCDR2

200

0

—

Consult call from agent A to route point information.

CCDR3

100

1

—

Outbound call is queued.

CRDR1

100

1

1

Overall queue information.

CQDR1

100

1

1

Detailed queue information for CSQ1 (targetType = 0; indicates
                                             					 CSQ-based routing).

ACDR1

100

1

1

Agent B and original call information.

Record

Reason

Remarks

ASDR1

4 (Reserved)

Agent A is presented with outbound call.

ASDR2

5 (Talking)

Agent A accepts call.

ASDR3

3 (Ready)

Agent A transfers call to route point.

ASDR1

4 (Reserved)

Agent B is selected for call.

ASDR2

5 (Talking)

Agent B answers call.

ASDR3

3 (Ready)

Call ends.

## Chat
                        	 Scenarios

### Chat-Related
                           	 Detail Records Flow

The following
                                 		  table presents an example of the general flow of detail records for incoming
                                 		  chat contacts.

Chat activity

Detail record activity

Contact reaches Unified CCX

Begins TCDR in memory.

Contact is queued to a CSQ

—

Agent is allocated to the contact

Writes ASDR (Busy).

Agent answers and contact is dequeued from CSQ

Collects TCQDR in memory.

Contact disconnects

Collects TACDR, TCCDR. Writes TCCDR, TCDR, TCQDR, TACDR.

Agent leaves Work state

Writes ASDR (Ready).

If the
                                 		  contact drops before agent is connected, TCQDR is collected and written when
                                 		  the contact disconnects.

### Chat Contact
                           	 Unanswered

Contact reaches Unified CCX and queues for one or more CSQs.

System allocates agent A for the contact and offers the contact to the agent, but agent A does not answer the contact within
                                       the configured timeout period.

Call goes into queue and is presented to agent B, who answers the call.

Record

Remarks

Contact is queued to a CSQ

—

Agent is allocated to the contact

Writes ASDR (Busy).

Agent does not accept the contact

Writes ASDR (Not Ready).

Contact is requeued to CSQ

Collects TACDR1.

Contact is allocated to a different agent

Writes ASDR (Busy).

Agent answers and contact is dequeued from the CSQ

Collects TCQDR in memory.

Contact disconnects

Collects TACDR2, TCCDE. Writes TACDR1, TACDR2, TCDR, TCQDR,
                                             					 TCCDR.

Agent leaves Work state

Writes ASDR (Ready).

| Call activity | Detail record activity |
|---|---|
| Call reaches the CTI port | Allocates session. Begins CCDR in memory. |
| Call executes the first Select Resource step | Begins CRDR and CQDR in memory. |
| System selects agent and rings the phone | Begins ACDR in memory, writes ASDR to change state to Reserved. |
| Agent answers | Writes ASDR (Talking). |
| Call disconnects | Writes CRDR, CQDRs, ASDR (Work). |
| Agent leaves Work state | Writes ACDR, CCDR, ASDR (Ready). |

| Record | Session ID | Session sequence number | qIndex | Remarks |
|---|---|---|---|---|
| CCDR1 | 100 | 0 | — | — |
| CRDR1 | 100 | 0 | 1 | Overall queue information. |
| CQDR1 | 100 | 0 | 1 | Detailed queue information for CSQ1 (targetType = 0; indicates
                                             					 CSQ-based routing). |
| ACDR1 | 100 | 0 | 1 | Agent A and original call information. |

| Record | Reason | Remarks |
|---|---|---|
| ASDR1 | 4 (Reserved) | Agent A is selected for call. |
| ASDR2 | 5 (Talking) | Agent A answers call. |
| ASDR3 | 3 (Ready) | Call ends. |

| Record | Session ID | Session sequence number | qIndex | Remarks |
|---|---|---|---|---|
| CCDR1 | 100 | 0 | — | — |
| CRDR1 | 100 | 0 | 1 | Overall queue information. |
| CQDR1 | 100 | 0 | 1 | Overall queue information for CSQ1 (targetType = 0, targetID =
                                             					 ID of CSQ1). |
| CQDR2 | 100 | 0 | 1 | Overall queue information for CSQ2 (targetType = 0, targetID =
                                             					 ID of CSQ2). |
| ACDR1 | 100 | 0 | 1 | Agent A and original call information. |

| Record | Session ID | Session sequence number | qIndex | Remarks |
|---|---|---|---|---|
| CCDR1 | 100 | 0 | — | — |
| CRDR1 | 100 | 0 | 1 | Overall queue information. |
| CQDR1 | 100 | 0 | 1 | Detailed queue information for CSQ1 (targetType = 0; indicates
                                             					 CSQ-based routing). |
| ACDR1 | 100 | 0 | 1 | Agent A and original call information with wrap-up code. |

| Record | Reason | Remarks |
|---|---|---|
| ASDR1 | 4 (Reserved) | Agent A is selected for call. |
| ASDR2 | 5 (Talking) | Agent A answers call. |
| ASDR3 | 6 (Work) | Call ends. |
| ASDR4 | 3 (Ready) | Agent A goes to Ready state. |

| Record | Reason | Remarks |
|---|---|---|
| ASDR1 | 4 (Reserved) | Agent A is selected for call. |
| ASDR2 | 5 (Talking) | Agent A answers call. |
| ASDR3 | 3 (Ready) | Call ends. |

| Record | Session ID | Session sequence number | qIndex | Remarks |
|---|---|---|---|---|
| CCDR1 | 100 | 0 | — | — |
| CRDR1 | 100 | 0 | 1 | Overall queue information. |
| CQDR1 | 100 | 0 | 1 | Detailed information for the routing attempt (targetType = 1;
                                             					 indicates agent-based routing). |
| ACDR1 | 100 | 0 | 1 | Agent A and original call information. |

| Record | Reason | Remarks |
|---|---|---|
| ASDR1 | 4 (Reserved) | Agent A is selected for call. |
| ASDR2 | 5 (Talking) | Agent A answers call. |
| ASDR3 | 3 (Ready) | Call ends. |

| Record | Session ID | Session sequence number | qIndex | Remarks |
|---|---|---|---|---|
| CCDR1 | 100 | 0 | — | Transfer field will be 1. |
| CRDR1 | 100 | 0 | 1 | Overall queue information for the first segment of the call
                                             					 (before the transfer). |
| ACDR1 | 100 | 0 | 1 | Agent A and original call information. |
| CQDR1 | 100 | 0 | 1 | Detailed queue information for the CSQ that is selected by the
                                             					 first route point’s script. |
| CCDR2 | 101 | 0 | — | Consult call from agent A to route point. |
| CCDR3 | 100 | 1 | — | Second leg of original call to new route point. |
| CRDR3 | 100 | 1 | — | Overall queue information for the second segment of the call
                                             					 (after the transfer). |
| CQDR3 | 100 | 1 | 1 | Queue information for second leg of call. |
| ACDR3 | 100 | 1 | 1 | Agent B and original call information. |

| Note | The server does not create a new CCDR or CRDR after the conference is completed. An asterisk (*) indicates that another record has the same name, but the record is for a different agent. |
|---|---|

| Record | Session ID | Session sequence number | qIndex | Remarks |
|---|---|---|---|---|
| CCDR1 | 100 | 0 | — | Conference field will be 1. |
| CRDR1 | 100 | 0 | 1 | Overall queue information. |
| ACDR1 | 100 | 0 | 1 | Agent A and original call information. |
| CQDR1 | 100 | 0 | 1 | Detailed queue information for CSQ1 (targetType = 0; indicates
                                             					 CSQ-based routing). |
| CCDR2 | 101 | 0 | — | Consult call from agent A to agent B. |
| ACDR1* | 100 | 0 | 0 | Agent B and original call information. |

| Record | Session ID | Session sequence number | Remarks |
|---|---|---|---|
| CCDR1 | 100 | 0 | Caller to first route point (redirect field will be 1). |
| CCDR2 | 100 | 1 | Caller to second route point. |

| Note | An asterisk (*) indicates that another record has the same name, but the record is for a different agent. |
|---|---|

| Record | Session ID | Session sequence number | qIndex | Remarks |
|---|---|---|---|---|
| CCDR1 | 100 | 0 | — | — |
| CRDR1 | 100 | 0 | 1 | Overall queue information. |
| CQDR1 | 100 | 0 | 1 | Detailed queue information for the CSQ selected by the route
                                             					 point script. |
| ACDR1 | 100 | 0 | 1 | Agent A information, ring time > 0 and talk time = 0. |
| ACDR1* | 100 | 0 | 1 | Agent B information, talk time > 0. |

| Record | Agent | State | Reason Code | Remarks |
|---|---|---|---|---|
| ASDR1 | A | 4 (Reserved) | — | Agent A is selected for call. |
| ASDR2 | A | 2 (Not Ready) | 32763 | Server retrieves call from the agent's phone. |
| ASDR3 | B | 4 (Reserved) | — | Agent B is selected for call. |
| ASDR4 | B | 5 (Talking) | — | Agent B answers call. |

| Record | Session ID | Session sequence number | Remarks |
|---|---|---|---|
| CCDR1 | 100 | 0 | Agent A to agent B information. |

| Record | Agent | State | Reason Code | Remarks |
|---|---|---|---|---|
| ASDR1 | A | 2 (Not Ready) | 32762 | Agent A goes off-hook. |
| ASDR2 | B | 2 (Not Ready) | 32761 | Call rings at agent B’s phone. |
| ASDR3 | B | 3 (Ready) | — | Agent B hangs up. |
| ASDR4 | A | 3 (Ready) | — | — |

| Record | Session ID | Session sequence number | Remarks |
|---|---|---|---|
| CCDR1 | 100 | 0 | Unknown party to agent A information (transfer field will be 1). |
| CCDR2 | 101 | 0 | Agent A to agent B information. |
| CCDR3 | 100 | 1 | Unknown party to agent B information. |

| Record | Agent | State | Reason Code | Remarks |
|---|---|---|---|---|
| ASDR1 | A | 2 (Not Ready) | 32761 | First call rings at agent A’s phone. |
| ASDR2 | B | 2 (Not Ready) | 32761 | Consult call rings at agent B’s phone. |
| ASDR3 | A | 3 (Ready) | — | Agent A completes transfer. |
| ASDR4 | B | 3 (Ready) | — | Agent B hangs up. |

| Record | Session ID | Session sequence number | Remarks |
|---|---|---|---|
| CCDR1 | 100 | 0 | Unknown party to agent A information (conference field will be
                                             					 1). |
| CCDR2 | 101 | 0 | Agent A to agent B information. |

| Record | Agent | State | Reason Code | Remarks |
|---|---|---|---|---|
| ASDR1 | A | 2 (Not Ready) | 32761 | First call rings at agent A's phone. |
| ASDR2 | B | 2 (Not Ready) | 32761 | Consult call rings at agent B's phone. |
| ASDR3 | A | 3 (Ready) | — | Agent A hangs up. |
| ASDR4 | B | 3 (Ready) | — | Agent B hangs up. |

| Record | Session ID | Session sequence number | qIndex | Remarks |
|---|---|---|---|---|
| CCDR1 | 100 | 0 | — | Original call and agent A information (transfer
                                             					 field will be 1). |
| CRDR1 | 100 | 0 | 1 | Overall queue information. |
| ACDR1 | 100 | 0 | 1 | Agent A information. |
| CQDR1 | 100 | 0 | 1 | Queue information. |
| CCDR2 | 101 | 0 | — | Agent A and agent B information. |
| CCDR3 | 100 | 1 | — | Original call and agent B information. |
| ACDR3 | 100 | 1 | 0 | Agent B information. |

| Record | Agent | Reason | Remarks |
|---|---|---|---|
| ASDR1 | A | 4 (Reserved) | Agent A is selected for original call. |
| ASDR2 | A | 5 (Talking) | Agent A answers. |
| ASDR3 | B | 4 (Reserved) | Agent A calls agent B, agent B’s phone rings. |
| ASDR4 | A | 3 (Ready) | Agent A competes the transfer. |
| ASDR5 | B | 5 (Talking) | Agent B answers. |
| ASDR6 | B | 3 (Ready) | Caller hangs up. |

| Record | Session ID | Session sequence number | qIndex | Remarks |
|---|---|---|---|---|
| CCDR | 100 | 0 | - | Contact and agent information. |
| CRDR | 100 | 0 | 1 | Overall queue information of CSQ of incoming ICD call. |
| ACDR1 | 100 | 0 | 1 | Agent A information. |
| CQDR | 100 | 0 | 1 | Queue information. |
| ACDR2 | 100 | 0 | 0 | Agent B information. |

| Record | Agent | Reason | Remarks |
|---|---|---|---|
| ASDR1 | A | 4 (Reserved) | Agent A is selected for original call. |
| ASDR2 | A | 5 (Talking) | Agent A answers. |
| ASDR3 | B | 4 (Reserved) | Agent A
                                             					 initiates blind transfer to agent B, agent B's phone rings. |
| ASDR4 | A | 3 (Ready) | Agent A after blind transfer. |
| ASDR5 | B | 5 (Talking) | Agent B answers. |
| ASDR6 | B | 3 (Ready) | Caller hangs up. |

| Record | Session ID | Session
                                             					 sequence number | qIndex | Remarks |
|---|---|---|---|---|
| CCDR | 100 | 0 | — | Contact
                                             					 and agent information. |
| CRDR1 | 100 | 0 | 1 | Overall
                                             					 queue information of CSQ of incoming ICD call. |
| ACDR1 | 100 | 0 | 1 | Agent A
                                             					 information. |
| CQDR1 | 100 | 0 | 1 | Queue
                                             					 information. |
| ACDR2 | 100 | 0 | 0 | Agent B
                                             					 information. |
| CQDR2 | 100 | 0 | 1 | Queue
                                             					 information. |
| CRDR2 | 100 | 0 | 1 | Overall
                                             					 queue information for CSQ after blind transfer is initiated. |

| Record | Agent | Reason | Remarks |
|---|---|---|---|
| ASDR1 | A | 4
                                             					 (Reserved) | Agent A
                                             					 is selected for original call. |
| ASDR2 | A | 5
                                             					 (Talking) | Agent A
                                             					 answers. |
| ASDR3 | B | 4
                                             					 (Reserved) | Agent A
                                             					 initiates blind transfer to agent B, agent B's phone rings. |
| ASDR4 | A | 3
                                             					 (Ready) | Agent A
                                             					 after blind transfer. |
| ASDR5 | B | 5
                                             					 (Talking) | Agent B
                                             					 answers. |
| ASDR6 | B | 3
                                             					 (Ready) | Caller
                                             					 hangs up. |

| Record | Session ID | Session sequence number | qIndex | Remarks |
|---|---|---|---|---|
| CCDR1 | 100 | 0 | — | Original call and agent A information. |
| CRDR1 | 100 | 0 | 1 | Overall queue information. |
| CQDR1 | 100 | 0 | 1 | Detailed queue information for CSQ1 (targetType = 0; indicates
                                             					 CSQ-based routing). |
| ACDR1 | 100 | 0 | 1 | Includes talk time both before and after the canceled consult
                                             					 call, and contains hold time for the duration of the canceled consult call. |
| CCDR2 | 101 | 0 | — | Agent A information, no called-party information. |

| Record | Agent | Reason | Remarks |
|---|---|---|---|
| ASDR1 | A | 4 (Reserved) | Agent A is selected for original call. |
| ASDR2 | A | 5 (Talking) | Agent A answers. |
| ASDR3 | A | 3 (Ready) | Caller hangs up. |

| Record | Session ID | Session sequence number | qIndex | Remarks |
|---|---|---|---|---|
| CCDR1 | 100 | 0 | — | Original call and agent A information. |
| CRDR1 | 100 | 0 | 1 | Overall queue information. |
| CQDR1 | 100 | 0 | 1 | Detailed queue information for CSQ1 (targetType = 0; indicates
                                             					 CSQ-based routing). |
| CCDR2 | 101 | 0 | — | Agent A to agent B. |
| ACDR1 | 100 | 0 | 1 | Includes talk time both before and after the consult call, and
                                             					 contains hold time for the duration of the canceled consult call. |

| Record | Agent | Reason | Remarks |
|---|---|---|---|
| ASDR1 | A | 4 (Reserved) | Agent A is selected for original call. |
| ASDR2 | A | 5 (Talking) | Agent A answers. |
| ASDR3 | B | 4 (Reserved) | Agent A calls agent B, agent B’s phone rings. |
| ASDR4 | B | 5 (Talking) | Agent B answers. |
| ASDR5 | B | 3 (Ready) | Agent B disconnects from consult call. |
| ASDR6 | A | 3 (Ready) | Caller disconnects original call. |

| Record | Session ID | Session sequence number | Remarks |
|---|---|---|---|
| CCDR1 | 100 | 0 | — |
| ACDR1 | 100 | 0 | Call result is 1 (voice). |

| Record | Reason | Remarks |
|---|---|---|
| ASDR1 | 4 (Reserved) | Agent A is presented with outbound call. |
| ASDR2 | 5 (Talking) | Agent A accepts call. |
| ASDR3 | 3 (Ready) | Call ends. |

| Record | Session ID | Session sequence number | Remarks |
|---|---|---|---|
| CCDR1 | 100 | 0 | — |
| ACDR1 | 100 | 0 | Call result is 9 (reject). |
| ACDR2 | 100 | 0 | Call result is 1 (voice). |

| Record | Reason | Remarks |
|---|---|---|
| ASDR1 | 4 (Reserved) | Agent A is presented with outbound call. |
| ASDR1 | 3 (Ready) | Agent A rejects call. |
| ASDR1 | 4 (Reserved) | Agent B is presented with outbound call. |
| ASDR2 | 5 (Talking) | Agent B accepts call. |
| ASDR3 | 3 (Ready) | Call ends. |

| Record | Session ID | Session sequence number | Remarks |
|---|---|---|---|
| CCDR1 | 100 | 0 | — |
| ACDR1 | 100 | 0 | Call result is 1 (voice). |
| CCDR2 | 200 | 0 | Consult call from agent A to agent B information. |
| CCDR3 | 100 | 1 | Outbound call at agent B information. |
| ACDR2 | 100 | 1 | Call result is 20 (transfer). |

| Record | Reason | Remarks |
|---|---|---|
| ASDR1 | 4 (Reserved) | Agent A is presented with outbound call. |
| ASDR2 | 5 (Talking) | Agent A accepts call. |
| ASDR3 | 3 (Ready) | Agent A transfers call to agent B. |
| ASDR1 | 4 (Reserved) | Agent B is presented with outbound call. |
| ASDR2 | 5 (Talking) | Agent B on outbound call. |
| ASDR3 | 3 (Ready) | Call ends. |

| Record | Session ID | Session sequence number | qIndex | Remarks |
|---|---|---|---|---|
| CCDR1 | 100 | 0 | — | — |
| ACDR1 | 100 | 0 | — | Call result is 1 (voice). |
| CCDR2 | 200 | 0 | — | Consult call from agent A to route point information. |
| CCDR3 | 100 | 1 | — | Outbound call is queued. |
| CRDR1 | 100 | 1 | 1 | Overall queue information. |
| CQDR1 | 100 | 1 | 1 | Detailed queue information for CSQ1 (targetType = 0; indicates
                                             					 CSQ-based routing). |
| ACDR1 | 100 | 1 | 1 | Agent B and original call information. |

| Record | Reason | Remarks |
|---|---|---|
| ASDR1 | 4 (Reserved) | Agent A is presented with outbound call. |
| ASDR2 | 5 (Talking) | Agent A accepts call. |
| ASDR3 | 3 (Ready) | Agent A transfers call to route point. |
| ASDR1 | 4 (Reserved) | Agent B is selected for call. |
| ASDR2 | 5 (Talking) | Agent B answers call. |
| ASDR3 | 3 (Ready) | Call ends. |

| Chat activity | Detail record activity |
|---|---|
| Contact reaches Unified CCX | Begins TCDR in memory. |
| Contact is queued to a CSQ | — |
| Agent is allocated to the contact | Writes ASDR (Busy). |
| Agent answers and contact is dequeued from CSQ | Collects TCQDR in memory. |
| Contact disconnects | Collects TACDR, TCCDR. Writes TCCDR, TCDR, TCQDR, TACDR. |
| Agent leaves Work state | Writes ASDR (Ready). |

| Record | Remarks |
|---|---|
| Contact is queued to a CSQ | — |
| Agent is allocated to the contact | Writes ASDR (Busy). |
| Agent does not accept the contact | Writes ASDR (Not Ready). |
| Contact is requeued to CSQ | Collects TACDR1. |
| Contact is allocated to a different agent | Writes ASDR (Busy). |
| Agent answers and contact is dequeued from the CSQ | Collects TCQDR in memory. |
| Contact disconnects | Collects TACDR2, TCCDE. Writes TACDR1, TACDR2, TCDR, TCQDR,
                                             					 TCCDR. |
| Agent leaves Work state | Writes ASDR (Ready). |