---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-finesse-finesse-1501-admin-guide-cfin-b-150-cisc-50e6f945d3
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/finesse/finesse_1501/admin/guide/cfin_b_150_cisco-finesse-administration-guide/cfin_m_150_manage-reasons.html
retrieved_at: 2026-08-21T12:04:40.358842+00:00
---

Cisco Finesse Administration Guide, Release 15.0(1)

# Cisco Finesse Administration Guide, Release 15.0(1)

Updated: December 12, 2025

Chapter: Manage Reasons

## Chapter: Manage Reasons

# Manage Reasons

## Wrap-Up Reasons

Wrap-Up reasons represent the reasons that agents can apply to calls and digital interactions. A Wrap-Up reason indicates
                              why a customer contacted the contact center. For example, you may have one Wrap-Up reason for sales interactions and another
                              for support interactions.

You can configure Wrap-Up reasons to be available globally to all agents or only to specific teams. The wrap-up reasons are applicable to both voice and digital channels.

Use the Manage Wrap-Up Reasons gadget to view, add, edit, or delete Wrap-Up reasons. Click the Reason Label header to sort
                              the Wrap-Up reasons in ascending or descending order. Click the Global header to sort the Wrap-Up reasons by whether they
                              are global (Yes) or not (No).

Cisco Finesse supports a maximum of 100 global and 1500 team Wrap-Up reasons. No more than 100 Wrap-Up reasons can be assigned
                                          to any one team.

Cisco Finesse supports the wrap-up functionality for all types of inbound and outbound calls.

Cisco Finesse supports the wrap-up functionality for all the digital channel interactions.

To enable wrap-up, you must configure both of the following attributes in the Unified CCE Agent Desktop Settings:

For more information about configuring Agent Desktop Settings, see the Configuration Manager Online Help for Unified CCE.

The showWrapUpTimer property can be used to show or hide timer in wrap-up state.

If showWrapUpTimer is set to true then timer is displayed.

If showWrapUpTimer is set to false then timer is hidden.

Wrap-Up timer is configurable. By default wrapUpCountDown property is set to true. The timer counts down by default when the agent is in wrap-up state. For more information, see Desktop Properties .

For Example, if you set the timer to 30 seconds, by default the timer starts from 30 and ends at zero.

The default behavior can be changed by setting the wrapUpCountDown property to false.

If an agent is configured for wrap-up and selects a pending state during a call, when the call finishes that agent goes into
                                          wrap-up and not the pending state selected during the call. The agent can end wrap-up by either selecting a new state (Ready
                                          or Not Ready) or letting the wrap-up timer expire. If the agent selects a new state, the new state overrides the pending state
                                          selected during the call. If the wrap-up timer expires, the agent transitions to the pending state.

Pending states are not applicable for digital channels.

The following table describes the fields on the Manage Wrap-Up Reasons gadget:

Field

Explanation

Reason Label

The label for the Wrap-Up reason.

This label must be unique for each Wrap-Up reason and has a maximum length of 39 bytes (which equals 39 US English characters).
                                          Both alphanumeric and special characters are supported.

Global?

Yes/No. Indicates if the Wrap-Up reason is available globally to all agents (Yes) or to specific teams of agents (No).

Actions on the Manage Wrap-Up Reasons gadget:

New: Add a new Wrap-Up reason

Edit: Edit an existing Wrap-Up reason

Delete: Delete a Wrap-Up reason

Refresh: Reload the list of Wrap-Up reasons from the server

When you add, edit, or delete a Wrap-Up reason, the changes you make take effect on the agent or supervisor desktop after
                                          three seconds. However, agents who are signed in when the changes are made must sign out and sign in again to see those changes
                                          reflected on their desktops.

### Add Wrap-Up Reason

Step 1

In the Manage Wrap-Up Reasons gadget, click New .

Step 2

In the Reason Label field, add a label for the Wrap-Up reason.

Wrap-Up reason labels are limited to 39 bytes.

Step 3

If the Wrap-Up reason is global, select the Global? check box. If the Wrap-Up reason is specific to a team, clear the Global?
                                          check box.

By default, the Global? check box is selected.

Step 4

Click Save .

### Edit Wrap-Up Reason

Step 1

In the Manage Wrap-Up Reasons gadget, select the Wrap-Up reason that you want to edit.

Step 2

Click Edit .

The Edit Wrap-Up Reason area appears.

Step 3

In the Wrap-Up Reason Label field, enter the new label for the Wrap-Up reason. If you want to change who has access to the
                                          Wrap-Up reason, select or clear the Global? check box.

Step 4

Click Save .

### Delete Wrap-Up Reason

Step 1

In the Manage Wrap-Up Reasons gadget, select the Wrap-Up reason that you want to delete.

Step 2

Click Delete .

A question appears asking you to confirm that you want to delete the selected Wrap-Up reason.

Step 3

Click Yes to confirm the deletion of the selected Wrap-Up reason.

### Force Wrap-Up Reason

For voice channel- If the Force Wrap-Up reason is configured, agents must select a Wrap-Up reason before changing the state after the call ends.
                                 The agent cannot change the state until the Wrap-up reason is applied. The Wrap-Up reason can be selected during the call
                                 or after the call ends.

For digital channels- If the Force Wrap-Up reason is configured, agents must select a Wrap-Up reason before transfering or ending an interaction.

The Force Wrap-Up reason is enabled by default. Use the CLI commands to disable and enable this feature. For more information,
                                             see Desktop Properties .

## Manage Reason Code Conflicts During Upgrade

System Reason Codes are auto-generated reason codes that may conflict with custom reason codes when upgrading from an older
                              version to Cisco Finesse 11.6(1). If there is a reason code conflict then the following message appears when you sign in to
                              the administration console:

Custom reason codes conflict with system reason codes. Resolve to avoid reporting inconsistency .

Clear your browser cache to ensure that you are allowed to view and resolve system reason code conflicts.

When performing an upgrade from an earlier version in a Unified CCE deployment, modify the following custom reason codes:
                                          999, 255, 20001, 20002, 20003, 50041 and 50045. This is done to avoid conflict with the system reason codes.

All conflicting reason codes are highlighted. To edit, select each conflicting reason code and click Edit . The Edit Reason Code area appears. Select the reason code from the available options listed or enter any other code you wish. The code must be
                              unique to the particular category (Not Ready or Sign Out).

Once resolved, the reason code gets sorted based on the reason code number and placed in the table accordingly.

## Predefined System Reason Codes

For Not Ready system reason codes and Sign Out system reason codes, only the reason code label can be edited and saved. The
                              Global attribute and system code cannot be modified. In case the system reason code label is modified and you wish to revert
                              to the default label, refer to the following list of predefined system reason codes:

System Reason Code

Reason Label

Reason Label Description

32767

Not Ready - Call Not Answered

Agent state changed because the agent did not answer the call.

32762

Not Ready - Offhook

The system issues this reason code in the following scenarios:

When the agent goes off-hook to place a call, the Finesse desktop changes the agent status to Not Ready with this reason code.

When the agent is in Ready state and a call is placed from the ACD (Automatic Call Distribution) line, the system issues this
                                                reason code.

Reason Code—50006 is used in place of 32762 in Cisco Finesse Release 12.5(1) when used along with Unified CCE Release 12.5(1)
                                                      or higher.

50001

Logged Out - System Disconnect

The Cisco Finesse client disconnected, logging out the agent.

50002

Logged Out - System Failure

A Cisco Finesse client disconnected, causing the agent to be logged out or set to the Not Ready state. This could be due to
                                          closing the agent desktop application, heart beat time out, or a Cisco Finesse server failure.

50002

Not Ready - Connection Failure

The system issues this reason code when the agent is forcibly logged out in certain cases.

50003

Logged Out - Device Error

Agent was logged out because the Unified CM reported the device out of service.

50004

Logged Out - Inactivity Timeout

Agent was logged out due to agent inactivity as configured in agent desk settings.

50005

Not Ready - Non ACD Busy

For a Unified CCE agent deployment, where the Agent Phone Line Control is enabled in the peripheral and the Non ACD Line
                                          Impact is configured to impact agent state, the agent is set to Not Ready while talking on a call on the Non ACD line with
                                          this reason code.

50006

Not Ready - Offhook

The system issues this reason code in the following scenarios:

When the agent goes off-hook to place a call, the Unified CCE changes the agent status to Not Ready with this reason code.

When the agent is in Ready state and a call is placed from the ACD (Automatic Call Distribution) line, the system issues this
                                                reason code.

This reason code is used from Cisco Finesse Release 12.5(1) along with Unified CCE Release 12.5(1) or higher.

50010

Not Ready - Call Overlap

Agent was set to Not Ready state because the agent was routed two consecutive calls that did not arrive.

50020

Logged Out - Queue Change

Agent was logged out when the agent's skill group dynamically changed on the Administration & Data Server.

50030

Logged Out - Device Conflict

If an agent is logged in to a dynamic device target that is using the same Dialed Number (DN) as the PG static device target,
                                          the agent is logged out.

50040

Logged Out - Mobile Agent Call Fail

Mobile agent was logged out because the call failed.

50041

Not Ready - Mobile Call Not Answered

Mobile agent state changed to Not Ready because the call fails when the mobile agent's phone line rings busy.

50042

Logged Out - Mobile Agent Disconnect

Mobile agent was logged out because the phone line disconnected while using nailed connection mode.

50045

Not Ready - Desktop Reconnect

Desktop reconnected to Finesse.

This reason code is used only to inform CCE about the desktop reconnection. It does not trigger any actual state change and
                                                      therefore is not present in state change events.

65535

Not Ready - System Reinitialized

Agent reinitialized (used if peripheral restarts).

65534

Not Ready - System Reset

PG reset the agent, usually due to a PG failure.

65533

Not Ready - Extension Modified

An administrator modified the agent's extension while the agent was logged in.

20001

Not Ready - Starting Force Logout

Places the agent in the Not Ready state first before forcefully logging them off.

20002

Logged Out - Force Logout

Forces the logout request; for example, when Agent A attempts to log in to Cisco Agent Desktop and Agent B is already logged
                                          in under that agent ID, Agent A is asked whether or not to force the login. If Agent A answers yes, Agent B is logged out
                                          and Agent A is logged in. Reports then show that Agent B logged out at a certain time with a reason code of 20002 (Agent B
                                          was forcibly logged out).

20003

Not Ready - Agent Logout Request

If not already in the Logout state, request is made to place agent in the Not Ready state. Then logout request is made to
                                          log agent out.

999

Not Ready - Supervisor Initiated

The system issues this reason code when the agent’s state is forcibly changed to Not Ready by the Supervisor.

999

Logged Out - Supervisor Initiated

The system issues this reason code when the agent’s state is forcibly changed to Logout by the Supervisor.

255

Logged Out - Connection Failure

The system issues this reason code when the agent is forcibly logged out when there is a connection failure between the Cisco
                                          Finesse Desktop and the Cisco Finesse Server.

## Sign Out Reason Codes

Sign Out reason codes represent reasons that agents can select when they sign out of the Finesse desktop.

Use the Manage Reason Codes (Sign Out) gadget to view, add, edit, or delete Sign Out reason codes. Click the Reason Label
                              or Reason Code headers to sort the Sign Out reason codes by label or by reason code, in ascending or descending order. Click
                              the Type header to sort and display system or custom reason codes. Click the Global header to sort the reason codes by whether
                              they are global (Yes) or not (No).

Sign Out reason codes can be global (visible to all agents) or team (visible only to agents on specified teams).

Finesse supports 200 Sign Out reason codes. These include 100 global Sign Out reason codes, and 100 Sign Out team reason codes.
                                          The team reason codes can be mapped to any team, and the same reason code can be mapped to multiple teams.

The following table describes the fields on the Manage Reason Codes (Sign Out) gadget:

Field

Explanation

Reason Label

The label for the Sign Out reason code.

The label has a maximum length of 40 characters and should be unique for each Sign Out reason code. Alphanumeric and special
                                          characters are supported.

Type

The type of reason code (System or Custom).

The column is default and can be sorted to display both System reason codes and Custom reason codes.

Reason Code

A code for the Sign Out reason.

The code can be any value between 1 and 65535 and must be unique.

Global?

Yes/No. Indicates if the reason code is available globally to all agents (Yes) or to specific teams of agents (No).

Actions on the Manage Reason Codes (Sign Out) gadget:

New: Add a new Sign Out reason code

Edit: Edit an existing Sign Out reason code

Delete: Delete a Sign Out reason code

Refresh: Reload the list of Sign Out reason codes from the server

When you add, edit, or delete a Sign Out reason code, the changes you make take effect on the Finesse desktop after three
                                          seconds. However, agents who are signed in when the changes are made must sign out and sign in again to see those changes
                                          reflected on their desktops.

When an agent clicks Sign Out on the desktop, any configured Sign Out codes appear in a drop-down list. The agent can select
                              the code that represents why that agent is signing out.

### Add Sign Out Reason Code

Step 1

In the Manage Reason Codes (Sign Out) gadget, click New .

Step 2

In the Reason Label box, enter a label for the reason code.

Sign Out reason code labels are limited to 40 characters.

Step 3

In the Reason Code box, an auto populated reason code is displayed. If you choose not to save the prepopulated reason, you
                                          can enter your own reason code.

The code must be between 1 and 65535 and must be unique.

Ensure there are no leading or trailing spaces.

Step 4

If the reason code is global, select the Global? check box. If the reason code is specific to a team, clear the Global? check
                                          box.

By default, the Global? check box is selected.

Step 5

Click Save .

### Edit Sign Out Reason Code

Step 1

In the Manage Reason Codes (Sign Out) gadget, select the reason code that you want to edit.

Step 2

Click Edit .

Step 3

If you want to change the label of the Sign Out reason code, in the Reason Label field, enter a new label for the reason code.
                                          If you want to change the code, in the Reason Code field, enter the new code. If you want to change who has access to the
                                          code, select or clear the Global? check box.

Step 4

Click Save .

### Delete Sign Out Reason Code

An error may occur if an agent selects a Sign Out reason code after it has been deleted. Agents who are signed in when you
                                             make changes to Sign Out reason codes must sign out and sign back in to see those changes reflected on their desktops.

Step 1

In the Manage Reason Codes (Sign Out) gadget, select the Sign Out reason code that you want to delete.

Step 2

Click Delete .

Step 3

Click Yes to confirm the deletion of the selected Sign Out reason code.

## Not Ready Reason Codes

Not Ready reason codes represent reasons that agents can select when they change their state to Not Ready.

Use the Manage Reason Codes (Not Ready) gadget to view, add, edit, or delete Not Ready reason codes.

Click the Reason Label or Reason Code headers to sort the Not Ready reason codes by label or reason code in ascending or descending
                                    order.

Click the Type header to sort and display system or custom reason codes.

Click the Global header to sort reason codes by whether they are global (Yes) or not (No).

Not Ready reason codes can be global (visible to all agents) or team (visible only to agents on specified teams).

Finesse supports a total of 200 Not Ready reason codes. This includes a maximum of 100 global Not Ready reason codes, and
                                          100 team Not Ready reason codes. The team reason codes can be mapped to any team, and the same reason code can be mapped to
                                          multiple teams.

The following table describes the fields on the Manage Reason Codes (Not Ready) gadget:

Field

Explanation

Reason Label

The label for the Not Ready reason code.

The label has a maximum length of 40 characters and should be unique for each Not Ready reason code. Alphanumeric and special
                                          characters are supported.

Type

The type of reason code (System or Custom).

The column is default and can be sorted to display both System reason codes and Custom reason codes.

Reason Code

A code for the Not Ready reason.

The code can be any value between 1 and 65535 and must be unique.

Global?

Yes/No. Indicates if the reason code is available globally to all agents (Yes) or to specific teams of agents (No).

Actions on the Manage Reason Codes (Not Ready) gadget:

New: Add a new Not Ready reason code

Edit: Edit an existing Not Ready reason code

Delete: Delete a Not Ready reason code

Refresh: Reload the list of Not Ready reason codes from the server

When you add, edit, or delete a Not Ready reason code, the changes you make take effect on the Finesse desktop after three
                                          seconds. However, agents who are signed in when the changes are made must sign out and sign back in to see those changes reflected
                                          on their desktops.

When an agent signs in to the Finesse desktop, the agent state is set to Not Ready. The agent can then choose to go to Ready
                              status or choose from one of the configured Not Ready reason codes from the agent state drop-down list.

If an agent wants to change from Ready to Not Ready status, that agent can choose the appropriate Not Ready reason code from
                              the list of configured codes.

An agent who is on a call can select a state to be applied when the call is complete. For example, if an agent wants to be
                              in Not Ready state when the call ends, that agent can choose Not Ready from the drop-down list while still on the call. The
                              Finesse desktop shows the agent in Talking state and a pending state of Not Ready.

If the agent also applies a Not Ready reason code, the desktop shows the pending state with the reason code (in this case,
                              Not Ready - Lunch).

Pending state changes appear on the desktop while the agent's state is Talking (for example, on hold, in a consult call, conference,
                              or silent monitor call).

During a PG or CTI server failover, the pending state of an agent is not retained.

### Add Not Ready Reason Code

Step 1

In the Manage Reason Codes (Not Ready) gadget, click New .

Step 2

In the Reason Label box, enter a label for the reason code.

Not Ready reason code labels are limited to 40 characters.

Step 3

In the Reason Code box, an auto populated reason code is displayed. If you choose not to save the  prepopulated reason code,
                                          you can enter your own reason code.

The code must be between 1 and 65532 and must be unique.

Ensure there are no leading or trailing spaces.

Step 4

If the reason code is global, select the Global? check box. If the reason code is specific to a team, clear the Global? check
                                          box.

By default, the Global? check box is selected.

Step 5

Click Save .

The Finesse server removes leading or trailing spaces before saving the Reason Label in the database.

### Edit Not Ready Reason Code

Step 1

In the Manage Reason Codes (Not Ready) gadget, select the reason code that you want to edit.

Step 2

Click Edit .

Step 3

If you want to change the label for the Not Ready reason code, in the Reason Label field, enter a new label for the reason
                                          code. If you want to change the code, in the Reason Code field, enter the new code. If you want to change who has access to
                                          the code, select or clear the Global? check box.

Step 4

Click Save .

### Delete Not Ready Reason Code

An error may occur if an agent selects a Not Ready reason code after it has been deleted. Agents who are signed in when you
                                             make changes to Not Ready reason codes must sign out and sign back in to see those changes reflected on their desktops.

Step 1

In the Manage Reason Codes (Not Ready) gadget, select the Not Ready reason code that you want to delete.

Step 2

Click Delete .

Step 3

Click Yes to confirm the deletion of the selected reason code.

| Note | Cisco Finesse supports a maximum of 100 global and 1500 team Wrap-Up reasons. No more than 100 Wrap-Up reasons can be assigned
                                          to any one team. |
|---|---|

| Note | The showWrapUpTimer property can be used to show or hide timer in wrap-up state. If showWrapUpTimer is set to true then timer is displayed. If showWrapUpTimer is set to false then timer is hidden. |
|---|---|

| Note | Wrap-Up timer is configurable. By default wrapUpCountDown property is set to true. The timer counts down by default when the agent is in wrap-up state. For more information, see Desktop Properties . For Example, if you set the timer to 30 seconds, by default the timer starts from 30 and ends at zero. The default behavior can be changed by setting the wrapUpCountDown property to false. If an agent is configured for wrap-up and selects a pending state during a call, when the call finishes that agent goes into
                                          wrap-up and not the pending state selected during the call. The agent can end wrap-up by either selecting a new state (Ready
                                          or Not Ready) or letting the wrap-up timer expire. If the agent selects a new state, the new state overrides the pending state
                                          selected during the call. If the wrap-up timer expires, the agent transitions to the pending state. Pending states are not applicable for digital channels. |
|---|---|

| Field | Explanation |
|---|---|
| Reason Label | The label for the Wrap-Up reason. This label must be unique for each Wrap-Up reason and has a maximum length of 39 bytes (which equals 39 US English characters).
                                          Both alphanumeric and special characters are supported. |
| Global? | Yes/No. Indicates if the Wrap-Up reason is available globally to all agents (Yes) or to specific teams of agents (No). |

| Note | When you add, edit, or delete a Wrap-Up reason, the changes you make take effect on the agent or supervisor desktop after
                                          three seconds. However, agents who are signed in when the changes are made must sign out and sign in again to see those changes
                                          reflected on their desktops. |
|---|---|

| Step 1 | In the Manage Wrap-Up Reasons gadget, click New . |
|---|---|
| Step 2 | In the Reason Label field, add a label for the Wrap-Up reason. Note Wrap-Up reason labels are limited to 39 bytes. | Note | Wrap-Up reason labels are limited to 39 bytes. |
| Note | Wrap-Up reason labels are limited to 39 bytes. |
| Step 3 | If the Wrap-Up reason is global, select the Global? check box. If the Wrap-Up reason is specific to a team, clear the Global?
                                          check box. Note By default, the Global? check box is selected. | Note | By default, the Global? check box is selected. |
| Note | By default, the Global? check box is selected. |
| Step 4 | Click Save . |

| Note | Wrap-Up reason labels are limited to 39 bytes. |
|---|---|

| Note | By default, the Global? check box is selected. |
|---|---|

| Step 1 | In the Manage Wrap-Up Reasons gadget, select the Wrap-Up reason that you want to edit. |
|---|---|
| Step 2 | Click Edit . The Edit Wrap-Up Reason area appears. |
| Step 3 | In the Wrap-Up Reason Label field, enter the new label for the Wrap-Up reason. If you want to change who has access to the
                                          Wrap-Up reason, select or clear the Global? check box. |
| Step 4 | Click Save . |

| Step 1 | In the Manage Wrap-Up Reasons gadget, select the Wrap-Up reason that you want to delete. |
|---|---|
| Step 2 | Click Delete . A question appears asking you to confirm that you want to delete the selected Wrap-Up reason. |
| Step 3 | Click Yes to confirm the deletion of the selected Wrap-Up reason. |

| Note | The Force Wrap-Up reason is enabled by default. Use the CLI commands to disable and enable this feature. For more information,
                                             see Desktop Properties . |
|---|---|

| Note | Clear your browser cache to ensure that you are allowed to view and resolve system reason code conflicts. |
|---|---|

| Note | When performing an upgrade from an earlier version in a Unified CCE deployment, modify the following custom reason codes:
                                          999, 255, 20001, 20002, 20003, 50041 and 50045. This is done to avoid conflict with the system reason codes. |
|---|---|

| System Reason Code | Reason Label | Reason Label Description |
|---|---|---|
| 32767 | Not Ready - Call Not Answered | Agent state changed because the agent did not answer the call. |
| 32762 | Not Ready - Offhook | The system issues this reason code in the following scenarios: When the agent goes off-hook to place a call, the Finesse desktop changes the agent status to Not Ready with this reason code. When the agent is in Ready state and a call is placed from the ACD (Automatic Call Distribution) line, the system issues this
                                                reason code. Note Reason Code—50006 is used in place of 32762 in Cisco Finesse Release 12.5(1) when used along with Unified CCE Release 12.5(1)
                                                      or higher. | Note | Reason Code—50006 is used in place of 32762 in Cisco Finesse Release 12.5(1) when used along with Unified CCE Release 12.5(1)
                                                      or higher. |
| Note | Reason Code—50006 is used in place of 32762 in Cisco Finesse Release 12.5(1) when used along with Unified CCE Release 12.5(1)
                                                      or higher. |
| 50001 | Logged Out - System Disconnect | The Cisco Finesse client disconnected, logging out the agent. |
| 50002 | Logged Out - System Failure | A Cisco Finesse client disconnected, causing the agent to be logged out or set to the Not Ready state. This could be due to
                                          closing the agent desktop application, heart beat time out, or a Cisco Finesse server failure. |
| 50002 | Not Ready - Connection Failure | The system issues this reason code when the agent is forcibly logged out in certain cases. |
| 50003 | Logged Out - Device Error | Agent was logged out because the Unified CM reported the device out of service. |
| 50004 | Logged Out - Inactivity Timeout | Agent was logged out due to agent inactivity as configured in agent desk settings. |
| 50005 | Not Ready - Non ACD Busy | For a Unified CCE agent deployment, where the Agent Phone Line Control is enabled in the peripheral and the Non ACD Line
                                          Impact is configured to impact agent state, the agent is set to Not Ready while talking on a call on the Non ACD line with
                                          this reason code. |
| 50006 | Not Ready - Offhook | The system issues this reason code in the following scenarios: When the agent goes off-hook to place a call, the Unified CCE changes the agent status to Not Ready with this reason code. When the agent is in Ready state and a call is placed from the ACD (Automatic Call Distribution) line, the system issues this
                                                reason code. Note This reason code is used from Cisco Finesse Release 12.5(1) along with Unified CCE Release 12.5(1) or higher. | Note | This reason code is used from Cisco Finesse Release 12.5(1) along with Unified CCE Release 12.5(1) or higher. |
| Note | This reason code is used from Cisco Finesse Release 12.5(1) along with Unified CCE Release 12.5(1) or higher. |
| 50010 | Not Ready - Call Overlap | Agent was set to Not Ready state because the agent was routed two consecutive calls that did not arrive. |
| 50020 | Logged Out - Queue Change | Agent was logged out when the agent's skill group dynamically changed on the Administration & Data Server. |
| 50030 | Logged Out - Device Conflict | If an agent is logged in to a dynamic device target that is using the same Dialed Number (DN) as the PG static device target,
                                          the agent is logged out. |
| 50040 | Logged Out - Mobile Agent Call Fail | Mobile agent was logged out because the call failed. |
| 50041 | Not Ready - Mobile Call Not Answered | Mobile agent state changed to Not Ready because the call fails when the mobile agent's phone line rings busy. |
| 50042 | Logged Out - Mobile Agent Disconnect | Mobile agent was logged out because the phone line disconnected while using nailed connection mode. |
| 50045 | Not Ready - Desktop Reconnect | Desktop reconnected to Finesse. Note This reason code is used only to inform CCE about the desktop reconnection. It does not trigger any actual state change and
                                                      therefore is not present in state change events. | Note | This reason code is used only to inform CCE about the desktop reconnection. It does not trigger any actual state change and
                                                      therefore is not present in state change events. |
| Note | This reason code is used only to inform CCE about the desktop reconnection. It does not trigger any actual state change and
                                                      therefore is not present in state change events. |
| 65535 | Not Ready - System Reinitialized | Agent reinitialized (used if peripheral restarts). |
| 65534 | Not Ready - System Reset | PG reset the agent, usually due to a PG failure. |
| 65533 | Not Ready - Extension Modified | An administrator modified the agent's extension while the agent was logged in. |
| 20001 | Not Ready - Starting Force Logout | Places the agent in the Not Ready state first before forcefully logging them off. |
| 20002 | Logged Out - Force Logout | Forces the logout request; for example, when Agent A attempts to log in to Cisco Agent Desktop and Agent B is already logged
                                          in under that agent ID, Agent A is asked whether or not to force the login. If Agent A answers yes, Agent B is logged out
                                          and Agent A is logged in. Reports then show that Agent B logged out at a certain time with a reason code of 20002 (Agent B
                                          was forcibly logged out). |
| 20003 | Not Ready - Agent Logout Request | If not already in the Logout state, request is made to place agent in the Not Ready state. Then logout request is made to
                                          log agent out. |
| 999 | Not Ready - Supervisor Initiated | The system issues this reason code when the agent’s state is forcibly changed to Not Ready by the Supervisor. |
| 999 | Logged Out - Supervisor Initiated | The system issues this reason code when the agent’s state is forcibly changed to Logout by the Supervisor. |
| 255 | Logged Out - Connection Failure | The system issues this reason code when the agent is forcibly logged out when there is a connection failure between the Cisco
                                          Finesse Desktop and the Cisco Finesse Server. |

| Note | Reason Code—50006 is used in place of 32762 in Cisco Finesse Release 12.5(1) when used along with Unified CCE Release 12.5(1)
                                                      or higher. |
|---|---|

| Note | This reason code is used from Cisco Finesse Release 12.5(1) along with Unified CCE Release 12.5(1) or higher. |
|---|---|

| Note | This reason code is used only to inform CCE about the desktop reconnection. It does not trigger any actual state change and
                                                      therefore is not present in state change events. |
|---|---|

| Note | Finesse supports 200 Sign Out reason codes. These include 100 global Sign Out reason codes, and 100 Sign Out team reason codes.
                                          The team reason codes can be mapped to any team, and the same reason code can be mapped to multiple teams. |
|---|---|

| Field | Explanation |
|---|---|
| Reason Label | The label for the Sign Out reason code. The label has a maximum length of 40 characters and should be unique for each Sign Out reason code. Alphanumeric and special
                                          characters are supported. |
| Type | The type of reason code (System or Custom). The column is default and can be sorted to display both System reason codes and Custom reason codes. |
| Reason Code | A code for the Sign Out reason. The code can be any value between 1 and 65535 and must be unique. |
| Global? | Yes/No. Indicates if the reason code is available globally to all agents (Yes) or to specific teams of agents (No). |

| Note | When you add, edit, or delete a Sign Out reason code, the changes you make take effect on the Finesse desktop after three
                                          seconds. However, agents who are signed in when the changes are made must sign out and sign in again to see those changes
                                          reflected on their desktops. |
|---|---|

| Step 1 | In the Manage Reason Codes (Sign Out) gadget, click New . |
|---|---|
| Step 2 | In the Reason Label box, enter a label for the reason code. Note Sign Out reason code labels are limited to 40 characters. | Note | Sign Out reason code labels are limited to 40 characters. |
| Note | Sign Out reason code labels are limited to 40 characters. |
| Step 3 | In the Reason Code box, an auto populated reason code is displayed. If you choose not to save the prepopulated reason, you
                                          can enter your own reason code. Note The code must be between 1 and 65535 and must be unique. Ensure there are no leading or trailing spaces. | Note | The code must be between 1 and 65535 and must be unique. Ensure there are no leading or trailing spaces. |
| Note | The code must be between 1 and 65535 and must be unique. Ensure there are no leading or trailing spaces. |
| Step 4 | If the reason code is global, select the Global? check box. If the reason code is specific to a team, clear the Global? check
                                          box. Note By default, the Global? check box is selected. | Note | By default, the Global? check box is selected. |
| Note | By default, the Global? check box is selected. |
| Step 5 | Click Save . |

| Note | Sign Out reason code labels are limited to 40 characters. |
|---|---|

| Note | The code must be between 1 and 65535 and must be unique. Ensure there are no leading or trailing spaces. |
|---|---|

| Note | By default, the Global? check box is selected. |
|---|---|

| Step 1 | In the Manage Reason Codes (Sign Out) gadget, select the reason code that you want to edit. |
|---|---|
| Step 2 | Click Edit . |
| Step 3 | If you want to change the label of the Sign Out reason code, in the Reason Label field, enter a new label for the reason code.
                                          If you want to change the code, in the Reason Code field, enter the new code. If you want to change who has access to the
                                          code, select or clear the Global? check box. |
| Step 4 | Click Save . |

| Note | An error may occur if an agent selects a Sign Out reason code after it has been deleted. Agents who are signed in when you
                                             make changes to Sign Out reason codes must sign out and sign back in to see those changes reflected on their desktops. |
|---|---|

| Step 1 | In the Manage Reason Codes (Sign Out) gadget, select the Sign Out reason code that you want to delete. |
|---|---|
| Step 2 | Click Delete . |
| Step 3 | Click Yes to confirm the deletion of the selected Sign Out reason code. |

| Note | Finesse supports a total of 200 Not Ready reason codes. This includes a maximum of 100 global Not Ready reason codes, and
                                          100 team Not Ready reason codes. The team reason codes can be mapped to any team, and the same reason code can be mapped to
                                          multiple teams. |
|---|---|

| Field | Explanation |
|---|---|
| Reason Label | The label for the Not Ready reason code. The label has a maximum length of 40 characters and should be unique for each Not Ready reason code. Alphanumeric and special
                                          characters are supported. |
| Type | The type of reason code (System or Custom). The column is default and can be sorted to display both System reason codes and Custom reason codes. |
| Reason Code | A code for the Not Ready reason. The code can be any value between 1 and 65535 and must be unique. |
| Global? | Yes/No. Indicates if the reason code is available globally to all agents (Yes) or to specific teams of agents (No). |

| Note | When you add, edit, or delete a Not Ready reason code, the changes you make take effect on the Finesse desktop after three
                                          seconds. However, agents who are signed in when the changes are made must sign out and sign back in to see those changes reflected
                                          on their desktops. |
|---|---|

| Note | During a PG or CTI server failover, the pending state of an agent is not retained. |
|---|---|

| Step 1 | In the Manage Reason Codes (Not Ready) gadget, click New . |
|---|---|
| Step 2 | In the Reason Label box, enter a label for the reason code. Note Not Ready reason code labels are limited to 40 characters. | Note | Not Ready reason code labels are limited to 40 characters. |
| Note | Not Ready reason code labels are limited to 40 characters. |
| Step 3 | In the Reason Code box, an auto populated reason code is displayed. If you choose not to save the  prepopulated reason code,
                                          you can enter your own reason code. Note The code must be between 1 and 65532 and must be unique. Ensure there are no leading or trailing spaces. | Note | The code must be between 1 and 65532 and must be unique. Ensure there are no leading or trailing spaces. |
| Note | The code must be between 1 and 65532 and must be unique. Ensure there are no leading or trailing spaces. |
| Step 4 | If the reason code is global, select the Global? check box. If the reason code is specific to a team, clear the Global? check
                                          box. Note By default, the Global? check box is selected. | Note | By default, the Global? check box is selected. |
| Note | By default, the Global? check box is selected. |
| Step 5 | Click Save . Note The Finesse server removes leading or trailing spaces before saving the Reason Label in the database. | Note | The Finesse server removes leading or trailing spaces before saving the Reason Label in the database. |
| Note | The Finesse server removes leading or trailing spaces before saving the Reason Label in the database. |

| Note | Not Ready reason code labels are limited to 40 characters. |
|---|---|

| Note | The code must be between 1 and 65532 and must be unique. Ensure there are no leading or trailing spaces. |
|---|---|

| Note | By default, the Global? check box is selected. |
|---|---|

| Note | The Finesse server removes leading or trailing spaces before saving the Reason Label in the database. |
|---|---|

| Step 1 | In the Manage Reason Codes (Not Ready) gadget, select the reason code that you want to edit. |
|---|---|
| Step 2 | Click Edit . |
| Step 3 | If you want to change the label for the Not Ready reason code, in the Reason Label field, enter a new label for the reason
                                          code. If you want to change the code, in the Reason Code field, enter the new code. If you want to change who has access to
                                          the code, select or clear the Global? check box. |
| Step 4 | Click Save . |

| Note | An error may occur if an agent selects a Not Ready reason code after it has been deleted. Agents who are signed in when you
                                             make changes to Not Ready reason codes must sign out and sign back in to see those changes reflected on their desktops. |
|---|---|

| Step 1 | In the Manage Reason Codes (Not Ready) gadget, select the Not Ready reason code that you want to delete. |
|---|---|
| Step 2 | Click Delete . |
| Step 3 | Click Yes to confirm the deletion of the selected reason code. |