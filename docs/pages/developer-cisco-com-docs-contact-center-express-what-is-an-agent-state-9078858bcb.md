---
doc_id: developer-cisco-com-docs-contact-center-express-what-is-an-agent-state-9078858bcb
source_url: https://developer.cisco.com/docs/contact-center-express/what-is-an-agent-state/
retrieved_at: 2026-09-07T14:05:36.733941+00:00
---

# What is an Agent State?

An agent is a person who has a phone on his desktop and
		  receives calls, transfers calls, ends calls, and so on. The state of this agent
		  and his phone are represented within the Unified CCX system by agent states and
		  agent state events.

The agent state is what is described by the last received
		  agent state event. Actions performed by the agent and his phone eventually
		  translate into updated agent states. For example, when an agent hangs up his
		  phone after working on a call, his state changes from talking to ready. The
		  change in the state of this agent is communicated with the system through the
		  AGENT_STATE_EVENT message.

The possible agent states are listed in Table 1 .
		  The AGENT_STATE_EVENT, the QUERY_AGENT_STATE_CONF, and the SET_AGENT_STATE_REQ
		  messages indicate an agent state by the values listed in Table 1 .

CCX maintains all agent states and may change an agent state
		  based on various conditions such as the state of an agent phone.

Unified CCX CTI clients are also allowed to change agent
		  states by a client using the SET_AGENT_STATE_REQ message. When Unified CCX
		  receives this request, it processes the request based on the current state of
		  the system. As a result, the SET_AGENT_STATE_REQ message may or may not
		  actually change the agent state. For example, the client might request that an
		  agent’s state be changed from not ready to ready, but Unified CCX may not be
		  able to change the agent’s state if the agent has not yet logged in.

A Unified CCX CTI client must always monitor the
		  AGENT_STATE_EVENT message or use the QUERY_AGENT_STATE_REQ message to obtain
		  the current agent state.

State name

Description

Value

AGENT_STATE_LOGIN

There is no specific Agent Login state in Unified
					 CCX.

However, this is a request value specified while
					 trying to login an agent.

0

AGENT_STATE_LOGOUT

The agent has logged out of the ACD and cannot accept
					 any additional calls.

1

AGENT_STATE_NOT_READY

The agent is not available to accept a routed call.

2

AGENT_STATE_READY

The agent is available to accept a routed call.

3

AGENT_STATE_TALKING

The agent is currently talking on a call with a
					 customer or another agent (inbound, outbound, or inside).

This state is automatically set for the agent by the
					 ACD.

4

AGENT_STATE_WORK

The agent is completing work from a previous call and
					 is unavailable to receive routed calls.

There are two (mutually exclusive) ways to put an
					 agent into AGENT_STATE_WORK:

- Automatically,
						through CSQ configuration settings selected in the Unified CCX Administration
						web page.

- Through the
						SET_AGENT_STATE_REQ message. In this case, when the agent is in the
						AGENT_STATE_TALKING state, the client can select the work state (by setting the
						AgentState field to AGENT_STATE_WORK). Then when the call ends, the agent will
						be moved by the Unified CCX server to the Work state.

5

BUSY_OTHER

This state signifies the agent state for a particular
					 CSQ. This state is notified in the CSQ State field of QUERY_AGENT_STATE_CONF
					 message only. The state of an agent for a CSQ will be BUSY_OTHER if that agent
					 is handling calls from other CSQs.

7

AGENT_STATE_RESERVED

The agent is reserved for a call that will arrive at
					 the ACD shortly.

The agent is temporarily set aside to receive a
					 specific call. The agent’s state is changed to the Talking state when the agent
					 answers the call.

If the agent fails to answer the call within a time
					 limit specified by the system administrator, the ACD places the agent in a Not
					 Ready state.

The Reserved state is automatically set for the agent
					 by the ACD. The agent can be in this state without the phone ringing (if the
					 agent is waiting for it to ring).

8

AGENT_STATE_UNKNOWN

The associated agent state is unknown.

9

State name

Description

Value

AGENT_STATE_LOGIN

There is no specific Agent Login state in Unified
					 CCX.

However, this is a request value specified while
					 trying to login an agent.

0

AGENT_STATE_LOGOUT

The agent has logged out of the ACD and cannot accept
					 any additional calls.

1

AGENT_STATE_NOT_READY

The agent is not available to accept a routed call.

2

AGENT_STATE_READY

The agent is available to accept a routed call.

3

AGENT_STATE_TALKING

The agent is currently talking on a call with a
					 customer or another agent (inbound, outbound, or inside).

This state is automatically set for the agent by the
					 ACD.

4

AGENT_STATE_WORK

The agent is completing work from a previous call and
					 is unavailable to receive routed calls.

There are two (mutually exclusive) ways to put an
					 agent into AGENT_STATE_WORK:

- Automatically,
						through CSQ configuration settings selected in the Unified CCX Administration
						web page.

- Through the
						SET_AGENT_STATE_REQ message. In this case, when the agent is in the
						AGENT_STATE_TALKING state, the client can select the work state (by setting the
						AgentState field to AGENT_STATE_WORK). Then when the call ends, the agent will
						be moved by the Unified CCX server to the Work state.

5

AGENT_STATE_ WORK_ READY

The agent is performing after call work, and will be ready to receive a call when completed.

6

BUSY_OTHER

This state signifies the agent state for a particular
					 CSQ. This state is notified in the CSQ State field of QUERY_AGENT_STATE_CONF
					 message only. The state of an agent for a CSQ will be BUSY_OTHER if that agent
					 is handling calls from other CSQs.

7

AGENT_STATE_ACTIVE

The agent state is currently active.

11

AGENT_STATE_PAUSED

The agent state is currently paused.

12

| State name | Description | Value |
|---|---|---|
| AGENT_STATE_LOGIN | There is no specific Agent Login state in Unified
					 CCX. However, this is a request value specified while
					 trying to login an agent. | 0 |
| AGENT_STATE_LOGOUT | The agent has logged out of the ACD and cannot accept
					 any additional calls. | 1 |
| AGENT_STATE_NOT_READY | The agent is not available to accept a routed call. | 2 |
| AGENT_STATE_READY | The agent is available to accept a routed call. | 3 |
| AGENT_STATE_TALKING | The agent is currently talking on a call with a
					 customer or another agent (inbound, outbound, or inside). This state is automatically set for the agent by the
					 ACD. | 4 |
| AGENT_STATE_WORK | The agent is completing work from a previous call and
					 is unavailable to receive routed calls. There are two (mutually exclusive) ways to put an
					 agent into AGENT_STATE_WORK: Automatically,
						through CSQ configuration settings selected in the Unified CCX Administration
						web page. Through the
						SET_AGENT_STATE_REQ message. In this case, when the agent is in the
						AGENT_STATE_TALKING state, the client can select the work state (by setting the
						AgentState field to AGENT_STATE_WORK). Then when the call ends, the agent will
						be moved by the Unified CCX server to the Work state. | 5 |
| BUSY_OTHER | This state signifies the agent state for a particular
					 CSQ. This state is notified in the CSQ State field of QUERY_AGENT_STATE_CONF
					 message only. The state of an agent for a CSQ will be BUSY_OTHER if that agent
					 is handling calls from other CSQs. | 7 |
| AGENT_STATE_RESERVED | The agent is reserved for a call that will arrive at
					 the ACD shortly. The agent is temporarily set aside to receive a
					 specific call. The agent’s state is changed to the Talking state when the agent
					 answers the call. If the agent fails to answer the call within a time
					 limit specified by the system administrator, the ACD places the agent in a Not
					 Ready state. The Reserved state is automatically set for the agent
					 by the ACD. The agent can be in this state without the phone ringing (if the
					 agent is waiting for it to ring). | 8 |
| AGENT_STATE_UNKNOWN | The associated agent state is unknown. | 9 |

| State name | Description | Value |
|---|---|---|
| AGENT_STATE_LOGIN | There is no specific Agent Login state in Unified
					 CCX. However, this is a request value specified while
					 trying to login an agent. | 0 |
| AGENT_STATE_LOGOUT | The agent has logged out of the ACD and cannot accept
					 any additional calls. | 1 |
| AGENT_STATE_NOT_READY | The agent is not available to accept a routed call. | 2 |
| AGENT_STATE_READY | The agent is available to accept a routed call. | 3 |
| AGENT_STATE_TALKING | The agent is currently talking on a call with a
					 customer or another agent (inbound, outbound, or inside). This state is automatically set for the agent by the
					 ACD. | 4 |
| AGENT_STATE_WORK | The agent is completing work from a previous call and
					 is unavailable to receive routed calls. There are two (mutually exclusive) ways to put an
					 agent into AGENT_STATE_WORK: Automatically,
						through CSQ configuration settings selected in the Unified CCX Administration
						web page. Through the
						SET_AGENT_STATE_REQ message. In this case, when the agent is in the
						AGENT_STATE_TALKING state, the client can select the work state (by setting the
						AgentState field to AGENT_STATE_WORK). Then when the call ends, the agent will
						be moved by the Unified CCX server to the Work state. | 5 |
| AGENT_STATE_ WORK_ READY | The agent is performing after call work, and will be ready to receive a call when completed. | 6 |
| BUSY_OTHER | This state signifies the agent state for a particular
					 CSQ. This state is notified in the CSQ State field of QUERY_AGENT_STATE_CONF
					 message only. The state of an agent for a CSQ will be BUSY_OTHER if that agent
					 is handling calls from other CSQs. | 7 |
| AGENT_STATE_ACTIVE | The agent state is currently active. | 11 |
| AGENT_STATE_PAUSED | The agent state is currently paused. | 12 |