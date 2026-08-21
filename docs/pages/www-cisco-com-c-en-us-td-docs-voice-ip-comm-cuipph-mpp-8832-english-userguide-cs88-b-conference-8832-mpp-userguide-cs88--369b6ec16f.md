---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cuipph-mpp-8832-english-userguide-cs88-b-conference-8832-mpp-userguide-cs88--369b6ec16f
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cuipph/MPP/8832/english/userguide/cs88_b_conference-8832-mpp-userguide/cs88_b_conference-8832-user-guide_chapter_0110.html
retrieved_at: 2026-08-21T02:39:12.229475+00:00
---

Cisco IP Conference Phone 8832 Multiplatform Phone User Guide

# Cisco IP Conference Phone 8832 Multiplatform Phone User Guide

Updated: January 22, 2025

Chapter: Settings

## Chapter: Settings

# Settings

## Phone Settings Overview

Your administrator can configure the phone to make the setting menus available on the phone screen or on the phone web interface.
                              If you can't find a specific menu, contact your administrator.

## Change the Ringtone

You can set a ringtone for an incoming call.

Step 1

Press Settings .

Step 2

Select User preferences > Ringtone > Ext (n) - Ring tone , where n= extension number.

Step 3

Scroll through the list of ringtones and press Play to hear a sample.

Step 4

Press Select and then Set to save a selection.

## Turn on Do Not Disturb from the Phone Screen

Set do not disturb (DND) to silence your phone and suppress incoming call notifications when you need to avoid distractions.
                              You can suppress all incoming call notifications or you can suppress a specific caller notification.

Step 1

Press Settings .

Step 2

Select User preferences > Call preferences > Do not disturb .

If the Do not disturb menu doesn't display on the screen, contact your administrator.

Step 3

Select On to turn on DND or select Off to turn off DND.

Step 4

Press Set to save the setting.

## Forward Calls from Your Phone

You can set up your phone to forward incoming calls after navigating to the Call forward settings screen.

There are two other methods to set up the call forward services. To set up the call forward services by a specific softkey,
                              see Forward Calls . To set up the call forward services from the phone web page, see Forward Calls with the Phone Web Page .

### Before you begin

Your administrator must enable the call forward services.

Your administrator disables the feature activation code synchronization for call forward. If enabled, the screen Call forward settings changes to be ready-only, however you can still change the setting for the Call Forward All service by pressing Forward or Forward all on the main screen. For more information, see Activate Call Forward All with Feature Activation Code Synchronization .

Step 1

Press Settings .

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

## Assign a Ring Tone with the Phone Web Page

Step 1

On the phone web page, select User Login > Voice > Ext(n) , where (n) is the number of an extension.

Step 2

In Call Feature Settings area, choose a ringtone from the Default Ring drop-down list.

If you don't want to specify a ringtone for the phone line, choose No ring . Your phone doesn't ring when receiving an incoming call.

Step 3

Click Submit All Changes .

## Turn on DND from the Phone Web Page

Step 1

On the phone web page, select User Login > Voice > User .

Step 2

Under Supplementary Services , set DND Settings to Yes .

You can turn on DND on for all lines if your administrator hasn't enabled feature key sync (FKS).

Step 3

Click Submit All Changes .

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

## Adjust the Backlight Timer from Phone Web Page

You can save energy by disabling the backlight on the phone at a preset time. The phone's desktop remains visible, even with
                              the backlight off.

Step 1

On the phone web page, select User Login > Advanced > Voice > User .

Step 2

Under Screen , select a duration for the Back Light Timer parameter.

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

## Block an Anonymous Call

You can block an incoming call that does not have caller information for a specific line or all lines .

If your administrator has enabled synchronization of Anonymous Call Rejection between a line and a BroadSoft XSI service,
                              then your setting only applies to the specific line instead of all lines. Typically, the setting applies to all the lines,
                              except for the ones where the synchronization is enabled.

Step 1

Press Settings .

Step 2

Select User preferences > Call preferences > Block anonymous call .

Step 3

Select On if you want to block the call that does not have caller information, or select Off to allow the call.

Step 4

Press Set to save the setting.

## Block Caller ID

You can block your caller identification to prevent your name and phone number from being displayed on the receiver's screen
                              when you make a call. This feature helps you to maintain privacy.

### Before you begin

Your administrator enables Block CID feature on your phone.

Your administrator enables Block CID feature on the XSI BroadWorks server.

Step 1

Press Settings .

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

## Enable Call Waiting

You can enable call waiting for a specific line or all lines. If enabled, you can receive the call notification (a single
                              beep and the line button flashes red) while on an active call.

If your administrator has enabled synchronization of Call Waiting between a line and a BroadSoft XSI service, then your setting
                              only applies to the specific line instead of all lines. Typically, the setting applies to all lines, except for the ones where
                              the synchronization is enabled.

Step 1

Press Settings .

Step 2

Select User preferences > Call preferences > Call waiting .

Step 3

Select On to allow you to answer an incoming call that rings while on another call, or select Off to disable the function.

Step 4

Press Set to save the setting.

## Secure a Call

You can encrypt calls to protect them from eavesdroppers. You can set up the secure call feature on all outbound calls or
                              for a specific call.

Step 1

Press Settings .

Step 2

Select User preferences > Call preferences > Secure call .

Step 3

Select On to enable secure call feature or select Off to disable the secure call feature.

Step 4

Press Set to save the setting.

## Set Up an Auto Answer Page

Step 1

Press Settings .

Step 2

Select User preferences > Call preferences > Auto answer page .

Step 3

Select On to enable the Auto answer page or select Off to disable Auto answer page.

Step 4

Press Set to save the changes.

## Set Up Voicemail

Step 1

Press Settings .

Step 2

Select User preferences > Call preferences > Voice mail .

Step 3

Enter a phone number to check voicemail.

Step 4

Press Set to confirm the assigned number.

Step 5

Press Back to exit.

## HTTP Proxy Settings

You can set up an HTTP proxy on your phone from the HTTP proxy settings menu under the Network configuration menu. The HTTP proxy settings are also available on the phone web page.

### Set Up a Proxy Server with the Auto Proxy Mode

Step 1

Press Settings .

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

Press Settings .

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

## Change the Time Format

You can change the current  time format that the phone screen displays.

Step 1

Press Settings .

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

Press Settings .

Step 2

Select Device administration > Date/Time > Date format .

Step 3

Select a date format and press Set to apply the changes.

## Change the Screen Saver

You can enable your phone screen saver, and specify its appearance and the amount of time for the phone to be idle before
                              the screen saver appears.

Step 1

Press Settings .

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

Trigger interval —Enter the number of seconds that the phone remains idle before the screen saver turns on.

Refresh interval —Enter the number of seconds before the screen saver should refresh (if, for example, you chose a rotation of pictures).

Step 5

Press Set .

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

Logo : In the phone web page you can select Logo as your phone background option. The logo that you add in the Logo URL is used as the wallpaper.

Caution

Do not exceed a maximum length of 255 characters for the Logo URL or Picture Download URL .

The logo display area is the center of the phone screen. The logo display area size of the phone is 128x128 pixels. If original
                                                logo size does not fit display area, the logo scales to fit the display area.

Step 3

Click Submit All Changes .

## Set Language

Depending upon how your phone is configured, you may be able to change the language used by your phone.

Step 1

Press Settings .

Step 2

Select Device administration > Language .

Step 3

Select a language from the list of available languages.

Step 4

Select Save .

## Set Password

### Before you begin

Step 1

Press Settings .

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

Press Settings .

Step 2

Select Device administration > Profile account setup .

Step 3

Press Sign in to save your username and password.

If any of the Username field or the Password field is empty, the phone displays a grey Sign in softkey and you can't press the softkey.

Step 4

(Optional) Enter a new username and password if you want to login with another set of credentials.

## Add Multiple Locations for a BroadWorks XSI User

### Before you begin

Step 1

Press Settings .

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

## Voice Feedback (Multiplatform Phones Only)

Voice feedback helps people who have trouble seeing use their Cisco IP phone. When enabled, a voice prompt helps you navigate
                              your phone buttons, and to use and configure phone features. The voice feedback also reads incoming caller IDs, displayed
                              screens and settings, and button functions. When on a call, only you hear voice feedback so your privacy is assured.

One of the methods to enable and disable voice feedback is to use the Select button that is located in the center of the Navigation bar. When the phone is idle, quickly press Select three times to turn this feature on or off. A voice prompt alerts you to the feature status.

Tip

After voice feedback is enabled, press a softkey once, and voice feedback reads the feature that is associated with the key.
                                          Quickly press the softkey twice to execute the feature.

Voice feedback is only available for English language users. If this feature is not available to you, then it is disabled
                                          on your phone.

### Enable or Disable Voice Feedback

Voice feedback helps people who have trouble seeing use their Cisco IP phone. When the phone is idle, you can enable or disable
                                 voice feedback by pressing the Settings button three times quickly. You can also access this feature from the Accessibility menu under Settings on your phone.

Step 1

Press the Settings button.

Step 2

Select Accessibility > Voice feedback .

Step 3

Select On to turn on voice feedback.

Step 4

Press the Set softkey twice quickly to save your settings.

Step 5

(Optional) If you want to disable voice feedback, select Off to turn off voice feedback, then press the Set softkey twice quickly to make the change take effect.

After you enable the voice feedback feature, your phone has the following behaviors.

Items

Behavior

Scrolling menu

When you press the Navigation bar to scroll through menus, the phone reads the highlight items.

Incoming call

When receiving an incoming call, the phone reads the caller ID twice.

All Calls list

In a multi-calls case, the phone reads the call state and Caller ID when you scroll through the items in the call list. For
                                                         example:

Active Call + Caller ID

Incoming Call + Caller ID

Held Call + Caller ID

Hard key

The phone reads the hard key name, such as number keys. For certain hard keys, the phone reads a hint. For example, "Mute".

To enter the settings menu, press the Settings button twice quickly.

Softkey

When you press a softkey once, the phone reads the softkey label.

When you press a softkey twice quickly, the phone performs the action.

Home Screen

Whenever you return to the home page, the phone reads “Home Screen”. If there is a missed call, the phone reads  "Home Screen
                                                         + New missed call…".

### Adjust Voice Speed

You can customize the speed of voice feedback if it reads too quickly or too slowly. Voice feedback must be enabled before
                                 you can select a voice speed.

Step 1

Press the Settings button twice quickly.

Step 2

Select Accessibility > Voice speed .

Step 3

Press Select twice quickly. Navigate up and down to hear the various speed options. You will hear the number and name of each option.
                                          Press Select twice quickly to choose and save a voice speed.

- 1 Slowest

- 2 Slower

- 3 Normal

- 4 Faster

- 5 Fastest

### Adjust Voice Volume

The voice feedback feature also allows you to set the voice volume. Voice feedback must be enabled before you can select a
                                 voice volume.

Step 1

Press the Settings button twice quickly.

Step 2

Select Accessibility > Voice volume .

Step 3

Press Select twice quickly. Navigate up and down to hear hear each of the five available volume settings.

- Highest

- High

- Normal

- Low

- Lowest

Step 4

Press Select twice quickly to save your settings.

Adjusting voice feedback volume will not affect the handset, headset, speakerphone volume (off hook), and the ringer volume
                                             (on hook)

## Adjust Font Size

To have a better visual experience, you can adjust the size of the fonts that are displayed on the phone screen. Note that
                              the customization of the font size does not change few of the texts, such as the texts on the phone screen header row (the
                              current date and time), the texts on the bottom row (the softkey labels), and the texts in a prompt window.

Step 1

Press Settings on your phone.

Step 2

Select Accessibility > Font size .

Step 3

Press the Select button to check the font size options. Press Set to choose and save a font size.

- Regular

- Large

The font size change is applied immediately.

| Step 1 | Press Settings . |
|---|---|
| Step 2 | Select User preferences > Ringtone > Ext (n) - Ring tone , where n= extension number. |
| Step 3 | Scroll through the list of ringtones and press Play to hear a sample. |
| Step 4 | Press Select and then Set to save a selection. |

| Step 1 | Press Settings . |
|---|---|
| Step 2 | Select User preferences > Call preferences > Do not disturb . Note If the Do not disturb menu doesn't display on the screen, contact your administrator. | Note | If the Do not disturb menu doesn't display on the screen, contact your administrator. |
| Note | If the Do not disturb menu doesn't display on the screen, contact your administrator. |
| Step 3 | Select On to turn on DND or select Off to turn off DND. |
| Step 4 | Press Set to save the setting. |

| Note | If the Do not disturb menu doesn't display on the screen, contact your administrator. |
|---|---|

| Step 1 | Press Settings . |
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

| Step 1 | On the phone web page, select User Login > Voice > Ext(n) , where (n) is the number of an extension. |
|---|---|
| Step 2 | In Call Feature Settings area, choose a ringtone from the Default Ring drop-down list. If you don't want to specify a ringtone for the phone line, choose No ring . Your phone doesn't ring when receiving an incoming call. |
| Step 3 | Click Submit All Changes . |

| Step 1 | On the phone web page, select User Login > Voice > User . |
|---|---|
| Step 2 | Under Supplementary Services , set DND Settings to Yes . You can turn on DND on for all lines if your administrator hasn't enabled feature key sync (FKS). |
| Step 3 | Click Submit All Changes . |

| Step 1 | On the phone web page, select Voice > User . |
|---|---|
| Step 2 | In the Screen section, set up the fields as described in the following table. Parameter Description Screen Saver Enable Select Yes to enable a screen saver on the phone. When the phone is idle for a specified time, it enters screen saver mode. Default: No Screen Saver Type Types of screen saver. Options you can choose: Clock —Displays a digital clock on a plain background. Download Picture —Displays a picture pushed from the phone webpage. Logo : Displays a logo on the phone screen. Add a logo image in the Logo URL field. Screen Saver Wait Amount of idle time before screen saver displays. Enter the number of seconds of idle time to elapse before the screen saver starts. Default: 300 Picture Download URL URL locating the (.png) file to display on the phone screen background. If you select picture as as screensaver type, this
                                                      image displays as a screensaver on the phone screen. When you enter an incorrect URL to download a new wallpaper, the phone fails to upgrade to the newer wallpaper and displays
                                                      the existing downloaded wallpaper. If the phone does not have any wallpaper downloaded earlier, it displays a gray screen. Logo URL Enter a URL or path for the location where the logo image is saved. If you select logo as as screensaver type, this image
                                                      displays as a screensaver on the phone screen. | Parameter | Description | Screen Saver Enable | Select Yes to enable a screen saver on the phone. When the phone is idle for a specified time, it enters screen saver mode. Default: No | Screen Saver Type | Types of screen saver. Options you can choose: Clock —Displays a digital clock on a plain background. Download Picture —Displays a picture pushed from the phone webpage. Logo : Displays a logo on the phone screen. Add a logo image in the Logo URL field. | Screen Saver Wait | Amount of idle time before screen saver displays. Enter the number of seconds of idle time to elapse before the screen saver starts. Default: 300 | Picture Download URL | URL locating the (.png) file to display on the phone screen background. If you select picture as as screensaver type, this
                                                      image displays as a screensaver on the phone screen. When you enter an incorrect URL to download a new wallpaper, the phone fails to upgrade to the newer wallpaper and displays
                                                      the existing downloaded wallpaper. If the phone does not have any wallpaper downloaded earlier, it displays a gray screen. | Logo URL | Enter a URL or path for the location where the logo image is saved. If you select logo as as screensaver type, this image
                                                      displays as a screensaver on the phone screen. |
| Parameter | Description |
| Screen Saver Enable | Select Yes to enable a screen saver on the phone. When the phone is idle for a specified time, it enters screen saver mode. Default: No |
| Screen Saver Type | Types of screen saver. Options you can choose: Clock —Displays a digital clock on a plain background. Download Picture —Displays a picture pushed from the phone webpage. Logo : Displays a logo on the phone screen. Add a logo image in the Logo URL field. |
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
| Screen Saver Type | Types of screen saver. Options you can choose: Clock —Displays a digital clock on a plain background. Download Picture —Displays a picture pushed from the phone webpage. Logo : Displays a logo on the phone screen. Add a logo image in the Logo URL field. |
| Screen Saver Wait | Amount of idle time before screen saver displays. Enter the number of seconds of idle time to elapse before the screen saver starts. Default: 300 |
| Picture Download URL | URL locating the (.png) file to display on the phone screen background. If you select picture as as screensaver type, this
                                                      image displays as a screensaver on the phone screen. When you enter an incorrect URL to download a new wallpaper, the phone fails to upgrade to the newer wallpaper and displays
                                                      the existing downloaded wallpaper. If the phone does not have any wallpaper downloaded earlier, it displays a gray screen. |
| Logo URL | Enter a URL or path for the location where the logo image is saved. If you select logo as as screensaver type, this image
                                                      displays as a screensaver on the phone screen. |

| Step 1 | On the phone web page, select User Login > Advanced > Voice > User . |
|---|---|
| Step 2 | Under Screen , select a duration for the Back Light Timer parameter. |

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

| Step 1 | Press Settings . |
|---|---|
| Step 2 | Select User preferences > Call preferences > Block anonymous call . |
| Step 3 | Select On if you want to block the call that does not have caller information, or select Off to allow the call. |
| Step 4 | Press Set to save the setting. |

| Step 1 | Press Settings . |
|---|---|
| Step 2 | Select User preferences > Call preferences . |
| Step 3 | Select Block caller ID . |
| Step 4 | Press Select to toggle caller ID blocking on or off. If your administrator enables the block caller ID feature on the XSI BroadWorks server, your phone retrieves the value from
                                          the server and you see the value that your administrator sets on the server. You can then modify the value from the Block caller ID menu on the phone. |
| Step 5 | Press Set to save the change. |

| Step 1 | Press Settings . |
|---|---|
| Step 2 | Select User preferences > Call preferences > Call waiting . |
| Step 3 | Select On to allow you to answer an incoming call that rings while on another call, or select Off to disable the function. |
| Step 4 | Press Set to save the setting. |

| Step 1 | Press Settings . |
|---|---|
| Step 2 | Select User preferences > Call preferences > Secure call . |
| Step 3 | Select On to enable secure call feature or select Off to disable the secure call feature. |
| Step 4 | Press Set to save the setting. |

| Step 1 | Press Settings . |
|---|---|
| Step 2 | Select User preferences > Call preferences > Auto answer page . |
| Step 3 | Select On to enable the Auto answer page or select Off to disable Auto answer page. |
| Step 4 | Press Set to save the changes. |

| Step 1 | Press Settings . |
|---|---|
| Step 2 | Select User preferences > Call preferences > Voice mail . |
| Step 3 | Enter a phone number to check voicemail. |
| Step 4 | Press Set to confirm the assigned number. |
| Step 5 | Press Back to exit. |

| Step 1 | Press Settings . |
|---|---|
| Step 2 | Select Network configuration > HTTP proxy settings > Proxy mode . |
| Step 3 | Press the Select button of the navigation cluster to choose Auto . |
| Step 4 | Highlight Auto discovery (WPAD) , select On to turn on Web Proxy Auto-Discovery (WPAD) that is used to retrieve a PAC file automatically, select Off to turn off WPAD. By default, your phone uses WPAD in the auto proxy mode. |
| Step 5 | (Optional) If you turn off WPAD in the previous step, you need to further enter a valid Proxy Auto-Configuration (PAC) URL in PAC URL . For example: http://proxy.department.branch.example.com/pac If you don't have the PAC URL, contact your administrator. |
| Step 6 | Press Set to apply the settings. |

| Step 1 | Press Settings . |
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

| Step 1 | Press Settings . |
|---|---|
| Step 2 | Select Device administration > Date/Time > Time format . To set daylight savings, select Device administration > Date/Time > Daylight savings . Select On to turn on the daylight savings and select Off to turn it off. |
| Step 3 | (Optional) Select Device administration > Date/Time > Time zone . |
| Step 4 | Select a time format and press Set to apply the changes. |

| Step 1 | Press Settings . |
|---|---|
| Step 2 | Select Device administration > Date/Time > Date format . |
| Step 3 | Select a date format and press Set to apply the changes. |

| Step 1 | Press Settings . |
|---|---|
| Step 2 | Select User preferences > Screen preferences > Screen saver . |
| Step 3 | Select On to turn on screen saver and select Off to turn it off. |
| Step 4 | Select Screen saver settings to choose the settings: Screen saver type —Choose one of the following options: Clock —Displays a rounded clock with the wallpaper in the background. Download Picture —Displays a picture pushed from the phone web page. Logo : Displays a logo as the phone screensaver. This image is added in the Logo URL field of the pone web page. Trigger interval —Enter the number of seconds that the phone remains idle before the screen saver turns on. Refresh interval —Enter the number of seconds before the screen saver should refresh (if, for example, you chose a rotation of pictures). |
| Step 5 | Press Set . |

| Step 1 | On the phone web page, select User Login > Voice > User . |
|---|---|
| Step 2 | In the Screen section, select Logo from the Phone Background field and in the Logo URL field enter a URL or path for the location where the logo image is saved. |
| Step 3 | Click Submit All Changes . After the logo is added in the phone background, if you select Default from the Phone Background list and save the changes, the logo icon on the phone screen will disappear. |

| Step 1 | On the phone web page, select User Login > Voice > User . |
|---|---|
| Step 2 | In the Phone Background field of the Screen section, select any of the options as a phone wallpaper. Default : Phone does not have any wallpaper. If no wallpaper is added to the phone screen, the phone screen displays monochrome wallpaper. Logo : In the phone web page you can select Logo as your phone background option. The logo that you add in the Logo URL is used as the wallpaper. Caution Do not exceed a maximum length of 255 characters for the Logo URL or Picture Download URL . The logo display area is the center of the phone screen. The logo display area size of the phone is 128x128 pixels. If original
                                                logo size does not fit display area, the logo scales to fit the display area. | Caution | Do not exceed a maximum length of 255 characters for the Logo URL or Picture Download URL . |
| Caution | Do not exceed a maximum length of 255 characters for the Logo URL or Picture Download URL . |
| Step 3 | Click Submit All Changes . |

| Caution | Do not exceed a maximum length of 255 characters for the Logo URL or Picture Download URL . |
|---|---|

| Step 1 | Press Settings . |
|---|---|
| Step 2 | Select Device administration > Language . |
| Step 3 | Select a language from the list of available languages. |
| Step 4 | Select Save . |

| Step 1 | Press Settings . |
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

| Step 1 | Press Settings . |
|---|---|
| Step 2 | Select Device administration > Profile account setup . Your username and password are automatically filled. These fields are blank if your username and password were not added before. |
| Step 3 | Press Sign in to save your username and password. Note If any of the Username field or the Password field is empty, the phone displays a grey Sign in softkey and you can't press the softkey. | Note | If any of the Username field or the Password field is empty, the phone displays a grey Sign in softkey and you can't press the softkey. |
| Note | If any of the Username field or the Password field is empty, the phone displays a grey Sign in softkey and you can't press the softkey. |
| Step 4 | (Optional) Enter a new username and password if you want to login with another set of credentials. |

| Note | If any of the Username field or the Password field is empty, the phone displays a grey Sign in softkey and you can't press the softkey. |
|---|---|

| Step 1 | Press Settings . |
|---|---|
| Step 2 | Select User preferences > Call preferences . |
| Step 3 | Select Anywhere . |
| Step 4 | (Optional) Select a line if  BroadWorks Anywhere is configured on multiple lines. |
| Step 5 | Add contact number and name in the Locations screen. Maximum length of a name that you can enter is 25. You can also keep the Name field empty. Maximum length of a number that you can enter is 20. |
| Step 6 | Enable or disable the location. |
| Step 7 | Press Save to add the locations to the Locations list. |

| Tip | After voice feedback is enabled, press a softkey once, and voice feedback reads the feature that is associated with the key.
                                          Quickly press the softkey twice to execute the feature. |
|---|---|

| Note | Voice feedback is only available for English language users. If this feature is not available to you, then it is disabled
                                          on your phone. |
|---|---|

| Step 1 | Press the Settings button. |
|---|---|
| Step 2 | Select Accessibility > Voice feedback . |
| Step 3 | Select On to turn on voice feedback. |
| Step 4 | Press the Set softkey twice quickly to save your settings. |
| Step 5 | (Optional) If you want to disable voice feedback, select Off to turn off voice feedback, then press the Set softkey twice quickly to make the change take effect. After you enable the voice feedback feature, your phone has the following behaviors. Items Behavior Scrolling menu When you press the Navigation bar to scroll through menus, the phone reads the highlight items. Incoming call When receiving an incoming call, the phone reads the caller ID twice. All Calls list In a multi-calls case, the phone reads the call state and Caller ID when you scroll through the items in the call list. For
                                                         example: Active Call + Caller ID Incoming Call + Caller ID Held Call + Caller ID Hard key The phone reads the hard key name, such as number keys. For certain hard keys, the phone reads a hint. For example, "Mute". Note To enter the settings menu, press the Settings button twice quickly. Softkey When you press a softkey once, the phone reads the softkey label. When you press a softkey twice quickly, the phone performs the action. Home Screen Whenever you return to the home page, the phone reads “Home Screen”. If there is a missed call, the phone reads  "Home Screen
                                                         + New missed call…". | Items | Behavior | Scrolling menu | When you press the Navigation bar to scroll through menus, the phone reads the highlight items. | Incoming call | When receiving an incoming call, the phone reads the caller ID twice. | All Calls list | In a multi-calls case, the phone reads the call state and Caller ID when you scroll through the items in the call list. For
                                                         example: Active Call + Caller ID Incoming Call + Caller ID Held Call + Caller ID | Hard key | The phone reads the hard key name, such as number keys. For certain hard keys, the phone reads a hint. For example, "Mute". Note To enter the settings menu, press the Settings button twice quickly. | Note | To enter the settings menu, press the Settings button twice quickly. | Softkey | When you press a softkey once, the phone reads the softkey label. When you press a softkey twice quickly, the phone performs the action. | Home Screen | Whenever you return to the home page, the phone reads “Home Screen”. If there is a missed call, the phone reads  "Home Screen
                                                         + New missed call…". |
| Items | Behavior |
| Scrolling menu | When you press the Navigation bar to scroll through menus, the phone reads the highlight items. |
| Incoming call | When receiving an incoming call, the phone reads the caller ID twice. |
| All Calls list | In a multi-calls case, the phone reads the call state and Caller ID when you scroll through the items in the call list. For
                                                         example: Active Call + Caller ID Incoming Call + Caller ID Held Call + Caller ID |
| Hard key | The phone reads the hard key name, such as number keys. For certain hard keys, the phone reads a hint. For example, "Mute". Note To enter the settings menu, press the Settings button twice quickly. | Note | To enter the settings menu, press the Settings button twice quickly. |
| Note | To enter the settings menu, press the Settings button twice quickly. |
| Softkey | When you press a softkey once, the phone reads the softkey label. When you press a softkey twice quickly, the phone performs the action. |
| Home Screen | Whenever you return to the home page, the phone reads “Home Screen”. If there is a missed call, the phone reads  "Home Screen
                                                         + New missed call…". |

| Items | Behavior |
|---|---|
| Scrolling menu | When you press the Navigation bar to scroll through menus, the phone reads the highlight items. |
| Incoming call | When receiving an incoming call, the phone reads the caller ID twice. |
| All Calls list | In a multi-calls case, the phone reads the call state and Caller ID when you scroll through the items in the call list. For
                                                         example: Active Call + Caller ID Incoming Call + Caller ID Held Call + Caller ID |
| Hard key | The phone reads the hard key name, such as number keys. For certain hard keys, the phone reads a hint. For example, "Mute". Note To enter the settings menu, press the Settings button twice quickly. | Note | To enter the settings menu, press the Settings button twice quickly. |
| Note | To enter the settings menu, press the Settings button twice quickly. |
| Softkey | When you press a softkey once, the phone reads the softkey label. When you press a softkey twice quickly, the phone performs the action. |
| Home Screen | Whenever you return to the home page, the phone reads “Home Screen”. If there is a missed call, the phone reads  "Home Screen
                                                         + New missed call…". |

| Note | To enter the settings menu, press the Settings button twice quickly. |
|---|---|

| Step 1 | Press the Settings button twice quickly. |
|---|---|
| Step 2 | Select Accessibility > Voice speed . |
| Step 3 | Press Select twice quickly. Navigate up and down to hear the various speed options. You will hear the number and name of each option.
                                          Press Select twice quickly to choose and save a voice speed. 1 Slowest 2 Slower 3 Normal 4 Faster 5 Fastest |

| Step 1 | Press the Settings button twice quickly. |
|---|---|
| Step 2 | Select Accessibility > Voice volume . |
| Step 3 | Press Select twice quickly. Navigate up and down to hear hear each of the five available volume settings. Highest High Normal Low Lowest |
| Step 4 | Press Select twice quickly to save your settings. Adjusting voice feedback volume will not affect the handset, headset, speakerphone volume (off hook), and the ringer volume
                                             (on hook) |

| Step 1 | Press Settings on your phone. |
|---|---|
| Step 2 | Select Accessibility > Font size . |
| Step 3 | Press the Select button to check the font size options. Press Set to choose and save a font size. Regular Large The font size change is applied immediately. |