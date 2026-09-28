---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-icm-enterprise-icm-enterprise-12-5-1-user-guide--c8eb3a15b2
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/icm_enterprise/icm_enterprise_12_5_1/user/guide/ucce_b_ctios-supervisor-desktop-user-guide-125/ucce_b_ctios-supervisor-desktop-user-guide-125_chapter_010.html
retrieved_at: 2026-08-22T00:00:32.178481+00:00
---

CTIOS Supervisor Desktop User Guide

# CTIOS Supervisor Desktop User Guide

Updated: January 31, 2020

Chapter: Supervisor Desktop

## Chapter: Supervisor Desktop

- Supervisor Desktop

- Supervisor                              	 Softphone Login

- Log Out of the Supervisor Softphone

# Supervisor Desktop

## Supervisor
                        	 Softphone Login

After the CTI
                           		Toolkit Supervisor Desktop software installation is complete, you can start the
                           		Supervisor Softphone by selecting Start
                              		  > All Programs > Cisco Systems CTI Toolkit
                              		  > Unified CC Supervisor Desktop.

Upon startup, the
                           		Supervisor Softphone and Team Real-Time Status windows appear.

To log in to the
                           		Supervisor Softphone, click Login ; the Login dialog box appears. Logging in connects you to
                           		the CTI OS Server and allows you to use a selected connection profile.

The Login dialog box varies for different peripheral types. For additional information, refer to the CTI OS Agent Desktop User Guide for Cisco Unified ICM at http://www.cisco.com/c/en/us/support/customer-collaboration/computer-telephony-integration-option/products-user-guide-list.html .

Enter the following
                           		information in the dialog box:

Connect to. The connection profile that you want to use. (Use the
                                 			 drop-down menu to choose a profile.)

Agent ID. Your agent ID as assigned by your manager.

Depending on
                                             				the option chosen for logging in during the installation of the CTI OS Server,
                                             				the Login dialog box on the Supervisor desktop prompts
                                             				for either the Agent ID or the Login Name.

Password. Your password as assigned by your manager.

Instrument. The device ID assigned to the phone set you receive calls
                                 			 on.

The fields in
                                             				the Mobile Agent section of the dialog box are accessible only if Mobile Agent
                                             				was enabled during the CTI OS Server installation.

Mobile Agent. Check this box if you are logging in as a Mobile Agent
                                 			 (that is, if you are logging in to a phone that is not directly controlled by
                                 			 Cisco Unified Communications Manager). In the Mobile
                                    				Agent section of the dialog box, enter the phone number that the
                                 			 Mobile Agent is using to receive calls. Enter the number in the same format as
                                 			 you would dial it from an IP Phone, unless your system administrator instructs
                                 			 you to enter the number in another format.

CTI OS does
                                             				not validate Mobile Agent phone numbers upon login. Take care to ensure that
                                             				the number you enter is valid and correct. Otherwise, a scenario results in
                                             				which the CTI OS desktop shows the incoming call, but the customer only hears
                                             				ringing out and the agent phone does not ring because the destination number is
                                             				not correct.

Choose one of
                                 			 the following Call Mode values from the drop-down menu:

Call-by-Call Agent’s phone is dialed for each incoming call.

Nailed Connection Agent’s phone is dialed once immediately after login and
                                 			 remains connected through multiple customer calls.

The instructions
                                       		  that are described in this document for using your agent or supervisor desktop
                                       		  do not address important differences that may apply when you log in as a Mobile
                                       		  Agent. For instructions on using your desktop when you log in as a Mobile
                                       		  Agent, please consult the Cisco Unified Contact Center Enterprise Features Guide at http://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-feature-guides-list.html .

Enter the
                           		information and click OK . After a successful login, the following events
                           		occur:

The supervisor
                                 			 automatically goes into the Not Ready state.

Agent ID for
                                          				  the logged-in supervisor

Supervisor’s
                                          				  extension

Supervisor’s
                                          				  instrument

Current
                                          				  supervisor status

The server
                                          				  that the supervisor is connected to

The Ready , Dial , and Logout agent state control buttons are enabled.

If a
                                       		  non-supervisor logs in to the Supervisor Softphone, the Real-Time Statistics
                                       		  grid remains blank. With the exception of this one variation, the Supervisor
                                       		  Softphone functions the same as the agent softphone.

## Log Out of the Supervisor Softphone

Start the logout process one of two ways:

- If Logout is enabled, click it. Unified CCE /CCH requires that an agent be in Not Ready state to log out; therefore, Logout is disabled if the agent is in any other state. In this case, click Not Ready first, then click Logout .

- If you click Not Ready first, a Select Reason Code dialog box might appear next, depending on how your administrator has configured your agent settings. This dialog box includes
                                          a drop-down list of reason codes.

Choose a reason code from the drop-down list.

Click OK . When you enter Not Ready state, Logout becomes enabled.

Click Logout . Depending on how your administrator has configured your agent settings, a Select Reason Code dialog box might appear next. This dialog box includes a drop-down list of defined reason codes.

Choose a reason code from the drop-down list.

Click OK .

### What to do next

After a successful logout, the following occurs:

You are logged out of CTI OS and Unified Contact Center.

All entries in the status bar at the bottom of the CTI Toolkit Supervisor Desktop window become blank.

All the agent state control buttons except Login are disabled.

All Call Control buttons are disabled.

In a Mobile Agent environment, if a Nailed-up mobile agent connection is dropped (for example, when disconnecting the phone),
                                          the agent is logged out automatically.

| Note | The Login dialog box varies for different peripheral types. For additional information, refer to the CTI OS Agent Desktop User Guide for Cisco Unified ICM at http://www.cisco.com/c/en/us/support/customer-collaboration/computer-telephony-integration-option/products-user-guide-list.html . |
|---|---|

| Note | Depending on
                                             				the option chosen for logging in during the installation of the CTI OS Server,
                                             				the Login dialog box on the Supervisor desktop prompts
                                             				for either the Agent ID or the Login Name. |
|---|---|

| Note | The fields in
                                             				the Mobile Agent section of the dialog box are accessible only if Mobile Agent
                                             				was enabled during the CTI OS Server installation. |
|---|---|

| Note | CTI OS does
                                             				not validate Mobile Agent phone numbers upon login. Take care to ensure that
                                             				the number you enter is valid and correct. Otherwise, a scenario results in
                                             				which the CTI OS desktop shows the incoming call, but the customer only hears
                                             				ringing out and the agent phone does not ring because the destination number is
                                             				not correct. |
|---|---|

| Note | The instructions
                                       		  that are described in this document for using your agent or supervisor desktop
                                       		  do not address important differences that may apply when you log in as a Mobile
                                       		  Agent. For instructions on using your desktop when you log in as a Mobile
                                       		  Agent, please consult the Cisco Unified Contact Center Enterprise Features Guide at http://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-feature-guides-list.html . |
|---|---|

| Note | If a
                                       		  non-supervisor logs in to the Supervisor Softphone, the Real-Time Statistics
                                       		  grid remains blank. With the exception of this one variation, the Supervisor
                                       		  Softphone functions the same as the agent softphone. |
|---|---|

| Step 1 | Start the logout process one of two ways: If Logout is enabled, click it. Unified CCE /CCH requires that an agent be in Not Ready state to log out; therefore, Logout is disabled if the agent is in any other state. In this case, click Not Ready first, then click Logout . If you click Not Ready first, a Select Reason Code dialog box might appear next, depending on how your administrator has configured your agent settings. This dialog box includes
                                          a drop-down list of reason codes. |
|---|---|
| Step 2 | Choose a reason code from the drop-down list. |
| Step 3 | Click OK . When you enter Not Ready state, Logout becomes enabled. |
| Step 4 | Click Logout . Depending on how your administrator has configured your agent settings, a Select Reason Code dialog box might appear next. This dialog box includes a drop-down list of defined reason codes. |
| Step 5 | Choose a reason code from the drop-down list. |
| Step 6 | Click OK . |

| Note | In a Mobile Agent environment, if a Nailed-up mobile agent connection is dropped (for example, when disconnecting the phone),
                                          the agent is logged out automatically. |
|---|---|