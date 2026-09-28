---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-managed-services-12-5-1-cucm-b-manager-assistant-user-guide-1251-cucm-b-816ecaf22a
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/managed_services/12_5_1/cucm_b_manager-assistant-user-guide-1251/cucm_b_manager-assistant-user-guide-1251_chapter_011.html
retrieved_at: 2026-08-21T01:28:42.247603+00:00
---

Manager Assistant User Guide for Cisco Unified Communications Manager, Release 12.5(1)

# Manager Assistant User Guide for Cisco Unified Communications Manager, Release 12.5(1)

Updated: January 22, 2019

Chapter: Use Assistant Console to Handle Calls

## Chapter: Use Assistant Console to Handle Calls

# Use Assistant Console to Handle Calls

## Use Assistant Console to Handle Calls

You can use your
                           		mouse and keyboard to place, answer, transfer, end, and generally handle calls
                           		from the Assistant Console.

Make sure that the  call you
                           		want to handle is selected (highlighted) on the console. Call-control buttons
                           		and menu items appear dimmed (inactive) if they are not relevant to the
                           		selected call.

## Place a Call

To place a call from the Assistant Console:

Select one of the options to place a call:

- Click the Dial call-control button.

- Right-click a phone line in the My Calls panel and select Dial from the popup menu.

- From the menu bar, choose Call > Dial .

- Double-click  speed dial or directory number.

- Drag directory number into the My Calls panel.

- Use the associated keyboard shortcut.

- With the console open and active on your desktop, enter the phone number that you want to call using your keyboard and then
                                          press Enter . You will see the number that you are calling in the status bar along the bottom of the console.

- If the Enter Number popup window appears, enter the phone number that you want to call and click OK . Enter the number exactly as you would if you were placing the call from your Cisco Unified IP Phone .

Calls originated from Assistant Console use the first physical line of the assistant phone.

## Answer a Call

To answer a selected call:

Select one of the options to answer a call:

- Click the Answer call-control button.

- In the My Calls panel, double-click a ringing call.

- Right-click the call and choose Answer from the popup menu.

- From the menu bar, choose Call > Answer .

- Use the associated keyboard shortcut.

- If the incoming call that you want to answer is not selected, click the incoming call to select it to answer the call.

## End a Call

To end a selected call:

Select one of the options to end a call:

- Click the Hang Up call-control button.

- Click the Hang Up call-control button.

- From the menu bar, choose Call > Hang Up .

- Use the associated keyboard shortcut.

## Put Calls On Hold

To put a selected call on hold:

Select one of the options to put calls on hold:

- Click the Hold call-control button.

- Double-click the connected call.

- Right-click the call and choose Hold from the popup menu

- From the menu bar, choose Call > Hold .

- Use the associated keyboard shortcut.

## Transfer Calls

To transfer a call, you must answer it first. After you transfer a call, you cannot retrieve it unless the call is transferred
                              back to you.

Transfer calls using:

Transfer—Redirects the call immediately without allowing you to speak to the transfer recipient (the person to whom you are
                                    transferring the call).

Consult transfer—Redirects the call after first allowing you to speak to the transfer recipient.

Direct transfer—Connects two calls (active calls and calls on hold) directly.

## Set Up  Conference Call

You can set up a conference call using:

Conference—Initiate a call to add participants in a conference.

Join—Connect active calls and calls on hold in a single conference call.

To add conference participants to an active and selected call:

Select one of these options:

- Click the Conference call-control button.

- Right-click the call and choose Conference from the popup menu.

- From the menu bar, choose Call > Conference .

- Right-click a listing in the Speed Dials or Directory panels and choose Conference from the popup menu.

- Use the associated keyboard shortcut.

The Enter Number popup window appears (unless you drag the call to a listing in the Speed Dials or Directory panel).

Enter the conference participant’s phone number and click OK .

Click the Conference button again to add the person to the call, after speaking to the new conference participant.

## Divert a Call to Another Number

Use Redirect to transfer a selected call to a predetermined target number. You can redirect a call that is ringing, connected, or on hold.
                              The default targets differ based on the mode:

In the proxy-line mode, the default target is the manager for whom the call was originally intended.

In the shared-line mode, no default target exists. However you can configure the target using any valid phone number or extension.

### Use Redirect

Unlike Transfer , which requires you to specify the target with each use, Redirect sends calls to a single, predetermined target number. You can divert a call that is ringing, connected, or on hold.

You cannot divert a call that you have placed or received on one of your own phone lines (rather than on a manager’s proxy
                                             line).

To redirect a selected call to the divert target:

Select one of these options:

- Click the Redirect call-control button.

- Right-click on the call and choose Redirect from the popup menu.

- From the menu bar, choose Call > Redirect .

- Use the associated keyboard shortcut.

### Configure the Divert Target

You can set your divert target to be the manager for whom the call was originally intended or another directory number.

To view or change the target:

Select Edit > Redirect from the menu bar.

The Divert Target popup window appears.

In the shared-line mode, enter a phone number or office extension in the text box. Enter the number exactly as you would dial
                                          it from your office phone.

In the proxy-line mode, you can choose to toggle between a manager or directory number target. If you choose the directory
                                          number option, enter a phone number or office extension. Enter the number exactly as you would dial it from your office phone.

Click Save .

You can also configure a divert target for your manager, which is unique from your target. For instructions, see Configure the Divert Target for a Manager .

You can divert a call using your Cisco Unified IP Phone . Answer the call, then press the Redirect softkey on your Cisco Unified IP Phone to transfer the call to your divert target.

## Send a Call to a Voice-Messaging Service

You can transfer a ringing or connected call that you are handling for a manager to that manager’s voice-messaging service.

This feature does not apply to calls that you have placed or received on one of your own phone lines. It applies only to calls
                                          on your manager’s proxy line.

To send the selected call:

Select one of these options:

- Click the Transfer to Voice Mail call-control button.

- Right-click on the call and choose Transfer to Voicemail from the popup menu.

- From the menu bar, choose Call > Transfer to Voicemail .

- Use the associated keyboard shortcut.

You can also perform this task from your Cisco Unified IP Phone . Answer the call and then press the TrnsfVM softkey on your Cisco Unified IP Phone to transfer the manager’s call to the voice-messaging service.

| Select one of the options to place a call: Click the Dial call-control button. Right-click a phone line in the My Calls panel and select Dial from the popup menu. From the menu bar, choose Call > Dial . Double-click  speed dial or directory number. Drag directory number into the My Calls panel. Use the associated keyboard shortcut. With the console open and active on your desktop, enter the phone number that you want to call using your keyboard and then
                                          press Enter . You will see the number that you are calling in the status bar along the bottom of the console. If the Enter Number popup window appears, enter the phone number that you want to call and click OK . Enter the number exactly as you would if you were placing the call from your Cisco Unified IP Phone . |
|---|

| Select one of the options to answer a call: Click the Answer call-control button. In the My Calls panel, double-click a ringing call. Right-click the call and choose Answer from the popup menu. From the menu bar, choose Call > Answer . Use the associated keyboard shortcut. If the incoming call that you want to answer is not selected, click the incoming call to select it to answer the call. |
|---|

| Select one of the options to end a call: Click the Hang Up call-control button. Click the Hang Up call-control button. From the menu bar, choose Call > Hang Up . Use the associated keyboard shortcut. |
|---|

| Select one of the options to put calls on hold: Click the Hold call-control button. Double-click the connected call. Right-click the call and choose Hold from the popup menu From the menu bar, choose Call > Hold . Use the associated keyboard shortcut. |
|---|

| Step 1 | Select one of these options: Click the Conference call-control button. Right-click the call and choose Conference from the popup menu. From the menu bar, choose Call > Conference . Right-click a listing in the Speed Dials or Directory panels and choose Conference from the popup menu. Use the associated keyboard shortcut. The Enter Number popup window appears (unless you drag the call to a listing in the Speed Dials or Directory panel). |
|---|---|
| Step 2 | Enter the conference participant’s phone number and click OK . |
| Step 3 | Click the Conference button again to add the person to the call, after speaking to the new conference participant. |

| Note | You cannot divert a call that you have placed or received on one of your own phone lines (rather than on a manager’s proxy
                                             line). |
|---|---|

| Select one of these options: Click the Redirect call-control button. Right-click on the call and choose Redirect from the popup menu. From the menu bar, choose Call > Redirect . Use the associated keyboard shortcut. |
|---|

| Step 1 | Select Edit > Redirect from the menu bar. The Divert Target popup window appears. |
|---|---|
| Step 2 | In the shared-line mode, enter a phone number or office extension in the text box. Enter the number exactly as you would dial
                                          it from your office phone. |
| Step 3 | In the proxy-line mode, you can choose to toggle between a manager or directory number target. If you choose the directory
                                          number option, enter a phone number or office extension. Enter the number exactly as you would dial it from your office phone. |
| Step 4 | Click Save . You can also configure a divert target for your manager, which is unique from your target. For instructions, see Configure the Divert Target for a Manager . You can divert a call using your Cisco Unified IP Phone . Answer the call, then press the Redirect softkey on your Cisco Unified IP Phone to transfer the call to your divert target. |

| Note | This feature does not apply to calls that you have placed or received on one of your own phone lines. It applies only to calls
                                          on your manager’s proxy line. |
|---|---|

| Step 1 | Select one of these options: Click the Transfer to Voice Mail call-control button. Right-click on the call and choose Transfer to Voicemail from the popup menu. From the menu bar, choose Call > Transfer to Voicemail . Use the associated keyboard shortcut. |
|---|---|
| Step 2 | You can also perform this task from your Cisco Unified IP Phone . Answer the call and then press the TrnsfVM softkey on your Cisco Unified IP Phone to transfer the manager’s call to the voice-messaging service. |