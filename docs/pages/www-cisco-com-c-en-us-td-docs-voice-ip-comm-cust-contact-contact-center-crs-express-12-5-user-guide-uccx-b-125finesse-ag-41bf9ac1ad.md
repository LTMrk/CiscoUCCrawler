---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-crs-express-12-5-user-guide-uccx-b-125finesse-ag-41bf9ac1ad
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/crs/express_12_5/user/guide/uccx_b_125finesse-agent-supervisor-desktop-guide/uccx_b_125finesse-agent-supervisor-desktop-guide_chapter_011.html
retrieved_at: 2026-08-16T21:24:51.641101+00:00
---

Cisco Finesse Agent and Supervisor Desktop User Guide for Cisco Unified Contact Center Express, Release 12.5(1)

# Cisco Finesse Agent and Supervisor Desktop User Guide for Cisco Unified Contact Center Express, Release 12.5(1)

Updated: February 9, 2020

Chapter: Call-Related
	 Tasks

## Chapter: Call-Related
	 Tasks

# Call-Related
                     	 Tasks

## Make a Call

Your status must be Ready or Not Ready to make an outgoing call.

Finesse supports the use of any ASCII character when you make a call. Finesse converts letters typed into the dial pad into
                                          numbers. It does not remove non-numeric characters (including parentheses and hyphens) from phone numbers. All alphabetical
                                          and special characters from the phone numbers including # , * , + , and : is supported.

Click the dialpad icon on the Cisco Finesse desktop.

The dialer dialog containing the keypad and a list of phone contacts is displayed. Your administrator assigns the phone contacts.

Click the contact from the list or manually enter the number into the dialpad to make a call.

Enter text in the search field to search the list of contacts. To edit the number before making a call, click the edit icon
                                                      next to the contact to populate the dialpad with the phone number.

To end the call, click End .

## Answer a Call

You must be in Ready state to be available for customer calls. When a call arrives at the desktop, your state automatically
                              changes to Reserved. A popover notification with configured customer details is displayed with the Answer button.

You can receive a call from another agent while you are in Not Ready state.

Sign in to the Finesse desktop using the URL: https://FQDN of Finesse Server:8445/desktop .

Click Answer in the notification popover.

Your state changes to Talking. You are connected to the caller. The configured call variables are displayed in the call control
                                          area and can be maximized or minimized, if required. This can be done by toggling the maximize/minimize arrow or clicking
                                          on call control. If a second call arrives on the desktop, the original call's call variables display is minimized.

To end the call, click End .

Your state changes to Ready and you are available for the next incoming call.

To be in Not Ready state when the call ends, click the drop-down arrow beside your state while you are on the call and choose
                                          Not Ready or Not Ready with the appropriate reason code. Your state changes to Talking->Not Ready (Pending). After the call
                                          ends, your state changes to Not Ready.

## Answer a Direct
                        	 Preview Outbound Call

A Direct Preview
                              		  Outbound call allows you to view a customer's contact information before you
                              		  choose to accept or decline the call.

Ensure your
                                       			 state is set to Ready. You must be in Ready state to receive a call.

When a Direct
                                          				Preview Outbound call arrives at the desktop, your state changes to Reserved
                                          				(Outbound). The Call Control gadget expands to show customer information.

After you
                                       			 review the information, click Accept to accept the call or click Decline to decline the call.

If you accept
                                          				the call, the system places the call to the customer directly from your phone.

If the attempt succeeds, you are connected to the customer. If
                                          				the attempt fails, Finesse places you in Ready state.

If you decline
                                          				the call, you must choose whether to reject or close the contact. If you click Reject , the contact remains in the campaign to be
                                          				retried at a later time. If you click Close , the contact is closed for the duration of the
                                          				campaign.

## Reclassify a
                        	 Direct Preview Outbound Call

The
                              		  Reclassify button allows you to reclassify a Direct Preview Outbound call as
                              		  Busy, Answering Machine, Fax, Invalid Number, or Voice. By default, a call is
                              		  classified as Voice. This button is available after you accept the Direct
                              		  Preview call and for the life of the call and while you are in the wrap-up
                              		  state. You can reclassify a call multiple times.

Answer a
                                       			 Direct Preview Outbound call.

Listen to the
                                       			 call. If you determine the number called is busy, an answering machine, a fax,
                                       			 or an invalid number, click Reclassify .

Choose the
                                       			 appropriate option from the resulting drop-down list.

To end the
                                       			 call, click End .

## Schedule a Callback

If you are on an Outbound Dialer call and the customer wants to be called back at a later time, you can schedule a callback.

While you are on the call, click Callback .

The Callback dialog box appears. The Current Time field contains the current time in the customer's time zone (this field
                                          is read-only).

If the customer prefers to be called back at a different phone number, enter the new phone number in the Phone Number field.

In the Date and Time fields, enter the date and time to call the customer. Type the date and time in to the respective fields
                                       or choose the date and time from the displayed calendar.

You must enter the time in the customer's location (not the time in your location).

You can toggle between AM or PM and click Enter .

The time corresponds to the customer's time zone. Finesse uses the customer's area code to determine the time zone. A customer
                                                      using a mobile phone may not be in the time zone that matches the area code of the phone. Therefore, you should confirm the
                                                      time zone with the customer.

Click Schedule .

If you need to update the information after you schedule a callback, click Callback to re-open the Callback dialog box.

Update the necessary fields and click Update .

If you need to cancel the callback after you schedule it, click Callback to re-open the Callback dialog box.

Click Cancel .

A message is displayed confirming that the callback has been canceled.

## Initiate a Consult Call

You must be on an active call to initiate a consult call.

Click Consult .

The dialer dialog containing the keypad and a list of phone contacts is displayed.

Choose the contact you want to consult from the list of contacts or enter the number into the dialpad.

On the dialpad, click Call .

The customer call is placed on hold and you are connected to the contact that you called.

After you consult with the contact that you called, you can choose to end the consult call and retrieve the customer call,
                                       conference the customer into the consult call, or transfer the customer to the agent or supervisor that you consulted.

To end the consult call and retrieve the customer call

Click End on the consult call and  click Retrieve on the customer call.

To place the other agent or supervisor on hold and go back to the customer

Click Retrieve on the customer call.

Click Retrieve on the consult call to place the customer on hold and go back to the other agent or supervisor.

To conference the customer into the consult call

Click Conference . If you want to leave the conference, click End .

To transfer the customer to the agent or supervisor you are consulting with

Click Transfer .

## Send DTMF

Use this feature to send a string of dual-tone multifrequency (DTMF) digits during a call. For example, you can use this feature
                              to interact with an interactive voice response (IVR) system to enter an account number or a password.

The Wrap-Up button and the call control buttons Hold , Transfer , Consult , and End are disabled across all calls when DTMF Keypad is opened, and until the responses to all DTMF requests are completed or have timed out. The number of outstanding requests
                              and the timeout duration is configured by your administrator.

You must be on an active call to use this feature.

Click Keypad .

The dialer dialog containing the keypad and a list of phone contacts are displayed.

Click the appropriate buttons on the dialpad to enter the DTMF digits.

You can send the following characters as part of a DTMF string:

0-9

pound sign (#)

asterisk (*)

The characters appear in the text field above the dialpad (this text field is read-only).

You can use the dialpad to enter the DTMF digits. You cannot type the DTMF digits using your keyboard.

Click Keypad again or click anywhere outside to close the dialpad.

## Apply Wrap-Up Reason

Wrap-up Reasons are applied to calls. If your administrator has assigned wrap-up reasons to you, the Wrap-Up Reason button
                              appears when you are on a call or when you are in Wrap-Up state after a call (if you are configured for Wrap-Up).

If you do not have any Wrap-Up Reasons assigned to you, you will not have this feature on your desktop. Your administrator
                              creates and assigns Wrap-Up Reasons.

Wrap-Up Reasons are set on per call basis. This means if you apply a wrap-up reason for a call, the same will be reflected
                                          on desktops of all other participants (agents) of the call.

You can enter a Wrap-Up Reason during a call or while you are in Wrap-Up state after the call ends (this includes normal call
                              termination as well as transfer and conference drop scenarios). If Wrap-Up is required, you automatically transition to Wrap-Up
                              state when the call ends. If wrap-up is optional, you can select Wrap-Up from the agent state drop-down during the call. Your
                              state then appears as Talking -> Wrap-Up (Pending) for the duration of the call. When the call ends, you transition to Wrap-Up
                              state and can complete any after call work.

If you want to specify what state to enter when the wrap-up timer expires, you can select the state from the drop-down before
                              you select Wrap-Up. For example, while on a call, select Not Ready from the drop-down. Then select Wrap-Up.

To end Wrap-Up state, select your new state (Ready or Not Ready) from the drop-down or wait for the preconfigured timer to
                              expire.

Once you enter a Wrap-Up state no further call updates will be made in the call control gadget. However, if you enter wrap-up
                                          reasons for the call while in wrap-up state, the call control gadget will be updated with the new wrap-up reason only; all
                                          other call information will remain as they were prior to entering the wrap-up state.

Click Wrap-Up .

You can either select the appropriate reasons by scrolling through the drop-down or use the provided search field in the Wrap-Up
                                       drop-down.

Click Apply .

A number appears on top of the Wrap-Up button indicating the number of wrap-up reasons Finesse successfully applied. You can apply maximum of five wrap-up reasons.
                                          The Wrap-Up reasons applied are displayed as a tag just below the search field in the Wrap-Up popover.

You can change the Wrap-Up reasons during the call. If you decide you want to use a different Wrap-Up reason, click the Wrap-Up button again, select new Wrap-Up reason, and click Apply .

If you want to cancel the Wrap-Up reasons, click Cancel to close the Wrap-Up popover.

## Force Wrap-Up

If your administrator has assigned wrap-up reasons and you wish to change your state from wrap-up to any other state, a tooltip
                              with the message Select Wrap-Up Reason is displayed. You cannot change your state unless the wrap-up reason is applied, or your timer expires and your state is
                              changed automatically.

The wrap-up timer is applicable when administrator has set the wrap-up time for the CSQ. When agents end a call, the wrap-up
                              timer starts the countdown and agents are required to wrap-up before the timer reaches zero.

For Example, if the timer is set to 30 seconds, the timer starts from 30 and ends on zero.

The wrap-up timer is displayed below the state.

## Initiate a Direct
                        	 Transfer Call

### Before you begin

You must be on an active call to initiate a direct transfer of a call.

Click Direct Transfer .

The call control area expands to reveal the keypad and a list of
                                          				contacts.

Choose the contact you want to transfer the call from the list of
                                       			 contacts or enter the number into the keypad.

On the keypad, click Call .

The customer call is transferred directly to another contact and
                                          				the call ends for you.

| Note | Finesse supports the use of any ASCII character when you make a call. Finesse converts letters typed into the dial pad into
                                          numbers. It does not remove non-numeric characters (including parentheses and hyphens) from phone numbers. All alphabetical
                                          and special characters from the phone numbers including # , * , + , and : is supported. |
|---|---|

| Step 1 | Click the dialpad icon on the Cisco Finesse desktop. The dialer dialog containing the keypad and a list of phone contacts is displayed. Your administrator assigns the phone contacts. |
|---|---|
| Step 2 | Click the contact from the list or manually enter the number into the dialpad to make a call. Note Enter text in the search field to search the list of contacts. To edit the number before making a call, click the edit icon
                                                      next to the contact to populate the dialpad with the phone number. | Note | Enter text in the search field to search the list of contacts. To edit the number before making a call, click the edit icon
                                                      next to the contact to populate the dialpad with the phone number. |
| Note | Enter text in the search field to search the list of contacts. To edit the number before making a call, click the edit icon
                                                      next to the contact to populate the dialpad with the phone number. |
| Step 3 | To end the call, click End . |

| Note | Enter text in the search field to search the list of contacts. To edit the number before making a call, click the edit icon
                                                      next to the contact to populate the dialpad with the phone number. |
|---|---|

| Note | You can receive a call from another agent while you are in Not Ready state. |
|---|---|

| Step 1 | Sign in to the Finesse desktop using the URL: https://FQDN of Finesse Server:8445/desktop . |
|---|---|
| Step 2 | Click Answer in the notification popover. Your state changes to Talking. You are connected to the caller. The configured call variables are displayed in the call control
                                          area and can be maximized or minimized, if required. This can be done by toggling the maximize/minimize arrow or clicking
                                          on call control. If a second call arrives on the desktop, the original call's call variables display is minimized. |
| Step 3 | To end the call, click End . Your state changes to Ready and you are available for the next incoming call. To be in Not Ready state when the call ends, click the drop-down arrow beside your state while you are on the call and choose
                                          Not Ready or Not Ready with the appropriate reason code. Your state changes to Talking->Not Ready (Pending). After the call
                                          ends, your state changes to Not Ready. |

| Step 1 | Ensure your
                                       			 state is set to Ready. You must be in Ready state to receive a call. When a Direct
                                          				Preview Outbound call arrives at the desktop, your state changes to Reserved
                                          				(Outbound). The Call Control gadget expands to show customer information. |
|---|---|
| Step 2 | After you
                                       			 review the information, click Accept to accept the call or click Decline to decline the call. If you accept
                                          				the call, the system places the call to the customer directly from your phone. If the attempt succeeds, you are connected to the customer. If
                                          				the attempt fails, Finesse places you in Ready state. If you decline
                                          				the call, you must choose whether to reject or close the contact. If you click Reject , the contact remains in the campaign to be
                                          				retried at a later time. If you click Close , the contact is closed for the duration of the
                                          				campaign. |

| Step 1 | Answer a
                                       			 Direct Preview Outbound call. |
|---|---|
| Step 2 | Listen to the
                                       			 call. If you determine the number called is busy, an answering machine, a fax,
                                       			 or an invalid number, click Reclassify . |
| Step 3 | Choose the
                                       			 appropriate option from the resulting drop-down list. The
                                       			 icon on the Reclassify button changes to the icon for the selected option. |
| Step 4 | To end the
                                       			 call, click End . |

| Step 1 | While you are on the call, click Callback . The Callback dialog box appears. The Current Time field contains the current time in the customer's time zone (this field
                                          is read-only). |
|---|---|
| Step 2 | If the customer prefers to be called back at a different phone number, enter the new phone number in the Phone Number field. |
| Step 3 | In the Date and Time fields, enter the date and time to call the customer. Type the date and time in to the respective fields
                                       or choose the date and time from the displayed calendar. You must enter the time in the customer's location (not the time in your location). You can toggle between AM or PM and click Enter . Note The time corresponds to the customer's time zone. Finesse uses the customer's area code to determine the time zone. A customer
                                                      using a mobile phone may not be in the time zone that matches the area code of the phone. Therefore, you should confirm the
                                                      time zone with the customer. | Note | The time corresponds to the customer's time zone. Finesse uses the customer's area code to determine the time zone. A customer
                                                      using a mobile phone may not be in the time zone that matches the area code of the phone. Therefore, you should confirm the
                                                      time zone with the customer. |
| Note | The time corresponds to the customer's time zone. Finesse uses the customer's area code to determine the time zone. A customer
                                                      using a mobile phone may not be in the time zone that matches the area code of the phone. Therefore, you should confirm the
                                                      time zone with the customer. |
| Step 4 | Click Schedule . |
| Step 5 | If you need to update the information after you schedule a callback, click Callback to re-open the Callback dialog box. |
| Step 6 | Update the necessary fields and click Update . |
| Step 7 | If you need to cancel the callback after you schedule it, click Callback to re-open the Callback dialog box. |
| Step 8 | Click Cancel . A message is displayed confirming that the callback has been canceled. |

| Note | The time corresponds to the customer's time zone. Finesse uses the customer's area code to determine the time zone. A customer
                                                      using a mobile phone may not be in the time zone that matches the area code of the phone. Therefore, you should confirm the
                                                      time zone with the customer. |
|---|---|

| Step 1 | Click Consult . The dialer dialog containing the keypad and a list of phone contacts is displayed. |
|---|---|
| Step 2 | Choose the contact you want to consult from the list of contacts or enter the number into the dialpad. |
| Step 3 | On the dialpad, click Call . The customer call is placed on hold and you are connected to the contact that you called. |
| Step 4 | After you consult with the contact that you called, you can choose to end the consult call and retrieve the customer call,
                                       conference the customer into the consult call, or transfer the customer to the agent or supervisor that you consulted. Option Description To end the consult call and retrieve the customer call Click End on the consult call and  click Retrieve on the customer call. To place the other agent or supervisor on hold and go back to the customer Click Retrieve on the customer call. Click Retrieve on the consult call to place the customer on hold and go back to the other agent or supervisor. To conference the customer into the consult call Click Conference . If you want to leave the conference, click End . To transfer the customer to the agent or supervisor you are consulting with Click Transfer . | Option | Description | To end the consult call and retrieve the customer call | Click End on the consult call and  click Retrieve on the customer call. | To place the other agent or supervisor on hold and go back to the customer | Click Retrieve on the customer call. Click Retrieve on the consult call to place the customer on hold and go back to the other agent or supervisor. | To conference the customer into the consult call | Click Conference . If you want to leave the conference, click End . | To transfer the customer to the agent or supervisor you are consulting with | Click Transfer . |
| Option | Description |
| To end the consult call and retrieve the customer call | Click End on the consult call and  click Retrieve on the customer call. |
| To place the other agent or supervisor on hold and go back to the customer | Click Retrieve on the customer call. Click Retrieve on the consult call to place the customer on hold and go back to the other agent or supervisor. |
| To conference the customer into the consult call | Click Conference . If you want to leave the conference, click End . |
| To transfer the customer to the agent or supervisor you are consulting with | Click Transfer . |

| Option | Description |
|---|---|
| To end the consult call and retrieve the customer call | Click End on the consult call and  click Retrieve on the customer call. |
| To place the other agent or supervisor on hold and go back to the customer | Click Retrieve on the customer call. Click Retrieve on the consult call to place the customer on hold and go back to the other agent or supervisor. |
| To conference the customer into the consult call | Click Conference . If you want to leave the conference, click End . |
| To transfer the customer to the agent or supervisor you are consulting with | Click Transfer . |

| Note | You must be on an active call to use this feature. |
|---|---|

| Step 1 | Click Keypad . The dialer dialog containing the keypad and a list of phone contacts are displayed. |
|---|---|
| Step 2 | Click the appropriate buttons on the dialpad to enter the DTMF digits. You can send the following characters as part of a DTMF string: 0-9 pound sign (#) asterisk (*) The characters appear in the text field above the dialpad (this text field is read-only). Note You can use the dialpad to enter the DTMF digits. You cannot type the DTMF digits using your keyboard. | Note | You can use the dialpad to enter the DTMF digits. You cannot type the DTMF digits using your keyboard. |
| Note | You can use the dialpad to enter the DTMF digits. You cannot type the DTMF digits using your keyboard. |
| Step 3 | Click Keypad again or click anywhere outside to close the dialpad. |

| Note | You can use the dialpad to enter the DTMF digits. You cannot type the DTMF digits using your keyboard. |
|---|---|

| Note | Wrap-Up Reasons are set on per call basis. This means if you apply a wrap-up reason for a call, the same will be reflected
                                          on desktops of all other participants (agents) of the call. |
|---|---|

| Note | Once you enter a Wrap-Up state no further call updates will be made in the call control gadget. However, if you enter wrap-up
                                          reasons for the call while in wrap-up state, the call control gadget will be updated with the new wrap-up reason only; all
                                          other call information will remain as they were prior to entering the wrap-up state. |
|---|---|

| Step 1 | Click Wrap-Up . |
|---|---|
| Step 2 | You can either select the appropriate reasons by scrolling through the drop-down or use the provided search field in the Wrap-Up
                                       drop-down. |
| Step 3 | Click Apply . A number appears on top of the Wrap-Up button indicating the number of wrap-up reasons Finesse successfully applied. You can apply maximum of five wrap-up reasons.
                                          The Wrap-Up reasons applied are displayed as a tag just below the search field in the Wrap-Up popover. Note You can change the Wrap-Up reasons during the call. If you decide you want to use a different Wrap-Up reason, click the Wrap-Up button again, select new Wrap-Up reason, and click Apply . If you want to cancel the Wrap-Up reasons, click Cancel to close the Wrap-Up popover. | Note | You can change the Wrap-Up reasons during the call. If you decide you want to use a different Wrap-Up reason, click the Wrap-Up button again, select new Wrap-Up reason, and click Apply . If you want to cancel the Wrap-Up reasons, click Cancel to close the Wrap-Up popover. |
| Note | You can change the Wrap-Up reasons during the call. If you decide you want to use a different Wrap-Up reason, click the Wrap-Up button again, select new Wrap-Up reason, and click Apply . If you want to cancel the Wrap-Up reasons, click Cancel to close the Wrap-Up popover. |

| Note | You can change the Wrap-Up reasons during the call. If you decide you want to use a different Wrap-Up reason, click the Wrap-Up button again, select new Wrap-Up reason, and click Apply . If you want to cancel the Wrap-Up reasons, click Cancel to close the Wrap-Up popover. |
|---|---|

| Step 1 | Click Direct Transfer . The call control area expands to reveal the keypad and a list of
                                          				contacts. |
|---|---|
| Step 2 | Choose the contact you want to transfer the call from the list of
                                       			 contacts or enter the number into the keypad. |
| Step 3 | On the keypad, click Call . The customer call is transferred directly to another contact and
                                          				the call ends for you. |