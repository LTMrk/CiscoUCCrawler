---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-finesse-finesse-1501-user-guide-cfin-b-1501-cisc-313b117fcc
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/finesse/finesse_1501/user/guide/cfin_b_1501_cisco-desktop-user-guide/cfin_m_1501_supervisor-tasks.html
retrieved_at: 2026-08-16T20:31:17.595522+00:00
---

Cisco Finesse Agent and Supervisor Desktop User Guide, Release 15.0(1)

# Cisco Finesse Agent and Supervisor Desktop User Guide, Release 15.0(1)

Updated: December 12, 2025

Chapter: Supervisor Tasks

## Chapter: Supervisor Tasks

# Supervisor Tasks

## View Team Performance

Use the Team Performance gadget to view the agents on each of your assigned teams.

Step 1

In the Team Performance gadget, you can view the details of the team selected by default in the Team Name drop-down.

A list of agents for the selected team with their current state, time in state, extension, and action appears. Click the headers
                                          of the columns to sort by Agent Name, State, Time in State, or Extension.

For the Time in State to appear for logged out and Not Ready agents, the agent state must have changed at least once post
                                                      server restart.

By default, the list will only contain logged in agents for the selected team. To view both, logged in and logged out agents,
                                          check the Include logged out agents check box.

Use the Search box to refine any agent details by using the search criterion such as Agent Name, State, or Extension. The search results
                                                      are retained even when you switch between tabs during the active session.

Select an agent and in the corresponding row, click under the Actions tab to monitor the agent, change the state to Ready, Not Ready, or Sign Out the agent.

The Time in State field refreshes every 10 seconds. When Finesse receives the next agent state change event for an agent,
                                                      the timer resets to 0.

Step 2

To view another team, click the Team Name drop-down and choose a new team.

## View Active Call Details

Step 1

From the Team Name drop-down, choose the agent's team.

Step 2

From the displayed list, choose an agent in the Talking state.

Step 3

In the Actions tab of the selected agent, click the down arrow.

The following call details are displayed:

The popover call variable header and the call variables configured by the administrator.

Active Participants : The phone numbers of the active participants in the call.

Held Participants : The phone numbers of the held participants in the call. The Held Participants information is not available for unmonitored
                                                devices. For example, customer or external devices.

Active Participants and Held Participants lists do not contain the expanded agent number, it contains only other participants
                                                            in the call.

Duration : The duration of the call.

Call Status : The current status of the call. Indicates the status of the expanded agent in the call.

Queue Name : The customer service queue to which the call belongs to.

## View Recent Call History

If the Administrator has configured view history for you, use the Team Performance gadget to view the call history of an agent
                              of your assigned team.

Step 1

From the Team Name drop-down, choose the agent's team.

Step 2

From the displayed list, choose any agent. The list contains all logged in agents for the selected team. To view logged in
                                       and logged out agents, check the Include logged out agents checkbox.

Step 3

In the Actions tab of the selected agent, click > View History .

The following call details of the selected agent's Recent Call History are displayed:

Start Time : Indicates the start time of the call.

Duration : Indicates the call duration.

Type : Indicates if the call was an Inbound or Outbound.

Number : Indicates the phone number of the call.

Disposition : Indicates the action taken on the call.

Queue : Indicates the name of the queue assigned to the agent.

Wrap-Up Reason : Indicates the Wrap-Up Reason selected by the agent.

You cannot select any other agent or choose another team while the recent call history of the selected agent is being loaded.
                                                      However, you may change an agent's state or monitor an agent's call during this time-frame.

To navigate back to the Team Performance gadget view, click on the left arrow next to the View Recent Call History header.

## View Recent State History

If the Administrator has configured view history for you, use the Team Performance gadget to view the state history of an
                              agent of your assigned team.

Step 1

From the Team Name drop-down, choose the agent's team.

Step 2

From the displayed list, choose any agent. The list contains all logged in agents for the selected team. To view logged in
                                       and logged out agents, check the Include logged out agents checkbox.

Step 3

In the Actions tab of the selected agent, click > View History .

The following details of the selected agent's Recent State History are displayed:

Start Time : Indicates the start time of the call.

State : Indicates the agent state. In the Team Performance gadget, when an agent state changes to Wrap-Up, the corresponding state
                                                in the Recent State History gadget will display as WORK_READY .

Reason : Indicates the wrap-up reason of the call.

Duration : Indicates the call duration.

You cannot select any other agent or choose another team while the recent state history of the selected agent is being loaded.
                                                      However, you may change an agent's state or monitor an agent's call during this time-frame.

To navigate back to the Team Performance gadget view, click on the left arrow next to the View Recent State History header.

## Change the State of an Agent

Use the Team Performance gadget to change the state of an agent to Ready, Not Ready, or Sign Out.

Step 1

From the Team Name drop-down list, choose the agent's
                                       team.

Step 2

From the displayed list, choose the agent whose state you want to change.

Step 3

In the Actions tab of the selected agent, click and choose:

Ready

To force the agent state to Ready.

Not Ready

To force the agent state to Not Ready.

Sign Out

To sign the agent out.

In the Actions tab, the Ready, Not Ready, and Sign Out options are active only if the action is allowed.

For example, if you select an agent who is in Ready state, you will see only the Not Ready and Sign Out options. If you select
                                          an agent who is in Not Ready state, you will see only the Ready and Sign Out options.

If you sign out an agent who is reserved for a call (in Reserved or Reserved (Outbound) state), is on an active call (in Talking
                                          state), or has a call on hold (in Hold state), the agent will be logged out of the desktop immediately after the call.

## Monitor a Call

You must be in Not Ready state to monitor an agent. You can monitor only one agent at
                              a time. To monitor another agent, you must End the silent
                              monitoring call and then select a new agent.

Step 1

From the Team Name drop-down list, choose the team whose
                                       agents you want to monitor.

Step 2

From the displayed list, choose an agent to monitor.

Step 3

In the Actions tab of the selected agent, click > Monitor .

The silent monitor call appears in the call control area of the desktop. The Hold , Barge In , and End buttons are enabled. Click:

To place the call on hold.

To retrieve the call placed on hold.

To barge in to the call.

Step 4

To end the silent monitor call, click End .

The monitoring initiated on a consult call terminates, when the consult
                                                      call is conferenced. This is due to the temporary nature of the
                                                      monitored call. The monitoring must be re-initiated again, to monitor
                                                      the conferenced call which is already in progress. Please note that
                                                      monitoring initiated on a call before the consult call is placed, will
                                                      not be affected due to conferencing activity and continues without
                                                      disruption.

## Barge In on a Call

The Barge In feature allows you to join a call between an agent and a caller.

You can only barge in on a call that you are silently monitoring.

For the supervisor to be able to barge in, the agent and supervisor
                                                extensions must have visibility to each other's partition or calling
                                                search space (CSS) without any prefix or steering digit.

Step 1

From the Team Name drop-down list, choose the agent's
                                       team.

Step 2

From the displayed list, choose an agent in the Talking state.

Step 3

In the Actions tab of the selected agent, click > Monitor .

The silent monitor call appears in the call control area of your desktop. The Barge In button appears.

Step 4

Click Barge In .

The call becomes a conference call between you, the agent, and the caller.

## Intercept a Call

If you have initiated the conference call you can drop other agents, supervisors, or non-agents from the conference call based
                              on the permission defined by your administrator.

The non-agents in the conference call include the caller, CTI Route Point, IVR port, a device to which no agent is signed
                              in, or a caller device.

The Drop button is displayed on the call control area only if the administrator has set the permission for you to drop participants
                              from the conference call.

Step 1

Click Drop .

Step 2

Click the agent, supervisor or non-agent to drop from the list of participants.

Step 3

Click Drop .

Limitation

Finesse desktop cannot distinguish agents from another peripheral gateway (PG) as agents. So the agents from another PG are
                                          displayed using the same icon used for non-agents ( ) in the Finesse desktop.

## Send Team Message

The Team Message feature allows you to create and send a broadcast message to one or multiple teams. The message appears as
                              a banner across the Finesse desktop and agents can view these messages in real-time. Team Message will be available on your
                              Finesse desktop only if the administrator has configured this feature for you.

Step 1

In the Finesse desktop, click the Team Message icon.

Step 2

In the Compose Message box, enter the broadcast message (maximum number of characters allowed is 255).

Step 3

Select the team or teams to send the message by checking the check box next to the team name.

You can send multiple messages to a single team, multiple teams, or all teams.

Step 4

From the drop-down, you can set an expiry time for the composed messages: starting at 5 minutes and ending at 23:55 hours.
                                       The time is displayed in hours and minutes. However, this time frame can be edited.

Step 5

Click Send .

You can view the latest messages sent by clicking Show recent messages . If you wish to delete any or all messages, check the check box next to the message. Click Delete and confirm the deletion.

The message is removed from active display and the previous non-expired team message will become the active message for the
                                          agent.

Administrator or supervisor who creates a Team Message can delete the created Team Message through TeamMessage API. For more information on deleting a TeamMessage, see https://developer.cisco.com/docs/finesse/#teammessagedelete-a-team-message .

The rate at which messages (create/delete) are published to the teams involved, is capped at 400 per hour and the maximum number of active messages allowed is 4800 . If the limit of active messages is reached, supervisors will not be able to broadcast new messages until an existing team
                                          message is deleted or it expires.

As there are no individual limitations on supervisors, either one or all supervisors can broadcast messages up to the maximum
                                          active messages limit.

| Step 1 | In the Team Performance gadget, you can view the details of the team selected by default in the Team Name drop-down. A list of agents for the selected team with their current state, time in state, extension, and action appears. Click the headers
                                          of the columns to sort by Agent Name, State, Time in State, or Extension. Note For the Time in State to appear for logged out and Not Ready agents, the agent state must have changed at least once post
                                                      server restart. By default, the list will only contain logged in agents for the selected team. To view both, logged in and logged out agents,
                                          check the Include logged out agents check box. Note Use the Search box to refine any agent details by using the search criterion such as Agent Name, State, or Extension. The search results
                                                      are retained even when you switch between tabs during the active session. Select an agent and in the corresponding row, click under the Actions tab to monitor the agent, change the state to Ready, Not Ready, or Sign Out the agent. Note The Time in State field refreshes every 10 seconds. When Finesse receives the next agent state change event for an agent,
                                                      the timer resets to 0. | Note | For the Time in State to appear for logged out and Not Ready agents, the agent state must have changed at least once post
                                                      server restart. | Note | Use the Search box to refine any agent details by using the search criterion such as Agent Name, State, or Extension. The search results
                                                      are retained even when you switch between tabs during the active session. | Note | The Time in State field refreshes every 10 seconds. When Finesse receives the next agent state change event for an agent,
                                                      the timer resets to 0. |
|---|---|---|---|---|---|---|---|
| Note | For the Time in State to appear for logged out and Not Ready agents, the agent state must have changed at least once post
                                                      server restart. |
| Note | Use the Search box to refine any agent details by using the search criterion such as Agent Name, State, or Extension. The search results
                                                      are retained even when you switch between tabs during the active session. |
| Note | The Time in State field refreshes every 10 seconds. When Finesse receives the next agent state change event for an agent,
                                                      the timer resets to 0. |
| Step 2 | To view another team, click the Team Name drop-down and choose a new team. |

| Note | For the Time in State to appear for logged out and Not Ready agents, the agent state must have changed at least once post
                                                      server restart. |
|---|---|

| Note | Use the Search box to refine any agent details by using the search criterion such as Agent Name, State, or Extension. The search results
                                                      are retained even when you switch between tabs during the active session. |
|---|---|

| Note | The Time in State field refreshes every 10 seconds. When Finesse receives the next agent state change event for an agent,
                                                      the timer resets to 0. |
|---|---|

| Step 1 | From the Team Name drop-down, choose the agent's team. |
|---|---|
| Step 2 | From the displayed list, choose an agent in the Talking state. |
| Step 3 | In the Actions tab of the selected agent, click the down arrow. The following call details are displayed: The popover call variable header and the call variables configured by the administrator. Active Participants : The phone numbers of the active participants in the call. Held Participants : The phone numbers of the held participants in the call. The Held Participants information is not available for unmonitored
                                                devices. For example, customer or external devices. Note Active Participants and Held Participants lists do not contain the expanded agent number, it contains only other participants
                                                            in the call. Duration : The duration of the call. Call Status : The current status of the call. Indicates the status of the expanded agent in the call. Queue Name : The customer service queue to which the call belongs to. | Note | Active Participants and Held Participants lists do not contain the expanded agent number, it contains only other participants
                                                            in the call. |
| Note | Active Participants and Held Participants lists do not contain the expanded agent number, it contains only other participants
                                                            in the call. |

| Note | Active Participants and Held Participants lists do not contain the expanded agent number, it contains only other participants
                                                            in the call. |
|---|---|

| Step 1 | From the Team Name drop-down, choose the agent's team. |
|---|---|
| Step 2 | From the displayed list, choose any agent. The list contains all logged in agents for the selected team. To view logged in
                                       and logged out agents, check the Include logged out agents checkbox. |
| Step 3 | In the Actions tab of the selected agent, click > View History . The following call details of the selected agent's Recent Call History are displayed: Start Time : Indicates the start time of the call. Duration : Indicates the call duration. Type : Indicates if the call was an Inbound or Outbound. Number : Indicates the phone number of the call. Disposition : Indicates the action taken on the call. Queue : Indicates the name of the queue assigned to the agent. Wrap-Up Reason : Indicates the Wrap-Up Reason selected by the agent. Note You cannot select any other agent or choose another team while the recent call history of the selected agent is being loaded.
                                                      However, you may change an agent's state or monitor an agent's call during this time-frame. Note To navigate back to the Team Performance gadget view, click on the left arrow next to the View Recent Call History header. | Note | You cannot select any other agent or choose another team while the recent call history of the selected agent is being loaded.
                                                      However, you may change an agent's state or monitor an agent's call during this time-frame. | Note | To navigate back to the Team Performance gadget view, click on the left arrow next to the View Recent Call History header. |
| Note | You cannot select any other agent or choose another team while the recent call history of the selected agent is being loaded.
                                                      However, you may change an agent's state or monitor an agent's call during this time-frame. |
| Note | To navigate back to the Team Performance gadget view, click on the left arrow next to the View Recent Call History header. |

| Note | You cannot select any other agent or choose another team while the recent call history of the selected agent is being loaded.
                                                      However, you may change an agent's state or monitor an agent's call during this time-frame. |
|---|---|

| Note | To navigate back to the Team Performance gadget view, click on the left arrow next to the View Recent Call History header. |
|---|---|

| Step 1 | From the Team Name drop-down, choose the agent's team. |
|---|---|
| Step 2 | From the displayed list, choose any agent. The list contains all logged in agents for the selected team. To view logged in
                                       and logged out agents, check the Include logged out agents checkbox. |
| Step 3 | In the Actions tab of the selected agent, click > View History . The following details of the selected agent's Recent State History are displayed: Start Time : Indicates the start time of the call. State : Indicates the agent state. In the Team Performance gadget, when an agent state changes to Wrap-Up, the corresponding state
                                                in the Recent State History gadget will display as WORK_READY . Reason : Indicates the wrap-up reason of the call. Duration : Indicates the call duration. Note You cannot select any other agent or choose another team while the recent state history of the selected agent is being loaded.
                                                      However, you may change an agent's state or monitor an agent's call during this time-frame. Note To navigate back to the Team Performance gadget view, click on the left arrow next to the View Recent State History header. | Note | You cannot select any other agent or choose another team while the recent state history of the selected agent is being loaded.
                                                      However, you may change an agent's state or monitor an agent's call during this time-frame. | Note | To navigate back to the Team Performance gadget view, click on the left arrow next to the View Recent State History header. |
| Note | You cannot select any other agent or choose another team while the recent state history of the selected agent is being loaded.
                                                      However, you may change an agent's state or monitor an agent's call during this time-frame. |
| Note | To navigate back to the Team Performance gadget view, click on the left arrow next to the View Recent State History header. |

| Note | You cannot select any other agent or choose another team while the recent state history of the selected agent is being loaded.
                                                      However, you may change an agent's state or monitor an agent's call during this time-frame. |
|---|---|

| Note | To navigate back to the Team Performance gadget view, click on the left arrow next to the View Recent State History header. |
|---|---|

| Step 1 | From the Team Name drop-down list, choose the agent's
                                       team. |
|---|---|
| Step 2 | From the displayed list, choose the agent whose state you want to change. |
| Step 3 | In the Actions tab of the selected agent, click and choose: Ready To force the agent state to Ready. Not Ready To force the agent state to Not Ready. Sign Out To sign the agent out. In the Actions tab, the Ready, Not Ready, and Sign Out options are active only if the action is allowed. For example, if you select an agent who is in Ready state, you will see only the Not Ready and Sign Out options. If you select
                                          an agent who is in Not Ready state, you will see only the Ready and Sign Out options. If you sign out an agent who is reserved for a call (in Reserved or Reserved (Outbound) state), is on an active call (in Talking
                                          state), or has a call on hold (in Hold state), the agent will be logged out of the desktop immediately after the call. | Ready | To force the agent state to Ready. | Not Ready | To force the agent state to Not Ready. | Sign Out | To sign the agent out. |
| Ready | To force the agent state to Ready. |
| Not Ready | To force the agent state to Not Ready. |
| Sign Out | To sign the agent out. |

| Ready | To force the agent state to Ready. |
|---|---|
| Not Ready | To force the agent state to Not Ready. |
| Sign Out | To sign the agent out. |

| Step 1 | From the Team Name drop-down list, choose the team whose
                                       agents you want to monitor. |
|---|---|
| Step 2 | From the displayed list, choose an agent to monitor. |
| Step 3 | In the Actions tab of the selected agent, click > Monitor . The silent monitor call appears in the call control area of the desktop. The Hold , Barge In , and End buttons are enabled. Click: Hold To place the call on hold. Retrieve To retrieve the call placed on hold. Barge In To barge in to the call. | Hold | To place the call on hold. | Retrieve | To retrieve the call placed on hold. | Barge In | To barge in to the call. |
| Hold | To place the call on hold. |
| Retrieve | To retrieve the call placed on hold. |
| Barge In | To barge in to the call. |
| Step 4 | To end the silent monitor call, click End . Note The monitoring initiated on a consult call terminates, when the consult
                                                      call is conferenced. This is due to the temporary nature of the
                                                      monitored call. The monitoring must be re-initiated again, to monitor
                                                      the conferenced call which is already in progress. Please note that
                                                      monitoring initiated on a call before the consult call is placed, will
                                                      not be affected due to conferencing activity and continues without
                                                      disruption. | Note | The monitoring initiated on a consult call terminates, when the consult
                                                      call is conferenced. This is due to the temporary nature of the
                                                      monitored call. The monitoring must be re-initiated again, to monitor
                                                      the conferenced call which is already in progress. Please note that
                                                      monitoring initiated on a call before the consult call is placed, will
                                                      not be affected due to conferencing activity and continues without
                                                      disruption. |
| Note | The monitoring initiated on a consult call terminates, when the consult
                                                      call is conferenced. This is due to the temporary nature of the
                                                      monitored call. The monitoring must be re-initiated again, to monitor
                                                      the conferenced call which is already in progress. Please note that
                                                      monitoring initiated on a call before the consult call is placed, will
                                                      not be affected due to conferencing activity and continues without
                                                      disruption. |

| Hold | To place the call on hold. |
|---|---|
| Retrieve | To retrieve the call placed on hold. |
| Barge In | To barge in to the call. |

| Note | The monitoring initiated on a consult call terminates, when the consult
                                                      call is conferenced. This is due to the temporary nature of the
                                                      monitored call. The monitoring must be re-initiated again, to monitor
                                                      the conferenced call which is already in progress. Please note that
                                                      monitoring initiated on a call before the consult call is placed, will
                                                      not be affected due to conferencing activity and continues without
                                                      disruption. |
|---|---|

| Note | You can only barge in on a call that you are silently monitoring. For the supervisor to be able to barge in, the agent and supervisor
                                                extensions must have visibility to each other's partition or calling
                                                search space (CSS) without any prefix or steering digit. |
|---|---|

| Step 1 | From the Team Name drop-down list, choose the agent's
                                       team. |
|---|---|
| Step 2 | From the displayed list, choose an agent in the Talking state. |
| Step 3 | In the Actions tab of the selected agent, click > Monitor . The silent monitor call appears in the call control area of your desktop. The Barge In button appears. |
| Step 4 | Click Barge In . The call becomes a conference call between you, the agent, and the caller. |

| Step 1 | Click Drop . The agents, supervisors, or non-agents from the conference call are displayed. The agents and supervisors are prefixed with
                                       the icon ( ) followed by the extension that is used to sign-in to the Finesse desktop. The non-agents are prefixed with the icon ( ) followed by the ID of the caller device, CTI Route Point, IVR port, or a device to which no agent is signed in. |
|---|---|
| Step 2 | Click the agent, supervisor or non-agent to drop from the list of participants. A prompt message is displayed to confirm the participant to be dropped from the conference call. |
| Step 3 | Click Drop . Limitation Finesse desktop cannot distinguish agents from another peripheral gateway (PG) as agents. So the agents from another PG are
                                          displayed using the same icon used for non-agents ( ) in the Finesse desktop. |

| Step 1 | In the Finesse desktop, click the Team Message icon. |
|---|---|
| Step 2 | In the Compose Message box, enter the broadcast message (maximum number of characters allowed is 255). |
| Step 3 | Select the team or teams to send the message by checking the check box next to the team name. Note You can send multiple messages to a single team, multiple teams, or all teams. | Note | You can send multiple messages to a single team, multiple teams, or all teams. |
| Note | You can send multiple messages to a single team, multiple teams, or all teams. |
| Step 4 | From the drop-down, you can set an expiry time for the composed messages: starting at 5 minutes and ending at 23:55 hours.
                                       The time is displayed in hours and minutes. However, this time frame can be edited. |
| Step 5 | Click Send . You can view the latest messages sent by clicking Show recent messages . If you wish to delete any or all messages, check the check box next to the message. Click Delete and confirm the deletion. The message is removed from active display and the previous non-expired team message will become the active message for the
                                          agent. Note Administrator or supervisor who creates a Team Message can delete the created Team Message through TeamMessage API. For more information on deleting a TeamMessage, see https://developer.cisco.com/docs/finesse/#teammessagedelete-a-team-message . | Note | Administrator or supervisor who creates a Team Message can delete the created Team Message through TeamMessage API. For more information on deleting a TeamMessage, see https://developer.cisco.com/docs/finesse/#teammessagedelete-a-team-message . |
| Note | Administrator or supervisor who creates a Team Message can delete the created Team Message through TeamMessage API. For more information on deleting a TeamMessage, see https://developer.cisco.com/docs/finesse/#teammessagedelete-a-team-message . |

| Note | You can send multiple messages to a single team, multiple teams, or all teams. |
|---|---|

| Note | Administrator or supervisor who creates a Team Message can delete the created Team Message through TeamMessage API. For more information on deleting a TeamMessage, see https://developer.cisco.com/docs/finesse/#teammessagedelete-a-team-message . |
|---|---|

| Note | The rate at which messages (create/delete) are published to the teams involved, is capped at 400 per hour and the maximum number of active messages allowed is 4800 . If the limit of active messages is reached, supervisors will not be able to broadcast new messages until an existing team
                                          message is deleted or it expires. As there are no individual limitations on supervisors, either one or all supervisors can broadcast messages up to the maximum
                                          active messages limit. |
|---|---|