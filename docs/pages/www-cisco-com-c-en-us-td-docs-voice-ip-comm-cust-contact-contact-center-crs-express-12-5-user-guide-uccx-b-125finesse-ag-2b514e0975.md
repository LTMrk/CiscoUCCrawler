---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-crs-express-12-5-user-guide-uccx-b-125finesse-ag-2b514e0975
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/crs/express_12_5/user/guide/uccx_b_125finesse-agent-supervisor-desktop-guide/uccx_b_125finesse-agent-supervisor-desktop-guide_appendix_01001.html
retrieved_at: 2026-08-16T21:25:22.193318+00:00
---

Cisco Finesse Agent and Supervisor Desktop User Guide for Cisco Unified Contact Center Express, Release 12.5(1)

# Cisco Finesse Agent and Supervisor Desktop User Guide for Cisco Unified Contact Center Express, Release 12.5(1)

Updated: February 9, 2020

Chapter: Chat - Customer Experience

## Chapter: Chat - Customer Experience

# Chat - Customer Experience

This appendix descibes the experience of the customer who uses the chat functionality.

## Bubble Chat Experience

Bubble chat can be launched on any device and the display adapts to the screen size of the device used. For example, if you
                              launch the bubble chat using a desktop, a small chat pop-over appears on the right-side bottom of the web page. If you use
                              a mobile device, the bubble chat launches in the full-screen mode.

The browser cookies and third-party cookies are enabled.

The Tracking Protection option in the browser is disabled.

The Customer Collaboration Platform server and customer website are in the same domain so that the bubble chat works on various browsers.

For more information about cookies and Tracking Protection option, see your browser-specific documentation.

The chat process is as follows:

The customer initiates the chat by clicking a text link, button, or icon.

The chat form attempts to collect the details of the customer, such as, name, email, phone number etc. The form also presents
                                    a list of problem statements - from which the customer has to mandatorily select one.

The customer provides details in the chat form and submits it.

The chat pop-over opens with a welcome message, such as 'Thanks for contacting. We will be with you shortly'. If all the agents
                                    are busy, an appropriate message appears.

When the agent joins the chat, the customer is notified by a message, and the pop-over divides into a conversation area (where
                                    messages appear) and a typing area (where the customer can type messages for the agent).

The customer and agent chat - more than one agent can join the chat to create a group chat. While chatting, the agent's messages
                                    are displayed on the left of the conversation area and the customer's messages are displayed on the right. All messages are
                                    displayed with the timestamp below the message (in the 24-hour format); the agent's message will additionally have the agent's
                                    name before the timestamp.

The chat pop-over can be minimized or maximized.

The following indicators appear on the chat pop-over at appropriate times:

Agent typing indicator: This indicator, represented by three squiggly dots, appears above the typing area whenever the agent
                                          types.

New messages indicator: The pop-over blinks in a minimized stated whenever a new event occurs during the chat, such as the
                                          receipt of a new message, joining of another agent, connection problems etc.

Agent left/joined indicator: The customer is informed when an agent leaves or joins the chat.

When the customer completes the chat and attempts to exit the chat, the following pop-ups are displayed in a sequence:

A chat closure confirmation box.

A chat transcript download box. The customer can choose to download the chat transcript.

A chat rating box, if rating is enabled for the chat. The customer can choose to rate or skip rating by closing this box.

Any connectivity or technical problems that are encountered during the chat session are notified as banner messages at the
                                          top of the conversation area.

## Agent Reports

### Agent CSQ Statistics
                           	 Report

The Agent CSQ Statistics Report presents the current day's call queue
                                 		  statistics, since midnight, of the Contact Service Queues (CSQ) to which the
                                 		  agent is associated.

#### Charts

None

#### Fields

The report includes a table that displays the following information:

Field

Description

Agent ID

Login ID of the agent.

CSQ Name

Name of the CSQ.

Calls Waiting

Number of calls in queue for a CSQ.

Longest Call in Queue

Elapsed wait time of the oldest call in the queue.

#### Filter Criteria

You can filter using the following parameter:

Filter parameter

Result

Team Name

Displays information for the CSQs that belong to the
                                             						specified teams.

#### Grouping Criteria

None

### Recent State
                           	 History Report

The
                                 		  Recent State History Report presents the agent state and duration in that state
                                 		  and the reason (where applicable) for the current day, since midnight.

#### Charts

None

#### Fields

The report
                                 		  includes a table that displays the following information:

Field

Description

Agent ID

Login ID of the agent.

This field is not listed in Gadget View.

Start
                                             						Time

Time the
                                             						agent state is initiated.

State

State of
                                             						the agent—Login, Logout, Not Ready, Ready, Reserved, Talking, or Work.

Reason

The reason selected by the agent moving to Logout state or Not Ready state. This displays the reason code if the reason label
                                             is unavailable. A blank is due to any one of the following:

No logout reason code is configured.

Agent was unable to enter a reason.

Reason codes for all other states except Not Ready and Logout.

To view
                                             						a list of reason codes and their descriptions, see the "Predefined" reason codes section below.

Duration

Time
                                             						duration that the agent was in that state.

Finesse Desktop client machines should be time synchronized with a reliable NTP server for the correct updates to the Duration
                                                         fields within Live Data reports.

#### Filter
                                 		  Criteria

You can filter
                                 		  using the following parameter:

Filter parameter

Result

Agent ID

Displays
                                             						information for the agents who belong to the specified teams.

#### Grouping
                                 		  Criteria

None

#### Predefined
                                 		  Reason Codes

Reason Code

State

Event

Event Description

22

Logout

SUP_AGT_TO_LOGOUT

Supervisor changes an agent’s state to Logout.

33

Ready/Not Ready

SUP_AGT_TO_READY/SUP_AGT_TO_NOT READY

Supervisor changes an agent’s state to either Ready or Not Ready.

255

Logout

—

The system issues this reason code when the agent is forcibly logged out when there is a connection failure between the Cisco
                                             Finesse Desktop and the Cisco Finesse Server.

32741

Logout

ICD_EXTENSION_CONFLICT

If an agent has already logged in and another agent tries to login with the same extension number, then the previously logged
                                             in agent will be logged out by the system.

32742

Not Ready

AGT_SEC_LINE_OFFHOOK

Agent's state is changed from Ready state to Not Ready state when the monitored Non ICD lines are used for Incoming or Outgoing
                                             calls.

32745

OUTBOUND

OUTBOUND_WORK_REASONCODE

This reason code is set when an agent goes into the Work state to select a wrap up code after ending an outbound call.

32746

OUTBOUND

AGENT_RESERVED_OUTBOUND_DIRECTPREVIEW

This reason code is set when an agent goes into a Reserved state for a direct preview outbound call.

32747

OUTBOUND

AGENT_RESERVED_OUTBOUND

This reason code is set when an agent goes into a Reserved state for an agent progressive or predictive outbound call.

32748

Logout

AGENT_DELETED

Agent is logged out from Unified CCX as the agent is deleted from Unified Communications Manager. This event is triggered
                                             when Unified CCX synchronizes the agent information with Unified Communications Manager.

32749

Not Ready

CANCEL_FEATURE

Agent's state changes from Talking to Not Ready because the Cancel feature is triggered during an Interactive Call Distribution
                                             (ICD) consult call between two agents.

When the consulting agent presses the Cancel softkey on the phone, the consulted agent is no longer associated with the ICD call, and the consulted agent's state changes
                                             to Not Ready. This feature is available only on some of the newer phones.

32750

Not Ready

AGT_IPCC_EXT_ CHANGED

Agent is logged out from Unified CCX because the agent’s Unified CCX extension changes in Unified Communications Manager.

32751

Ready

AGENT_SKIPS

Agent receives a preview outbound call and skips the call.

32752

Ready

CANCEL_RESERVATION

Agent receives a preview outbound call, decides to cancel the reservation, and presses the Cancel Reservation button on the desktop.

32753

Not Ready

LINE_RESTRICTED

Agent’s phone line is flagged as a restricted device by the administrator of Unified Communications Manager.

If Allow Control of Device from CTI is not checked in the Default Device Profile Configuration window in Unified Communications Manager, the line remains restricted and cannot be controlled. You can modify this setting
                                             for devices that register with Unified Communications Manager. See the Cisco Unified
                                                      				  Communications Manager Administration Guide , located at: https://www.cisco.com/en/US/products/sw/voicesw/ps556/prod_maintenance_guides_list.html .

32754

Not Ready

DEVICE_RESTRICTED

Agent's device is flagged as a restricted device by the administrator of Unified Communications Manager.

If Allow Control of Device from CTI is not checked in the Default Device Profile Configuration window in Unified Communications Manager, the device remains restricted and cannot be controlled. You can modify this setting
                                             for devices that register with Unified Communications Manager. See the Cisco Unified
                                                      				  Communications Manager Administration Guide , located at: https://www.cisco.com/en/US/products/sw/voicesw/ps556/prod_maintenance_guides_list.html .

32755

Not Ready

CALL_ENDED

Agent moves to Not Ready state after handling a Unified CCX call. This event occurs in the following cases:

Agent 1 is in Not Ready state and gets a consult call from Agent 2. After handling the call, Agent 1 moves back to Not Ready
                                                   state.

The Automatic Available option is disabled for the agent. After handling a call, agent moves to Not Ready state.

32756

Not Ready

PHONE_UP

Agent’s phone becomes active after it was in Phone Down state.

32757

Not Ready

CM_FAILOVER

Unified Communications Manager fails over, and the agent is moved to Not Ready state.

32758

Not Ready

WORK_TIMER_EXP

Agent’s state changes from Work to Not Ready. This change occurs if the Work state for that agent’s CSQ is associated with
                                             an expired wrap-up timer.

32759

Not Ready

PHONE_DOWN

Agent’s phone stops functioning and the agent is placed in the Unavailable state.

32760

Not Ready

AGT_LOGON

Agent logs in and is automatically placed in the Not Ready state.

32761

Not Ready

AGT_RCV_NON_ICD

Agent is logged in to the desktop or IP phone and receives a call that is not queued on the Unified CCX platform.

32762

Not Ready

AGT_OFFHOOK

Agent goes off hook to place a call. If the agent enters a reason, that reason is displayed. If the agent does not select
                                             any reason, the system issues this reason code.

32763

Not Ready

AGT_RNA

Agent fails to answer a Unified CCX call within the specified timeout period.

32764

Logout

CRS_FAILURE

Active server becomes the standby server, and the agent loses connection to the Unified CCX platform.

32765

Logout

CONNECTION_DOWN

IP Phone Agent or desktop stops functioning, or connection is disrupted.

32766

Logout

CLOSE_FINESSE_DESKTOP

Agent manually logs out from the Finesse Desktop using the default Logout (without any custom reason label) option.

32767

Logout

AGT_RELOGIN

Agent is logged in to one device (computer or phone) and tries to log in to a second device.

### Recent Call
                           	 History Report

The
                                 		  Recent call History Report presents the recent call history details like the
                                 		  start time, duration of the call, type of call, phone number, contact
                                 		  disposition, queue and Wrap-Up reasons for the current day, since midnight.

The following call based scenarios are not reported:

Consult calls between any two agents.

Outbound campaign calls and any such type of calls that were transferred or conferenced.

#### Charts

None

#### Fields

The report
                                 		  includes a table that displays the following information:

Field

Description

Agent ID

Login ID
                                             						of the agent.

Type

Type of
                                             						the call. For example, Inbound or Outbound.

Number

Phone
                                             						number of the call.

To view
                                             						a list of reason codes and their descriptions, see the "Predefined" reason codes section below.

Disposition

Contact
                                             						disposition type of the call.

Wrap-Up
                                             						Reason

Wrap-Up
                                             						Reasons entered by the agent.

Queue

Queue
                                             						details that the call was routed to.

Start
                                             						Time

Start
                                             						time of the call.

Duration

Time
                                             						duration of the call.

Finesse Desktop client machines should be time synchronized with a reliable NTP server for the correct updates to the Duration
                                                         fields within Live Data reports.

#### Filter
                                 		  Criteria

You can filter
                                 		  using the following parameter:

Filter parameter

Result

Agent ID

Displays
                                             						information for the agents who belong to the specified teams.

#### Grouping
                                 		  Criteria

None

### Agent Statistics
                           	 Report

The Agent Statistics Report presents performance statistics of the
                                 		  agents for the current day, since midnight.

#### Charts

None

#### Fields

The report includes a table that display the following information:

Field

Description

Agent ID

Login ID of the agent.

Calls Offered

Calls sent to the agent, regardless of whether the agent picks up the call.

Calls Handled

Calls connected to the agent.

Talk Time—Avg

Average time the agent spent in Talking state.

Average talk time = Total time in Talking state / Calls handled

Talk Time—Max

Longest time the agent spent in Talking state.

Talk Time—Total

Total time the agent spent in Talking state.

Hold Time—Avg

Average time the agent put the calls on hold.

Average hold time = Total time the calls were on hold / Calls handled

Hold Time—Max

Longest time the agent put a call on hold.

Hold Time—Total

Total time the agent put the calls on hold.

Ready—Avg

Average time the agent spent in Ready state.

Average ready time = Total time the agent spent in Ready state / Number of times the agent moved to Ready state

Ready—Max

Longest time the agent spent in Ready state.

Ready—Total

Total time the agent spent in Ready state.

Not Ready—Avg

Average time the agent spent in Not Ready state.

Average not ready time = Total time the agent spent in Not Ready state / Number of times the agent moved to Not Ready state

Not Ready—Max

Longest time the agent spent in Not Ready state.

Not Ready—Total

Total time the agent spent in Not Ready state.

After Call Work—Avg

Average time the agent spent in Work state.

Average work time = Total time in Work state / Calls completed

After Call Work—Max

Longest time the agent spent in Work state.

After Call Work—Total

Total time the agent spent in Work state.

#### Filter Criteria

You can filter using the following parameter:

Filter parameter

Result

Agent ID

Displays information for the agents who belong to the
                                             						specified teams.

#### Grouping Criteria

None

### Agent Team Summary
                           	 Report

The
                                 		  Agent Team Summary Report presents the agent state and the reason (where
                                 		  applicable). An agent can view details of all the agents in the team.

#### Charts

None

#### Fields

The report
                                 		  includes a table that displays the following information:

Field

Description

Agent
                                             						Name

First
                                             						name and last name of the agent.

State

State of
                                             						the agent—Logged-In, Logout, Not Ready, Ready, Reserved, Talking, or Work.

Reason

The reason selected by the agent when moving to Logout state
                                             						or Not Ready state. This displays the reason code if the reason is unavailable.
                                             						A blank is due to one of the following:

No logout reason code is configured.

Agent was unable to select a reason.

Reason codes for all other states except Not Ready and Logout.

To view
                                             						a list of reason codes and their descriptions, see the "Predefined" reason codes section below.

#### Filter
                                 		  Criteria

You can filter
                                 		  using the following parameter:

Filter parameter

Result

Agent ID

Displays
                                             						information for the agents who belong to the specified teams.

#### Grouping
                                 		  Criteria

None

#### Predefined
                                 		  Reason Codes

Reason Code

State

Event

Event Description

22

Logout

SUP_AGT_TO_LOGOUT

Supervisor changes an agent’s state to Logout.

33

Ready/Not Ready

SUP_AGT_TO_READY/SUP_AGT_TO_NOT READY

Supervisor changes an agent’s state to either Ready or Not Ready.

255

Logout

—

The system issues this reason code when the agent is forcibly logged out when there is a connection failure between the Cisco
                                             Finesse Desktop and the Cisco Finesse Server.

32741

Logout

ICD_EXTENSION_CONFLICT

If an agent has already logged in and another agent tries to login with the same extension number, then the previously logged
                                             in agent will be logged out by the system.

32742

Not Ready

AGT_SEC_LINE_OFFHOOK

Agent's state is changed from Ready state to Not Ready state when the monitored Non ICD lines are used for Incoming or Outgoing
                                             calls.

32745

OUTBOUND

OUTBOUND_WORK_REASONCODE

This reason code is set when an agent goes into the Work state to select a wrap up code after ending an outbound call.

32746

OUTBOUND

AGENT_RESERVED_OUTBOUND_DIRECTPREVIEW

This reason code is set when an agent goes into a Reserved state for a direct preview outbound call.

32747

OUTBOUND

AGENT_RESERVED_OUTBOUND

This reason code is set when an agent goes into a Reserved state for an agent progressive or predictive outbound call.

32748

Logout

AGENT_DELETED

Agent is logged out from Unified CCX as the agent is deleted from Unified Communications Manager. This event is triggered
                                             when Unified CCX synchronizes the agent information with Unified Communications Manager.

32749

Not Ready

CANCEL_FEATURE

Agent's state changes from Talking to Not Ready because the Cancel feature is triggered during an Interactive Call Distribution
                                             (ICD) consult call between two agents.

When the consulting agent presses the Cancel softkey on the phone, the consulted agent is no longer associated with the ICD call, and the consulted agent's state changes
                                             to Not Ready. This feature is available only on some of the newer phones.

32750

Not Ready

AGT_IPCC_EXT_ CHANGED

Agent is logged out from Unified CCX because the agent’s Unified CCX extension changes in Unified Communications Manager.

32751

Ready

AGENT_SKIPS

Agent receives a preview outbound call and skips the call.

32752

Ready

CANCEL_RESERVATION

Agent receives a preview outbound call, decides to cancel the reservation, and presses the Cancel Reservation button on the desktop.

32753

Not Ready

LINE_RESTRICTED

Agent’s phone line is flagged as a restricted device by the administrator of Unified Communications Manager.

If Allow Control of Device from CTI is not checked in the Default Device Profile Configuration window in Unified Communications Manager, the line remains restricted and cannot be controlled. You can modify this setting
                                             for devices that register with Unified Communications Manager. See the Cisco Unified
                                                      				  Communications Manager Administration Guide , located at: https://www.cisco.com/en/US/products/sw/voicesw/ps556/prod_maintenance_guides_list.html .

32754

Not Ready

DEVICE_RESTRICTED

Agent's device is flagged as a restricted device by the administrator of Unified Communications Manager.

If Allow Control of Device from CTI is not checked in the Default Device Profile Configuration window in Unified Communications Manager, the device remains restricted and cannot be controlled. You can modify this setting
                                             for devices that register with Unified Communications Manager. See the Cisco Unified
                                                      				  Communications Manager Administration Guide , located at: https://www.cisco.com/en/US/products/sw/voicesw/ps556/prod_maintenance_guides_list.html .

32755

Not Ready

CALL_ENDED

Agent moves to Not Ready state after handling a Unified CCX call. This event occurs in the following cases:

Agent 1 is in Not Ready state and gets a consult call from Agent 2. After handling the call, Agent 1 moves back to Not Ready
                                                   state.

The Automatic Available option is disabled for the agent. After handling a call, agent moves to Not Ready state.

32756

Not Ready

PHONE_UP

Agent’s phone becomes active after it was in Phone Down state.

32757

Not Ready

CM_FAILOVER

Unified Communications Manager fails over, and the agent is moved to Not Ready state.

32758

Not Ready

WORK_TIMER_EXP

Agent’s state changes from Work to Not Ready. This change occurs if the Work state for that agent’s CSQ is associated with
                                             an expired wrap-up timer.

32759

Not Ready

PHONE_DOWN

Agent’s phone stops functioning and the agent is placed in the Unavailable state.

32760

Not Ready

AGT_LOGON

Agent logs in and is automatically placed in the Not Ready state.

32761

Not Ready

AGT_RCV_NON_ICD

Agent is logged in to the desktop or IP phone and receives a call that is not queued on the Unified CCX platform.

32762

Not Ready

AGT_OFFHOOK

Agent goes off hook to place a call. If the agent enters a reason, that reason is displayed. If the agent does not select
                                             any reason, the system issues this reason code.

32763

Not Ready

AGT_RNA

Agent fails to answer a Unified CCX call within the specified timeout period.

32764

Logout

CRS_FAILURE

Active server becomes the standby server, and the agent loses connection to the Unified CCX platform.

32765

Logout

CONNECTION_DOWN

IP Phone Agent or desktop stops functioning, or connection is disrupted.

32766

Logout

CLOSE_FINESSE_DESKTOP

Agent manually logs out from the Finesse Desktop using the default Logout (without any custom reason label) option.

32767

Logout

AGT_RELOGIN

Agent is logged in to one device (computer or phone) and tries to log in to a second device.

## Supervisor Reports

### Agent Outbound
                           	 Team Summary Report

The Agent Outbound Team Summary Report provides performance statistics of the agents in the team for direct preview, progressive,
                                 and predictive outbound campaigns. The following two views are available for this report:

Short and Long Term Average —Provides the performance statistics of the agents who handle outbound calls for the current day based on short term and long
                                       term values.

Since Midnight —Provides the performance statistics of the agents in the team who handle outbound calls for the current day, beginning at
                                       midnight.

Your administrator can set the short term value to 5, 10, or 15 minutes.

Long term value is set to 30 minutes.

#### Charts

None

#### Fields

The following view-wise tables are included in the report.

Field

Description

Agent Name

First name and last name of the agent.

Agent ID

Login ID of the agent.

Average Talk Time—Short Term

Average time the agent spent in Talking state for outbound calls in the last 5, 10, or 15 minutes.

Average Talk Time—Long Term

Average time the agent spent in Talking state for outbound calls in the last 30 minutes.

Average Hold Time—Short Term

Average time the agent put the outbound calls on hold in the last 5, 10, or 15 minutes.

Average Hold Time—Long Term

Average time the agent put the outbound calls on hold in the last 30 minutes.

Field

Description

Agent Name

First name and last name of the agent.

Agent ID

Login ID of the agent.

Talk Time—Avg

Average time the agent spent in Talking state for outbound calls.

Average talk time = Total time in Talking state / calls handled

Talk Time—Max

Longest time the agent spent in Talking state for outbound calls.

Talk Time—Total

Total time the agent spent in Talking state for outbound calls.

Hold Time—Avg

Average time the agent put the outbound calls on hold.

Average hold time = Total time calls were put on hold / calls handled

Hold Time—Max

Longest time the agent put an outbound call on hold.

Hold Time—Total

Total time the agent put the outbound calls on hold.

After Call Work Time—Avg

Average time the agent spent in Work state for outbound calls.

Average work time = Total time in Work state / calls completed

After Call Work Time—Max

Longest time the agent spent in Work state for outbound calls.

After Call Work Time—Total

Total time the agent spent in Work state for outbound calls.

#### Filter Criteria

You can filter using the following parameter:

Filter Parameter

Result

Agent ID

Displays information for the agents who belong to the
                                             						specified teams.

#### Grouping Criteria

None

### Chat Agent
                           	 Statistics Report

The Chat Agent
                                 		  Statistics Report provides agent statistics.

#### Charts

None

#### Fields

The report includes a table that displays the following information:

Visible fields—These fields are displayed in the report.

Hidden fields—These fields are not displayed in the report. You can customize the report to display these fields. For more
                                       information, see the Cisco Unified Contact
                                                				  Center Express Report User Guide , located at:

https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-express/products-user-guide-list.html .

Field

Description

Agent Name

First name
                                             					 and last name of the agent.

Agent ID

Login ID
                                             					 of the agent.

Current
                                             					 State

State of
                                             					 the agent—Logged-In, Logout, Not Ready, Ready, Partial Busy, Busy, Reserved.

Duration

Time that
                                             					 the agent spent in the current state.

Finesse Desktop client machines should be time synchronized with a reliable NTP server for the correct updates to the Duration
                                                         fields within Live Data reports.

Current
                                             					 Active Contacts

Number of
                                             					 contacts that the agent is handling.

Contacts
                                             					 Presented

Number of
                                             					 contacts that are offered to the agent since midnight.

Contacts
                                             					 Handled

Number of
                                             					 contacts that are handled by the agent since midnight. A contact is marked
                                             					 handled if a contact is connected to an agent.

Contacts
                                             					 Abandoned

Number of
                                             					 contacts that are routed to the CSQ since midnight but are not answered by an
                                             					 agent, because the customer ends the chat or the customer is disconnected.

This also includes the number of group chats that were
                                             					 abandoned when these were routed to a CSQ. They are abandoned when the group
                                             					 chat is not accepted by the second agent. This can be due to, either the chat
                                             					 submitter or the first agent ended the chat before the second agent accepted or
                                             					 was disconnected.

Contacts
                                             					 RNA

Number of
                                             					 contacts that the agent did not answer since midnight. Ring-no-answer (RNA).

Contacts
                                             					 Declined

Number of
                                             					 group chat contacts that are declined by the agent since midnight.

Field

Description

Login
                                             					 Duration

Elapsed
                                             					 time between the login time and the logout time since midnight.

CSQs
                                             					 Serving

List of
                                             					 CSQs that the agent is serving.

Agent
                                             					 Utilization—Not Ready

Percentage
                                             					 of time that the agent spent in Not Ready state since midnight. It is
                                             					 calculated every minute and is one of the components that add up to the agent's
                                             					 total login duration.

Agent
                                             					 Utilization—Ready

Percentage
                                             					 of time that the agent spent in Ready state since midnight. It is calculated
                                             					 every minute and is one of the components that add up to the agent's total
                                             					 login duration.

Agent
                                             					 Utilization—Partial Busy

Percentage of time that the agent spent in Partial Busy state
                                             					 since midnight. It is calculated every minute and is one of the components that
                                             					 add up to the agent's total login duration.

Agent
                                             					 Utilization—Busy

Percentage of time that the agent spent in Busy state since
                                             					 midnight. It is calculated every minute and is one of the components that add
                                             					 up to the agent's total login duration.

#### Filter
                                 		  Criteria

You can filter
                                 		  using the following parameter:

Filter Parameter

Result

Agent
                                             						ID

Displays information for the agents who belong to the specified
                                             						teams.

#### Grouping
                                 		  Criteria

None

### Chat CSQ Summary
                           	 Report

The Chat CSQ Summary Report provides agent statistics and contact
                                 		  statistics for a Contact Service Queue (CSQ).

#### Charts

None

#### Fields

The report includes a table that displays the following information:

Visible fields—These fields are displayed in the report.

Hidden fields—These fields are not displayed in the report. You can customize the report to display these fields. For more
                                       information, see the Cisco Unified Contact
                                                				  Center Express Report User Guide , located at:

http://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-express/products-user-guide-list.html .

Field

Description

CSQ Name

Name of the CSQ.

Contacts Waiting

Number of contacts in queue for a CSQ.

Agents—Logged-In

Number of agents in Logged-In state.

Agents—Not Ready

Number of agents in Not Ready state.

Agents—Ready

Number of agents in Ready state.

Agents—Partial Busy

Number of agents in Partial Busy state. An agent is set to
                                             					 Partial Busy state when the agent has not reached the maximum number of chat
                                             					 sessions that is set by the administrator.

Agents—Busy

Number of agents in Busy state. An agent is set to Busy state
                                             					 when the agent reaches the maximum number of chat sessions that is set by the
                                             					 administrator.

Agents—Reserved

Number of agents in Reserved state.

Field

Description

Contacts Total

Number of contacts routed to the CSQ since midnight.

Contacts Handled

Number of contacts that are handled by the CSQ since midnight.
                                             					 A contact is marked handled if a contact is connected to an agent while queued
                                             					 for this CSQ.

Contacts Abandoned

Number of contacts that are routed to the CSQ since midnight
                                             					 but are not answered by an agent, because the customer ends the chat or the
                                             					 customer is disconnected.

#### Filter Criteria

You can filter using the following parameter:

Filter Parameter

Result

Queue Name

Displays information for the CSQs that belong to the
                                             						specified queues.

#### Grouping Criteria

None

### Email Agent Statistics Report

The Email Agent Statistics Report provides the email statistics of the agents.

#### Charts

None

#### Fields

The report includes a table that displays the following information:

Visible fields—These fields are displayed in the report.

Hidden fields—These fields are not displayed in the report. You can customize the report to display these fields. For more
                                       information, see the Cisco Unified Contact Center Express Report User Guide , located at:

https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-express/products-user-guide-list.html .

Field

Description

Agent Name

First name and last name of the agent.

Agent ID

Login ID of the agent.

State

State of the agent—Not Ready, Ready, Partial Busy, Busy, Reserved.

Duration

Time that the agent spent in the current state.

Finesse Desktop client machines should be time synchronized with a reliable NTP server for the correct updates to the Duration
                                                         fields within Live Data reports.

Active Emails

Number of email messages that the agent is handling.

Emails Presented

The number of emails that are presented include new and requeued emails.

Emails Handled

Number of email messages that are handled by the agent since midnight.

Emails Discarded

Number of email messages discarded by the agent or by the system during service disruption. The system discarded emails would
                                             be reinjected into the system when the service is restored.

Emails Requeued

Number of email messages that the agent requeued since midnight.

Field

Description

Login Duration

Elapsed time between the login time and the logout time since midnight.

CSQs Serving

List of CSQs that the agent is serving.

Agent Utilization—Not Ready

Percentage of time that the agent spent in Not Ready state since midnight. It is calculated every minute and is one of the
                                             components that add up to the agent's total login duration.

Agent Utilization—Ready

Percentage of time that the agent spent in Ready state since midnight. It is calculated every minute and is one of the components
                                             that add up to the agent's total login duration.

Agent Utilization—Partial Busy

Percentage of time that the agent spent in Partial Busy state since midnight. It is calculated every minute and is one of
                                             the components that add up to the agent's total login duration.

Agent Utilization—Busy

Percentage of time that the agent spent in Busy state since midnight. It is calculated every minute and is one of the components
                                             that add up to the agent's total login duration.

Agent Utilization—Reserved

Percentage of time that the agent spent in Reserved state since midnight. It is calculated every minute and is one of the
                                             components that add up to the agent's total login duration.

#### Filter Criteria

You can filter using the following parameter:

Filter Parameter

Result

Agent ID

Displays information for the agents who belong to the specified teams.

#### Grouping Criteria

None

### Email CSQ Summary
                           	 Report

The Email CSQ Summary Report presents the email activity summary of
                                 		  agents in a Contact Service Queue (CSQ).

#### Charts

None

#### Fields

The report includes a table that displays the following information:

Visible fields—These fields are displayed in the report.

Hidden fields—These fields are not displayed in the report. You can customize the report to display these fields. For more
                                       information, see the Cisco Unified Contact Center Express Report User Guide , located at:

https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-express/products-user-guide-list.html .

Field

Description

CSQ Name

Name of the Email CSQ.

Emails in Queue

Emails in Process

Number of email messages that are assigned to agents.

Emails Discarded

Number of email messages that have been discarded, both by agents and due to service disruptions.

Agents-Logged In

Number of agents in Logged-In state.

Agents-Not Ready

Number of agents in Not Ready state.

Agents-Ready

Number of agents in Ready state.

Agents-Partial Busy

Number of agents in Partial Busy state. Agents are set to Partial Busy state as soon as an email is assigned to them. They
                                             will continue to be in this state until they clear all the emails assigned to them or the state changes to Busy.

Agents-Busy

Number of agents in Busy state. Agents are set to Busy state when the number of emails reach the maximum limit set. Agents
                                             state is changed to Partial Busy as soon as the number of assigned email messages is one less than the maximum limit set.

Field

Description

Emails Total

Number of email messages routed to the CSQ since midnight.

Emails Handled

Number of email messages that are handled by the CSQ since
                                             					 midnight. An email is marked handled if it is responded by an agent while
                                             					 queued for this CSQ.

#### Filter Criteria

You can filter using the following parameter:

Filter Parameter

Result

Queue Name

Displays information for the CSQs that belong to the
                                             						specified queues.

#### Grouping Criteria

None

### Team State
                           	 Report

The Team State Report presents each agent state and the time spent in
                                 		  a state. The supervisor can see agents of all the assigned teams.

#### Charts

None

#### Fields

The report includes a table that displays the following information:

Field

Description

Agent Name

First name and last name of the agent.

Agent ID

Login ID of the agent.

Login Duration (since midnight)

Time the agent logged in since midnight.

Current State

State of the agent—Logged-In, Logout, Not Ready, Ready,
                                             						Reserved, Talking, or Work.

Duration

Time that the agent spent in the current state.

Finesse Desktop client machines should be time synchronized with a reliable NTP server for the correct updates to the Duration
                                                         fields within Live Data reports.

#### Filter Criteria

You can filter using the following parameter:

Filter parameter

Result

Agent ID

Displays information for the agents who belong to the
                                             						specified teams.

#### Grouping Criteria

None

### Team Summary
                           	 Report

The Team Summary Report presents performance statistics of all the agents in the team. The following two views are available
                                 for this report:

Short and Long Term Average —Presents the performance statistics of the team members for the current day based on short term and long term values.

Since Midnight —Presents the performance statistics for the current day, since midnight.

Your administrator can set the short term value to 5, 10 or 15 minutes.

Long term value is set to 30 minutes.

#### Charts

None

#### Fields

The following are the view-wise tables that are part of the report:

Field

Description

Agent Name

First name and last name of the agent.

Agent ID

Login ID of the agent.

Login Duration (since midnight)

Total login duration of the agent, since midnight.

Average Talk Time—Short Term

Average time the agent spent in Talking state in the last 5, 10 or 15 minutes.

Average Talk Time—Long Term

Average time the agent spent in Talking state in the last 30 minutes.

Average Hold Time—Short Term

Average time the agent put the calls on hold in the last 5, 10 or 15 minutes.

Average Hold Time—Long Term

Average time the agent put the calls on hold in the last 30 minutes.

Field

Description

Agent Name

First name and last name of the agent.

Agent ID

Login ID of the agent.

Login Duration

Total login duration of the agent.

Calls Offered

Number of calls that are sent to the agent, regardless of whether the agent answered the call.

Calls Handled

Number of calls that are answered by the agent.

Average Ring Time

Average ring time of calls before the calls were answered.

Average ring time = Total ring time / Calls handled

Talk Time—Avg

Average time the agent spent in Talking state.

Average talk time = Total time in Talking state / Calls handled

Talk Time—Max

Longest time the agent spent in Talking state.

Talk Time—Total

Total time the agent spent in Talking state.

Hold Time—Avg

Average time the agent put the calls on hold.

Average hold time = Total time calls were put on hold / Calls handled

Hold Time—Max

Longest time the agent put a call on hold.

Hold Time—Total

Total time the agent put the calls on hold.

Ready Time—Avg

Average time the agent spent in Ready state.

Average ready time = Total time the agent spent in Ready state / Number of times the agent moved to Ready state

Ready Time—Max

Longest time the agent spent in Ready state.

Ready Time—Total

Total time the agent spent in Ready state.

Not Ready Time—Avg

Average time the agent spent in Not Ready state.

Average not ready time = Total time the agent spent in Not Ready state / Number of times the agent moved to Not Ready state

Not Ready Time—Max

Longest time the agent spent in Not Ready state.

Not Ready Time—Total

Total time the agent spent in Not Ready state.

After Call Work Time—Avg

Average time the agent spent in Work state.

Average work time = Total time in Work state / Calls completed

After Call Work Time—Max

Longest time the agent spent in Work state.

After Call Work Time—Total

Total time the agent spent in Work state.

#### Filter Criteria

You can filter using the following parameter:

Filter parameter

Result

Agent ID

Displays information for the agents who belong to the
                                             						specified teams.

#### Grouping Criteria

None

### Voice CSQ Agent Detail
                           	 Report

The Voice CSQ Agent Detail Report presents the agent current state, duration in the state and the reason code where applicable.

#### Charts

None

#### Fields

The report includes a table that displays the following information:

Field

Description

CSQ

Name of the Contact Service Queue (CSQ).

Agent Name

First name and last name of the agent.

Agent ID

Login ID of the agent.

Current State

State of the agent—Logged-In, Logout, Not Ready, Ready,
                                             						Reserved, Talking (from CSQ: <CSQ Name>), or Work.

Duration

Time that the agent spent in the current state.

Finesse Desktop client machines should be time synchronized with a reliable NTP server for the correct updates to the Duration
                                                         fields within Live Data reports.

Reason

The reason selected by the agent when moving to Logout state
                                             						or Not Ready state. This displays the reason code if the reason is unavailable.
                                             						A blank is due to any one of the following:

No logout reason code is configured.

Agent was unable to enter a reason.

Reason codes for all other states except Not Ready and Logout.

To view a list of reason codes and their descriptions, see
                                             						the "Predefined" reason codes section below.

#### Filter Criteria

You can filter using the following parameter:

Filter parameter

Result

Agent ID

Displays information for the agents who belong to the
                                             						specified teams.

#### Grouping Criteria

None

#### Predefined
                                 		  Reason Codes

Reason Code

State

Event

Event Description

22

Logout

SUP_AGT_TO_LOGOUT

Supervisor changes an agent’s state to Logout.

33

Ready/Not Ready

SUP_AGT_TO_READY/SUP_AGT_TO_NOT READY

Supervisor changes an agent’s state to either Ready or Not Ready.

255

Logout

—

The system issues this reason code when the agent is forcibly logged out when there is a connection failure between the Cisco
                                             Finesse Desktop and the Cisco Finesse Server.

32741

Logout

ICD_EXTENSION_CONFLICT

If an agent has already logged in and another agent tries to login with the same extension number, then the previously logged
                                             in agent will be logged out by the system.

32742

Not Ready

AGT_SEC_LINE_OFFHOOK

Agent's state is changed from Ready state to Not Ready state when the monitored Non ICD lines are used for Incoming or Outgoing
                                             calls.

32745

OUTBOUND

OUTBOUND_WORK_REASONCODE

This reason code is set when an agent goes into the Work state to select a wrap up code after ending an outbound call.

32746

OUTBOUND

AGENT_RESERVED_OUTBOUND_DIRECTPREVIEW

This reason code is set when an agent goes into a Reserved state for a direct preview outbound call.

32747

OUTBOUND

AGENT_RESERVED_OUTBOUND

This reason code is set when an agent goes into a Reserved state for an agent progressive or predictive outbound call.

32748

Logout

AGENT_DELETED

Agent is logged out from Unified CCX as the agent is deleted from Unified Communications Manager. This event is triggered
                                             when Unified CCX synchronizes the agent information with Unified Communications Manager.

32749

Not Ready

CANCEL_FEATURE

Agent's state changes from Talking to Not Ready because the Cancel feature is triggered during an Interactive Call Distribution
                                             (ICD) consult call between two agents.

When the consulting agent presses the Cancel softkey on the phone, the consulted agent is no longer associated with the ICD call, and the consulted agent's state changes
                                             to Not Ready. This feature is available only on some of the newer phones.

32750

Not Ready

AGT_IPCC_EXT_ CHANGED

Agent is logged out from Unified CCX because the agent’s Unified CCX extension changes in Unified Communications Manager.

32751

Ready

AGENT_SKIPS

Agent receives a preview outbound call and skips the call.

32752

Ready

CANCEL_RESERVATION

Agent receives a preview outbound call, decides to cancel the reservation, and presses the Cancel Reservation button on the desktop.

32753

Not Ready

LINE_RESTRICTED

Agent’s phone line is flagged as a restricted device by the administrator of Unified Communications Manager.

If Allow Control of Device from CTI is not checked in the Default Device Profile Configuration window in Unified Communications Manager, the line remains restricted and cannot be controlled. You can modify this setting
                                             for devices that register with Unified Communications Manager. See the Cisco Unified
                                                      				  Communications Manager Administration Guide , located at: https://www.cisco.com/en/US/products/sw/voicesw/ps556/prod_maintenance_guides_list.html .

32754

Not Ready

DEVICE_RESTRICTED

Agent's device is flagged as a restricted device by the administrator of Unified Communications Manager.

If Allow Control of Device from CTI is not checked in the Default Device Profile Configuration window in Unified Communications Manager, the device remains restricted and cannot be controlled. You can modify this setting
                                             for devices that register with Unified Communications Manager. See the Cisco Unified
                                                      				  Communications Manager Administration Guide , located at: https://www.cisco.com/en/US/products/sw/voicesw/ps556/prod_maintenance_guides_list.html .

32755

Not Ready

CALL_ENDED

Agent moves to Not Ready state after handling a Unified CCX call. This event occurs in the following cases:

Agent 1 is in Not Ready state and gets a consult call from Agent 2. After handling the call, Agent 1 moves back to Not Ready
                                                   state.

The Automatic Available option is disabled for the agent. After handling a call, agent moves to Not Ready state.

32756

Not Ready

PHONE_UP

Agent’s phone becomes active after it was in Phone Down state.

32757

Not Ready

CM_FAILOVER

Unified Communications Manager fails over, and the agent is moved to Not Ready state.

32758

Not Ready

WORK_TIMER_EXP

Agent’s state changes from Work to Not Ready. This change occurs if the Work state for that agent’s CSQ is associated with
                                             an expired wrap-up timer.

32759

Not Ready

PHONE_DOWN

Agent’s phone stops functioning and the agent is placed in the Unavailable state.

32760

Not Ready

AGT_LOGON

Agent logs in and is automatically placed in the Not Ready state.

32761

Not Ready

AGT_RCV_NON_ICD

Agent is logged in to the desktop or IP phone and receives a call that is not queued on the Unified CCX platform.

32762

Not Ready

AGT_OFFHOOK

Agent goes off hook to place a call. If the agent enters a reason, that reason is displayed. If the agent does not select
                                             any reason, the system issues this reason code.

32763

Not Ready

AGT_RNA

Agent fails to answer a Unified CCX call within the specified timeout period.

32764

Logout

CRS_FAILURE

Active server becomes the standby server, and the agent loses connection to the Unified CCX platform.

32765

Logout

CONNECTION_DOWN

IP Phone Agent or desktop stops functioning, or connection is disrupted.

32766

Logout

CLOSE_FINESSE_DESKTOP

Agent manually logs out from the Finesse Desktop using the default Logout (without any custom reason label) option.

32767

Logout

AGT_RELOGIN

Agent is logged in to one device (computer or phone) and tries to log in to a second device.

### Voice CSQ Summary
                           	 Report

The Voice CSQ Summary Report presents agent statistics and call statistics for a Contact Service Queue (CSQ). The following
                                 three views are available for this report:

Snapshot —Presents the performance statistics of the agents that are associated with the specified CSQs.

Short and Long Term Average —Presents the call statistics of the CSQ for the current day based on short term and long term values.

Since Midnight —Presents the call statistics of the CSQ, since midnight.

Your administrator can set the short term value to 5, 10 or 15 minutes.

Long term value is set to 30 minutes.

#### Charts

None

#### Fields

The following are
                                 		  the view-wise tables that are part of the report:

Field

Description

CSQ Name

Name of the CSQ.

Waiting Calls

Number of calls in queue for a CSQ.

Longest Call in Queue

Elapsed wait time of the oldest call in the queue.

Agents Logged In

Number of agents in Logged-In state.

Agents Talking

Number of agents in Talking state.

Agents Ready

Number of agents in Ready state.

Agents Not Ready

Number of agents in Not Ready state.

Agents in After Call Work

Number of agents in Work state.

Agents Reserved

Number of agents in Reserved state.

Field

Description

CSQ Name

Name of the CSQ.

Calls Abandoned—Short Term

Number of abandoned calls in the last 5, 10 or 15 minutes.

Calls Abandoned—Long Term

Number of abandoned calls in the last 30 minutes.

Calls Dequeued—Short Term

Number of dequeued calls in the last 5, 10 or 15 minutes.

Calls Dequeued—Long Term

Number of dequeued calls in the last 30 minutes.

Average Contact Handling Time—Short Term

Average handle time of the calls that are routed to the CSQ in the last 5, 10 or 15 minutes.

Average Contact Handling Time—Long Term

Average handle time of the calls that are routed to the CSQ in the last 30 minutes.

Average Waiting Duration—Short Term

Average wait time of the calls that are routed to the CSQ in the last 5, 10 or 15 minutes.

Average Waiting Duration—Long Term

Average wait time of the calls that are routed to the CSQ in the last 30 minutes.

Service Level—Short Term

Service level is measured in the last 5, 10 or 15 minutes. The most recent service level is displayed in case there are no
                                             calls in the measurement window.

Service Level—Long Term

Service level in the last 30 minutes.

Field

Description

CSQ Name

Name of the CSQ.

Waiting Calls

Number of calls in queue for a CSQ.

Abandoned Calls

Number of calls that are abandoned for a CSQ.

Handled Calls

Number of calls that are answered by the agents in the CSQ.

Total Calls

Number of calls that are presented to the CSQ.

Longest Call in Queue

Longest wait time of any call before it is answered.

Longest Handle Time

Longest talk time of any call that the agent handled.

#### Filter
                                 		  Criteria

You can filter
                                 		  using the following parameter:

Filter parameter

Result

CSQ
                                             						Name

Displays information for the CSQs that belong to the specified
                                             						queues.

#### Grouping
                                 		  Criteria

None

| Note | For more information about cookies and Tracking Protection option, see your browser-specific documentation. |
|---|---|

| Note | Any connectivity or technical problems that are encountered during the chat session are notified as banner messages at the
                                          top of the conversation area. |
|---|---|

| Field | Description |
|---|---|
| Agent ID | Login ID of the agent. |
| CSQ Name | Name of the CSQ. |
| Calls Waiting | Number of calls in queue for a CSQ. |
| Longest Call in Queue | Elapsed wait time of the oldest call in the queue. |

| Filter parameter | Result |
|---|---|
| Team Name | Displays information for the CSQs that belong to the
                                             						specified teams. |

| Note | Filter parameters are applicable only for CUIC based reports and not Finesse live data. |
|---|---|

| Field | Description |
|---|---|
| Agent ID | Login ID of the agent. Note This field is not listed in Gadget View. | Note | This field is not listed in Gadget View. |
| Note | This field is not listed in Gadget View. |
| Start
                                             						Time | Time the
                                             						agent state is initiated. |
| State | State of
                                             						the agent—Login, Logout, Not Ready, Ready, Reserved, Talking, or Work. |
| Reason | The reason selected by the agent moving to Logout state or Not Ready state. This displays the reason code if the reason label
                                             is unavailable. A blank is due to any one of the following: No logout reason code is configured. Agent was unable to enter a reason. Reason codes for all other states except Not Ready and Logout. To view
                                             						a list of reason codes and their descriptions, see the "Predefined" reason codes section below. |
| Duration | Time
                                             						duration that the agent was in that state. Note Finesse Desktop client machines should be time synchronized with a reliable NTP server for the correct updates to the Duration
                                                         fields within Live Data reports. | Note | Finesse Desktop client machines should be time synchronized with a reliable NTP server for the correct updates to the Duration
                                                         fields within Live Data reports. |
| Note | Finesse Desktop client machines should be time synchronized with a reliable NTP server for the correct updates to the Duration
                                                         fields within Live Data reports. |

| Note | This field is not listed in Gadget View. |
|---|---|

| Note | Finesse Desktop client machines should be time synchronized with a reliable NTP server for the correct updates to the Duration
                                                         fields within Live Data reports. |
|---|---|

| Filter parameter | Result |
|---|---|
| Agent ID | Displays
                                             						information for the agents who belong to the specified teams. |

| Note | Filter parameters are applicable only for CUIC based reports and not Finesse live data. |
|---|---|

| Reason Code | State | Event | Event Description |
|---|---|---|---|
| 22 | Logout | SUP_AGT_TO_LOGOUT | Supervisor changes an agent’s state to Logout. |
| 33 | Ready/Not Ready | SUP_AGT_TO_READY/SUP_AGT_TO_NOT READY | Supervisor changes an agent’s state to either Ready or Not Ready. |
| 255 | Logout | — | The system issues this reason code when the agent is forcibly logged out when there is a connection failure between the Cisco
                                             Finesse Desktop and the Cisco Finesse Server. |
| 32741 | Logout | ICD_EXTENSION_CONFLICT | If an agent has already logged in and another agent tries to login with the same extension number, then the previously logged
                                             in agent will be logged out by the system. |
| 32742 | Not Ready | AGT_SEC_LINE_OFFHOOK | Agent's state is changed from Ready state to Not Ready state when the monitored Non ICD lines are used for Incoming or Outgoing
                                             calls. |
| 32745 | OUTBOUND | OUTBOUND_WORK_REASONCODE | This reason code is set when an agent goes into the Work state to select a wrap up code after ending an outbound call. |
| 32746 | OUTBOUND | AGENT_RESERVED_OUTBOUND_DIRECTPREVIEW | This reason code is set when an agent goes into a Reserved state for a direct preview outbound call. |
| 32747 | OUTBOUND | AGENT_RESERVED_OUTBOUND | This reason code is set when an agent goes into a Reserved state for an agent progressive or predictive outbound call. |
| 32748 | Logout | AGENT_DELETED | Agent is logged out from Unified CCX as the agent is deleted from Unified Communications Manager. This event is triggered
                                             when Unified CCX synchronizes the agent information with Unified Communications Manager. |
| 32749 | Not Ready | CANCEL_FEATURE | Agent's state changes from Talking to Not Ready because the Cancel feature is triggered during an Interactive Call Distribution
                                             (ICD) consult call between two agents. When the consulting agent presses the Cancel softkey on the phone, the consulted agent is no longer associated with the ICD call, and the consulted agent's state changes
                                             to Not Ready. This feature is available only on some of the newer phones. |
| 32750 | Not Ready | AGT_IPCC_EXT_ CHANGED | Agent is logged out from Unified CCX because the agent’s Unified CCX extension changes in Unified Communications Manager. |
| 32751 | Ready | AGENT_SKIPS | Agent receives a preview outbound call and skips the call. |
| 32752 | Ready | CANCEL_RESERVATION | Agent receives a preview outbound call, decides to cancel the reservation, and presses the Cancel Reservation button on the desktop. |
| 32753 | Not Ready | LINE_RESTRICTED | Agent’s phone line is flagged as a restricted device by the administrator of Unified Communications Manager. Attention If an agent’s line is added to the restricted list, it affects the function of RmCm subsystem. If Allow Control of Device from CTI is not checked in the Default Device Profile Configuration window in Unified Communications Manager, the line remains restricted and cannot be controlled. You can modify this setting
                                             for devices that register with Unified Communications Manager. See the Cisco Unified
                                                      				  Communications Manager Administration Guide , located at: https://www.cisco.com/en/US/products/sw/voicesw/ps556/prod_maintenance_guides_list.html . | Attention | If an agent’s line is added to the restricted list, it affects the function of RmCm subsystem. |
| Attention | If an agent’s line is added to the restricted list, it affects the function of RmCm subsystem. |
| 32754 | Not Ready | DEVICE_RESTRICTED | Agent's device is flagged as a restricted device by the administrator of Unified Communications Manager. Attention If an agent’s device is added to the Restricted list, it affects the function of RmCm subsystem. If Allow Control of Device from CTI is not checked in the Default Device Profile Configuration window in Unified Communications Manager, the device remains restricted and cannot be controlled. You can modify this setting
                                             for devices that register with Unified Communications Manager. See the Cisco Unified
                                                      				  Communications Manager Administration Guide , located at: https://www.cisco.com/en/US/products/sw/voicesw/ps556/prod_maintenance_guides_list.html . | Attention | If an agent’s device is added to the Restricted list, it affects the function of RmCm subsystem. |
| Attention | If an agent’s device is added to the Restricted list, it affects the function of RmCm subsystem. |
| 32755 | Not Ready | CALL_ENDED | Agent moves to Not Ready state after handling a Unified CCX call. This event occurs in the following cases: Agent 1 is in Not Ready state and gets a consult call from Agent 2. After handling the call, Agent 1 moves back to Not Ready
                                                   state. The Automatic Available option is disabled for the agent. After handling a call, agent moves to Not Ready state. |
| 32756 | Not Ready | PHONE_UP | Agent’s phone becomes active after it was in Phone Down state. |
| 32757 | Not Ready | CM_FAILOVER | Unified Communications Manager fails over, and the agent is moved to Not Ready state. |
| 32758 | Not Ready | WORK_TIMER_EXP | Agent’s state changes from Work to Not Ready. This change occurs if the Work state for that agent’s CSQ is associated with
                                             an expired wrap-up timer. |
| 32759 | Not Ready | PHONE_DOWN | Agent’s phone stops functioning and the agent is placed in the Unavailable state. |
| 32760 | Not Ready | AGT_LOGON | Agent logs in and is automatically placed in the Not Ready state. |
| 32761 | Not Ready | AGT_RCV_NON_ICD | Agent is logged in to the desktop or IP phone and receives a call that is not queued on the Unified CCX platform. |
| 32762 | Not Ready | AGT_OFFHOOK | Agent goes off hook to place a call. If the agent enters a reason, that reason is displayed. If the agent does not select
                                             any reason, the system issues this reason code. |
| 32763 | Not Ready | AGT_RNA | Agent fails to answer a Unified CCX call within the specified timeout period. |
| 32764 | Logout | CRS_FAILURE | Active server becomes the standby server, and the agent loses connection to the Unified CCX platform. |
| 32765 | Logout | CONNECTION_DOWN | IP Phone Agent or desktop stops functioning, or connection is disrupted. |
| 32766 | Logout | CLOSE_FINESSE_DESKTOP | Agent manually logs out from the Finesse Desktop using the default Logout (without any custom reason label) option. |
| 32767 | Logout | AGT_RELOGIN | Agent is logged in to one device (computer or phone) and tries to log in to a second device. |

| Attention | If an agent’s line is added to the restricted list, it affects the function of RmCm subsystem. |
|---|---|

| Attention | If an agent’s device is added to the Restricted list, it affects the function of RmCm subsystem. |
|---|---|

| Field | Description |
|---|---|
| Agent ID | Login ID
                                             						of the agent. |
| Type | Type of
                                             						the call. For example, Inbound or Outbound. |
| Number | Phone
                                             						number of the call. To view
                                             						a list of reason codes and their descriptions, see the "Predefined" reason codes section below. |
| Disposition | Contact
                                             						disposition type of the call. |
| Wrap-Up
                                             						Reason | Wrap-Up
                                             						Reasons entered by the agent. |
| Queue | Queue
                                             						details that the call was routed to. |
| Start
                                             						Time | Start
                                             						time of the call. |
| Duration | Time
                                             						duration of the call. Note Finesse Desktop client machines should be time synchronized with a reliable NTP server for the correct updates to the Duration
                                                         fields within Live Data reports. | Note | Finesse Desktop client machines should be time synchronized with a reliable NTP server for the correct updates to the Duration
                                                         fields within Live Data reports. |
| Note | Finesse Desktop client machines should be time synchronized with a reliable NTP server for the correct updates to the Duration
                                                         fields within Live Data reports. |

| Note | Finesse Desktop client machines should be time synchronized with a reliable NTP server for the correct updates to the Duration
                                                         fields within Live Data reports. |
|---|---|

| Filter parameter | Result |
|---|---|
| Agent ID | Displays
                                             						information for the agents who belong to the specified teams. |

| Note | Filter parameters are applicable only for CUIC based reports and not Finesse live data. |
|---|---|

| Field | Description |
|---|---|
| Agent ID | Login ID of the agent. |
| Calls Offered | Calls sent to the agent, regardless of whether the agent picks up the call. |
| Calls Handled | Calls connected to the agent. |
| Talk Time—Avg | Average time the agent spent in Talking state. Average talk time = Total time in Talking state / Calls handled |
| Talk Time—Max | Longest time the agent spent in Talking state. |
| Talk Time—Total | Total time the agent spent in Talking state. |
| Hold Time—Avg | Average time the agent put the calls on hold. Average hold time = Total time the calls were on hold / Calls handled |
| Hold Time—Max | Longest time the agent put a call on hold. |
| Hold Time—Total | Total time the agent put the calls on hold. |
| Ready—Avg | Average time the agent spent in Ready state. Average ready time = Total time the agent spent in Ready state / Number of times the agent moved to Ready state |
| Ready—Max | Longest time the agent spent in Ready state. |
| Ready—Total | Total time the agent spent in Ready state. |
| Not Ready—Avg | Average time the agent spent in Not Ready state. Average not ready time = Total time the agent spent in Not Ready state / Number of times the agent moved to Not Ready state |
| Not Ready—Max | Longest time the agent spent in Not Ready state. |
| Not Ready—Total | Total time the agent spent in Not Ready state. |
| After Call Work—Avg | Average time the agent spent in Work state. Average work time = Total time in Work state / Calls completed |
| After Call Work—Max | Longest time the agent spent in Work state. |
| After Call Work—Total | Total time the agent spent in Work state. |

| Filter parameter | Result |
|---|---|
| Agent ID | Displays information for the agents who belong to the
                                             						specified teams. |

| Note | Filter parameters are applicable only for CUIC based reports and not Finesse live data. |
|---|---|

| Field | Description |
|---|---|
| Agent
                                             						Name | First
                                             						name and last name of the agent. |
| State | State of
                                             						the agent—Logged-In, Logout, Not Ready, Ready, Reserved, Talking, or Work. |
| Reason | The reason selected by the agent when moving to Logout state
                                             						or Not Ready state. This displays the reason code if the reason is unavailable.
                                             						A blank is due to one of the following: No logout reason code is configured. Agent was unable to select a reason. Reason codes for all other states except Not Ready and Logout. To view
                                             						a list of reason codes and their descriptions, see the "Predefined" reason codes section below. |

| Filter parameter | Result |
|---|---|
| Agent ID | Displays
                                             						information for the agents who belong to the specified teams. |

| Note | Filter parameters are applicable only for CUIC based reports and not Finesse live data. |
|---|---|

| Reason Code | State | Event | Event Description |
|---|---|---|---|
| 22 | Logout | SUP_AGT_TO_LOGOUT | Supervisor changes an agent’s state to Logout. |
| 33 | Ready/Not Ready | SUP_AGT_TO_READY/SUP_AGT_TO_NOT READY | Supervisor changes an agent’s state to either Ready or Not Ready. |
| 255 | Logout | — | The system issues this reason code when the agent is forcibly logged out when there is a connection failure between the Cisco
                                             Finesse Desktop and the Cisco Finesse Server. |
| 32741 | Logout | ICD_EXTENSION_CONFLICT | If an agent has already logged in and another agent tries to login with the same extension number, then the previously logged
                                             in agent will be logged out by the system. |
| 32742 | Not Ready | AGT_SEC_LINE_OFFHOOK | Agent's state is changed from Ready state to Not Ready state when the monitored Non ICD lines are used for Incoming or Outgoing
                                             calls. |
| 32745 | OUTBOUND | OUTBOUND_WORK_REASONCODE | This reason code is set when an agent goes into the Work state to select a wrap up code after ending an outbound call. |
| 32746 | OUTBOUND | AGENT_RESERVED_OUTBOUND_DIRECTPREVIEW | This reason code is set when an agent goes into a Reserved state for a direct preview outbound call. |
| 32747 | OUTBOUND | AGENT_RESERVED_OUTBOUND | This reason code is set when an agent goes into a Reserved state for an agent progressive or predictive outbound call. |
| 32748 | Logout | AGENT_DELETED | Agent is logged out from Unified CCX as the agent is deleted from Unified Communications Manager. This event is triggered
                                             when Unified CCX synchronizes the agent information with Unified Communications Manager. |
| 32749 | Not Ready | CANCEL_FEATURE | Agent's state changes from Talking to Not Ready because the Cancel feature is triggered during an Interactive Call Distribution
                                             (ICD) consult call between two agents. When the consulting agent presses the Cancel softkey on the phone, the consulted agent is no longer associated with the ICD call, and the consulted agent's state changes
                                             to Not Ready. This feature is available only on some of the newer phones. |
| 32750 | Not Ready | AGT_IPCC_EXT_ CHANGED | Agent is logged out from Unified CCX because the agent’s Unified CCX extension changes in Unified Communications Manager. |
| 32751 | Ready | AGENT_SKIPS | Agent receives a preview outbound call and skips the call. |
| 32752 | Ready | CANCEL_RESERVATION | Agent receives a preview outbound call, decides to cancel the reservation, and presses the Cancel Reservation button on the desktop. |
| 32753 | Not Ready | LINE_RESTRICTED | Agent’s phone line is flagged as a restricted device by the administrator of Unified Communications Manager. Attention If an agent’s line is added to the restricted list, it affects the function of RmCm subsystem. If Allow Control of Device from CTI is not checked in the Default Device Profile Configuration window in Unified Communications Manager, the line remains restricted and cannot be controlled. You can modify this setting
                                             for devices that register with Unified Communications Manager. See the Cisco Unified
                                                      				  Communications Manager Administration Guide , located at: https://www.cisco.com/en/US/products/sw/voicesw/ps556/prod_maintenance_guides_list.html . | Attention | If an agent’s line is added to the restricted list, it affects the function of RmCm subsystem. |
| Attention | If an agent’s line is added to the restricted list, it affects the function of RmCm subsystem. |
| 32754 | Not Ready | DEVICE_RESTRICTED | Agent's device is flagged as a restricted device by the administrator of Unified Communications Manager. Attention If an agent’s device is added to the Restricted list, it affects the function of RmCm subsystem. If Allow Control of Device from CTI is not checked in the Default Device Profile Configuration window in Unified Communications Manager, the device remains restricted and cannot be controlled. You can modify this setting
                                             for devices that register with Unified Communications Manager. See the Cisco Unified
                                                      				  Communications Manager Administration Guide , located at: https://www.cisco.com/en/US/products/sw/voicesw/ps556/prod_maintenance_guides_list.html . | Attention | If an agent’s device is added to the Restricted list, it affects the function of RmCm subsystem. |
| Attention | If an agent’s device is added to the Restricted list, it affects the function of RmCm subsystem. |
| 32755 | Not Ready | CALL_ENDED | Agent moves to Not Ready state after handling a Unified CCX call. This event occurs in the following cases: Agent 1 is in Not Ready state and gets a consult call from Agent 2. After handling the call, Agent 1 moves back to Not Ready
                                                   state. The Automatic Available option is disabled for the agent. After handling a call, agent moves to Not Ready state. |
| 32756 | Not Ready | PHONE_UP | Agent’s phone becomes active after it was in Phone Down state. |
| 32757 | Not Ready | CM_FAILOVER | Unified Communications Manager fails over, and the agent is moved to Not Ready state. |
| 32758 | Not Ready | WORK_TIMER_EXP | Agent’s state changes from Work to Not Ready. This change occurs if the Work state for that agent’s CSQ is associated with
                                             an expired wrap-up timer. |
| 32759 | Not Ready | PHONE_DOWN | Agent’s phone stops functioning and the agent is placed in the Unavailable state. |
| 32760 | Not Ready | AGT_LOGON | Agent logs in and is automatically placed in the Not Ready state. |
| 32761 | Not Ready | AGT_RCV_NON_ICD | Agent is logged in to the desktop or IP phone and receives a call that is not queued on the Unified CCX platform. |
| 32762 | Not Ready | AGT_OFFHOOK | Agent goes off hook to place a call. If the agent enters a reason, that reason is displayed. If the agent does not select
                                             any reason, the system issues this reason code. |
| 32763 | Not Ready | AGT_RNA | Agent fails to answer a Unified CCX call within the specified timeout period. |
| 32764 | Logout | CRS_FAILURE | Active server becomes the standby server, and the agent loses connection to the Unified CCX platform. |
| 32765 | Logout | CONNECTION_DOWN | IP Phone Agent or desktop stops functioning, or connection is disrupted. |
| 32766 | Logout | CLOSE_FINESSE_DESKTOP | Agent manually logs out from the Finesse Desktop using the default Logout (without any custom reason label) option. |
| 32767 | Logout | AGT_RELOGIN | Agent is logged in to one device (computer or phone) and tries to log in to a second device. |

| Attention | If an agent’s line is added to the restricted list, it affects the function of RmCm subsystem. |
|---|---|

| Attention | If an agent’s device is added to the Restricted list, it affects the function of RmCm subsystem. |
|---|---|

| Note | Your administrator can set the short term value to 5, 10, or 15 minutes. Long term value is set to 30 minutes. |
|---|---|

| Field | Description |
|---|---|
| Agent Name | First name and last name of the agent. |
| Agent ID | Login ID of the agent. |
| Average Talk Time—Short Term | Average time the agent spent in Talking state for outbound calls in the last 5, 10, or 15 minutes. |
| Average Talk Time—Long Term | Average time the agent spent in Talking state for outbound calls in the last 30 minutes. |
| Average Hold Time—Short Term | Average time the agent put the outbound calls on hold in the last 5, 10, or 15 minutes. |
| Average Hold Time—Long Term | Average time the agent put the outbound calls on hold in the last 30 minutes. |

| Field | Description |
|---|---|
| Agent Name | First name and last name of the agent. |
| Agent ID | Login ID of the agent. |
| Talk Time—Avg | Average time the agent spent in Talking state for outbound calls. Average talk time = Total time in Talking state / calls handled |
| Talk Time—Max | Longest time the agent spent in Talking state for outbound calls. |
| Talk Time—Total | Total time the agent spent in Talking state for outbound calls. |
| Hold Time—Avg | Average time the agent put the outbound calls on hold. Average hold time = Total time calls were put on hold / calls handled |
| Hold Time—Max | Longest time the agent put an outbound call on hold. |
| Hold Time—Total | Total time the agent put the outbound calls on hold. |
| After Call Work Time—Avg | Average time the agent spent in Work state for outbound calls. Average work time = Total time in Work state / calls completed |
| After Call Work Time—Max | Longest time the agent spent in Work state for outbound calls. |
| After Call Work Time—Total | Total time the agent spent in Work state for outbound calls. |

| Filter Parameter | Result |
|---|---|
| Agent ID | Displays information for the agents who belong to the
                                             						specified teams. |

| Note | Filter parameters are applicable only for CUIC based reports and not Finesse live data. |
|---|---|

| Field | Description |
|---|---|
| Agent Name | First name
                                             					 and last name of the agent. |
| Agent ID | Login ID
                                             					 of the agent. |
| Current
                                             					 State | State of
                                             					 the agent—Logged-In, Logout, Not Ready, Ready, Partial Busy, Busy, Reserved. |
| Duration | Time that
                                             					 the agent spent in the current state. Note Finesse Desktop client machines should be time synchronized with a reliable NTP server for the correct updates to the Duration
                                                         fields within Live Data reports. | Note | Finesse Desktop client machines should be time synchronized with a reliable NTP server for the correct updates to the Duration
                                                         fields within Live Data reports. |
| Note | Finesse Desktop client machines should be time synchronized with a reliable NTP server for the correct updates to the Duration
                                                         fields within Live Data reports. |
| Current
                                             					 Active Contacts | Number of
                                             					 contacts that the agent is handling. |
| Contacts
                                             					 Presented | Number of
                                             					 contacts that are offered to the agent since midnight. |
| Contacts
                                             					 Handled | Number of
                                             					 contacts that are handled by the agent since midnight. A contact is marked
                                             					 handled if a contact is connected to an agent. |
| Contacts
                                             					 Abandoned | Number of
                                             					 contacts that are routed to the CSQ since midnight but are not answered by an
                                             					 agent, because the customer ends the chat or the customer is disconnected. This also includes the number of group chats that were
                                             					 abandoned when these were routed to a CSQ. They are abandoned when the group
                                             					 chat is not accepted by the second agent. This can be due to, either the chat
                                             					 submitter or the first agent ended the chat before the second agent accepted or
                                             					 was disconnected. |
| Contacts
                                             					 RNA | Number of
                                             					 contacts that the agent did not answer since midnight. Ring-no-answer (RNA). |
| Contacts
                                             					 Declined | Number of
                                             					 group chat contacts that are declined by the agent since midnight. |

| Note | Finesse Desktop client machines should be time synchronized with a reliable NTP server for the correct updates to the Duration
                                                         fields within Live Data reports. |
|---|---|

| Field | Description |
|---|---|
| Login
                                             					 Duration | Elapsed
                                             					 time between the login time and the logout time since midnight. |
| CSQs
                                             					 Serving | List of
                                             					 CSQs that the agent is serving. |
| Agent
                                             					 Utilization—Not Ready | Percentage
                                             					 of time that the agent spent in Not Ready state since midnight. It is
                                             					 calculated every minute and is one of the components that add up to the agent's
                                             					 total login duration. |
| Agent
                                             					 Utilization—Ready | Percentage
                                             					 of time that the agent spent in Ready state since midnight. It is calculated
                                             					 every minute and is one of the components that add up to the agent's total
                                             					 login duration. |
| Agent
                                             					 Utilization—Partial Busy | Percentage of time that the agent spent in Partial Busy state
                                             					 since midnight. It is calculated every minute and is one of the components that
                                             					 add up to the agent's total login duration. |
| Agent
                                             					 Utilization—Busy | Percentage of time that the agent spent in Busy state since
                                             					 midnight. It is calculated every minute and is one of the components that add
                                             					 up to the agent's total login duration. |

| Filter Parameter | Result |
|---|---|
| Agent
                                             						ID | Displays information for the agents who belong to the specified
                                             						teams. |

| Field | Description |
|---|---|
| CSQ Name | Name of the CSQ. |
| Contacts Waiting | Number of contacts in queue for a CSQ. |
| Agents—Logged-In | Number of agents in Logged-In state. |
| Agents—Not Ready | Number of agents in Not Ready state. |
| Agents—Ready | Number of agents in Ready state. |
| Agents—Partial Busy | Number of agents in Partial Busy state. An agent is set to
                                             					 Partial Busy state when the agent has not reached the maximum number of chat
                                             					 sessions that is set by the administrator. |
| Agents—Busy | Number of agents in Busy state. An agent is set to Busy state
                                             					 when the agent reaches the maximum number of chat sessions that is set by the
                                             					 administrator. |
| Agents—Reserved | Number of agents in Reserved state. |

| Field | Description |
|---|---|
| Contacts Total | Number of contacts routed to the CSQ since midnight. |
| Contacts Handled | Number of contacts that are handled by the CSQ since midnight.
                                             					 A contact is marked handled if a contact is connected to an agent while queued
                                             					 for this CSQ. |
| Contacts Abandoned | Number of contacts that are routed to the CSQ since midnight
                                             					 but are not answered by an agent, because the customer ends the chat or the
                                             					 customer is disconnected. |

| Filter Parameter | Result |
|---|---|
| Queue Name | Displays information for the CSQs that belong to the
                                             						specified queues. |

| Field | Description |
|---|---|
| Agent Name | First name and last name of the agent. |
| Agent ID | Login ID of the agent. |
| State | State of the agent—Not Ready, Ready, Partial Busy, Busy, Reserved. |
| Duration | Time that the agent spent in the current state. Note Finesse Desktop client machines should be time synchronized with a reliable NTP server for the correct updates to the Duration
                                                         fields within Live Data reports. | Note | Finesse Desktop client machines should be time synchronized with a reliable NTP server for the correct updates to the Duration
                                                         fields within Live Data reports. |
| Note | Finesse Desktop client machines should be time synchronized with a reliable NTP server for the correct updates to the Duration
                                                         fields within Live Data reports. |
| Active Emails | Number of email messages that the agent is handling. |
| Emails Presented | Number of email messages that are presented to the agent since midnight. Note The number of emails that are presented include new and requeued emails. | Note | The number of emails that are presented include new and requeued emails. |
| Note | The number of emails that are presented include new and requeued emails. |
| Emails Handled | Number of email messages that are handled by the agent since midnight. |
| Emails Discarded | Number of email messages discarded by the agent or by the system during service disruption. The system discarded emails would
                                             be reinjected into the system when the service is restored. |
| Emails Requeued | Number of email messages that the agent requeued since midnight. |

| Note | Finesse Desktop client machines should be time synchronized with a reliable NTP server for the correct updates to the Duration
                                                         fields within Live Data reports. |
|---|---|

| Note | The number of emails that are presented include new and requeued emails. |
|---|---|

| Field | Description |
|---|---|
| Login Duration | Elapsed time between the login time and the logout time since midnight. |
| CSQs Serving | List of CSQs that the agent is serving. |
| Agent Utilization—Not Ready | Percentage of time that the agent spent in Not Ready state since midnight. It is calculated every minute and is one of the
                                             components that add up to the agent's total login duration. |
| Agent Utilization—Ready | Percentage of time that the agent spent in Ready state since midnight. It is calculated every minute and is one of the components
                                             that add up to the agent's total login duration. |
| Agent Utilization—Partial Busy | Percentage of time that the agent spent in Partial Busy state since midnight. It is calculated every minute and is one of
                                             the components that add up to the agent's total login duration. |
| Agent Utilization—Busy | Percentage of time that the agent spent in Busy state since midnight. It is calculated every minute and is one of the components
                                             that add up to the agent's total login duration. |
| Agent Utilization—Reserved | Percentage of time that the agent spent in Reserved state since midnight. It is calculated every minute and is one of the
                                             components that add up to the agent's total login duration. |

| Filter Parameter | Result |
|---|---|
| Agent ID | Displays information for the agents who belong to the specified teams. |

| Note | Filter parameters are applicable only for CUIC based reports and not Finesse live data. |
|---|---|

| Field | Description |
|---|---|
| CSQ Name | Name of the Email CSQ. |
| Emails in Queue | Number of email messages in queue. (This includes the emails requeued by the agent.) Note System requeues email messages that are in agents desktop when agents sign off or loose connectivity. | Note | System requeues email messages that are in agents desktop when agents sign off or loose connectivity. |
| Note | System requeues email messages that are in agents desktop when agents sign off or loose connectivity. |
| Emails in Process | Number of email messages that are assigned to agents. |
| Emails Discarded | Number of email messages that have been discarded, both by agents and due to service disruptions. |
| Agents-Logged In | Number of agents in Logged-In state. |
| Agents-Not Ready | Number of agents in Not Ready state. |
| Agents-Ready | Number of agents in Ready state. |
| Agents-Partial Busy | Number of agents in Partial Busy state. Agents are set to Partial Busy state as soon as an email is assigned to them. They
                                             will continue to be in this state until they clear all the emails assigned to them or the state changes to Busy. |
| Agents-Busy | Number of agents in Busy state. Agents are set to Busy state when the number of emails reach the maximum limit set. Agents
                                             state is changed to Partial Busy as soon as the number of assigned email messages is one less than the maximum limit set. |

| Note | System requeues email messages that are in agents desktop when agents sign off or loose connectivity. |
|---|---|

| Field | Description |
|---|---|
| Emails Total | Number of email messages routed to the CSQ since midnight. |
| Emails Handled | Number of email messages that are handled by the CSQ since
                                             					 midnight. An email is marked handled if it is responded by an agent while
                                             					 queued for this CSQ. |

| Filter Parameter | Result |
|---|---|
| Queue Name | Displays information for the CSQs that belong to the
                                             						specified queues. |

| Field | Description |
|---|---|
| Agent Name | First name and last name of the agent. |
| Agent ID | Login ID of the agent. |
| Login Duration (since midnight) | Time the agent logged in since midnight. |
| Current State | State of the agent—Logged-In, Logout, Not Ready, Ready,
                                             						Reserved, Talking, or Work. |
| Duration | Time that the agent spent in the current state. Note Finesse Desktop client machines should be time synchronized with a reliable NTP server for the correct updates to the Duration
                                                         fields within Live Data reports. | Note | Finesse Desktop client machines should be time synchronized with a reliable NTP server for the correct updates to the Duration
                                                         fields within Live Data reports. |
| Note | Finesse Desktop client machines should be time synchronized with a reliable NTP server for the correct updates to the Duration
                                                         fields within Live Data reports. |

| Note | Finesse Desktop client machines should be time synchronized with a reliable NTP server for the correct updates to the Duration
                                                         fields within Live Data reports. |
|---|---|

| Filter parameter | Result |
|---|---|
| Agent ID | Displays information for the agents who belong to the
                                             						specified teams. |

| Note | Filter parameters are applicable only for CUIC based reports and not Finesse live data. |
|---|---|

| Note | Your administrator can set the short term value to 5, 10 or 15 minutes. Long term value is set to 30 minutes. |
|---|---|

| Field | Description |
|---|---|
| Agent Name | First name and last name of the agent. |
| Agent ID | Login ID of the agent. |
| Login Duration (since midnight) | Total login duration of the agent, since midnight. |
| Average Talk Time—Short Term | Average time the agent spent in Talking state in the last 5, 10 or 15 minutes. |
| Average Talk Time—Long Term | Average time the agent spent in Talking state in the last 30 minutes. |
| Average Hold Time—Short Term | Average time the agent put the calls on hold in the last 5, 10 or 15 minutes. |
| Average Hold Time—Long Term | Average time the agent put the calls on hold in the last 30 minutes. |

| Field | Description |
|---|---|
| Agent Name | First name and last name of the agent. |
| Agent ID | Login ID of the agent. |
| Login Duration | Total login duration of the agent. |
| Calls Offered | Number of calls that are sent to the agent, regardless of whether the agent answered the call. |
| Calls Handled | Number of calls that are answered by the agent. |
| Average Ring Time | Average ring time of calls before the calls were answered. Average ring time = Total ring time / Calls handled |
| Talk Time—Avg | Average time the agent spent in Talking state. Average talk time = Total time in Talking state / Calls handled |
| Talk Time—Max | Longest time the agent spent in Talking state. |
| Talk Time—Total | Total time the agent spent in Talking state. |
| Hold Time—Avg | Average time the agent put the calls on hold. Average hold time = Total time calls were put on hold / Calls handled |
| Hold Time—Max | Longest time the agent put a call on hold. |
| Hold Time—Total | Total time the agent put the calls on hold. |
| Ready Time—Avg | Average time the agent spent in Ready state. Average ready time = Total time the agent spent in Ready state / Number of times the agent moved to Ready state |
| Ready Time—Max | Longest time the agent spent in Ready state. |
| Ready Time—Total | Total time the agent spent in Ready state. |
| Not Ready Time—Avg | Average time the agent spent in Not Ready state. Average not ready time = Total time the agent spent in Not Ready state / Number of times the agent moved to Not Ready state |
| Not Ready Time—Max | Longest time the agent spent in Not Ready state. |
| Not Ready Time—Total | Total time the agent spent in Not Ready state. |
| After Call Work Time—Avg | Average time the agent spent in Work state. Average work time = Total time in Work state / Calls completed |
| After Call Work Time—Max | Longest time the agent spent in Work state. |
| After Call Work Time—Total | Total time the agent spent in Work state. |

| Filter parameter | Result |
|---|---|
| Agent ID | Displays information for the agents who belong to the
                                             						specified teams. |

| Note | Filter parameters are applicable only for CUIC based reports and not Finesse live data. |
|---|---|

| Note | If an agent is configured in two or more CSQs, the Supervisor is able to view on which CSQ the agent is in Talking state. |
|---|---|

| Field | Description |
|---|---|
| CSQ | Name of the Contact Service Queue (CSQ). |
| Agent Name | First name and last name of the agent. |
| Agent ID | Login ID of the agent. |
| Current State | State of the agent—Logged-In, Logout, Not Ready, Ready,
                                             						Reserved, Talking (from CSQ: <CSQ Name>), or Work. |
| Duration | Time that the agent spent in the current state. Note Finesse Desktop client machines should be time synchronized with a reliable NTP server for the correct updates to the Duration
                                                         fields within Live Data reports. | Note | Finesse Desktop client machines should be time synchronized with a reliable NTP server for the correct updates to the Duration
                                                         fields within Live Data reports. |
| Note | Finesse Desktop client machines should be time synchronized with a reliable NTP server for the correct updates to the Duration
                                                         fields within Live Data reports. |
| Reason | The reason selected by the agent when moving to Logout state
                                             						or Not Ready state. This displays the reason code if the reason is unavailable.
                                             						A blank is due to any one of the following: No logout reason code is configured. Agent was unable to enter a reason. Reason codes for all other states except Not Ready and Logout. To view a list of reason codes and their descriptions, see
                                             						the "Predefined" reason codes section below. |

| Note | Finesse Desktop client machines should be time synchronized with a reliable NTP server for the correct updates to the Duration
                                                         fields within Live Data reports. |
|---|---|

| Filter parameter | Result |
|---|---|
| Agent ID | Displays information for the agents who belong to the
                                             						specified teams. |

| Note | Filter parameters are applicable only for CUIC based reports and not Finesse live data. |
|---|---|

| Reason Code | State | Event | Event Description |
|---|---|---|---|
| 22 | Logout | SUP_AGT_TO_LOGOUT | Supervisor changes an agent’s state to Logout. |
| 33 | Ready/Not Ready | SUP_AGT_TO_READY/SUP_AGT_TO_NOT READY | Supervisor changes an agent’s state to either Ready or Not Ready. |
| 255 | Logout | — | The system issues this reason code when the agent is forcibly logged out when there is a connection failure between the Cisco
                                             Finesse Desktop and the Cisco Finesse Server. |
| 32741 | Logout | ICD_EXTENSION_CONFLICT | If an agent has already logged in and another agent tries to login with the same extension number, then the previously logged
                                             in agent will be logged out by the system. |
| 32742 | Not Ready | AGT_SEC_LINE_OFFHOOK | Agent's state is changed from Ready state to Not Ready state when the monitored Non ICD lines are used for Incoming or Outgoing
                                             calls. |
| 32745 | OUTBOUND | OUTBOUND_WORK_REASONCODE | This reason code is set when an agent goes into the Work state to select a wrap up code after ending an outbound call. |
| 32746 | OUTBOUND | AGENT_RESERVED_OUTBOUND_DIRECTPREVIEW | This reason code is set when an agent goes into a Reserved state for a direct preview outbound call. |
| 32747 | OUTBOUND | AGENT_RESERVED_OUTBOUND | This reason code is set when an agent goes into a Reserved state for an agent progressive or predictive outbound call. |
| 32748 | Logout | AGENT_DELETED | Agent is logged out from Unified CCX as the agent is deleted from Unified Communications Manager. This event is triggered
                                             when Unified CCX synchronizes the agent information with Unified Communications Manager. |
| 32749 | Not Ready | CANCEL_FEATURE | Agent's state changes from Talking to Not Ready because the Cancel feature is triggered during an Interactive Call Distribution
                                             (ICD) consult call between two agents. When the consulting agent presses the Cancel softkey on the phone, the consulted agent is no longer associated with the ICD call, and the consulted agent's state changes
                                             to Not Ready. This feature is available only on some of the newer phones. |
| 32750 | Not Ready | AGT_IPCC_EXT_ CHANGED | Agent is logged out from Unified CCX because the agent’s Unified CCX extension changes in Unified Communications Manager. |
| 32751 | Ready | AGENT_SKIPS | Agent receives a preview outbound call and skips the call. |
| 32752 | Ready | CANCEL_RESERVATION | Agent receives a preview outbound call, decides to cancel the reservation, and presses the Cancel Reservation button on the desktop. |
| 32753 | Not Ready | LINE_RESTRICTED | Agent’s phone line is flagged as a restricted device by the administrator of Unified Communications Manager. Attention If an agent’s line is added to the restricted list, it affects the function of RmCm subsystem. If Allow Control of Device from CTI is not checked in the Default Device Profile Configuration window in Unified Communications Manager, the line remains restricted and cannot be controlled. You can modify this setting
                                             for devices that register with Unified Communications Manager. See the Cisco Unified
                                                      				  Communications Manager Administration Guide , located at: https://www.cisco.com/en/US/products/sw/voicesw/ps556/prod_maintenance_guides_list.html . | Attention | If an agent’s line is added to the restricted list, it affects the function of RmCm subsystem. |
| Attention | If an agent’s line is added to the restricted list, it affects the function of RmCm subsystem. |
| 32754 | Not Ready | DEVICE_RESTRICTED | Agent's device is flagged as a restricted device by the administrator of Unified Communications Manager. Attention If an agent’s device is added to the Restricted list, it affects the function of RmCm subsystem. If Allow Control of Device from CTI is not checked in the Default Device Profile Configuration window in Unified Communications Manager, the device remains restricted and cannot be controlled. You can modify this setting
                                             for devices that register with Unified Communications Manager. See the Cisco Unified
                                                      				  Communications Manager Administration Guide , located at: https://www.cisco.com/en/US/products/sw/voicesw/ps556/prod_maintenance_guides_list.html . | Attention | If an agent’s device is added to the Restricted list, it affects the function of RmCm subsystem. |
| Attention | If an agent’s device is added to the Restricted list, it affects the function of RmCm subsystem. |
| 32755 | Not Ready | CALL_ENDED | Agent moves to Not Ready state after handling a Unified CCX call. This event occurs in the following cases: Agent 1 is in Not Ready state and gets a consult call from Agent 2. After handling the call, Agent 1 moves back to Not Ready
                                                   state. The Automatic Available option is disabled for the agent. After handling a call, agent moves to Not Ready state. |
| 32756 | Not Ready | PHONE_UP | Agent’s phone becomes active after it was in Phone Down state. |
| 32757 | Not Ready | CM_FAILOVER | Unified Communications Manager fails over, and the agent is moved to Not Ready state. |
| 32758 | Not Ready | WORK_TIMER_EXP | Agent’s state changes from Work to Not Ready. This change occurs if the Work state for that agent’s CSQ is associated with
                                             an expired wrap-up timer. |
| 32759 | Not Ready | PHONE_DOWN | Agent’s phone stops functioning and the agent is placed in the Unavailable state. |
| 32760 | Not Ready | AGT_LOGON | Agent logs in and is automatically placed in the Not Ready state. |
| 32761 | Not Ready | AGT_RCV_NON_ICD | Agent is logged in to the desktop or IP phone and receives a call that is not queued on the Unified CCX platform. |
| 32762 | Not Ready | AGT_OFFHOOK | Agent goes off hook to place a call. If the agent enters a reason, that reason is displayed. If the agent does not select
                                             any reason, the system issues this reason code. |
| 32763 | Not Ready | AGT_RNA | Agent fails to answer a Unified CCX call within the specified timeout period. |
| 32764 | Logout | CRS_FAILURE | Active server becomes the standby server, and the agent loses connection to the Unified CCX platform. |
| 32765 | Logout | CONNECTION_DOWN | IP Phone Agent or desktop stops functioning, or connection is disrupted. |
| 32766 | Logout | CLOSE_FINESSE_DESKTOP | Agent manually logs out from the Finesse Desktop using the default Logout (without any custom reason label) option. |
| 32767 | Logout | AGT_RELOGIN | Agent is logged in to one device (computer or phone) and tries to log in to a second device. |

| Attention | If an agent’s line is added to the restricted list, it affects the function of RmCm subsystem. |
|---|---|

| Attention | If an agent’s device is added to the Restricted list, it affects the function of RmCm subsystem. |
|---|---|

| Note | Your administrator can set the short term value to 5, 10 or 15 minutes. Long term value is set to 30 minutes. |
|---|---|

| Field | Description |
|---|---|
| CSQ Name | Name of the CSQ. |
| Waiting Calls | Number of calls in queue for a CSQ. |
| Longest Call in Queue | Elapsed wait time of the oldest call in the queue. |
| Agents Logged In | Number of agents in Logged-In state. |
| Agents Talking | Number of agents in Talking state. |
| Agents Ready | Number of agents in Ready state. |
| Agents Not Ready | Number of agents in Not Ready state. |
| Agents in After Call Work | Number of agents in Work state. |
| Agents Reserved | Number of agents in Reserved state. |

| Field | Description |
|---|---|
| CSQ Name | Name of the CSQ. |
| Calls Abandoned—Short Term | Number of abandoned calls in the last 5, 10 or 15 minutes. |
| Calls Abandoned—Long Term | Number of abandoned calls in the last 30 minutes. |
| Calls Dequeued—Short Term | Number of dequeued calls in the last 5, 10 or 15 minutes. |
| Calls Dequeued—Long Term | Number of dequeued calls in the last 30 minutes. |
| Average Contact Handling Time—Short Term | Average handle time of the calls that are routed to the CSQ in the last 5, 10 or 15 minutes. |
| Average Contact Handling Time—Long Term | Average handle time of the calls that are routed to the CSQ in the last 30 minutes. |
| Average Waiting Duration—Short Term | Average wait time of the calls that are routed to the CSQ in the last 5, 10 or 15 minutes. |
| Average Waiting Duration—Long Term | Average wait time of the calls that are routed to the CSQ in the last 30 minutes. |
| Service Level—Short Term | Service level is measured in the last 5, 10 or 15 minutes. The most recent service level is displayed in case there are no
                                             calls in the measurement window. |
| Service Level—Long Term | Service level in the last 30 minutes. |

| Field | Description |
|---|---|
| CSQ Name | Name of the CSQ. |
| Waiting Calls | Number of calls in queue for a CSQ. |
| Abandoned Calls | Number of calls that are abandoned for a CSQ. |
| Handled Calls | Number of calls that are answered by the agents in the CSQ. |
| Total Calls | Number of calls that are presented to the CSQ. |
| Longest Call in Queue | Longest wait time of any call before it is answered. |
| Longest Handle Time | Longest talk time of any call that the agent handled. |

| Filter parameter | Result |
|---|---|
| CSQ
                                             						Name | Displays information for the CSQs that belong to the specified
                                             						queues. |