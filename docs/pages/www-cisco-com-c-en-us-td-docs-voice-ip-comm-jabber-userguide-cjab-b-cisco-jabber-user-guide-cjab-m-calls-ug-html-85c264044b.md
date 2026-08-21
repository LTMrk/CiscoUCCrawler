---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-jabber-userguide-cjab-b-cisco-jabber-user-guide-cjab-m-calls-ug-html-85c264044b
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/jabber/userguide/cjab_b_cisco-jabber-user-guide/cjab_m_calls_ug.html
retrieved_at: 2026-08-21T06:55:50.741349+00:00
---

Cisco Jabber User Guide

# Cisco Jabber User Guide

Updated: May 4, 2026

Chapter: Calls

## Chapter: Calls

# Calls

## Phone Service Accounts

When you call Cisco Jabber, the app uses your work phone number and displays that work number to the person you call.

You can make calls in different ways, depending on how your account is set up.

A basic Phone Services account allows you to make audio calls using Voice over Internet Protocol (VoIP). Your system administrator
                              can also enable the following features for your account:

A basic Phone Services account allows you to make audio/video calls using VoIP. The video capability is enabled by default.
                              Your system administrator can also enable the Dial via Office (DVO) feature. This feature allows you to call using your work
                              phone number and your mobile voice network.

Check your account settings to ensure your system administrator has enabled the DVO feature.

Video: Allows you to make video calls.

DVO is only available on iPhone. It is not supported in the collaboration edge environment. A VPN is required to use this
                                    feature when you are out of office.

The following table compares the call behavior between VoIP and DVO calls, based on various criteria:

In-call features

(such as hold or conference)

The following table lists the call settings that you can set up in the Cisco Jabber Settings menu, based on your Phone Services
                              account setup.

Send Automatically: Use this setting to turn automatic video for calls on and off.

Mobile Data Network: Use this setting to automatically turn video on or off when you use a mobile data network.

These options are not available if you enable low-bandwidth mode.

Calling Options: Specify whether you want Cisco Jabber to always make VoIP calls, always make calls with your mobile voice network, or automatically
                                          select the call method based on your network connection.

Low-Bandwidth Mode: If you select a calling option that uses VoIP, Cisco Jabber displays the Low-Bandwidth Mode setting. Use this setting to optimize audio, if you make VoIP calls while you are connected to a low-bandwidth network.

## Make a Call

Use Cisco Jabber to call your coworkers, and anyone else you need to be in touch with.

### Choose a Phone Number for Multiple Lines in Desktop

If you’re using Cisco Jabber 12.0 or later on Windows or Mac and your admin has set you up with the multiline feature, you
                                 can select which line to use when you call someone.

Step 1

From the drop-down list of phone numbers next to the search bar, select the phone number you’d like to use to make the call.

Step 2

Make the call.

### Make a Call Using the Desktop Keypad

You can use the keypad if you're using Cisco Jabber for Windows or Mac 12.6 or later.

Step 1

Go to Calls , and select the keypad icon.

Step 2

Use your mouse to click on the keypad to dial the number you want, and then click Call . You can use the backspace to correct
                                          any dialing mistakes.

### Contact List Call

You can use the search bar to quickly call anyone in your directory. If the person has only one number, Cisco Jabber uses
                                 it; otherwise, you can select the number to call first.

#### Call Someone from Your Contact List in Desktop

Step 1

Click the search bar and enter the name of the person you want to call.

Step 2

In the search results, hover over their name, and click Call .

#### Call Someone from Your Contact List in Mobile

Step 1

Go to Contacts , tap the search bar, and enter the name of the person you want to call.

Step 2

In the search results, tap their name, and then tap Call .

### Messaging Window Call

Sometimes, its just easier to talk to someone instead of sending lots of lengthy messages. But if you're already messaging
                                 someone, then you can just quickly call them directly from your messaging window.

#### Call Someone While Messaging in Desktop

From your conversation window, select Call from the top-right corner of the conversation window.

#### Call Someone While Messaging in iPhone and iPad

From the conversation window, tap , and tap the number to call.

#### Call Someone While Messaging in Android

While you’re chatting with someone in Cisco Jabber, you might get new chat message from a different person, Cisco Jabber displays
                                    a preview of the new chat message in your current chat window, so that you don't miss anything.

When you're on a video call, tap the back button on your device to minimize the video call window. Tap the minimized video
                                    call window to view the video call on full screen. You can drag and position the video anywhere on your device.

From the conversation window, tap , and tap the number to call.

### SIP URI Calling

You can use Uniform Resource Identifier (URI) dialing to make calls and resolve contacts with URI. For example, a user named
                                 Anita Perez has the following SIP URI associated with her directory number: aperez@example.com. URI dialing allows you to
                                 call Anita with her SIP URI rather than her directory number.

You can also send DTMF tones with the SIP URI. Use these tones to dial extensions, or other digit sequences. For example,
                                 to dial Anita Perez at extension 1234, enter aperez@example.com,1234. The comma (,) gives a 2 second pause before the next
                                 character is dialed.

Users that are connected to Cisco TelePresence Video Communication Server (VCS), are only accessible using their associated
                                 URI.

Contacts imported from Microsoft Outlook may contain SIP URIs. For releases prior to Apple OS X Maverick Version 10.9, the
                                 Mac address book may not display some characters, for example aperez@example.com can display as aperezexamplecom. However,
                                 you can still search and call using these URIs.

#### Dial a Contact Using a SIP URI in Windows

##### Before you begin

Your administrator must enable URI dialing.

Step 1

Enter the SIP URI.

Step 2

(Optional) Add a comma and the DTMF tones.

Step 3

Click Call .

#### Dial a Contact Using a SIP URI in Mac

Step 1

Enter the characters of the URI including the @ symbol and at least two characters after the @. For example, aperez@ex.

Step 2

Select Call in the bricklet to call the contact using their SIP URI.

## Answer Calls

### Respond to a Call with Chat in Windows

When you get a call in Jabber, you can choose to answer or decline it. You can also respond with a text message, in case you
                                 are unable to accept it.

If you choose Chat reply , the call is automatically forwarded to your voicemail. A chat window with the caller also pops up, giving you the option
                                 to send a quick reply to the caller.

#### Before you begin

To use the Chat reply feature, you must have voicemail set up.

Step 1

When you receive a call from one of your contacts, choose one of these options:

- Answer

- Decline

- Chat reply

Step 2

If you choose Chat reply , you can send a quick reply to the caller in the chat window.

### Turn on Automatic Answering

Jabber for iPhone and iPad can answer calls automatically, even from the lock screen. Before you can turn this on, you need
                                 to open the Jabber app in an active Guided Access session. Your administrator controls whether you can turn on automatic answering.

#### Before you begin

Jabber needs to be open in an active Guided Access session. You can learn how to start a Guided Access session from Apple Support .

Jabber needs to have made at least one phone call before automatic answering can work. If you're on a fresh installation,
                                 make a phone call before you attempt to turn on automatic answering.

Step 1

Tap your profile picture, and then go Settings > Call Option .

Step 2

Toggle Auto Answer to on .

### Automatic Call Mute

If you don't want to worry about interrupting your calls with background noise, set up Cisco Jabber to automatically mute
                                 your audio when you connect to a call.

#### Mute My Calls Automatically in Windows

Go to Options > Calls and turn on Mute audio by default for Jabber calls .

The Calls tab is only available if you have set up Phone Services in your Accounts tab.

#### Mute My Calls Automatically in Mac

Go to Preferences > Calls and turn on Mute audio by default for Jabber calls .

The Calls tab is only available if you have set up Phone Services in your Accounts tab.

#### Mute My Calls Automatically in Mobile

Go to Settings > Calls and tap  Auto Mute in the Mute me on all Jabber calls field.

The Calls tab is only available if you have set up Phone Services in your Accounts tab.

## During a Call

### Merge Calls in iPhone and iPad

Use the Merge feature to merge two existing calls into a conference call.

This procedure applies only to Cisco Jabber VoIP calls. The Merge feature is not available for DvO calls.

Step 1

From the in-call view, tap More .

Step 2

Tap Merge .

Step 3

Tap OK .

Step 4

(Optional) Tap to view a list of conference participants.

### Merge Calls in Android

Use the Merge feature to merge two existing calls into a conference call.

This procedure applies only to Cisco Jabber VoIP calls. The Merge feature is not available for DvO calls.

Step 1

From the in-call view, tap More .

Step 2

Tap Merge .

Step 3

Tap OK .

Step 4

(Optional) Tap to view a list of conference participants.

### Move a Call to the Mobile Network for iPhone and iPad

If you are on a Cisco Jabber VoIP call with call quality issues, you can move the call to your mobile network and receive
                                 the call on your mobile.

This procedure applies only to Cisco Jabber VoIP calls. This feature is not available for DvO calls.

Your system administrator must enable the Transfer to Mobile Network option on the server.

Step 1

From the in-call view, tap More .

Step 2

Tap Move to Mobile and tap OK .

Step 3

Tap Answer when your device rings.

### Move a Call to the Mobile Network for Android

You can move a call to a mobile network This procedure applies only to Cisco Jabber VoIP calls. This feature is not available
                                 for DvO calls.

Step 1

From the in-call view, tap More .

Step 2

Tap Move to Mobile and tap OK .

Step 3

Tap Answer when your device rings.

### Park a Call in Android

If you’re on a call, you can park the call to a call park extension (for example, to a phone in another office or in a conference
                                 room) or temporarily place the call on hold. Another phone in your system can dial the call park extension to retrieve the
                                 call.

Complete this task to park an ongoing call so that you can transfer it to another device or temporarily place it on hold.

Step 1

From the in-call view, tap More .

Step 2

Tap Park .

Step 3

Retrieve the call from another device or resume the call from the current device.

### Conference Calls

When you need to talk to more than just one person at a time, you can start a conference call in Cisco Jabber. Rather than
                                 setting up a formal meeting by sending out invitations and booking conference rooms, you can just get your group call started
                                 right away.

#### Start Conference Calls in Windows

Step 1

To get your conference call started, choose any of these methods:

- While on a call—convert the call to a conference call by clicking the More button on the call control strip, and then selecting the Conference Call option.

- From a group header—hover over a group header and click the call button to start a conference call with all of the available
                                                contacts in that group.

- From multiple contact selection—select the contacts that you want in your conference call and click the call button that appears
                                                when you hover over any of the selected contacts.

Step 2

Add contacts to a conference call using these options:

- Search for contacts in the Add participants field.

- Drag contacts from your Contacts tab and drop them into the conference call window.

#### Make a Conference Call in Android

Step 1

From the in-call view, tap More .

Step 2

Tap Conference .

Step 3

Follow one of these steps:

- Enter a phone number and select Call .

- Enter a name or video address, and tap an item in the search results.

Cisco Jabber automatically places your first call on hold and displays the status of both calls.

Step 4

On the control bar, tap Merge .

### Hold and Resume Calls in Android

Step 1

From the in-call view, tap More .

Step 2

Tap Hold .

Step 3

To resume the call, tap Resume .

### Toggle Between Calls in Android

When you are connected to two internet calls, only one call is active at a time; the other is automatically placed on hold.

Tap the red bar to toggle between the two calls.

### Transfer a Call in Android

Step 1

From the in-call view, tap More .

Step 2

Tap Transfer .

Step 3

Follow one of these steps:

Enter a phone number and select Call .

Enter a name or video address, and tap an item in the search results.

### Call Forwarding

If you're going to be away from your desk but don't want to miss an important call, you can forward your calls to another
                                 phone number, or voicemail.

#### Forward Calls in Windows

Step 1

Select the phone control menu on the main window.

Step 2

Select Forward calls to and then select the appropriate option.

#### Forward Calls in Mac

Step 1

Select Jabber > Preferences > Calls .

Step 2

Select Call Forward .

Step 3

In the Forward Calls to section, do one of these options:

- Select Plus (+) and add a new number in the available list.

- Enter a phone number, including country and area codes.

#### Forward Calls in iPhone and iPad

Step 1

Go to Settings > Call > Call forwarding .

Step 2

Select one of these options:

- Do not forward calls

- Voicemail

- Mobile

- Home

- Customize—Enter the number (with country and area codes) to forward calls to an alternate number.

#### Forward Calls in Android

Step 1

Go to Settings > Call > Call forwarding .

Step 2

Select one of these options:

- Disable call forwarding

- Voicemail

- Mobile

- Home

- Add a number—Enter the URI or phone number (with country and area codes) to forward calls to an alternate number.

### Far-End Camera Control

If you call a unit or person that has a device with a controllable camera, you can control the far-end camera to give you
                                 a better view during the video call. If you call a Cisco bridge, you can choose the layout of the video displays on your conference
                                 call.

#### Control Far-End Cameras in Windows

##### Before you begin

Ensure that the system you are calling supports far-end camera control (FECC). For more information, see the documentation
                                    for each device.

Your video conference administrator must enable this feature.

You also need to be in softphone mode, which means you've selected Use my computer for calls in your hub window.

Step 1

After you have started a video call, select the Show Far End Camera Control icon.

Step 2

Choose one of these options:

- For direct calls to devices, use the controls to pan left or right, tilt up or down, and zoom the camera in and out.

- For calls to bridges, use the controls to select the conference layout that you want to use.

- Use the following keyboard shortcuts to manually control the camera.

#### Control Far-End Cameras in Mac

##### Before you begin

Ensure that the system you are calling supports far-end camera control (FECC). For more information, see the documentation
                                    for each device.

Your video conference administrator must enable this feature.

Step 1

After you have started a video call, select the Show Far End Camera Control icon.

Step 2

Choose one of these options:

- For direct calls to devices, use the controls to pan left or right, tilt up or down, and zoom the camera in and out.

- For calls to bridges, use the controls to select the conference layout that you want to use.

- Use the following keyboard shortcuts to manually control the camera.

#### Control Far-End Cameras in iPhone and iPad

##### Before you begin

Ensure that the system you are calling supports far-end camera control (FECC). For more information, see the documentation
                                    for each device.

Your video conference administrator must enable this feature.

Step 1

After you have started a video call, select the Show Far End Camera Control icon.

Step 2

Choose one of these options:

- For direct calls to devices, use the controls to pan left or right, tilt up or down, and zoom the camera in and out.

- For calls to bridges, use the controls to select the conference layout that you want to use.

- Use the following keyboard shortcuts to manually control the camera.

#### Control Far-End Cameras in Android

##### Before you begin

Ensure that the system you are calling supports far-end camera control (FECC). For more information, see the documentation
                                    for each device.

Your video conference administrator must enable this feature.

Step 1

After you have started a video call, select the Show Far End Camera Control icon.

Step 2

Choose one of these options:

- For direct calls to devices, use the controls to pan left or right, tilt up or down, and zoom the camera in and out.

- For calls to bridges, use the controls to select the conference layout that you want to use.

- Use the following keyboard shortcuts to manually control the camera.

### Control Call Recording

In Jabber installations configured with this feature, you can start and stop recording of a Cisco Jabber call.

Depending on your Jabber configuration, you can record calls between yourself and another user. Either person can start and
                                 stop the recording. After the call ends, one of you would receive an email with a link to download the recording.

Step 1

In the Jabber Phone tab, dial the conference bridge number or click the link that is provided to you. Then, enter the passcode,
                                          if needed.

Step 2

In the call window, click More to display the menu and select Record .

After several seconds, an automated voice announces that the recording has started.

Step 3

To stop the recording, click More > Stop .

The recording automatically stops when the call ends and a link to the recording is sent out.

### Show Call Statistics in Android

Step 1

From the in-call view, tap More .

Step 2

Tap Call Statistics .

| Criteria | VoIP | DVO |
|---|---|---|
| Networks used | Wi-Fi or mobile data networks | Mobile voice network |
| Maximum number of calls at a time | TwoOnly one call is active at a time; the other is automatically placed on hold. | One |
| In-call features (such as hold or conference) | Available | Not available |
| Incoming calls | Open in Cisco Jabber | Open in the native phone application |
| Outgoing calls | Cisco Jabber immediately dials the number that you enter. | The corporate calling system calls you back before dialing the number that you enter. |

| If your account is... | You can modify these Cisco Jabber settings |
|---|---|
| Video enabled | Send Automatically: Use this setting to turn automatic video for calls on and off. Mobile Data Network: Use this setting to automatically turn video on or off when you use a mobile data network. Note These options are not available if you enable low-bandwidth mode. | Note | These options are not available if you enable low-bandwidth mode. |
| Note | These options are not available if you enable low-bandwidth mode. |
| Not DVO enabled | Low-Bandwidth Mode: Use this setting to optimize audio if you make VoIP calls while you are connected to a low-bandwidth network. |
| DVO enabled | Calling Options: Specify whether you want Cisco Jabber to always make VoIP calls, always make calls with your mobile voice network, or automatically
                                          select the call method based on your network connection. Low-Bandwidth Mode: If you select a calling option that uses VoIP, Cisco Jabber displays the Low-Bandwidth Mode setting. Use this setting to optimize audio, if you make VoIP calls while you are connected to a low-bandwidth network. |

| Note | These options are not available if you enable low-bandwidth mode. |
|---|---|

| Step 1 | From the drop-down list of phone numbers next to the search bar, select the phone number you’d like to use to make the call. |
|---|---|
| Step 2 | Make the call. |

| Step 1 | Go to Calls , and select the keypad icon. |
|---|---|
| Step 2 | Use your mouse to click on the keypad to dial the number you want, and then click Call . You can use the backspace to correct
                                          any dialing mistakes. |

| Step 1 | Click the search bar and enter the name of the person you want to call. |
|---|---|
| Step 2 | In the search results, hover over their name, and click Call . |

| Step 1 | Go to Contacts , tap the search bar, and enter the name of the person you want to call. |
|---|---|
| Step 2 | In the search results, tap their name, and then tap Call . |

| From your conversation window, select Call from the top-right corner of the conversation window. |
|---|

| From the conversation window, tap , and tap the number to call. |
|---|

| From the conversation window, tap , and tap the number to call. |
|---|

| Step 1 | Enter the SIP URI. |
|---|---|
| Step 2 | (Optional) Add a comma and the DTMF tones. |
| Step 3 | Click Call . |

| Step 1 | Enter the characters of the URI including the @ symbol and at least two characters after the @. For example, aperez@ex. |
|---|---|
| Step 2 | Select Call in the bricklet to call the contact using their SIP URI. |

| Step 1 | When you receive a call from one of your contacts, choose one of these options: Answer Decline Chat reply |
|---|---|
| Step 2 | If you choose Chat reply , you can send a quick reply to the caller in the chat window. |

| Step 1 | Tap your profile picture, and then go Settings > Call Option . |
|---|---|
| Step 2 | Toggle Auto Answer to on . |

| Go to Options > Calls and turn on Mute audio by default for Jabber calls . The Calls tab is only available if you have set up Phone Services in your Accounts tab. |
|---|

| Go to Preferences > Calls and turn on Mute audio by default for Jabber calls . The Calls tab is only available if you have set up Phone Services in your Accounts tab. |
|---|

| Go to Settings > Calls and tap  Auto Mute in the Mute me on all Jabber calls field. The Calls tab is only available if you have set up Phone Services in your Accounts tab. |
|---|

| Step 1 | From the in-call view, tap More . |
|---|---|
| Step 2 | Tap Merge . |
| Step 3 | Tap OK . |
| Step 4 | (Optional) Tap to view a list of conference participants. |

| Step 1 | From the in-call view, tap More . |
|---|---|
| Step 2 | Tap Merge . |
| Step 3 | Tap OK . |
| Step 4 | (Optional) Tap to view a list of conference participants. |

| Note | Your system administrator must enable the Transfer to Mobile Network option on the server. |
|---|---|

| Step 1 | From the in-call view, tap More . |
|---|---|
| Step 2 | Tap Move to Mobile and tap OK . |
| Step 3 | Tap Answer when your device rings. |

| Step 1 | From the in-call view, tap More . |
|---|---|
| Step 2 | Tap Move to Mobile and tap OK . |
| Step 3 | Tap Answer when your device rings. |

| Step 1 | From the in-call view, tap More . |
|---|---|
| Step 2 | Tap Park . |
| Step 3 | Retrieve the call from another device or resume the call from the current device. |

| Step 1 | To get your conference call started, choose any of these methods: While on a call—convert the call to a conference call by clicking the More button on the call control strip, and then selecting the Conference Call option. From a group header—hover over a group header and click the call button to start a conference call with all of the available
                                                contacts in that group. From multiple contact selection—select the contacts that you want in your conference call and click the call button that appears
                                                when you hover over any of the selected contacts. |
|---|---|
| Step 2 | Add contacts to a conference call using these options: Search for contacts in the Add participants field. Drag contacts from your Contacts tab and drop them into the conference call window. |

| Step 1 | From the in-call view, tap More . |
|---|---|
| Step 2 | Tap Conference . |
| Step 3 | Follow one of these steps: Enter a phone number and select Call . Enter a name or video address, and tap an item in the search results. Cisco Jabber automatically places your first call on hold and displays the status of both calls. |
| Step 4 | On the control bar, tap Merge . |

| Step 1 | From the in-call view, tap More . |
|---|---|
| Step 2 | Tap Hold . |
| Step 3 | To resume the call, tap Resume . |

| Tap the red bar to toggle between the two calls. |
|---|

| Step 1 | From the in-call view, tap More . |
|---|---|
| Step 2 | Tap Transfer . |
| Step 3 | Follow one of these steps: Enter a phone number and select Call . Enter a name or video address, and tap an item in the search results. |

| Step 1 | Select the phone control menu on the main window. |
|---|---|
| Step 2 | Select Forward calls to and then select the appropriate option. |

| Step 1 | Select Jabber > Preferences > Calls . |
|---|---|
| Step 2 | Select Call Forward . |
| Step 3 | In the Forward Calls to section, do one of these options: Select Plus (+) and add a new number in the available list. Enter a phone number, including country and area codes. |

| Step 1 | Go to Settings > Call > Call forwarding . |
|---|---|
| Step 2 | Select one of these options: Do not forward calls Voicemail Mobile Home Customize—Enter the number (with country and area codes) to forward calls to an alternate number. |

| Step 1 | Go to Settings > Call > Call forwarding . |
|---|---|
| Step 2 | Select one of these options: Disable call forwarding Voicemail Mobile Home Add a number—Enter the URI or phone number (with country and area codes) to forward calls to an alternate number. |

| Step 1 | After you have started a video call, select the Show Far End Camera Control icon. |
|---|---|
| Step 2 | Choose one of these options: For direct calls to devices, use the controls to pan left or right, tilt up or down, and zoom the camera in and out. For calls to bridges, use the controls to select the conference layout that you want to use. Use the following keyboard shortcuts to manually control the camera. Option Description Tilt up Up arrow key Tilt down Down arrow key Pan left Left arrow key Pan right Right arrow key Zoom in Plus sign (Shift + Equal key) Zoom out Minus sign key | Option | Description | Tilt up | Up arrow key | Tilt down | Down arrow key | Pan left | Left arrow key | Pan right | Right arrow key | Zoom in | Plus sign (Shift + Equal key) | Zoom out | Minus sign key |
| Option | Description |
| Tilt up | Up arrow key |
| Tilt down | Down arrow key |
| Pan left | Left arrow key |
| Pan right | Right arrow key |
| Zoom in | Plus sign (Shift + Equal key) |
| Zoom out | Minus sign key |

| Option | Description |
|---|---|
| Tilt up | Up arrow key |
| Tilt down | Down arrow key |
| Pan left | Left arrow key |
| Pan right | Right arrow key |
| Zoom in | Plus sign (Shift + Equal key) |
| Zoom out | Minus sign key |

| Step 1 | After you have started a video call, select the Show Far End Camera Control icon. |
|---|---|
| Step 2 | Choose one of these options: For direct calls to devices, use the controls to pan left or right, tilt up or down, and zoom the camera in and out. For calls to bridges, use the controls to select the conference layout that you want to use. Use the following keyboard shortcuts to manually control the camera. Option Description Tilt up Up arrow key Tilt down Down arrow key Pan left Left arrow key Pan right Right arrow key Zoom in Plus sign (Shift + Equal key) Zoom out Minus sign key | Option | Description | Tilt up | Up arrow key | Tilt down | Down arrow key | Pan left | Left arrow key | Pan right | Right arrow key | Zoom in | Plus sign (Shift + Equal key) | Zoom out | Minus sign key |
| Option | Description |
| Tilt up | Up arrow key |
| Tilt down | Down arrow key |
| Pan left | Left arrow key |
| Pan right | Right arrow key |
| Zoom in | Plus sign (Shift + Equal key) |
| Zoom out | Minus sign key |

| Option | Description |
|---|---|
| Tilt up | Up arrow key |
| Tilt down | Down arrow key |
| Pan left | Left arrow key |
| Pan right | Right arrow key |
| Zoom in | Plus sign (Shift + Equal key) |
| Zoom out | Minus sign key |

| Step 1 | After you have started a video call, select the Show Far End Camera Control icon. |
|---|---|
| Step 2 | Choose one of these options: For direct calls to devices, use the controls to pan left or right, tilt up or down, and zoom the camera in and out. For calls to bridges, use the controls to select the conference layout that you want to use. Use the following keyboard shortcuts to manually control the camera. Option Description Tilt up Up arrow key Tilt down Down arrow key Pan left Left arrow key Pan right Right arrow key Zoom in Plus sign (Shift + Equal key) Zoom out Minus sign key | Option | Description | Tilt up | Up arrow key | Tilt down | Down arrow key | Pan left | Left arrow key | Pan right | Right arrow key | Zoom in | Plus sign (Shift + Equal key) | Zoom out | Minus sign key |
| Option | Description |
| Tilt up | Up arrow key |
| Tilt down | Down arrow key |
| Pan left | Left arrow key |
| Pan right | Right arrow key |
| Zoom in | Plus sign (Shift + Equal key) |
| Zoom out | Minus sign key |

| Option | Description |
|---|---|
| Tilt up | Up arrow key |
| Tilt down | Down arrow key |
| Pan left | Left arrow key |
| Pan right | Right arrow key |
| Zoom in | Plus sign (Shift + Equal key) |
| Zoom out | Minus sign key |

| Step 1 | After you have started a video call, select the Show Far End Camera Control icon. |
|---|---|
| Step 2 | Choose one of these options: For direct calls to devices, use the controls to pan left or right, tilt up or down, and zoom the camera in and out. For calls to bridges, use the controls to select the conference layout that you want to use. Use the following keyboard shortcuts to manually control the camera. Option Description Tilt up Up arrow key Tilt down Down arrow key Pan left Left arrow key Pan right Right arrow key Zoom in Plus sign (Shift + Equal key) Zoom out Minus sign key | Option | Description | Tilt up | Up arrow key | Tilt down | Down arrow key | Pan left | Left arrow key | Pan right | Right arrow key | Zoom in | Plus sign (Shift + Equal key) | Zoom out | Minus sign key |
| Option | Description |
| Tilt up | Up arrow key |
| Tilt down | Down arrow key |
| Pan left | Left arrow key |
| Pan right | Right arrow key |
| Zoom in | Plus sign (Shift + Equal key) |
| Zoom out | Minus sign key |

| Option | Description |
|---|---|
| Tilt up | Up arrow key |
| Tilt down | Down arrow key |
| Pan left | Left arrow key |
| Pan right | Right arrow key |
| Zoom in | Plus sign (Shift + Equal key) |
| Zoom out | Minus sign key |

| Step 1 | In the Jabber Phone tab, dial the conference bridge number or click the link that is provided to you. Then, enter the passcode,
                                          if needed. |
|---|---|
| Step 2 | In the call window, click More to display the menu and select Record . After several seconds, an automated voice announces that the recording has started. |
| Step 3 | To stop the recording, click More > Stop . The recording automatically stops when the call ends and a link to the recording is sent out. |

| Step 1 | From the in-call view, tap More . |
|---|---|
| Step 2 | Tap Call Statistics . |