---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cuipph-mpp-7800-english-userguide-pa2d-b-7800-user-guide-mpp-11-pa2d-b-7800--583d62de93
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cuipph/MPP/7800/english/userguide/pa2d_b_7800-user-guide-mpp-11/pa2d_b_7800-user-guide-mpp-11_chapter_0101.html
retrieved_at: 2026-08-21T02:23:28.903043+00:00
---

Cisco IP Phone 7800 Series Multiplatform Phones User Guide

# Cisco IP Phone 7800 Series Multiplatform Phones User Guide

Updated: January 30, 2024

Chapter: Settings

## Chapter: Settings

# Settings

## Phone Settings Overview

Your administrator can configure the phone to make the setting menus available on the phone screen or on the phone web interface.
                              If you can't find a specific menu, contact your administrator.

## Change the Ringtone

You can set a ringtone for an incoming call.

Step 1

Press Applications .

Step 2

Select User preferences > Ringtone > Ext (n) - Ring tone , where n= extension number.

Step 3

Scroll through the list of ringtones and press Play to hear a sample.

Step 4

Press Select and then Set to save a selection.

## Assign a Ring Tone with the Phone Web Page

Step 1

On the phone web page, select User Login > Voice > Ext(n) , where (n) is the number of an extension.

Step 2

In Call Feature Settings area, choose a ringtone from the Default Ring drop-down list.

If you don't want to specify a ringtone for the phone line, choose No ring . Your phone doesn't ring when receiving an incoming call.

Step 3

Click Submit All Changes .

## Control Ringer Volume

You can control the ringer volume of an incoming call on the phone, or from the phone administration web page.

If your administrator restricts your ability to control the ringer volume, you can't perform this task from either the phone
                              volume key or from the phone administration web page.

### Before you begin

Your administrator must allow you to control the ringer volume.

To control the ringer volume do one of the following.

When your administrator restricts your ability to control the ringer volume, a message appears indicating that you have no
                                                         permission to change the ringer volume.

The valid value for the Ringer Volume parameter ranges from 0 to 15.

When your administrator restricts your ability to control the ringer volume, the Ringer Volume parameter doesn't appear under the Audio Volume section.

## Forward Calls from Your Phone

You can set up your phone to forward incoming calls after navigating to the Call forward settings screen.

There are two other methods to set up the call forward services. To set up the call forward services by a specific softkey,
                              see Forward Calls . To set up the call forward services from the phone web page, see Forward Calls with the Phone Web Page .

### Before you begin

Your administrator must enable the call forward services.

Your administrator disables the feature activation code synchronization for call forward. If enabled, the screen Call forward settings changes to be ready-only, however you can still change the setting for the Call Forward All service by pressing Forward or Forward all on the main screen. For more information, see Activate Call Forward All with Feature Activation Code Synchronization .

Step 1

Press Applications .

Step 2

Select User preferences > Call preferences > Call forwarding to access the Call forward settings screen.

Step 3

Select a call forward service.

- Forward all —Determines whether to forward all incoming calls to a target phone number.

- Forward busy —Determines whether to forward an incoming call to a target phone number when the line is busy.

- Forward no answer —Determines whether to forward an incoming call to a target phone number when the call isn't answered.

Step 4

Enable the call forward service by pressing Select button of the Navigation cluster .

Step 5

Assign a target phone number for the call forward service.

- Forward all number —Specifies the target phone number to which you want to forward all incoming calls.

- Forward busy number —Specifies the target phone number to which you want to forward the incoming call when the line is busy.

- Fwd no answer number —Specifies the target phone number to which you want to forward the coming call when the call isn't answered.

If your administrator disables the feature key synchronization (FKS) and XSI sync for call forward on your phone, you can enter the value as number of seconds after which call needs to be forwarded.

If your administrator enables FKS or XSI sync for call forward on your phone, you can enter the value as number of rings after which call needs to be forwarded.

The call forward settings on the phone take effect only when FKS and XSI are disabled. For more information, consult your
                                          administrator.

Step 6

(Optional) Assign a target phone number by using the Contacts softkey.

In the Call forward settings screen, select any of the call forward service.

Select Forward all number , Forward busy number , or Fwd no answer number based on the call forward service that you selected, then press the Contacts softkey.

Search for a contact. For more information, see Search for a Contact in the All Directories Screen .

Press Call to assign the target phone number.

Step 7

Press Set to apply the settings.

Step 8

Verify if the setting takes effect by looking for the call forward icon. The icon displays with a target number on the top left or middle of the phone screen.

After you enable any of the call forward services, the Forward or Forward all softkey changes to the Clr fwd or Clf fwd all respectively . You can press the softkey to disable the call forward service or services, while the target phone number still remains.

Clf fwd all disables only the Call Forward All service, Clf fwd disables all call forward services.

If the call forward settings on the phone don't take effect, consult your administrator.

## Turn on Do Not Disturb for a Specific Line

Set do not disturb (DND) to silence your phone and suppress incoming call notifications when you need to avoid distractions.
                              You can suppress all incoming call notifications or you can suppress a specific caller notification.

Step 1

Select a phone line using the Navigation cluster.

Step 2

Press Applications .

Step 3

Select User preferences > Call preferences > Do not disturb .

If the Do not disturb menu doesn't display on the screen, contact your administrator.

Step 4

Select On to turn on DND or select Off to turn off DND.

Step 5

Press Set to save the setting.

## Turn on DND from the Phone Web Page

Step 1

On the phone web page, select User Login > Voice > User .

Step 2

Under Supplementary Services , set DND Settings to Yes .

Step 3

Click Submit All Changes .

## Block an Anonymous Call

You can block an incoming call that does not have caller information for a specific line or all lines .

If your administrator has enabled synchronization of Anonymous Call Rejection between a line and a BroadSoft XSI service,
                              then your setting only applies to the specific line instead of all lines. Typically, the setting applies to all the lines,
                              except for the ones where the synchronization is enabled.

Step 1

Press the Navigation cluster up or down to select a phone line.

Step 2

Press Applications .

Step 3

Select User preferences > Call preferences > Block anonymous call .

Step 4

Select On if you want to block the call that does not have caller information, or select Off to allow the call.

Step 5

Press Set to save the setting.

## Block Caller ID

You can block your caller identification to prevent your name and phone number from being displayed on the receiver's screen
                              when you make a call. This feature helps you to maintain privacy.

### Before you begin

Your administrator enables Block CID feature on your phone.

Your administrator enables Block CID feature on the XSI BroadWorks server.

Step 1

Press Applications .

Step 2

Select User preferences > Call preferences .

Step 3

Select Block caller ID .

Step 4

Press Select to toggle caller ID blocking on or off.

If your administrator enables the block caller ID feature on the XSI BroadWorks server, your phone retrieves the value from
                                          the server and you see the value that your administrator sets on the server. You can then modify the value from the Block caller ID menu on the phone.

Step 5

Press Set to save the change.

## Secure a Call

You can encrypt calls to protect them from eavesdroppers. You can set up the secure call feature on all outbound calls or
                              for a specific call.

Step 1

Press Applications .

Step 2

Select User preferences > Call preferences > Secure call .

Step 3

Select On to enable secure call feature or select Off to disable the secure call feature.

Step 4

Press Set to save the setting.

## Set Up an Auto Answer Page

Step 1

Press Applications .

Step 2

Select User preferences > Call preferences > Auto answer page .

Step 3

Select On to enable the Auto answer page or select Off to disable Auto answer page.

Step 4

Press Set to save the changes.

## Enable Call Waiting

You can enable call waiting for a specific line or all lines. If enabled, you can receive the call notification (a single
                              beep and the line button flashes red) while on an active call.

If your administrator has enabled synchronization of Call Waiting between a line and a BroadSoft XSI service, then your setting
                              only applies to the specific line instead of all lines. Typically, the setting applies to all lines, except for the ones where
                              the synchronization is enabled.

Step 1

Press the Navigation cluster up or down to select a phone line.

Step 2

Press Applications .

Step 3

Select User preferences > Call preferences > Call waiting .

Step 4

Select On to allow you to answer an incoming call that rings while on another call, or select Off to disable the function.

Step 5

Press Set to save the setting.

## Set Up Voicemail

Step 1

Press Applications .

Step 2

Select User preferences > Call preferences > Voice mail .

Step 3

Enter a phone number to check voicemail.

If you press the Messages button, it dials the voicemail number and displays the voice message list.

Step 4

Press Set to confirm the assigned number.

Step 5

Press Back to exit.

## HTTP Proxy Settings

You can set up an HTTP proxy on your phone from the HTTP proxy settings menu under the Network configuration menu. The HTTP proxy settings are also available on the phone web page.

### Set Up a Proxy Server with the Auto Proxy Mode

Step 1

Select Network configuration > HTTP proxy settings > Proxy mode .

Step 2

Press the Select button of the navigation cluster to choose Auto .

Step 3

Highlight Auto discovery (WPAD) , select On to turn on Web Proxy Auto-Discovery (WPAD) that is used to retrieve a PAC file automatically, select Off to turn off WPAD.

By default, your phone uses WPAD in the auto proxy mode.

Step 4

(Optional) If you turn off WPAD in the previous step, you need to further enter a valid Proxy Auto-Configuration (PAC) URL in PAC URL . For example:

```
http://proxy.department.branch.example.com/pac
```

If you don't have the PAC URL, contact your administrator.

Step 5

Press Set to apply the settings.

### Set Up a Proxy Server with the Manual Proxy Mode

#### Before you begin

Step 1

Select Network configuration > HTTP proxy settings > Proxy mode .

Step 2

Press the Select button of the navigation cluster to choose Manual .

Step 3

Enter a valid hostname or IP address of a proxy server in Proxy host .

Do not provide the scheme ( http:// or https:// ) for the proxy host.

Step 4

Enter a valid server port of the specified proxy server in Proxy port .

Step 5

(Optional) If your proxy server requires authentication, highlight Proxy authentication and then select On .

Step 6

(Optional) Enter your username and password to access the proxy server.

If you don't have the username and password, contact your administrator.

Step 7

Press Set to apply the settings.

### Set Up a Proxy Server from the Phone Web Page

Step 1

On the phone web page, select Voice > System .

Step 2

Under the section HTTP Proxy Settings , set the parameters described in the following table:

Parameter

Description

Proxy Mode

Choose the proxy mode for the HTTP proxy setting. Options are:

Auto

Manual

Off

Default: Off

Use Auto Discovery (WPAD)

Select Yes to use the Web Proxy Auto-Discovery (WPAD) mechanism to automatically retrieve a Proxy Auto-Configuration (PAC) file.

If the parameter is set to No , you must configure PAC URL .

This parameter is available when you set Proxy Mode to Auto .

Default: Yes

PAC URL

URL locating the PAC file.

This parameter is available when you set Proxy Mode to Auto and Use Auto Discovery (WPAD) to No .

Proxy Host

Server address (hostname or IP address) of the proxy server.

Do not provide the scheme ( http:// or https:// ).

This parameter is available when you set Proxy Mode to Manual .

Proxy Port

Port number of the proxy server.

This parameter is available when you set Proxy Mode to Manual .

Proxy Server Requires Authentication

If your proxy server requires authentication, select Yes . Otherwise, select No . The parameter configuration depends on the actual behaviour of the proxy server.

This parameter is available when you set Proxy Mode to Manual .

Username

Enter a username of a credential user on the proxy server.

This parameter is available when you set Proxy Mode to Manual and Proxy Server Requires Authentication to Yes .

Password

Enter a password of the specified username for the proxy authentication purpose.

This parameter is available when you set Proxy Mode to Manual and Proxy Server Requires Authentication to Yes .

Step 3

Click Submit All Changes .

## VPN Connection Settings

You can set up and enable a VPN connection on your phone from the VPN settings menu under the Network configuration menu. To facilitate the settings, you can also configure the VPN settings related parameters on the phone web page. If you
                              want to enable the VPN connection, you need to reboot the phone.

### Set Up a VPN Connection

If you want to set up the VPN connection from the phone web page, see Set Up a VPN Connection from the Phone Web Page .

#### Before you begin

Step 1

Press Applications .

Step 2

Select Network configuration > VPN settings .

Step 3

Enter the IP address or FQDN of a VPN server in VPN server .

Step 4

Enter the user credentials in Username and Password .

Step 5

(Optional) If needed, enter the name of a tunnel group in Tunnel group .

If the field is empty, this means no tunnel group is used for this VPN connection.

Step 6

Highlight Connect to VPN on bootup , press the Select button of the navigation cluster to select On .

Step 7

Press Set to save the settings.

The VPN settings are finished. For information about how to enable the VPN connection, see Enable a VPN Connection .

### Enable a VPN Connection

#### Before you begin

Step 1

Press Applications .

Step 2

Select Network configuration > VPN settings .

Step 3

Highlight Enable VPN connection , press the Select button of the navigation cluster to select On to apply the changes.

Once you set Enable VPN connection to On , the phone immediately tries to connect to the VPN server. During the process, the phone reboots automatically.

The VPN connection takes about one minute.

After your phone reboots, the VPN connection icon on the upper-right corner of the phone screen indicates that the VPN connection is established successfully.

If the VPN connection fails, the value of Enable VPN connection remains Off .

Step 4

(Optional) View the details of the VPN connection. For example, the current VPN connection status and VPN IP address. For details, see View the VPN Status .

### Disable a VPN Connection

#### Before you begin

Step 1

Press Applications .

Step 2

Select Network configuration > VPN settings .

Step 3

Highlight Connect to VPN on bootup , press the Select button of the navigation cluster to select Off .

Step 4

Press Set to save the setting.

Step 5

Do one of the following actions:

Highlight Enable VPN connection , select Off .

Once you set Enable VPN connection to Off , the phone immediately tries to disconnect from the VPN server. During the process, the phone reboots automatically.

Manually reboot your phone, see Reboot Your Phone .

The VPN disconnection takes about one minute.

After the phone reboots, the VPN connection icon on the phone screen disappears. This means that the VPN connection is disabled successfully.

Step 6

(Optional) Check whether the VPN connection is Disconnected . For details, see View the VPN Status .

### Set Up a VPN Connection from the Phone Web Page

You can do the same configuration on your phone, see Set Up a VPN Connection .

Step 1

On the phone web page, select Voice > System .

Step 2

Under the section VPN Settings , set the parameters described in the following table.

Parameter

Description

VPN Server

IP address or FQDN of the VPN server.

Default: Empty

VPN User Name

Enter a username for a credential user on the VPN server.

Default: Empty

VPN Password

Enter a password of the specified username to access the VPN server.

Default: Empty

VPN Tunnel Group

Enter a tunnel group assigned to the VPN user.

Tunnel group is used to identify the group policy for the VPN connection.

Default: Empty

Connect on Bootup

Choose whether your phone connects to the VPN server automatically after the phone reboots.

Default: No

Step 3

Click Submit All Changes to save the changes.

The VPN settings are finished. For information about how to enable the VPN connection, see Enable a VPN Connection .

### View the VPN Status

You can also view the status from the phone web page by selecting Info > Status > VPN Status .

Step 1

Press Applications .

Step 2

Select Status > VPN status .

You can view the following information:

VPN connection —Indicates whether the phone connects to the VPN server. The status can be either Connected or Disconnected .

VPN IP address —VPN IP address assigned from the VPN server.

VPN subnet mask —VPN subnet mask assigned from the VPN server.

Sent bytes —Total bytes the phone sent out to the network through the VPN server.

Received bytes —Total bytes the phone received from the network through the VPN server.

## Change the Display Mode

This feature is supported on Cisco IP Phone 7821, 7841, and 7861.

Step 1

Press Applications .

Step 2

Select User preferences > Attendant console preferences > Display mode .

The following options are available:

Name

Ext

Both

Step 3

Choose the display mode and press Set .

## Change the Time Format

You can change the current  time format that the phone screen displays.

Step 1

Press Applications .

Step 2

Select Device administration > Date/Time > Time format .

To set daylight savings, select Device administration > Date/Time > Daylight savings . Select On to turn on the daylight savings and select Off to turn it off.

Step 3

(Optional) Select Device administration > Date/Time > Time zone .

Step 4

Select a time format and press Set to apply the changes.

## Change the Date Format

You can change the date format that you want to see on your phone screen.

Step 1

Press Applications .

Step 2

Select Device administration > Date/Time > Date format .

Step 3

Select a date format and press Set to apply the changes.

## Change the Screen Saver

You can enable your phone screen saver, and specify its appearance and the amount of time for the phone to be idle before
                              the screen saver appears.

Step 1

Press Applications .

Step 2

Select User preferences > Screen preferences > Screen saver .

Step 3

Select On to turn on screen saver and select Off to turn it off.

Step 4

Select Screen saver settings to choose the settings:

Screen saver type —Choose one of the following options:

Clock —Displays a rounded clock with the wallpaper in the background.

Download Picture —Displays a picture pushed from the phone web page.

Logo : Displays a logo as the phone screensaver. This image is added in the Logo URL field of the pone web page.

Lock —Displays a lock icon on the phone screen wallpaper.

Trigger interval —Enter the number of seconds that the phone remains idle before the screen saver turns on.

Refresh interval —Enter the number of seconds before the screen saver should refresh (if, for example, you chose a rotation of pictures).

Step 5

Press Set .

## Configure the Screen Saver with the Phone Web Interface

You can configure a screen saver for the phone. When the phone is idle for a specified time, it enters screen saver mode.

Any button press returns the phone to normal mode.

Step 1

On the phone web page, select Voice > User .

Step 2

In the Screen section, set up the fields as described in the following table.

Parameter

Description

Screen Saver Enable

Select Yes to enable a screen saver on the phone. When the phone is idle for a specified time, it enters screen saver mode.

Default: No

Screen Saver Type

Types of screen saver. Options you can choose:

Clock —Displays a digital clock on a plain background.

Download Picture —Displays a picture pushed from the phone webpage.

Logo : Displays a logo on the phone screen. Add a logo image in the Logo URL field.

Lock —Enables locking of the screensaver.

Screen Saver Wait

Amount of idle time before screen saver displays.

Enter the number of seconds of idle time to elapse before the screen saver starts.

Default: 300

Picture Download URL

URL locating the (.png) file to display on the phone screen background. If you select picture as as screensaver type, this
                                                      image displays as a screensaver on the phone screen.

When you enter an incorrect URL to download a new wallpaper, the phone fails to upgrade to the newer wallpaper and displays
                                                      the existing downloaded wallpaper. If the phone does not have any wallpaper downloaded earlier, it displays a gray screen.

Logo URL

Enter a URL or path for the location where the logo image is saved. If you select logo as as screensaver type, this image
                                                      displays as a screensaver on the phone screen.

Step 3

Click Submit All Changes .

## Add a Logo as a Phone Background

Step 1

On the phone web page, select User Login > Voice > User .

Step 2

In the Screen section, select Logo from the Phone Background field and in the Logo URL field enter a URL or path for the location where the logo image is saved.

Step 3

Click Submit All Changes .

After the logo is added in the phone background, if you select Default from the Phone Background list and save the changes, the logo icon on the phone screen will disappear.

## Adjust the Phone Screen Contrast

Step 1

Press Applications .

Step 2

Select User preferences > Screen preferences > Contrast level .

Step 3

Step 4

Press Save .

## Adjust the Phone Screen Backlight

You can adjust the backlight to make the phone screen easier to read.

Step 1

Press Applications .

Step 2

Select User preferences > Backlight timer .

Step 3

Press Edit to change the backlight mode.

Step 4

Press On to turn the backlight on or press Off to turn the backlight off.

You can also select a time from the list to set a duration for which the backlight will remain on.

Step 5

(Optional) Select a time from the list to set a duration that the backlight remains off.

You can also select the option to set the backlight always on.

Step 6

Press Select to apply the selected backlight mode.

## Adjust the Backlight Timer from Phone Web Page

You can save energy by disabling the backlight on the phone at a preset time. The phone's desktop remains visible, even with
                              the backlight off.

Step 1

On the phone web page, select User Login > Advanced > Voice > User .

Step 2

Under Screen , select a duration for the Back Light Timer parameter.

Step 3

In the LCD Contrast field, enter a number for the desired brightness.

## Specify an Audio Device for a Call

When you connect multiple headsets to the phone, you can choose the audio device to use for a call. Your choice applies when
                              you place or answer a call with a line key or the corresponding softkey.

Step 1

Press Applications .

Step 2

Select User preferences > Audio preferences > Preferred audio device .

Step 3

Press Select to choose one of the options:

- None —Selects the last used audio device.

- Speaker —Selects the speakerphone as the audio device.

- Headset —Selects a headset as the audio device.

Step 4

Press Set to save the selection.

## Set Language

Depending upon how your phone is configured, you may be able to change the language used by your phone.

Step 1

Press Applications .

Step 2

Select Device administration > Language .

Step 3

Select a language from the list of available languages.

Step 4

Select Save .

## Set Password

### Before you begin

Step 1

Press Applications .

Step 2

Select Device administration > Set password .

Step 3

Enter your current password in the Old password field.

Step 4

Enter your new password in the New password  and the Reenter new password fields.

Step 5

Select Save .

## Set Password from Phone Web Page

### Before you begin

Step 1

On the phone web page, select Voice > System .

Step 2

Under the section System Configuration , locate the parameter User Password , and click Change Password next to the parameter.

Step 3

Enter your current password in the Old Password field.

If you don't have a password, keep the field empty.

Step 4

Enter your new password in the New Password field.

Step 5

Click Submit .

The message Password has been changed successfully. will display in the web page.

## Set up the Profile Account

You need to enter the authentication credentials to resynchronize your phone with the provisioning profile when prompted with
                              the Profile account setup screen.

If you missed the Profile account setup screen, you can also access it from the phone menu or the Setup softkey if available.

If the phone fails to sign in, contact your administrator.

### Before you begin

Your administrator specifies the profile authentication type on your phone and provides you with the authentication credentials.

Step 1

Press Applications .

Step 2

Select Device administration > Profile account setup .

Step 3

Press Sign in to save your username and password.

If any of the Username field or the Password field is empty, the phone displays a grey Sign in softkey and you can't press the softkey.

If any of the Username field or the Password field is empty, the Sign in softkey doesn't appear. After you enter values in both the fileds you see the Sign in softkey.

Step 4

(Optional) Enter a new username and password if you want to login with another set of credentials.

## Add Multiple Locations for a BroadWorks XSI User

### Before you begin

Step 1

Press Applications .

Step 2

Select User preferences > Call preferences .

Step 3

Select Anywhere .

Step 4

(Optional) Select a line if  BroadWorks Anywhere is configured on multiple lines.

Step 5

Add contact number and name in the Locations screen.

Maximum length of a name that you can enter is 25. You can also keep the Name field empty.

Maximum length of a number that you can enter is 20.

Step 6

Enable or disable the location.

Step 7

Press Save to add the locations to the Locations list.

## Enable Anonymous Call Blocking from the Phone Web Page

Step 1

On the phone web page, select User Login > Voice > User .

Step 2

Under Supplementary Services , set Block ANC Setting to Yes .

The setting applies to all lines, except for the ones where your administrator has enabled synchronization of Anonymous Call
                                          Rejection between the lines and the BroadSoft XSI service.

Step 3

Click Submit All Changes .

## Enable Call Waiting from the Phone Web Page

Step 1

On the phone web page, select User Login > Voice > User .

Step 2

Under Supplementary Services , set CW Setting to Yes .

The setting applies to all lines, except for the ones where your administrator has enabled synchronization of Call Waiting
                                          between the lines and the BroadSoft XSI service.

Step 3

Click Submit All Changes .

## Reboot Your Phone

Step 1

Press Applications .

Step 2

Select Device administration > Restart .

Step 3

Select OK to confirm that you want to reboot your phone.

| Step 1 | Press Applications . |
|---|---|
| Step 2 | Select User preferences > Ringtone > Ext (n) - Ring tone , where n= extension number. |
| Step 3 | Scroll through the list of ringtones and press Play to hear a sample. |
| Step 4 | Press Select and then Set to save a selection. |

| Step 1 | On the phone web page, select User Login > Voice > Ext(n) , where (n) is the number of an extension. |
|---|---|
| Step 2 | In Call Feature Settings area, choose a ringtone from the Default Ring drop-down list. If you don't want to specify a ringtone for the phone line, choose No ring . Your phone doesn't ring when receiving an incoming call. |
| Step 3 | Click Submit All Changes . |

| To control the ringer volume do one of the following. On the phone, press the Volume or button to reduce or to increase the volume. Note When your administrator restricts your ability to control the ringer volume, a message appears indicating that you have no
                                                         permission to change the ringer volume. On the phone administration web page, access the User Login > Advanced and then select Voice > User > Audio Volume . Enter a value for the Ringer Volume parameter and click Submit All Changes . The valid value for the Ringer Volume parameter ranges from 0 to 15. Note When your administrator restricts your ability to control the ringer volume, the Ringer Volume parameter doesn't appear under the Audio Volume section. | Note | When your administrator restricts your ability to control the ringer volume, a message appears indicating that you have no
                                                         permission to change the ringer volume. | Note | When your administrator restricts your ability to control the ringer volume, the Ringer Volume parameter doesn't appear under the Audio Volume section. |
|---|---|---|---|---|
| Note | When your administrator restricts your ability to control the ringer volume, a message appears indicating that you have no
                                                         permission to change the ringer volume. |
| Note | When your administrator restricts your ability to control the ringer volume, the Ringer Volume parameter doesn't appear under the Audio Volume section. |

| Note | When your administrator restricts your ability to control the ringer volume, a message appears indicating that you have no
                                                         permission to change the ringer volume. |
|---|---|

| Note | When your administrator restricts your ability to control the ringer volume, the Ringer Volume parameter doesn't appear under the Audio Volume section. |
|---|---|

| Step 1 | Press Applications . |
|---|---|
| Step 2 | Select User preferences > Call preferences > Call forwarding to access the Call forward settings screen. |
| Step 3 | Select a call forward service. Forward all —Determines whether to forward all incoming calls to a target phone number. Forward busy —Determines whether to forward an incoming call to a target phone number when the line is busy. Forward no answer —Determines whether to forward an incoming call to a target phone number when the call isn't answered. |
| Step 4 | Enable the call forward service by pressing Select button of the Navigation cluster . |
| Step 5 | Assign a target phone number for the call forward service. Forward all number —Specifies the target phone number to which you want to forward all incoming calls. Forward busy number —Specifies the target phone number to which you want to forward the incoming call when the line is busy. Fwd no answer number —Specifies the target phone number to which you want to forward the coming call when the call isn't answered. Fwd no answer delay —Assigns a response delay time for the no answer scenario. Note If your administrator disables the feature key synchronization (FKS) and XSI sync for call forward on your phone, you can enter the value as number of seconds after which call needs to be forwarded. If your administrator enables FKS or XSI sync for call forward on your phone, you can enter the value as number of rings after which call needs to be forwarded. The call forward settings on the phone take effect only when FKS and XSI are disabled. For more information, consult your
                                          administrator. | Note | If your administrator disables the feature key synchronization (FKS) and XSI sync for call forward on your phone, you can enter the value as number of seconds after which call needs to be forwarded. If your administrator enables FKS or XSI sync for call forward on your phone, you can enter the value as number of rings after which call needs to be forwarded. |
| Note | If your administrator disables the feature key synchronization (FKS) and XSI sync for call forward on your phone, you can enter the value as number of seconds after which call needs to be forwarded. If your administrator enables FKS or XSI sync for call forward on your phone, you can enter the value as number of rings after which call needs to be forwarded. |
| Step 6 | (Optional) Assign a target phone number by using the Contacts softkey. In the Call forward settings screen, select any of the call forward service. Select Forward all number , Forward busy number , or Fwd no answer number based on the call forward service that you selected, then press the Contacts softkey. Search for a contact. For more information, see Search for a Contact in the All Directories Screen . Press Call to assign the target phone number. You can find that the target phone number displays next to the call forward service. |
| Step 7 | Press Set to apply the settings. |
| Step 8 | Verify if the setting takes effect by looking for the call forward icon. The icon displays with a target number on the top left or middle of the phone screen. After you enable any of the call forward services, the Forward or Forward all softkey changes to the Clr fwd or Clf fwd all respectively . You can press the softkey to disable the call forward service or services, while the target phone number still remains. Clf fwd all disables only the Call Forward All service, Clf fwd disables all call forward services. If the call forward settings on the phone don't take effect, consult your administrator. |

| Note | If your administrator disables the feature key synchronization (FKS) and XSI sync for call forward on your phone, you can enter the value as number of seconds after which call needs to be forwarded. If your administrator enables FKS or XSI sync for call forward on your phone, you can enter the value as number of rings after which call needs to be forwarded. |
|---|---|

| Step 1 | Select a phone line using the Navigation cluster. |
|---|---|
| Step 2 | Press Applications . |
| Step 3 | Select User preferences > Call preferences > Do not disturb . Note If the Do not disturb menu doesn't display on the screen, contact your administrator. | Note | If the Do not disturb menu doesn't display on the screen, contact your administrator. |
| Note | If the Do not disturb menu doesn't display on the screen, contact your administrator. |
| Step 4 | Select On to turn on DND or select Off to turn off DND. |
| Step 5 | Press Set to save the setting. |

| Note | If the Do not disturb menu doesn't display on the screen, contact your administrator. |
|---|---|

| Step 1 | On the phone web page, select User Login > Voice > User . |
|---|---|
| Step 2 | Under Supplementary Services , set DND Settings to Yes . |
| Step 3 | Click Submit All Changes . |

| Step 1 | Press the Navigation cluster up or down to select a phone line. |
|---|---|
| Step 2 | Press Applications . |
| Step 3 | Select User preferences > Call preferences > Block anonymous call . |
| Step 4 | Select On if you want to block the call that does not have caller information, or select Off to allow the call. |
| Step 5 | Press Set to save the setting. |

| Step 1 | Press Applications . |
|---|---|
| Step 2 | Select User preferences > Call preferences . |
| Step 3 | Select Block caller ID . |
| Step 4 | Press Select to toggle caller ID blocking on or off. If your administrator enables the block caller ID feature on the XSI BroadWorks server, your phone retrieves the value from
                                          the server and you see the value that your administrator sets on the server. You can then modify the value from the Block caller ID menu on the phone. |
| Step 5 | Press Set to save the change. |

| Step 1 | Press Applications . |
|---|---|
| Step 2 | Select User preferences > Call preferences > Secure call . |
| Step 3 | Select On to enable secure call feature or select Off to disable the secure call feature. |
| Step 4 | Press Set to save the setting. |

| Step 1 | Press Applications . |
|---|---|
| Step 2 | Select User preferences > Call preferences > Auto answer page . |
| Step 3 | Select On to enable the Auto answer page or select Off to disable Auto answer page. |
| Step 4 | Press Set to save the changes. |

| Step 1 | Press the Navigation cluster up or down to select a phone line. |
|---|---|
| Step 2 | Press Applications . |
| Step 3 | Select User preferences > Call preferences > Call waiting . |
| Step 4 | Select On to allow you to answer an incoming call that rings while on another call, or select Off to disable the function. |
| Step 5 | Press Set to save the setting. |

| Step 1 | Press Applications . |
|---|---|
| Step 2 | Select User preferences > Call preferences > Voice mail . |
| Step 3 | Enter a phone number to check voicemail. If you press the Messages button, it dials the voicemail number and displays the voice message list. |
| Step 4 | Press Set to confirm the assigned number. |
| Step 5 | Press Back to exit. |

| Step 1 | Select Network configuration > HTTP proxy settings > Proxy mode . |
|---|---|
| Step 2 | Press the Select button of the navigation cluster to choose Auto . |
| Step 3 | Highlight Auto discovery (WPAD) , select On to turn on Web Proxy Auto-Discovery (WPAD) that is used to retrieve a PAC file automatically, select Off to turn off WPAD. By default, your phone uses WPAD in the auto proxy mode. |
| Step 4 | (Optional) If you turn off WPAD in the previous step, you need to further enter a valid Proxy Auto-Configuration (PAC) URL in PAC URL . For example: http://proxy.department.branch.example.com/pac If you don't have the PAC URL, contact your administrator. |
| Step 5 | Press Set to apply the settings. |

| Step 1 | Select Network configuration > HTTP proxy settings > Proxy mode . |
|---|---|
| Step 2 | Press the Select button of the navigation cluster to choose Manual . |
| Step 3 | Enter a valid hostname or IP address of a proxy server in Proxy host . Note Do not provide the scheme ( http:// or https:// ) for the proxy host. | Note | Do not provide the scheme ( http:// or https:// ) for the proxy host. |
| Note | Do not provide the scheme ( http:// or https:// ) for the proxy host. |
| Step 4 | Enter a valid server port of the specified proxy server in Proxy port . |
| Step 5 | (Optional) If your proxy server requires authentication, highlight Proxy authentication and then select On . |
| Step 6 | (Optional) Enter your username and password to access the proxy server. If you don't have the username and password, contact your administrator. |
| Step 7 | Press Set to apply the settings. |

| Note | Do not provide the scheme ( http:// or https:// ) for the proxy host. |
|---|---|

| Step 1 | On the phone web page, select Voice > System . |
|---|---|
| Step 2 | Under the section HTTP Proxy Settings , set the parameters described in the following table: Table 1. HTTP Proxy Settings Parameter Description Proxy Mode Choose the proxy mode for the HTTP proxy setting. Options are: Auto Manual Off Default: Off Use Auto Discovery (WPAD) Select Yes to use the Web Proxy Auto-Discovery (WPAD) mechanism to automatically retrieve a Proxy Auto-Configuration (PAC) file. If the parameter is set to No , you must configure PAC URL . This parameter is available when you set Proxy Mode to Auto . Default: Yes PAC URL URL locating the PAC file. This parameter is available when you set Proxy Mode to Auto and Use Auto Discovery (WPAD) to No . Proxy Host Server address (hostname or IP address) of the proxy server. Do not provide the scheme ( http:// or https:// ). This parameter is available when you set Proxy Mode to Manual . Proxy Port Port number of the proxy server. This parameter is available when you set Proxy Mode to Manual . Proxy Server Requires Authentication If your proxy server requires authentication, select Yes . Otherwise, select No . The parameter configuration depends on the actual behaviour of the proxy server. This parameter is available when you set Proxy Mode to Manual . Username Enter a username of a credential user on the proxy server. This parameter is available when you set Proxy Mode to Manual and Proxy Server Requires Authentication to Yes . Password Enter a password of the specified username for the proxy authentication purpose. This parameter is available when you set Proxy Mode to Manual and Proxy Server Requires Authentication to Yes . | Parameter | Description | Proxy Mode | Choose the proxy mode for the HTTP proxy setting. Options are: Auto Manual Off Default: Off | Use Auto Discovery (WPAD) | Select Yes to use the Web Proxy Auto-Discovery (WPAD) mechanism to automatically retrieve a Proxy Auto-Configuration (PAC) file. If the parameter is set to No , you must configure PAC URL . This parameter is available when you set Proxy Mode to Auto . Default: Yes | PAC URL | URL locating the PAC file. This parameter is available when you set Proxy Mode to Auto and Use Auto Discovery (WPAD) to No . | Proxy Host | Server address (hostname or IP address) of the proxy server. Do not provide the scheme ( http:// or https:// ). This parameter is available when you set Proxy Mode to Manual . | Proxy Port | Port number of the proxy server. This parameter is available when you set Proxy Mode to Manual . | Proxy Server Requires Authentication | If your proxy server requires authentication, select Yes . Otherwise, select No . The parameter configuration depends on the actual behaviour of the proxy server. This parameter is available when you set Proxy Mode to Manual . | Username | Enter a username of a credential user on the proxy server. This parameter is available when you set Proxy Mode to Manual and Proxy Server Requires Authentication to Yes . | Password | Enter a password of the specified username for the proxy authentication purpose. This parameter is available when you set Proxy Mode to Manual and Proxy Server Requires Authentication to Yes . |
| Parameter | Description |
| Proxy Mode | Choose the proxy mode for the HTTP proxy setting. Options are: Auto Manual Off Default: Off |
| Use Auto Discovery (WPAD) | Select Yes to use the Web Proxy Auto-Discovery (WPAD) mechanism to automatically retrieve a Proxy Auto-Configuration (PAC) file. If the parameter is set to No , you must configure PAC URL . This parameter is available when you set Proxy Mode to Auto . Default: Yes |
| PAC URL | URL locating the PAC file. This parameter is available when you set Proxy Mode to Auto and Use Auto Discovery (WPAD) to No . |
| Proxy Host | Server address (hostname or IP address) of the proxy server. Do not provide the scheme ( http:// or https:// ). This parameter is available when you set Proxy Mode to Manual . |
| Proxy Port | Port number of the proxy server. This parameter is available when you set Proxy Mode to Manual . |
| Proxy Server Requires Authentication | If your proxy server requires authentication, select Yes . Otherwise, select No . The parameter configuration depends on the actual behaviour of the proxy server. This parameter is available when you set Proxy Mode to Manual . |
| Username | Enter a username of a credential user on the proxy server. This parameter is available when you set Proxy Mode to Manual and Proxy Server Requires Authentication to Yes . |
| Password | Enter a password of the specified username for the proxy authentication purpose. This parameter is available when you set Proxy Mode to Manual and Proxy Server Requires Authentication to Yes . |
| Step 3 | Click Submit All Changes . |

| Parameter | Description |
|---|---|
| Proxy Mode | Choose the proxy mode for the HTTP proxy setting. Options are: Auto Manual Off Default: Off |
| Use Auto Discovery (WPAD) | Select Yes to use the Web Proxy Auto-Discovery (WPAD) mechanism to automatically retrieve a Proxy Auto-Configuration (PAC) file. If the parameter is set to No , you must configure PAC URL . This parameter is available when you set Proxy Mode to Auto . Default: Yes |
| PAC URL | URL locating the PAC file. This parameter is available when you set Proxy Mode to Auto and Use Auto Discovery (WPAD) to No . |
| Proxy Host | Server address (hostname or IP address) of the proxy server. Do not provide the scheme ( http:// or https:// ). This parameter is available when you set Proxy Mode to Manual . |
| Proxy Port | Port number of the proxy server. This parameter is available when you set Proxy Mode to Manual . |
| Proxy Server Requires Authentication | If your proxy server requires authentication, select Yes . Otherwise, select No . The parameter configuration depends on the actual behaviour of the proxy server. This parameter is available when you set Proxy Mode to Manual . |
| Username | Enter a username of a credential user on the proxy server. This parameter is available when you set Proxy Mode to Manual and Proxy Server Requires Authentication to Yes . |
| Password | Enter a password of the specified username for the proxy authentication purpose. This parameter is available when you set Proxy Mode to Manual and Proxy Server Requires Authentication to Yes . |

| Step 1 | Press Applications . |
|---|---|
| Step 2 | Select Network configuration > VPN settings . |
| Step 3 | Enter the IP address or FQDN of a VPN server in VPN server . |
| Step 4 | Enter the user credentials in Username and Password . |
| Step 5 | (Optional) If needed, enter the name of a tunnel group in Tunnel group . If the field is empty, this means no tunnel group is used for this VPN connection. |
| Step 6 | Highlight Connect to VPN on bootup , press the Select button of the navigation cluster to select On . |
| Step 7 | Press Set to save the settings. The VPN settings are finished. For information about how to enable the VPN connection, see Enable a VPN Connection . |

| Step 1 | Press Applications . |
|---|---|
| Step 2 | Select Network configuration > VPN settings . |
| Step 3 | Highlight Enable VPN connection , press the Select button of the navigation cluster to select On to apply the changes. Note Once you set Enable VPN connection to On , the phone immediately tries to connect to the VPN server. During the process, the phone reboots automatically. The VPN connection takes about one minute. After your phone reboots, the VPN connection icon on the upper-right corner of the phone screen indicates that the VPN connection is established successfully. If the VPN connection fails, the value of Enable VPN connection remains Off . | Note | Once you set Enable VPN connection to On , the phone immediately tries to connect to the VPN server. During the process, the phone reboots automatically. |
| Note | Once you set Enable VPN connection to On , the phone immediately tries to connect to the VPN server. During the process, the phone reboots automatically. |
| Step 4 | (Optional) View the details of the VPN connection. For example, the current VPN connection status and VPN IP address. For details, see View the VPN Status . |

| Note | Once you set Enable VPN connection to On , the phone immediately tries to connect to the VPN server. During the process, the phone reboots automatically. |
|---|---|

| Step 1 | Press Applications . |
|---|---|
| Step 2 | Select Network configuration > VPN settings . |
| Step 3 | Highlight Connect to VPN on bootup , press the Select button of the navigation cluster to select Off . |
| Step 4 | Press Set to save the setting. |
| Step 5 | Do one of the following actions: Highlight Enable VPN connection , select Off . Note Once you set Enable VPN connection to Off , the phone immediately tries to disconnect from the VPN server. During the process, the phone reboots automatically. Manually reboot your phone, see Reboot Your Phone . The VPN disconnection takes about one minute. After the phone reboots, the VPN connection icon on the phone screen disappears. This means that the VPN connection is disabled successfully. | Note | Once you set Enable VPN connection to Off , the phone immediately tries to disconnect from the VPN server. During the process, the phone reboots automatically. |
| Note | Once you set Enable VPN connection to Off , the phone immediately tries to disconnect from the VPN server. During the process, the phone reboots automatically. |
| Step 6 | (Optional) Check whether the VPN connection is Disconnected . For details, see View the VPN Status . |

| Note | Once you set Enable VPN connection to Off , the phone immediately tries to disconnect from the VPN server. During the process, the phone reboots automatically. |
|---|---|

| Step 1 | On the phone web page, select Voice > System . |
|---|---|
| Step 2 | Under the section VPN Settings , set the parameters described in the following table. Table 2. VPN Settings Parameter Description VPN Server IP address or FQDN of the VPN server. Default: Empty VPN User Name Enter a username for a credential user on the VPN server. Default: Empty VPN Password Enter a password of the specified username to access the VPN server. Default: Empty VPN Tunnel Group Enter a tunnel group assigned to the VPN user. Tunnel group is used to identify the group policy for the VPN connection. Default: Empty Connect on Bootup Choose whether your phone connects to the VPN server automatically after the phone reboots. Default: No | Parameter | Description | VPN Server | IP address or FQDN of the VPN server. Default: Empty | VPN User Name | Enter a username for a credential user on the VPN server. Default: Empty | VPN Password | Enter a password of the specified username to access the VPN server. Default: Empty | VPN Tunnel Group | Enter a tunnel group assigned to the VPN user. Tunnel group is used to identify the group policy for the VPN connection. Default: Empty | Connect on Bootup | Choose whether your phone connects to the VPN server automatically after the phone reboots. Default: No |
| Parameter | Description |
| VPN Server | IP address or FQDN of the VPN server. Default: Empty |
| VPN User Name | Enter a username for a credential user on the VPN server. Default: Empty |
| VPN Password | Enter a password of the specified username to access the VPN server. Default: Empty |
| VPN Tunnel Group | Enter a tunnel group assigned to the VPN user. Tunnel group is used to identify the group policy for the VPN connection. Default: Empty |
| Connect on Bootup | Choose whether your phone connects to the VPN server automatically after the phone reboots. Default: No |
| Step 3 | Click Submit All Changes to save the changes. The VPN settings are finished. For information about how to enable the VPN connection, see Enable a VPN Connection . |

| Parameter | Description |
|---|---|
| VPN Server | IP address or FQDN of the VPN server. Default: Empty |
| VPN User Name | Enter a username for a credential user on the VPN server. Default: Empty |
| VPN Password | Enter a password of the specified username to access the VPN server. Default: Empty |
| VPN Tunnel Group | Enter a tunnel group assigned to the VPN user. Tunnel group is used to identify the group policy for the VPN connection. Default: Empty |
| Connect on Bootup | Choose whether your phone connects to the VPN server automatically after the phone reboots. Default: No |

| Step 1 | Press Applications . |
|---|---|
| Step 2 | Select Status > VPN status . You can view the following information: VPN connection —Indicates whether the phone connects to the VPN server. The status can be either Connected or Disconnected . VPN IP address —VPN IP address assigned from the VPN server. VPN subnet mask —VPN subnet mask assigned from the VPN server. Sent bytes —Total bytes the phone sent out to the network through the VPN server. Received bytes —Total bytes the phone received from the network through the VPN server. |

| Step 1 | Press Applications . |
|---|---|
| Step 2 | Select User preferences > Attendant console preferences > Display mode . The following options are available: Name Ext Both |
| Step 3 | Choose the display mode and press Set . |

| Step 1 | Press Applications . |
|---|---|
| Step 2 | Select Device administration > Date/Time > Time format . To set daylight savings, select Device administration > Date/Time > Daylight savings . Select On to turn on the daylight savings and select Off to turn it off. |
| Step 3 | (Optional) Select Device administration > Date/Time > Time zone . |
| Step 4 | Select a time format and press Set to apply the changes. |

| Step 1 | Press Applications . |
|---|---|
| Step 2 | Select Device administration > Date/Time > Date format . |
| Step 3 | Select a date format and press Set to apply the changes. |

| Step 1 | Press Applications . |
|---|---|
| Step 2 | Select User preferences > Screen preferences > Screen saver . |
| Step 3 | Select On to turn on screen saver and select Off to turn it off. |
| Step 4 | Select Screen saver settings to choose the settings: Screen saver type —Choose one of the following options: Clock —Displays a rounded clock with the wallpaper in the background. Download Picture —Displays a picture pushed from the phone web page. Logo : Displays a logo as the phone screensaver. This image is added in the Logo URL field of the pone web page. Lock —Displays a lock icon on the phone screen wallpaper. Trigger interval —Enter the number of seconds that the phone remains idle before the screen saver turns on. Refresh interval —Enter the number of seconds before the screen saver should refresh (if, for example, you chose a rotation of pictures). |
| Step 5 | Press Set . |

| Step 1 | On the phone web page, select Voice > User . |
|---|---|
| Step 2 | In the Screen section, set up the fields as described in the following table. Parameter Description Screen Saver Enable Select Yes to enable a screen saver on the phone. When the phone is idle for a specified time, it enters screen saver mode. Default: No Screen Saver Type Types of screen saver. Options you can choose: Clock —Displays a digital clock on a plain background. Download Picture —Displays a picture pushed from the phone webpage. Logo : Displays a logo on the phone screen. Add a logo image in the Logo URL field. Lock —Enables locking of the screensaver. Screen Saver Wait Amount of idle time before screen saver displays. Enter the number of seconds of idle time to elapse before the screen saver starts. Default: 300 Picture Download URL URL locating the (.png) file to display on the phone screen background. If you select picture as as screensaver type, this
                                                      image displays as a screensaver on the phone screen. When you enter an incorrect URL to download a new wallpaper, the phone fails to upgrade to the newer wallpaper and displays
                                                      the existing downloaded wallpaper. If the phone does not have any wallpaper downloaded earlier, it displays a gray screen. Logo URL Enter a URL or path for the location where the logo image is saved. If you select logo as as screensaver type, this image
                                                      displays as a screensaver on the phone screen. | Parameter | Description | Screen Saver Enable | Select Yes to enable a screen saver on the phone. When the phone is idle for a specified time, it enters screen saver mode. Default: No | Screen Saver Type | Types of screen saver. Options you can choose: Clock —Displays a digital clock on a plain background. Download Picture —Displays a picture pushed from the phone webpage. Logo : Displays a logo on the phone screen. Add a logo image in the Logo URL field. Lock —Enables locking of the screensaver. | Screen Saver Wait | Amount of idle time before screen saver displays. Enter the number of seconds of idle time to elapse before the screen saver starts. Default: 300 | Picture Download URL | URL locating the (.png) file to display on the phone screen background. If you select picture as as screensaver type, this
                                                      image displays as a screensaver on the phone screen. When you enter an incorrect URL to download a new wallpaper, the phone fails to upgrade to the newer wallpaper and displays
                                                      the existing downloaded wallpaper. If the phone does not have any wallpaper downloaded earlier, it displays a gray screen. | Logo URL | Enter a URL or path for the location where the logo image is saved. If you select logo as as screensaver type, this image
                                                      displays as a screensaver on the phone screen. |
| Parameter | Description |
| Screen Saver Enable | Select Yes to enable a screen saver on the phone. When the phone is idle for a specified time, it enters screen saver mode. Default: No |
| Screen Saver Type | Types of screen saver. Options you can choose: Clock —Displays a digital clock on a plain background. Download Picture —Displays a picture pushed from the phone webpage. Logo : Displays a logo on the phone screen. Add a logo image in the Logo URL field. Lock —Enables locking of the screensaver. |
| Screen Saver Wait | Amount of idle time before screen saver displays. Enter the number of seconds of idle time to elapse before the screen saver starts. Default: 300 |
| Picture Download URL | URL locating the (.png) file to display on the phone screen background. If you select picture as as screensaver type, this
                                                      image displays as a screensaver on the phone screen. When you enter an incorrect URL to download a new wallpaper, the phone fails to upgrade to the newer wallpaper and displays
                                                      the existing downloaded wallpaper. If the phone does not have any wallpaper downloaded earlier, it displays a gray screen. |
| Logo URL | Enter a URL or path for the location where the logo image is saved. If you select logo as as screensaver type, this image
                                                      displays as a screensaver on the phone screen. |
| Step 3 | Click Submit All Changes . |

| Parameter | Description |
|---|---|
| Screen Saver Enable | Select Yes to enable a screen saver on the phone. When the phone is idle for a specified time, it enters screen saver mode. Default: No |
| Screen Saver Type | Types of screen saver. Options you can choose: Clock —Displays a digital clock on a plain background. Download Picture —Displays a picture pushed from the phone webpage. Logo : Displays a logo on the phone screen. Add a logo image in the Logo URL field. Lock —Enables locking of the screensaver. |
| Screen Saver Wait | Amount of idle time before screen saver displays. Enter the number of seconds of idle time to elapse before the screen saver starts. Default: 300 |
| Picture Download URL | URL locating the (.png) file to display on the phone screen background. If you select picture as as screensaver type, this
                                                      image displays as a screensaver on the phone screen. When you enter an incorrect URL to download a new wallpaper, the phone fails to upgrade to the newer wallpaper and displays
                                                      the existing downloaded wallpaper. If the phone does not have any wallpaper downloaded earlier, it displays a gray screen. |
| Logo URL | Enter a URL or path for the location where the logo image is saved. If you select logo as as screensaver type, this image
                                                      displays as a screensaver on the phone screen. |

| Step 1 | On the phone web page, select User Login > Voice > User . |
|---|---|
| Step 2 | In the Screen section, select Logo from the Phone Background field and in the Logo URL field enter a URL or path for the location where the logo image is saved. |
| Step 3 | Click Submit All Changes . After the logo is added in the phone background, if you select Default from the Phone Background list and save the changes, the logo icon on the phone screen will disappear. |

| Step 1 | Press Applications . |
|---|---|
| Step 2 | Select User preferences > Screen preferences > Contrast level . |
| Step 3 |  |
| Step 4 | Press Save . |

| Step 1 | Press Applications . |
|---|---|
| Step 2 | Select User preferences > Backlight timer . |
| Step 3 | Press Edit to change the backlight mode. |
| Step 4 | Press On to turn the backlight on or press Off to turn the backlight off. You can also select a time from the list to set a duration for which the backlight will remain on. |
| Step 5 | (Optional) Select a time from the list to set a duration that the backlight remains off. You can also select the option to set the backlight always on. |
| Step 6 | Press Select to apply the selected backlight mode. |

| Step 1 | On the phone web page, select User Login > Advanced > Voice > User . |
|---|---|
| Step 2 | Under Screen , select a duration for the Back Light Timer parameter. |
| Step 3 | In the LCD Contrast field, enter a number for the desired brightness. |

| Step 1 | Press Applications . |
|---|---|
| Step 2 | Select User preferences > Audio preferences > Preferred audio device . |
| Step 3 | Press Select to choose one of the options: None —Selects the last used audio device. Speaker —Selects the speakerphone as the audio device. Headset —Selects a headset as the audio device. |
| Step 4 | Press Set to save the selection. |

| Step 1 | Press Applications . |
|---|---|
| Step 2 | Select Device administration > Language . |
| Step 3 | Select a language from the list of available languages. |
| Step 4 | Select Save . |

| Step 1 | Press Applications . |
|---|---|
| Step 2 | Select Device administration > Set password . |
| Step 3 | Enter your current password in the Old password field. |
| Step 4 | Enter your new password in the New password  and the Reenter new password fields. |
| Step 5 | Select Save . |

| Step 1 | On the phone web page, select Voice > System . |
|---|---|
| Step 2 | Under the section System Configuration , locate the parameter User Password , and click Change Password next to the parameter. |
| Step 3 | Enter your current password in the Old Password field. If you don't have a password, keep the field empty. |
| Step 4 | Enter your new password in the New Password field. |
| Step 5 | Click Submit . The message Password has been changed successfully. will display in the web page. |

| Step 1 | Press Applications . |
|---|---|
| Step 2 | Select Device administration > Profile account setup . Your username and password are automatically filled. These fields are blank if your username and password were not added before. |
| Step 3 | Press Sign in to save your username and password. Note If any of the Username field or the Password field is empty, the phone displays a grey Sign in softkey and you can't press the softkey. If any of the Username field or the Password field is empty, the Sign in softkey doesn't appear. After you enter values in both the fileds you see the Sign in softkey. | Note | If any of the Username field or the Password field is empty, the phone displays a grey Sign in softkey and you can't press the softkey. If any of the Username field or the Password field is empty, the Sign in softkey doesn't appear. After you enter values in both the fileds you see the Sign in softkey. |
| Note | If any of the Username field or the Password field is empty, the phone displays a grey Sign in softkey and you can't press the softkey. If any of the Username field or the Password field is empty, the Sign in softkey doesn't appear. After you enter values in both the fileds you see the Sign in softkey. |
| Step 4 | (Optional) Enter a new username and password if you want to login with another set of credentials. |

| Note | If any of the Username field or the Password field is empty, the phone displays a grey Sign in softkey and you can't press the softkey. If any of the Username field or the Password field is empty, the Sign in softkey doesn't appear. After you enter values in both the fileds you see the Sign in softkey. |
|---|---|

| Step 1 | Press Applications . |
|---|---|
| Step 2 | Select User preferences > Call preferences . |
| Step 3 | Select Anywhere . |
| Step 4 | (Optional) Select a line if  BroadWorks Anywhere is configured on multiple lines. |
| Step 5 | Add contact number and name in the Locations screen. Maximum length of a name that you can enter is 25. You can also keep the Name field empty. Maximum length of a number that you can enter is 20. |
| Step 6 | Enable or disable the location. |
| Step 7 | Press Save to add the locations to the Locations list. |

| Step 1 | On the phone web page, select User Login > Voice > User . |
|---|---|
| Step 2 | Under Supplementary Services , set Block ANC Setting to Yes . The setting applies to all lines, except for the ones where your administrator has enabled synchronization of Anonymous Call
                                          Rejection between the lines and the BroadSoft XSI service. |
| Step 3 | Click Submit All Changes . |

| Step 1 | On the phone web page, select User Login > Voice > User . |
|---|---|
| Step 2 | Under Supplementary Services , set CW Setting to Yes . The setting applies to all lines, except for the ones where your administrator has enabled synchronization of Call Waiting
                                          between the lines and the BroadSoft XSI service. |
| Step 3 | Click Submit All Changes . |

| Step 1 | Press Applications . |
|---|---|
| Step 2 | Select Device administration > Restart . |
| Step 3 | Select OK to confirm that you want to reboot your phone. |