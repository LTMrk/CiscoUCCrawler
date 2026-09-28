---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-crs-express-15-0-user-guide-uccx-b-1501-reportin-64e4f48e9a
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/crs/express_15_0/user/guide/uccx_b_1501_reporting_user_guide/uccx_m_125report-reference-values-list.html
retrieved_at: 2026-08-16T21:23:35.142320+00:00
---

Cisco Unified Contact Center Express Reporting User Guide, Release 15.0

# Cisco Unified Contact Center Express Reporting User Guide, Release 15.0

Updated: April 30, 2025

Chapter: Report Reference
	 Values List

## Chapter: Report Reference
	 Values List

- Report Reference                              	 Values List

- Report Reference                              	 Values List

# Report Reference
                     	 Values List

## Report Reference
                        	 Values List

### Call
                              		  Priority

Calls are assigned a default priority of 1, unless a different
                              		  priority is set in the workflow.

1 —Lowest.

10 —Highest.

N/A —Call is abandoned
                                    				before a priority is assigned.

### Call
                              		  Result

1 —Customer answers
                                    				and is connected to an agent.

2 — Fax machine or
                                    				modem is detected.

3 — Answering machine
                                    				is detected.

4 — Network reports an
                                    				invalid number.

5 —Customer does not
                                    				want to be called again.

6 —Call connected, but
                                    				wrong number.

7 —Call connected, but
                                    				reached the wrong person.

8 —Customer requests
                                    				callback.

11 —Busy tone is
                                    				detected.

15 —Customer phone
                                    				timed out because either the customer did not answer or there is a gateway
                                    				failure.

16 —Call is abandoned
                                    				because either the Interactive Voice Response (IVR) port is not available or
                                    				Unified CCX fails to transfer the call to the IVR port.

17 — Call failed due any one of the following reasons:

Dialer asked the Gateway to cancel a call that has not yet been placed

Gateway has declined the call

Gateway is down or Gateway has timed out while placing the call

Gateway failure or configuration issues at the Gateway.

After an Answering Machine is detected, the call is disconnected from the Gateway with a Bye request before the Termination Tone from Answering Machine is detected.

18 —Customer abandons
                                    				the call. Customer disconnects the call within the Abandoned Call Wait Time
                                    				that is configured in the Unified CCX Application Administration web interface.

### Call
                              		  Status

1 —Pending. Call is
                                    				pending.

2 —Active. Record is
                                    				sent to the outbound subsystem for dialing.

3 —Closed. Record is
                                    				closed.

4 —Callback. Record is
                                    				marked for a callback.

5 —Max Calls. Maximum
                                    				attempts are made for the record, so it is closed.

6 —Retry. Call is
                                    				redialed immediately whenever there is any miss in the callbacks for Retries
                                       				  with Delay .

7 —Unknown. If the
                                    				outbound system is restarted with active records then the records are moved to
                                    				Unknown state.

8 —Retries with Delay.
                                    				Call is redialed because the contact was either busy or did not answer, or the
                                    				customer or the system abandoned the call.

Retry time
                                    				is set according to the corresponding configuration in the Unified CCX
                                    				Application Administration web interface.

### Call Type

1 =
                                       				  Conference. —Conference call.

2 = Inbound
                                       				  ACD. —Unified CCX call that is handled by an agent.

3 = Inbound non-ACD on
                                       				  IPCC. —Non-Unified CCX call that is received by the agent on a Unified CCX
                                    				extension.

4 = Inbound non-ACD on
                                       				  non-IPCC. —Non-Unified CCX call that is received by the agent on a
                                    				non-Unified CCX extension.

5 = Outbound on
                                       				  IPCC. —Call that an agent dials on a Unified CCX extension.

6 = Outbound on
                                       				  non-IPCC. —Call that an agent dials on a non-Unified CCX extension.

7 = Transfer-In. —Call
                                    				that is transferred to an agent.

8 =
                                       				  Transfer-Out. —Call that the agent transfers out.

### Contact
                              		  Disposition

The following
                              		  are the contact dispositions and their respective values based on the outcome
                              		  of the call:

1 —Abandoned

2 —Handled

4 —Aborted

5 to 98 —Rejected

99 —Cleaned

### Contact
                              		  Type

1 = Incoming. Outside
                                    				call that is received by Unified CCX.

2 = Outgoing. Call
                                    				that originated from the Unified CCX Computer Telephony Interface (CTI) port,
                                    				other than the call that is made within the system.

3 = Internal. Call
                                    				that is transferred or conferenced between agents, or a call that is made
                                    				within the system.

4 = Redirect. A
                                    				previous call leg that redirected the call to this leg.

5 = Transfer-in. A
                                    				previous call leg that transferred the call to this leg.

6 = Preview Outbound. Call that originated from a Unified CCX agent phone to an outside destination,
                                    				after an agent accepts a preview call.

7 = IVR Outbound. Call that originated from a Unified CCX outbound dialer to an outside
                                    				destination for an IVR outbound campaign.

### Destination
                              		  Telephone Number / Destination DN and Destination Type

1 = Agent. Call that
                                    				is presented to an agent. Displays the Unified CCX extension or the non-Unified
                                    				CCX extension of the agent.

2 = Device. Call that
                                    				is presented to a route point. Displays the CTI port number that is associated
                                    				with the route point on which the call is answered.

3 = Unknown. Call
                                    				that is presented either to an outside destination through a gateway or to an
                                    				unmonitored device. Displays the telephone number that is dialed.

### Monitoring
                              		  Session Status

Normal –
                                       				  Monitored —Monitoring is completed successfully.

Normal – Agent
                                       				  RNA —Agent did not answer the call.

Error – Unable to Stop
                                       				  Monitoring —Supervisor presses the * key to terminate the monitoring session, but it
                                    				fails to terminate.

Error – Unable to Monitor
                                       				  New Call —Supervisor chooses to monitor a new call, but the system fails to
                                    				respond.

Error – Agent Logged
                                       				  Off —The agent whom supervisor wants to monitor has logged off.

Error – Network
                                       				  Problem —Monitoring session is not successful due to network problems.

Error – VoIP Server
                                       				  Unable to Communicate —Monitoring session is not successful because the
                                    				server with the Unified CCX Monitoring component fails to communicate.

Error – Monitoring Not
                                       				  Allowed —Supervisor attempts to monitor an agent or a CSQ that is not on the
                                    				Allowed list.

Error – Agent Not Logged
                                       				  In —The agent whom supervisor intends to monitor is not logged in.

Error – Invalid
                                       				  Input —Supervisor enters an input that the system does not recognize.

Error – Other —Errors
                                    				that are not defined in any of the above messages.

### Originator
                              		  Telephone Number / Originator DN and Originator Type

1= Agent. Call that
                                    				originated from an agent. Displays the Unified CCX extension of the agent.

2 = Device. Call that
                                    				originated from a device that is not associated to an agent or from a device
                                    				that is associated to an agent, but the agent is not currently logged in.
                                    				Displays the Computer Telephony Interface (CTI) port number that is associated
                                    				with the route point that the caller dialed.

3 = Unknown. Call
                                    				that originated from an outside caller through a gateway or from an unmonitored
                                    				device. Displays the telephone number of the caller.

### Predefined
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

Attention

If Allow Control of Device from CTI is not checked in the Default Device Profile Configuration window in Unified Communications Manager, the line remains restricted and cannot be controlled. You can modify this setting
                                          for devices that register with Unified Communications Manager. See the Cisco Unified
                                                   				  Communications Manager Administration Guide , located at: https://www.cisco.com/en/US/products/sw/voicesw/ps556/prod_maintenance_guides_list.html .

32754

Not Ready

DEVICE_RESTRICTED

Agent's device is flagged as a restricted device by the administrator of Unified Communications Manager.

Attention

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