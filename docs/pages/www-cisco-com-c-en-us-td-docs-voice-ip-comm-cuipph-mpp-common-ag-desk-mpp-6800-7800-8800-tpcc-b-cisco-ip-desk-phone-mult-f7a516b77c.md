---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cuipph-mpp-common-ag-desk-mpp-6800-7800-8800-tpcc-b-cisco-ip-desk-phone-mult-f7a516b77c
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cuipph/MPP/common/ag_desk_mpp_6800_7800_8800/tpcc_b_cisco-ip-desk-phone-multiplatform/tpcc_m_calling-features-config-1131.html
retrieved_at: 2026-08-21T13:46:46.405977+00:00
---

Cisco IP Desk Phone with Multiplatform Firmware (MPP) － Administration Guide

# Cisco IP Desk Phone with Multiplatform Firmware (MPP) － Administration Guide

Updated: November 19, 2025

Chapter: Call Features Configuration

## Chapter: Call Features Configuration

# Call Features Configuration

The phone web user interface and the xml configuration files allows you to customize calling features of your phone such as
                           call transfer, call park, conferencing, and speed-dial.

## Enable Call Transfer

You can enable attended call transfer and blind call transfer services for your user.

You can also configure the parameters in the phone configuration file with
                              XML(cfg.xml) code. To configure each parameter, see the syntax of the string in Parameters for Enable Call Transfer table.

### Before you begin

Access the phone administration web page. See Access the Phone Web Interface .

Step 1

Select Voice > Phone .

Step 2

Under Supplementary
                                          Services , configure the parameters as defined in the Parameters for Enable Call Transfer table.

Step 3

Click Submit All Changes .

### Parameters for Enable Call Transfer

The following table defines the function and usage of Enable Call Transfer parameters in the Supplementary Services section
                                    under the Phone tab in the phone web interface. It also defines the syntax of the string that is added in the phone configuration
                                    file with XML(cfg.xml) code to configure a parameter.

Parameter

Description

Attn Transfer Serv

Attended call transfer service. The user answers the call before transferring it.

Perform one of the following:

In the phone configuration file with XML(cfg.xml), enter a string in this format:

In the phone web page, select Yes to enable the transfer service. Select No to disable it.

Options: Yes and No

Default: Yes

Blind Transfer Serv

Blind call transfer service. The user transfers the call without speaking to the caller.

Perform one of the following:

In the phone configuration file with XML(cfg.xml), enter a string in this format:

In the phone web page, select Yes to enable the transfer service. Select No to disable it.

Options: Yes and No

Default: Yes

## Call Forward

To enable call forward, you can enable the feature in two places: on the Voice tab and the User tab of the phone web page.

### Enable Call Forward on Voice Tab

Perform this task if you want to enable call forward for a user.

You can also configure the parameters in the phone configuration file with XML(cfg.xml) code. To configure each parameter,
                                 see the syntax of the string in the Parameters for Enable Call Forward on Voice Tab table.

#### Before you begin

Access the phone administration web page. See Access the Phone Web Interface .

Step 1

Select Voice > Phone .

Step 2

Under Supplementary Services , configure the parameters as described in the Parameters for Enable Call Forward on Voice Tab table.

Step 3

Click Submit All Changes .

#### Parameters for Enable Call Forward on Voice Tab

The following table defines the function and usage of  Enable Call Forward on Voice Tab parameters in the Supplementary Services
                                       section under the Phone tab in the phone web interface. It also defines the syntax of the string that is added in the phone
                                       configuration file with XML(cfg.xml) code to configure a parameter.

Parameter

Description

Cfwd All Serv

Forwards all calls.

Perform one of the following:

In the phone configuration file with XML(cfg.xml), enter a string in this format:

In the phone web page, select Yes to forward all calls. Select No to disable it.

Options: Yes and No

Default: Yes

Cfwd Busy Serv

Forwards calls only if the line is busy.

Perform one of the following:

In the phone configuration file with XML(cfg.xml), enter a string in this format:

In the phone web page, select Yes to forward calls when the line is busy. Select No to disable it.

Options: Yes and No

Default: Yes

Cfwd No Ans Serv

Forwards calls only if the line is not answered.

Perform one of the following:

In the phone configuration file with XML(cfg.xml), enter a string in this format:

In the phone web page, select Yes to forward calls if the line is not answered. Select No to disable it.

Options: Yes and No

Default: Yes

### Enable Call Forward on User Tab

Perform the following task to change the call forward settings from the phone web page.

The settings of call forward are synchronized between the phone and the server when one of the following ways is enabled:

Feature key synchronization (FKS)

BroadSoft's Extended Services Interface (XSI) Synchronization

To ensure the settings of call forward on the local phone take effect, you need to disable FKS and XSI first. See Enable Feature Key Sync and Enable Call Forward Status Sync via XSI Service .

The priority of taking effect for call forward setting in the supported modes is: FKS > XSI > Local.

#### Before you begin

Access the phone administration web page. See Access the Phone Web Interface .

Ensure that the call forward setting is enabled on the Voice tab. See Enable Call Forward on Voice Tab .

Step 1

Select Voice > User .

Step 2

In the Call Forward section, configure the parameters as described in the Parameters for Enable Call Forward on User Tab table.

Step 3

Click Submit All Changes .

#### Parameters for Enable Call Forward on User Tab

The following table defines the function and usage of Voice > User > Call Forward in the phone web page. It also defines the
                                    syntax of the string that is added in the phone configuration file with XML(cfg.xml) code to configure a parameter.

Parameter

Description

Cfwd All

Forwards all calls. The setting of this parameter takes precedence over Cfwd Busy and Cfwd No Answer.

Perform one of the following:

In the phone configuration file with XML(cfg.xml), enter a string in this format:

In the phone web page, select Yes to forward all calls. Select No to disable it.

Options: Yes and No

Default: No

Cfwd All Dest

Specifies the destination to which all calls are forwarded. The destination can be an alphanumeric input, a phone number,
                                                or a SIP URI.

Perform one of the following:

In the phone configuration file with XML(cfg.xml), enter a string in this format:

In the phone web page, enter the destination number in the field.

When you select Yes for Cfwd All, make sure to configure the parameter.

Default: Empty

Cfwd Busy

Forwards calls only if the line is busy.

Perform one of the following:

In the phone configuration file with XML(cfg.xml), enter a string in this format:

In the phone web page, select Yes to forward calls when the line is busy. Select No to disable it.

Options: Yes and No

Default: No

Cfwd Busy Dest

Specifies the destination to which calls are forwarded if the line is busy. The destination can be an alphanumeric input,
                                                a phone number, or a SIP URI.

Perform one of the following:

In the phone configuration file with XML(cfg.xml), enter a string in this format:

In the phone web page, enter the destination number in the field.

When you select Yes for Cfwd Busy, make sure to configure the parameter.

Default: Empty

Cfwd No Answer

Forwards the incoming call only if the call isn’t answered.

Perform one of the following:

In the phone configuration file with XML(cfg.xml), enter a string in this format:

In the phone web page, select Yes to forward the incoming call if the call isn't answered. Select No to disable it.

Options: Yes and No

Default: No

Cfwd No Ans Dest

Specifies the phone number of destination to which the incoming call is forwarded if the call isn’t answered. The destination
                                                can be an alphanumeric input, a phone number, or a SIP URI.

Perform one of the following:

In the phone configuration file with XML(cfg.xml), enter a string in this format:

In the phone web page, enter the destination number in the field.

When you select Yes for Cfwd No Answer, make sure to configure the parameter.

Default: Empty

Cfwd No Ans Delay

Assigns a response delay time (in seconds) for the no answer scenario.

Perform one of the following:

In the phone configuration file with XML(cfg.xml), enter a string in this format:

In the phone web page, enter the delay time in the field.

Default: 20

Forward Softkey

Controls the scope of the call forward services that the user can set up by a dedicated softkey. Options are:

All Cfwds : Allows the user to set up all call forward services, including Call Forward All, Call Forward Busy, and Call Forward No
                                                      Answer by pressing the Forward softkey.

In this setting, the softkey name is Forward for activation and Clr fwd for deactivation.

Only the Cfwd All : Allows the user to directly set up the Call Forward All service by pressing the softkey Forward all .

The user can still set up all call forward services from the Settings > User preferences > Call preferences > Call forwarding > Call forward settings screen.

In this setting, the softkey name is Forward all for activation and Clr fwd all for deactivation.

Perform one of the following:

In the phone configuration file with XML(cfg.xml), enter a string in this format:

In the phone web page, select the value that determines the scope of the call forward services for the users.

The parameter takes effect even though FKS, XSI, or FAC is enabled.

Default: All Cfwds

## Enable Feature Activation Code Synchronization for Forward All Calls

You can synchronize forwarding all calls feature to the server with a Feature Activation Code (FAC). When you enable this
                              feature, the FAC sends out the star code and the destination number with INVITE to the server.

### Before you begin

Access the phone administration web page. See Access the Phone Web Interface .

Step 1

Select Voice > Ext (n) .

Step 2

In the Feature Activation Code Sync field, select Yes to enable the feature.

After you enable this feature, your user can press the Forward or Forward all softkey on the phone and enter the destination contact number. When the user presses the Call softkey, a voice message plays to confirm the call forward setting status. After successful configuration, a call forward icon displays at the top of the phone screen.

The softkey name is different based on the value of the parameter Forward Softkey , see Parameters for Enable Call Forward on User Tab .

In the phone configuration file with XML(cfg.xml), enter a string in this format:

where, n is the extension number.

Default value: No

Allowed values: Yes or No

Step 3

Click Submit All Changes .

### Set Feature Activation Code for the Call Forward All Service

You can set activation code (star code) that can be used to activate or deactivate the call forward all service.

#### Before you begin

Access the phone administration web page. See Access the Phone Web Interface .

Step 1

Select Voice > Regional .

Step 2

In the Vertical Service Activation Codes section, ensure that the Cfwd All Act Code field is set to the value defined by the server. The default value is *72.

In the phone configuration file with XML(cfg.xml), enter a string in this format:

Step 3

In the Vertical Service Activation Codes section, ensure that the Cfwd All Deact Code field is set to the value defined by the server. The default value is *73.

In the phone configuration file with XML(cfg.xml), enter a string in this format:

Step 4

Click Submit All Changes .

Your user can dial *72 in combination with the destination number and press the Call softkey to activate the call forward all service.

Your user can dial *73 and press the Call softkey to deactivate the call forward all service.

## Webex One Button to Join on Phone

Webex One button to Join (OBTJ) facilitates user to join Webex meeting from the phone. To enable this feature the phone should
                              onboarded to Webex cloud. You can enable this feature from the phone configuration file. You should also enable the phone
                              with meeting service. You can add the Meetings softkey on the home screen of the phone from the phone web interface. To get more information on how to add the Meetings softkey, see Add Meetings Softkey on Phone .

OBTJ enables the phone with the following functionalities.

Phone displays a meeting notification window as a reminder five minutes before a scheduled meeting. The phone displays mutiple
                                    softkeys, Meetings , Join , Snooze , Ignore on this notification window to help user decide to join a meeting or to ignore it. If there are multiple meetings at the
                                    same time, new notification window pops up and the previous notification window disappears.

User presses the Meetings softkey to check the list of meetings on the phone scheduled for next 24 hours. If the meeting is in-progress, phone displays
                                    duration of the meeting since the start time. For upcoming meetings, the phone displays the meeting start time and end time.

User can press the Join button to join a Webex meeting. If the user presess Snooze softkey, the notification window of this meeting disappears temporarily, and again pops up after 5 minutes. User can also
                                    press Ignore softkey to ignore the meeting notification. When user presses Ignore softkey, it only ignores the current meeting and doesn't ignore all the meetings in the list.

If the meeting has no SIP URI, Join softkey is not available on the notification window and in the meeting list.

For video meetings, user can press Self-view on or Self-view off softkey on the phone to show or hide the self-view.

In Firmware release 11.3(7), user can join meeting only with SIP URL. OBTJ with user account is supported but workspace account
                                          is not supported.

### Add Meetings Softkey on Phone

You can add Meetings softkey on the home screen of the phone and check details of scheduled meetings.

#### Before you begin

Phone onboards to Cisco Webex cloud successfully.

Access the phone administration web page. See Access the Phone Web Interface .

Step 1

Select Voice > Phone .

Step 2

In the Programmable Softkeys section, set the Programmable Softkey Enable to Yes .

Step 3

In the Idle Key List and Missed Call Key List field, enter meetings in the key list.

Edit the field as described in the following example:

Meetings softkey gets added to the phone screen. When Idle Key List field doesn't have meetings keyword in the field, the softkey doesn't appear.

Step 4

Click Submit All Changes .

## Control Webex OBTJ Meetings (8800 Only)

You can enable a phone with the ability of displaying multiple OBTJ meeting notificaitons in the Meetings list and  to control these meetings.

When meeting service is enabled phone shows following behaviour:

Meetings list displays all meetings scheduled for a specific day. For example, if today is Jan 3rd, the list will display all the
                                    meetings scheduled for Jan 3rd, it will not display next day meetings.

Barge and BargeSlnt softkeys are not visible.

PIN challenge meetings are not supported.

### Before you begin

Access the phone administration web page. See Access the Phone Web Interface .

Phone onboards to Cisco Webex cloud successfully.

Phone has Meeting service enabled.

Step 1

Select Voice > Phone .

Step 2

In the Webex section, set up Calender Enable to Yes or No .

You can configure this parameter in the phone configuration XML file (cfg.xml) by entering a string in this format:

```
<Webex_Calendar_Enable ua="na">No</Webex_Calendar_Enable>
```

When you set Calender Enable to Yes , phone supports Webex OBTJ meetings with display of multiple meeting notifications in the meeting list. Also, Meeting softkey appears. To know more about adding the Meeting softkey, see Add Meetings Softkey on Phone .

Step 3

Click Submit All Changes .

## Configure Connected Meeting Key List (8800 only)

In a connected meeting, user can use leave, self-view off/on, dnd, psk (only DTMF) softkeys.

You can also control the video layout during a meeting usning Layout softkey on the phone.

### Before you begin

Access the phone administration web page. See Access the Phone Web Interface .

Phone onboards to Cisco Webex cloud successfully.

Phone has Meeting service enabled. For more information, see Add Meetings Softkey on Phone .

Step 1

Select Voice > Phone .

Step 2

In the Programmable Softkeys section, set the Programmable Softkey Enable to Yes .

Step 3

In the Connected Meeting Key List field, edit the field as described in the following example:

For psk, only DTMF is supported.

To control video layout, add the Layout softkey on the phone by adding the layout keyword in the Connected Meeting Key List field. You can add the keyword in the this format: leave|2;layout;selfviewoff|3;dnd;psk1

Step 4

Click Submit All Changes .

## Enable Conferencing

You can enable your user to talk to several people in a single call. When you enable this feature, your user dials several
                              people and add them to the call.

You can also configure the parameters in the phone configuration file with XML(cfg.xml) code.

### Before you begin

Access the phone administration web page. See Access the Phone Web Interface .

Step 1

Select Voice > Phone .

Step 2

Under Supplementary Services , choose Yes for the Conference Serv parameter.

You can configure this parameter in the phone configuration XML file (cfg.xml) by entering a string in this format:

```
<Conference_Serv ua="na">Yes</Conference_Serv>
```

Options: Yes and No

Default: Yes

Step 3

Click Submit All Changes .

## Manage Participant List for Ad Hoc Conference

During an Ad Hoc conference, you can show the participant list, add others into the conference. You can also remove a participant
                              if you are the host of this meeting.

### Before you begin

Access the phone administration web page. See Access the Phone Web Interface .

In the Call Feature Settings section, Conference Bridge URL has some valid URL and cannot be empty.

Step 1

Select Voice > Ext (n) where n is an extension number.

Step 2

In the Call Feature Settings section, select Yes from the Callinfo Subscribe list.

When you select Yes , the line will subscribe call-info event, and receive notify from the server for call status changes. This will make participant
                                          aware if the current call is in an Ad Hoc conference. Also, it allows to show the participants list.

If you select No , for shared lines, both the host and the participants can show participants list. But for private lines, only host can show
                                          the participants list.

You can configure this parameter in the phone configuration XML file (cfg.xml) by entering a string in this format:

```
<CallInfo_Subscribe_1_ ua="na">Yes</CallInfo_Subscribe_1_>
```

Default: No

Step 3

Click Submit All Changes .

## Enable Remote Call Recording with SIP REC

You can enable call recording on a phone so that your user can record an active call. The recording mode configured on the
                              server controls the display of the recording softkeys for each phone.

Recording Mode in Server

Recording Softkeys Available on the Phone

Always

No softkeys available.

Your user can't control recording from the phone. Recording starts automatically when a call is connected.

Never

PauseRec

ResumeRec

When a call is connected, recording starts automatically and your user can control the recording.

On Demand

Record

PauseRec

ResumeRec

When a call is connected, recording starts automatically but the recording is not saved until the user presses the Record softkey. Your user sees a message when recording state changes.

On Demand with User Initiated Start

Record

PauseRec

StopRec

ResumeRec

The recording only starts when your user presses the Record softkey. Your user sees a message when recording state changes.

During a recording, your user sees different icons which depend on the recording state. The icons are displayed on the Calls
                              screen and also on the line key on which the user is recording a call.

Icon

Meaning

Recording in progress.

Recording paused

Icon

Meaning

Recording in progress

Recording in progress (8811)

Recording paused

Recording paused (8811)

### Before you begin

Access the phone administration web page. See Access the Phone Web Interface .

Step 1

Select Voice > Phone .

Step 2

In the Supplementary Services section, click Yes or click No to enable or to disable the Call Recording Serv parameter.

You can configure this parameter in the phone configuration XML file (cfg.xml) by entering a string in this format:

```
<Call_Recording_Serv ua="na">Yes</Call_Recording_Serv>
```

Options: Yes and No

Default: No

Step 3

(Optional) In the Programmable Softkeys section, to enable softkeys, add a string in this format in the Connected Key List and Conferencing Key List fields.

crdstart;crdstop;crdpause;crdresume

Step 4

Click the Ext(n) tab that requires call recording.

Step 5

In the SIP Settings section, in the Call Recording Protocol , select SIPREC as the call recording protocol.

You can configure this parameter in the phone configuration XML file (cfg.xml) by entering a string in this format:

```
<Call_Recording_Protocol_3_ ua="na">SIPREC</Call_Recording_Protocol_3_>
```

Options: SIPREC and SIPINFO

Default: SIPREC

Step 6

Click Submit All Changes .

## Enable Remote Call Recording with SIP INFO

You can enable call recording on a phone so that your user can record an active call.

You can also configure the parameters in the phone configuration file with XML(cfg.xml) code.

During a recording, your user sees different icons which depend on the recording state. The icons are displayed on the Calls
                              screen and also on the line key on which the user is recording a call.

Your user presses the following softkeys to control the phone recording:

Record

StopRec

The recording only starts when your user presses the Record softkey. Your user sees a message when recording state changes and the recording icon displays on the call screen.

Once a phone recording starts, the StopRec softkey can work. The recording stops when your user presses the StopRec softkey. Your user sees a message when the recording state changes.

Icon

Meaning

Recording in progress.

Icon

Meaning

Recording in progress

Recording in progress (8811)

### Before you begin

You need to set up call recording on the call control system.

Access the phone administration web page. See Access the Phone Web Interface .

Step 1

Select Voice > Phone .

Step 2

In the Supplementary Services section, click Yes or click No to enable or to disable call recording in the Call Recording Serv parameter.

You can configure this parameter in the phone configuration XML file (cfg.xml) by entering a string in this format:

```
<Call_Recording_Serv ua="na">Yes</Call_Recording_Serv>
```

Options: Yes and No

Default: No

Step 3

(Optional) In the Programmable Softkeys section, to enable softkeys, add a string in this format in the Connected Key List and Conferencing Key List fields.

crdstart;crdstop;crdpause;crdresume

Step 4

Click the Ext(n) tab that requires call recording.

Step 5

In the SIP Settings section, for the Call Recording Protocol parameter, select SIPINFO as the call recording protocol.

You can configure this parameter in the phone configuration XML file (cfg.xml) by entering a string in this format:

```
<Call_Recording_Protocol_1_ ua="na">SIPINFO</Call_Recording_Protocol_1_>
```

Options: SIPREC and SIPINFO

Default: SIPREC

Step 6

Click Submit All Changes .

## Configure Missed Call Indication

You can configure a missed call alert on the phone handset LED.

You can also configure the parameters in the phone configuration file with XML(cfg.xml) code.

### Before you begin

Access the phone administration web page. See Access the Phone Web Interface .

Step 1

Select Voice > User .

The user can select User Login > Voice > User .

Step 2

In the Supplementary Services section, for the Handset LED Alert parameter, select Voicemail, Missed Call .

You can configure this parameter in the phone configuration XML file (cfg.xml) by entering a string in this format:

```
<Handset_LED_Alert ua="rw">Voicemail,Missed Call</Handset_LED_Alert>
```

Options: Voicemail and Voicemail, Missed Call

Default: Voicemail

Step 3

Click Submit All Changes .

## Enable Do Not Disturb

You can allow persons to turn the Do not disturb feature on or off. The caller receives a message that the person is unavailable.
                              A person can press the Ignore softkey on the phone to divert an incoming call to another destination.

If the feature is enabled for the phone, users can turn the feature on or off with the DND softkey.

You can also configure the parameters in the phone configuration file with XML(cfg.xml) code.

### Before you begin

Access the phone administration web page. See Access the Phone Web Interface .

Step 1

Select Voice > User .

Step 2

In the Supplementary Services area, for the DND Setting parameter, select Yes .

You can configure this parameter in the phone configuration XML file (cfg.xml) by entering a string in this format:

```
<DND_Setting ua="rw">Yes</DND_Setting>
```

Options: Yes and No

Default: No

Step 3

Click Submit All Changes .

When you select a line (multiline phone), a Do Not Disturb banner displays at the top of the phone screen.

### What to do next

Change another setting to ensure that multiline phones correctly display the Do not disturb (currently, a steady, green color)
                              status for each selected or unselected line. See DND and Call Forward Status Sync .

Users can enable or turn off the DND feature for each phone line if you configure star codes for DND. See Configure Star Codes for DND .

## Enable Synchronization of Settings Between the Phone and the Server

Enable the synchronization of settings between the phone and the server.

This setting must be enabled for the following features and types of users:

Call forward all

DND

Executives and assistants (Cisco IP Phone 6871 only)

You can also configure the parameters in the phone configuration file with XML(cfg.xml) code.

If a line key is configured with feature key sync and is also enabled with DND or call forward feature, the respective DND icon or the call forward icon is displayed next to the line key label. If the line key has a missed call, a voice message, or an urgent voicemail
                              alert, the DND icon or the call forward icon is also displayed with the alert notification.

### Before you begin

Access the phone administration web page. See Access the Phone Web Interface .

Step 1

Select Voice > Ext [n] (where [n] is the extension number).

Step 2

In the Call Feature Settings section, set the Feature Key Sync parameter to Yes .

You can configure this parameter in the phone configuration XML file (cfg.xml) by entering a string in this format:

Options: Yes and No

Default: No

Step 3

Click Submit All Changes .

## Enable Webex Contacts on the Phone

When you onboard a phone to Webex cloud successfully, you can enable the phone to support Webex contacts. When you enable
                              this feature on the phone, your user can see the Webex directory under the phone directory list.

When you configure Max Display Records parameter value more than 100, the query result displays only hundred contacts for a search in Webex directory and All directory.
                              When search result has count more than the allowed display record value, user see a message: Too many matches found.Refine your search . For more information on Max Display Records parameter, see Parameters for Directory Services .

### Before you begin

Phone onboards to Cisco Webex cloud successfully. For more information on phone onboarding to Webex Cloud, see Webex for Cisco BroadWorks Solution Guide .

Access the phone administration web page. See Access the Phone Web Interface .

Step 1

Select Voice > Phone .

Step 2

In the Webex section, set the Directory Enable to Yes .

You can configure this parameter in the phone configuration XML file (cfg.xml) by entering a string in this format:

```
<Webex_Directory_Enable ua="na”>Yes</Webex_Directory_Enable>
```

Default value: No

Step 3

In the Directory Name field, enter a name for the Webex directory.

You can configure this parameter in the phone configuration XML file (cfg.xml) by entering a string in this format:

```
<Webex_Directory_Name ua="na”>wcdir</Webex_Directory_Name>
```

Default value: Empty

The name you enter (for example, wcdir ), displays as the Webex directory name on the phone under the directory list. You can modify this name from the phone administration
                                          web page or from the configuration XML file string. When required, your user can also modify this name from the phone. When
                                          the Directory Name field is empty, by default, the Webex directory name on the phone appears as Webex directory .

When the phone is not onboarded to Cisco Webex cloud successfully, the Webex directory doesn't appear under the directory list.

Step 4

Click Submit All Changes .

## Configure Webex Contacts on a Line Key

You can configure Webex contacts on a line key. This line key becomes a shortcut to the Webex directory.

### Before you begin

Phone onboards to Cisco Webex cloud successfully.

Access the phone administration web page. See Access the Phone Web Interface .

Directory Enable on the phone administration web page is set to Yes.

Step 1

Select Voice > Phone .

Step 2

Select a line key.

Step 3

(Optional) Set the Extension parameter to Disabled to disable the extension.

If the Direct PLK Configuration feature is disabled, you must disable the extension to configure Webex contacts on the line
                                                      key. If the feature is enabled, you can skip this step. For details, see Enable Direct PLK Configuration .

```
<Extension_ n _ ua="na">Disabled</Extension_ n _>
```

where n is the extension number.

Step 4

In the Extended Function parameter, enter a string in this format:

fnc=shortcut;url=webexdir;nme=cloudplk

where fnc=shortcut means function=shortcut, url is the menu to open this line key, and nme is the name for the Webex directory.

In the string, when nme is empty or you don't include nme in the string, by default, the line key displays the directory name as Webex directory .

You can also configure this parameter in the configuration file (cfg.xml). Enter a string in this format:

where n is the extension number.

The line key is configured with the feature. For example, if you assign the feature in line key number nine, the user sees cloudplk appears in the line number nine as a shortcut to the Webex directory. By pressing this configured line key, user can access
                                          the Search Webex directory screen and can search the Webex contacts.

If Directory Enable on the phone administration web page is set to No , the line key doesn't work.

If the phone is not onboarded to the Webex cloud successfully, the line key doesn't work.

Step 5

Click Submit All Changes .

## Add a Softkey for Webex Contacts

You can configure Webex contacts to a softkey. This softkey becomes a shortcut to the Webex directory.

### Before you begin

Phone onboards to Cisco Webex cloud successfully.

Access the phone administration web page. See Access the Phone Web Interface .

Directory Enable on the phone administration web page is set to Yes.

Step 1

Select Voice > Phone .

Step 2

In the Programmable Softkeys section, set the Programmable Softkey Enable to Yes .

Step 3

Configure a PSK field from PSK 1 through PSK 16 with a string in this format:

You can also configure this parameter in the configuration file (cfg.xml). Enter a string in this format:

A softkey is configured with the feature and appears on the phone. For example, cloudplk appears as a softkey and acts as a shortcut to the Webex directory. By pressing this softkey, user can access the Search Webex directory screen and can search the Webex contacts.

In the string, when nme is empty or you don't include nme in the string, by default, the softkey displays the directory name as Webex Dir .

If Directory Enable on the phone administration web page is set to No , the softkey doesn't work.

If the phone is not onboarded to Cisco Webex cloud successfully, the softkey doesn't work.

## Enable Webex Call Logs on the Phone

You can now enable a phone to support Webex call logs. When you enable this feature, the Display recents from menu under the Recents screen includes the Webex option in the calls list. The user then can set the option Webex to see the list of recent Webex calls.

### Before you begin

Phone onboards to Webex cloud successfully. For more information on phone onboarding to Webex cloud, see Webex for Cisco BroadWorks Solution Guide .

Access the phone administration web page. See Access the Phone Web Interface .

Under the Call Log section, enable the CallLog Enable parameter and select a phone line from CallLog Associated Line for which you want to display the Webex recent call logs.

Step 1

Select Voice > Phone .

Step 2

In the Call Log section, set the CallLog Enable parameter to Yes and Display Recents From parameter to Webex .

You can configure this parameter in the phone configuration XML file (cfg.xml) by entering a string in this format:

```
<CallLog_Enable ua="na">Yes</CallLog_Enable>
```

```
<Display_Recents_From ua="na”>Webex</Display_Recents_From>
```

Default value of Display Recents From : Phone

Step 3

Click Submit All Changes .

On the phone, the user can view the duration of any received or placed Webex call log by selecting a call log under Recents > All calls . For a missed call, the call duration is not available.

## Configure Star Codes for DND

You can configure star codes that a user dials to turn on or off the do not disturb (DND) feature  on a phone.

You can also configure the parameters in the phone configuration file with XML(cfg.xml) code.

### Before you begin

Access the phone administration web page. See Access the Phone Web Interface .

Step 1

Select Voice > Regional .

Step 2

In the Vertical Service Activation Codes section, enter *78 for the DND Act Code parameter.

You can configure this parameter in the phone configuration XML file (cfg.xml) by entering a string in this format:

```
<DND_Act_Code ua="na">*78</DND_Act_Code>
```

Step 3

In the Vertical Service Activation Codes section, enter *79 for the DND Deact Code parameter.

You can configure this parameter in the phone configuration XML file (cfg.xml) by entering a string in this format:

```
<DND_Deact_Code ua="na">*79</DND_Deact_Code>
```

Step 4

Click Submit All Changes .

## Set Up a Call Center Agent Phone

You can enable a phone with Automatic Call Distribution (ACD) features. This phone acts as a call center agent's phone and
                              can be used to trace a customer call, to escalate any customer call to a supervisor in emergency, to categorize contact numbers
                              using disposition codes, and to view customer call details.

You can also configure the parameters in the phone configuration file with
                              XML(cfg.xml) code. To configure each parameter, see the syntax of the string in the Parameters for Call Center Agent Setup table.

### Before you begin

Set up the phone as a call center phone on the BroadSoft server.

Access the phone administration web page. See Access the Phone Web Interface .

Step 1

Select Voice > Ext(n) .

Step 2

In the ACD Settings section, set up the fields as
                                       described in Parameters for Call Center Agent Setup table.

Step 3

Click Submit All Changes .

### Parameters for Call Center Agent Setup

The following table defines the function and usage of  Call Center Agent Setup parameters in the ACD Settings section under
                                    the Ext(n) tab in the phone web interface. It also defines the syntax of the string that is added in the phone configuration
                                    file with XML(cfg.xml) code to configure a parameter.

Parameter

Description

Broadsoft ACD

Enables the phone for Automatic Call Distribution (ACD).

Perform one of the following:

In the phone configuration file with XML(cfg.xml), enter a string in this format:

In the phone web page, select Yes to enable this feature and select No to disable it.

Options: Yes and No

Default: No

Call Information Enable

Enables the phone to display details of a call center call.

Perform one of the following:

In the phone configuration file with XML(cfg.xml), enter a string in this format:

In the phone web page, select Yes to enable this feature. Select No to disable it.

Options: Yes and No

Default: Yes

Disposition Code Enable

Enables the user to add a disposition code.

Perform one of the following:

In the phone configuration file with XML(cfg.xml), enter a string in this format:

In the phone web page, select Yes to enable this feature. Select No to disable it.

Options: Yes and No

Default: Yes

Trace Enable

Enables the user to trace the last incoming call.

Perform one of the following:

In the phone configuration file with XML(cfg.xml), enter a string in this format:

In the phone web page, select Yes to enable this feature. Select No to disable it.

Options: Yes and No

Default: Yes

Emergency Escalation Enable

Enables the user to escalate a call to a supervisor in case of emergency.

Perform one of the following:

In the phone configuration file with XML(cfg.xml), enter a string in this format:

In the phone web page, select Yes to enable this feature. Select No to disable it.

Options: Yes and No

Default: Yes

Queue Status Notification Enable

Displays the call center status and the agent status.

Perform one of the following:

In the phone configuration file with XML(cfg.xml), enter a string in this format:

In the phone web page, select Yes to enable this feature. Select No to disable it.

Options: Yes and No

Default: Yes

Auto Available After Sign-In

Sets the agent status to Available automatically when the user signs into the phone as a call center agent.

Perform one of the following:

In the phone configuration file with XML(cfg.xml), enter a string in this format:

In the phone web page, select Yes to enable this feature and select No to disable it.

Options: Yes and No

Default: No

### Restore the ACD Status

You can enable the phone to automatically set the ACD status to the last local value in one of
                                 				the following situations:

Phone is powered on.

Phone status is changed to “Registered” from “Unregistered” or “Registration
                                       						failed” status.

Registration destination server IP address is changed when failover happens, a fallback
                                       						happens, or a DNS response is changed.

#### Before you begin

Set up the phone as a call center phone on the BroadSoft server.

Access the phone administration web page. See Access the Phone Web Interface .

Step 1

Select Voice > Ext(n) .

Step 2

In the ACD Settings section, set BraodSoft
                                             						ACD to Yes .

Step 3

From ACD Status field, select one of the options:

Sync From Local : Select this option to restore the
                                                							last local status as ACD status when the phone boots up, status is
                                                							changed to "Registered" from "Unregistered" or "Registration failed", or
                                                							registration destination ip address is changed due to failover, fallback
                                                							or DNS response is changed.

When the intial ACD status is configured to sync from local, and the last
                                                							local status is unavailable with a reason code, after the phone boots
                                                							up, the reason code will not be restored.

- Sync From Server : Select this option to get ACD intial status
                                             						from the server. This is the default value.

You can configure this parameter in the phone configuration XML file
                                             						(cfg.xml) by entering a string in this format:

```
<ACD_Status_n_ ua="na">Sync From Local</ACD_Status_n_>
```

where n = 1 to 16

Step 4

Click Submit All Changes .

### Display or Hide Unavailable Menu Text Box of Agent Status on the Phone

You can control if your user wants to hide the Unavailable menu text box of the Set agent status screen on the phone.

#### Before you begin

Set up the phone as a call center phone on the BroadSoft server.

Access the phone administration web page. See Access the Phone Web Interface .

Step 1

Select Voice > Ext(n) .

Step 2

In the ACD Settings section, set the Unavailable Reason Code Enable parameter to No to hide the Unavailable text box on the phone.

To display the text box, select Yes . This is the default value.

You can configure this parameter in the phone configuration XML file (cfg.xml) by entering a string in this format:

Step 3

Click Submit All Changes .

## Set Up a Phone for Presence

You can enable the BroadSoft XMPP directory for the phone user.

You can also configure the parameters in the phone configuration file with
                              XML(cfg.xml) code. To configure each parameter, see the syntax of the string in the Parameters for Set Up Presence table.

### Before you begin

Set up the BroadSoft server for XMPP.

Access the phone administration web page. See Access the Phone Web Interface .

Step 1

Select Voice > Phone .

Step 2

In the Broadsoft XMPP section, set the fields as
                                       described in the Parameters for Set Up Presence .

Step 3

Click Submit All Changes .

### Parameters for Set Up Presence

The following table defines the function and usage of Set Up Presence parameters in the Broadsoft XMPP section under the Phone
                                    tab in the phone web interface. It also defines the syntax of the string that is added in the phone configuration file with
                                    XML(cfg.xml) code to configure a parameter.

Parameter

Description

XMPP Enable

Enables the BroadSoft XMPP directory for the phone user.

Perform one of the following:

In the phone configuration file with XML(cfg.xml), enter a string in this format:

In the phone web page, select Yes to forward all calls. Select No to disable it.

Options: Yes and No

Default: No

Server

Name of the XMPP server; for example, xsi.iop1.broadworks.net.

Perform one of the following:

In the phone configuration file with XML(cfg.xml), enter a string in this format:

In the phone web page, enter a name for the server.

Default: Empty

Port

Server port for the XMPP server.

Perform one of the following:

In the phone configuration file with XML(cfg.xml), enter a string in this format:

In the phone web page, enter the server port.

Allowed values: An integer from 0 through 65535

If the value is set to 0, the phone first sends a DNS SRV query for the domain (specified in Server or User ID ) to obtain the XMPP server IP address. If there is no A record in the DNS SRV response, then the phone sends as fallback
                                             an A record lookup for the same domain to obtain the IP address. In this scenario, the actual port number is 5222.

When both Server and User ID contain the domain names, the domain name in Server is preferred.

If the value isn't set to 0, the phone directly sends an A record lookup for the domain (specified in Server or User ID ) to obtain the XMPP server IP address.

Default: 5222

User ID

BroadSoft User ID of the phone user; for example, username1@xdp.broadsoft.com or username1 .

Perform one of the following:

In the phone configuration file with XML(cfg.xml), enter a string in this format:

In the phone web page, enter the user ID.

If the value doesn't contain the domain name, the phone first generates a new user ID by combining the values of this parameter
                                             and Server . For example, the server is xsi.iop1.broadworks.net and user ID is username1 , the generated user ID is username1@xsi.iop1.broadworks.net .

Then, the phone sends A record lookup or DNS SRV query for the domain xsi.iop1.broadworks.net to obtain the XMPP server IP address.

Default: Empty

Password

Alphanumeric password associated with the User ID.

Perform one of the following:

In the phone configuration file with XML(cfg.xml), enter a string in this format:

In the phone web page, enter a supported password.

Default: Empty

Login Invisible

When enabled, the user's presence information is not published when the user signs in.

Perform one of the following:

In the phone configuration file with XML(cfg.xml), enter a string in this format:

In the phone web page, select Yes to enable the feature.

Options: Yes and No

Default: No

Retry Intvl

Interval, in seconds, to allow a reconnect without a log in after the client disconnects from the server. After this interval,
                                             the client needs to reauthenticate.

Perform one of the following:

In the phone configuration file with XML(cfg.xml), enter a string in this format:

In the phone web page, select Yes to enable the feature.

Options: Yes and No

Default: No

Display XMPP User ID With Top Priority

Displays the XMPP user ID with the highest priority at the top left of the phone screen. If enabled, the XMPP user ID overrides
                                             other display names, for example, Station Name.

This parameter takes effect only when the XMPP Enable is set to Yes .

Perform one of the following:

In the phone configuration file with XML(cfg.xml), enter a string in this format:

In the phone web page, select Yes to enable the feature.

Options: Yes and No

Default: No

### Use DNS SRV for XMPP

#### Before you begin

Set up the BroadSoft server for XMPP.

Access the phone administration web page. See Access the Phone Web Interface .

Step 1

Select Voice > Phone .

Step 2

In the Broadsoft XMPP section, set XMPP Enable to Yes .

Step 3

Set the field Port to 0 .

Step 4

Set the fields Server , User ID , and Password as described in the Parameters for Set Up Presence table.

Step 5

Click Submit All Changes .

### Display XMPP User ID on the Phone Screen

Before the release 11.3(4), the XMPP user ID always displays on the phone screen with top priority. However, in this release,
                                 the phone doesn't prioritize the displaying of the XMPP user ID by default. Therefore, if you don't change the setting, the
                                 XMPP user ID might not display on the phone screen.

#### Before you begin

Set up the BroadWorks server for the XMPP service.

Configure the IM&P service on the XSI BroadWorks server.

Access the phone administration web page. See Access the Phone Web Interface .

Step 1

Select Voice > Phone .

Step 2

In the Broadsoft XMPP section, set XMPP Enable to Yes .

Step 3

Set the fields Server , User ID , and Password as described in the Parameters for Set Up Presence table.

Step 4

Set Display XMPP User ID With Top Priority to Yes .

Step 5

Click Submit All Changes .

If you set Display XMPP User ID With Top Priority to No and configure either Station Name or Station Display Name , the XMPP icon and the configured name display at the top left of the phone screen. When you configure both names, the phone
                                 only displays the Station Display Name .

If you set Display XMPP User ID With Top Priority to No and both names are empty, the phone still displays the XMPP icon and the XMPP user ID.

If you set XMPP Enable to No or the XMPP configuration is incorrect, the XMPP user ID doesn't display on the phone screen.

## Configure the Number of Call Appearances Per Line

Phones that support multiple call appearances on a line can be configured to specify the number of calls to allow on the line.

You can restrict a line to allow only a single call at a time.

You can also configure the parameters in the phone configuration file with XML(cfg.xml) code.

### Before you begin

Access the phone administration web page. See Access the Phone Web Interface .

Step 1

Select Voice > Phone .

Step 2

In the Miscellaneous Line Key Settings section, for the Call Appearances Per Line parameter, specify the number of calls per line to allow.

```
<Call_Appearances_Per_Line ua="na">2</Call_Appearances_Per_Line>
```

The allowed values range from 1 to 10. The default value is 2. For allowing multiple calls on a line, select a value from
                                          2 to 10.

When the value is set to 1 and one extension is configured on the phone, then the user will not be able to:

- place a new call if there is an active call.

- transfer if there is an active call.

- conference an active call.

When the line has a shared line call, the user will not be able to make a new call, transfer a call, or make a conference.

Step 3

Click Submit All Changes .

## Enable Reverse Name Lookup

Reverse name lookup searches for the name of a number in an incoming, outgoing, conference, or transferred call. The reverse
                              name lookup acts when the phone cannot find a name using the service provider directory, Call History, or your contacts. Reverse
                              name lookup needs a valid BroadSoft (XSI) Directory, LDAP Directory, or XML Directory configuration.

The reverse name lookup searches the phone's external directories. When a search succeeds, the name is placed in the call
                              session and in the call history. For simultaneous, multiple phone calls, reverse name lookup searches for a name to match
                              the first call number. When the second call connects or is placed on hold, reverse name lookup searches for a name to match
                              the second call. The reverse lookup searches the external directories for 8 secs, if in 8secs there are no results found,
                              there will be no display of the name. If results are found in 8secs, the name is diplayed on the phone. The external directory
                              search priority order is : BroadSoft (XSI) > LDAP > XML .

While searching if the lower priority name is received before the higher priority name, the search shows the lower prioirty
                              name first and then replaced it with the higher priority name if the higher priority name is found within 8 secs.

The precedence of the phone list lookup in BroadSoft (XSI) Directory is:

Personal phone list

Group common phone list

Enterprise common phone list

Reverse name lookup is enabled by default.

Personal Address Book

SIP Header

Call History

BroadSoft (XSI) Directory

LDAP Directory

XML Directory

The phone searches the XML directory using this format: directory_url?n=incoming_call_number .

Example: For a multiplatform phone using a third-party service, the phone number (1234) search query has this format, http://your-service.com/dir.xml?n=1234 .

### Before you begin

Configure one of these directories before you can enable or disable the reverse name lookup:

BroadSoft (XSI) Directory

LDAP Corporate Directory

XML Directory

Access the phone administration web page. See Access the Phone Web Interface .

Step 1

Select Voice > Phone .

Step 2

In the Supplementary Services area, set the Reverse Phone Lookup Serv parameter to Yes to enable this feature.

```
<Reverse_Phone_Lookup_Serv ua="na">Yes</Reverse_Phone_Lookup_Serv>
```

The allowed values are Yes|No. The default value is Yes.

Step 3

Click Submit All Changes .

## Emergency Calls

### Emergency Call Support Background

Emergency call service providers can register a phone's location for each IP-based phone in a company. The location information
                              server (LIS) transfers the emergency response location (ERL) to the phone. The phone stores its location during registration,
                              after the phone restarts, and when a person signs in to the phone. The location entry can specify the street address, building
                              number, floor, room, and other office location information.

When you place an emergency call, the phone transfers the location to the call server. The call server forwards the call and
                              the location to the emergency call service provider. The emergency call service provider forwards the call and a unique call-back
                              number (ELIN) to the emergency services. The emergency service or public safety answering point (PSAP) receives the phone
                              location. The PSAP also receives a number to call you back, if the call disconnects.

See Emergency Call Support Terminology for the terms used to describe emergency calls from the phone.

You insert the following parameters to obtain the phone's location for any phone extension number:

Company Identifier–A Unique number (UUID) assigned to your company by the NG9-1-1 service provider.

Primary Request URL–The HTTPS address of the primary server used to obtain the phone location.

Secondary Request URL–The HTTPS address of a secondary server (backup) used to obtain the phone location.

Emergency Number–A sequence of digits that identify an emergency call. You can specify multiple emergency numbers, by separating
                                    each emergency number with a comma.

Common emergency service numbers include:

North America–911

European countries–112

Hong Kong–999

The phone requests new location information for the following activities:

You register the phone with the call server.

A person restarts the phone and the phone was previously registered with the call server.

A guest signs in to the phone.

You change the network interface used in the SIP registration. For example, change Wi-Fi to Ethernet.

You change the IP address of the phone.

If all of the location servers do not send a location response, the phone re-sends the location request every two minutes.

### Emergency Call Support Terminology

The following terms describe emergency call support for the Cisco Multiplatform Phones.

Emergency Location ID Number (ELIN)–A number used to represent one or more phone extensions that locate the person who dialed
                                       emergency services.

Emergency Response Location (ERL)–A logical location that groups a set of phone extensions.

HTTP Enabled Location Delivery (HELD)–An encrypted protocol that obtains the PIDF-LO location for a phone from a location
                                       information server (LIS).

Location Information Server (LIS)–A server that responds to a SIP-based phone HELD request and provides the phone location
                                       using a HELD XML response.

Emergency Call Service Provider–The company that responds to a phone HELD request with the phone's location. When you make
                                       an emergency call (which carries the phone's location), a call server routes the call to this company The emergency call service
                                       provider adds an ELIN and routes the call to the emergency services (PSAP). If the call is disconnected, the PSAP uses the
                                       ELIN to reconnect with the phone used to make the emergency call.

Public Safety Answering Point (PSAP)–Any emergency service (for example, fire, police, or ambulance) joined to the Emergency
                                       Services IP Network.

Universally Unique Identifier (UUID)–A 128-bit number used to uniquely identify a company using emergency call support.

### Configure a Phone to Make Emergency Calls

#### Before you begin

Obtain the E911 Geolocation Configuration URLs and the company identifier for the phone from your emergency call services
                                       provider. You can use the same Geolocation URLs and company identifier for multiple phone extensions in the same office area.

Access the phone administration web page. See Access the Phone Web Interface .

Step 1

Select Voice > Ext n , where n is the phone extension number (1-10) of the phone web dialog.

Step 2

In the Dial Plan section, set the Emergency Number parameter

Step 3

In the E911 Geolocation Configuration section, set the Company UUID , Primary Request URL , and Secondary Request URL parameters as described in the Parameters to Make an Emergency Call .

Step 4

Click Submit All Changes .

#### Parameters to Make an Emergency Call

The following table defines the function and usage of  Making of  Emergency Calls  parameters in the Dial Plan and E911 Geolocation
                                       Configuration sections under the Ext(n) tab in the phone web interface. It also defines the syntax of the string that is added
                                       in the phone configuration file with XML(cfg.xml) code to configure a parameter.

Parameter

Description

Section: Dial Plan

Emergency Number

Enter a comma-separated list of emergency numbers.

To specify multiple emergency numbers, separate each emergency number with a comma.

When one of these numbers is dialed, the unit disables processing of CONF, HOLD, and other similar softkeys or buttons to
                                                avoid accidentally putting the current call on hold. The phone also disables hook flash event handling.

Only the far end can terminate an emergency call. The phone is restored to normalcy after the call is terminated and the receiver
                                                is back on-hook.

Perform one of the following: to the digits that correspond to the customer emergency service numbers.

In the phone configuration file with XML(cfg.xml), enter a string in this format:

In the phone web page, set Emergency Number parameter to the digits that correspond to the customer emergency service numbers.

Valid Values: Maximum number length is 63 characters

Default: Blank (no emergency number)

Section: E911 Geolocation Configuration

Company UUID

The Universally Unique Identifier (UUID) assigned to the customer by the emergency call services provider.

For example:

07072db6-2dd5-4aa1-b2ff-6d588822dd46

Perform one of the following:

In the phone configuration file with XML(cfg.xml), enter a string in this format:

In the phone web page, enter a valid identifier assigned by the call services provider.

Valid Values: Maximum identifier length is 128 characters.

Default: Blank

Primary Request URL

Encrypted HTTPS phone location request. The request uses the phone IP addresses, MAC address, Network Access Identifier (NAI),
                                                and chassis ID and port ID assigned by the network switch manufacturer. The request also includes the location server name
                                                and the customer identifier.

The server used by the emergency call services provider responds with an Emergency Response Location (ERL) that has a location
                                                Uniform Resource Identifier (URI) tied to the user phone IP address.

Perform one of the following:

In the phone configuration file with XML(cfg.xml), enter a string in this format:

In the phone web page, enter encrypted HTTPS phone location request.

For example:

https://prod.blueearth.com/e911Locate/held/held_request.action

Default: Blank

Secondary Request URL

Encrypted HTTPS request sent to the emergency call services provider's backup server to obtain the user's phone location.

Perform one of the following:

In the phone configuration file with XML(cfg.xml), enter a string in this format:

In the phone web page, enter the encrypted  for the backup server that can return location information.

For example:

https://prod2.blueearth.com/e911Locate/held/held_request.action

Default: Blank

## PLK Configuration

### Programmable Line Keys

The Programmable Line Key (PLK) feature allows you to program feature buttons or services URL buttons on the line key buttons.
                              You can configure the line keys with:

Line buttons—see Enable the Extension of a Line Key

Speed dials—see Configure Speed Dial on a Line Key

Call Park—see Add Call Park to a Line Key

Busy Lamp Field (BLF)—see Phone Configuration for Monitoring Other Phones

Executive and Assistant—

Only the Cisco IP Phone 6871 Multiplatform Phones support the feature.

XML Services—see Add an XML Service to a Line Key

Voicemail—see Configure the Voicemail PLK on a Line Key

Webex Contacts—see Configure Webex Contacts on a Line Key

### Enable the Extension of a Line Key

You can use the buttons on both sides of the phone screen as line keys when you enable the extensions of the line keys.

```
<Extension_ n _ ua="rw">1</Extension_ n _>
```

where n is the extension number.

#### Before you begin

Access the phone administration web interface. See Access the Phone Web Interface .

Step 1

Select Voice > Phone .

Step 2

Choose a line key and assign an extension number in the Extension parameter to enable it.

When Extension is set to Disabled , the user can't use the line key as a telephony extension.

Step 3

Click Submit All Changes .

### Enable Direct PLK Configuration

#### Before you begin

Access the phone administration web page. See Access the Phone Web Interface .

Step 1

Select Voice > Phone .

Step 2

In the Miscellaneous Line Key Settings section, set the Enable Direct PLK Configuration parameter to Yes .

You can also configure the parameter in the phone configuration file (cfg.xml) with the following XML string:

```
<Enable_Direct_PLK_Configuration ua="na">Yes</Enable_Direct_PLK_Configuration>
```

Allowed values: Yes and No

Default value: Yes

If you set the parameter to No , the extension of a line key must be disabled for the PLK configuration.

Step 3

Select Voice > Ext [n] (where [n] is the extension number).

Step 4

In the Proxy and Registration section, ensure that the Proxy parameter is empty.

You can also configure this parameter in the configuration file (cfg.xml) by entering a string in this format:

```
<Proxy_ n _ ua="na"></Proxy_ n _>
```

where n is the extension number.

Step 5

In the Subscriber Information section, ensure that the User ID parameter is empty.

You can also configure this parameter in the configuration file (cfg.xml) by entering a string in this format:

```
<User_ID_ n _ ua="na"></User_ID_ n _>
```

where n is the extension number.

Step 6

Click Submit All Changes .

### Phone Configuration for Monitoring Other Phones

You can configure the phone to monitor the status of lines on other phones. This feature is useful if users routinely handle
                              calls for colleagues and need to see if they are available to answer calls. The phone monitors each line  on a separate line
                              key. The monitoring line keys function as Busy Lamp Field (BLF) keys. A BLF is an LED that changes color to indicate the status
                              of the monitored line:

LED Color

Meaning

Green

The monitored line is available.

Red

The monitored line is busy.

Blinking red

The monitored line is ringing.

Amber

Error in BLF key configuration.

If the phone is registered to a BroadSoft server, you can set up the phone to monitor multiple users, with a single set of
                              configurations.

### Add an XML Service to a Line Key

You can add an XML service to a line key to enable the user to access the XML application or directory.

#### Before you begin

Access the phone administration web page. See Access the Phone Web Interface .

Step 1

Select Voice > Phone .

Step 2

Select a line key.

Step 3

(Optional) Set the Extension parameter to Disabled to disable the extension.

If the Direct PLK Configuration feature is disabled, you must disable the extension to add an XML service to the line key.
                                                         If the feature is enabled, you can skip this step. For details, see Enable Direct PLK Configuration .

You can also configure this parameter in the phone configuration file (cfg.xml). The parameter is line-specific. Enter a string
                                             in this format:

```
<Extension_ n _ ua="na">Disabled</Extension_ n _>
```

where n is the extension number.

Step 4

In the Extended Function parameter, enter a string in this format:

```
fnc=xml;url=http://xml.service.url;nme=name
```

where:

fnc= prk means function=call park.

url= http://xml.service.url is the URL for the xml application or directory.

nme= XXXX is the name displayed on the phone for the xml service. Replace XXXX with a name.

```
<Extended_Function_2_ ua="na">fnc=xml;url=http://xml.service.url;nme=name</Extended_Function_2_>
```

Step 5

Click Submit All Changes .

## Programmable Softkeys Configuration

### Customize Display of the Softkeys

You can customize display of the softkeys on the phone screen during a specific state.

You can also configure the parameters in the phone configuration file with XML (cfg.xml) code. To configure each parameter,
                                 see the syntax of the string in Parameters for Programmable Softkeys .

#### Before you begin

Access the phone administration web page. See Access the Phone Web Interface .

Step 1

Select Voice > Phone .

Step 2

In the Programmable Softkeys section, edit the softkeys depending on the call state that you want the softkey to display. For more information, see Parameters for Programmable Softkeys and .

Step 3

Click Submit
                                             				All Changes .

#### Parameters for Programmable Softkeys

The following table defines the function and usage of the programmable softkeys parameters in the Programmable Softkeys section under the Voice > Phone tab in the phone web interface. It also defines the syntax of the string that is added in the phone configuration file (cfg.xml)
                                    with the XML code to configure a parameter.

Parameter

Description and default value

Programmable Softkey Enable

Enables or disables the programmable softkeys. Set this field to Yes to enable the programmable softkeys.

Perform one of the following:

```
<Programmable_Softkey_Enable ua="na">Yes</Programmable_Softkey_Enable>
```

In the phone web interface, set this field to Yes or No to enable or disable the programmable softkeys.

Allowed values: Yes | No

Default: No

PSK 1 through PSK 16

Programmable softkey fields. Enter a string in these fields to configure softkeys that display on the phone screen. You can
                                                create softkeys for speed dials to numbers or extensions, vertical service activation codes (* codes), or XML scripts.

Configure the PSKs in this format:

```
fnc=sd;ext=extension_number@$PROXY;vid=n;nme=display_name
```

```
fnc=sd;ext=star_code@$PROXY;vid=n;nme=display_name
```

See Vertical Service Activation Codes .

```
fnc=xml;url=http://server_IP/services.xml;vid=n;nme=display_name
```

```
fnc=shortcut;url=userpref;nme=User preferences
```

For more information, see Menu Shortcuts Mapping on PLK and PSK .

When you add a programmable softkey to a softkey list, such as Idle Key List, Missed Call Key List, and so on, the programmable
                                                softkey displays on the phone screen.

Perform one of the following:

```
<PSK_1 ua="na">fnc=xml;url=http://server_IP/services.xml;vid=n;
nme=display_name</PSK_1>
```

In the phone web interface, set the PSKs in the valid format.

Default: Empty

### Customize a
                           	 Programmable Softkey

The phone provides
                                 		  sixteen programmable softkeys (fields PSK1 through PSK16). You can define the
                                 		  fields by a speed-dial script.

#### Before you begin

Access the phone administration web page. See Access the Phone Web Interface .

Step 1

Select Voice > Phone .

Step 2

In the Programmable Softkeys section, set the Programmable Softkey Enable to Yes .

Step 3

Select a
                                          			 programmable softkey number field on which to configure a phone feature.

Step 4

Enter the
                                          			 string for the programmable soft key. See the different types of programmable
                                          			 softkeys described in Configure Speed Dial on a Programmable Softkey .

Step 5

Click Submit
                                             				All Changes .

### Configure Speed
                           	 Dial on a Programmable Softkey

You can configure programmable softkeys as speed dials. The speed dials can be extensions or phone numbers. You can also configure
                                 programmable softkeys with speed dials that perform an action that a vertical service activation code (or a star [*] code)
                                 defines. For example, if you configure a programmable softkey with a speed dial for *67, the call is placed on hold.

#### Before you begin

Access the phone administration web page. See Access the Phone Web Interface .

Step 1

Select Voice > Phone .

Step 2

In the Programmable Softkeys section, set the Programmable Softkey Enable to Yes .

Step 3

To configure a
                                          			 speed dial PSK, enter the following in the PSK number field:

fnc=sd;ext=extensionname/starcode@$PROXY;vid=n;nme=name

Where:

fnc=
                                                   					 function of the key (speed dial)

extensionname=extension being dialed or the star code action to
                                                   					 perform

vid= n
                                                   					 is the extension that the speed dial will dial out

name is
                                                   					 the name of the speed dial being configured

The name field displays on the softkey on the IP phone
                                                         				  screen. We recommend a maximum of 10 characters for a phone. If more characters
                                                         				  are used, the label might be truncated on the phone screen.

Step 4

Edit the
                                          			 following:

Idle Key List: Edit the field as described in the following example:

redial|1;newcall|2;dnd;psk1

If the user incorrectly configures the programmable softkey list features on the phone, the key list on the phone LCD does
                                                   not update. For example:

If a user enters rdeial;newcall;cfwd (redial has been misspelt), the key list is not updated and the user does not see any change on the LCD.

If a user enters redial;newcall;cfwd;delchar , the user will not see a change on the LCD, as the delchar softkey is not allowed in the Idle Key List . Hence, this is an incorrect configuration of the programmable softkey list.

PSK1:

In this
                                                         				  example, we are configuring a softkey on a phone as a speed dial number for
                                                         				  extension 5014 (sktest1).

You can also configure an XML service on the programmable softkey. Enter the string in this format:

<PSK_1 ua="na">fnc=xml;url=http://xml.service.url;nme=name</PSK_1>

Step 5

Click Submit
                                             				All Changes .

### Configure a PSK with DTMF Support

You can configure programmable softkeys (PSK) with dual tone multifrequency (DTMF). This configuration enables the phone to
                                 send digital pulses inband (or out-of-band via SIP INFO) to the server during an active call. When you enable a function on
                                 a PSK, the user sees the softkey name, and presses it to perform the named function. The applied actions to the DTMF digit
                                 string are similar to those applied to Speed Dial, such as the following:

Pause represented by ,

Wait represented by X

For example, ext=<DTMF_DIGITS>[[,|X][<DTMF_DIGITS>]] , where the valid DTMF digits are 0-9,*, #, a, b, c, d, and where the parts in [ ] brackets are optional.

This feature applies only to programmable softkeys. It doesn’t apply to the programmable line keys (PLK) on the desk phones.
                                 If you configure any PLK for this feature, the display will present the Circled X icon Ⓧ, and nothing will happen if you press
                                 the key.

This feature supports only Connected Key List and Connected Video Key List .

#### Before you begin

Access the Phone Web Interface .

Step 1

Select Voice > Phone > Programmable Softkeys .

Step 2

Set the Programmable Softkey Enable field to yes .

Step 3

From the PSK list (PSK#1 - PSK#16), select a PSK to configure.

Step 4

In the PSK(n) field, where n is a programmable softkey number, enter a string in this format:

```
fnc=dtmf;ext=<dtmf_digits_to_be_outpulsed>;nme=<softkey_display_name>;
vid=<extension_n_to_be_associated>
```

When a phone has more than one registered line, you must include the vid= that is asociated with the particular line/extension in order for the softkey to appear. Otherwise, the softkey will not
                                             display.

Step 5

(Optional) To configure the PSK softkey to toggle within a pair (outpulse-display) each time you press it, enter a string
                                          in this format:

```
fnc=dtmf;ext=<dtmf_digits_to_be_outpulsed>;nme=<softkey_display_name>;
ext2=<second_set_of_dtmf_digits_to_be_outpulsed>;nme2=<second_softkey_display_name_after_first_press>;
vid=<extension_n_to_be_associated>
```

The PSK softkey toggle always starts with the ext/nme for each new call.

Step 6

In the Connected Key List field or Connected Video Key List field, enter the configured PSK keywords according to where on the phone screen you wish the softkey name to appear.

For example, in the following entry, the hold softkey name appears in the first position. The softkey name that is listed in the psk1 field appears in the second position, and so on.

```
hold;psk1;endcall;xfer;conf;xferLx;confLx;bxfer;phold;redial;dir;park
```

Step 7

Select Voice > Ext(n) , where n is the extension number you wish to configure.

Step 8

In the Audio Configuration section, set the DTMF Tx Method to one of the following methods from the drop-down list.

InBand

AVT

INFO

Auto

InBand+INFO

AVT+INFO

Step 9

Click Submit All Changes .

Use these examples to help you understand how to configure PSK with DTMF Support options:

Example: PSK toggles when pressed.

Voice > Phone > Programmable Softkeys > Programmable Softkey Enable: Yes

Connected Key List: psk1|1 ;endcall|2;conf|3;xfer|4;

PSK 1: fnc=dtmf;ext=#1;nme=PressStart;ext2=*2;nme2=PressStop;vid=1

Voice > Ext 1 > DTMF Tx Method: Auto

Example: Phone sends DTMF digits inband via a PSK softkey.

Voice > Phone > Programmable Softkeys

Programmable Softkey Enable: yes .

Connected Key List: psk1|1;endcall|2;conf|3;xfer|4;

PSK 1: fnc=dtmf;ext=#1;nme=PressMe;vid=1

Voice > Ext 1 > DTMF Tx Method: Auto

Example: The PSK softkey pauses between digits.

Voice > Phone > Programmable Softkeys > Programmable Softkey Enable: Yes

Connected Key List: psk1|1;endcall|2;conf|3;xfer|4;

PSK 1: fnc=dtmf;ext=#1,1006;nme=PressMe;vid=1

Voice > Ext 1 > DTMF Tx Method: Auto

Example: The PSK softkey waits for the user's input between digits.

Voice > Phone > Programmable Softkeys > Programmable Softkey Enable: Yes

Connected Key List: psk1|1;endcall|2;conf|3;xfer|4;

PSK 1: fnc=dtmf;ext=#1X1006;nme=PressMe;vid=1

Voice > Ext 1 > DTMF Tx Method: Auto

### Enable Softkeys to Calls History List Menu

You can configure the Option , Call , Edit call , and Filter softkeys on the screen for All, Placed, Received, and Missed calls list. When you press the Recents softkey on the phone, you can directly access the All calls screen and see the list of all types of recents calls.

#### Before you begin

Access the phone administration web page. See Access the Phone Web Interface .

Step 1

Select Voice > Phone .

Step 2

Configure the XSI account information by providing values in the XSI Host Server , XSI Authentication Type , Login User ID , Login Password , and CallLog Associated Line parameters.

For more information about configuring XSI account, see Configure BroadSoft Settings .

Step 3

Set the CallLog Enable parameter to Yes .

Step 4

Set Display Recents From to Server .

Step 5

In the Programmable Softkeys section,

Set the Programmable Softkey Enable parameter to Yes.

In the Broadsoft Call History Key List field, the default string is: option|1;call|2;editcall|3; .

In the Broadsoft Call History Key List field, the default string is: option|1;call|2;editcall|3;back|4;

Supported strings are option, call, editcall, filter, and back. This parameter doesn't support psk string.

Availability of all these softkeys under the All, Placed, Received, and Missed calls list or the Option menu in these calls list depends on the following conditions:

Programmable Softkey Enable = Yes and Broadsoft Call History Key List = option|1;call|2;editcall|3;back|4; － Option , Call , Edit call , Back softkeys appear on the All, Placed, Received, and Missed calls list. Filter appears in the Option menu of calls list.

Programmable Softkey Enable = Yes and Broadsoft Call History Key List = option|1;call|2;editcall|3;back|4; － Option , Call , Edit call , softkeys appear on the All, Placed, Received, and Missed calls list. Back softkey doesn't appear. Filter appears in the Option menu of calls list.

Programmable Softkey Enable = Yes and Broadsoft Call History Key List = option|1;call|2;back|4; － Option , Call , Back softkeys appear on the All, Placed, Received, and Missed calls list. Edit call and Filter appears in the Option menu of calls list.

Programmable Softkey Enable = Yes and Broadsoft Call History Key List = option|1;call|2;editcall|3;filter|4; － Option , Call , Edit call , Filter softkeys appear on the All, Placed, Received, and Missed calls list.

Programmable Softkey Enable = Yes , PSK 1 = fnc=shortcut;url=missedcalls , and Broadsoft Call History Key List = option|1;call|2;psk1|3;filter222|4; －only Option and Call softkeys appear on the All, Placed, Received, and Missed calls list because strings psk and filter222 are invalid values. Edit call and Filter appears in the Option menu of calls list.

Programmable Softkey Enable = Yes , and Broadsoft Call History Key List = blank －The softkeys appears as default setting option|1;call|2;editcall|3 . Option , Call , Edit call softkeys appear on the All, Placed, Received, and Missed calls list. Filter appears in the Option menu of calls list.

In the phone configuration file with XML(cfg.xml), enter a string in this format:

```
<Broadsoft_Call_History_Key_List ua="na">option|1;call|2;editcall|3</Broadsoft_Call_History_Key_List>
```

Step 6

Click Submit All Changes .

### Enable Sign In softkey for Hot Desking (8800 only)

You can configure a Sign in softkey for hot desking and it appears on the phone home screen.

#### Before you begin

The workspace where the phone resides has the Scheduling mode set to Hot Desking.

Access the phone administration web page. See Access the Phone Web Interface .

Phone onboards to Cisco Webex cloud successfully.

Step 1

Select Voice > Phone .

Step 2

In the Programmable Softkeys section, set the Programmable Softkey Enable to Yes .

Step 3

In the Idle Key List and Missed Call Key List fields, add the value hdsignin and edit the field as described in the following example:

Step 4

Click Submit All Changes .

#### Set the Time Format for Booking a Desk for a Specific Duration (8800 only)

You can set the time format (in hours) which your user uses to enter a time to reserve an available desk.

##### Before you begin

Your administrator has enabled Sign in softkey on the phone.

Phone onboards to Cisco Webex cloud successfully.

Access the phone administration web page. See Access the Phone Web Interface .

Step 1

Select Voice > User .

Step 2

In Time Format parameter, set the format to 12hr or 24hr.

You can also enable the parameters in the phone configuration file (cfg.xml).

```
<Time_Format ua="na">12hr</Time_Format>
```

Default: 12 hr

Step 3

Click Submit All Changes .

### Spam Indication for Incoming Calls

New technology standard Secure Telephony Identity Revisited (STIR) and Signature-based Handling of Asserted information using
                                 toKENs (SHAKEN). These standards define procedures to authenticate and verify caller identification for calls carried over
                                 the IP network. The STIR-SHAKEN framework is developed to provide the end user with a great degree of identification and control
                                 over the type of calls they receive. These sets of standards are intended to provide a basis for verifying calls, classifying
                                 calls, and facilitating the ability to trust caller identity end to end. Illegitimate callers can easily be identified.

When STIR/SHAKEN support is implemented on the server, the phone displays an extra icon next to the caller ID based on the
                                 caller's STIR/SHAKEN verification result. Based on the verification result, the phone displays three types of icons. This
                                 helps reduce wasted time from answering calls from robocallers, and the security risk from callers with spoofed or tampered
                                 Caller ID.

Validated call－When the caller carries verstat=TN-Validation-Passed in the SIP Header PAID or FROM, an extra icon next to the caller id is displayed on the phone with a color screen indicating a validated caller. For a phone with grayscale
                                                   screen, an extra icon next to the caller id is displayed.

Spam call－When the caller carries verstat=TN-Validation-Failed in the SIP Header PAID or FROM, an extra icon next to the caller id is displayed on the phone indicating an illegitimate caller.

Unverified call－When the caller carries verstat=NO-TN-Validation in the SIP Header PAID or FROM, an extra icon next to the caller id is displayed on the phone indicating an unverified call.

For detailed spam notifications for calls in Webex environment, see Spam Indication for Incoming Webex Calls .

### Add Participants Softkey on the Phone

You can add Participants softkey on the phone. By pressing this softkey the host or the participants can show the list of participants that has joined
                                 an Ad Hoc conference.

For an Ad Hoc conference host, the Participants softkey is always available on the phone when the phone subscribes the Call-Info and receives the list from NOTIFY sent by
                                 the server. When Programmable Softkey Enable is enabled or disabled this softkey is always available for the host.

#### Before you begin

Access the phone administration web page. See Access the Phone Web Interface .

Step 1

Select Voice > Phone .

Step 2

In the Programmable Softkeys section:

Set the Programmable Softkey Enable parameter to Yes .

In the Connected Key List field, add the adhocparticipants keyword in the string.

In the Hold Key List field, add the adhocparticipants keyword in the string.

The Participants softkey shows up during an Ad Hoc conference call.

If you set the Programmable Softkey Enable parameter to No , for a participant, the Participants softkey is always available when the list is received from the server.

Step 3

Click Submit All Changes .

### Add Participants Softkey on Phone (8800 only)

You can add Participants softkey on the phone. By pressing this softkey the user can view participant list and their status of a hybrid meeting.

#### Before you begin

Access the phone administration web page. See Access the Phone Web Interface .

In the Webex section, Calender Enable must be set to Yes . Also this parameter must be set to Yes in the phone configuration .XML file.

Step 1

Select Voice > Phone .

Step 2

In the Programmable Softkeys section:

Set the Programmable Softkey Enable parameter to Yes .

In the Connected Meeting Key List field, add the participants keyword in the string.

The Participants softkey shows up during a hybrid meeting.

If the Programmable Softkey Enable parameter is No , the Participants softkey is displayed by default.

Step 3

Click Submit All Changes .

### Add Mute and Unmute Softkey on Phone (8800 only)

You can add Mute and Unmute softkeys on the phone. By pressing the softkeys the  participants can mute or unmute them by using either a softkey, a hardkey,
                                 or a headset button. Mute or unmute status also synchronizes with the server.

#### Before you begin

Access the phone administration web page. See Access the Phone Web Interface .

In the Webex section, Calender Enable must be set to Yes . Also this parameter must be set to Yes in the phone configuration .XML file.

Step 1

Select Voice > Phone .

Step 2

In the Programmable Softkeys section:

Set the Programmable Softkey Enable parameter to Yes .

In the Connected Meeting Key List field, add the audiomute keyword in the string.

The Mute or Unmute softkey shows up during a hybrid meeting.

If the Programmable Softkey Enable parameter is No , the Mute or the Unmute softkey is displayed by default.

Step 3

Click Submit All Changes .

### Add Start Video Softkey on Phone

You can add Start video or Stop video softkeys on the phone. By pressing the softkeys the participants can mute or unmute their video. Mute or unmute status also
                                 synchronizes with the server.

#### Before you begin

Access the phone administration web page. See Access the Phone Web Interface .

Step 1

Select Voice > Phone .

Step 2

In the Programmable Softkeys section:

Set the Programmable Softkey Enable parameter to Yes .

In the Connected Meeting Key List field, add the videounmute keyword in the string.

The Start video or Stop video softkey shows up during a hybrid meeting.

If the Programmable Softkey Enable parameter is No , the Start video or Stop video softkeys are displayed by default.

Step 3

Click Submit All Changes .

### Spam Indication for Incoming Webex Calls

To support a spam indication for the incoming calls in Webex environment, server sends the X-Cisco-CallerId-Disposition disposition information to the phone. The phone translates this information as authentication icons. Based on the caller's
                                 STIR/SHAKEN verification result, the phone displays three types of icons. The icons are displayed next to the caller ID for
                                 call session, local call logs, Webex cloud call logs.

Validated call－The server sends the disposition information, X-Cisco-CallerId-Disposition=valid , to the phone. The phone displays an extra icon next to the caller ID with a color screen indicating a validated caller. For a phone with grayscale screen, an extra icon next to the caller ID is displayed.

Invalidated or Spam call－The server sends the disposition information, X-Cisco-CallerId-Disposition=invalid , to the phone. The phone displays an extra icon next to the caller id indicating an illegitimate caller.

Unverified call－The server sends the disposition information, X-Cisco-CallerId-Disposition=unverified , to the phone. The phone displays an extra icon next to the caller id indicating an unverified call.

When there is no disposition information, the phone displays the same icons as before.

### Programmable Softkeys

Keyword

Key Label

Definition

Available Phone Status

acd_login

Agt signin

Logs user in to Automatic Call Distribution (ACD).

Idle

acd_logout

AgtSignOut

Logs user out of ACD.

Idle

answer

Answer

Answers an incoming call.

Ringing

astate

Agt Status

Checks the ACD status.

Idle

avail

Avail

Denotes that a user who is logged in to an ACD server has set his status as available.

Idle

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

Performs a blind call transfer (transfers a call without speaking to the party to whom the call is transferred). Requires
                                             that Blind Xfer Serv is enabled.

Connected

Connected Video

call (or dial)

Call

Calls the selected item in a list.

Dialing Input

call info

Call Info

Show call information

Progressing

calllist

Call list

Provides access to the call list while on a connected video call.

Connected, Connected Video

cancel

Cancel

Cancels a call (for example, when conferencing a call and the second party is not answering.

Off-Hook

cfwd

Forward / Clr fwd

Forwards all calls to a specified number.

Idle, Off-Hook, Shared-Active, Hold, Shared-Held

crdpause

PauseRec

Pause recording

Connected, Conferencing

crdresume

ResumeRec

Resume recording

Connected, Conferencing

crdstart

Record

Start a recording

Connected, Conferencing

crdstop

StopRec

Stop recording

Connected, Conferencing

conf

Conference

Initiates a conference call. Requires that Conf Server is enabled and there are two or more calls that are active or on hold.

Connected

Connected Video

confLx

Conf line

Conferences active lines on the phone. Requires that Conf Serv is enabled and there are two or more calls that are active
                                             or on hold.

Connected

Connected Video

delchar

delChar - backspace Icon

Deletes a character when entering text.

Dialing Input

dir

Dir

Provides access to phone directories.

Idle, Miss, Off-Hook (no input), Connected, Start-Xfer, Start-Conf, Conferencing, Hold, Ringing, Shared-Active, Shared-Held

disp_code

DispCode

Enter Disposition Code

Idle, Connected, Conferencing, Hold

dnd

DND / Clr Dnd

Sets Do Not Disturb to prevent calls from ringing the phone.

Idle, Off-Hook, Hold, Shared-Active, Shared-Held, Conferencing, Start-Conf, Start-Xfer, Connected video

emergency

Emergency

Enter emergency number

Connected

em_login (or signin)

Sign in

Logs user in to Extension Mobility.

Idle

em_logout (or signout)

Sign out

Logs user out of Extension Mobility.

Idle

endcall

End call

Ends a call.

Connected, Off-hook, Progressing, Start-Xfer, Start-Conf, Conferencing, Releasing, Hold, and Connected Video

favorites

Favorites

Provides access to "Speed Dials".

Idle, Miss, Off-Hook (no input), Connected, Start-Xfer, Start-Conf, Conferencing, Hold, Ringing, Shared-Active, Shared-Held

Connected Video

gpickup

GrPickup

Allows user to answer a call ringing on an extension by discovering the number of the ringing extension.

Idle, Off-Hook

hold

Hold

Put a call on Hold.

Connected, Start-Xfer, Start-Conf, Conferencing, Connected Video

ignore

Decline

Ignores an incoming call.

Ringing

ignoresilent

Ignore

Silences an incoming call

Ringing

join

Join

Connects a conference call. If the conference host is user A and users B & C are participants, when A presses "Join", A will
                                             drop off and users B & C will be connected.

Conferencing

lcr

Call Rtn/lcr

Returns the last missed call.

Idle, Missed-Call,Off-Hook (no input)

left

Left arrow icon

Moves the cursor to the left.

Dialing Input

messages

Messages

Provides access to voicemail.

Idle, Miss, Off-Hook (no input), Connected, Start-Xfer, Start-Conf, Conferencing, Hold, Ringing, Shared-Active, Shared-Held

Connected Video

miss

Miss

Displays the list of missed calls.

Missed-Call

newcall

New Call

Begins a new call.

Idle, Hold, Shared-Active, Shared-Held

option

Option

Opens a menu of input options.

Off-Hook

park

Park

Puts a call on hold at a designated "park" number.

Connected

Connected Video

phold

PrivHold

Puts a call on hold on an active shared line.

Connected

Connected Video

pickup

PickUp

Allows a user to answer a call ringing on another extension by entering the extension number.

Idle, Off-Hook

pip

PIP icon

Allows user to move PIP to one of the four corners of the screen or turn PIP off.

Connected Video

recents

Recents

Displays the All calls list from call history.

Idle, Off-Hook, Shared-Active, Shared-Held

redial

Redial

Displays the redial list.

Idle, Connected, Start-Conf, Start-Xfer, Off-Hook (no input), Hold

Connected Video

resume

Resume

Resumes a call that is on hold.

Hold, Shared-Held

right

Right arrow icon

Moves the cursor to the right.

Dialing (input)

settings

Settings

Provides access to "Information and Settings".

All

showvideo

Show video

Provides access to the video session while on a connected video call and the call list is in view

Connected

starcode

Input Star Code/*code

Displays a list of star codes that can be selected.

Off-Hook, Dialing (input)

swap

Swap

Allows user to swap the remote video stream and selfview during an active video call.

Connected Video

trace

Trace

Trigger trace

Idle, Connected, Conferencing, Hold

unavail

Unavail

Denotes that a user who is logged in to an ACD server has set his status as unavailable.

Idle

unpark

Unpark

Resumes a parked call.

Idle, Off-Hook, Connected, Shared-Active

Connected Video

xfer

Transfer

Performs a call transfer. Requires that Attn Xfer Serv is enabled and there is at least one connected call and one idle call.

Connected, Start-Xfer, Start-Conf

xferlx

Xfer line

Transfers an active line on the phone to a called number. Requires that Attn Xfer Serv is enabled and there are two or more
                                             calls that are active or on hold.

Connected

Connected Video

#### Programmable Softkeys for Executives and Assistants

Only the Cisco IP Phone 6871 Multiplatform Phones support the executive and assistant  programmable softkeys.

Keyword

Key Label

Definition

Available Phone Status

bridgein

Bridge in

Only available to executives who have assistants. Joins the user (executive) to an ongoing call with an assistant.

Idle, Shared-Active

callpush

Call push

Only available to executive assistants. Transfers an ongoing call from the user (assistant) to the executive.

Hold , Shared-Active

callretrieve

Retrieve

Only available to executives who have assistants. Transfers an ongoing call from the assistant to the user (executive).

Idle, Shared-Active

divert

Clr divert

Only available to executive assistants. Deactivates call diversion for the user (assistant).

Available only when call diversion is active and you navigate to the menu Settings > Assistant .

It is also available when you press the line key that is configured as Assistant .

divert

Divert

Only available to executive assistants. Activates call diversion for the user (assistant). All incoming calls to the user,
                                             for executives that the user handles, are diverted to the specified destination.

Available when you navigate the menu Settings > Assistant .

It is also available when you press the line key that is configured as Assistant .

proxycall

Proxy call

Only available to executive assistants. Initiates a call on behalf of the selected executive.

Available when you navigate the menu Settings > Assistant .

It is also available when you press the line key that is configured as Assistant .

## Enable Inline Call Label or Session (8800  only)

You can enable inline call label feature to automatically minimize the active call window and view the call session information,
                              such as caller or the callee name, number, call duration, call state, and any special icons like secure call, call recording,
                              etc. in the line label itself. This lets you to view status of various other lines, BLF/SD features, along with the current
                              call information.

### Before you begin

Access the phone administration web page. See Access the Phone Web Interface .

Step 1

Select Voice > User .

Step 2

Select Yes for the parameter Auto Collapse Into Line Key .

To disable the feature, select No .

You can also configure this parameter in the phone configuration XML file (cfg.xml) by entering a string in this format:

```
<Auto_Collapse_Into_Line_Key ua="rw">Yes</Auto_Collapse_Into_Line_Key>
```

Default: No .

If the Auto Collapse Into Line Key feature is enabled, the call info screen will be closed once the call is answered.

Step 3

Click Submit All Changes .

## Add Call Park on a Specific Line Key

You can add call park functionality on a specific line key to use only a single button to park or unpark a call.

### Before you begin

Access the phone administration web page. See Access the Phone Web Interface .

Step 1

Select Voice > Att Console > General .

Step 2

Select Yes for the parameter BLF Callpark On Line Key Enable .

To disable the feature, select No .

You can also configure this parameter in the phone configuration XML file (cfg.xml) by entering a string in this format:

```
<BLF_Callpark_On_Line_Key_Enable ua=”na“>Yes</BLF_Callpark_On_Line_Key_Enable>
```

Default: No .

Step 3

Navigate to Voice > Phone and select a line key.

Step 4

(Optional) To disable the extension, set the Extension parameter to Disabled .

You must disable the extension to add an extended function to the line key, if the Direct PLK Configuration feature is disabled.
                                                      For more information, see Enable Direct PLK Configuration section in the Administration Guide .

Step 5

Enter the string in the following format in the Extended Function field:

```
fnc=prk;sub=BLF_List_URI@$PROXY;usr=user_ID@$PROXY
```

Where,

sub— the URI to which the SUBSCRIBE message is sent. This name must be identical to the name defined in the BLF List URI.

usr— the call park extension that the BLF monitors.

Step 6

Click Submit All Changes .

| Step 1 | Select Voice > Phone . |
|---|---|
| Step 2 | Under Supplementary
                                          Services , configure the parameters as defined in the Parameters for Enable Call Transfer table. |
| Step 3 | Click Submit All Changes . |

| Parameter | Description |
|---|---|
| Attn Transfer Serv | Attended call transfer service. The user answers the call before transferring it. Perform one of the following: In the phone configuration file with XML(cfg.xml), enter a string in this format: <Attn_Transfer_Serv ua="na">Yes</Attn_Transfer_Serv> In the phone web page, select Yes to enable the transfer service. Select No to disable it. Options: Yes and No Default: Yes |
| Blind Transfer Serv | Blind call transfer service. The user transfers the call without speaking to the caller. Perform one of the following: In the phone configuration file with XML(cfg.xml), enter a string in this format: <Blind_Transfer_Serv ua="na">Yes</Blind_Transfer_Serv> In the phone web page, select Yes to enable the transfer service. Select No to disable it. Options: Yes and No Default: Yes |

| Step 1 | Select Voice > Phone . |
|---|---|
| Step 2 | Under Supplementary Services , configure the parameters as described in the Parameters for Enable Call Forward on Voice Tab table. |
| Step 3 | Click Submit All Changes . |

| Parameter | Description |
|---|---|
| Cfwd All Serv | Forwards all calls. Perform one of the following: In the phone configuration file with XML(cfg.xml), enter a string in this format: <Cfwd_All_Serv ua="na">Yes</Cfwd_All_Serv> In the phone web page, select Yes to forward all calls. Select No to disable it. Options: Yes and No Default: Yes |
| Cfwd Busy Serv | Forwards calls only if the line is busy. Perform one of the following: In the phone configuration file with XML(cfg.xml), enter a string in this format: <Cfwd_Busy_Serv ua="na">Yes</Cfwd_Busy_Serv> In the phone web page, select Yes to forward calls when the line is busy. Select No to disable it. Options: Yes and No Default: Yes |
| Cfwd No Ans Serv | Forwards calls only if the line is not answered. Perform one of the following: In the phone configuration file with XML(cfg.xml), enter a string in this format: <Cfwd_No_Ans_Serv ua="na">Yes</Cfwd_No_Ans_Serv> In the phone web page, select Yes to forward calls if the line is not answered. Select No to disable it. Options: Yes and No Default: Yes |

| Step 1 | Select Voice > User . |
|---|---|
| Step 2 | In the Call Forward section, configure the parameters as described in the Parameters for Enable Call Forward on User Tab table. |
| Step 3 | Click Submit All Changes . |

| Parameter | Description |
|---|---|
| Cfwd All | Forwards all calls. The setting of this parameter takes precedence over Cfwd Busy and Cfwd No Answer. Perform one of the following: In the phone configuration file with XML(cfg.xml), enter a string in this format: <Cfwd_All ua="rw">No</Cfwd_All> In the phone web page, select Yes to forward all calls. Select No to disable it. Options: Yes and No Default: No |
| Cfwd All Dest | Specifies the destination to which all calls are forwarded. The destination can be an alphanumeric input, a phone number,
                                                or a SIP URI. Perform one of the following: In the phone configuration file with XML(cfg.xml), enter a string in this format: <Cfwd_All_Dest ua="rw"> DestinationNumber </Cfwd_All_Dest> In the phone web page, enter the destination number in the field. When you select Yes for Cfwd All, make sure to configure the parameter. Default: Empty |
| Cfwd Busy | Forwards calls only if the line is busy. Perform one of the following: In the phone configuration file with XML(cfg.xml), enter a string in this format: <Cfwd_Busy ua="rw">No</Cfwd_Busy> In the phone web page, select Yes to forward calls when the line is busy. Select No to disable it. Options: Yes and No Default: No |
| Cfwd Busy Dest | Specifies the destination to which calls are forwarded if the line is busy. The destination can be an alphanumeric input,
                                                a phone number, or a SIP URI. Perform one of the following: In the phone configuration file with XML(cfg.xml), enter a string in this format: <Cfwd_Busy_Dest ua="rw"> DestinationNumber </Cfwd_Busy_Dest> In the phone web page, enter the destination number in the field. When you select Yes for Cfwd Busy, make sure to configure the parameter. Default: Empty |
| Cfwd No Answer | Forwards the incoming call only if the call isn’t answered. Perform one of the following: In the phone configuration file with XML(cfg.xml), enter a string in this format: <Cfwd_No_Answer ua="rw">No</Cfwd_No_Answer> In the phone web page, select Yes to forward the incoming call if the call isn't answered. Select No to disable it. Options: Yes and No Default: No |
| Cfwd No Ans Dest | Specifies the phone number of destination to which the incoming call is forwarded if the call isn’t answered. The destination
                                                can be an alphanumeric input, a phone number, or a SIP URI. Perform one of the following: In the phone configuration file with XML(cfg.xml), enter a string in this format: <Cfwd_No_Answer_Dest ua="rw"> DestinationNumber </Cfwd_No_Answer_Dest> In the phone web page, enter the destination number in the field. When you select Yes for Cfwd No Answer, make sure to configure the parameter. Default: Empty |
| Cfwd No Ans Delay | Assigns a response delay time (in seconds) for the no answer scenario. Perform one of the following: In the phone configuration file with XML(cfg.xml), enter a string in this format: <Cfwd_No_Answer_Delay ua="rw">20</Cfwd_No_Answer_Delay> In the phone web page, enter the delay time in the field. Default: 20 |
| Forward Softkey | Controls the scope of the call forward services that the user can set up by a dedicated softkey. Options are: All Cfwds : Allows the user to set up all call forward services, including Call Forward All, Call Forward Busy, and Call Forward No
                                                      Answer by pressing the Forward softkey. In this setting, the softkey name is Forward for activation and Clr fwd for deactivation. Only the Cfwd All : Allows the user to directly set up the Call Forward All service by pressing the softkey Forward all . The user can still set up all call forward services from the Settings > User preferences > Call preferences > Call forwarding > Call forward settings screen. In this setting, the softkey name is Forward all for activation and Clr fwd all for deactivation. Perform one of the following: In the phone configuration file with XML(cfg.xml), enter a string in this format: <Forward_Softkey ua="na">All Cfwds</Forward_Softkey> In the phone web page, select the value that determines the scope of the call forward services for the users. Note The parameter takes effect even though FKS, XSI, or FAC is enabled. Default: All Cfwds | Note | The parameter takes effect even though FKS, XSI, or FAC is enabled. |
| Note | The parameter takes effect even though FKS, XSI, or FAC is enabled. |

| Note | The parameter takes effect even though FKS, XSI, or FAC is enabled. |
|---|---|

| Step 1 | Select Voice > Ext (n) . |
|---|---|
| Step 2 | In the Feature Activation Code Sync field, select Yes to enable the feature. After you enable this feature, your user can press the Forward or Forward all softkey on the phone and enter the destination contact number. When the user presses the Call softkey, a voice message plays to confirm the call forward setting status. After successful configuration, a call forward icon displays at the top of the phone screen. The softkey name is different based on the value of the parameter Forward Softkey , see Parameters for Enable Call Forward on User Tab . In the phone configuration file with XML(cfg.xml), enter a string in this format: <Feature_Activation_Code_Sync_n_ ua="na">Yes</Feature_Activation_Code_Sync_n_> where, n is the extension number. Default value: No Allowed values: Yes or No |
| Step 3 | Click Submit All Changes . |

| Step 1 | Select Voice > Regional . |
|---|---|
| Step 2 | In the Vertical Service Activation Codes section, ensure that the Cfwd All Act Code field is set to the value defined by the server. The default value is *72. In the phone configuration file with XML(cfg.xml), enter a string in this format: <Cfwd_All_Act_Code ua="na">*72</Cfwd_All_Act_Code> |
| Step 3 | In the Vertical Service Activation Codes section, ensure that the Cfwd All Deact Code field is set to the value defined by the server. The default value is *73. In the phone configuration file with XML(cfg.xml), enter a string in this format: <Cfwd_All_Deact_Code ua="na">*73</Cfwd_All_Deact_Code> |
| Step 4 | Click Submit All Changes . Your user can dial *72 in combination with the destination number and press the Call softkey to activate the call forward all service. Your user can dial *73 and press the Call softkey to deactivate the call forward all service. |

| Note | In Firmware release 11.3(7), user can join meeting only with SIP URL. OBTJ with user account is supported but workspace account
                                          is not supported. |
|---|---|

| Step 1 | Select Voice > Phone . |
|---|---|
| Step 2 | In the Programmable Softkeys section, set the Programmable Softkey Enable to Yes . |
| Step 3 | In the Idle Key List and Missed Call Key List field, enter meetings in the key list. Edit the field as described in the following example: meetings\|;redial\|1;newcall\|2;dnd;psk1 Meetings softkey gets added to the phone screen. When Idle Key List field doesn't have meetings keyword in the field, the softkey doesn't appear. |
| Step 4 | Click Submit All Changes . |

| Step 1 | Select Voice > Phone . |
|---|---|
| Step 2 | In the Webex section, set up Calender Enable to Yes or No . You can configure this parameter in the phone configuration XML file (cfg.xml) by entering a string in this format: <Webex_Calendar_Enable ua="na">No</Webex_Calendar_Enable> When you set Calender Enable to Yes , phone supports Webex OBTJ meetings with display of multiple meeting notifications in the meeting list. Also, Meeting softkey appears. To know more about adding the Meeting softkey, see Add Meetings Softkey on Phone . |
| Step 3 | Click Submit All Changes . |

| Step 1 | Select Voice > Phone . |
|---|---|
| Step 2 | In the Programmable Softkeys section, set the Programmable Softkey Enable to Yes . |
| Step 3 | In the Connected Meeting Key List field, edit the field as described in the following example: leave\|2;selfviewoff\|3;dnd;psk1 For psk, only DTMF is supported. To control video layout, add the Layout softkey on the phone by adding the layout keyword in the Connected Meeting Key List field. You can add the keyword in the this format: leave\|2;layout;selfviewoff\|3;dnd;psk1 |
| Step 4 | Click Submit All Changes . |

| Step 1 | Select Voice > Phone . |
|---|---|
| Step 2 | Under Supplementary Services , choose Yes for the Conference Serv parameter. You can configure this parameter in the phone configuration XML file (cfg.xml) by entering a string in this format: <Conference_Serv ua="na">Yes</Conference_Serv> Options: Yes and No Default: Yes |
| Step 3 | Click Submit All Changes . |

| Step 1 | Select Voice > Ext (n) where n is an extension number. |
|---|---|
| Step 2 | In the Call Feature Settings section, select Yes from the Callinfo Subscribe list. When you select Yes , the line will subscribe call-info event, and receive notify from the server for call status changes. This will make participant
                                          aware if the current call is in an Ad Hoc conference. Also, it allows to show the participants list. If you select No , for shared lines, both the host and the participants can show participants list. But for private lines, only host can show
                                          the participants list. You can configure this parameter in the phone configuration XML file (cfg.xml) by entering a string in this format: <CallInfo_Subscribe_1_ ua="na">Yes</CallInfo_Subscribe_1_> Default: No |
| Step 3 | Click Submit All Changes . |

| Recording Mode in Server | Recording Softkeys Available on the Phone |
|---|---|
| Always | No softkeys available. Your user can't control recording from the phone. Recording starts automatically when a call is connected. |
| Never | PauseRec ResumeRec When a call is connected, recording starts automatically and your user can control the recording. |
| On Demand | Record PauseRec ResumeRec When a call is connected, recording starts automatically but the recording is not saved until the user presses the Record softkey. Your user sees a message when recording state changes. |
| On Demand with User Initiated Start | Record PauseRec StopRec ResumeRec The recording only starts when your user presses the Record softkey. Your user sees a message when recording state changes. |

| Icon | Meaning |
|---|---|
|  | Recording in progress. |
|  | Recording paused |

| Icon | Meaning |
|---|---|
|  | Recording in progress |
|  | Recording in progress (8811) |
|  | Recording paused |
|  | Recording paused (8811) |

| Step 1 | Select Voice > Phone . |
|---|---|
| Step 2 | In the Supplementary Services section, click Yes or click No to enable or to disable the Call Recording Serv parameter. You can configure this parameter in the phone configuration XML file (cfg.xml) by entering a string in this format: <Call_Recording_Serv ua="na">Yes</Call_Recording_Serv> Options: Yes and No Default: No |
| Step 3 | (Optional) In the Programmable Softkeys section, to enable softkeys, add a string in this format in the Connected Key List and Conferencing Key List fields. crdstart;crdstop;crdpause;crdresume |
| Step 4 | Click the Ext(n) tab that requires call recording. |
| Step 5 | In the SIP Settings section, in the Call Recording Protocol , select SIPREC as the call recording protocol. You can configure this parameter in the phone configuration XML file (cfg.xml) by entering a string in this format: <Call_Recording_Protocol_3_ ua="na">SIPREC</Call_Recording_Protocol_3_> Options: SIPREC and SIPINFO Default: SIPREC |
| Step 6 | Click Submit All Changes . |

| Icon | Meaning |
|---|---|
|  | Recording in progress. |

| Icon | Meaning |
|---|---|
|  | Recording in progress |
|  | Recording in progress (8811) |

| Step 1 | Select Voice > Phone . |
|---|---|
| Step 2 | In the Supplementary Services section, click Yes or click No to enable or to disable call recording in the Call Recording Serv parameter. You can configure this parameter in the phone configuration XML file (cfg.xml) by entering a string in this format: <Call_Recording_Serv ua="na">Yes</Call_Recording_Serv> Options: Yes and No Default: No |
| Step 3 | (Optional) In the Programmable Softkeys section, to enable softkeys, add a string in this format in the Connected Key List and Conferencing Key List fields. crdstart;crdstop;crdpause;crdresume |
| Step 4 | Click the Ext(n) tab that requires call recording. |
| Step 5 | In the SIP Settings section, for the Call Recording Protocol parameter, select SIPINFO as the call recording protocol. You can configure this parameter in the phone configuration XML file (cfg.xml) by entering a string in this format: <Call_Recording_Protocol_1_ ua="na">SIPINFO</Call_Recording_Protocol_1_> Options: SIPREC and SIPINFO Default: SIPREC |
| Step 6 | Click Submit All Changes . |

| Step 1 | Select Voice > User . The user can select User Login > Voice > User . |
|---|---|
| Step 2 | In the Supplementary Services section, for the Handset LED Alert parameter, select Voicemail, Missed Call . You can configure this parameter in the phone configuration XML file (cfg.xml) by entering a string in this format: <Handset_LED_Alert ua="rw">Voicemail,Missed Call</Handset_LED_Alert> Options: Voicemail and Voicemail, Missed Call Default: Voicemail |
| Step 3 | Click Submit All Changes . |

| Step 1 | Select Voice > User . |
|---|---|
| Step 2 | In the Supplementary Services area, for the DND Setting parameter, select Yes . You can configure this parameter in the phone configuration XML file (cfg.xml) by entering a string in this format: <DND_Setting ua="rw">Yes</DND_Setting> Options: Yes and No Default: No |
| Step 3 | Click Submit All Changes . |

| Step 1 | Select Voice > Ext [n] (where [n] is the extension number). |
|---|---|
| Step 2 | In the Call Feature Settings section, set the Feature Key Sync parameter to Yes . You can configure this parameter in the phone configuration XML file (cfg.xml) by entering a string in this format: Options: Yes and No Default: No |
| Step 3 | Click Submit All Changes . |

| Step 1 | Select Voice > Phone . |
|---|---|
| Step 2 | In the Webex section, set the Directory Enable to Yes . You can configure this parameter in the phone configuration XML file (cfg.xml) by entering a string in this format: <Webex_Directory_Enable ua="na”>Yes</Webex_Directory_Enable> Default value: No |
| Step 3 | In the Directory Name field, enter a name for the Webex directory. You can configure this parameter in the phone configuration XML file (cfg.xml) by entering a string in this format: <Webex_Directory_Name ua="na”>wcdir</Webex_Directory_Name> Default value: Empty The name you enter (for example, wcdir ), displays as the Webex directory name on the phone under the directory list. You can modify this name from the phone administration
                                          web page or from the configuration XML file string. When required, your user can also modify this name from the phone. When
                                          the Directory Name field is empty, by default, the Webex directory name on the phone appears as Webex directory . When the phone is not onboarded to Cisco Webex cloud successfully, the Webex directory doesn't appear under the directory list. |
| Step 4 | Click Submit All Changes . |

| Step 1 | Select Voice > Phone . |
|---|---|
| Step 2 | Select a line key. |
| Step 3 | (Optional) Set the Extension parameter to Disabled to disable the extension. Note If the Direct PLK Configuration feature is disabled, you must disable the extension to configure Webex contacts on the line
                                                      key. If the feature is enabled, you can skip this step. For details, see Enable Direct PLK Configuration . You can also configure this parameter in the phone configuration file (cfg.xml). The parameter is line-specific. Enter a string
                                          in this format: <Extension_ n _ ua="na">Disabled</Extension_ n _> where n is the extension number. | Note | If the Direct PLK Configuration feature is disabled, you must disable the extension to configure Webex contacts on the line
                                                      key. If the feature is enabled, you can skip this step. For details, see Enable Direct PLK Configuration . |
| Note | If the Direct PLK Configuration feature is disabled, you must disable the extension to configure Webex contacts on the line
                                                      key. If the feature is enabled, you can skip this step. For details, see Enable Direct PLK Configuration . |
| Step 4 | In the Extended Function parameter, enter a string in this format: fnc=shortcut;url=webexdir;nme=cloudplk where fnc=shortcut means function=shortcut, url is the menu to open this line key, and nme is the name for the Webex directory. In the string, when nme is empty or you don't include nme in the string, by default, the line key displays the directory name as Webex directory . You can also configure this parameter in the configuration file (cfg.xml). Enter a string in this format: <Extended_Function_ n _ ua="na">fnc=shortcut;url=webexdir;nme=cloudplk</Extended_Function_ n _> where n is the extension number. The line key is configured with the feature. For example, if you assign the feature in line key number nine, the user sees cloudplk appears in the line number nine as a shortcut to the Webex directory. By pressing this configured line key, user can access
                                          the Search Webex directory screen and can search the Webex contacts. If Directory Enable on the phone administration web page is set to No , the line key doesn't work. If the phone is not onboarded to the Webex cloud successfully, the line key doesn't work. |
| Step 5 | Click Submit All Changes . |

| Note | If the Direct PLK Configuration feature is disabled, you must disable the extension to configure Webex contacts on the line
                                                      key. If the feature is enabled, you can skip this step. For details, see Enable Direct PLK Configuration . |
|---|---|

| Step 1 | Select Voice > Phone . |
|---|---|
| Step 2 | In the Programmable Softkeys section, set the Programmable Softkey Enable to Yes . |
| Step 3 | Configure a PSK field from PSK 1 through PSK 16 with a string in this format: fnc=shortcut;url=webexdir;nme=cloudplk You can also configure this parameter in the configuration file (cfg.xml). Enter a string in this format: <PSK_ n ua=na>fnc=shortcut;url=webexdir;nme=cloudplk</PSK_ n > A softkey is configured with the feature and appears on the phone. For example, cloudplk appears as a softkey and acts as a shortcut to the Webex directory. By pressing this softkey, user can access the Search Webex directory screen and can search the Webex contacts. In the string, when nme is empty or you don't include nme in the string, by default, the softkey displays the directory name as Webex Dir . If Directory Enable on the phone administration web page is set to No , the softkey doesn't work. If the phone is not onboarded to Cisco Webex cloud successfully, the softkey doesn't work. |

| Step 1 | Select Voice > Phone . |
|---|---|
| Step 2 | In the Call Log section, set the CallLog Enable parameter to Yes and Display Recents From parameter to Webex . You can configure this parameter in the phone configuration XML file (cfg.xml) by entering a string in this format: <CallLog_Enable ua="na">Yes</CallLog_Enable> <Display_Recents_From ua="na”>Webex</Display_Recents_From> Default value of Display Recents From : Phone |
| Step 3 | Click Submit All Changes . Note On the phone, the user can view the duration of any received or placed Webex call log by selecting a call log under Recents > All calls . For a missed call, the call duration is not available. | Note | On the phone, the user can view the duration of any received or placed Webex call log by selecting a call log under Recents > All calls . For a missed call, the call duration is not available. |
| Note | On the phone, the user can view the duration of any received or placed Webex call log by selecting a call log under Recents > All calls . For a missed call, the call duration is not available. |

| Note | On the phone, the user can view the duration of any received or placed Webex call log by selecting a call log under Recents > All calls . For a missed call, the call duration is not available. |
|---|---|

| Step 1 | Select Voice > Regional . |
|---|---|
| Step 2 | In the Vertical Service Activation Codes section, enter *78 for the DND Act Code parameter. You can configure this parameter in the phone configuration XML file (cfg.xml) by entering a string in this format: <DND_Act_Code ua="na">*78</DND_Act_Code> |
| Step 3 | In the Vertical Service Activation Codes section, enter *79 for the DND Deact Code parameter. You can configure this parameter in the phone configuration XML file (cfg.xml) by entering a string in this format: <DND_Deact_Code ua="na">*79</DND_Deact_Code> |
| Step 4 | Click Submit All Changes . |

| Step 1 | Select Voice > Ext(n) . |
|---|---|
| Step 2 | In the ACD Settings section, set up the fields as
                                       described in Parameters for Call Center Agent Setup table. |
| Step 3 | Click Submit All Changes . |

| Parameter | Description |
|---|---|
| Broadsoft ACD | Enables the phone for Automatic Call Distribution (ACD). Perform one of the following: In the phone configuration file with XML(cfg.xml), enter a string in this format: <Broadsoft_ACD_1_ ua="na">Yes</Broadsoft_ACD_1_> In the phone web page, select Yes to enable this feature and select No to disable it. Options: Yes and No Default: No |
| Call Information Enable | Enables the phone to display details of a call center call. Perform one of the following: In the phone configuration file with XML(cfg.xml), enter a string in this format: <Call_Information_Enable_1_ ua="na">Yes</Call_Information_Enable_1_> In the phone web page, select Yes to enable this feature. Select No to disable it. Options: Yes and No Default: Yes |
| Disposition Code Enable | Enables the user to add a disposition code. Perform one of the following: In the phone configuration file with XML(cfg.xml), enter a string in this format: <Disposition_Code_Enable_1_ ua="na">Yes</Disposition_Code_Enable_1_> In the phone web page, select Yes to enable this feature. Select No to disable it. Options: Yes and No Default: Yes |
| Trace Enable | Enables the user to trace the last incoming call. Perform one of the following: In the phone configuration file with XML(cfg.xml), enter a string in this format: <Trace_Enable_1_ ua="na">Yes</Trace_Enable_1_> In the phone web page, select Yes to enable this feature. Select No to disable it. Options: Yes and No Default: Yes |
| Emergency Escalation Enable | Enables the user to escalate a call to a supervisor in case of emergency. Perform one of the following: In the phone configuration file with XML(cfg.xml), enter a string in this format: <Emergency_Escalation_Enable_1_ ua="na">Yes</Emergency_Escalation_Enable_1_> In the phone web page, select Yes to enable this feature. Select No to disable it. Options: Yes and No Default: Yes |
| Queue Status Notification Enable | Displays the call center status and the agent status. Perform one of the following: In the phone configuration file with XML(cfg.xml), enter a string in this format: <Queue_Status_Notification_Enable_1_ ua="na">Yes</Queue_Status_Notification_Enable_1_> In the phone web page, select Yes to enable this feature. Select No to disable it. Options: Yes and No Default: Yes |
| Auto Available After Sign-In | Sets the agent status to Available automatically when the user signs into the phone as a call center agent. Perform one of the following: In the phone configuration file with XML(cfg.xml), enter a string in this format: <Auto_Available_After_Sign-In_1_ ua="na">Yes</Auto_Available_After_Sign-In_1_> In the phone web page, select Yes to enable this feature and select No to disable it. Options: Yes and No Default: No |

| Step 1 | Select Voice > Ext(n) . |
|---|---|
| Step 2 | In the ACD Settings section, set BraodSoft
                                             						ACD to Yes . |
| Step 3 | From ACD Status field, select one of the options: Sync From Local : Select this option to restore the
                                                							last local status as ACD status when the phone boots up, status is
                                                							changed to "Registered" from "Unregistered" or "Registration failed", or
                                                							registration destination ip address is changed due to failover, fallback
                                                							or DNS response is changed. When the intial ACD status is configured to sync from local, and the last
                                                							local status is unavailable with a reason code, after the phone boots
                                                							up, the reason code will not be restored. Sync From Server : Select this option to get ACD intial status
                                             						from the server. This is the default value. You can configure this parameter in the phone configuration XML file
                                             						(cfg.xml) by entering a string in this format: <ACD_Status_n_ ua="na">Sync From Local</ACD_Status_n_> where n = 1 to 16 |
| Step 4 | Click Submit All Changes . |

| Step 1 | Select Voice > Ext(n) . |
|---|---|
| Step 2 | In the ACD Settings section, set the Unavailable Reason Code Enable parameter to No to hide the Unavailable text box on the phone. To display the text box, select Yes . This is the default value. You can configure this parameter in the phone configuration XML file (cfg.xml) by entering a string in this format: <Unavailable_Reason_Code_Enable_1_ ua="na"> Yes </Unavailable_Reason_Code_Enable_1_> |
| Step 3 | Click Submit All Changes . |

| Step 1 | Select Voice > Phone . |
|---|---|
| Step 2 | In the Broadsoft XMPP section, set the fields as
                                       described in the Parameters for Set Up Presence . |
| Step 3 | Click Submit All Changes . |

| Parameter | Description |
|---|---|
| XMPP Enable | Enables the BroadSoft XMPP directory for the phone user. Perform one of the following: In the phone configuration file with XML(cfg.xml), enter a string in this format: <XMPP_Enable ua="na">Yes</XMPP_Enable> In the phone web page, select Yes to forward all calls. Select No to disable it. Options: Yes and No Default: No |
| Server | Name of the XMPP server; for example, xsi.iop1.broadworks.net. Perform one of the following: In the phone configuration file with XML(cfg.xml), enter a string in this format: <XMPP_Server ua="na">xsi.iop1.broadworks.net</XMPP_Server> In the phone web page, enter a name for the server. Default: Empty |
| Port | Server port for the XMPP server. Perform one of the following: In the phone configuration file with XML(cfg.xml), enter a string in this format: <XMPP_Port ua="na">5222</XMPP_Port> In the phone web page, enter the server port. Allowed values: An integer from 0 through 65535 If the value is set to 0, the phone first sends a DNS SRV query for the domain (specified in Server or User ID ) to obtain the XMPP server IP address. If there is no A record in the DNS SRV response, then the phone sends as fallback
                                             an A record lookup for the same domain to obtain the IP address. In this scenario, the actual port number is 5222. Note When both Server and User ID contain the domain names, the domain name in Server is preferred. If the value isn't set to 0, the phone directly sends an A record lookup for the domain (specified in Server or User ID ) to obtain the XMPP server IP address. Default: 5222 | Note | When both Server and User ID contain the domain names, the domain name in Server is preferred. |
| Note | When both Server and User ID contain the domain names, the domain name in Server is preferred. |
| User ID | BroadSoft User ID of the phone user; for example, username1@xdp.broadsoft.com or username1 . Perform one of the following: In the phone configuration file with XML(cfg.xml), enter a string in this format: <XMPP_User_ID ua="na">username1</XMPP_User_ID> In the phone web page, enter the user ID. If the value doesn't contain the domain name, the phone first generates a new user ID by combining the values of this parameter
                                             and Server . For example, the server is xsi.iop1.broadworks.net and user ID is username1 , the generated user ID is username1@xsi.iop1.broadworks.net . Then, the phone sends A record lookup or DNS SRV query for the domain xsi.iop1.broadworks.net to obtain the XMPP server IP address. Default: Empty |
| Password | Alphanumeric password associated with the User ID. Perform one of the following: In the phone configuration file with XML(cfg.xml), enter a string in this format: <XMPP_Password ua="na"></XMPP_Password> In the phone web page, enter a supported password. Default: Empty |
| Login Invisible | When enabled, the user's presence information is not published when the user signs in. Perform one of the following: In the phone configuration file with XML(cfg.xml), enter a string in this format: <Login_Invisible ua="na">Yes</Login_Invisible> In the phone web page, select Yes to enable the feature. Options: Yes and No Default: No |
| Retry Intvl | Interval, in seconds, to allow a reconnect without a log in after the client disconnects from the server. After this interval,
                                             the client needs to reauthenticate. Perform one of the following: In the phone configuration file with XML(cfg.xml), enter a string in this format: <Login_Invisible ua="na">Yes</Login_Invisible> In the phone web page, select Yes to enable the feature. Options: Yes and No Default: No |
| Display XMPP User ID With Top Priority | Displays the XMPP user ID with the highest priority at the top left of the phone screen. If enabled, the XMPP user ID overrides
                                             other display names, for example, Station Name. This parameter takes effect only when the XMPP Enable is set to Yes . Perform one of the following: In the phone configuration file with XML(cfg.xml), enter a string in this format: <Display_XMPP_User_ID_With_Top_Priority ua="na">Yes</Display_XMPP_User_ID_With_Top_Priority> In the phone web page, select Yes to enable the feature. Options: Yes and No Default: No |

| Note | When both Server and User ID contain the domain names, the domain name in Server is preferred. |
|---|---|

| Step 1 | Select Voice > Phone . |
|---|---|
| Step 2 | In the Broadsoft XMPP section, set XMPP Enable to Yes . |
| Step 3 | Set the field Port to 0 . |
| Step 4 | Set the fields Server , User ID , and Password as described in the Parameters for Set Up Presence table. |
| Step 5 | Click Submit All Changes . |

| Step 1 | Select Voice > Phone . |
|---|---|
| Step 2 | In the Broadsoft XMPP section, set XMPP Enable to Yes . |
| Step 3 | Set the fields Server , User ID , and Password as described in the Parameters for Set Up Presence table. |
| Step 4 | Set Display XMPP User ID With Top Priority to Yes . |
| Step 5 | Click Submit All Changes . |

| Step 1 | Select Voice > Phone . |
|---|---|
| Step 2 | In the Miscellaneous Line Key Settings section, for the Call Appearances Per Line parameter, specify the number of calls per line to allow. You can also configure this parameter in the configuration file (cfg.xml) by entering a string in this format: <Call_Appearances_Per_Line ua="na">2</Call_Appearances_Per_Line> The allowed values range from 1 to 10. The default value is 2. For allowing multiple calls on a line, select a value from
                                          2 to 10. Note When the value is set to 1 and one extension is configured on the phone, then the user will not be able to: place a new call if there is an active call. transfer if there is an active call. conference an active call. When the line has a shared line call, the user will not be able to make a new call, transfer a call, or make a conference. | Note | When the value is set to 1 and one extension is configured on the phone, then the user will not be able to: place a new call if there is an active call. transfer if there is an active call. conference an active call. When the line has a shared line call, the user will not be able to make a new call, transfer a call, or make a conference. |
| Note | When the value is set to 1 and one extension is configured on the phone, then the user will not be able to: place a new call if there is an active call. transfer if there is an active call. conference an active call. When the line has a shared line call, the user will not be able to make a new call, transfer a call, or make a conference. |
| Step 3 | Click Submit All Changes . |

| Note | When the value is set to 1 and one extension is configured on the phone, then the user will not be able to: place a new call if there is an active call. transfer if there is an active call. conference an active call. When the line has a shared line call, the user will not be able to make a new call, transfer a call, or make a conference. |
|---|---|

| Note | The phone searches the XML directory using this format: directory_url?n=incoming_call_number . Example: For a multiplatform phone using a third-party service, the phone number (1234) search query has this format, http://your-service.com/dir.xml?n=1234 . |
|---|---|

| Step 1 | Select Voice > Phone . |
|---|---|
| Step 2 | In the Supplementary Services area, set the Reverse Phone Lookup Serv parameter to Yes to enable this feature. You can also configure this parameter in the configuration file (cfg.xml) by entering a string in this format: <Reverse_Phone_Lookup_Serv ua="na">Yes</Reverse_Phone_Lookup_Serv> The allowed values are Yes\|No. The default value is Yes. |
| Step 3 | Click Submit All Changes . |

| Step 1 | Select Voice > Ext n , where n is the phone extension number (1-10) of the phone web dialog. |
|---|---|
| Step 2 | In the Dial Plan section, set the Emergency Number parameter |
| Step 3 | In the E911 Geolocation Configuration section, set the Company UUID , Primary Request URL , and Secondary Request URL parameters as described in the Parameters to Make an Emergency Call . |
| Step 4 | Click Submit All Changes . |

| Parameter | Description |
|---|---|
| Section: Dial Plan |
| Emergency Number | Enter a comma-separated list of emergency numbers. To specify multiple emergency numbers, separate each emergency number with a comma. When one of these numbers is dialed, the unit disables processing of CONF, HOLD, and other similar softkeys or buttons to
                                                avoid accidentally putting the current call on hold. The phone also disables hook flash event handling. Only the far end can terminate an emergency call. The phone is restored to normalcy after the call is terminated and the receiver
                                                is back on-hook. Perform one of the following: to the digits that correspond to the customer emergency service numbers. In the phone configuration file with XML(cfg.xml), enter a string in this format: <Emergency_Number_1_ ua="na"/> In the phone web page, set Emergency Number parameter to the digits that correspond to the customer emergency service numbers. Valid Values: Maximum number length is 63 characters Default: Blank (no emergency number) |
| Section: E911 Geolocation Configuration |
| Company UUID | The Universally Unique Identifier (UUID) assigned to the customer by the emergency call services provider. For example: 07072db6-2dd5-4aa1-b2ff-6d588822dd46 Perform one of the following: In the phone configuration file with XML(cfg.xml), enter a string in this format: <Company_UUID_1_ ua="na"/> In the phone web page, enter a valid identifier assigned by the call services provider. Valid Values: Maximum identifier length is 128 characters. Default: Blank |
| Primary Request URL | Encrypted HTTPS phone location request. The request uses the phone IP addresses, MAC address, Network Access Identifier (NAI),
                                                and chassis ID and port ID assigned by the network switch manufacturer. The request also includes the location server name
                                                and the customer identifier. The server used by the emergency call services provider responds with an Emergency Response Location (ERL) that has a location
                                                Uniform Resource Identifier (URI) tied to the user phone IP address. Perform one of the following: In the phone configuration file with XML(cfg.xml), enter a string in this format: <Primary_Request_URL_1_ ua="na"/> In the phone web page, enter encrypted HTTPS phone location request. For example: https://prod.blueearth.com/e911Locate/held/held_request.action Default: Blank |
| Secondary Request URL | Encrypted HTTPS request sent to the emergency call services provider's backup server to obtain the user's phone location. Perform one of the following: In the phone configuration file with XML(cfg.xml), enter a string in this format: <Secondary_Request_URL_1_ ua="na"/> In the phone web page, enter the encrypted  for the backup server that can return location information. For example: https://prod2.blueearth.com/e911Locate/held/held_request.action Default: Blank |

| Note | Only the Cisco IP Phone 6871 Multiplatform Phones support the feature. |
|---|---|

| Step 1 | Select Voice > Phone . |
|---|---|
| Step 2 | Choose a line key and assign an extension number in the Extension parameter to enable it. When Extension is set to Disabled , the user can't use the line key as a telephony extension. |
| Step 3 | Click Submit All Changes . |

| Step 1 | Select Voice > Phone . |
|---|---|
| Step 2 | In the Miscellaneous Line Key Settings section, set the Enable Direct PLK Configuration parameter to Yes . You can also configure the parameter in the phone configuration file (cfg.xml) with the following XML string: <Enable_Direct_PLK_Configuration ua="na">Yes</Enable_Direct_PLK_Configuration> Allowed values: Yes and No Default value: Yes Note If you set the parameter to No , the extension of a line key must be disabled for the PLK configuration. | Note | If you set the parameter to No , the extension of a line key must be disabled for the PLK configuration. |
| Note | If you set the parameter to No , the extension of a line key must be disabled for the PLK configuration. |
| Step 3 | Select Voice > Ext [n] (where [n] is the extension number). |
| Step 4 | In the Proxy and Registration section, ensure that the Proxy parameter is empty. You can also configure this parameter in the configuration file (cfg.xml) by entering a string in this format: <Proxy_ n _ ua="na"></Proxy_ n _> where n is the extension number. |
| Step 5 | In the Subscriber Information section, ensure that the User ID parameter is empty. You can also configure this parameter in the configuration file (cfg.xml) by entering a string in this format: <User_ID_ n _ ua="na"></User_ID_ n _> where n is the extension number. |
| Step 6 | Click Submit All Changes . |

| Note | If you set the parameter to No , the extension of a line key must be disabled for the PLK configuration. |
|---|---|

| LED Color | Meaning |
|---|---|
| Green | The monitored line is available. |
| Red | The monitored line is busy. |
| Blinking red | The monitored line is ringing. |
| Amber | Error in BLF key configuration. |

| Step 1 | Select Voice > Phone . |
|---|---|
| Step 2 | Select a line key. |
| Step 3 | (Optional) Set the Extension parameter to Disabled to disable the extension. Note If the Direct PLK Configuration feature is disabled, you must disable the extension to add an XML service to the line key.
                                                         If the feature is enabled, you can skip this step. For details, see Enable Direct PLK Configuration . You can also configure this parameter in the phone configuration file (cfg.xml). The parameter is line-specific. Enter a string
                                             in this format: <Extension_ n _ ua="na">Disabled</Extension_ n _> where n is the extension number. | Note | If the Direct PLK Configuration feature is disabled, you must disable the extension to add an XML service to the line key.
                                                         If the feature is enabled, you can skip this step. For details, see Enable Direct PLK Configuration . |
| Note | If the Direct PLK Configuration feature is disabled, you must disable the extension to add an XML service to the line key.
                                                         If the feature is enabled, you can skip this step. For details, see Enable Direct PLK Configuration . |
| Step 4 | In the Extended Function parameter, enter a string in this format: fnc=xml;url=http://xml.service.url;nme=name where: fnc= prk means function=call park. url= http://xml.service.url is the URL for the xml application or directory. nme= XXXX is the name displayed on the phone for the xml service. Replace XXXX with a name. You can also configure the line-specific parameter in the configuration file (cfg.xml). Enter a string in the following format: <Extended_Function_2_ ua="na">fnc=xml;url=http://xml.service.url;nme=name</Extended_Function_2_> |
| Step 5 | Click Submit All Changes . |

| Note | If the Direct PLK Configuration feature is disabled, you must disable the extension to add an XML service to the line key.
                                                         If the feature is enabled, you can skip this step. For details, see Enable Direct PLK Configuration . |
|---|---|

| Step 1 | Select Voice > Phone . |
|---|---|
| Step 2 | In the Programmable Softkeys section, edit the softkeys depending on the call state that you want the softkey to display. For more information, see Parameters for Programmable Softkeys and . |
| Step 3 | Click Submit
                                             				All Changes . |

| Parameter | Description and default value |
|---|---|
| Programmable Softkey Enable | Enables or disables the programmable softkeys. Set this field to Yes to enable the programmable softkeys. Perform one of the following: In the phone configuration file with XML(cfg.xml), enter a string in this format: <Programmable_Softkey_Enable ua="na">Yes</Programmable_Softkey_Enable> In the phone web interface, set this field to Yes or No to enable or disable the programmable softkeys. Allowed values: Yes \| No Default: No |
| PSK 1 through PSK 16 | Programmable softkey fields. Enter a string in these fields to configure softkeys that display on the phone screen. You can
                                                create softkeys for speed dials to numbers or extensions, vertical service activation codes (* codes), or XML scripts. Configure the PSKs in this format: Speed Dial: fnc=sd;ext=extension_number@$PROXY;vid=n;nme=display_name Vertical Service Activation Code: fnc=sd;ext=star_code@$PROXY;vid=n;nme=display_name See Vertical Service Activation Codes . XML Service: fnc=xml;url=http://server_IP/services.xml;vid=n;nme=display_name Menu shortcut: fnc=shortcut;url=userpref;nme=User preferences For more information, see Menu Shortcuts Mapping on PLK and PSK . When you add a programmable softkey to a softkey list, such as Idle Key List, Missed Call Key List, and so on, the programmable
                                                softkey displays on the phone screen. Perform one of the following: In the phone configuration file with XML(cfg.xml), enter a string in this format: <PSK_1 ua="na">fnc=xml;url=http://server_IP/services.xml;vid=n;
nme=display_name</PSK_1> In the phone web interface, set the PSKs in the valid format. Default: Empty |

| Step 1 | Select Voice > Phone . |
|---|---|
| Step 2 | In the Programmable Softkeys section, set the Programmable Softkey Enable to Yes . |
| Step 3 | Select a
                                          			 programmable softkey number field on which to configure a phone feature. |
| Step 4 | Enter the
                                          			 string for the programmable soft key. See the different types of programmable
                                          			 softkeys described in Configure Speed Dial on a Programmable Softkey . |
| Step 5 | Click Submit
                                             				All Changes . |

| Step 1 | Select Voice > Phone . |
|---|---|
| Step 2 | In the Programmable Softkeys section, set the Programmable Softkey Enable to Yes . |
| Step 3 | To configure a
                                          			 speed dial PSK, enter the following in the PSK number field: fnc=sd;ext=extensionname/starcode@$PROXY;vid=n;nme=name Where: fnc=
                                                   					 function of the key (speed dial) extensionname=extension being dialed or the star code action to
                                                   					 perform vid= n
                                                   					 is the extension that the speed dial will dial out name is
                                                   					 the name of the speed dial being configured Note The name field displays on the softkey on the IP phone
                                                         				  screen. We recommend a maximum of 10 characters for a phone. If more characters
                                                         				  are used, the label might be truncated on the phone screen. | Note | The name field displays on the softkey on the IP phone
                                                         				  screen. We recommend a maximum of 10 characters for a phone. If more characters
                                                         				  are used, the label might be truncated on the phone screen. |
| Note | The name field displays on the softkey on the IP phone
                                                         				  screen. We recommend a maximum of 10 characters for a phone. If more characters
                                                         				  are used, the label might be truncated on the phone screen. |
| Step 4 | Edit the
                                          			 following: Idle Key List: Edit the field as described in the following example: redial\|1;newcall\|2;dnd;psk1 If the user incorrectly configures the programmable softkey list features on the phone, the key list on the phone LCD does
                                                   not update. For example: If a user enters rdeial;newcall;cfwd (redial has been misspelt), the key list is not updated and the user does not see any change on the LCD. If a user enters redial;newcall;cfwd;delchar , the user will not see a change on the LCD, as the delchar softkey is not allowed in the Idle Key List . Hence, this is an incorrect configuration of the programmable softkey list. PSK1: fnc=sd;ext=5014@$PROXY;nme=sktest1 Note In this
                                                         				  example, we are configuring a softkey on a phone as a speed dial number for
                                                         				  extension 5014 (sktest1). You can also configure an XML service on the programmable softkey. Enter the string in this format: <PSK_1 ua="na">fnc=xml;url=http://xml.service.url;nme=name</PSK_1> | Note | In this
                                                         				  example, we are configuring a softkey on a phone as a speed dial number for
                                                         				  extension 5014 (sktest1). |
| Note | In this
                                                         				  example, we are configuring a softkey on a phone as a speed dial number for
                                                         				  extension 5014 (sktest1). |
| Step 5 | Click Submit
                                             				All Changes . |

| Note | The name field displays on the softkey on the IP phone
                                                         				  screen. We recommend a maximum of 10 characters for a phone. If more characters
                                                         				  are used, the label might be truncated on the phone screen. |
|---|---|

| Note | In this
                                                         				  example, we are configuring a softkey on a phone as a speed dial number for
                                                         				  extension 5014 (sktest1). |
|---|---|

| Step 1 | Select Voice > Phone > Programmable Softkeys . |
|---|---|
| Step 2 | Set the Programmable Softkey Enable field to yes . |
| Step 3 | From the PSK list (PSK#1 - PSK#16), select a PSK to configure. |
| Step 4 | In the PSK(n) field, where n is a programmable softkey number, enter a string in this format: fnc=dtmf;ext=<dtmf_digits_to_be_outpulsed>;nme=<softkey_display_name>;
vid=<extension_n_to_be_associated> When a phone has more than one registered line, you must include the vid= that is asociated with the particular line/extension in order for the softkey to appear. Otherwise, the softkey will not
                                             display. |
| Step 5 | (Optional) To configure the PSK softkey to toggle within a pair (outpulse-display) each time you press it, enter a string
                                          in this format: fnc=dtmf;ext=<dtmf_digits_to_be_outpulsed>;nme=<softkey_display_name>;
ext2=<second_set_of_dtmf_digits_to_be_outpulsed>;nme2=<second_softkey_display_name_after_first_press>;
vid=<extension_n_to_be_associated> The PSK softkey toggle always starts with the ext/nme for each new call. |
| Step 6 | In the Connected Key List field or Connected Video Key List field, enter the configured PSK keywords according to where on the phone screen you wish the softkey name to appear. For example, in the following entry, the hold softkey name appears in the first position. The softkey name that is listed in the psk1 field appears in the second position, and so on. hold;psk1;endcall;xfer;conf;xferLx;confLx;bxfer;phold;redial;dir;park |
| Step 7 | Select Voice > Ext(n) , where n is the extension number you wish to configure. |
| Step 8 | In the Audio Configuration section, set the DTMF Tx Method to one of the following methods from the drop-down list. InBand AVT INFO Auto InBand+INFO AVT+INFO |
| Step 9 | Click Submit All Changes . Use these examples to help you understand how to configure PSK with DTMF Support options: Example: PSK toggles when pressed. Voice > Phone > Programmable Softkeys > Programmable Softkey Enable: Yes Connected Key List: psk1\|1 ;endcall\|2;conf\|3;xfer\|4; PSK 1: fnc=dtmf;ext=#1;nme=PressStart;ext2=*2;nme2=PressStop;vid=1 Voice > Ext 1 > DTMF Tx Method: Auto Example: Phone sends DTMF digits inband via a PSK softkey. Voice > Phone > Programmable Softkeys Programmable Softkey Enable: yes . Connected Key List: psk1\|1;endcall\|2;conf\|3;xfer\|4; PSK 1: fnc=dtmf;ext=#1;nme=PressMe;vid=1 Voice > Ext 1 > DTMF Tx Method: Auto Example: The PSK softkey pauses between digits. Voice > Phone > Programmable Softkeys > Programmable Softkey Enable: Yes Connected Key List: psk1\|1;endcall\|2;conf\|3;xfer\|4; PSK 1: fnc=dtmf;ext=#1,1006;nme=PressMe;vid=1 Voice > Ext 1 > DTMF Tx Method: Auto Example: The PSK softkey waits for the user's input between digits. Voice > Phone > Programmable Softkeys > Programmable Softkey Enable: Yes Connected Key List: psk1\|1;endcall\|2;conf\|3;xfer\|4; PSK 1: fnc=dtmf;ext=#1X1006;nme=PressMe;vid=1 Voice > Ext 1 > DTMF Tx Method: Auto |

| Step 1 | Select Voice > Phone . |
|---|---|
| Step 2 | Configure the XSI account information by providing values in the XSI Host Server , XSI Authentication Type , Login User ID , Login Password , and CallLog Associated Line parameters. For more information about configuring XSI account, see Configure BroadSoft Settings . |
| Step 3 | Set the CallLog Enable parameter to Yes . |
| Step 4 | Set Display Recents From to Server . |
| Step 5 | In the Programmable Softkeys section, Set the Programmable Softkey Enable parameter to Yes. In the Broadsoft Call History Key List field, the default string is: option\|1;call\|2;editcall\|3; . In the Broadsoft Call History Key List field, the default string is: option\|1;call\|2;editcall\|3;back\|4; Supported strings are option, call, editcall, filter, and back. This parameter doesn't support psk string. Availability of all these softkeys under the All, Placed, Received, and Missed calls list or the Option menu in these calls list depends on the following conditions: Programmable Softkey Enable = Yes and Broadsoft Call History Key List = option\|1;call\|2;editcall\|3;back\|4; － Option , Call , Edit call , Back softkeys appear on the All, Placed, Received, and Missed calls list. Filter appears in the Option menu of calls list. Programmable Softkey Enable = Yes and Broadsoft Call History Key List = option\|1;call\|2;editcall\|3;back\|4; － Option , Call , Edit call , softkeys appear on the All, Placed, Received, and Missed calls list. Back softkey doesn't appear. Filter appears in the Option menu of calls list. Programmable Softkey Enable = Yes and Broadsoft Call History Key List = option\|1;call\|2;back\|4; － Option , Call , Back softkeys appear on the All, Placed, Received, and Missed calls list. Edit call and Filter appears in the Option menu of calls list. Programmable Softkey Enable = Yes and Broadsoft Call History Key List = option\|1;call\|2;editcall\|3;filter\|4; － Option , Call , Edit call , Filter softkeys appear on the All, Placed, Received, and Missed calls list. Programmable Softkey Enable = Yes , PSK 1 = fnc=shortcut;url=missedcalls , and Broadsoft Call History Key List = option\|1;call\|2;psk1\|3;filter222\|4; －only Option and Call softkeys appear on the All, Placed, Received, and Missed calls list because strings psk and filter222 are invalid values. Edit call and Filter appears in the Option menu of calls list. Programmable Softkey Enable = Yes , and Broadsoft Call History Key List = blank －The softkeys appears as default setting option\|1;call\|2;editcall\|3 . Option , Call , Edit call softkeys appear on the All, Placed, Received, and Missed calls list. Filter appears in the Option menu of calls list. Note In the phone configuration file with XML(cfg.xml), enter a string in this format: <Broadsoft_Call_History_Key_List ua="na">option\|1;call\|2;editcall\|3</Broadsoft_Call_History_Key_List> | Note | In the phone configuration file with XML(cfg.xml), enter a string in this format: <Broadsoft_Call_History_Key_List ua="na">option\|1;call\|2;editcall\|3</Broadsoft_Call_History_Key_List> |
| Note | In the phone configuration file with XML(cfg.xml), enter a string in this format: <Broadsoft_Call_History_Key_List ua="na">option\|1;call\|2;editcall\|3</Broadsoft_Call_History_Key_List> |
| Step 6 | Click Submit All Changes . |

| Note | In the phone configuration file with XML(cfg.xml), enter a string in this format: <Broadsoft_Call_History_Key_List ua="na">option\|1;call\|2;editcall\|3</Broadsoft_Call_History_Key_List> |
|---|---|---|---|---|

| Step 1 | Select Voice > Phone . |
|---|---|
| Step 2 | In the Programmable Softkeys section, set the Programmable Softkey Enable to Yes . |
| Step 3 | In the Idle Key List and Missed Call Key List fields, add the value hdsignin and edit the field as described in the following example: hdsignin\|;guestin\|;guestout\|;redial\|;newcall\|;cfwd\|;recents\|;dnd\|;unpark\|;psk1\|;gpickup\|;pickup\|;dir\|4;miss\|5;acd_login\|;acd_logout\|; |
| Step 4 | Click Submit All Changes . |

| Step 1 | Select Voice > User . |
|---|---|
| Step 2 | In Time Format parameter, set the format to 12hr or 24hr. You can also enable the parameters in the phone configuration file (cfg.xml). <Time_Format ua="na">12hr</Time_Format> Default: 12 hr |
| Step 3 | Click Submit All Changes . |

| Note | Validated call－When the caller carries verstat=TN-Validation-Passed in the SIP Header PAID or FROM, an extra icon next to the caller id is displayed on the phone with a color screen indicating a validated caller. For a phone with grayscale
                                                   screen, an extra icon next to the caller id is displayed. Spam call－When the caller carries verstat=TN-Validation-Failed in the SIP Header PAID or FROM, an extra icon next to the caller id is displayed on the phone indicating an illegitimate caller. Unverified call－When the caller carries verstat=NO-TN-Validation in the SIP Header PAID or FROM, an extra icon next to the caller id is displayed on the phone indicating an unverified call. |
|---|---|

| Step 1 | Select Voice > Phone . |
|---|---|
| Step 2 | In the Programmable Softkeys section: Set the Programmable Softkey Enable parameter to Yes . In the Connected Key List field, add the adhocparticipants keyword in the string. In the Hold Key List field, add the adhocparticipants keyword in the string. The Participants softkey shows up during an Ad Hoc conference call. Note If you set the Programmable Softkey Enable parameter to No , for a participant, the Participants softkey is always available when the list is received from the server. | Note | If you set the Programmable Softkey Enable parameter to No , for a participant, the Participants softkey is always available when the list is received from the server. |
| Note | If you set the Programmable Softkey Enable parameter to No , for a participant, the Participants softkey is always available when the list is received from the server. |
| Step 3 | Click Submit All Changes . |

| Note | If you set the Programmable Softkey Enable parameter to No , for a participant, the Participants softkey is always available when the list is received from the server. |
|---|---|

| Step 1 | Select Voice > Phone . |
|---|---|
| Step 2 | In the Programmable Softkeys section: Set the Programmable Softkey Enable parameter to Yes . In the Connected Meeting Key List field, add the participants keyword in the string. The Participants softkey shows up during a hybrid meeting. Note If the Programmable Softkey Enable parameter is No , the Participants softkey is displayed by default. | Note | If the Programmable Softkey Enable parameter is No , the Participants softkey is displayed by default. |
| Note | If the Programmable Softkey Enable parameter is No , the Participants softkey is displayed by default. |
| Step 3 | Click Submit All Changes . |

| Note | If the Programmable Softkey Enable parameter is No , the Participants softkey is displayed by default. |
|---|---|

| Step 1 | Select Voice > Phone . |
|---|---|
| Step 2 | In the Programmable Softkeys section: Set the Programmable Softkey Enable parameter to Yes . In the Connected Meeting Key List field, add the audiomute keyword in the string. The Mute or Unmute softkey shows up during a hybrid meeting. Note If the Programmable Softkey Enable parameter is No , the Mute or the Unmute softkey is displayed by default. | Note | If the Programmable Softkey Enable parameter is No , the Mute or the Unmute softkey is displayed by default. |
| Note | If the Programmable Softkey Enable parameter is No , the Mute or the Unmute softkey is displayed by default. |
| Step 3 | Click Submit All Changes . |

| Note | If the Programmable Softkey Enable parameter is No , the Mute or the Unmute softkey is displayed by default. |
|---|---|

| Step 1 | Select Voice > Phone . |
|---|---|
| Step 2 | In the Programmable Softkeys section: Set the Programmable Softkey Enable parameter to Yes . In the Connected Meeting Key List field, add the videounmute keyword in the string. The Start video or Stop video softkey shows up during a hybrid meeting. Note If the Programmable Softkey Enable parameter is No , the Start video or Stop video softkeys are displayed by default. | Note | If the Programmable Softkey Enable parameter is No , the Start video or Stop video softkeys are displayed by default. |
| Note | If the Programmable Softkey Enable parameter is No , the Start video or Stop video softkeys are displayed by default. |
| Step 3 | Click Submit All Changes . |

| Note | If the Programmable Softkey Enable parameter is No , the Start video or Stop video softkeys are displayed by default. |
|---|---|

| Keyword | Key Label | Definition | Available Phone Status |
|---|---|---|---|
| acd_login | Agt signin | Logs user in to Automatic Call Distribution (ACD). | Idle |
| acd_logout | AgtSignOut | Logs user out of ACD. | Idle |
| answer | Answer | Answers an incoming call. | Ringing |
| astate | Agt Status | Checks the ACD status. | Idle |
| avail | Avail | Denotes that a user who is logged in to an ACD server has set his status as available. | Idle |
| barge | Barge | Allows another user to interrupt a shared call. | Shared-Active, Shared-Held |
| bargesilent | BargeSilent or BargeSlnt | Allows another user to interrupt a shared call with the mic disabled. | Shared-Active |
| bxfer | BlindXfer | Performs a blind call transfer (transfers a call without speaking to the party to whom the call is transferred). Requires
                                             that Blind Xfer Serv is enabled. | Connected Connected Video |
| call (or dial) | Call | Calls the selected item in a list. | Dialing Input |
| call info | Call Info | Show call information | Progressing |
| calllist | Call list | Provides access to the call list while on a connected video call. | Connected, Connected Video |
| cancel | Cancel | Cancels a call (for example, when conferencing a call and the second party is not answering. | Off-Hook |
| cfwd | Forward / Clr fwd | Forwards all calls to a specified number. | Idle, Off-Hook, Shared-Active, Hold, Shared-Held |
| crdpause | PauseRec | Pause recording | Connected, Conferencing |
| crdresume | ResumeRec | Resume recording | Connected, Conferencing |
| crdstart | Record | Start a recording | Connected, Conferencing |
| crdstop | StopRec | Stop recording | Connected, Conferencing |
| conf | Conference | Initiates a conference call. Requires that Conf Server is enabled and there are two or more calls that are active or on hold. | Connected Connected Video |
| confLx | Conf line | Conferences active lines on the phone. Requires that Conf Serv is enabled and there are two or more calls that are active
                                             or on hold. | Connected Connected Video |
| delchar | delChar - backspace Icon | Deletes a character when entering text. | Dialing Input |
| dir | Dir | Provides access to phone directories. | Idle, Miss, Off-Hook (no input), Connected, Start-Xfer, Start-Conf, Conferencing, Hold, Ringing, Shared-Active, Shared-Held |
| disp_code | DispCode | Enter Disposition Code | Idle, Connected, Conferencing, Hold |
| dnd | DND / Clr Dnd | Sets Do Not Disturb to prevent calls from ringing the phone. | Idle, Off-Hook, Hold, Shared-Active, Shared-Held, Conferencing, Start-Conf, Start-Xfer, Connected video |
| emergency | Emergency | Enter emergency number | Connected |
| em_login (or signin) | Sign in | Logs user in to Extension Mobility. | Idle |
| em_logout (or signout) | Sign out | Logs user out of Extension Mobility. | Idle |
| endcall | End call | Ends a call. | Connected, Off-hook, Progressing, Start-Xfer, Start-Conf, Conferencing, Releasing, Hold, and Connected Video |
| favorites | Favorites | Provides access to "Speed Dials". | Idle, Miss, Off-Hook (no input), Connected, Start-Xfer, Start-Conf, Conferencing, Hold, Ringing, Shared-Active, Shared-Held Connected Video |
| gpickup | GrPickup | Allows user to answer a call ringing on an extension by discovering the number of the ringing extension. | Idle, Off-Hook |
| hold | Hold | Put a call on Hold. | Connected, Start-Xfer, Start-Conf, Conferencing, Connected Video |
| ignore | Decline | Ignores an incoming call. | Ringing |
| ignoresilent | Ignore | Silences an incoming call | Ringing |
| join | Join | Connects a conference call. If the conference host is user A and users B & C are participants, when A presses "Join", A will
                                             drop off and users B & C will be connected. | Conferencing |
| lcr | Call Rtn/lcr | Returns the last missed call. | Idle, Missed-Call,Off-Hook (no input) |
| left | Left arrow icon | Moves the cursor to the left. | Dialing Input |
| messages | Messages | Provides access to voicemail. | Idle, Miss, Off-Hook (no input), Connected, Start-Xfer, Start-Conf, Conferencing, Hold, Ringing, Shared-Active, Shared-Held Connected Video |
| miss | Miss | Displays the list of missed calls. | Missed-Call |
| newcall | New Call | Begins a new call. | Idle, Hold, Shared-Active, Shared-Held |
| option | Option | Opens a menu of input options. | Off-Hook |
| park | Park | Puts a call on hold at a designated "park" number. | Connected Connected Video |
| phold | PrivHold | Puts a call on hold on an active shared line. | Connected Connected Video |
| pickup | PickUp | Allows a user to answer a call ringing on another extension by entering the extension number. | Idle, Off-Hook |
| pip | PIP icon | Allows user to move PIP to one of the four corners of the screen or turn PIP off. | Connected Video |
| recents | Recents | Displays the All calls list from call history. | Idle, Off-Hook, Shared-Active, Shared-Held |
| redial | Redial | Displays the redial list. | Idle, Connected, Start-Conf, Start-Xfer, Off-Hook (no input), Hold Connected Video |
| resume | Resume | Resumes a call that is on hold. | Hold, Shared-Held |
| right | Right arrow icon | Moves the cursor to the right. | Dialing (input) |
| settings | Settings | Provides access to "Information and Settings". | All |
| showvideo | Show video | Provides access to the video session while on a connected video call and the call list is in view | Connected |
| starcode | Input Star Code/*code | Displays a list of star codes that can be selected. | Off-Hook, Dialing (input) |
| swap | Swap | Allows user to swap the remote video stream and selfview during an active video call. | Connected Video |
| trace | Trace | Trigger trace | Idle, Connected, Conferencing, Hold |
| unavail | Unavail | Denotes that a user who is logged in to an ACD server has set his status as unavailable. | Idle |
| unpark | Unpark | Resumes a parked call. | Idle, Off-Hook, Connected, Shared-Active Connected Video |
| xfer | Transfer | Performs a call transfer. Requires that Attn Xfer Serv is enabled and there is at least one connected call and one idle call. | Connected, Start-Xfer, Start-Conf |
| xferlx | Xfer line | Transfers an active line on the phone to a called number. Requires that Attn Xfer Serv is enabled and there are two or more
                                             calls that are active or on hold. | Connected Connected Video |

| Note | Only the Cisco IP Phone 6871 Multiplatform Phones support the executive and assistant  programmable softkeys. |
|---|---|

| Keyword | Key Label | Definition | Available Phone Status |
|---|---|---|---|
| bridgein | Bridge in | Only available to executives who have assistants. Joins the user (executive) to an ongoing call with an assistant. | Idle, Shared-Active |
| callpush | Call push | Only available to executive assistants. Transfers an ongoing call from the user (assistant) to the executive. | Hold , Shared-Active |
| callretrieve | Retrieve | Only available to executives who have assistants. Transfers an ongoing call from the assistant to the user (executive). | Idle, Shared-Active |
| divert | Clr divert | Only available to executive assistants. Deactivates call diversion for the user (assistant). | Available only when call diversion is active and you navigate to the menu Settings > Assistant . It is also available when you press the line key that is configured as Assistant . |
| divert | Divert | Only available to executive assistants. Activates call diversion for the user (assistant). All incoming calls to the user,
                                             for executives that the user handles, are diverted to the specified destination. | Available when you navigate the menu Settings > Assistant . It is also available when you press the line key that is configured as Assistant . |
| proxycall | Proxy call | Only available to executive assistants. Initiates a call on behalf of the selected executive. | Available when you navigate the menu Settings > Assistant . It is also available when you press the line key that is configured as Assistant . |

| Step 1 | Select Voice > User . |
|---|---|
| Step 2 | Select Yes for the parameter Auto Collapse Into Line Key . To disable the feature, select No . You can also configure this parameter in the phone configuration XML file (cfg.xml) by entering a string in this format: <Auto_Collapse_Into_Line_Key ua="rw">Yes</Auto_Collapse_Into_Line_Key> Default: No . If the Auto Collapse Into Line Key feature is enabled, the call info screen will be closed once the call is answered. |
| Step 3 | Click Submit All Changes . |

| Step 1 | Select Voice > Att Console > General . |
|---|---|
| Step 2 | Select Yes for the parameter BLF Callpark On Line Key Enable . To disable the feature, select No . You can also configure this parameter in the phone configuration XML file (cfg.xml) by entering a string in this format: <BLF_Callpark_On_Line_Key_Enable ua=”na“>Yes</BLF_Callpark_On_Line_Key_Enable> Default: No . |
| Step 3 | Navigate to Voice > Phone and select a line key. |
| Step 4 | (Optional) To disable the extension, set the Extension parameter to Disabled . Note You must disable the extension to add an extended function to the line key, if the Direct PLK Configuration feature is disabled.
                                                      For more information, see Enable Direct PLK Configuration section in the Administration Guide . | Note | You must disable the extension to add an extended function to the line key, if the Direct PLK Configuration feature is disabled.
                                                      For more information, see Enable Direct PLK Configuration section in the Administration Guide . |
| Note | You must disable the extension to add an extended function to the line key, if the Direct PLK Configuration feature is disabled.
                                                      For more information, see Enable Direct PLK Configuration section in the Administration Guide . |
| Step 5 | Enter the string in the following format in the Extended Function field: fnc=prk;sub=BLF_List_URI@$PROXY;usr=user_ID@$PROXY Where, sub— the URI to which the SUBSCRIBE message is sent. This name must be identical to the name defined in the BLF List URI. usr— the call park extension that the BLF monitors. |
| Step 6 | Click Submit All Changes . |

| Note | You must disable the extension to add an extended function to the line key, if the Direct PLK Configuration feature is disabled.
                                                      For more information, see Enable Direct PLK Configuration section in the Administration Guide . |
|---|---|