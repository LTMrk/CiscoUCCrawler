---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cuipph-800-series-adminguide-w800-b-wireless-800-administration-guide-w800-m-d6dd5627ef
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cuipph/800-series/adminguide/w800_b_wireless-800-administration-guide/w800_m_appendix.html
retrieved_at: 2026-08-21T23:27:36.812261+00:00
---

Cisco Wireless Phone 840 and 860 Administration Guide for Cisco Unified Communications Manager

# Cisco Wireless Phone 840 and 860 Administration Guide for Cisco Unified Communications Manager

Updated: August 13, 2026

Chapter: Appendix

## Chapter: Appendix

# Appendix

## InformaCast Advanced Notification Support

### Configure and Troubleshoot Informacast

In general, Cisco Wireless Phone 840 or 860 support multicast audio broadcasts, text notifications, and user feedback to the
                              InformaCast server using the XSI APIs. InformaCast can be configured to use HTTP or Cisco Unified Communications Manager JTAPI
                              interfaces to the Cisco Unified Communications Manager.

For more information about Configure and Troubleshoot Informacast, see Configure and Troubleshoot Informacast

### Unsupported InformaCast Features

Cisco Wireless Phone 840 or 860 currentlly doesnot support Push to Talk and Quick Page services. Phones subscribed to these
                              services will have no way to activate the service on the device. Cisco Wireless Phone 840 or 860 also does not support One
                              Button Paging, where the QuickPage service is assigned to a Service URL button in the device’s Phone Button Template. As the
                              phone does not allow configuration of buttons in the Cisco Unified Communications Manager.

### Partially Supported InformaCast Features

Call Aware

Call Aware is primarily used to detect when a 911 emergency call has been dialed, which then triggers an InformaCast broadcast.
                              It can also be used to detect calls to numbers other than 911, monitor calls that have been detected, and record those calls.
                              For example, you could use it to trigger an InformaCast broadcast whenever someone calls the Front Desk, and a supervisor
                              could elect to monitor those calls for quality assurance or record them for review later. Cisco Wireless Phone 840 or 860
                              does not support monitoring and recording of calls.

Text and Audio Messages using Talk and Listen

InformaCast messages that contain both text and audio can be configured with the option to “Start a phone call with any phones
                              in a recipient group and allow everyone to speak in real time (Talk and Listen)”. When Cisco Wireless Phone 840 or 860 receives
                              one of these messages, the “talk” and “exit” softkeys are not displayed, so the Cisco Wireless Phone 840 or 860 can only listen
                              to other phones that are transmitting audio.

### Notes on InformaCast Features

Panic Button

Cisco Wireless Phone 840 or 860 have a red button which by default is configured to be the Emergency button on the device.
                              This function can also be mapped to other device buttons using the Buttons application. Using the Emergency app, you can configure
                              the phone to trigger an alarm or make an emergency call through the CiscoPhone app when the user does either a long press,
                              2 short presses, or 2 short or one long press of the configured Emergency button. By default, no actions are taken.

InformaCast’s panic button service can be used with or without the configuration of the Emergency app. In the step where the
                              Cisco IP Phone Service is configured on the Cisco Unified Communications Manager ( Create an InformaCast XML Service (singlewire.com) ), the Cisco IP Phone Service created must be named InformaCast (this is not case-sensitive), otherwise the device will not recognize it as a service configured for the Panic button feature,
                              and there will be no way for the user to activate it.

If the Emergency App is enabled, it continues to do what it currently does when the panic button is pressed. If both InformaCast
                              and the Emergency App are being used, the Emergency app should be configured to trigger the alarm after one long press of
                              the button, because if 2 presses are configured, the InformaCast service will be triggered twice. The Red circular on-screen
                              panic button press in the Emergency app will not trigger the InformaCast panic button service.

Other Notes

If the phone is not in an active call, the Cisco Wireless Phone 840 or 860 displays a notification to the user when it receives
                              a broadcast message from InformaCast.

The user can choose to view or ignore the message and stop the multicast audio stream by touching the corresponding button
                              on the notification. If a broadcast contains audio only, this behavior differs from the 8821, which has no way of disabling
                              the audio stream. If the phone is in a call, the multicast audio stream will not be played unless the user elects to play
                              it by clicking on the button in the notification, which will place the existing call on hold.

If the phone is locked, the broadcast message is automatically displayed, and audio is played (if not in a call) without any
                              user interaction. The user still has the ability to stop the audio through the stop button on the displayed message. If the
                              user is in a call while the phone is locked, then ANSWER button in the notification must be clicked to hear the broadcast.

Phone vibration settings set on the InformaCast Broadcast Parameters page are ignored by Cisco Wireless Phone 840 or 860.

Cisco Wireless Phone 840 or 860 behaves as shown in the following table when multiple broadcasts are sent by InformaCast,
                              depending on the configuration of the Enable Message Blending check box on the InformaCast Broadcast Parameters page:

Priority and Arrival Order

Blending Enabled

Blending Disabled

Lower priority broadcast (A) followed by higher priority broadcast (B).

Switches from playing broadcast A to playing broadcast B; once B is over, switches back to playing the rest of A.

Switches from playing broadcast A to playing broadcast B; once B is over, switches back to playing the rest of A.

Broadcast (A) followed by broadcast (B) with the same priority.

Plays A in full, ignores broadcast B.

Plays broadcast A in full, then switches to playing the rest of B.

Higher priority broadcast (A) followed by lower priority broadcast (B).

Plays broadcast A in full, then switches to playing the rest of broadcast B.

Plays broadcast A in full, then switches to playing the rest of broadcast B.

## CTI-Controlled Support

### Need

InformaCast can use either HTTP or Cisco Unified Communications Manager JTAPI.

Using Cisco Unified Communications Manager JTAPI requires Cisco Unified Communications Manager to say the device supports
                              computer telephony integration (CTI).

The one key feature that is used by InformaCast is XSI object pass thru – see page 276 of the Cisco Unified Communications
                              Manager JTAPI developers guide:

XSI Object Pass Through Applications can pass XML objects through Cisco Unified Communications Manager JTAPI and CTI interfaces to the phone. The
                              XML object can contain display updates, softkey update/enable/disable, and other types of updates on the phone that are available
                              through Cisco IP Phone Services features. This allows applications to access Cisco IP Phone Service capabilities through Cisco
                              Unified Communications Manager JTAPI and CTI interfaces without maintaining independent connections to the phones.

Authentication and Mechanism Sending an HTTP POST request to the phone web server, which requires the phone IP address, performs an object push. The web
                              server parses the request, authorizes the request through the HTTP that is returned to the Cisco Unified Communications Manager,
                              runs the request, and returns an XML response that indicates the success or failure of the request to the application. With
                              XSI, the Cisco IP Phone Services object gets sent directly to the phone by the Skinny Client Control Protocol (SCCP). The
                              phone does not authenticate the request, because the Cisco Unified Communications Manager JTAPI client is trusted and does
                              not require the phone IP address. For more information on actual XML contents, see the Cisco IP Phone Services Application
                              Development Notes.

### Discussion

Cisco Wireless Phone 840 or 860 offers limited CTI support and customers can enable and test functionality with Third-party
                              Software that exercises the CTI, but their results maybe limited based on what exact functionality is exercised by the Third-party
                              Software.

### SIP Signaling and CTI

The line messaging guide details the kinds of remotecc REFERs we can get from CTI.

The following requests are supported from Cisco Unified Communications Manager to the phone. Details are in the CMCM 8.0 Line
                              Messaging guide (see table on page 78) and CUCM 12 version of the guide on page 125.

Remote cc request

Purpose

Currently supported in CiscoPhone app

initiatecallreq

Triggers endpoint to send an INVITE to Cisco Unified CM. An offhook NOTIFY may precede this INVITE

No

holdretrievereq

Used to resume a held dialog.

No

privacyreq

Used to send shared line privacy setting to the endpoint

Yes

statuslineupdatereq

Used to display a status message on a phone UI

Yes (although we do not display the message passed in this by the CUCM – we use our own logic). Looks like this was put in
                                          when we did CUCM conferencing and is used for call pickup Our code is feature state specific and this could come with no context.

playtonereq

Used to play a tone at the device.

Yes – for call pickup. Initially we also would get this with CUCM conferencing, but we changed the implementation method.
                                          Our code is feature state specific and this could come with no context.

cfwdallupdate

Used to send call forward all settings to the endpoint for a particular line

Yes, this is how devices learn whether CFA is active when they first register.

datapassthroughreq

Cisco Unified CM uses Data PassThrough Request to pass subelements to features and CTI applications

Yes (new in 1.10 for supporting XSI over JTAPI)

holdreversionreq

The Cisco Unified CM hold reversion feature uses this request to trigger the endpoint to invoke hold reversion on the specified
                                          call

No

monitorcallreq

CTI applications use this to request that a phone begin monitoring a call on another phone.

No – but will if we implement silent monitoring

dndrequest

CTI applications use this to request that a phone simulate the user pressing the DND softkey. This toggles the phone DND state
                                          from enabled to disabled or from disabled to endabled

No

dndupdate

Cisco Unified CM uses this request to convey DND status and DND option settings when either setting is modified by using the
                                          Cisco Unified CM web administrative interface

No

Linekeyupdate

CTI uses this to request the phone to update the Intercom speeddial setting.

No

talkbackreq

CTI applications use this request to initiate Intercom talkback for establishing two-way media.

No

dialdtmfreq

Requests phone to dial the DTMF digit

No. This is only in the 12.5 document

Even if we do not support a particular request, we should still send an appropriate SIP response and a terminating NOTIFY,
                              if necessary.

Part of supporting CTI is also that the phone informs CUCM of various events via remotecc REFER messages. See the table on
                              page 120 of the 12.5 version of the document:

Remotecc request

Feature

Description

Currently supported in CiscoPhone app

softkeyeventmsg

conference

Create a conference

Yes, for CUCM conferencing

softkeyeventmsg

park

Park a call

Yes – note we use parkmonitor, not park. Parkmonitor is not listed in the document.

softkeyeventmsg

conflist

List participants in a conference

No. We use the NOTIFY sent from CUCM. We don’t support the phone pressing the softkey to get it.

softkeyeventmsg

rmlastconf

Remove last participant added to a conference

No

softkeyeventmsg

idivert

Activate immediate diversion feature

Yes

softkeyeventmsg

callback

The CallBack feature allows you to receive notification when a busy extension is available to receive calls. You can activate
                                          Call Back for a destination phone that is within the same Unified Communications Manager cluster as your phone or on a remote
                                          Private Integrated Network Exchange (PINX) over QSIG trunks or QSIG-enabled intercluster trunks.

No

Softkeyeventmsg

Qrt

Quality Reporting Tool

No

Softkeyeventmsg

Select

Allows a call to be locked such that remote devices can’t remotely resume a held call.

Yes

Softkeyeventmsg

Unselect

Opposite of Select

Yes

Softkeyeventmsg

Privacy

Toggle privacy status for all lines on the phone

Yes

Linekeyeventmsg

This is how the phone sends line key presses to the CUCM for features that don’t have an associated standard SIP primitive
                                          in this release. Document mentions privacy, but we support that through softkey press.

No

Datapassthrureq

Send XSI XML key presses to CUCM features and CTI applications

No

jtapi - Cisco Developer

Cisco Unified JTAPI Developers Guide for Cisco Unified Communications Manager, Release 14 and SUs (upload-large-file.s3.us-east-2.amazonaws.com)

## Android 13 App Permissions

With firmware release 2.1(0) for Cisco Wireless Phone 860, the Android OS is upgraded from version 10 to 13. Since Android
                              13 manages permissions differently, Cisco application permissions must be granted for the CP-860 software to function properly.

If the phone is managed by a Cisco Wireless Phone Configuration Management Utility configuration file, permissions are granted
                              automatically. If the phone is managed by an EMM (Enterprise Mobility Management) solution, you must configure the EMM to
                              grant all necessary permissions in the configuration profile or within the specific application settings. Additionally, location
                              services must be enabled on the Android device.

The table below lists the app and the respective permission.

Barcode

android.permission.CAMERA <br> android.permission.READ_PHONE_STATE <br> android.permission.CALL_PHONE <br> android.permission.POST_NOTIFICATIONS
                                          <br> android.permission.READ_EXTERNAL_STORAGE <br> android.permission.WRITE_EXTERNAL_STORAGE

Battery Life

android.permission.POST_NOTIFICATIONS

Cisco Phone

android.permission.READ_CALL_LOG <br> android.permission.WRITE_CALL_LOG <br> android.permission.CAMERA <br> android.permission.READ_CONTACTS
                                          <br> android.permission.WRITE_CONTACTS <br> android.permission.RECORD_AUDIO <br> android.permission.CALL_PHONE <br> android.permission.READ_PHONE_STATE
                                          <br> android.permission.POST_NOTIFICATIONS <br> android.permission.USE_SIP <br> android.permission.ACCESS_COARSE_LOCATION
                                          <br> android.permission.ACCESS_FINE_LOCATION <br> android.permission.ACCESS_BACKGROUND_LOCATION <br><br> Additionally, Android
                                          must be configured to allow the use of location services by turning on the Use location setting in Android settings > Location.

Custom Settings

android.permission.BLUETOOTH_CONNECT <br> android.permission.POST_NOTIFICATIONS <br> android.permission.READ_PHONE_STATE <br>
                                          android.permission.READ_MEDIA_IMAGES <br> android.permission.READ_EXTERNAL_STORAGE

Diagnostics

android.permission.CAMERA <br> android.permission.ACCESS_FINE_LOCATION <br> android.permission.ACCESS_COARSE_LOCATION <br>
                                          android.permission.BLUETOOTH_SCAN <br> android.permission.BLUETOOTH_CONNECT <br> android.permission.RECORD_AUDIO <br> android.permission.READ_EXTERNAL_STORAGE
                                          <br> android.permission.WRITE_EXTERNAL_STORAGE

Logging

android.permission.READ_PHONE_STATE <br> android.permission.POST_NOTIFICATIONS

Emergency

android.permission.POST_NOTIFICATIONS

Sound Stage

android.permission.POST_NOTIFICATIONS

System Updater

android.permission.READ_PHONE_STATE <br> android.permission.POST_NOTIFICATIONS

Web API

android.permission.ACCESS_FINE_LOCATION <br> android.permission.READ_PHONE_STATE <br> android.permission.POST_NOTIFICATIONS
                                          <br> android.permission.ACCESS_COARSE_LOCATION <br> android.permission.CALL_PHONE

AppUrl Buttons PIT Call Quality

(No permission requested)

| Priority and Arrival Order | Blending Enabled | Blending Disabled |
|---|---|---|
| Lower priority broadcast (A) followed by higher priority broadcast (B). | Switches from playing broadcast A to playing broadcast B; once B is over, switches back to playing the rest of A. | Switches from playing broadcast A to playing broadcast B; once B is over, switches back to playing the rest of A. |
| Broadcast (A) followed by broadcast (B) with the same priority. | Plays A in full, ignores broadcast B. | Plays broadcast A in full, then switches to playing the rest of B. |
| Higher priority broadcast (A) followed by lower priority broadcast (B). | Plays broadcast A in full, then switches to playing the rest of broadcast B. | Plays broadcast A in full, then switches to playing the rest of broadcast B. |

| Remote cc request | Purpose | Currently supported in CiscoPhone app |
|---|---|---|
| initiatecallreq | Triggers endpoint to send an INVITE to Cisco Unified CM. An offhook NOTIFY may precede this INVITE | No |
| holdretrievereq | Used to resume a held dialog. | No |
| privacyreq | Used to send shared line privacy setting to the endpoint | Yes |
| statuslineupdatereq | Used to display a status message on a phone UI | Yes (although we do not display the message passed in this by the CUCM – we use our own logic). Looks like this was put in
                                          when we did CUCM conferencing and is used for call pickup Our code is feature state specific and this could come with no context. |
| playtonereq | Used to play a tone at the device. | Yes – for call pickup. Initially we also would get this with CUCM conferencing, but we changed the implementation method.
                                          Our code is feature state specific and this could come with no context. |
| cfwdallupdate | Used to send call forward all settings to the endpoint for a particular line | Yes, this is how devices learn whether CFA is active when they first register. |
| datapassthroughreq | Cisco Unified CM uses Data PassThrough Request to pass subelements to features and CTI applications | Yes (new in 1.10 for supporting XSI over JTAPI) |
| holdreversionreq | The Cisco Unified CM hold reversion feature uses this request to trigger the endpoint to invoke hold reversion on the specified
                                          call | No |
| monitorcallreq | CTI applications use this to request that a phone begin monitoring a call on another phone. | No – but will if we implement silent monitoring |
| dndrequest | CTI applications use this to request that a phone simulate the user pressing the DND softkey. This toggles the phone DND state
                                          from enabled to disabled or from disabled to endabled | No |
| dndupdate | Cisco Unified CM uses this request to convey DND status and DND option settings when either setting is modified by using the
                                          Cisco Unified CM web administrative interface | No |
| Linekeyupdate | CTI uses this to request the phone to update the Intercom speeddial setting. | No |
| talkbackreq | CTI applications use this request to initiate Intercom talkback for establishing two-way media. | No |
| dialdtmfreq | Requests phone to dial the DTMF digit | No. This is only in the 12.5 document |

| Remotecc request | Feature | Description | Currently supported in CiscoPhone app |
|---|---|---|---|
| softkeyeventmsg | conference | Create a conference | Yes, for CUCM conferencing |
| softkeyeventmsg | park | Park a call | Yes – note we use parkmonitor, not park. Parkmonitor is not listed in the document. |
| softkeyeventmsg | conflist | List participants in a conference | No. We use the NOTIFY sent from CUCM. We don’t support the phone pressing the softkey to get it. |
| softkeyeventmsg | rmlastconf | Remove last participant added to a conference | No |
| softkeyeventmsg | idivert | Activate immediate diversion feature | Yes |
| softkeyeventmsg | callback | The CallBack feature allows you to receive notification when a busy extension is available to receive calls. You can activate
                                          Call Back for a destination phone that is within the same Unified Communications Manager cluster as your phone or on a remote
                                          Private Integrated Network Exchange (PINX) over QSIG trunks or QSIG-enabled intercluster trunks. | No |
| Softkeyeventmsg | Qrt | Quality Reporting Tool | No |
| Softkeyeventmsg | Select | Allows a call to be locked such that remote devices can’t remotely resume a held call. | Yes |
| Softkeyeventmsg | Unselect | Opposite of Select | Yes |
| Softkeyeventmsg | Privacy | Toggle privacy status for all lines on the phone | Yes |
| Linekeyeventmsg |  | This is how the phone sends line key presses to the CUCM for features that don’t have an associated standard SIP primitive
                                          in this release. Document mentions privacy, but we support that through softkey press. | No |
| Datapassthrureq |  | Send XSI XML key presses to CUCM features and CTI applications | No |

| Application | Permission |
|---|---|
| Barcode | android.permission.CAMERA <br> android.permission.READ_PHONE_STATE <br> android.permission.CALL_PHONE <br> android.permission.POST_NOTIFICATIONS
                                          <br> android.permission.READ_EXTERNAL_STORAGE <br> android.permission.WRITE_EXTERNAL_STORAGE |
| Battery Life | android.permission.POST_NOTIFICATIONS |
| Cisco Phone | android.permission.READ_CALL_LOG <br> android.permission.WRITE_CALL_LOG <br> android.permission.CAMERA <br> android.permission.READ_CONTACTS
                                          <br> android.permission.WRITE_CONTACTS <br> android.permission.RECORD_AUDIO <br> android.permission.CALL_PHONE <br> android.permission.READ_PHONE_STATE
                                          <br> android.permission.POST_NOTIFICATIONS <br> android.permission.USE_SIP <br> android.permission.ACCESS_COARSE_LOCATION
                                          <br> android.permission.ACCESS_FINE_LOCATION <br> android.permission.ACCESS_BACKGROUND_LOCATION <br><br> Additionally, Android
                                          must be configured to allow the use of location services by turning on the Use location setting in Android settings > Location. |
| Custom Settings | android.permission.BLUETOOTH_CONNECT <br> android.permission.POST_NOTIFICATIONS <br> android.permission.READ_PHONE_STATE <br>
                                          android.permission.READ_MEDIA_IMAGES <br> android.permission.READ_EXTERNAL_STORAGE |
| Diagnostics | android.permission.CAMERA <br> android.permission.ACCESS_FINE_LOCATION <br> android.permission.ACCESS_COARSE_LOCATION <br>
                                          android.permission.BLUETOOTH_SCAN <br> android.permission.BLUETOOTH_CONNECT <br> android.permission.RECORD_AUDIO <br> android.permission.READ_EXTERNAL_STORAGE
                                          <br> android.permission.WRITE_EXTERNAL_STORAGE |
| Logging | android.permission.READ_PHONE_STATE <br> android.permission.POST_NOTIFICATIONS |
| Emergency | android.permission.POST_NOTIFICATIONS |
| Sound Stage | android.permission.POST_NOTIFICATIONS |
| System Updater | android.permission.READ_PHONE_STATE <br> android.permission.POST_NOTIFICATIONS |
| Web API | android.permission.ACCESS_FINE_LOCATION <br> android.permission.READ_PHONE_STATE <br> android.permission.POST_NOTIFICATIONS
                                          <br> android.permission.ACCESS_COARSE_LOCATION <br> android.permission.CALL_PHONE |
| AppUrl Buttons PIT Call Quality | (No permission requested) |