---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cuipph-mpp-8800-english-userguide-p881-b-8800-3pcc-user-guide-p881-b-8800-3p-56906b6d84
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cuipph/MPP/8800/english/userguide/p881_b_8800-3pcc-user-guide/p881_b_8800-3pcc-user-guide-110_chapter_0110.html
retrieved_at: 2026-08-21T02:35:50.820017+00:00
---

Cisco IP Phone 8800 Series Multiplatform Phones User Guide

# Cisco IP Phone 8800 Series Multiplatform Phones User Guide

Updated: November 19, 2025

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

## Enable Call
                        	 Forwarding with the Phone Web Page

Step 1

On the phone web page, click User
                                             				  Login > advanced > Voice > User .

Step 2

Under Call Forward , choose Yes for CFWD Setting.

Step 3

Click Submit All Changes.

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

You can turn on DND on for all lines if your administrator hasn't enabled feature key sync (FKS).

Step 3

Click Submit All Changes .

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

## Enable Call Waiting from the Phone Web Page

Step 1

On the phone web page, select User Login > Voice > User .

Step 2

Under Supplementary Services , set CW Setting to Yes .

The setting applies to all lines, except for the ones where your administrator has enabled synchronization of Call Waiting
                                          between the lines and the BroadSoft XSI service.

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

## Enable Anonymous Call Blocking from the Phone Web Page

Step 1

On the phone web page, select User Login > Voice > User .

Step 2

Under Supplementary Services , set Block ANC Setting to Yes .

The setting applies to all lines, except for the ones where your administrator has enabled synchronization of Anonymous Call
                                          Rejection between the lines and the BroadSoft XSI service.

Step 3

Click Submit All Changes .

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

## Enable Dial Assistance

### Before you begin

Step 1

Press Applications .

Step 2

Select User Preferences > Call Preferences > Dial assistance .

Step 3

Press On to enable the dial assistance or press Off to disable it.

Step 4

Press Set to apply the mode.

Step 5

Press Back to return to the Call Preferences screen.

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

## Set Up an Auto Answer Page

Step 1

Press Applications .

Step 2

Select User preferences > Call preferences > Auto answer page .

Step 3

Select On to enable the Auto answer page or select Off to disable Auto answer page.

Step 4

Press Set to save the changes.

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

Press to exit.

Step 6

Press Back to exit.

## HTTP Proxy Settings

You can set up an HTTP proxy on your phone from the HTTP proxy settings menu under the Network configuration menu. The HTTP proxy settings are also available on the phone web page.

### Set Up a Proxy Server with the Auto Proxy Mode

Step 1

Press Applications .

Step 2

Select Network configuration > HTTP proxy settings > Proxy mode .

Step 3

Press the Select button of the navigation cluster to choose Auto .

Step 4

Highlight Auto discovery (WPAD) , select On to turn on Web Proxy Auto-Discovery (WPAD) that is used to retrieve a PAC file automatically, select Off to turn off WPAD.

By default, your phone uses WPAD in the auto proxy mode.

Step 5

(Optional) If you turn off WPAD in the previous step, you need to further enter a valid Proxy Auto-Configuration (PAC) URL in PAC URL . For example:

```
http://proxy.department.branch.example.com/pac
```

If you don't have the PAC URL, contact your administrator.

Step 6

Press Set to apply the settings.

### Set Up a Proxy Server with the Manual Proxy Mode

#### Before you begin

Step 1

Press Applications .

Step 2

Select Network configuration > HTTP proxy settings > Proxy mode .

Step 3

Press the Select button of the navigation cluster to choose Manual .

Step 4

Enter a valid hostname or IP address of a proxy server in Proxy host .

Do not provide the scheme ( http:// or https:// ) for the proxy host.

Step 5

Enter a valid server port of the specified proxy server in Proxy port .

Step 6

(Optional) If your proxy server requires authentication, highlight Proxy authentication and then select On .

Step 7

(Optional) Enter your username and password to access the proxy server.

If you don't have the username and password, contact your administrator.

Step 8

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

## Change Wallpaper from the Phone Page

Your administrator can allow you to change the default wallpaper on your phone to one of the wallpapers available.

Step 1

On the phone web page, select User Login > Voice > User .

Step 2

In the Phone Background field of the Screen section, select any of the options as a phone wallpaper.

Default : Phone does not have any wallpaper. If no wallpaper is added to the phone screen, the phone screen displays monochrome wallpaper.

Download Picture : In the phone web page, you can select the Download Picture as your phone background option. The picture that you add in the Picture Download URL is used as the phone wallpaper.

Phone supports .jpg, and .png image files and the image size can be a maximum of 625 KB. You can scale-up or scale-down the
                                                image so that a picture can fully fit into the screen. If the aspect ratio of the target picture is not 5:3, some parts of
                                                the picture are lost.

Logo : In the phone web page you can select Logo as your phone background option. The logo that you add in the Logo URL is used as the wallpaper.

Caution

Do not exceed a maximum length of 255 characters for the Logo URL or Picture Download URL .

The logo display area is the center of the phone screen. The logo display area size of the phone is 128x128 pixels. If original
                                                logo size does not fit display area, the logo scales to fit the display area.

## Configure the Screen Saver from the Phone Web Page

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

## Change Wallpaper from the Phone Page

Your administrator can allow you to change the default wallpaper on your phone to one of the wallpapers available.

Step 1

On the phone web page, select User Login > Voice > User .

Step 2

In the Phone Background field of the Screen section, select any of the options as a phone wallpaper.

Default : Phone does not have any wallpaper. If no wallpaper is added to the phone screen, the phone screen displays monochrome wallpaper.

Download Picture : In the phone web page, you can select the Download Picture as your phone background option. The picture that you add in the Picture Download URL is used as the phone wallpaper.

Phone supports .jpg, and .png image files and the image size can be a maximum of 625 KB. You can scale-up or scale-down the
                                                image so that a picture can fully fit into the screen. If the aspect ratio of the target picture is not 5:3, some parts of
                                                the picture are lost.

Logo : In the phone web page you can select Logo as your phone background option. The logo that you add in the Logo URL is used as the wallpaper.

Caution

Do not exceed a maximum length of 255 characters for the Logo URL or Picture Download URL .

The logo display area is the center of the phone screen. The logo display area size of the phone is 128x128 pixels. If original
                                                logo size does not fit display area, the logo scales to fit the display area.

## Download Wallpaper

You can download a picture to customize the background on the
                              		  phone screen.

Step 1

On the phone
                                       			 web page, select User Login > Voice > User .

Step 2

In the Screen section, choose Download Picture for the Phone
                                             				  Background field.

Step 3

Upload the
                                       			 custom wallpaper to a TFTP,HTTP, or HTTPS server.

The image is a
                                          				.jpg file. Preferred dimension is 800x480 pixels. If the image is not the
                                          				preferred size, user still can upload it but it will resize to fit the screen.

Step 4

In
                                       			 the Picture
                                          				Download URL field, enter the path where the wallpaper image has
                                       			 been uploaded.

The URL must
                                          				include the TFTP,HTTP, or HTTPS server name (or IP address), directory, and
                                          				filename.

```
http:// 10.64.84.147/pictures/image04_800x480x24.jpg
```

When you enter
                                          				an incorrect URL to download a new wallpaper, the phone fails to upgrade to the
                                          				newer wallpaper and displays the existing downloaded wallpaper. If the phone
                                          				does not have any wallpaper downloaded earlier, it displays a gray screen.

Step 5

Click Submit
                                          				All Changes .

The phone does
                                          				not reboot after you change the background image URL.

## Adjust the Phone Screen Brightness

Step 1

Press Applications .

Step 2

Select User preferences > Screen preferences > Display brightness .

Step 3

Press the Navigation cluster, right or left, to increase or decrease the brightness.

Step 4

Press Save .

## Adjust the Backlight Duration

You can adjust the backlight to make the phone screen easier to read.

Step 1

Press Applications .

Step 2

Select User preferences > Screen preferences > Backlight timer .

Step 3

Press Edit or Select button.

Step 4

Scroll through the list and select a duration for which the backlight remains on:

1 min

5 min

30 min

Always On

Default value is 5 min.

Step 5

Press Set to apply the selection.

## Adjust Backlight Timer from the Phone Web Interface

You
                              		  can save energy by disabling the backlight on each phone at a preset time.

Step 1

Select Voice > User .

Step 2

In the Screen section, select a duration for the Back Light Timer parameter.

```
<Back_Light_Timer ua="rw">30s</Back_Light_Timer>
```

The allowed values are 1m|5m|30m|Always On. The default value is 5m (5 minutes).

Step 3

In the Display Brightness field, enter an integer ranging from 4 to 15 for the desired brightness.

```
<Display_Brightness ua="rw">15</Display_Brightness>
```

The allowed value is an integer ranging from 4 through 15. The bigger the value, the brighter the screen display. The default
                                          value is 15.

Step 4

Click Submit All Changes .

## Change the Display Mode

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

## Specify an Audio Device for a Call

You can connect an analog headset, a Bluetooth headset, and a USB headset simultaneously to your phone. However, you can use
                              only one headset at time.

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

USB (highest)

Bluetooth (medium)

analog headset (lowest)

- Bluetooth —Selects Bluetooth as the audio device. The priority order is Bluetooth (highest), USB (medium), and analog headset (lowest).

Step 4

Press Set to save the selection.

## Reboot Your Phone

Step 1

Press Applications .

Step 2

Select Device administration > Restart .

Step 3

Select OK to confirm that you want to reboot your phone.

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

Step 4

(Optional) Enter a new username and password if you want to login with another set of credentials.

## Executive Settings

If your administrator has configured you as an executive user with a pool of assistants, you can configure the following settings
                           to share control of your calls with your assistants:

You can active or deactivate call filtering. If your extension connects to the XSI BroadWorks server, you can also select
                                 the call filtering mode and type.

When call filtering is on, your incoming calls go to your assistants according to the criteria configured by your administrator
                                 on the BroadWorks server.

You also receive your incoming calls that go to your assistants, if your administrator has enabled call screening for you.

You can check the Opt-in/Opt-out status of your assistants.

The assistants with the Opt-in status have controls of the executive's calls.

Important

The menu items that display on the phone screen are different in the following scenarios:

Your administrator enables the feature key synchronization (FKS) on your extension.

Your administrator connects your extension to the XSI BroadWorks server.

### Activate Call Filtering as an Executive

Perform this task to active call filtering. If your administrator configures your extension to connect to the XSI BroadWorks
                                 server, you can also select the call filtering mode and call filtering type.

When call filtering is active, your incoming calls go to your assistants according to the criteria configured by your administrator.

You also receive your incoming calls that go to your assistants, if your administrator has enabled call screening for you.
                                 When an assistant answers a call, the call doesn't display on your extension.

Important

If you activate DND on your phone, your assistants do not receive your incoming calls.

Dial the service activation code provided by your administrator, or follow the procedure described below to activate call
                                 filtering.

#### Before you begin

Your administrator configures and enables the call filtering criteria on the XSI BroadWorks server.

Step 1

Do one of the following actions:

- If your administrator has programmed the Executive function on a line key, the phone shows the Executive together with the call filtering status ( On or Off ) on the main screen. Press the line key.

Press Applications .

Select Executive .

Step 2

Follow the below procedure according to the actual menus displayed on the phone.

Select Call filter > Call filter .

Press to select On .

Select the call filter mode and the call filter type.

Call filter mode —Choose one of the following options:

Simple —Your incoming calls go to your assistants according to the call filtering criteria configured in the simple mode.

Advanced —Your incoming calls go to your assistants according to the call filtering criteria configured in the advanced mode.

Call filter type —Choose one of the following options:

This menu item is available when the Call filter mode is set to Simple .

All Calls —All your incoming calls go to your assistants.

Internal Calls —If you and the callers are in the same BroadSoft group, their incoming calls go to your assistants.

External Calls —If you and the callers are not in the same BroadSoft group, their incoming calls go to your assistants.

Press Set to apply the changes.

Press the On softkey to activate call filtering.

Press to exit.

### Deactivate Call Filtering as an Executive

When call filtering is off, none of your incoming calls go to your assistants.

Dial the service activation code provided by your administrator, or follow the procedure described below to deactivate call
                                 filtering.

#### Before you begin

Step 1

Do one of the following actions:

- If your administrator has programmed the Executive function on a line key, the phone shows the Executive together with the call filtering status ( On or Off ) on the main screen. Press the line key.

Press Applications .

Select Executive .

Step 2

Follow the below procedure according to the actual menus displayed on the phone.

Select Call filter > Call filter

Press to select Off .

Press Set to apply the changes.

Press the Off softkey to deactivate call filtering.

Press to exit.

### Check Assistant List as an Executive

#### Before you begin

Your administrator has configured your extension to connect to the XSI BroadWorks server. Otherwise, the menu Assistant List doesn't display on the phone.

Your administrator has enabled alphanumeric dialing. Otherwise, you can't make a call to an assistant from the assistant list.

Step 1

Do one of the following actions:

- If your administrator has programmed the Executive function on a line key, the phone shows the Executive together with the call filtering status ( On or Off ) on the main screen. Press the line key.

Press Applications .

Select Executive .

Step 2

Select Assistant List .

The Assistant List screen displays a maximum of 10 assistants on the phone.

If your administrator configures more than one executive on the phone, then the screen only displays the assistants of the
                                             first available executive.

Step 3

(Optional) If you want to make a call to one of your assistants, then highlight the assistant's phone number, and press Call .

## Executive Assistant Settings

If your administrator has configured you as an executive assistant, you can configure the following settings for shared control
                           of the executives' calls:

You can view the associated executives.

You can opt in to or out of an executive's pool of assistants if your administrator has enabled this option for the pool.

If you have opted in to a pool, when you want someone else to answer calls on behalf of executives instead of you, you can
                                 activate call diversion to a number of your choice.

You can deactivate call diversion at any time.

If you have opted in to a pool, you can activate or deactivate call filtering for an executive.

When call filtering is on, you and other assistants associated with the executive receive the executive's incoming calls according
                                 to the criteria configured by your administrator.

Important

The menu items that display on the phone screen are different in the following scenarios:

Your administrator enables the feature key synchronization (FKS) on your extension.

Your administrator connects your extension to the XSI BroadWorks server.

### Opt in to or Out of an Executive's Pool as an Assistant

When you opt in to an executive's pool, you get shared control of the executive's calls.

When you opt out of an executive's pool, you do not have any control of the executive's calls.

If your administrator only enables the feature key synchronization (FSK) on your extension, dial the appropriate service activation
                                 code provided by your administrator to opt in to or out of an executive's pool. Skip the below procedure.

If your administrator has configured your extension to connect to the XSI BroadWorks server, you can either dial the appropriate
                                 service activation code or follow the procedure described below.

#### Before you begin

Your administrator gives you the assistant user privileges and includes you in the executive's pool of assistants.

Your administrator grants you the permission to opt in to or out of the executive's pool.

Step 1

Do one of the following actions:

- If your administrator has programmed the Assistant function on a line key, press the line key.

Press Applications .

Select Assistant .

Step 2

Select Executive List .

Step 3

Select an executive of whose assistant pool that you want to opt in to or out of.

Step 4

Press to select Opt-in to opt in to the executive's pool or select Opt-out to opt out of the executive's pool.

Step 5

Press Set to apply the changes.

### Activate or Deactivate Call Filtering as an Executive Assistant

Access the Call filter screen to activate or deactivate call filtering. The screen shows a list of executives associated with all the assistant
                                 extensions on the phone together with the call filtering status ( On or Off ).

When call filtering is on for an executive, you and other assistants associated with the executive receive the executive's
                                 incoming calls according to the criteria configured by your administrator.

When the executive or another assistant answers a call, you no longer see the call on your extension.

Important

Activating or deactivating call filtering for an executive activates or deactivates the setting for all the assistants in
                                             the executive’s pool.

#### Before you begin

You administrator enables the Call filter menu item on the phone screen.

Step 1

Do one of the following actions:

- If your administrator has programmed the Assistant function on a line key, press the line key.

Press Applications .

Select Assistant .

Step 2

Follow the below procedure according to the actual menus displayed on the phone.

Select Call filter .

Highlight an executive, press to toggle call filtering on or off for the highlighted executive.

Press Set , and then press OK to apply the changes.

Highlight the executive for whom you want to activate or deactivate call filtering.

Press to toggle call filtering on or off for the highlighted executive.

Press to exit.

### Activate Call Diversion as an Executive Assistant

Access the Divert screen to activate call diversion when you want someone else to receive executives' incoming calls.

Important

If you activate DND on your extension, calls are not diverted.

You activate call diversion for an assistant extension. When you activate call diversion for an extension, if you handle multiple
                                 executives on that extension, all of the executives' incoming calls are diverted from that extension.

Other assistants in the executives' pool continue to receive executives' incoming calls.

Other assistant extensions on your phone also continue to receive executives' incoming calls.

#### Before you begin

Step 1

Do one of the following actions:

- If your administrator has programmed the Assistant function on a line key, press the line key.

Press Applications .

Select Assistant .

Step 2

Follow the below procedure according to the actual menus displayed on the phone.

Select Divert > Divert .

Select On to activate call diversion.

Highlight Divert number and enter the destination number to which you want the calls to be diverted.

Press Set to apply the changes.

Typically, the screen shows a list of all the executives associated with all the assistant extensions on the phone. Select
                                                      an executive associated with the extension for which you want to activate call diversion.

The extension with which the selected executive is associated appears at the top.

Press Divert .

Enter the destination number to which you want the calls to be diverted.

Press Call to complete the action.

Press to exit.

If your administrator has programmed the Assistant function on a line key, the icon in the line key label changes to to show that call diversion is on.

If you are the only executive assistant with an extension on the phone, the diversion destination number appears under the Assistant line key.

### Deactivate Call Diversion as an Executive Assistant

#### Before you begin

Step 1

Do one of the following actions:

- If your administrator has programmed the Assistant function on a line key, press the line key.

Press Applications .

Select Assistant .

Step 2

Follow the below procedure according to the actual menus displayed on the phone.

Select Divert > Divert .

Select Off to deactivate call diversion.

Press Set to apply the change.

Press Clr divert .

Press to exit.

If your administrator has programmed the Assistant function on a line key, and call diversion is not on for any other assistant extension on the phone, the icon in the Assistant line key label changes back from to .

### Check Executive List as an Assistant

#### Before you begin

Your administrator has configured your extension to connect to the XSI BroadWorks server.

Step 1

Do one of the following actions:

- If your administrator has programmed the Assistant function on a line key, press the line key.

Press Applications .

Select Assistant .

Step 2

Select Executive List .

The Executive List screen displays a maximum of 10 executives on the phone.

If your administrator configures more than one assistant on the phone, then the screen only displays the executives of the
                                             first available assistant.

### Troubleshooting Executive Assistant Settings

#### Calls Fail Although Call Diversion Is On

Ensure that DND is not activated for your extension.

## Wi-Fi Settings

Wi-Fi settings are available only on Cisco IP phone 8861 and 8865 Multiplatform Phones.

You can customize Wi-Fi settings for your phone from the Wi-Fi configuration menu under the Network configuration menu on the phone. Some of the Wi-Fi settings are also available on the phone web page.

### Connect the Phone to a Wireless Network at the First Boot

The phone automatically scans for available Wi-Fi networks in any of the following situations:

when the phone first boots up without a network connection.

when the phone isn't connected to a network after a factory reset.

A list of available Wi-Fi networks is displayed after the Wi-Fi scan process completes.

Step 1

Select a Wi-Fi network from the list.

You see the following options:

Scan —The phone scans again for available networks.

Setup —Opens the Setup Wi-Fi page.

Skip —You see the message If you skip this step, you will need to configure the network manually . If you confirm to skip the Connect to Wi-Fi page, the Wi-Fi Scan softkey displays.

Step 2

Press Setup and complete the fields.

Step 3

Press Connect .

### Trigger Wi-Fi Scan with Softkey

You can use the Wi-Fi Scan softkey to scan for available wireless networks. The softkey displays on the phone screen in any of the following situations:

when you skip the Wi-Fi connection at the first boot with no wired network connection

whenever the phone loses network connection and the phone Wi-Fi is turned on

Step 1

Press the Wi-Fi Scan softkey when it displays on the phone screen.

Scan —Scans again for available networks.

Select —Opens the Setup Wi-Fi page.

Cancel —Closes the network list.

Step 2

Select a Wi-Fi network from the list.

Step 3

Press Select and complete the fields.

Step 4

(Optional) Press Save to save the setups as a Wi-Fi profile. You can connect to this network later with the profile.

Step 5

Press Connect .

### Turn the Wi-Fi On or Off from the Phone Web Page

You can enable or disable the wireless LAN of your phone from the phone web page. You turn on the Wi-Fi so that the phone
                                 connects to a wireless network automatically or manually. By default, the wireless LAN on your phone is enabled.

Step 1

On the phone web page, select User Login > Advanced > Voice > System .

Step 2

Go to the Wi-Fi Settings section and set the Phone-wifi-on field to Yes .

Step 3

Click Submit All Changes .

### Turn the Wi-Fi On or Off from Your phone

You can enable or disable the wireless LAN of your phone from the Wi-Fi configuration menu. By default, the wireless LAN on your phone is enabled.

Step 1

Press Applications .

Step 2

Select Network configuration > Wi-Fi configuration > Wi-Fi .

Step 3

Press the Select button, to turn the Wi-Fi on or off. You can also press the Navigation cluster, left or right, to turn the Wi-Fi on or off.

Step 4

Press Set to save the changes.

### Connect the Phone to a Wi-Fi Manually

When you set up a Wi-Fi profile, it provides you the options to connect the phone manually to a wireless network. You can
                                 establish the connection from the Wi-Fi profile screen or from the Setup Wi-Fi screen.

The top most Wi-Fi profile in the Wi-Fi profile screen gets connected automatically when the phone provisions.

#### Before you begin

Turn on the Wi-Fi of your phone.

Step 1

Press Applications .

Step 2

Select Network configuration > Wi-Fi configuration > Wi-Fi profile .

Step 3

In the Wi-Fi profile screen, do any of the actions to connect to Wi-Fi.

- Select any of the configured Wi-Fi profile and click Connect .

- Press Scan and select one wireless in the Connect to Wi-Fi screen. In the Setup Wi-Fi screen, enter values in the fields and press Connect .

See the Profile Parameter table in the Set Up a Wi-Fi Profile from the Phone for the field values.

### Connect to a Wi-Fi Network When Your Phone Displays a Connection Failure Message

If your phone supports Wi-Fi, it provides status information if it doesn't have a network connection when it boots up. You
                                 see the message Verify your internet settings or contact your service provider.

#### Before you begin

Step 1

Press Wi-Fi Scan .

Step 2

Press one of these options:

Scan —to scan for networks again.

Select —to configure the highlighted network.

Step 3

Highlight a network from the list.

Step 4

Press Select .

Step 5

Select one of the following options:

Cancel —go back to the previous screen.

Save —save the network with the information you input.

Connect —connect to the selected network.

Step 6

Press Connect .

The steps above also apply if your phone loses its network connection any time after it has booted up, and it's not connected
                                                         to an Ethernet cable.

### Enable or Disable Backward Compatibility with WPA from Your Phone

You can enable or disable backward compatibility with Wi-Fi Protected Access (WPA) from the Wi-Fi configuration menu on your phone. By default, WPA is disabled on a Cisco IP phone. A phone will not list a WPA-only SSID in the Wi-Fi scan
                                 results. Meanwhile, a phone fails to connect to any Wi-Fi router that supports only WPA. Once enabled, the phone will list
                                 and connect to a WPA-only Wi-Fi router.

Step 1

Press Applications .

Step 2

Select Network configuration > Wi-Fi configuration > Backward compatibility with WPA .

Step 3

Press the Select button, to turn this option on or off. You can also press the Navigation cluster, left or right, to turn this option on or
                                          off.

Step 4

Press Set to save the changes.

### Set Up a Wi-Fi Profile from the Phone

Step 1

Press Applications .

Step 2

Select Network configuration > Wi-Fi configuration > Wi-Fi profile .

Step 3

In the Wi-Fi profile screen, move to a row in the list on which you want to set up the profile.

Step 4

Press the Select button.

You can also press Options and then select Edit .

Step 5

In the Edit profile screen, set the parameters as mentioned in the Profile Parameters table.

Parameter

Description

Security mode

Allows you to select the authentication method that is used to secure access to the Wi-Fi network. Depending on the method
                                                         you choose, a password, passphrase, or key field appears so that you can provide the credentials that are required to join
                                                         this Wi-Fi network. Options are:

Auto

EAP-FAST

PEAP-GTC

PEAP-MSCHAPV2

PSK

WEP

None

Default: PSK

Network name

Allows you to enter a name for the SSIDs. This name displays on the phone. Multiple profiles can have the same network name
                                                         with different security mode.This name displays on the phone.

User ID

Allows you to enter a user ID for the network profile.

This field is available when you set the security mode to Auto, EAP-FAST, PEAP-GTC, PEAP-MSCHAPV2. This is a mandatory field
                                                         and it allows maximum length of 32 alphanumeric characters.

Password

Allows you to enter password for the network profile that you create.

This field is available when you set the security mode to Auto, EAP-FAST, PEAP-GTC, PEAP-MSCHAPV2. This is a mandatory field
                                                         and it allows maximum length of 64 alphanumeric characters.

WEP key

Allows you to enter password for the network profile that you create.

This field is available when you set the security mode to WEP. This is a mandatory field and it allows maximum length of 32
                                                         alphanumeric characters.

Passphrase

Allows you to enter password for the network profile that you create. You need to enter this value when the security mode
                                                         is PSK.

Frequency band

Allows you to select the wireless signal frequency band that is used in the WLAN. Options are:

Auto

2.4 GHz

5 GHz

Default: Auto

Step 6

Press Save .

### Set Up a Wi-Fi Profile

You can configure a Wi-Fi profile from the phone web page or from remote device profile resync and then associate the profile
                                 to the available Wi-Fi networks. You can use this Wi-Fi profile to connect to a Wi-Fi. You can configure maximum of four profiles.

Step 1

On the phone web page, select User Login > Advanced > Voice > System .

Step 2

Set the Wi-Fi Profile fields with the information that your administrator provided.

Step 3

Click Submit All Changes .

If the phone has an active call, you can not save the changes.

### Delete a Wi-Fi Profile

You can remove a Wi-Fi profile from the list when the profile is no more required.

Step 1

Press Applications .

Step 2

Select Network configuration > Wi-Fi configuration > Wi-Fi profile .

Step 3

In the Wi-Fi profile screen, select the Wi-Fi profile that you want to remove.

Step 4

Press Options .

Step 5

Select Delete and then confirm the deletion.

### Change the Order of a Wi-Fi Profile

You can determine the position of a Wi-Fi profile in the list. The Wi-Fi profile at the top of the list has the highest priority.
                                 When the Wi-Fi is turned on, the phone uses the Wi-Fi profile on the top of the list to connect automatically to a wirless
                                 network while provisioning.

Step 1

If you change the Wi-Fi profile order from the phone, follow these steps:

Press Applications .

Select Network configuration > Wi-Fi configuration > Wi-Fi profile .

In the Wi-Fi profile screen , select a Wi-Fi of which you want to change the order.

Press Options .

Select Move up or Move down to move the Wi-Fi profile one level up or one level down respectively in the list.

Step 2

If you change the Wi-Fi profile order from the phone web page, follow these steps:

On the phone web page, select User Login > Advanced > Voice > System .

In the Wi-Fi Profile (n) section, set the Wi-Fi Profile Order field to the desired order.

Click Submit All Changes .

### Scan and Save a Wi-Fi Network

You can scan a Wi-Fi profile to get the list of available wireless networks (SSID). The security mode and the network name
                                 have the same value of the scanned SSID. You can then edit the fields of any of the wireless networks. When you save the changes,
                                 it saves as a Wi-Fi profile in the phone Wi-Fi profile list. You can then use this new Wi-Fi profile to connect the phone
                                 to a wireless network.

When the security mode of a wireless network is None, PSK, and WEP, you can't modify the security mode. On the Security mode screen, you only see the security mode that is set for the network. For example, if the security mode of a network is PSK,
                                                   you see only PSK in the Security mode screen.

When you scan a wireless network (SSID) which is the current connected wireless, you can't edit the Network name of this SSID.

Step 1

Press Applications .

Step 2

Select Network configuration > Wi-Fi configuration > Wi-Fi profile .

Step 3

In the Wi-Fi profile screen, press Scan to get all available wireless networks.

Step 4

(Optional) In the Connect to Wi-Fi screen, press Scan again to rescan the list.

Step 5

Select a wireless and press Select or the Select button.

Step 6

In the Setup Wi-Fi screen, set the parameters as mentioned in the Profile Parameters table.

Parameter

Description

Security mode

Allows you to select the authentication method that is used to secure access to the Wi-Fi network. Depending on the method
                                                         you choose, a password, passphrase, or key field appears so that you can provide the credentials that are required to join
                                                         this Wi-Fi network. Options are:

Auto

EAP-FAST

PEAP-GTC

PEAP-MSCHAPV2

PSK

WEP

None

Default: PSK

Network name

Allows you to enter a name for the SSIDs. This name displays on the phone. Multiple profiles can have the same network name
                                                         with different security mode.This name displays on the phone.

User ID

Allows you to enter a user ID for the network profile.

This field is available when you set the security mode to Auto, EAP-FAST, PEAP-GTC, PEAP-MSCHAPV2. This is a mandatory field
                                                         and it allows maximum length of 32 alphanumeric characters.

Password

Allows you to enter password for the network profile that you create.

This field is available when you set the security mode to Auto, EAP-FAST, PEAP-GTC, PEAP-MSCHAPV2. This is a mandatory field
                                                         and it allows maximum length of 64 alphanumeric characters.

WEP key

Allows you to enter password for the network profile that you create.

This field is available when you set the security mode to WEP. This is a mandatory field and it allows maximum length of 32
                                                         alphanumeric characters.

Passphrase

Allows you to enter password for the network profile that you create. You need to enter this value when the security mode
                                                         is PSK.

Frequency band

Allows you to select the wireless signal frequency band that is used in the WLAN. Options are:

Auto

2.4 GHz

5 GHz

Default: Auto

Step 7

Press Save .

### View the Wi-Fi Status

You can also view the status from the phone web page by selecting User Login > Advanced > Info > Status > System Information .

Step 1

Press Applications .

Step 2

Select Network configuration > Wi-Fi configuration > Wi-Fi status .

You see the information:

Wi-Fi status : Displays if the Wi-Fi is connected or disconnected.

Network name : Indicates the name of the SSID.

Signal strength : Indicates strength of the network signal.

MAC address : Indicates MAC address of the phone.

AP MAC address : Indicates MAC address of the access point (SSID).

Channel : Indicated the channel on which the Wi-Fi network transmits and receives data.

Frequency : Indicates the wireless signal frequency band that is used in the Wireless LAN.

Security mode : Indicates the security mode that is set for the wireless LAN.

### View Wi-Fi Status Messages on the Phone

You can view messages about the Wi-Fi connection status of your phone. The messages can help you diagnose Wi-Fi connection
                                 problems. The messages contain:

connection time and MAC address of the AP

disconnection time and diagnostic code

connection failure time

time that weak signal of the AP continues over 12 seconds

Step 1

Press Applications .

Step 2

Select Status > Wi-Fi messages .

Step 3

Use the outer ring of the navigation cluster to scroll through the messages.

Step 4

Press Details to view more details of the selected message.

Step 5

(Optional) Press Clear to delete all the messages.

## Accessibility with Voice Feedback

Voice Feedback helps people who have trouble seeing use their Cisco IP phone. When enabled, a voice prompt helps you navigate
                              your phone buttons, and to use and configure phone features. The voice feedback also reads incoming caller IDs, displayed
                              screens and settings, and button functions.

Voice Feedback is enabled and disabled with the Select button that is located in the center of the Navigation cluster. When the phone is idle, quickly tap Select three times to turn this feature on or off. A voice prompt alerts you to the feature status.

Tip

Push a softkey once, and Voice Feedback reads the feature that is associated with the key. Quickly push the softkey twice
                                                to execute the feature.

Hardkeys such as the Contacts, Applications, and Messages buttons are treated differently. Push a hardkey once, and a voice
                                    reads the screen name followed by the application or setting that is displayed on the phone.

You may not hear Voice Feedback if you select the Headset button, but don't have a connected headset. Select Speakerphone and you hear Voice Feedback again. When on a call, only you hear Voice Feedback so your privacy is assured.

Voice Feedback is only available for English language users. If this feature is not available to you, then it is disabled
                              on your phone.

## Enable or Disable Voice Feedback

Voice Feedback helps people who have trouble seeing use their Cisco IP phone. You can enable or disable Voice Feedback by
                              pressing the Select button three times quickly. You can also access this feature from the Accessibility menu under Applications on your phone.

Step 1

Press Applications .

Step 2

Select Accessibility > Voice Feedback .

Step 3

Select On to turn On Voice Feedback.

Step 4

Press the Set softkey twice quickly to save your settings.

Step 5

(Optional) If you want to disable Voice Feedback, select Off to turn off Voice Feedback, then press the Set softkey twice to make the change take effect.

When you press the Set at the first time, you can hear the feature. After you press the Set at the second time, the Voice Feedback is disabled.

## Adjust Voice Speed

You can customize the speed of Voice Feedback if it reads too quickly or too slowly. Voice Feedback must be enabled before
                              you can select a Voice Speed.

Step 1

Press Applications on your phone, or press Select three times quickly to turn on Voice Feedback.

Step 2

Select Accessibility , and navigate up and down using the Select button ring. Press Select when you hear the option for Voice Speed .

Step 3

Navigate up and down to hear the various speed options. You will hear the number and name of each option. Press Select to choose and save a voice speed.

1 Slowest

2 Slower

3 Normal

4 Faster

5 Fastest

## Adjust Voice Volume

The Voice Feedback feature also allows you to set the voice volume.

### Before you begin

Step 1

Press Applications on your phone, or press Select three times quickly to turn on Voice Feedback.

Step 2

Select Accessibility , and navigate to Voice Volume using the Select button ring.

Step 3

Press Select , and continue pressing until you hear each of the five available volume settings.

Highest

High

Normal

Low

Lowest

Step 4

Press the Set softkey twice to save your settings.

## Adjust Font Size

To have a better visual experience, you can adjust the size of the fonts that are displayed on the phone screen. Note that
                              the customization of the font size does not change few of the texts, such as the texts in a prompt window.

Step 1

Press Settings on your phone.

Step 2

Select Accessibility > Font size .

Step 3

Press the Select button to check the font size options. Press Set to choose and save a font size.

- Regular

- Large

The font size change is applied immediately.

## Enable or Disable Noise Removal from Your Phone

The noise removal feature allows you to filter out the background noises from your environment in a call or meeting.

### Before you begin

Step 1

Press Applications .

Step 2

Select User preferences > Audio preferences > Noise removal .

Step 3

From the Navigation cluster, press the Select button to enable or disable the feature.

Step 4

Press Set to save the changes.

## Enable or Disable Noise Removal with the Phone Web Page

### Before you begin

Step 1

On the phone web page, click User Login > Voice > User .

Step 2

In the Acoustic Setting section, set Noise Removal to Yes to enable the feature.

If you don't want your phone to remove the background noises in a call or meeting, set Noise Removal to No .

Step 3

Click Submit All Changes .

## Sign In to the Desk (Hot Desking)

A phone in a workspace where the scheduling mode is set to Hot Desking is beneficial in a hybrid work environment where remote employees frequently travel to the office and do not have assigned
                              workspaces. In this scenario, employees may only need access to a phone occasionally while in the office. This feature allows
                              hybrid workers quick access to a device with their personal line and settings without the need to have a permanently assigned
                              device thus optimizing office utilization. Your company prefers to enable hot desking in few phones for your use instead of
                              purchasing phones for all employees.

In hot desking, if the calling service of a phone is set to Hot desk only , the phone operates in the host mode by default. The phone cannot receive inbound calls and you can press the Emergency softkey to dial emergency numbers only. Besides, you cannot view call history, assign features on line keys, access voicemails,
                              or use Contacts. To access the hot desking guest mode, you can pair your mobile phone with this phone and sign in as a guest
                              for a certain duration.

### Before you begin

Phone registered to Webex Calling with a workspace account with the scheduling mode set to Hot Desking . Phone displays Desk available screen with a QR code to be used for pairing with a mobile.

Webex application is installed and logged in on the mobile device.

Step 1

In your mobile phone, log in to Webex application with your account.

Step 2

You see the QR code in the Desk available screen of the phone. Use the camera of your mobile and scan the QR code on the phone.

After you scan the QR code, Signing in screen appears. You see Book this desk until screen which allows you to enter a time in hours until which you can use the desk. After you click Book , the Applying configuration screen appears for a while. After succesful sign in, the configuration is applied and the phone reboots and returns to the
                                          home screen. You notice the following changes in the phone and in the paired mobile.

Your personal phone number is displayed on the workspace phone.

If you press Applications , you see the Hot desking settings menu is added to the Information and settings screen.

Your personal data syncs with the phone and Webex call logs sync with the phone's Recents list from the Webex cloud server.
                                                For example, if there is a missed call in your call logs, it will display on the phone screen. Also, you can access the Missed
                                                call screen and make a call back to that contact.

You can search contact by "name" from Webex directory and make a call. If you access the Recents list, you see this call is logged.

While you use the desk, there can be one of your Webex meetings notification pop-up. You can press Join to join the meeting. If you access the Recents list, you see this meeting is added to the list.

In the mobile phone, open the Webex application and check the Connect to a Device list. You see the booked phone name, duration of the desk booking, and a sign-out button.

### Sign Out from the Desk (Hot Desking)

After using a phone or a desk in hot desking mode, you can sign out using phone menu or from Webex application at any point
                                 of time. Also, once the desk duration ended, signing out occurs automatically.

Sign out using any of the following:

```
This will remove your desk booking and personal data from the device
```

- On the mobile, open the Webex application and access the Booked Devices , click the Sign out button next to the booked phone name.

After you sign out, your personal data and synced Webex call logs remove from the phone (desk). The user account and the phone
                                             number changes to workspace account.

### Error Scenarios during Hot Desking

You may encounter the following errors before sign-in, after sign-in, and after sign-out from the desk and may need to contact
                                 your administrator.

#### Before Sign-in

Sign in unavailable during call

Desk unavailable during upgrade

Desk unavailable during service issue

Desk unavailable during service failure

#### After Sign-in Errors

Failed to connect to Webex calling. You will be unable to make or receive calls with your personal number.

Error code contains the message: Personal Account data already populated

Error code contains the messages:

Couldn't resolve host name

Couldn't connect to server

Timeout was reached

Operation timed out

System time adjustment failed

Error code contains messages:

Peer certificate cannot be authenticated with given CA certificates

Missing 'serviceDomain' (unknown CI location)

SRP group must be 3072 bits or higher

Unsupported CI SRP handshake protocol

Failed to register on spark with given activation code

No access token

Incomplete account data

GDS refused to process our activation id

#### Sign-out Errors

WxC sign-out error

Network is down

Call is on or Meeting is on

Factory reset is not allowed during hotdesking sign-in

## Switch the Operating Mode

You can manually switch the operating mode of call queues, auto attendants, and hunt groups on your phone. Hence, the incoming
                              calls are effectively routed to different destinations based on the operating mode you've selected.

### Before you begin

Your administrator has configured a series of operating modes for the organization and locations.

Your administrator has configured the Mode management function for features on line keys. Your phone screen displays up to
                                    five features with respective line keys.

Step 1

Press the line key for a specific feature to enter mode management.

Step 2

Do one of the following actions:

Press the Navigation cluster , up or down, to switch between the modes. The current switch back mode is displayed on the right side of the mode name.

Press the Manual on or Manual off softkey to specify how to switch back to the normal operation mode: automatically or manually.

For example, an operating mode <Mode name> Automatic switch will be changed to <Mode name> Manual switch after you press the Manual on softkey. It indicates that the operating mode retains until you manually switch back to a normal mode.

Press the Set softkey.

Press the Details softkey to view detailed time duration of a mode.

Select Specify duration to add time extension to an operating mode.

Press the Navigation cluster , up or down, to add time extension in minutes. The minimum value is 30 minutes. The value must be multiple of 30 and cannot
                                                         exceed 720 (12 hours).

If this value is greater than 30 minutes, the phone displays the time in hours. However, the phone always displays Time extention ends at as a 24-hour system.

Press the Set softkey.

(Optional) After you extend an operating mode, the Extend softkey becomes Edit extend . Press this softkey and then select Switch manually . The current operating mode retains till you manually switch back to a normal mode.

Select Switch manually . The current operating mode retains till you manually switch back to a normal mode.

You cannot extend an operating mode that needs to be switched manually back to normal.

Press the All features softkey for batch edit.

Press Batch edit to list all features except the ones with mode-based forwarding disabled.

Press the Navigation cluster , up or down, to switch between the features, and then press Select to select one or more features. Alternatively, select All features .

Press the Edit mode softkey to select an operating mode.

Only common operating modes will be displayed for batch edit. If there are no common modes available, the phone displays an
                                                   alert.

Press the Set softkey.

By default, the operating status is set to Switch manually for the mode you have selected during batch editing.

- Press the Revert mode softkey to return to the normal operating mode if this operating mode has a time extension or has been set to switch manually.

Your phone screen displays features with line keys illuminate to indicate the operating mode status. The following table describes
                              the default operating modes and the associated LED colors displayed on the line keys.

LED Color

Operating Mode Status

Description

Green

Normal operating mode

The current routing follows the normal operating mode, even if in some periods there is no operating mode configured by your
                                          administrator. The feature's operating mode switches automatically under the following circumstances:

The current mode reaches its end time.

A higher precedence mode reaches its start time.

Amber

Automatic switch back exception (Start early)

You have switched the feature to an operating mode before its start time. This mode runs as an exception until its start time
                                          is reached. At this point, the mode automatically switches the feature back to normal operation.

Automatic switch back exception (Extended)

You have extended the operating mode before it reaches its end time. This mode runs as an exception until the extension end
                                          time is reached. That is, the mode's end time plus an extension of up to 12 hours. At this point, the mode automatically switches
                                          the feature back to normal operation.

Automatic switch back exception (Exception)

You have switched the feature to another operating mode that is running in its scheduled time, but the original operating
                                          mode takes precedence. The mode runs as an exception until its end time is reached. At this point, the mode automatically
                                          switches the feature back to normal operation.

For example, there are Mode A (8 AM to 5 PM) and Mode B (12 PM to 1 PM). The administrator sets Mode B to have precedence
                                          over Mode A. Hence, the system operates in Mode B from 12 PM to 1 PM. If you switch Mode B to Mode A during this period, this
                                          exception occurs. In this exception state, Mode A remains active until 5 PM.

Red

Manual switch back exception (Switch manually)

You have switched the operating mode or extended the mode for manual switch back. The operating mode runs as an exception
                                          until you manually switches the feature back to normal operation or a different mode.

Gray (Off)

Mode-based fwd disabled

Unrecognized

One of the following scenarios occurs:

There is no operating mode associated with the feature.

Mode-based forwarding is disabled.

Your phone doesn’t receive a response from the server.

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

| Step 1 | On the phone web page, click User
                                             				  Login > advanced > Voice > User . |
|---|---|
| Step 2 | Under Call Forward , choose Yes for CFWD Setting. |
| Step 3 | Click Submit All Changes. |

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
| Step 2 | Under Supplementary Services , set DND Settings to Yes . You can turn on DND on for all lines if your administrator hasn't enabled feature key sync (FKS). |
| Step 3 | Click Submit All Changes . |

| Step 1 | Press the Navigation cluster up or down to select a phone line. |
|---|---|
| Step 2 | Press Applications . |
| Step 3 | Select User preferences > Call preferences > Call waiting . |
| Step 4 | Select On to allow you to answer an incoming call that rings while on another call, or select Off to disable the function. |
| Step 5 | Press Set to save the setting. |

| Step 1 | On the phone web page, select User Login > Voice > User . |
|---|---|
| Step 2 | Under Supplementary Services , set CW Setting to Yes . The setting applies to all lines, except for the ones where your administrator has enabled synchronization of Call Waiting
                                          between the lines and the BroadSoft XSI service. |
| Step 3 | Click Submit All Changes . |

| Step 1 | Press the Navigation cluster up or down to select a phone line. |
|---|---|
| Step 2 | Press Applications . |
| Step 3 | Select User preferences > Call preferences > Block anonymous call . |
| Step 4 | Select On if you want to block the call that does not have caller information, or select Off to allow the call. |
| Step 5 | Press Set to save the setting. |

| Step 1 | On the phone web page, select User Login > Voice > User . |
|---|---|
| Step 2 | Under Supplementary Services , set Block ANC Setting to Yes . The setting applies to all lines, except for the ones where your administrator has enabled synchronization of Anonymous Call
                                          Rejection between the lines and the BroadSoft XSI service. |
| Step 3 | Click Submit All Changes . |

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
| Step 2 | Select User Preferences > Call Preferences > Dial assistance . |
| Step 3 | Press On to enable the dial assistance or press Off to disable it. |
| Step 4 | Press Set to apply the mode. |
| Step 5 | Press Back to return to the Call Preferences screen. |

| Step 1 | Press Applications . |
|---|---|
| Step 2 | Select User preferences > Call preferences . |
| Step 3 | Select Anywhere . |
| Step 4 | (Optional) Select a line if  BroadWorks Anywhere is configured on multiple lines. |
| Step 5 | Add contact number and name in the Locations screen. Maximum length of a name that you can enter is 25. You can also keep the Name field empty. Maximum length of a number that you can enter is 20. |
| Step 6 | Enable or disable the location. |
| Step 7 | Press Save to add the locations to the Locations list. |

| Step 1 | Press Applications . |
|---|---|
| Step 2 | Select User preferences > Call preferences > Auto answer page . |
| Step 3 | Select On to enable the Auto answer page or select Off to disable Auto answer page. |
| Step 4 | Press Set to save the changes. |

| Step 1 | Press Applications . |
|---|---|
| Step 2 | Select User preferences > Call preferences > Voice mail . |
| Step 3 | Enter a phone number to check voicemail. If you press the Messages button, it dials the voicemail number and displays the voice message list. |
| Step 4 | Press Set to confirm the assigned number. |
| Step 5 | Press to exit. |
| Step 6 | Press Back to exit. |

| Step 1 | Press Applications . |
|---|---|
| Step 2 | Select Network configuration > HTTP proxy settings > Proxy mode . |
| Step 3 | Press the Select button of the navigation cluster to choose Auto . |
| Step 4 | Highlight Auto discovery (WPAD) , select On to turn on Web Proxy Auto-Discovery (WPAD) that is used to retrieve a PAC file automatically, select Off to turn off WPAD. By default, your phone uses WPAD in the auto proxy mode. |
| Step 5 | (Optional) If you turn off WPAD in the previous step, you need to further enter a valid Proxy Auto-Configuration (PAC) URL in PAC URL . For example: http://proxy.department.branch.example.com/pac If you don't have the PAC URL, contact your administrator. |
| Step 6 | Press Set to apply the settings. |

| Step 1 | Press Applications . |
|---|---|
| Step 2 | Select Network configuration > HTTP proxy settings > Proxy mode . |
| Step 3 | Press the Select button of the navigation cluster to choose Manual . |
| Step 4 | Enter a valid hostname or IP address of a proxy server in Proxy host . Note Do not provide the scheme ( http:// or https:// ) for the proxy host. | Note | Do not provide the scheme ( http:// or https:// ) for the proxy host. |
| Note | Do not provide the scheme ( http:// or https:// ) for the proxy host. |
| Step 5 | Enter a valid server port of the specified proxy server in Proxy port . |
| Step 6 | (Optional) If your proxy server requires authentication, highlight Proxy authentication and then select On . |
| Step 7 | (Optional) Enter your username and password to access the proxy server. If you don't have the username and password, contact your administrator. |
| Step 8 | Press Set to apply the settings. |

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

| Step 1 | On the phone web page, select User Login > Voice > User . |
|---|---|
| Step 2 | In the Phone Background field of the Screen section, select any of the options as a phone wallpaper. Default : Phone does not have any wallpaper. If no wallpaper is added to the phone screen, the phone screen displays monochrome wallpaper. Download Picture : In the phone web page, you can select the Download Picture as your phone background option. The picture that you add in the Picture Download URL is used as the phone wallpaper. Phone supports .jpg, and .png image files and the image size can be a maximum of 625 KB. You can scale-up or scale-down the
                                                image so that a picture can fully fit into the screen. If the aspect ratio of the target picture is not 5:3, some parts of
                                                the picture are lost. Logo : In the phone web page you can select Logo as your phone background option. The logo that you add in the Logo URL is used as the wallpaper. Caution Do not exceed a maximum length of 255 characters for the Logo URL or Picture Download URL . The logo display area is the center of the phone screen. The logo display area size of the phone is 128x128 pixels. If original
                                                logo size does not fit display area, the logo scales to fit the display area. | Caution | Do not exceed a maximum length of 255 characters for the Logo URL or Picture Download URL . |
| Caution | Do not exceed a maximum length of 255 characters for the Logo URL or Picture Download URL . |

| Caution | Do not exceed a maximum length of 255 characters for the Logo URL or Picture Download URL . |
|---|---|

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

| Step 1 | On the phone web page, select User Login > Voice > User . |
|---|---|
| Step 2 | In the Phone Background field of the Screen section, select any of the options as a phone wallpaper. Default : Phone does not have any wallpaper. If no wallpaper is added to the phone screen, the phone screen displays monochrome wallpaper. Download Picture : In the phone web page, you can select the Download Picture as your phone background option. The picture that you add in the Picture Download URL is used as the phone wallpaper. Phone supports .jpg, and .png image files and the image size can be a maximum of 625 KB. You can scale-up or scale-down the
                                                image so that a picture can fully fit into the screen. If the aspect ratio of the target picture is not 5:3, some parts of
                                                the picture are lost. Logo : In the phone web page you can select Logo as your phone background option. The logo that you add in the Logo URL is used as the wallpaper. Caution Do not exceed a maximum length of 255 characters for the Logo URL or Picture Download URL . The logo display area is the center of the phone screen. The logo display area size of the phone is 128x128 pixels. If original
                                                logo size does not fit display area, the logo scales to fit the display area. | Caution | Do not exceed a maximum length of 255 characters for the Logo URL or Picture Download URL . |
| Caution | Do not exceed a maximum length of 255 characters for the Logo URL or Picture Download URL . |

| Caution | Do not exceed a maximum length of 255 characters for the Logo URL or Picture Download URL . |
|---|---|

| Step 1 | On the phone
                                       			 web page, select User Login > Voice > User . |
|---|---|
| Step 2 | In the Screen section, choose Download Picture for the Phone
                                             				  Background field. |
| Step 3 | Upload the
                                       			 custom wallpaper to a TFTP,HTTP, or HTTPS server. The image is a
                                          				.jpg file. Preferred dimension is 800x480 pixels. If the image is not the
                                          				preferred size, user still can upload it but it will resize to fit the screen. |
| Step 4 | In
                                       			 the Picture
                                          				Download URL field, enter the path where the wallpaper image has
                                       			 been uploaded. The URL must
                                          				include the TFTP,HTTP, or HTTPS server name (or IP address), directory, and
                                          				filename. Example: http:// 10.64.84.147/pictures/image04_800x480x24.jpg When you enter
                                          				an incorrect URL to download a new wallpaper, the phone fails to upgrade to the
                                          				newer wallpaper and displays the existing downloaded wallpaper. If the phone
                                          				does not have any wallpaper downloaded earlier, it displays a gray screen. |
| Step 5 | Click Submit
                                          				All Changes . The phone does
                                          				not reboot after you change the background image URL. |

| Step 1 | Press Applications . |
|---|---|
| Step 2 | Select User preferences > Screen preferences > Display brightness . |
| Step 3 | Press the Navigation cluster, right or left, to increase or decrease the brightness. |
| Step 4 | Press Save . |

| Step 1 | Press Applications . |
|---|---|
| Step 2 | Select User preferences > Screen preferences > Backlight timer . |
| Step 3 | Press Edit or Select button. |
| Step 4 | Scroll through the list and select a duration for which the backlight remains on: 1 min 5 min 30 min Always On Note Default value is 5 min. | Note | Default value is 5 min. |
| Note | Default value is 5 min. |
| Step 5 | Press Set to apply the selection. |

| Note | Default value is 5 min. |
|---|---|

| Step 1 | Select Voice > User . |
|---|---|
| Step 2 | In the Screen section, select a duration for the Back Light Timer parameter. You can also configure this parameter in the configuration file (cfg.xml) by entering a string in this format: <Back_Light_Timer ua="rw">30s</Back_Light_Timer> The allowed values are 1m\|5m\|30m\|Always On. The default value is 5m (5 minutes). |
| Step 3 | In the Display Brightness field, enter an integer ranging from 4 to 15 for the desired brightness. You can also configure this parameter in the configuration file (cfg.xml) by entering a string in this format: <Display_Brightness ua="rw">15</Display_Brightness> The allowed value is an integer ranging from 4 through 15. The bigger the value, the brighter the screen display. The default
                                          value is 15. |
| Step 4 | Click Submit All Changes . |

| Step 1 | Press Applications . |
|---|---|
| Step 2 | Select User preferences > Attendant console preferences > Display mode . The following options are available: Name Ext Both |
| Step 3 | Choose the display mode and press Set . |

| Step 1 | Press Applications . |
|---|---|
| Step 2 | Select User preferences > Audio preferences > Preferred audio device . |
| Step 3 | Press Select to choose one of the options: None —Selects the last used audio device. Speaker —Selects the speakerphone as the audio device. Headset —Selects a headset as the audio device. A headset priority order is: USB (highest) Bluetooth (medium) analog headset (lowest) Bluetooth —Selects Bluetooth as the audio device. The priority order is Bluetooth (highest), USB (medium), and analog headset (lowest). |
| Step 4 | Press Set to save the selection. |

| Step 1 | Press Applications . |
|---|---|
| Step 2 | Select Device administration > Restart . |
| Step 3 | Select OK to confirm that you want to reboot your phone. |

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
| Step 3 | Press Sign in to save your username and password. Note If any of the Username field or the Password field is empty, the phone displays a grey Sign in softkey and you can't press the softkey. | Note | If any of the Username field or the Password field is empty, the phone displays a grey Sign in softkey and you can't press the softkey. |
| Note | If any of the Username field or the Password field is empty, the phone displays a grey Sign in softkey and you can't press the softkey. |
| Step 4 | (Optional) Enter a new username and password if you want to login with another set of credentials. |

| Note | If any of the Username field or the Password field is empty, the phone displays a grey Sign in softkey and you can't press the softkey. |
|---|---|

| Important | The menu items that display on the phone screen are different in the following scenarios: Your administrator enables the feature key synchronization (FKS) on your extension. Your administrator connects your extension to the XSI BroadWorks server. |
|---|---|

| Important | If you activate DND on your phone, your assistants do not receive your incoming calls. |
|---|---|

| Step 1 | Do one of the following actions: If your administrator has programmed the Executive function on a line key, the phone shows the Executive together with the call filtering status ( On or Off ) on the main screen. Press the line key. If you do not have the Executive function that is configured on a line key: Press Applications . Select Executive . |
|---|---|
| Step 2 | Follow the below procedure according to the actual menus displayed on the phone. If your administrator configures your extension to connect to the XSI BroadWorks server: Select Call filter > Call filter . Press to select On . Select the call filter mode and the call filter type. Call filter mode —Choose one of the following options: Simple —Your incoming calls go to your assistants according to the call filtering criteria configured in the simple mode. Advanced —Your incoming calls go to your assistants according to the call filtering criteria configured in the advanced mode. Call filter type —Choose one of the following options: Note This menu item is available when the Call filter mode is set to Simple . All Calls —All your incoming calls go to your assistants. Internal Calls —If you and the callers are in the same BroadSoft group, their incoming calls go to your assistants. External Calls —If you and the callers are not in the same BroadSoft group, their incoming calls go to your assistants. Press Set to apply the changes. If your administrator only enables the feature key synchronization (FKS) on your extension: Press the On softkey to activate call filtering. Press to exit. | Note | This menu item is available when the Call filter mode is set to Simple . |
| Note | This menu item is available when the Call filter mode is set to Simple . |

| Note | This menu item is available when the Call filter mode is set to Simple . |
|---|---|

| Step 1 | Do one of the following actions: If your administrator has programmed the Executive function on a line key, the phone shows the Executive together with the call filtering status ( On or Off ) on the main screen. Press the line key. If you do not have the Executive function that is configured on a line key: Press Applications . Select Executive . |
|---|---|
| Step 2 | Follow the below procedure according to the actual menus displayed on the phone. If your administrator configures your extension to connect to the XSI BroadWorks server: Select Call filter > Call filter Press to select Off . Press Set to apply the changes. If your administrator only enables the feature key synchronization (FKS) on your extension: Press the Off softkey to deactivate call filtering. Press to exit. |

| Step 1 | Do one of the following actions: If your administrator has programmed the Executive function on a line key, the phone shows the Executive together with the call filtering status ( On or Off ) on the main screen. Press the line key. If you do not have the Executive function that is configured on a line key: Press Applications . Select Executive . |
|---|---|
| Step 2 | Select Assistant List . The Assistant List screen displays a maximum of 10 assistants on the phone. If your administrator configures more than one executive on the phone, then the screen only displays the assistants of the
                                             first available executive. |
| Step 3 | (Optional) If you want to make a call to one of your assistants, then highlight the assistant's phone number, and press Call . |

| Important | The menu items that display on the phone screen are different in the following scenarios: Your administrator enables the feature key synchronization (FKS) on your extension. Your administrator connects your extension to the XSI BroadWorks server. |
|---|---|

| Step 1 | Do one of the following actions: If your administrator has programmed the Assistant function on a line key, press the line key. If you do not have the Assistant function on a line key: Press Applications . Select Assistant . |
|---|---|
| Step 2 | Select Executive List . |
| Step 3 | Select an executive of whose assistant pool that you want to opt in to or out of. |
| Step 4 | Press to select Opt-in to opt in to the executive's pool or select Opt-out to opt out of the executive's pool. |
| Step 5 | Press Set to apply the changes. |

| Important | Activating or deactivating call filtering for an executive activates or deactivates the setting for all the assistants in
                                             the executive’s pool. |
|---|---|

| Step 1 | Do one of the following actions: If your administrator has programmed the Assistant function on a line key, press the line key. If you do not have the Assistant function on a line key: Press Applications . Select Assistant . |
|---|---|
| Step 2 | Follow the below procedure according to the actual menus displayed on the phone. If your administrator configures your extension to connect to the XSI BroadWorks server: Select Call filter . Highlight an executive, press to toggle call filtering on or off for the highlighted executive. Press Set , and then press OK to apply the changes. If your administrator only enables the feature key synchronization (FKS) on your extension: Highlight the executive for whom you want to activate or deactivate call filtering. Press to toggle call filtering on or off for the highlighted executive. Press to exit. |

| Important | If you activate DND on your extension, calls are not diverted. |
|---|---|

| Step 1 | Do one of the following actions: If your administrator has programmed the Assistant function on a line key, press the line key. If you do not have the Assistant function on a line key: Press Applications . Select Assistant . |
|---|---|
| Step 2 | Follow the below procedure according to the actual menus displayed on the phone. If your administrator configures your extension to connect to the XSI BroadWorks server: Select Divert > Divert . Select On to activate call diversion. Highlight Divert number and enter the destination number to which you want the calls to be diverted. Press Set to apply the changes. If your administrator only enables the feature key synchronization (FKS) on your extension: Typically, the screen shows a list of all the executives associated with all the assistant extensions on the phone. Select
                                                      an executive associated with the extension for which you want to activate call diversion. The extension with which the selected executive is associated appears at the top. Press Divert . Enter the destination number to which you want the calls to be diverted. Press Call to complete the action. Press to exit. |

| Step 1 | Do one of the following actions: If your administrator has programmed the Assistant function on a line key, press the line key. If you do not have the Assistant function on a line key: Press Applications . Select Assistant . |
|---|---|
| Step 2 | Follow the below procedure according to the actual menus displayed on the phone. If your administrator configures your extension to connect to the XSI BroadWorks server: Select Divert > Divert . Select Off to deactivate call diversion. Press Set to apply the change. If your administrator only enables the feature key synchronization (FKS) on your extension: Press Clr divert . Press to exit. |

| Step 1 | Do one of the following actions: If your administrator has programmed the Assistant function on a line key, press the line key. If you do not have the Assistant function on a line key: Press Applications . Select Assistant . |
|---|---|
| Step 2 | Select Executive List . The Executive List screen displays a maximum of 10 executives on the phone. If your administrator configures more than one assistant on the phone, then the screen only displays the executives of the
                                             first available assistant. |

| Step 1 | Select a Wi-Fi network from the list. You see the following options: Scan —The phone scans again for available networks. Setup —Opens the Setup Wi-Fi page. Skip —You see the message If you skip this step, you will need to configure the network manually . If you confirm to skip the Connect to Wi-Fi page, the Wi-Fi Scan softkey displays. |
|---|---|
| Step 2 | Press Setup and complete the fields. |
| Step 3 | Press Connect . |

| Step 1 | Press the Wi-Fi Scan softkey when it displays on the phone screen. The message Wireless scan in progress displays. After the scan completes, a list of networks is displayed. You see the following options: Scan —Scans again for available networks. Select —Opens the Setup Wi-Fi page. Cancel —Closes the network list. |
|---|---|
| Step 2 | Select a Wi-Fi network from the list. |
| Step 3 | Press Select and complete the fields. |
| Step 4 | (Optional) Press Save to save the setups as a Wi-Fi profile. You can connect to this network later with the profile. |
| Step 5 | Press Connect . |

| Step 1 | On the phone web page, select User Login > Advanced > Voice > System . |
|---|---|
| Step 2 | Go to the Wi-Fi Settings section and set the Phone-wifi-on field to Yes . |
| Step 3 | Click Submit All Changes . |

| Step 1 | Press Applications . |
|---|---|
| Step 2 | Select Network configuration > Wi-Fi configuration > Wi-Fi . |
| Step 3 | Press the Select button, to turn the Wi-Fi on or off. You can also press the Navigation cluster, left or right, to turn the Wi-Fi on or off. |
| Step 4 | Press Set to save the changes. |

| Step 1 | Press Applications . |
|---|---|
| Step 2 | Select Network configuration > Wi-Fi configuration > Wi-Fi profile . |
| Step 3 | In the Wi-Fi profile screen, do any of the actions to connect to Wi-Fi. Select any of the configured Wi-Fi profile and click Connect . Press Scan and select one wireless in the Connect to Wi-Fi screen. In the Setup Wi-Fi screen, enter values in the fields and press Connect . See the Profile Parameter table in the Set Up a Wi-Fi Profile from the Phone for the field values. |

| Step 1 | Press Wi-Fi Scan . A list of Wi-Fi networks displays. |
|---|---|
| Step 2 | Press one of these options: Scan —to scan for networks again. Select —to configure the highlighted network. |
| Step 3 | Highlight a network from the list. |
| Step 4 | Press Select . |
| Step 5 | Select one of the following options: Cancel —go back to the previous screen. Save —save the network with the information you input. Connect —connect to the selected network. |
| Step 6 | Press Connect . Note The steps above also apply if your phone loses its network connection any time after it has booted up, and it's not connected
                                                         to an Ethernet cable. | Note | The steps above also apply if your phone loses its network connection any time after it has booted up, and it's not connected
                                                         to an Ethernet cable. |
| Note | The steps above also apply if your phone loses its network connection any time after it has booted up, and it's not connected
                                                         to an Ethernet cable. |

| Note | The steps above also apply if your phone loses its network connection any time after it has booted up, and it's not connected
                                                         to an Ethernet cable. |
|---|---|

| Step 1 | Press Applications . |
|---|---|
| Step 2 | Select Network configuration > Wi-Fi configuration > Backward compatibility with WPA . |
| Step 3 | Press the Select button, to turn this option on or off. You can also press the Navigation cluster, left or right, to turn this option on or
                                          off. |
| Step 4 | Press Set to save the changes. |

| Step 1 | Press Applications . |
|---|---|
| Step 2 | Select Network configuration > Wi-Fi configuration > Wi-Fi profile . |
| Step 3 | In the Wi-Fi profile screen, move to a row in the list on which you want to set up the profile. |
| Step 4 | Press the Select button. You can also press Options and then select Edit . |
| Step 5 | In the Edit profile screen, set the parameters as mentioned in the Profile Parameters table. Table 3. Profile Parameters Parameter Description Security mode Allows you to select the authentication method that is used to secure access to the Wi-Fi network. Depending on the method
                                                         you choose, a password, passphrase, or key field appears so that you can provide the credentials that are required to join
                                                         this Wi-Fi network. Options are: Auto EAP-FAST PEAP-GTC PEAP-MSCHAPV2 PSK WEP None Default: PSK Network name Allows you to enter a name for the SSIDs. This name displays on the phone. Multiple profiles can have the same network name
                                                         with different security mode.This name displays on the phone. User ID Allows you to enter a user ID for the network profile. This field is available when you set the security mode to Auto, EAP-FAST, PEAP-GTC, PEAP-MSCHAPV2. This is a mandatory field
                                                         and it allows maximum length of 32 alphanumeric characters. Password Allows you to enter password for the network profile that you create. This field is available when you set the security mode to Auto, EAP-FAST, PEAP-GTC, PEAP-MSCHAPV2. This is a mandatory field
                                                         and it allows maximum length of 64 alphanumeric characters. WEP key Allows you to enter password for the network profile that you create. This field is available when you set the security mode to WEP. This is a mandatory field and it allows maximum length of 32
                                                         alphanumeric characters. Passphrase Allows you to enter password for the network profile that you create. You need to enter this value when the security mode
                                                         is PSK. Frequency band Allows you to select the wireless signal frequency band that is used in the WLAN. Options are: Auto 2.4 GHz 5 GHz Default: Auto | Parameter | Description | Security mode | Allows you to select the authentication method that is used to secure access to the Wi-Fi network. Depending on the method
                                                         you choose, a password, passphrase, or key field appears so that you can provide the credentials that are required to join
                                                         this Wi-Fi network. Options are: Auto EAP-FAST PEAP-GTC PEAP-MSCHAPV2 PSK WEP None Default: PSK | Network name | Allows you to enter a name for the SSIDs. This name displays on the phone. Multiple profiles can have the same network name
                                                         with different security mode.This name displays on the phone. | User ID | Allows you to enter a user ID for the network profile. This field is available when you set the security mode to Auto, EAP-FAST, PEAP-GTC, PEAP-MSCHAPV2. This is a mandatory field
                                                         and it allows maximum length of 32 alphanumeric characters. | Password | Allows you to enter password for the network profile that you create. This field is available when you set the security mode to Auto, EAP-FAST, PEAP-GTC, PEAP-MSCHAPV2. This is a mandatory field
                                                         and it allows maximum length of 64 alphanumeric characters. | WEP key | Allows you to enter password for the network profile that you create. This field is available when you set the security mode to WEP. This is a mandatory field and it allows maximum length of 32
                                                         alphanumeric characters. | Passphrase | Allows you to enter password for the network profile that you create. You need to enter this value when the security mode
                                                         is PSK. | Frequency band | Allows you to select the wireless signal frequency band that is used in the WLAN. Options are: Auto 2.4 GHz 5 GHz Default: Auto |
| Parameter | Description |
| Security mode | Allows you to select the authentication method that is used to secure access to the Wi-Fi network. Depending on the method
                                                         you choose, a password, passphrase, or key field appears so that you can provide the credentials that are required to join
                                                         this Wi-Fi network. Options are: Auto EAP-FAST PEAP-GTC PEAP-MSCHAPV2 PSK WEP None Default: PSK |
| Network name | Allows you to enter a name for the SSIDs. This name displays on the phone. Multiple profiles can have the same network name
                                                         with different security mode.This name displays on the phone. |
| User ID | Allows you to enter a user ID for the network profile. This field is available when you set the security mode to Auto, EAP-FAST, PEAP-GTC, PEAP-MSCHAPV2. This is a mandatory field
                                                         and it allows maximum length of 32 alphanumeric characters. |
| Password | Allows you to enter password for the network profile that you create. This field is available when you set the security mode to Auto, EAP-FAST, PEAP-GTC, PEAP-MSCHAPV2. This is a mandatory field
                                                         and it allows maximum length of 64 alphanumeric characters. |
| WEP key | Allows you to enter password for the network profile that you create. This field is available when you set the security mode to WEP. This is a mandatory field and it allows maximum length of 32
                                                         alphanumeric characters. |
| Passphrase | Allows you to enter password for the network profile that you create. You need to enter this value when the security mode
                                                         is PSK. |
| Frequency band | Allows you to select the wireless signal frequency band that is used in the WLAN. Options are: Auto 2.4 GHz 5 GHz Default: Auto |
| Step 6 | Press Save . |

| Parameter | Description |
|---|---|
| Security mode | Allows you to select the authentication method that is used to secure access to the Wi-Fi network. Depending on the method
                                                         you choose, a password, passphrase, or key field appears so that you can provide the credentials that are required to join
                                                         this Wi-Fi network. Options are: Auto EAP-FAST PEAP-GTC PEAP-MSCHAPV2 PSK WEP None Default: PSK |
| Network name | Allows you to enter a name for the SSIDs. This name displays on the phone. Multiple profiles can have the same network name
                                                         with different security mode.This name displays on the phone. |
| User ID | Allows you to enter a user ID for the network profile. This field is available when you set the security mode to Auto, EAP-FAST, PEAP-GTC, PEAP-MSCHAPV2. This is a mandatory field
                                                         and it allows maximum length of 32 alphanumeric characters. |
| Password | Allows you to enter password for the network profile that you create. This field is available when you set the security mode to Auto, EAP-FAST, PEAP-GTC, PEAP-MSCHAPV2. This is a mandatory field
                                                         and it allows maximum length of 64 alphanumeric characters. |
| WEP key | Allows you to enter password for the network profile that you create. This field is available when you set the security mode to WEP. This is a mandatory field and it allows maximum length of 32
                                                         alphanumeric characters. |
| Passphrase | Allows you to enter password for the network profile that you create. You need to enter this value when the security mode
                                                         is PSK. |
| Frequency band | Allows you to select the wireless signal frequency band that is used in the WLAN. Options are: Auto 2.4 GHz 5 GHz Default: Auto |

| Step 1 | On the phone web page, select User Login > Advanced > Voice > System . |
|---|---|
| Step 2 | Set the Wi-Fi Profile fields with the information that your administrator provided. |
| Step 3 | Click Submit All Changes . If the phone has an active call, you can not save the changes. |

| Step 1 | Press Applications . |
|---|---|
| Step 2 | Select Network configuration > Wi-Fi configuration > Wi-Fi profile . |
| Step 3 | In the Wi-Fi profile screen, select the Wi-Fi profile that you want to remove. |
| Step 4 | Press Options . |
| Step 5 | Select Delete and then confirm the deletion. |

| Step 1 | If you change the Wi-Fi profile order from the phone, follow these steps: Press Applications . Select Network configuration > Wi-Fi configuration > Wi-Fi profile . In the Wi-Fi profile screen , select a Wi-Fi of which you want to change the order. Press Options . Select Move up or Move down to move the Wi-Fi profile one level up or one level down respectively in the list. |
|---|---|
| Step 2 | If you change the Wi-Fi profile order from the phone web page, follow these steps: On the phone web page, select User Login > Advanced > Voice > System . In the Wi-Fi Profile (n) section, set the Wi-Fi Profile Order field to the desired order. Click Submit All Changes . |

| Note | When the security mode of a wireless network is None, PSK, and WEP, you can't modify the security mode. On the Security mode screen, you only see the security mode that is set for the network. For example, if the security mode of a network is PSK,
                                                   you see only PSK in the Security mode screen. When you scan a wireless network (SSID) which is the current connected wireless, you can't edit the Network name of this SSID. |
|---|---|

| Step 1 | Press Applications . |
|---|---|
| Step 2 | Select Network configuration > Wi-Fi configuration > Wi-Fi profile . |
| Step 3 | In the Wi-Fi profile screen, press Scan to get all available wireless networks. |
| Step 4 | (Optional) In the Connect to Wi-Fi screen, press Scan again to rescan the list. |
| Step 5 | Select a wireless and press Select or the Select button. |
| Step 6 | In the Setup Wi-Fi screen, set the parameters as mentioned in the Profile Parameters table. Table 4. Profile Parameters Parameter Description Security mode Allows you to select the authentication method that is used to secure access to the Wi-Fi network. Depending on the method
                                                         you choose, a password, passphrase, or key field appears so that you can provide the credentials that are required to join
                                                         this Wi-Fi network. Options are: Auto EAP-FAST PEAP-GTC PEAP-MSCHAPV2 PSK WEP None Default: PSK Network name Allows you to enter a name for the SSIDs. This name displays on the phone. Multiple profiles can have the same network name
                                                         with different security mode.This name displays on the phone. User ID Allows you to enter a user ID for the network profile. This field is available when you set the security mode to Auto, EAP-FAST, PEAP-GTC, PEAP-MSCHAPV2. This is a mandatory field
                                                         and it allows maximum length of 32 alphanumeric characters. Password Allows you to enter password for the network profile that you create. This field is available when you set the security mode to Auto, EAP-FAST, PEAP-GTC, PEAP-MSCHAPV2. This is a mandatory field
                                                         and it allows maximum length of 64 alphanumeric characters. WEP key Allows you to enter password for the network profile that you create. This field is available when you set the security mode to WEP. This is a mandatory field and it allows maximum length of 32
                                                         alphanumeric characters. Passphrase Allows you to enter password for the network profile that you create. You need to enter this value when the security mode
                                                         is PSK. Frequency band Allows you to select the wireless signal frequency band that is used in the WLAN. Options are: Auto 2.4 GHz 5 GHz Default: Auto | Parameter | Description | Security mode | Allows you to select the authentication method that is used to secure access to the Wi-Fi network. Depending on the method
                                                         you choose, a password, passphrase, or key field appears so that you can provide the credentials that are required to join
                                                         this Wi-Fi network. Options are: Auto EAP-FAST PEAP-GTC PEAP-MSCHAPV2 PSK WEP None Default: PSK | Network name | Allows you to enter a name for the SSIDs. This name displays on the phone. Multiple profiles can have the same network name
                                                         with different security mode.This name displays on the phone. | User ID | Allows you to enter a user ID for the network profile. This field is available when you set the security mode to Auto, EAP-FAST, PEAP-GTC, PEAP-MSCHAPV2. This is a mandatory field
                                                         and it allows maximum length of 32 alphanumeric characters. | Password | Allows you to enter password for the network profile that you create. This field is available when you set the security mode to Auto, EAP-FAST, PEAP-GTC, PEAP-MSCHAPV2. This is a mandatory field
                                                         and it allows maximum length of 64 alphanumeric characters. | WEP key | Allows you to enter password for the network profile that you create. This field is available when you set the security mode to WEP. This is a mandatory field and it allows maximum length of 32
                                                         alphanumeric characters. | Passphrase | Allows you to enter password for the network profile that you create. You need to enter this value when the security mode
                                                         is PSK. | Frequency band | Allows you to select the wireless signal frequency band that is used in the WLAN. Options are: Auto 2.4 GHz 5 GHz Default: Auto |
| Parameter | Description |
| Security mode | Allows you to select the authentication method that is used to secure access to the Wi-Fi network. Depending on the method
                                                         you choose, a password, passphrase, or key field appears so that you can provide the credentials that are required to join
                                                         this Wi-Fi network. Options are: Auto EAP-FAST PEAP-GTC PEAP-MSCHAPV2 PSK WEP None Default: PSK |
| Network name | Allows you to enter a name for the SSIDs. This name displays on the phone. Multiple profiles can have the same network name
                                                         with different security mode.This name displays on the phone. |
| User ID | Allows you to enter a user ID for the network profile. This field is available when you set the security mode to Auto, EAP-FAST, PEAP-GTC, PEAP-MSCHAPV2. This is a mandatory field
                                                         and it allows maximum length of 32 alphanumeric characters. |
| Password | Allows you to enter password for the network profile that you create. This field is available when you set the security mode to Auto, EAP-FAST, PEAP-GTC, PEAP-MSCHAPV2. This is a mandatory field
                                                         and it allows maximum length of 64 alphanumeric characters. |
| WEP key | Allows you to enter password for the network profile that you create. This field is available when you set the security mode to WEP. This is a mandatory field and it allows maximum length of 32
                                                         alphanumeric characters. |
| Passphrase | Allows you to enter password for the network profile that you create. You need to enter this value when the security mode
                                                         is PSK. |
| Frequency band | Allows you to select the wireless signal frequency band that is used in the WLAN. Options are: Auto 2.4 GHz 5 GHz Default: Auto |
| Step 7 | Press Save . |

| Parameter | Description |
|---|---|
| Security mode | Allows you to select the authentication method that is used to secure access to the Wi-Fi network. Depending on the method
                                                         you choose, a password, passphrase, or key field appears so that you can provide the credentials that are required to join
                                                         this Wi-Fi network. Options are: Auto EAP-FAST PEAP-GTC PEAP-MSCHAPV2 PSK WEP None Default: PSK |
| Network name | Allows you to enter a name for the SSIDs. This name displays on the phone. Multiple profiles can have the same network name
                                                         with different security mode.This name displays on the phone. |
| User ID | Allows you to enter a user ID for the network profile. This field is available when you set the security mode to Auto, EAP-FAST, PEAP-GTC, PEAP-MSCHAPV2. This is a mandatory field
                                                         and it allows maximum length of 32 alphanumeric characters. |
| Password | Allows you to enter password for the network profile that you create. This field is available when you set the security mode to Auto, EAP-FAST, PEAP-GTC, PEAP-MSCHAPV2. This is a mandatory field
                                                         and it allows maximum length of 64 alphanumeric characters. |
| WEP key | Allows you to enter password for the network profile that you create. This field is available when you set the security mode to WEP. This is a mandatory field and it allows maximum length of 32
                                                         alphanumeric characters. |
| Passphrase | Allows you to enter password for the network profile that you create. You need to enter this value when the security mode
                                                         is PSK. |
| Frequency band | Allows you to select the wireless signal frequency band that is used in the WLAN. Options are: Auto 2.4 GHz 5 GHz Default: Auto |

| Step 1 | Press Applications . |
|---|---|
| Step 2 | Select Network configuration > Wi-Fi configuration > Wi-Fi status . You see the information: Wi-Fi status : Displays if the Wi-Fi is connected or disconnected. Network name : Indicates the name of the SSID. Signal strength : Indicates strength of the network signal. MAC address : Indicates MAC address of the phone. AP MAC address : Indicates MAC address of the access point (SSID). Channel : Indicated the channel on which the Wi-Fi network transmits and receives data. Frequency : Indicates the wireless signal frequency band that is used in the Wireless LAN. Security mode : Indicates the security mode that is set for the wireless LAN. |

| Step 1 | Press Applications . |
|---|---|
| Step 2 | Select Status > Wi-Fi messages . |
| Step 3 | Use the outer ring of the navigation cluster to scroll through the messages. |
| Step 4 | Press Details to view more details of the selected message. |
| Step 5 | (Optional) Press Clear to delete all the messages. |

| Tip | Push a softkey once, and Voice Feedback reads the feature that is associated with the key. Quickly push the softkey twice
                                                to execute the feature. |
|---|---|

| Step 1 | Press Applications . |
|---|---|
| Step 2 | Select Accessibility > Voice Feedback . |
| Step 3 | Select On to turn On Voice Feedback. |
| Step 4 | Press the Set softkey twice quickly to save your settings. |
| Step 5 | (Optional) If you want to disable Voice Feedback, select Off to turn off Voice Feedback, then press the Set softkey twice to make the change take effect. When you press the Set at the first time, you can hear the feature. After you press the Set at the second time, the Voice Feedback is disabled. |

| Step 1 | Press Applications on your phone, or press Select three times quickly to turn on Voice Feedback. |
|---|---|
| Step 2 | Select Accessibility , and navigate up and down using the Select button ring. Press Select when you hear the option for Voice Speed . |
| Step 3 | Navigate up and down to hear the various speed options. You will hear the number and name of each option. Press Select to choose and save a voice speed. 1 Slowest 2 Slower 3 Normal 4 Faster 5 Fastest |

| Step 1 | Press Applications on your phone, or press Select three times quickly to turn on Voice Feedback. |
|---|---|
| Step 2 | Select Accessibility , and navigate to Voice Volume using the Select button ring. |
| Step 3 | Press Select , and continue pressing until you hear each of the five available volume settings. Highest High Normal Low Lowest |
| Step 4 | Press the Set softkey twice to save your settings. |

| Step 1 | Press Settings on your phone. |
|---|---|
| Step 2 | Select Accessibility > Font size . |
| Step 3 | Press the Select button to check the font size options. Press Set to choose and save a font size. Regular Large The font size change is applied immediately. |

| Step 1 | Press Applications . |
|---|---|
| Step 2 | Select User preferences > Audio preferences > Noise removal . |
| Step 3 | From the Navigation cluster, press the Select button to enable or disable the feature. |
| Step 4 | Press Set to save the changes. |

| Step 1 | On the phone web page, click User Login > Voice > User . |
|---|---|
| Step 2 | In the Acoustic Setting section, set Noise Removal to Yes to enable the feature. If you don't want your phone to remove the background noises in a call or meeting, set Noise Removal to No . |
| Step 3 | Click Submit All Changes . |

| Step 1 | In your mobile phone, log in to Webex application with your account. |
|---|---|
| Step 2 | You see the QR code in the Desk available screen of the phone. Use the camera of your mobile and scan the QR code on the phone. After you scan the QR code, Signing in screen appears. You see Book this desk until screen which allows you to enter a time in hours until which you can use the desk. After you click Book , the Applying configuration screen appears for a while. After succesful sign in, the configuration is applied and the phone reboots and returns to the
                                          home screen. You notice the following changes in the phone and in the paired mobile. Your personal phone number is displayed on the workspace phone. If you press Applications , you see the Hot desking settings menu is added to the Information and settings screen. Your personal data syncs with the phone and Webex call logs sync with the phone's Recents list from the Webex cloud server.
                                                For example, if there is a missed call in your call logs, it will display on the phone screen. Also, you can access the Missed
                                                call screen and make a call back to that contact. You can search contact by "name" from Webex directory and make a call. If you access the Recents list, you see this call is logged. While you use the desk, there can be one of your Webex meetings notification pop-up. You can press Join to join the meeting. If you access the Recents list, you see this meeting is added to the list. In the mobile phone, open the Webex application and check the Connect to a Device list. You see the booked phone name, duration of the desk booking, and a sign-out button. |

| Sign out using any of the following: On the phone, press Applications . Then select Hot desking settings menu in the Information and settings screen and click Sign out in the Hot desking settings screen. A window appears with a notification: This will remove your desk booking and personal data from the device Click Sign out to confirm the action. On the mobile, open the Webex application and access the Booked Devices , click the Sign out button next to the booked phone name. After you sign out, your personal data and synced Webex call logs remove from the phone (desk). The user account and the phone
                                             number changes to workspace account. |
|---|

| Step 1 | Press the line key for a specific feature to enter mode management. |
|---|---|
| Step 2 | Do one of the following actions: Press the Edit mode softkey to select an operating mode. Press the Navigation cluster , up or down, to switch between the modes. The current switch back mode is displayed on the right side of the mode name. Press the Manual on or Manual off softkey to specify how to switch back to the normal operation mode: automatically or manually. For example, an operating mode <Mode name> Automatic switch will be changed to <Mode name> Manual switch after you press the Manual on softkey. It indicates that the operating mode retains until you manually switch back to a normal mode. Press the Set softkey. Press the Details softkey to view detailed time duration of a mode. Press the Extend softkey to add time extension to an operating mode or retain the current operating mode. Select Specify duration to add time extension to an operating mode. Press the Navigation cluster , up or down, to add time extension in minutes. The minimum value is 30 minutes. The value must be multiple of 30 and cannot
                                                         exceed 720 (12 hours). If this value is greater than 30 minutes, the phone displays the time in hours. However, the phone always displays Time extention ends at as a 24-hour system. Press the Set softkey. (Optional) After you extend an operating mode, the Extend softkey becomes Edit extend . Press this softkey and then select Switch manually . The current operating mode retains till you manually switch back to a normal mode. Select Switch manually . The current operating mode retains till you manually switch back to a normal mode. Note You cannot extend an operating mode that needs to be switched manually back to normal. Press the All features softkey for batch edit. Press Batch edit to list all features except the ones with mode-based forwarding disabled. Press the Navigation cluster , up or down, to switch between the features, and then press Select to select one or more features. Alternatively, select All features . Press the Edit mode softkey to select an operating mode. Only common operating modes will be displayed for batch edit. If there are no common modes available, the phone displays an
                                                   alert. Press the Set softkey. By default, the operating status is set to Switch manually for the mode you have selected during batch editing. Press the Revert mode softkey to return to the normal operating mode if this operating mode has a time extension or has been set to switch manually. | Note | You cannot extend an operating mode that needs to be switched manually back to normal. |
| Note | You cannot extend an operating mode that needs to be switched manually back to normal. |

| Note | You cannot extend an operating mode that needs to be switched manually back to normal. |
|---|---|

| LED Color | Operating Mode Status | Description |
|---|---|---|
| Green | Normal operating mode | The current routing follows the normal operating mode, even if in some periods there is no operating mode configured by your
                                          administrator. The feature's operating mode switches automatically under the following circumstances: The current mode reaches its end time. A higher precedence mode reaches its start time. |
| Amber | Automatic switch back exception (Start early) | You have switched the feature to an operating mode before its start time. This mode runs as an exception until its start time
                                          is reached. At this point, the mode automatically switches the feature back to normal operation. |
| Automatic switch back exception (Extended) | You have extended the operating mode before it reaches its end time. This mode runs as an exception until the extension end
                                          time is reached. That is, the mode's end time plus an extension of up to 12 hours. At this point, the mode automatically switches
                                          the feature back to normal operation. |
| Automatic switch back exception (Exception) | You have switched the feature to another operating mode that is running in its scheduled time, but the original operating
                                          mode takes precedence. The mode runs as an exception until its end time is reached. At this point, the mode automatically
                                          switches the feature back to normal operation. For example, there are Mode A (8 AM to 5 PM) and Mode B (12 PM to 1 PM). The administrator sets Mode B to have precedence
                                          over Mode A. Hence, the system operates in Mode B from 12 PM to 1 PM. If you switch Mode B to Mode A during this period, this
                                          exception occurs. In this exception state, Mode A remains active until 5 PM. |
| Red | Manual switch back exception (Switch manually) | You have switched the operating mode or extended the mode for manual switch back. The operating mode runs as an exception
                                          until you manually switches the feature back to normal operation or a different mode. |
| Gray (Off) | Mode-based fwd disabled Unrecognized | One of the following scenarios occurs: There is no operating mode associated with the feature. Mode-based forwarding is disabled. Your phone doesn’t receive a response from the server. |

| Step 1 | Press Applications . |
|---|---|
| Step 2 | Select Device administration > Restart . |
| Step 3 | Select OK to confirm that you want to reboot your phone. |