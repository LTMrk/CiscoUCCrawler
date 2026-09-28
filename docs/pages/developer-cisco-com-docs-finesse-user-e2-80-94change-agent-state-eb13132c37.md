---
doc_id: developer-cisco-com-docs-finesse-user-e2-80-94change-agent-state-eb13132c37
source_url: https://developer.cisco.com/docs/finesse/user%e2%80%94change-agent-state/
retrieved_at: 2026-09-07T14:07:23.726483+00:00
---

# User—Change Agent
	 State

This API allows a
		  user to change the state of an agent on the CTI server. Agents can change their
		  own states

To
			 change user state in a nonvoice Media Routing Domain, see Media—Change State or Sign Out .

If the request to
		  change an agent's state is successful, the response is sent as part of a User
		  notification.

The following
		  figure illustrates the supported state transitions by Unified CCE agents.

The following
			 diagram contains only logical state transitions. Because the underlying system
			 determines the state, an agent can transition from any state to any state,
			 especially under failover conditions. The diagram describes the typical state
			 changes that occur in the system.

In the preceding
			 diagram, RESERVED_OUTBOUND can represent RESERVED_OUTBOUND or
			 RESERVED_OUTBOUND_PREVIEW state.

The following
		  table describes supported agent state transitions for Unified CCE.

From

To

Description

*

UNKNOWN

If the
						agent state is unknown, the state is UNKNOWN. This scenario is unlikely.

LOGOUT

LOGIN

To sign
						in to Finesse, the agent sets the state to LOGIN. LOGIN is a transient state
						and transitions to NOT_READY.

LOGIN

NOT_READY

After a
						successful LOGIN, the agent transitions to NOT_READY.

NOT_READY

LOGOUT

To sign
						out of Finesse, the agent sets the state to LOGOUT. An agent can set the state
						to LOGOUT only if that agent is in NOT_READY state.

NOT_READY

NOT_READY

To
						change their Not Ready reason code, agents can set a NOT_READY state from
						NOT_READY.

NOT_READY

READY

To
						become available for incoming or Outbound Option calls, agents set their state
						to READY.

NOT_READY

TALKING

An agent
						who places a call while in NOT_READY state transitions to TALKING.

READY

RESERVED

An
						incoming call arrives at an agent.

READY

RESERVED
						_OUTBOUND

An
						outbound agent becomes reserved to handle an Outbound Option Progressive or
						Predictive call.

READY

RESERVED_OUTBOUND _PREVIEW

An
						outbound agent becomes reserved to handle an Outbound Option Preview call.

READY

NOT_READY

Agents
						can change to NOT_READY to make themselves unavailable for incoming calls.

RESERVED

READY

An
						agent can become RESERVED but never take a call.

RESERVED

TALKING

When
						an agent answers an incoming call, the agent transitions to TALKING.

RESERVED _OUTBOUND

READY

An
						agent can change to READY state to leave RESERVED_OUTBOUND. If the system deems
						it necessary, that agent may transition back to RESERVED_OUTBOUND.

RESERVED _OUTBOUND

NOT_READY

An
						agent can change to NOT_READY state to leave RESERVED_OUTBOUND.

RESERVED _OUTBOUND

TALKING

An
						agent transitions to TALKING when an Outbound Option call arrives at the agent.

RESERVED_OUTBOUND _PREVIEW

READY

An
						agent transitions to READY if the agent was in READY state before being
						reserved in an Outbound Option Preview campaign.

RESERVED_OUTBOUND _PREVIEW

NOT_READY

An
						agent transitions to NOT_READY if that agent changes state to NOT_READY while
						reserved in an Outbound Option Preview campaign. This state change is a pending
						state change. The agent does not transition to NOT_READY until the call is
						complete or the Outbound Option Preview reservation is closed or rejected.

RESERVED_OUTBOUND _PREVIEW

TALKING

An
						agent transitions to TALKING when an Outbound Option call arrives at the agent.

TALKING

READY

If an
						agent is on a call that is dropped, the agent transitions to READY (if the
						agent was in READY state before the call).

TALKING

NOT_READY

If an
						agent is on a call that is dropped, the agent transitions to NOT_READY if that
						agent was in NOT_READY state before the call.

TALKING

WORK

If
						wrap-up is enabled, and the agent chooses NOT_READY while on a call, that agent
						enters WORK state after the call is dropped.

TALKING

WORK_READY

If
						wrap-up is enabled, an agent enters WORK_READY state after a call is dropped.

TALKING

HOLD

An
						agent puts a call on hold and transitions to HOLD state.

HOLD

READY

If an
						agent is connected to a held call and the call is dropped, the agent
						transitions to READY state (if the agent was in READY state before the call).

HOLD

NOT_READY

If an
						agent is connected to a held call and the call is dropped, the agent
						transitions to NOT_READY state (if the agent was in NOT_READY state before the
						call).

HOLD

WORK

If
						wrap-up is enabled and an agent is connected to a held call that is dropped,
						the agent transitions to WORK state if the agent chose to go NOT_READY during
						the call.

HOLD

WORK_READY

If
						wrap-up is enabled and an agent is connected to a held call that is dropped,
						the agent transitions to WORK_READY state.

HOLD

TALKING

When
						an agent retrieves a held call, the agent transitions to TALKING state.

WORK

READY

To
						leave WORK state, agents can set their state to READY.

WORK

NOT_READY

To
						leave WORK state, agents can set their state to NOT_READY. Agents automatically
						transition to NOT_READY after the wrap-up timer expires.

WORK_READY

READY

To
						leave WORK_READY state, agents can set their state to READY. Agents
						automatically transition to READY after the wrap-up timer expires.

WORK_READY

NOT_READY

To
						leave WORK_READY state, agents can set their state to NOT_READY.

The following
		  table describes supported agent state transitions for Unified CCX.

From

To

Description

LOGIN

NOT_READY

After
						a successful LOGIN, the agent transitions to NOT_READY.

NOT_READY

LOGOUT

To
						sign out of Finesse, the agent sets the state to LOGOUT.

NOT_READY

NOT_READY

To
						change their Not Ready reason code, agents can set a NOT_READY state from
						NOT_READY.

NOT_READY

READY

To
						become available for incoming calls, agents set their state to READY.

READY

NOT_READY

Agents
						can change their state to NOT_READY to make themselves unavailable for incoming
						calls.

READY

LOGOUT

To
						sign out of Finesse, agents set their state to LOGOUT.

READY

RESERVED_

OUTBOUND_

PREVIEW

An
						outbound agent becomes reserved to handle an Outbound Option Direct Preview
						call.

RESERVED_

OUTBOUND_

PREVIEW

TALKING

An
						outbound agent accepts a direct preview call and the call is active.

Users can set
		  the following states with this API:

READY

NOT_READY

LOGOUT

The LOGIN state
		  is a transitive state. That is, when set, LOGIN triggers a change that results
		  in a new state.

Users can be in
		  the following states while on a call. However, users cannot place themselves in
		  these states. For example, agents cannot change their state to TALKING. Agents
		  enter TALKING state when they answer a call.

RESERVED

RESERVED_OUTBOUND

RESERVED_OUTBOUND_PREVIEW

TALKING

HOLD

WORK

WORK_READY

RESERVED_OUTBOUND user
			 state:

Users who belong
		  to Outbound Option skill groups transition from READY state to
		  RESERVED_OUTBOUND state when those users are reserved for Progressive or
		  Predictive Outbound Option calls.

In a Unified CCE
		  deployment, users can change their state to READY or NOT_READY to exit this
		  state. If not ready reason codes are configured, users must specify a reason
		  code to transition to NOT_READY state. If the user does nothing and then the
		  call is transferred to the user, the user transitions to TALKING state. If the
		  call is not transferred to the user, the user transitions back to READY state.

In a Unified CCX
		  deployment, users cannot change their state to exit RESERVED_OUTBOUND state. If
		  auto-answer for the predictive or progressive call is not enabled and the agent
		  does not answer the call, the agent transitions to NOT_READY state. If the call
		  does not reach a voice contact or if the reservation timer on Unified CCX
		  expires, the agent transitions to READY state.

RESERVED_OUTBOUND_PREVIEW
			 user state:

Users who belong
		  to Outbound Option skill groups transition from READY state to
		  RESERVED_OUTBOUND_PREVIEW state when they are reserved for Outbound Option
		  Preview or Direct Preview calls. Users cannot set their state to
		  RESERVED_OUTBOUND_PREVIEW.

In a Unified CCE
		  deployment, users can click Close or Reject on the Outbound Option dialog.
		  Changing the user's state to READY or NOT_READY does not generate a state
		  change notification but does affect the user state when the call is complete.
		  For example, if the user selects NOT_READY state while in
		  RESERVED_OUTBOUND_PREVIEW state, the user transitions to NOT_READY state after
		  clicking Close or Reject.

In a Unified CCX
		  deployment, users cannot change their state directly when in
		  RESERVED_OUTBOUND_PREVIEW state. The state can only be changed by issuing a
		  Dialog Accept, Close, or Reject request or when the reservation call times out.

WORK and WORK_READY user
			 states:

A user is in
		  WORK or WORK_READY state during wrap-up. A user is placed in WORK state when
		  the user is set to transition to NOT_READY state when wrap-up ends. A user is
		  in WORK_READY state when the user is set to transition to READY state when
		  wrap-up ends.

A user
		  transitions to WORK state for the following reasons:

The user was
				in NOT_READY state before taking a call.

The user set
				a state of NOT_READY while in TALKING state.

When the wrap-up
		  timer expires, the user transitions to NOT_READY state.

WORK_READY state
		  applies only to Unified CCE deployments. A user transitions to WORK_READY state
		  for the following reasons:

The user was
				in READY state before taking a call.

The user set
				a state of READY while in TALKING state.

When the wrap-up
		  timer expires, the user transitions to READY state.

The following
			 statements apply to a supervisor using this API to change the state of an agent
			 or other supervisor:

A
				  supervisor can only change the state of a user who is assigned to that
				  supervisor's team.

A
				  supervisor can only set the state of another user to NOT_READY, READY, or
				  LOGOUT.

A
				  supervisor can set the state of a user to LOGOUT only if that user is in READY,
				  NOT_READY, RESERVED, RESERVED_OUTBOUND, RESERVED_OUTBOUND_PREVIEW, TALKING,
				  HOLD, WORK, or WORK_READY state.

A
				  supervisor can set the state of a user to NOT_READY only if that user is in
				  READY, WORK, or WORK_READY state.

When a
				  supervisor uses this API to set the state of a user to NOT_READY, a reason code
				  must not be used. If a reason code is provided, Finesse rejects it and returns
				  a 400 Invalid Input error. Finesse sends a hard-coded reason code to indicate
				  that the state change was performed by the supervisor.

URI:

https ://<FQDN>/finesse/api/User/<id>

Example URI:

https ://finesse1.xyz.com/finesse/api/User/1234

Security Constraints:

Agents
						can only act on their own User objects. Supervisors can act on the User objects
						of agents who belong to their team.

HTTP Method:

PUT

Content Type:

Application/XML

Input/Output Format:

XML

HTTP Request:

Code Snippet

```
< User > < state > READY </ state > </ User >
```

Request Parameters:

id
						(required): The ID of the user

state
						(required): The new state the user wants to be in (for example, LOGOUT, READY,
						NOT_READY)

HTTP Response:

200:
						Success

400:
						Bad Request

401:
						Invalid Supervisor

401:
						Unauthorized

404:
						Not Found

500:
						Internal Server Error

503:
						Service Unavailable

Example Failure
						  Response:

Code Snippet

```
< ApiErrors > < ApiError > < ErrorType > Parameter Missing </ ErrorType > < ErrorData > state </ ErrorData > < ErrorMessage > State Parameter missing </ ErrorMessage > </ ApiError > </ ApiErrors >
```

Notifications
						  Triggered:

User
						notification

## Platform-Based API Differences

The following
		  table describes API differences between a stand-alone Finesse deployment with
		  Unified CCE and a coresident Finesse deployment with Unified CCX.

Scenario

Response

Change
						from LOGOUT to NOT_READY.

Code Snippet

```
< data > < apiErrors > < apiError > < errorData > 257 </ errorData > < errorMessage > CF_INVALID_PASSWORD_SPECIFIED </ errorMessage > < errorType > Invalid State </ errorType > </ apiError > </ apiErrors > </ data >
```

Code Snippet

```
< data > < apiErrors > < apiError > < errorData > 1010 </ errorData > < errorMessage > CF_INVALID_PARAMETER </ errorMessage > < errorType > Invalid State </ errorType > </ apiError > </ apiErrors > </ data >
```

Agent
						receives and answers a non-ICD call.

Stand-alone Finesse with
						  Unified CCE:

Finesse sends a User notification with state=TALKING.

Coresident Finesse with
						  Unified CCX:

Finesse does not send a User notification. The agent remains in
						NOT_READY state.

Agent
						puts an ICD call on hold.

Stand-alone Finesse with
						  Unified CCE:

Finesse sends a User notification with state=HOLD.

Coresident Finesse with
						  Unified CCX:

Finesse does not send a User notification. The agent remains in
						TALKING state.

While
						talking on an ICD call, the agent sets a pending state of READY.

Stand-alone Finesse with
						  Unified CCE:

Agent
						transitions to READY state after the call ends.

Coresident Finesse with
						  Unified CCX:

Unified CCX does not allow an agent to set a pending state of
						READY while that agent is talking on an ICD call.

Code Snippet

```
< data > < apiErrors > < apiError > < errorData > 265 </ errorData > < errorMessage > CF_INVALID_AGENT_WORKMODE </ errorMessage > < errorType > Invalid State </ errorType > </ apiError > </ apiErrors > </ data >
```

While
						talking on a non-ICD call (agent state can be TALKING in Unified CCE or
						NOT_READY in Unified CCX), the agent sets a pending state of READY.

Stand-alone Finesse with
						  Unified CCE:

Agent
						transitions to READY state after the call ends.

Coresident Finesse with
						  Unified CCX:

Unified CCX does not allow an agent to set a pending state of
						READY while that agent is talking on a non-ICD call.

Code Snippet

```
< data > < apiErrors > < apiError > < errorData > 33 </ errorData > < errorMessage > CF_RESOURCE_BUSY </ errorMessage > < errorType > Invalid State </ errorType > </ apiError > </ apiErrors > </ data >
```

While
						talking on an ICD call, the agent attempts to change from a pending state of
						NOT_READY with reason code 1 to a pending state of NOT_READY with reason code
						2.

Stand-alone Finesse with
						  Unified CCE:

Agent
						transitions to NOT_READY state with reason code 2 after the call ends.

Coresident Finesse with
						  Unified CCX:

Unified CCX allows an agent to set a pending state of NOT_READY
						only once during a call. Unified CCX does not allow an agent to change from one
						Not Ready reason code to another.

Code Snippet

```
< data > < apiErrors > < apiError > < errorData > 265 </ errorData > < errorMessage > CF_INVALID_AGENT_WORKMODE </ errorMessage > < errorType > Invalid State </ errorType > </ apiError > </ apiErrors > </ data >
```

A
						supervisor changes the state of an agent on that supervisor's team to
						NOT_READY.

Stand-alone Finesse with
						  Unified CCE:

Finesse sends a hard-coded reason code of 999 to indicate the
						forced state change.

Coresident Finesse with
						  Unified CCX:

Finesse sends a hard-coded reason code of 33 to indicate the
						forced state change.

## Asynchronous
		  Errors

When accessing
			 the Finesse REST API through the Finesse JavaScript library, asynchronous
			 errors have a status code of 400. When receiving the asynchronous error
			 directly through XMPP, the error message has the format described in "Dialog
			 CTI Error Notification."

Invalid State

Invalid state transition requested.

For
						example, attempt to set Wrap-Up state on an agent that is not allowed to go to
						Wrap-Up, or attempt to change an agent's state from READY state to Wrap-up or
						WORK state.

All

Internal Server Error

Attempt to change an agent's state from RESERVED_OUTBOUND to any
						other state.

Unified CCX

| Note | To
			 change user state in a nonvoice Media Routing Domain, see Media—Change State or Sign Out . |
|---|---|

| Note | The following
			 diagram contains only logical state transitions. Because the underlying system
			 determines the state, an agent can transition from any state to any state,
			 especially under failover conditions. The diagram describes the typical state
			 changes that occur in the system. |
|---|---|

| Note | In the preceding
			 diagram, RESERVED_OUTBOUND can represent RESERVED_OUTBOUND or
			 RESERVED_OUTBOUND_PREVIEW state. |
|---|---|

| From | To | Description |
|---|---|---|
| * | UNKNOWN | If the
						agent state is unknown, the state is UNKNOWN. This scenario is unlikely. |
| LOGOUT | LOGIN | To sign
						in to Finesse, the agent sets the state to LOGIN. LOGIN is a transient state
						and transitions to NOT_READY. |
| LOGIN | NOT_READY | After a
						successful LOGIN, the agent transitions to NOT_READY. |
| NOT_READY | LOGOUT | To sign
						out of Finesse, the agent sets the state to LOGOUT. An agent can set the state
						to LOGOUT only if that agent is in NOT_READY state. |
| NOT_READY | NOT_READY | To
						change their Not Ready reason code, agents can set a NOT_READY state from
						NOT_READY. |
| NOT_READY | READY | To
						become available for incoming or Outbound Option calls, agents set their state
						to READY. |
| NOT_READY | TALKING | An agent
						who places a call while in NOT_READY state transitions to TALKING. |
| READY | RESERVED | An
						incoming call arrives at an agent. |
| READY | RESERVED
						_OUTBOUND | An
						outbound agent becomes reserved to handle an Outbound Option Progressive or
						Predictive call. |
| READY | RESERVED_OUTBOUND _PREVIEW | An
						outbound agent becomes reserved to handle an Outbound Option Preview call. |
| READY | NOT_READY | Agents
						can change to NOT_READY to make themselves unavailable for incoming calls. |
| RESERVED | READY | An
						agent can become RESERVED but never take a call. |
| RESERVED | TALKING | When
						an agent answers an incoming call, the agent transitions to TALKING. |
| RESERVED _OUTBOUND | READY | An
						agent can change to READY state to leave RESERVED_OUTBOUND. If the system deems
						it necessary, that agent may transition back to RESERVED_OUTBOUND. |
| RESERVED _OUTBOUND | NOT_READY | An
						agent can change to NOT_READY state to leave RESERVED_OUTBOUND. |
| RESERVED _OUTBOUND | TALKING | An
						agent transitions to TALKING when an Outbound Option call arrives at the agent. |
| RESERVED_OUTBOUND _PREVIEW | READY | An
						agent transitions to READY if the agent was in READY state before being
						reserved in an Outbound Option Preview campaign. |
| RESERVED_OUTBOUND _PREVIEW | NOT_READY | An
						agent transitions to NOT_READY if that agent changes state to NOT_READY while
						reserved in an Outbound Option Preview campaign. This state change is a pending
						state change. The agent does not transition to NOT_READY until the call is
						complete or the Outbound Option Preview reservation is closed or rejected. |
| RESERVED_OUTBOUND _PREVIEW | TALKING | An
						agent transitions to TALKING when an Outbound Option call arrives at the agent. |
| TALKING | READY | If an
						agent is on a call that is dropped, the agent transitions to READY (if the
						agent was in READY state before the call). |
| TALKING | NOT_READY | If an
						agent is on a call that is dropped, the agent transitions to NOT_READY if that
						agent was in NOT_READY state before the call. |
| TALKING | WORK | If
						wrap-up is enabled, and the agent chooses NOT_READY while on a call, that agent
						enters WORK state after the call is dropped. |
| TALKING | WORK_READY | If
						wrap-up is enabled, an agent enters WORK_READY state after a call is dropped. |
| TALKING | HOLD | An
						agent puts a call on hold and transitions to HOLD state. |
| HOLD | READY | If an
						agent is connected to a held call and the call is dropped, the agent
						transitions to READY state (if the agent was in READY state before the call). |
| HOLD | NOT_READY | If an
						agent is connected to a held call and the call is dropped, the agent
						transitions to NOT_READY state (if the agent was in NOT_READY state before the
						call). |
| HOLD | WORK | If
						wrap-up is enabled and an agent is connected to a held call that is dropped,
						the agent transitions to WORK state if the agent chose to go NOT_READY during
						the call. |
| HOLD | WORK_READY | If
						wrap-up is enabled and an agent is connected to a held call that is dropped,
						the agent transitions to WORK_READY state. |
| HOLD | TALKING | When
						an agent retrieves a held call, the agent transitions to TALKING state. |
| WORK | READY | To
						leave WORK state, agents can set their state to READY. |
| WORK | NOT_READY | To
						leave WORK state, agents can set their state to NOT_READY. Agents automatically
						transition to NOT_READY after the wrap-up timer expires. |
| WORK_READY | READY | To
						leave WORK_READY state, agents can set their state to READY. Agents
						automatically transition to READY after the wrap-up timer expires. |
| WORK_READY | NOT_READY | To
						leave WORK_READY state, agents can set their state to NOT_READY. |

| From | To | Description |
|---|---|---|
| LOGIN | NOT_READY | After
						a successful LOGIN, the agent transitions to NOT_READY. |
| NOT_READY | LOGOUT | To
						sign out of Finesse, the agent sets the state to LOGOUT. |
| NOT_READY | NOT_READY | To
						change their Not Ready reason code, agents can set a NOT_READY state from
						NOT_READY. |
| NOT_READY | READY | To
						become available for incoming calls, agents set their state to READY. |
| READY | NOT_READY | Agents
						can change their state to NOT_READY to make themselves unavailable for incoming
						calls. |
| READY | LOGOUT | To
						sign out of Finesse, agents set their state to LOGOUT. |
| READY | RESERVED_ OUTBOUND_ PREVIEW | An
						outbound agent becomes reserved to handle an Outbound Option Direct Preview
						call. |
| RESERVED_ OUTBOUND_ PREVIEW | TALKING | An
						outbound agent accepts a direct preview call and the call is active. |

| Note | The following
			 statements apply to a supervisor using this API to change the state of an agent
			 or other supervisor: A
				  supervisor can only change the state of a user who is assigned to that
				  supervisor's team. A
				  supervisor can only set the state of another user to NOT_READY, READY, or
				  LOGOUT. A
				  supervisor can set the state of a user to LOGOUT only if that user is in READY,
				  NOT_READY, RESERVED, RESERVED_OUTBOUND, RESERVED_OUTBOUND_PREVIEW, TALKING,
				  HOLD, WORK, or WORK_READY state. A
				  supervisor can set the state of a user to NOT_READY only if that user is in
				  READY, WORK, or WORK_READY state. When a
				  supervisor uses this API to set the state of a user to NOT_READY, a reason code
				  must not be used. If a reason code is provided, Finesse rejects it and returns
				  a 400 Invalid Input error. Finesse sends a hard-coded reason code to indicate
				  that the state change was performed by the supervisor. |
|---|---|

| URI: | https ://<FQDN>/finesse/api/User/<id> |
|---|---|
| Example URI: | https ://finesse1.xyz.com/finesse/api/User/1234 |
| Security Constraints: | Agents
						can only act on their own User objects. Supervisors can act on the User objects
						of agents who belong to their team. |
| HTTP Method: | PUT |
| Content Type: | Application/XML |
| Input/Output Format: | XML |
| HTTP Request: | Code Snippet < User > < state > READY </ state > </ User > |
| Request Parameters: | id
						(required): The ID of the user state
						(required): The new state the user wants to be in (for example, LOGOUT, READY,
						NOT_READY) |
| HTTP Response: | 200:
						Success 400:
						Bad Request 401:
						Invalid Supervisor 401:
						Unauthorized 404:
						Not Found 500:
						Internal Server Error 503:
						Service Unavailable |
| Example Failure
						  Response: | Code Snippet < ApiErrors > < ApiError > < ErrorType > Parameter Missing </ ErrorType > < ErrorData > state </ ErrorData > < ErrorMessage > State Parameter missing </ ErrorMessage > </ ApiError > </ ApiErrors > |
| Notifications
						  Triggered: | User
						notification |

| Scenario | Response |
|---|---|
| Change
						from LOGOUT to NOT_READY. | Stand-alone Finesse with
						  Unified CCE: Code Snippet < data > < apiErrors > < apiError > < errorData > 257 </ errorData > < errorMessage > CF_INVALID_PASSWORD_SPECIFIED </ errorMessage > < errorType > Invalid State </ errorType > </ apiError > </ apiErrors > </ data > Coresident Finesse with
						  Unified CCX: Code Snippet < data > < apiErrors > < apiError > < errorData > 1010 </ errorData > < errorMessage > CF_INVALID_PARAMETER </ errorMessage > < errorType > Invalid State </ errorType > </ apiError > </ apiErrors > </ data > |
| Agent
						receives and answers a non-ICD call. | Stand-alone Finesse with
						  Unified CCE: Finesse sends a User notification with state=TALKING. Coresident Finesse with
						  Unified CCX: Finesse does not send a User notification. The agent remains in
						NOT_READY state. |
| Agent
						puts an ICD call on hold. | Stand-alone Finesse with
						  Unified CCE: Finesse sends a User notification with state=HOLD. Coresident Finesse with
						  Unified CCX: Finesse does not send a User notification. The agent remains in
						TALKING state. |
| While
						talking on an ICD call, the agent sets a pending state of READY. | Stand-alone Finesse with
						  Unified CCE: Agent
						transitions to READY state after the call ends. Coresident Finesse with
						  Unified CCX: Unified CCX does not allow an agent to set a pending state of
						READY while that agent is talking on an ICD call. Code Snippet < data > < apiErrors > < apiError > < errorData > 265 </ errorData > < errorMessage > CF_INVALID_AGENT_WORKMODE </ errorMessage > < errorType > Invalid State </ errorType > </ apiError > </ apiErrors > </ data > |
| While
						talking on a non-ICD call (agent state can be TALKING in Unified CCE or
						NOT_READY in Unified CCX), the agent sets a pending state of READY. | Stand-alone Finesse with
						  Unified CCE: Agent
						transitions to READY state after the call ends. Coresident Finesse with
						  Unified CCX: Unified CCX does not allow an agent to set a pending state of
						READY while that agent is talking on a non-ICD call. Code Snippet < data > < apiErrors > < apiError > < errorData > 33 </ errorData > < errorMessage > CF_RESOURCE_BUSY </ errorMessage > < errorType > Invalid State </ errorType > </ apiError > </ apiErrors > </ data > |
| While
						talking on an ICD call, the agent attempts to change from a pending state of
						NOT_READY with reason code 1 to a pending state of NOT_READY with reason code
						2. | Stand-alone Finesse with
						  Unified CCE: Agent
						transitions to NOT_READY state with reason code 2 after the call ends. Coresident Finesse with
						  Unified CCX: Unified CCX allows an agent to set a pending state of NOT_READY
						only once during a call. Unified CCX does not allow an agent to change from one
						Not Ready reason code to another. Code Snippet < data > < apiErrors > < apiError > < errorData > 265 </ errorData > < errorMessage > CF_INVALID_AGENT_WORKMODE </ errorMessage > < errorType > Invalid State </ errorType > </ apiError > </ apiErrors > </ data > |
| A
						supervisor changes the state of an agent on that supervisor's team to
						NOT_READY. | Stand-alone Finesse with
						  Unified CCE: Finesse sends a hard-coded reason code of 999 to indicate the
						forced state change. Coresident Finesse with
						  Unified CCX: Finesse sends a hard-coded reason code of 33 to indicate the
						forced state change. |

| Note | When accessing
			 the Finesse REST API through the Finesse JavaScript library, asynchronous
			 errors have a status code of 400. When receiving the asynchronous error
			 directly through XMPP, the error message has the format described in "Dialog
			 CTI Error Notification." |
|---|---|

| ErrorType | Reason | Deployment Type |
|---|---|---|
| Invalid State | Invalid state transition requested. For
						example, attempt to set Wrap-Up state on an agent that is not allowed to go to
						Wrap-Up, or attempt to change an agent's state from READY state to Wrap-up or
						WORK state. | All |
| Internal Server Error | Attempt to change an agent's state from RESERVED_OUTBOUND to any
						other state. | Unified CCX |