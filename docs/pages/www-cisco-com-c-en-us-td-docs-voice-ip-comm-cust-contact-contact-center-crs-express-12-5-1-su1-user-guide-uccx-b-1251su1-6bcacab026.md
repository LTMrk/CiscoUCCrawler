---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-crs-express-12-5-1-su1-user-guide-uccx-b-1251su1-6bcacab026
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/crs/express_12_5_1_su1/user/guide/uccx_b_1251su1finesse-agent-supervisor-desktop-guide/uccx_b_1252finesse-agent-supervisor-desktop-guide_chapter_0110.html
retrieved_at: 2026-08-16T21:25:51.684589+00:00
---

Cisco Finesse Agent and Supervisor Desktop User Guide for Cisco Unified Contact Center Express, Release 12.5(1)SU1

# Cisco Finesse Agent and Supervisor Desktop User Guide for Cisco Unified Contact Center Express, Release 12.5(1)SU1

Updated: February 1, 2021

Chapter: Finesse IP Phone Agent Tasks

## Chapter: Finesse IP Phone Agent Tasks

# Finesse IP Phone Agent Tasks

## Finesse IP Phone Agent

With Finesse IP Phone Agent (IPPA), you can access Finesse features on your Cisco IP Phone as an alternative to accessing
                              Finesse through your browser. Finesse IPPA supports fewer features when compared to the Finesse desktop in the browser, but
                              it does allow you to receive and manage Finesse calls if you lose or do not have access to a computer.

### Supervisor Tasks

Finesse IPPA does not support supervisor tasks such as monitor, barge, and intercept, but supervisors can sign in and perform
                              all agent tasks on their IP Phones.

To perform supervisor tasks for Finesse IPPA agents, supervisors must sign in to the Finesse desktop and follow the same steps
                              that they use for the Finesse desktop agents (currently restricted to viewing team performance and changing an agent's state).

### Agent Tasks

The following table provides a quick reference for common agent tasks:

Task

Steps

Sign In

Press Services > Cisco Finesse .

Enter your ID, password, and extension.

Press SignIn .

Change State

Press Ready or NotReady .

Apply Wrap-Up Reasons

Press WrapUp and select from the list.

CData

Press CData from the queue statistics screen during the call to view Call Data information.

View Queue Statistics data

Press QStats from the Call Data screen during the call to view queue statistics data.

Refresh

Press Refresh to view the latest queue statistics data during the call.

Sign Out

From the Not Ready state, press SignOut .

For more information about agent tasks, see the following sections.

## Sign In to Finesse on the IP Phone

### Before you begin

Your administrator must set up your Finesse IPPA access.

On your IP Phone, press the Services button.

The example figures shown in this procedure may differ from your phone's layout and display.

Select Cisco Finesse .

Enter your agent ID (or username), password, and extension, and press SignIn .

The ID (Finesse IPPA) in Unified CCX deployments refers to the AgentID.

Your State : Current call state - Ready or Not Ready (Your call state is Not Ready by default. Press Ready to change the state).

Calls Queued : Number of calls waiting across queues assigned to you.

Longest Queue Time : Longest queue time across queues assigned to you.

Last Updated : Last refreshed time of the Queue Statistics data (auto update happens every 15 seconds).

While in talking state, if you wish to view queue statistics data from the call data screen, press QStats .

To go back to the call data screen, press CData .

Your administrator can set up your phone with One Button Sign In, which allows you to sign in without specifying your ID,
                                          password, or extension. In this case, when you select Finesse from the Services menu, Finesse IPPA automatically enters your
                                          sign-in information, and you move directly to the home screen. Finesse IPPA One Button log in can also be configured by the
                                          Administrator with only some of the parameters like ID and Extension. In this case, you must enter only your password to sign
                                          in.

When signing out from the Finesse IPPA application, the Sign In page is displayed. Click on the Exit button to ensure that Single-Sign On works correctly the next time you log in to the Cisco Finesse application.

## Change State on the IP Phone

When you sign in to Finesse on the IP Phone, your initial state is set to Not Ready. To receive calls, set your state to Ready.

While you are on a call, you can set the state that will apply when the call is complete. In this case, Finesse shows your
                              current state and the pending state that Finesse applies after the call ends.

To set your state to Ready, press the Ready button.

To set your state to Not Ready, press the NotReady button.

If Not Ready reason codes appear, scroll to the desired reason, and press the Select button.

After the call ends, you can change your selected reason code by pressing the NotReady button again and selecting a different reason.

## Apply Wrap-Up Reason on the IP Phone

A Wrap-Up reason indicates why a customer called the contact center. For example, you can have one Wrap-Up reason for sales
                              calls and another for support calls.

Your administrator can assign Wrap-Up reasons to you. In this case, the WrapUp button appears when you are on a call or while
                              you are in Wrap-Up state after the call ends.

When you are on a call (talking state), the WrapUp button is displayed with the Ready and Not Ready buttons. You can select
                                          the WrapUp reason before ending the call.

If you do not select the Wrap-Up reason before ending the call, and if Wrap-Up reason is configured for you by the administrator,
                                          then WrapUp button is displayed after you end the call. You can now select the Wrap-Up reason.

If the administrator has not configured Wrap-Up reasons for you, the WrapUp button is not displayed.

Press WrapUp during or after the call and select a Wrap-Up reason from the list.

To end the Wrap-Up state after the call ends, select your new state (Ready or NotReady) or wait for the preconfigured timer
                                       to expire.

While you are on a call, you can specify the next state to apply after Wrap-Up by selecting that state first. For example,
                              while on a call, select NotReady and then select WrapUp . When the call ends, you enter the Wrap-Up state with a pending state of Not Ready. When the Wrap-Up timer expires, you enter
                              the Not Ready state.

You cannot enter a Wrap-Up reason after you transfer a call. To enter a Wrap-Up reason for a call you transfer, select the
                              Wrap-Up reason while the call is in progress.

## Sign Out of Finesse on the IP Phone

### Before you begin

You must be in the Not Ready state to sign out.

Press the SignOut button.

If Sign Out reason codes appear, select the desired Sign Out reason, and press the Select button.

## Recover Finesse IP Phone Agent Service After Failure

If the Finesse server you are currently signed in to goes out of service, the IP Phone displays an error indicating the Finesse
                              service is unavailable. Unlike the Finesse desktop, the Finesse IP Phone Agent does not automatically failover to the alternate
                              Finesse server. To resume normal operations, exit from the current Finesse IP Phone service and manually sign in to an alternate
                              Finesse IP Phone service.

Press Retry to retry the current Finesse service.

If the issue is not resolved, sign in to an alternate Finesse service:

Press Exit to exit the current Finesse service.

Press the Services button.

Select an alternate Cisco Finesse service from the menu.

Enter your agent ID, password, and extension, and press the SignIn button.

If none of the available Finesse services allow you to connect, contact your administrator.

If your IP Phone displays pending state information when you lose connection with the Finesse service, that state information
                                                is lost when you sign in again.

## Set Finesse Service and Credentials Using the Self Care Portal

Your administrator may ask you to subscribe your phone to the Finesse service using the Unified CM Self Care Portal. If your
                              administrator sets up One Button Sign In, they may also ask you to enter your ID, extension, or password in the Unified CM
                              Self Care Portal. (Finesse IPPA can then enter these credentials for you automatically each time you sign in.)

Use your ID and password to sign in to the Self Care Portal from the following URL:

http:// UCM address /ucmuser

Where UCM address is the address of Cisco Unified CM provided by your administrator.

On the Self Care Portal, navigate to Phones > Phone Settings > Services .

Select the phone that you want to subscribe to the Finesse service.

If your administrator has already subscribed this phone to the Finesse service, click the Edit Service icon for the Finesse service, and go to Step 7. Else, go to Step 5.

Click Add New Service for the phone and select the Finesse service from the drop-down.

In the Display Name field, enter Cisco Finesse (or another display name that is appropriate for your phone).

If your administrator requests that you enter your credentials, enter the required values for your agent id, password, and
                                       extension.

Click Save .

### What to do next

If your administrator has also set up a secondary Finesse service as a backup, perform these steps again on the secondary
                              service.

## Finesse IPPA Behavior

The following notes describe how Finesse IPPA behaves when you perform certain agent tasks.

### Call Data Display

When you make or receive a call, Finesse IPPA displays call data on the phone based on the administrator-defined layout.
                                    Unlike the Finesse desktop, Finesse IPPA displays all call data in one column. The display order relative to the Finesse desktop
                                    is: header, left column, right column. You can scroll to view the data as required.

When you are on multiple calls (such as a consult call), Finesse IPPA displays call data for the active call. If all calls
                                    are on hold, Finesse IPPA displays call data for the last active call.

Some IP Phone models display the Finesse IPPA screen and not the home screen during an ACD incoming call. You cannot accept
                                    the call as the Answer and Decline soft keys are not enabled in the Finesse IPPA screen. To answer the call:

Press the hard key on the top right of the IP Phone.

Use the phone handset.

Press the speaker button.

You cannot end an active call as the End soft key is not enabled in the Finesse IPPA screen. To end a call:

Press End button on the IP Phone.

Press the speaker button.

### Phone Behavior When You Make a Call

If you make a call from the Ready state, Finesse IPPA changes your state to Not Ready and displays the Finesse screen. Similarly,
                                    if you make a call without first navigating to the home phone screen, sometimes the IP Phone changes the display to the Finesse
                                    screen. In either case, to view the dialed numbers, navigate back to the home phone screen.

If you call a busy number, the IP Phone first displays a Busy message, and then Finesse displays a Talking message until you end the call. You can safely ignore the Talking message.

### Reserved and Hold State Not Displayed

Unlike the Finesse desktop, Finesse IPPA does not display Reserved or Hold states. Instead, Finesse IPPA continues to display
                                    the previous state that applied (for example, Ready or Talking) before you move to reserved or are on hold. The one exception
                                    to this behavior occurs when you receive a direct call from another agent while in the Not Ready state. In this case, Finesse
                                    IPPA continues to display the Not Ready state.

### No Wrap Up on Transferred Calls

If you transfer a call, you cannot set any Wrap Up data for the call even if Finesse IPPA shows you in the Wrap Up state.
                                    To enter a Wrap Up reason for a transferred call, select the Wrap Up reason while the call is in progress.

### Additional Finesse IPPA Behavior

The Simplified New Call UI is currently not supported in Finesse IPPA. Enabling this feature will not allow the agent to make
                                    outbound calls in READY state.

Finesse IPPA is not supported on VPN.

When Finesse IPPA phone is powered off or reset, you will be logged out of the physical device.

| Task | Steps |
|---|---|
| Sign In | Press Services > Cisco Finesse . Enter your ID, password, and extension. Press SignIn . |
| Change State | Press Ready or NotReady . |
| Apply Wrap-Up Reasons | Press WrapUp and select from the list. |
| CData | Press CData from the queue statistics screen during the call to view Call Data information. |
| View Queue Statistics data | Press QStats from the Call Data screen during the call to view queue statistics data. |
| Refresh | Press Refresh to view the latest queue statistics data during the call. |
| Sign Out | From the Not Ready state, press SignOut . |

| Step 1 | On your IP Phone, press the Services button. Note The example figures shown in this procedure may differ from your phone's layout and display. | Note | The example figures shown in this procedure may differ from your phone's layout and display. |
|---|---|---|---|
| Note | The example figures shown in this procedure may differ from your phone's layout and display. |
| Step 2 | Select Cisco Finesse . |
| Step 3 | Enter your agent ID (or username), password, and extension, and press SignIn . Note The ID (Finesse IPPA) in Unified CCX deployments refers to the AgentID. The home screen appears and the following options on queue statistics is displayed: Your State : Current call state - Ready or Not Ready (Your call state is Not Ready by default. Press Ready to change the state). Calls Queued : Number of calls waiting across queues assigned to you. Longest Queue Time : Longest queue time across queues assigned to you. Last Updated : Last refreshed time of the Queue Statistics data (auto update happens every 15 seconds). | Note | The ID (Finesse IPPA) in Unified CCX deployments refers to the AgentID. |
| Note | The ID (Finesse IPPA) in Unified CCX deployments refers to the AgentID. |
| Step 4 | While in talking state, if you wish to view queue statistics data from the call data screen, press QStats . |
| Step 5 | To go back to the call data screen, press CData . |

| Note | The example figures shown in this procedure may differ from your phone's layout and display. |
|---|---|

| Note | The ID (Finesse IPPA) in Unified CCX deployments refers to the AgentID. |
|---|---|

| Note | Your administrator can set up your phone with One Button Sign In, which allows you to sign in without specifying your ID,
                                          password, or extension. In this case, when you select Finesse from the Services menu, Finesse IPPA automatically enters your
                                          sign-in information, and you move directly to the home screen. Finesse IPPA One Button log in can also be configured by the
                                          Administrator with only some of the parameters like ID and Extension. In this case, you must enter only your password to sign
                                          in. When signing out from the Finesse IPPA application, the Sign In page is displayed. Click on the Exit button to ensure that Single-Sign On works correctly the next time you log in to the Cisco Finesse application. |
|---|---|

| Step 1 | To set your state to Ready, press the Ready button. |
|---|---|
| Step 2 | To set your state to Not Ready, press the NotReady button. |
| Step 3 | If Not Ready reason codes appear, scroll to the desired reason, and press the Select button. After the call ends, you can change your selected reason code by pressing the NotReady button again and selecting a different reason. |

| Note | When you are on a call (talking state), the WrapUp button is displayed with the Ready and Not Ready buttons. You can select
                                          the WrapUp reason before ending the call. If you do not select the Wrap-Up reason before ending the call, and if Wrap-Up reason is configured for you by the administrator,
                                          then WrapUp button is displayed after you end the call. You can now select the Wrap-Up reason. If the administrator has not configured Wrap-Up reasons for you, the WrapUp button is not displayed. |
|---|---|

| Step 1 | Press WrapUp during or after the call and select a Wrap-Up reason from the list. |
|---|---|
| Step 2 | To end the Wrap-Up state after the call ends, select your new state (Ready or NotReady) or wait for the preconfigured timer
                                       to expire. |

| Step 1 | Press the SignOut button. |
|---|---|
| Step 2 | If Sign Out reason codes appear, select the desired Sign Out reason, and press the Select button. |

| Step 1 | Press Retry to retry the current Finesse service. |
|---|---|
| Step 2 | If the issue is not resolved, sign in to an alternate Finesse service: Press Exit to exit the current Finesse service. Press the Services button. Select an alternate Cisco Finesse service from the menu. Enter your agent ID, password, and extension, and press the SignIn button. |

| Note | If none of the available Finesse services allow you to connect, contact your administrator. If your IP Phone displays pending state information when you lose connection with the Finesse service, that state information
                                                is lost when you sign in again. |
|---|---|

| Step 1 | Use your ID and password to sign in to the Self Care Portal from the following URL: http:// UCM address /ucmuser Where UCM address is the address of Cisco Unified CM provided by your administrator. |
|---|---|
| Step 2 | On the Self Care Portal, navigate to Phones > Phone Settings > Services . |
| Step 3 | Select the phone that you want to subscribe to the Finesse service. |
| Step 4 | If your administrator has already subscribed this phone to the Finesse service, click the Edit Service icon for the Finesse service, and go to Step 7. Else, go to Step 5. |
| Step 5 | Click Add New Service for the phone and select the Finesse service from the drop-down. |
| Step 6 | In the Display Name field, enter Cisco Finesse (or another display name that is appropriate for your phone). |
| Step 7 | If your administrator requests that you enter your credentials, enter the required values for your agent id, password, and
                                       extension. |
| Step 8 | Click Save . |