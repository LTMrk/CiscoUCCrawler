---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-icm-enterprise-icm-enterprise-12-5-1-user-guide--ba27d428ac
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/icm_enterprise/icm_enterprise_12_5_1/user/guide/ucce_b_ctios-supervisor-desktop-user-guide-125/ucce_b_ctios-supervisor-desktop-user-guide-125_chapter_0101.html
retrieved_at: 2026-08-22T00:00:44.420343+00:00
---

CTIOS Supervisor Desktop User Guide

# CTIOS Supervisor Desktop User Guide

Updated: January 31, 2020

Chapter: Use Cases

## Chapter: Use Cases

- Use Cases

- Unified CM-Based Silent Monitor Use Cases

# Use Cases

## Unified CM-Based Silent Monitor Use Cases

The following use cases illustrate how Unified CM silent monitor behaves in various scenarios.

Supervisor Silent Monitors Agent with Legacy Unified CM

The supervisor desktop receives a control failure and displays error 13140.

Supervisor Silent Monitors Agent; Agent has Legacy Phone

The supervisor desktop receives a control failure and displays error 13139.

Supervisor Silent Monitors Agent; Supervisor has Legacy Phone

Silent monitor is successful. The supervisor is not required to have a 79x1 phone for silent monitor.

Supervisor Silent Monitors Mobile Agent

The supervisor desktop receives a control failure and displays error 13140.

Supervisor Silent Monitors Agent Whose Phone Has the Built-in-Bridge Disabled

The supervisor desktop receives a control failure and displays error 13141.

Supervisor Silent Monitors Agent Whose Line Does Not Belong to a Partition Included in the Monitoring Calling Search Space

The supervisor desktop receives a control failure and displays error 13142.

Supervisor Selects an Agent with No Calls

Because Unified CM does not allow a silent monitor session to start before a call is active on the device, CTI OS disables Start Silent Monitor until the agent has a call. This behavior is different from that of the CTI OS-based silent monitor, where an agent without
                                       a call can be monitored.

Supervisor Selects an Agent with a Call

Start Silent Monitor is enabled.

Supervisor Silent Monitors Agent

The supervisor is silent monitoring an agent. Because Unified CM-based silent monitor is implemented via a call, the supervisor
                                       can hold, retrieve, and release the call. This behavior is different from the CTI OS-based silent monitor, where silent monitor
                                       is implemented using a UDP stream between the two party's desktops.

Supervisor Silent Monitors Agent and Updates Call Data

The supervisor can update call data for a silent monitor call. However, because the call cannot be transferred or conferenced,
                                       and because the agent cannot see the call, this functionality has limited use. This behavior is not possible using CTI OS-based
                                       silent monitor because no call exists for the silent monitor session.

Supervisor Stops Silent Monitoring

The monitoring call is linked to the call being monitored. When either the agent or the customer terminates the monitored
                                       call, the monitoring call ends as well.

Supervisors can also stop monitoring anytime after it is started by releasing the monitor call from either their desktop or
                                       their IP Phone. This is different from the CTI OS-based silent monitor because no call exists for the silent monitor session.

Supervisor Selects Agent with a Call while Silent Monitoring another Agent

Because supervisors are not allowed to silent monitor two agents at the same time, the supervisor's Start Silent Monitor button is disabled.

Supervisor Silent Monitors Agent, Agent Holds and Resumes Call

In this case, the supervisor is silent monitoring an agent while an agent puts the call on hold and then resumes the call.
                                       When the call is on hold, the supervisor's silent monitor call is put on hold. A Music on Hold (MOH) server is not inserted
                                       into the silent monitor call so the supervisor hears nothing until the agent resumes the call. The only means that the supervisor
                                       has of knowing that the agent has put the call on hold is that the call appears on the supervisor desktop's Monitored Calls
                                       grid.

Supervisor Silent Monitors Agent, Customer/Other Agent Local to Unified CM Holds Call

In this case, the supervisor is silent monitoring an agent on a call with another agent or customer; supervisor and agent
                                       are on the same Unified CM. When the customer or other agent puts the call on hold, the supervisor's silent monitor call is
                                       put on hold. An MOH server is inserted into the silent monitor call so the supervisor hears MOH.

Supervisor Silent Monitors Customer External to Unified CM Holds Call

In this case, the supervisor is silent monitoring an agent on a call with a customer using a device not controlled by Unified
                                       CM. When the customer puts the call on hold, the supervisor's silent monitor call is put on hold. The supervisor hears whatever
                                       the agent hears.

Supervisor Silent Monitors Agent, Supervisor Holds and Retrieves Silent Monitor Call

When the supervisor holds a silent monitor call, the supervisor hears nothing when the call is put on hold. An MOH server
                                       is not inserted into the call. This behavior  is not allowed in the CTI OS-based silent monitor because the CTI OS silent
                                       monitor solution is not implemented through a call.

Supervisor Silent Monitors Agent Who Has Put Call on Hold

Unified CM does not allow a supervisor to monitor a call that is on hold. Start Silent Monitor is disabled when the supervisor selects an agent who is on hold. This behavior is different from the CTI OS-based silent
                                       monitor. Supervisors can start silent monitor on held calls using the CTI OS silent monitor solution.

Supervisor Silent Monitors Agent, Agent Hangs Up

The supervisor's silent monitor call ends when the agent hangs up the call. After the silent monitor call ends, the supervisor's Start Silent Monitor button is enabled. If the supervisor wants to monitor the agent's next call, the supervisor must start monitoring the agent
                                       again when the agent receives a new call.

This behavior is different from the CTI OS-based silent monitor. The CTI OS-based silent monitor continues to monitor the
                                       agent until the supervisor clicks Stop Silent Monitor or until the agent logs out.

Supervisor Silent Monitors Agent, Caller Hangs Up

The supervisor's silent monitor call ends when the caller hangs up the call. This behavior is different from the CTI OS-based
                                       silent monitor. The CTI OS-based silent monitor continues to monitor the agent until the supervisor clicks Stop Silent Monitor or until the agent logs out.

Supervisor Silent Monitors Agent, Supervisor Configured for Wrap Up

Supervisors do not wrap up after a silent monitor call ends regardless of the supervisor's desk settings.

Supervisor Silent Monitors Agent, Agent Wraps Up

The supervisor's silent monitor call ends when the voice portion of the call has terminated. This means that the supervisor's
                                       silent monitor session ends when the agent transitions to the wrap-up state. This behavior is different from the CTI OS-based
                                       silent monitor. The CTI OS-based silent monitor continues to monitor the agent until the supervisor clicks Stop Silent Monitor or until the agent logs out.

Agent puts the monitored call on hold and accepts a new call, then supervisor monitors the new call

The supervisor must stop monitoring the held call. Choose the  new call to the agent and then start monitoring that call.
                                       The supervisor can monitor only one call at a time. This behavior is different from the CTI OS-based silent monitor. The CTI
                                       OS-based silent monitor automatically monitors the active call.

The Supervisor Receives a Call While Monitoring an Agent

The supervisor can accept an incoming call while silently  monitoring an agent. The silent monitor call is put on hold when
                                       the supervisor answers the new call. The supervisor can click Alternate to cycle between the calls. The supervisor can click Reconnect to release the new call and return to the silent monitor call.

This behavior is different from the CTI OS-based silent monitor. Because CTI OS-based silent monitor sessions are played to
                                       the supervisor desktop's speaker, there is no silent monitor call to be put on hold. The supervisor hears the new call on
                                       the phone and the silent monitor session on the speaker.

Supervisor Silent Monitors Agent, Agent Consults

The supervisor's silent monitor call is put on hold while the agent is talking to the consulted party. If the supervisor wants
                                       to monitor the consult call, the supervisor must stop monitoring the held call first. This behavior is different from the
                                       CTI OS-based silent monitor. The CTI OS-based silent monitor automatically monitors the active call.

Supervisor Silent Monitors Agent, Agent Consults and Reconnects

The supervisor's silent monitor call is put on hold while the agent is talking to the consulted party. When the agent reconnects,
                                       the supervisor's silent monitor call is taken off hold and the supervisor resumes hearing the agent's call. This behavior
                                       is different from the CTI OS-based silent monitor. The CTI OS-based silent monitor automatically monitors the active call.

Supervisor Silent Monitoring Agent, Agent Consults, Supervisor Monitors Consult Call

Because a supervisor is only allowed one silent monitor session at a time, the supervisor must stop silent monitoring the
                                       current call and then start silent monitoring the consult call. The silent monitor session ends when the supervisor stops
                                       silent monitor or when the original agent transfers or conferences the consult call. This behavior is different from the CTI
                                       OS-based silent monitor. The CTI OS-based silent monitor automatically monitors the active call. If the call is transferred
                                       or conferenced, the supervisor continues to monitor the agent until the supervisor clicks Stop Silent Monitor or the agent logs out.

Supervisor Silent Monitors Agent, Agent Consults and Conferences

The supervisor's silent monitor call is put on hold while the agent is talking to the consulted party. When the agent completes
                                       the conference, the supervisor hears all parties on the conference. This behavior is slightly different from the CTI OS-based
                                       silent monitor. The CTI OS-based silent monitor automatically monitors the active call (the consult call is monitored until
                                       the conference is completed).

Supervisor Silent Monitors Agent Already Monitored by another Supervisor

The supervisor's Start Silent Monitor button is disabled when an agent who currently has a call monitored by another supervisor is selected in the agent grid.

Supervisor Silent Monitors Agent, Barges In, and Intercepts

Currently, a supervisor is not allowed to barge in on an agent when the supervisor has an active call with the agent. Because
                                       silent monitor is implemented through a special call with the agent, the supervisor must stop silent monitoring by clicking
                                       either Release or Stop Silent Monitor before barging in. This behavior is different from the CTI OS-based silent monitor. The supervisor does not need to stop
                                       silent monitor session to barge in.

Supervisor Silent Monitors and Consultative Conference

Supervisor Silent Monitors and Consultative Transfer

Supervisor Silent Monitors and Single Step Transfer

Not supported. Transfer and Conference are disabled when the supervisor is silent monitoring.

Supervisor Silent Monitors in Not Ready State

The supervisor is allowed to silent monitor in this state provided the supervisor has selected an agent who is in the Talking
                                       state.

Supervisor Silent Monitors in Ready State

Supervisor Silent Monitors in Talking State

Supervisor Silent Monitors in Wrap Up State

The supervisor is not allowed to silent monitor in these states. Start Silent Monitor is disabled.  This behavior is different from the CTI OS-based silent monitor. Because  the CTI OS-based silent monitor is
                                       not implemented through a  call, the supervisor does not have to be Not Ready.

Supervisor Silent Monitors Outbound Agent

A supervisor can monitor an outbound agent the same as any other agent.

Supervisor Silent Monitors Outbound Agent with Reservation Call

When a supervisor selects an outbound reservation call, Start Silent Monitor is disabled. This behavior is different from the CTI OS-based silent monitor. The CTI OS-based silent monitor does not prevent
                                       supervisors from monitoring the reservation call.

Supervisor Silent Monitors another Supervisor

When a supervisor monitors another supervisor, the monitoring supervisor sees the silent monitor call on the desktop. The
                                       button enablement for the monitoring supervisor is the same as when an agent is monitored. The monitored supervisor does not
                                       see the monitored call on the desktop.

Supervisor Barges In on Agent Monitored by another Supervisor

If Supervisor A is monitoring Agent A and Supervisor B barges in, Supervisor A hears the conference among Agent A, Supervisor
                                       B, and the customer.

Supervisor Silent Monitors 7.1 or Earlier Agent Desktop

Supervisors can monitor legacy CTI OS desktops and Siebel  desktops with Unified CM-based silent monitor. The only restriction
                                       is the silent monitor warning that can optionally be displayed on the agent desktop. Because the events that legacy desktops
                                       use to display the warning are now different, the legacy desktop cannot display the warning.

7.1 or Earlier Supervisor Silent Monitors 7.2 Agent desktop

If CTI OS Server is configured for Unified CM-based silent  monitor and a supervisor using a 7.1 or earlier desktop attempts
                                       to monitor an agent using a 7.2 desktop, CTI OS rejects the request to silent monitor the agent. The supervisor desktop displays
                                       a dialog containing error code 0x15.

Supervisor Silent Monitors Agent Whose Device has Security Enabled

Unified CM rejects requests to silent monitor agents whose devices have security enabled.

| Supervisor Silent Monitors Agent with Legacy Unified CM | The supervisor desktop receives a control failure and displays error 13140. |
|---|---|
| Supervisor Silent Monitors Agent; Agent has Legacy Phone | The supervisor desktop receives a control failure and displays error 13139. |
| Supervisor Silent Monitors Agent; Supervisor has Legacy Phone | Silent monitor is successful. The supervisor is not required to have a 79x1 phone for silent monitor. |
| Supervisor Silent Monitors Mobile Agent | The supervisor desktop receives a control failure and displays error 13140. |
| Supervisor Silent Monitors Agent Whose Phone Has the Built-in-Bridge Disabled | The supervisor desktop receives a control failure and displays error 13141. |
| Supervisor Silent Monitors Agent Whose Line Does Not Belong to a Partition Included in the Monitoring Calling Search Space | The supervisor desktop receives a control failure and displays error 13142. |
| Supervisor Selects an Agent with No Calls | Because Unified CM does not allow a silent monitor session to start before a call is active on the device, CTI OS disables Start Silent Monitor until the agent has a call. This behavior is different from that of the CTI OS-based silent monitor, where an agent without
                                       a call can be monitored. |
| Supervisor Selects an Agent with a Call | Start Silent Monitor is enabled. |
| Supervisor Silent Monitors Agent | The supervisor is silent monitoring an agent. Because Unified CM-based silent monitor is implemented via a call, the supervisor
                                       can hold, retrieve, and release the call. This behavior is different from the CTI OS-based silent monitor, where silent monitor
                                       is implemented using a UDP stream between the two party's desktops. |
| Supervisor Silent Monitors Agent and Updates Call Data | The supervisor can update call data for a silent monitor call. However, because the call cannot be transferred or conferenced,
                                       and because the agent cannot see the call, this functionality has limited use. This behavior is not possible using CTI OS-based
                                       silent monitor because no call exists for the silent monitor session. |
| Supervisor Stops Silent Monitoring | The monitoring call is linked to the call being monitored. When either the agent or the customer terminates the monitored
                                       call, the monitoring call ends as well. Supervisors can also stop monitoring anytime after it is started by releasing the monitor call from either their desktop or
                                       their IP Phone. This is different from the CTI OS-based silent monitor because no call exists for the silent monitor session. |
| Supervisor Selects Agent with a Call while Silent Monitoring another Agent | Because supervisors are not allowed to silent monitor two agents at the same time, the supervisor's Start Silent Monitor button is disabled. |
| Supervisor Silent Monitors Agent, Agent Holds and Resumes Call | In this case, the supervisor is silent monitoring an agent while an agent puts the call on hold and then resumes the call.
                                       When the call is on hold, the supervisor's silent monitor call is put on hold. A Music on Hold (MOH) server is not inserted
                                       into the silent monitor call so the supervisor hears nothing until the agent resumes the call. The only means that the supervisor
                                       has of knowing that the agent has put the call on hold is that the call appears on the supervisor desktop's Monitored Calls
                                       grid. |
| Supervisor Silent Monitors Agent, Customer/Other Agent Local to Unified CM Holds Call | In this case, the supervisor is silent monitoring an agent on a call with another agent or customer; supervisor and agent
                                       are on the same Unified CM. When the customer or other agent puts the call on hold, the supervisor's silent monitor call is
                                       put on hold. An MOH server is inserted into the silent monitor call so the supervisor hears MOH. |
| Supervisor Silent Monitors Customer External to Unified CM Holds Call | In this case, the supervisor is silent monitoring an agent on a call with a customer using a device not controlled by Unified
                                       CM. When the customer puts the call on hold, the supervisor's silent monitor call is put on hold. The supervisor hears whatever
                                       the agent hears. |
| Supervisor Silent Monitors Agent, Supervisor Holds and Retrieves Silent Monitor Call | When the supervisor holds a silent monitor call, the supervisor hears nothing when the call is put on hold. An MOH server
                                       is not inserted into the call. This behavior  is not allowed in the CTI OS-based silent monitor because the CTI OS silent
                                       monitor solution is not implemented through a call. |
| Supervisor Silent Monitors Agent Who Has Put Call on Hold | Unified CM does not allow a supervisor to monitor a call that is on hold. Start Silent Monitor is disabled when the supervisor selects an agent who is on hold. This behavior is different from the CTI OS-based silent
                                       monitor. Supervisors can start silent monitor on held calls using the CTI OS silent monitor solution. |
| Supervisor Silent Monitors Agent, Agent Hangs Up | The supervisor's silent monitor call ends when the agent hangs up the call. After the silent monitor call ends, the supervisor's Start Silent Monitor button is enabled. If the supervisor wants to monitor the agent's next call, the supervisor must start monitoring the agent
                                       again when the agent receives a new call. This behavior is different from the CTI OS-based silent monitor. The CTI OS-based silent monitor continues to monitor the
                                       agent until the supervisor clicks Stop Silent Monitor or until the agent logs out. |
| Supervisor Silent Monitors Agent, Caller Hangs Up | The supervisor's silent monitor call ends when the caller hangs up the call. This behavior is different from the CTI OS-based
                                       silent monitor. The CTI OS-based silent monitor continues to monitor the agent until the supervisor clicks Stop Silent Monitor or until the agent logs out. |
| Supervisor Silent Monitors Agent, Supervisor Configured for Wrap Up | Supervisors do not wrap up after a silent monitor call ends regardless of the supervisor's desk settings. |
| Supervisor Silent Monitors Agent, Agent Wraps Up | The supervisor's silent monitor call ends when the voice portion of the call has terminated. This means that the supervisor's
                                       silent monitor session ends when the agent transitions to the wrap-up state. This behavior is different from the CTI OS-based
                                       silent monitor. The CTI OS-based silent monitor continues to monitor the agent until the supervisor clicks Stop Silent Monitor or until the agent logs out. |
| Agent puts the monitored call on hold and accepts a new call, then supervisor monitors the new call | The supervisor must stop monitoring the held call. Choose the  new call to the agent and then start monitoring that call.
                                       The supervisor can monitor only one call at a time. This behavior is different from the CTI OS-based silent monitor. The CTI
                                       OS-based silent monitor automatically monitors the active call. |
| The Supervisor Receives a Call While Monitoring an Agent | The supervisor can accept an incoming call while silently  monitoring an agent. The silent monitor call is put on hold when
                                       the supervisor answers the new call. The supervisor can click Alternate to cycle between the calls. The supervisor can click Reconnect to release the new call and return to the silent monitor call. This behavior is different from the CTI OS-based silent monitor. Because CTI OS-based silent monitor sessions are played to
                                       the supervisor desktop's speaker, there is no silent monitor call to be put on hold. The supervisor hears the new call on
                                       the phone and the silent monitor session on the speaker. |
| Supervisor Silent Monitors Agent, Agent Consults | The supervisor's silent monitor call is put on hold while the agent is talking to the consulted party. If the supervisor wants
                                       to monitor the consult call, the supervisor must stop monitoring the held call first. This behavior is different from the
                                       CTI OS-based silent monitor. The CTI OS-based silent monitor automatically monitors the active call. |
| Supervisor Silent Monitors Agent, Agent Consults and Reconnects | The supervisor's silent monitor call is put on hold while the agent is talking to the consulted party. When the agent reconnects,
                                       the supervisor's silent monitor call is taken off hold and the supervisor resumes hearing the agent's call. This behavior
                                       is different from the CTI OS-based silent monitor. The CTI OS-based silent monitor automatically monitors the active call. |
| Supervisor Silent Monitoring Agent, Agent Consults, Supervisor Monitors Consult Call | Because a supervisor is only allowed one silent monitor session at a time, the supervisor must stop silent monitoring the
                                       current call and then start silent monitoring the consult call. The silent monitor session ends when the supervisor stops
                                       silent monitor or when the original agent transfers or conferences the consult call. This behavior is different from the CTI
                                       OS-based silent monitor. The CTI OS-based silent monitor automatically monitors the active call. If the call is transferred
                                       or conferenced, the supervisor continues to monitor the agent until the supervisor clicks Stop Silent Monitor or the agent logs out. |
| Supervisor Silent Monitors Agent, Agent Consults and Conferences | The supervisor's silent monitor call is put on hold while the agent is talking to the consulted party. When the agent completes
                                       the conference, the supervisor hears all parties on the conference. This behavior is slightly different from the CTI OS-based
                                       silent monitor. The CTI OS-based silent monitor automatically monitors the active call (the consult call is monitored until
                                       the conference is completed). |
| Supervisor Silent Monitors Agent Already Monitored by another Supervisor | The supervisor's Start Silent Monitor button is disabled when an agent who currently has a call monitored by another supervisor is selected in the agent grid. |
| Supervisor Silent Monitors Agent, Barges In, and Intercepts | Currently, a supervisor is not allowed to barge in on an agent when the supervisor has an active call with the agent. Because
                                       silent monitor is implemented through a special call with the agent, the supervisor must stop silent monitoring by clicking
                                       either Release or Stop Silent Monitor before barging in. This behavior is different from the CTI OS-based silent monitor. The supervisor does not need to stop
                                       silent monitor session to barge in. |
| Supervisor Silent Monitors and Consultative Conference Supervisor Silent Monitors and Consultative Transfer Supervisor Silent Monitors and Single Step Transfer | Not supported. Transfer and Conference are disabled when the supervisor is silent monitoring. |
| Supervisor Silent Monitors in Not Ready State | The supervisor is allowed to silent monitor in this state provided the supervisor has selected an agent who is in the Talking
                                       state. |
| Supervisor Silent Monitors in Ready State Supervisor Silent Monitors in Talking State Supervisor Silent Monitors in Wrap Up State | The supervisor is not allowed to silent monitor in these states. Start Silent Monitor is disabled.  This behavior is different from the CTI OS-based silent monitor. Because  the CTI OS-based silent monitor is
                                       not implemented through a  call, the supervisor does not have to be Not Ready. |
| Supervisor Silent Monitors Outbound Agent | A supervisor can monitor an outbound agent the same as any other agent. |
| Supervisor Silent Monitors Outbound Agent with Reservation Call | When a supervisor selects an outbound reservation call, Start Silent Monitor is disabled. This behavior is different from the CTI OS-based silent monitor. The CTI OS-based silent monitor does not prevent
                                       supervisors from monitoring the reservation call. |
| Supervisor Silent Monitors another Supervisor | When a supervisor monitors another supervisor, the monitoring supervisor sees the silent monitor call on the desktop. The
                                       button enablement for the monitoring supervisor is the same as when an agent is monitored. The monitored supervisor does not
                                       see the monitored call on the desktop. |
| Supervisor Barges In on Agent Monitored by another Supervisor | If Supervisor A is monitoring Agent A and Supervisor B barges in, Supervisor A hears the conference among Agent A, Supervisor
                                       B, and the customer. |
| Supervisor Silent Monitors 7.1 or Earlier Agent Desktop | Supervisors can monitor legacy CTI OS desktops and Siebel  desktops with Unified CM-based silent monitor. The only restriction
                                       is the silent monitor warning that can optionally be displayed on the agent desktop. Because the events that legacy desktops
                                       use to display the warning are now different, the legacy desktop cannot display the warning. |
| 7.1 or Earlier Supervisor Silent Monitors 7.2 Agent desktop | If CTI OS Server is configured for Unified CM-based silent  monitor and a supervisor using a 7.1 or earlier desktop attempts
                                       to monitor an agent using a 7.2 desktop, CTI OS rejects the request to silent monitor the agent. The supervisor desktop displays
                                       a dialog containing error code 0x15. |
| Supervisor Silent Monitors Agent Whose Device has Security Enabled | Unified CM rejects requests to silent monitor agents whose devices have security enabled. |