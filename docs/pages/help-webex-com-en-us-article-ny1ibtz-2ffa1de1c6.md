---
doc_id: help-webex-com-en-us-article-ny1ibtz-2ffa1de1c6
source_url: https://help.webex.com/en-us/article/ny1ibtz
retrieved_at: 2026-11-02T13:07:40.791052+00:00
---

## Customize phone programmable softkeys

You can customize the softkeys displayed on the phone. Some of the the default softkeys
        (when the phone is in an idle state) are Call, Recents, Forward, and DND. Other softkeys are
        available during specific call states (for example, if a call is on hold, the Resume softkey
        displays).

You can define the parameters under Programmable Softkeys section
        with keywords and assign a service to the softkey to provide user easy access to the
        service. The customized softkeys can be found located at the bottom of the phone screen. You
        can associate the softykeys with a service to provide a quick access for users

Access the phone administration web page.

Select Voice > Phone .

In the Programmable Softkeys section, set the Programmable Softkey Enable to Yes .

Edit the softkeys by entering specific keywords depending on the call state that you
          want the softkey to display.

In the Programmable Softkeys section, each phone state is
            displayed and the softkeys that are available to display during that state are listed.
            Each softkey is separated by a semicolon. Softkeys are shown in the
            format:

For more information on the PSK
            parameters (phone state), see Programmable softkeys parameters .

For more inforamtion
            on the softkeys and the related keywords, see Keywords .

Click Submit All Changes .

### Programmable softkeys parameters

Your phones come with default key list settings that provide access to features in
          different sates of the phone. When customizing the key lists, make sure to enter the
          correct keyword for the supported feature using the proper syntax.

A configured softkey may not take effect or appear if any of the following conditions are
            met:

- The feature is disabled.

- The feature isn't supported in the key list to which it's added.

- An incorrect keyword is added.

- An incorrect syntax is used.

For more information on the keywords and related softkeys, see Keywords .

Parameter

Default and Syntax

Description

Default value: No

Options: Yes|No

Enables or disables the programmable softkeys. Set this field to Yes to
                  enable the programmable softkeys.

Default syntax: Empty

Programmable softkey fields. Enter a string in these fields to configure softkeys
                  that display on the phone screen.

For example, you can create softkeys for speed dials to numbers or extensions,
                  vertical service activation codes (* codes), and PSK with DTMF support.

For detailed steps about how to configure Speed dial PSK, see Configure Speed Dial on a programmable softkey .

For detailed steps about how to configure DTMF PSK, see Configure a PSK with DTMF support .

For detailed steps about how to configure Call Pull PSK, see Configure a softkey for call pull .

(8875 and 9871 only)

Default
                    syntax:

Configurable
                      keywords:

calls, meetings, recents, settings, dir, redial,
                    emergency_call

Specifies the softkeys and the order in which they are available on the Home
                    screen of touch phones.

Default syntax:

9811 / 9841 / 9851 /
                        9861

8875 / 9871

Configurable keywords:

calls, acd_login, acd_logout, astate, disp_code, trace, agents, redial, dir,
                    cfwd, dnd, pickup, gpickup, unpark, guestin, guestout, hoteling, newcall,
                    recents, selfview, callretrieve, bridgein, meetings, hotdesk, hotdesk_signout,
                    calendar, meeting, emergency_call, queues, redial

- meeting, calendar, hotdesk, and hotdesk_signout are for 9841, 9851, and
                        9861 only.

- agents, hoteling, and redial are for 9841, 9851, and 9861 only. agents and
                        hoteling are available with multiple lines.

- selfview, callretrieve, and bridgein are for 8875 only.

Specifies the softkeys and the order in which they are available when the phone
                    is idle.

Default syntax:

9811 / 9841 / 9851 /
                          9861

9871

8875

Configurable keywords:

endcall, meetings, participants, audiomute, videomute, layout, pip, home,
                    captionsoff, ai_assistant

videomute and pip are for 8875 only.

Specifies the softkeys and the order in which they are available on the phone
                    screen when a calendar meeting is in progress.

(9800 Series only)

Default syntax:

9811 / 9841 / 9851 /
                        9861

9871

Configurable keywords:

redial, dir, cfwd, dnd, unpark, pickup, gpickup, endcall, cancel, settings,
                    recents, back, guestin, guestout, acd_login, acd_logout, astate, disp_code,
                    home, activecalls, speeddial

guestin, guestout, acd_login, acd_logout, astate, and disp_code are for
                          9871 only.

speeddial is for 9811, 9841, 9851 and 9861 only.

Specifies the softkeys and the order in which they are available when the phone
                    is on Off-Hook state.

For example, the dnd keyword adds the DND softkey to the screen. On pressing, this softkey
                    helps to turn on the DND mode.

(9811, 9841, 9851, 9861, and
                  9871 only)

Default syntax:

9811 / 9841 / 9851 /
                          9861

9871

Configurable keywords:

abc, line, dial, delchar, cancel, call, endcall, settings, back, home

abc, line, and delchar are for 9811, 9841, 9851, and 9861 only.

Specifies the softkeys and the order in which they are available when a user
                    must enter dialing data.

Default syntax:

9811 / 9841 / 9851 /
                        9861

8875 / 9871

Configurable keywords:

endcall, settings, back, home

Specifies the softkey that are available  when a call is attempting to
                    connect.

For example, the endcall|2 keyword adds the End
                      call softkey to the screen.

Default syntax:

9811 / 9841 / 9851 /
                          9861

8875 / 9871

Configurable keywords:

audiomute, audiounmute, hold, endcall, newcall,conf, captionsoff,
                    adhocparticipants, xfer, call_info, bxfer, park, disp_code, trace, emergency,
                    phold, crdstart, crdpause, crdresume, crdstop, dnd, settings, dir, back,
                    home

Specifies the softkeys and the order in which they are available on the phone
                    screen when a call is connected.

Default syntax:

9811 / 9841 / 9851 /
                        9861

8875 / 9871

Configurable keywords:

hold, xfer, endcall, dnd, redial, settings, back, home, dir

Specifies the softkeys available when a call transfer has been initiated.

For example, the xfer keyword adds the Transfer softkey to the screen. A user can press this
                    key to transfer a call when there is one connected call and one idle call.

Default syntax:

9811 / 9841 / 9851 /
                          9861

8875 / 9871

Configurable keywords:

hold, endcall, conf, dnd, redial, settings, dir, back, home

Specifies the softkeys available when a conference call has been initiated.

For example, the conf keyword adds the Conference softkey to the screen. A user can press this
                    key to initiate a conference call.

Default syntax:

9811 / 9841 / 9851 /
                          9861

8875 /
                          9871

Configurable keywords:

hold, endcall, join, phold, crdstart, crdpause, crdresume, crdstop, dnd, dir,
                    back, home

Specifies the softkeys and the order in which they are available when a
                    conference call is in progress.

For example, on 9841, the crdstart , crdpause , crdresume , and crdstop keywords add the Record , PauseRec , ResRec , and StopRec softkeys to
                    the screen, respectively.

Default syntax:

9811 / 9841 / 9851 / 9861

```
endcall|2;home;
```

8875 / 9871

```
endcall|2;
```

Configurable keywords:

endcall, settings, back, home

Specifies the softkeys available when a call is disconnecting.

Default syntax:

9811 / 9841 / 9851 /
                          9861

8875 / 9871

Configurable keywords:

resume, endcall, newcall, redial, recents, dir, cfwd, dnd, settings, back,
                    home

Specifies the softkeys and the order in which they are available when one or
                    more calls are on hold.

Default syntax:

9811 / 9841 / 9851 /
                          9861

8875 /
                          9871

Configurable keywords:

answer, ignore, ignoresilent, call_info, settings, dir, back, ignoreall, home,
                    decline

Specifies the softkeys available when a call is incoming.

For example, the answer|1;ignore|2; keywords add the Answer and Decline softkeys to
                    the screen. A user can press these softkeys to either answer a call or decline a
                    call when the phone rings.

Default syntax:

9811 / 9841 / 9851 /
                          9861

8875 / 9871

Configurable keywords:

newcall, barge, bargesilent, cfwd, dnd, unpark, recents, settings, dir, back,
                    home

Specifies the softkeys available when the phone is in Shared-Active state.

For example, the dir keyword adds the Dir softkey to the screen. A user can press this
                    softkey to access phone directory.

Default syntax:

9811 / 9841 / 9851 /
                        9861

8875 / 9871

Configurable keywords:

resume, barge, cfwd, dnd, settings, recents, dir, newcall, back, home

Specifies the softkeys available when the phone is on Hold or in Shared-Held
                    state.

For example, the resume keyword adds the softkey Resume . User can press this softkey to resume a call
                    that is on hold.

(8875 only)

Default
                    syntax:

Configurable
                      keywords:

hold, endcall, adhocparticipants, pip, conf, xfer,
                    call_info, bxfer, park, disp_code, trace, emergency, phold, crdstart, crdpause,
                    crdresume, crdstop, dnd, unpark, settings, dir, back, home

Specifies the softkeys and the order in which they are available during a
                    connected video call and video conference.

### Keywords

Keyword

Key Label

Description

Phone state

acd_login

AgtSignIn

Logs user in to Automatic Call Distribution (ACD).

Idle

acd_logout

AgtSignOut

Logs user out of ACD.

Idle

activecalls

Calls

Opens the on-hold calls list while conferencing or transferring a call.

Connected

adhocparticipants

Participants

Opens the participants list in conferences.

Connected, Hold

ai_assistant

AI Assistant

Allows the Webex meeting hosts and participants to get the meeting summaries with
                  AI Assistant.

Connected

answer

Answer

Answers an incoming call.

Ringing

astate

Agt Status

Checks the ACD status.

Idle

audiomute

Mute

Allows meeting participants to mute themselves in a Webex meeting.

Connected

audiounmute

Unmute

Allows meeting participants to unmute themselves in a Webex meeting.

Connected

barge

Barge

Allows another user to interrupt a shared call.

Shared-Active, Shared-Held

bargesilent

BargeSilent or BargeSlnt

Allows another user to interrupt a shared call with the mic disabled.

Shared-Active

bxfer

BlindXfer

Performs a blind call transfer (transfers a call without speaking to the party to
                  whom the call is transferred). Requires that Blind Xfer Serv is enabled.

Connected

calendar

Calendar

Opens the Meetings list

Idle

call

Call

Always displays at the first position when the phone is registered.

Dialing Input or On-Hook

(Not for 9811 running PhoneOS 4.0.1 or earlier)

Allows a user to pull a call from another device.

Connected

captionsoff

Captions on/off

Allows the Webex meeting participants to show or hide the real-time transcription
                  on the phone screen. By default, the closed captions are turned off.

If the parameter Programmable Softkey Enable is set to No , the softkey or soft button Captions displays instead.

Connected

cancel

Cancel

Cancels a call (for example, when conferencing a call and the second party is not
                  answering.

Off-Hook

cfwd

Forward / Clrfwd  / Call forward

Forwards all calls to a specified number.

Idle, Off-Hook, Shared-Active, Hold, Shared-Held

crdpause

PauseRec / Pause record

Pauses recording.

Connected, Conferencing

crdresume

ResRec / Resume record

Resumes recording.

Connected, Conferencing

crdstart

Record

Starts recording.

Connected, Conferencing

crdstop

StopRec / Stop record

Stops recording

Connected, Conferencing

conf

Conf / Conference

Initiates a conference call. Requires that Conf Server is enabled and there are
                  two or more calls that are active or on hold.

Connected

delchar

(9811, 9841, 9851, and 9861 only)

delChar - backspace Icon

Deletes a character when entering text.

Dialing Input

dir

Contacts

Opens the directory menu.

Idle, Connected, Hold

dnd

DND

Sets Do Not Disturb to prevent calls from ringing the phone.

Idle, Off-Hook, Hold, Shared-Active, Shared-Held, Conferencing, Start-Conf,
                  Start-Xfer

endcall

End call

Ends a call.

Connected, Off-hook, Progressing, Start-Xfer, Start-Conf, Conferencing,Releasing,
                  Hold

hold

Hold

Puts a call on hold.

Connected, Start-Xfer, Start-Conf, Conferencing

ignore

Decline

Ignores an incoming call.

Ringing

ignoresilent

Ignore

Silences an incoming call.

Ringing

join

Join

Connects a conference call. If the Conferencing conference host is user A and
                  users B & C are participants, when A presses Join , A
                  will drop off and users B & C will be connected.

Conferencing

meetings

Meeting

Returns to the active Webex meeting screen.

Conferencing

newcall

New call

Begins a new call.

Idle, Hold, Shared-Active, Shared-Held

park

Call park

Puts a call on hold at a designated "park" number.

Connected

participants

Participants (n)

Displays the meeting participant list, where (n) represents the count of the
                  person who have joined the meeting.

Connected

phold

PrivHold

Puts a call on hold on an active shared line.

Connected

pip

(8875 only)

PIP icon

Allows user to move PIP to one of the four corners of the screen or turn PIP
                  off.

Connected Video

recents

Recents

Displays the All calls list from call history.

Idle, Off-Hook, Shared-Active, Shared-Held

redial

Redial

Displays the redial list.

Idle, Connected, Start-Conf, Start-Xfer, Off-Hook (no input), Hold

resume

Resume

Resumes a call that is on hold.

Hold, Shared-Held

settings

Settings

Provides access to phone menus.

All

speeddial

Speed dial

unpark

Call unpark

Resumes a parked call.

Idle, Off-Hook, Connected, Shared-Active

videounmute

(8875 only)

Start/Stop video

Turns your video on or off.

Connected

xfer

Transfer

Transfers a call.

Requires that Attn Xfer Serv is enabled and there is at least one connected call
                  and one idle call.

Connected, Start-Xfer, Start-Conf

## Configure Speed Dial on a programmable softkey

You can configure programmable softkeys as speed dials. The speed dials can be extensions
        or phone numbers. You can also configure programmable softkeys with speed dials that perform
        an action that a vertical service activation code (or a star [*] code) defines. For example,
        if you configure a programmable softkey with a speed dial for *67, the call is placed on
        hold.

Access the phone administration web page.

Select Voice > Phone .

In the Programmable Softkeys section, set the Programmable Softkey Enable to Yes .

Edit the Idle Key List field as described in the following
          example.

If any keyword is misspelled or the
            list contains any keyword that is not supported by the parameter, the phone screen does
            not display any change.

Enter the following in any of the PSK[1-16] number field:

where:

- In fnc=sd , sd is the function of the key (speed
              dial).

- In ext=extensionname/starcode@$PROXY , extensionname is the extension being dialed or the star code action
              to perform.

- In vid=n , n is the extension that the speed dial
              will dial out.

The name field displays on the softkey on the IP phone screen. We recommend a
                  maximum of 10 characters for a phone. If more characters are used, the label might
                  be truncated on the phone screen.

For example, enter fnc=sd;ext=5014@$PROXY;nme=speeddial in the PSK1 field.

In this example, we are configuring a softkey speeddial on a
              phone as a speed dial number for extension 5014 (sktest1).

You can also configure an XML service on the programmable softkey. Enter the
            string in this format:

Click Submit All Changes .

## Configure a PSK with DTMF support

You can configure programmable softkeys (PSK) with dual tone multifrequency (DTMF). This
        configuration enables the phone to send digital pulses inband (or out-of-band via SIP INFO)
        to the server during an active call. When you enable a function on a PSK, the user sees the
        softkey name, and presses it to perform the named function. The applied actions to the DTMF
        digit string are similar to those applied to Speed Dial, such as the following:

- Pause represented by ,

- Wait represented by X

For example, ext=<DTMF_DIGITS>[[,|X][<DTMF_DIGITS>]] , where
        the valid DTMF digits are 0-9,*, #, a, b, c, d, and where the parts in [ ] brackets are
        optional.

- This feature applies only to programmable softkeys. It doesn’t apply to the
            programmable line keys (PLK) on the desk phones. If you configure any PLK for this
            feature, the display will present the Circled X icon Ⓧ, and nothing will happen if you
            press the key.

- This feature supports Connected Key List only.

Before you begin

Access the phone administration web page.

Select Voice > Phone .

In the Programmable Softkeys section, set the Programmable Softkey Enable to Yes .

In the Connected Key List field, edit the PSK keywords according
          to where on the phone screen you wish the softkey name to appear.

In
            this example, the hold softkey name appears in the first position. The softkey name that
            is listed in the psk1 field appears in the second position, and so on.

To configure a DTMF PSK, enter the following in any of the PSK[1-16] number field:

When a phone has more than one registered line, you must include vid= that is asociated with the particular line or extension in
              order for the softkey to appear. Otherwise, the softkey will not display.

Select Voice > Ext(n) , where n is the
          extension number you wish to configure.

In the Audio Configuration section, set the DTMF Tx
            Method to one of the following methods from the drop-down list.

- InBand

- AVT

- INFO

- Auto

- InBand+INFO

- AVT+INFO

Click Submit All Changes .

Use these examples to help you understand how to configure PSK with DTMF Support
        options.

Example 1: PSK toggles when pressed.

- Voice > Phone > Programmable Softkeys > Programmable Softkey Enable : Yes

- Connected Key List : psk1|1;endcall|2;conf|3;xfer|4;

- PSK 1 : fnc=dtmf;ext=#1;nme=PressStart;ext2=*2;nme2=PressStop;vid=1

- Voice > Ext 1 > DTMF Tx Method : Auto

Example 2: Phone sends DTMF digits inband via a PSK softkey.

- Voice > Phone > Programmable Softkeys > Programmable Softkey Enable : Yes

- Connected Key List : psk1|1;endcall|2;conf|3;xfer|4;

- PSK 1 : fnc=dtmf;ext=#1;nme=PressMe;vid=1

- Voice > Ext 1 > DTMF Tx Method : Auto

Example 3: The PSK softkey pauses between digits.

- Voice > Phone > Programmable Softkeys > Programmable Softkey Enable : Yes

- Connected Key List : psk1|1;endcall|2;conf|3;xfer|4;

- PSK 1 : fnc=dtmf;ext=#1,1006;nme=PressMe;vid=1

- Voice > Ext 1 > DTMF Tx Method : Auto

Example 4: The PSK softkey waits for the user's input between digits.

- Voice > Phone > Programmable Softkeys > Programmable Softkey Enable : Yes

- Connected Key List : psk1|1;endcall|2;conf|3;xfer|4;

- PSK 1 : fnc=dtmf;ext=#1X1006;nme=PressMe;vid=1

- Voice > Ext 1 > DTMF Tx Method : Auto

## Configure a softkey for call pull

You can configure a programmable softkeys to support call pull, which provides users with a
        quick and convenient way to move active calls to their desk phone.

By default, the Pull call softkey is configured as a speed dial in
        the PSK 1 filed. You can configure it in any field of PSK[1-16] as needed and make sure that your PSK is added to Idle Key List and Shared Active Key
        List .

Access the phone administration web page.

Select Voice > Phone .

In the Programmable Softkeys section, set the Programmable Softkey Enable to Yes .

Enter the following in any of the PSK[1-16] field:

where:

- In fnc=sd , sd is the function of the key (speed
              dial).

- In ext=*11 is the star code action to perform.

The name field displays on the softkey on the phone screen. We recommend a
                  maximum of 10 characters. If more characters are used, the label might be
                  truncated on the phone screen.

For example, enter fnc=sd;ext=*11;nme=Call pull in the PSK5 field.

Add your customized PSK to the Idle Key List and Shared Active Key List field as described in the following
          example.

Idle Key List : redial|;newcall|;cfwd|;recents|;dnd|;unpark|;psk5|;gpickup|;pickup|;dir|4;miss|5;

Shared Active Key List : newcall|1;psk5|2;dir|3;back|4

If any keyword is misspelled or if the list includes a keyword that the parameter does
            not support, the phone screen will not reflect any changes.

In this example, we configure the Call pull softkey in the PSK 5 field and add psk5 to both the Idle Key List and Shared Active Key
                List fields. When there's an active call for the shared line on another
              device, the user can press the Call pull softkey to move the
              call to the desk phone.

Click Submit All Changes .

## Add the Speed dial softkey for call transfer and conference

The Speed dial softkey allows users to easily transfer a call to or
        conference with a speed dial contact on Cisco Desk Phone 9811, 9841, 9851, and 9861.

Make sure that speeddial is included in the Off Hook Key List. Otherwise,
        the Speed dial softkey isn't available.

Access the phone administration web page.

Select Voice > Phone .

In the Programmable Softkeys section, set the Programmable Softkey Enable to Yes .

In the Off Hook Key List field, add speeddial in the following format:

endcall|1;redial|2;dir|3;lcr|4;unpark|5;pickup|6;gpickup|7;speeddial;

You can also configure the softkey in the phone configuration file (cfg.xml). Enter the
            string in this format:

```
<Off_Hook_Key_List ua="na">endcall|1;redial|2;dir|3;lcr|4;unpark|5;pickup|6;gpickup|7;speeddial;</Off_Hook_Key_List>
```

Click Submit All Changes .

| 1 | Access the phone administration web page. |
|---|---|
| 2 | Select Voice > Phone . |
| 3 | In the Programmable Softkeys section, set the Programmable Softkey Enable to Yes . |
| 4 | Edit the softkeys by entering specific keywords depending on the call state that you
          want the softkey to display. In the Programmable Softkeys section, each phone state is
            displayed and the softkeys that are available to display during that state are listed.
            Each softkey is separated by a semicolon. Softkeys are shown in the
            format: softkeyname\|[position] For more information on the PSK
            parameters (phone state), see Programmable softkeys parameters . For more inforamtion
            on the softkeys and the related keywords, see Keywords . |
| 5 | Click Submit All Changes . |

| Parameter | Default and Syntax | Description |
|---|---|---|
| Programmable Softkey Enable | Default value: No Options: Yes\|No | Enables or disables the programmable softkeys. Set this field to Yes to
                  enable the programmable softkeys. |
| PSK 1 through PSK16 | Default syntax: Empty | Programmable softkey fields. Enter a string in these fields to configure softkeys
                  that display on the phone screen. For example, you can create softkeys for speed dials to numbers or extensions,
                  vertical service activation codes (* codes), and PSK with DTMF support. For detailed steps about how to configure Speed dial PSK, see Configure Speed Dial on a programmable softkey . For detailed steps about how to configure DTMF PSK, see Configure a PSK with DTMF support . For detailed steps about how to configure Call Pull PSK, see Configure a softkey for call pull . |
| Device Key List (8875 and 9871 only) | Default
                    syntax: calls;meetings;recents;settings;dir; Configurable
                      keywords: calls, meetings, recents, settings, dir, redial,
                    emergency_call | Specifies the softkeys and the order in which they are available on the Home
                    screen of touch phones. |
| Idle Key List | Default syntax: 9811 / 9841 / 9851 /
                        9861 calls;calendar;meeting;acd_login;
                        acd_logout;astate;agents;recents; settings;dir;cfwd;dnd;pickup;gpickup;
                        unpark;guestin;guestout;hoteling;redial;
                        hotdesk\|3;hotdesk_signout\|3; 8875 / 9871 acd_login;acd_logout;astate;recents;
                        cfwd;dnd;pickup;gpickup;unpark;guestin;guestout; Configurable keywords: calls, acd_login, acd_logout, astate, disp_code, trace, agents, redial, dir,
                    cfwd, dnd, pickup, gpickup, unpark, guestin, guestout, hoteling, newcall,
                    recents, selfview, callretrieve, bridgein, meetings, hotdesk, hotdesk_signout,
                    calendar, meeting, emergency_call, queues, redial meeting, calendar, hotdesk, and hotdesk_signout are for 9841, 9851, and
                        9861 only. agents, hoteling, and redial are for 9841, 9851, and 9861 only. agents and
                        hoteling are available with multiple lines. selfview, callretrieve, and bridgein are for 8875 only. | Specifies the softkeys and the order in which they are available when the phone
                    is idle. |
| Connected Meeting Key List | Default syntax: 9811 / 9841 / 9851 /
                          9861 audiomute;endcall\|2;participants\|3;captionsoff;home; 9871 audiomute;endcall\|2;ai_assistant;
                          captionsoff;participants; 8875 audiomute;endcall\|2;videounmute;ai_assistant;
                          layout;participants;pip;captionsoff; Configurable keywords: endcall, meetings, participants, audiomute, videomute, layout, pip, home,
                    captionsoff, ai_assistant videomute and pip are for 8875 only. | Specifies the softkeys and the order in which they are available on the phone
                    screen when a calendar meeting is in progress. |
| Off Hook Key List (9800 Series only) | Default syntax: 9811 / 9841 / 9851 /
                        9861 abc;redial;cancel;cfwd;dnd;unpark;
                        pickup;gpickup;activecalls;speeddial 9871 cancel;acd_login;acd_logout;astate;dnd;
                        cfwd;unpark;pickup;gpickup;guestin;guestout; Configurable keywords: redial, dir, cfwd, dnd, unpark, pickup, gpickup, endcall, cancel, settings,
                    recents, back, guestin, guestout, acd_login, acd_logout, astate, disp_code,
                    home, activecalls, speeddial guestin, guestout, acd_login, acd_logout, astate, and disp_code are for
                          9871 only. speeddial is for 9811, 9841, 9851 and 9861 only. | Specifies the softkeys and the order in which they are available when the phone
                    is on Off-Hook state. For example, the dnd keyword adds the DND softkey to the screen. On pressing, this softkey
                    helps to turn on the DND mode. |
| Dialing Input Key List (9811, 9841, 9851, 9861, and
                  9871 only) | Default syntax: 9811 / 9841 / 9851 /
                          9861 abc;call;delchar;line;cancel 9871 cancel\|1;call\|2; Configurable keywords: abc, line, dial, delchar, cancel, call, endcall, settings, back, home abc, line, and delchar are for 9811, 9841, 9851, and 9861 only. | Specifies the softkeys and the order in which they are available when a user
                    must enter dialing data. |
| Progressing Key List | Default syntax: 9811 / 9841 / 9851 /
                        9861 endcall\|2;home\|3; 8875 / 9871 endcall\|2; Configurable keywords: endcall, settings, back, home | Specifies the softkey that are available  when a call is attempting to
                    connect. For example, the endcall\|2 keyword adds the End
                      call softkey to the screen. |
| Connected Key List | Default syntax: 9811 / 9841 / 9851 /
                          9861 hold;endcall;newcall;captionsoff;
                          conf;xfer;bxfer;park;phold;
                          crdstart;crdpause;crdresume;crdstop;home; 8875 / 9871 audiomute;audiounmute;hold;endcall;
                          captionsoff;conf;xfer;bxfer;park;phold;
                          crdstart;crdpause;crdresume;crdstop; Configurable keywords: audiomute, audiounmute, hold, endcall, newcall,conf, captionsoff,
                    adhocparticipants, xfer, call_info, bxfer, park, disp_code, trace, emergency,
                    phold, crdstart, crdpause, crdresume, crdstop, dnd, settings, dir, back,
                    home | Specifies the softkeys and the order in which they are available on the phone
                    screen when a call is connected. |
| Start-Xfer Key List | Default syntax: 9811 / 9841 / 9851 /
                        9861 endcall;xfer;home; 8875 / 9871 hold;endcall;xfer; Configurable keywords: hold, xfer, endcall, dnd, redial, settings, back, home, dir | Specifies the softkeys available when a call transfer has been initiated. For example, the xfer keyword adds the Transfer softkey to the screen. A user can press this
                    key to transfer a call when there is one connected call and one idle call. |
| Start-Conf Key List | Default syntax: 9811 / 9841 / 9851 /
                          9861 hold;endcall;conf;home; 8875 / 9871 hold;endcall;conf; Configurable keywords: hold, endcall, conf, dnd, redial, settings, dir, back, home | Specifies the softkeys available when a conference call has been initiated. For example, the conf keyword adds the Conference softkey to the screen. A user can press this
                    key to initiate a conference call. |
| Conferencing Key List | Default syntax: 9811 / 9841 / 9851 /
                          9861 hold;endcall;join;phold;crdstart\|5;crdpause\|5;
                          crdresume\|5;crdstop\|6;home; 8875 /
                          9871 hold;endcall;join;phold;crdstart;crdpause;
                          crdresume;crdstop; Configurable keywords: hold, endcall, join, phold, crdstart, crdpause, crdresume, crdstop, dnd, dir,
                    back, home | Specifies the softkeys and the order in which they are available when a
                    conference call is in progress. For example, on 9841, the crdstart , crdpause , crdresume , and crdstop keywords add the Record , PauseRec , ResRec , and StopRec softkeys to
                    the screen, respectively. |
| Releasing Key List | Default syntax: 9811 / 9841 / 9851 / 9861 endcall\|2;home; 8875 / 9871 endcall\|2; Configurable keywords: endcall, settings, back, home | Specifies the softkeys available when a call is disconnecting. |
| Hold Key List | Default syntax: 9811 / 9841 / 9851 /
                          9861 resume;endcall;newcall;home; 8875 / 9871 resume;endcall;newcall; Configurable keywords: resume, endcall, newcall, redial, recents, dir, cfwd, dnd, settings, back,
                    home | Specifies the softkeys and the order in which they are available when one or
                    more calls are on hold. |
| Ringing Key List | Default syntax: 9811 / 9841 / 9851 /
                          9861 answer\|1;ignore\|2;ignoresilent\|3;
                          ignoreall;home; 8875 /
                          9871 answer\|1;ignore\|2;ignoresilent\|3;ignoreall; Configurable keywords: answer, ignore, ignoresilent, call_info, settings, dir, back, ignoreall, home,
                    decline | Specifies the softkeys available when a call is incoming. For example, the answer\|1;ignore\|2; keywords add the Answer and Decline softkeys to
                    the screen. A user can press these softkeys to either answer a call or decline a
                    call when the phone rings. |
| Shared Active Key List | Default syntax: 9811 / 9841 / 9851 /
                          9861 newcall;barge;home; 8875 / 9871 newcall;barge; Configurable keywords: newcall, barge, bargesilent, cfwd, dnd, unpark, recents, settings, dir, back,
                    home | Specifies the softkeys available when the phone is in Shared-Active state. For example, the dir keyword adds the Dir softkey to the screen. A user can press this
                    softkey to access phone directory. |
| Shared Held Key List | Default syntax: 9811 / 9841 / 9851 /
                        9861 resume;barge;home; 8875 / 9871 resume;barge; Configurable keywords: resume, barge, cfwd, dnd, settings, recents, dir, newcall, back, home | Specifies the softkeys available when the phone is on Hold or in Shared-Held
                    state. For example, the resume keyword adds the softkey Resume . User can press this softkey to resume a call
                    that is on hold. |
| Connected Video Key List (8875 only) | Default
                    syntax: hold;endcall;conf;xfer;bxfer;park;
                    phold;crdstart;crdpause;crdresume;crdstop;pip; Configurable
                      keywords: hold, endcall, adhocparticipants, pip, conf, xfer,
                    call_info, bxfer, park, disp_code, trace, emergency, phold, crdstart, crdpause,
                    crdresume, crdstop, dnd, unpark, settings, dir, back, home | Specifies the softkeys and the order in which they are available during a
                    connected video call and video conference. |

| Keyword | Key Label | Description | Phone state |
|---|---|---|---|
| acd_login | AgtSignIn | Logs user in to Automatic Call Distribution (ACD). | Idle |
| acd_logout | AgtSignOut | Logs user out of ACD. | Idle |
| activecalls | Calls | Opens the on-hold calls list while conferencing or transferring a call. | Connected |
| adhocparticipants | Participants | Opens the participants list in conferences. | Connected, Hold |
| ai_assistant | AI Assistant | Allows the Webex meeting hosts and participants to get the meeting summaries with
                  AI Assistant. | Connected |
| answer | Answer | Answers an incoming call. | Ringing |
| astate | Agt Status | Checks the ACD status. | Idle |
| audiomute | Mute | Allows meeting participants to mute themselves in a Webex meeting. | Connected |
| audiounmute | Unmute | Allows meeting participants to unmute themselves in a Webex meeting. | Connected |
| barge | Barge | Allows another user to interrupt a shared call. | Shared-Active, Shared-Held |
| bargesilent | BargeSilent or BargeSlnt | Allows another user to interrupt a shared call with the mic disabled. | Shared-Active |
| bxfer | BlindXfer | Performs a blind call transfer (transfers a call without speaking to the party to
                  whom the call is transferred). Requires that Blind Xfer Serv is enabled. | Connected |
| calendar | Calendar | Opens the Meetings list | Idle |
| call | Call | Always displays at the first position when the phone is registered. | Dialing Input or On-Hook |
| call pull (Not for 9811 running PhoneOS 4.0.1 or earlier) | Call Pull | Allows a user to pull a call from another device. | Connected |
| captionsoff | Captions on/off | Allows the Webex meeting participants to show or hide the real-time transcription
                  on the phone screen. By default, the closed captions are turned off. If the parameter Programmable Softkey Enable is set to No , the softkey or soft button Captions displays instead. | Connected |
| cancel | Cancel | Cancels a call (for example, when conferencing a call and the second party is not
                  answering. | Off-Hook |
| cfwd | Forward / Clrfwd  / Call forward | Forwards all calls to a specified number. | Idle, Off-Hook, Shared-Active, Hold, Shared-Held |
| crdpause | PauseRec / Pause record | Pauses recording. | Connected, Conferencing |
| crdresume | ResRec / Resume record | Resumes recording. | Connected, Conferencing |
| crdstart | Record | Starts recording. | Connected, Conferencing |
| crdstop | StopRec / Stop record | Stops recording | Connected, Conferencing |
| conf | Conf / Conference | Initiates a conference call. Requires that Conf Server is enabled and there are
                  two or more calls that are active or on hold. | Connected |
| delchar (9811, 9841, 9851, and 9861 only) | delChar - backspace Icon | Deletes a character when entering text. | Dialing Input |
| dir | Contacts | Opens the directory menu. | Idle, Connected, Hold |
| dnd | DND | Sets Do Not Disturb to prevent calls from ringing the phone. | Idle, Off-Hook, Hold, Shared-Active, Shared-Held, Conferencing, Start-Conf,
                  Start-Xfer |
| endcall | End call | Ends a call. | Connected, Off-hook, Progressing, Start-Xfer, Start-Conf, Conferencing,Releasing,
                  Hold |
| hold | Hold | Puts a call on hold. | Connected, Start-Xfer, Start-Conf, Conferencing |
| ignore | Decline | Ignores an incoming call. | Ringing |
| ignoresilent | Ignore | Silences an incoming call. | Ringing |
| join | Join | Connects a conference call. If the Conferencing conference host is user A and
                  users B & C are participants, when A presses Join , A
                  will drop off and users B & C will be connected. | Conferencing |
| meetings | Meeting | Returns to the active Webex meeting screen. | Conferencing |
| newcall | New call | Begins a new call. | Idle, Hold, Shared-Active, Shared-Held |
| park | Call park | Puts a call on hold at a designated "park" number. | Connected |
| participants | Participants (n) | Displays the meeting participant list, where (n) represents the count of the
                  person who have joined the meeting. | Connected |
| phold | PrivHold | Puts a call on hold on an active shared line. | Connected |
| pip (8875 only) | PIP icon | Allows user to move PIP to one of the four corners of the screen or turn PIP
                  off. | Connected Video |
| recents | Recents | Displays the All calls list from call history. | Idle, Off-Hook, Shared-Active, Shared-Held |
| redial | Redial | Displays the redial list. | Idle, Connected, Start-Conf, Start-Xfer, Off-Hook (no input), Hold |
| resume | Resume | Resumes a call that is on hold. | Hold, Shared-Held |
| settings | Settings | Provides access to phone menus. | All |
| speeddial | Speed dial | Provides access to the speed dial list while transferring a call or add a
                participant to a conference call. | Off -Hook |
| unpark | Call unpark | Resumes a parked call. | Idle, Off-Hook, Connected, Shared-Active |
| videounmute (8875 only) | Start/Stop video | Turns your video on or off. | Connected |
| xfer | Transfer | Transfers a call. Requires that Attn Xfer Serv is enabled and there is at least one connected call
                  and one idle call. | Connected, Start-Xfer, Start-Conf |

| 1 | Access the phone administration web page. |
|---|---|
| 2 | Select Voice > Phone . |
| 3 | In the Programmable Softkeys section, set the Programmable Softkey Enable to Yes . |
| 4 | Edit the Idle Key List field as described in the following
          example. redial\|1;newcall\|2;dnd;psk1 If any keyword is misspelled or the
            list contains any keyword that is not supported by the parameter, the phone screen does
            not display any change. |
| 5 | Enter the following in any of the PSK[1-16] number field: fnc=sd;ext=extensionname/starcode@$PROXY;vid=n;nme=name where: In fnc=sd , sd is the function of the key (speed
              dial). In ext=extensionname/starcode@$PROXY , extensionname is the extension being dialed or the star code action
              to perform. In vid=n , n is the extension that the speed dial
              will dial out. In nme=name , name is the name of the speed dial
              being configured. The name field displays on the softkey on the IP phone screen. We recommend a
                  maximum of 10 characters for a phone. If more characters are used, the label might
                  be truncated on the phone screen. For example, enter fnc=sd;ext=5014@$PROXY;nme=speeddial in the PSK1 field. In this example, we are configuring a softkey speeddial on a
              phone as a speed dial number for extension 5014 (sktest1). You can also configure an XML service on the programmable softkey. Enter the
            string in this format: <PSK_1
            ua="na">fnc=xml;url=http://xml.service.url;nme=name</PSK_1> |
| 6 | Click Submit All Changes . |

| 1 | Access the phone administration web page. |
|---|---|
| 2 | Select Voice > Phone . |
| 3 | In the Programmable Softkeys section, set the Programmable Softkey Enable to Yes . |
| 4 | In the Connected Key List field, edit the PSK keywords according
          to where on the phone screen you wish the softkey name to appear. hold;psk1;endcall;xfer;conf;xferLx;confLx;bxfer;phold;redial;dir;park In
            this example, the hold softkey name appears in the first position. The softkey name that
            is listed in the psk1 field appears in the second position, and so on. |
| 5 | To configure a DTMF PSK, enter the following in any of the PSK[1-16] number field: fnc=dtmf;ext=<dtmf_digits_to_be_outpulsed>;nme=<softkey_display_name>;vid=<extension_n_to_be_associated> When a phone has more than one registered line, you must include vid= that is asociated with the particular line or extension in
              order for the softkey to appear. Otherwise, the softkey will not display. |
| 6 | Select Voice > Ext(n) , where n is the
          extension number you wish to configure. |
| 7 | In the Audio Configuration section, set the DTMF Tx
            Method to one of the following methods from the drop-down list. InBand AVT INFO Auto InBand+INFO AVT+INFO |
| 8 | Click Submit All Changes . |

| 1 | Access the phone administration web page. |
|---|---|
| 2 | Select Voice > Phone . |
| 3 | In the Programmable Softkeys section, set the Programmable Softkey Enable to Yes . |
| 4 | Enter the following in any of the PSK[1-16] field: fnc=sd;ext=*11;nme=Call Pull where: In fnc=sd , sd is the function of the key (speed
              dial). In ext=*11 is the star code action to perform. In nme=Call pull , Call Pull is the name of the
              softkey being configured. The name field displays on the softkey on the phone screen. We recommend a
                  maximum of 10 characters. If more characters are used, the label might be
                  truncated on the phone screen. For example, enter fnc=sd;ext=*11;nme=Call pull in the PSK5 field. |
| 5 | Add your customized PSK to the Idle Key List and Shared Active Key List field as described in the following
          example. Idle Key List : redial\|;newcall\|;cfwd\|;recents\|;dnd\|;unpark\|;psk5\|;gpickup\|;pickup\|;dir\|4;miss\|5; Shared Active Key List : newcall\|1;psk5\|2;dir\|3;back\|4 If any keyword is misspelled or if the list includes a keyword that the parameter does
            not support, the phone screen will not reflect any changes. In this example, we configure the Call pull softkey in the PSK 5 field and add psk5 to both the Idle Key List and Shared Active Key
                List fields. When there's an active call for the shared line on another
              device, the user can press the Call pull softkey to move the
              call to the desk phone. |
| 6 | Click Submit All Changes . |

| 1 | Access the phone administration web page. |
|---|---|
| 2 | Select Voice > Phone . |
| 3 | In the Programmable Softkeys section, set the Programmable Softkey Enable to Yes . |
| 4 | In the Off Hook Key List field, add speeddial in the following format: endcall\|1;redial\|2;dir\|3;lcr\|4;unpark\|5;pickup\|6;gpickup\|7;speeddial; You can also configure the softkey in the phone configuration file (cfg.xml). Enter the
            string in this format: <Off_Hook_Key_List ua="na">endcall\|1;redial\|2;dir\|3;lcr\|4;unpark\|5;pickup\|6;gpickup\|7;speeddial;</Off_Hook_Key_List> |
| 5 | Click Submit All Changes . |