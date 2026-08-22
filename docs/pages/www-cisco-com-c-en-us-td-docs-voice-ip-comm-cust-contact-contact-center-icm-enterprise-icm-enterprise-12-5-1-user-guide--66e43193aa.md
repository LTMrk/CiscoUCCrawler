---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-icm-enterprise-icm-enterprise-12-5-1-user-guide--66e43193aa
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/icm_enterprise/icm_enterprise_12_5_1/user/guide/ucce_b_ctios-supervisor-desktop-user-guide-125/ucce_b_ctios-supervisor-desktop-user-guide-125_chapter_011.html
retrieved_at: 2026-08-22T00:00:36.127542+00:00
---

CTIOS Supervisor Desktop User Guide

# CTIOS Supervisor Desktop User Guide

Updated: January 31, 2020

Chapter: Supervisor Softphone

## Chapter: Supervisor Softphone

# Supervisor Softphone

## Supervisor Softphone Capabilities

The Supervisor Softphone has all of the capabilities of an agent softphone and also includes functions that allow supervisors
                           to monitor and manage their agent team members.

Provides real-time agent status information of all agent members managed by the supervisor.

Provides call information (call data and events) of an actively monitored agent (that is, the agent currently selected in
                                    the Real-Time Statistics grid).

Supports call monitoring features (silent monitor, barge in, and intercept).

Supports emergency and supervisor assist calls.

Allows exchange of text messages between the supervisor and one of the agent team members (chat).

Allows the supervisor to change the agent state of a supervised agent to Logout or Ready, depending on the agent’s current
                                    state.

## Softphone User
                        	 Interface

The Supervisor
                           		Softphone is similar in appearance and operation to the Agent Softphone. The
                           		softphone buttons are grouped for login, agent state, dial/answer/release,
                           		hold/retrieve, alternate/reconnect, conference/transfer, and tools.

### Supervisor State
                           	 Control

Login . This
                                       			 section contains:

Login . Displays
                                             				  the Login window.

Logout .
                                             				  Displays the Logout window.

Agent State .
                                       			 This section contains:

Ready . Puts the
                                             				  supervisor in a ready state.

Not Ready . Puts
                                             				  the supervisor in a not ready state.

Wrap Up . Puts
                                             				  the supervisor in wrap up mode.

When a supervisor
                                          		  logs in to the Supervisor Desktop after an agent, the real-time agent state is
                                          		  displayed as Unknown (until there is a change in the agent’s
                                          		  state), instead of the existing state. However, if the supervisor logs in
                                          		  before an agent, the existing state is shown.

### Supervisor Call
                           	 Control

Dial . Initiate
                                       			 a new call.

Answer . Answer
                                       			 the selected call.

Release . Drop a
                                       			 selected call.

Hold . Put the
                                       			 selected call on hold.

Retrieve . Take
                                       			 back the call from the hold state.

Alternate . Put
                                       			 an active call on hold and retrieve the held call.

Reconnect . Drop
                                       			 the talking connection and reconnect to the held call.

Conference .
                                       			 Initiate a conference operation.

Transfer .
                                       			 Initiate a call transfer operation.

### Tools

Show
                                          				Statistics . Display the CTI Statistics window with Agent and Queues
                                       			 statistics.

Chat . Initiate
                                       			 a chat session with a specified agent.

Record . Record
                                       			 any call that appears in the supervisor’s call information display.

Bad Line . Log a
                                       			 poor-quality connection in the Unified CCE database.

### Call Information Grid

The Call Information Grid of the Supervisor Softphone displays call information about all supervisor calls. Any emergency
                              and assist calls appear in this grid and can then be answered by the supervisor.

### Supervisor Status Bar

The Supervisor Softphone has a status bar that appears at the bottom of the window.

## Process Calls

Make calls

Answer calls

Hang up calls

Transfer calls

Initiate conference calls

Send DTMF Tones

The following sections describe each function.

### Make Calls

Enter the Not Ready state.

Click Dial .

Enter the phone number to be dialed in the Number to Dial field or choose a destination from the drop-down menu. The drop-down menu contains the last six numbers dialed from this
                                          desktop.

Optionally, you can click More to see the following information:

This dialog box contains the Call Data tab, where you can optionally enter data associated with the call. When you finish, click Close .

Click Make Call .

### Answer Calls

To answer an incoming call, click Answer . When the call is answered, the Release button becomes enabled.

### Hang Up Calls

To hang up a call, click Release .

### Transfer Calls

Click Transfer .

Enter the phone number to be dialed in the Number to Dial field or choose a destination from the drop-down menu. The drop-down menu contains the last six numbers dialed from this
                                          desktop.

Optionally, you can click More to see additional information.

This dialog box contains the Call Data tab, where you can optionally enter data associated with the call.

Choose one:

- If you do not want to speak with the consulted agent, click Single Step . The call is transferred automatically.

- If you want to speak with the consulted agent, click Transf Init to put the call on hold. You can speak to the consulted agent before completing the transfer. When the consult call is answered, Transf Init changes to Transf Complete . To complete the transfer, click Transf Complete .

### Initiate Conference Calls

Click Conference .

Enter the phone number to be dialed in the Number to Dial field or choose a destination from the drop-down menu. The drop-down menu contains the last six numbers dialed from this
                                          desktop.

Optionally, you can click More to see additional information.

Click Conf Init . The call is now put on hold. You can speak to the consulted agent before completing the conference. When the consult call
                                          is answered, Conf Init changes to Conf Complete . To complete the conference, click Conf Complete .

When the conference operation is complete, the two calls then appear on the Call Information Grid as one call.

### Send DTMF
                           	 Tones

Choose an
                                          			 active call in the Call Information Grid.

Click Dial .

Enter or click
                                          			 the keypad button that corresponds to the digit or character for which you want
                                          			 to send a DTMF tone.

| Note | When a supervisor
                                          		  logs in to the Supervisor Desktop after an agent, the real-time agent state is
                                          		  displayed as Unknown (until there is a change in the agent’s
                                          		  state), instead of the existing state. However, if the supervisor logs in
                                          		  before an agent, the existing state is shown. |
|---|---|

| Step 1 | Enter the Not Ready state. |
|---|---|
| Step 2 | Click Dial . |
| Step 3 | Enter the phone number to be dialed in the Number to Dial field or choose a destination from the drop-down menu. The drop-down menu contains the last six numbers dialed from this
                                          desktop. Optionally, you can click More to see the following information: This dialog box contains the Call Data tab, where you can optionally enter data associated with the call. When you finish, click Close . |
| Step 4 | Click Make Call . |

| Step 1 | Click Transfer . |
|---|---|
| Step 2 | Enter the phone number to be dialed in the Number to Dial field or choose a destination from the drop-down menu. The drop-down menu contains the last six numbers dialed from this
                                          desktop. Optionally, you can click More to see additional information. This dialog box contains the Call Data tab, where you can optionally enter data associated with the call. |
| Step 3 | Choose one: If you do not want to speak with the consulted agent, click Single Step . The call is transferred automatically. If you want to speak with the consulted agent, click Transf Init to put the call on hold. You can speak to the consulted agent before completing the transfer. When the consult call is answered, Transf Init changes to Transf Complete . To complete the transfer, click Transf Complete . |

| Step 1 | Click Conference . |
|---|---|
| Step 2 | Enter the phone number to be dialed in the Number to Dial field or choose a destination from the drop-down menu. The drop-down menu contains the last six numbers dialed from this
                                          desktop. Optionally, you can click More to see additional information. |
| Step 3 | Click Conf Init . The call is now put on hold. You can speak to the consulted agent before completing the conference. When the consult call
                                          is answered, Conf Init changes to Conf Complete . To complete the conference, click Conf Complete . When the conference operation is complete, the two calls then appear on the Call Information Grid as one call. |

| Step 1 | Choose an
                                          			 active call in the Call Information Grid. |
|---|---|
| Step 2 | Click Dial . |
| Step 3 | Enter or click
                                          			 the keypad button that corresponds to the digit or character for which you want
                                          			 to send a DTMF tone. |