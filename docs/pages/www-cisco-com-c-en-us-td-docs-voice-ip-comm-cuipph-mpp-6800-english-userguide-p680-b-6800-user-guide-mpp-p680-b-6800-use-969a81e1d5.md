---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cuipph-mpp-6800-english-userguide-p680-b-6800-user-guide-mpp-p680-b-6800-use-969a81e1d5
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cuipph/MPP/6800/english/userguide/p680_b_6800-user-guide-mpp/p680_b_6800-user-guide-mpp_chapter_0101.html
retrieved_at: 2026-08-17T01:05:16.212780+00:00
---

Cisco IP Phone 6800 Series Multiplatform Phones User Guide

# Cisco IP Phone 6800 Series Multiplatform Phones User Guide

Updated: June 26, 2025

Chapter: Settings

## Chapter: Settings

# Settings

## Phone Settings Overview

Your administrator can configure the phone to make the setting menus available on the phone screen or on the phone web interface.
                              If you can't find a specific menu, contact your administrator.

## Settings Overview

You can customize your phone in a number of ways:

From the menus on the phone, accessed from the Applications button. The common settings menus are:

User preferences

Device administration

From the phone web page.

## User Preferences Menu

You can customize many settings for your phone from the User preferences menu. The menu groups settings according to functions.

### Call Preferences

The User preferences > Call preferences menu allows you to set the way your phone handles calls.

#### Forward Calls from Your Phone

You can set up your phone to forward incoming calls after navigating to the Call forward settings screen.

There are two other methods to set up the call forward services. To set up the call forward services by a specific softkey,
                                    see Forward Calls . To set up the call forward services from the phone web page, see Forward Calls with the Phone Web Page .

##### Before you begin

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

- (6821) Forward all —Specifies the target phone number to which you want to forward all incoming calls.

- (6841, 6851, and 6861) Forward all number —Specifies the target phone number to which you want to forward all incoming calls.

- (6821) Forward busy —Specifies the target phone number to which you want to forward the incoming call when the line is busy.

- (6841, 6851, and 6861) Forward busy number —Specifies the target phone number to which you want to forward the incoming call when the line is busy.

- (6821) Forward no answer —Specifies the target phone number to which you want to forward the coming call when the call isn't answered.

- (6841, 6851, and 6861) Fwd no answer number —Specifies the target phone number to which you want to forward the coming call when the call isn't answered.

If your administrator disables the feature key synchronization (FKS) and XSI sync for call forward on your phone, you can enter the value as number of seconds after which call needs to be forwarded.

If your administrator enables FKS or XSI sync for call forward on your phone, you can enter the value as number of rings after which call needs to be forwarded.

The call forward settings on the phone take effect only when FKS and XSI are disabled. For more information, consult your
                                                administrator.

Step 6

(Optional) Assign a target phone number by using the Contacts softkey.

In the Call forward settings screen, select any of the call forward service.

Select Forward all number , Forward busy number , or Fwd no answer number based on the call forward service that you selected, then press the Contacts softkey.

For 6821, the service names are Forward all , Forward busy , and Forward no answer .

Search for a contact. For more information, see Search for a Contact in the All Directories Screen .

Press Call to assign the target phone number.

Step 7

Press Set to apply the settings.

Step 8

Verify if the setting takes effect by looking for the call forward icon. The icon displays with a target number on the top left or middle of the phone screen.

After you enable any of the call forward services, the Forward or Forward all softkey changes to the Clr fwd or Clf fwd all respectively . You can press the softkey to disable the call forward service or services, while the target phone number still remains.

Clf fwd all disables only the Call Forward All service, Clf fwd disables all call forward services.

If the call forward settings on the phone don't take effect, consult your administrator.

#### Set up Voicemail on Your Phone

Step 1

Press Applications .

Step 2

Select User preferences > Call preferences .

Step 3

Enter your personal voicemail phone number in Voice mail .

Step 4

Press Set .

#### Block Caller ID

You can block your caller identification to prevent your name and phone number from being displayed on the receiver's screen
                                    when you make a call. This feature helps you to maintain privacy.

##### Before you begin

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

#### Block an Anonymous Call

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

#### Turn on Do Not Disturb for a Specific Line

Set do not disturb (DND) to silence your phone and suppress incoming call notifications when you need to avoid distractions.
                                    You can suppress all incoming call notifications or you can suppress a specific caller notification.

Step 1

Select a phone line using the Navigation cluster.

Step 2

Press Applications .

Step 3

Select User preferences > Call preferences > Do not disturb .

Step 4

Select On to turn on DND or select Off to turn off DND.

Step 5

Press Set to save the setting.

#### Control the Call Waiting Tone

When you are talking with someone and get another call, you can set the phone to give a call waiting tone.

Step 1

Press Applications .

Step 2

Select User preferences > Call preferences > Call waiting .

Step 3

Press On you want the call waiting tone, or press Off if you don't want the call waiting tone.

Step 4

Select Set to apply the changes.

#### Secure a Call

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

#### Set Up an Auto Answer Page

Step 1

Press Applications .

Step 2

Select User preferences > Call preferences > Auto answer page .

Step 3

Select On to enable the Auto answer page or select Off to disable Auto answer page.

Step 4

Press Set to save the changes.

#### Enable the Missed Call Shortcut

When you turn on the Missed call shortcut, you can use Call rtn softkey to call the person whose call you missed.

Step 1

Press Applications .

Step 2

Select User preferences > Call preferences > Missed call shortcut .

Step 3

Press On if you want to the shortcut, or press Off if you don't want the shortcut.

Step 4

Select Set to apply the changes.

#### Add Multiple Locations for a BroadWorks XSI User

##### Before you begin

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

#### Enable Call Waiting

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

### Audio Preferences

The User preferences > Audio preferences menu allows you to customize ringtones and how you prefer to answer calls.

#### Specify an Audio Device for a Call

You can connect an analog headset and a USB headset simultaneously to your phone. However, you can use only one headset at
                                    time.

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

#### Change the Ringtone

You can set a ringtone for an incoming call.

Step 1

Press Applications .

Step 2

Select User preferences > Ringtone > Ext (n) - Ring tone , where n= extension number.

Step 3

Scroll through the list of ringtones and press Play to hear a sample.

Step 4

Press Select and then Set to save a selection.

### Screen Preferences

The User preferences > Screen preferences menu allows you to set your phone screen display options.

#### Change the Screen Saver

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

Trigger interval —Enter the number of seconds that the phone remains idle before the screen saver turns on.

Refresh interval —Enter the number of seconds before the screen saver should refresh (if, for example, you chose a rotation of pictures).

Step 5

Press Set .

#### Set the Backlight Timer

You can adjust the length of time that the phone screen is bright before it automatically dims.

Step 1

Press Applications .

Step 2

Select User preferences > Screen preferences > Backlight timer .

Step 3

Press Select to scroll through the list and select a duration for which the backlight remains on:

10 seconds

20 seconds

30 seconds

Always On

Off

Step 4

Press Set to apply the selection.

#### Adjust the Phone Screen Brightness or Contrast

Step 1

Press Applications .

Step 2

Select User preferences > Screen preferences , then select Contrast level or Display brightness (For 6871 only).

Step 3

Press the Navigation cluster up or down to increase or decrease the contrast or brightness.

Step 4

Press Save .

#### Set the phone wallpaper

You can select the wallpaper (background) for the phone screen.

Step 1

Press Applications .

Step 2

Select User preferences > Screen preferences > Wallpaper .

Step 3

Press Select to scroll through the list and select a wallpaper.

Step 4

Press Set to apply the selection.

### Attendant Console Preferences

The User preferences > Attendant console preferences menu allows you to customize how calls display.

#### Change the Display Mode

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

## Wi-Fi Settings

Wi-Fi settings are available only on Cisco IP phone 6861 Multiplatform Phones.

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

The Wi-Fi Scan softkey doesn't display if Wi-Fi type is set to WPS .

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

### Turn the Wi-Fi On or Off from Your phone

You can enable or disable the wireless LAN of your phone from the Wi-Fi configuration menu. By default, the wireless LAN on your phone is enabled.

Step 1

Press Applications .

Step 2

Select Network configuration > Wi-Fi configuration > Wi-Fi .

Step 3

Press the Select button, to turn the Wi-Fi on or off.

Step 4

Press Set to save the changes.

### Turn the Wi-Fi On or Off from the Phone Web Page

You can enable or disable the wireless LAN of your phone from the phone web page. You turn on the Wi-Fi so that the phone
                                 connects to a wireless network automatically or manually. By default, the wireless LAN on your phone is enabled.

Step 1

On the phone web page, select User Login > Advanced > Voice > System .

Step 2

Go to the Wi-Fi Settings section and set the Phone-wifi-on field to Yes .

Step 3

Click Submit All Changes .

### Connect the Phone to a Wi-Fi Manually

When you set up a Wi-Fi profile, it provides you the options to connect the phone manually to a wireless network. You can
                                 establish the connection from the Wi-Fi profile screen or from the Setup Wi-Fi screen.

The top most Wi-Fi profile in the Wi-Fi profile screen gets connected automatically when the phone provisions.

#### Before you begin

Turn on the Wi-Fi of your phone.

Disconnect your phone with the wired network.

Step 1

Press Applications .

Step 2

Select Network configuration > Wi-Fi configuration > Wi-Fi profile .

Step 3

In the Wi-Fi profile screen, do any of the actions to connect to Wi-Fi.

- Select any of the configured Wi-Fi profile and click Connect .

- Press Scan and select one wireless in the Connect to Wi-Fi screen. In the Setup Wi-Fi screen, enter values in the fields and press Connect .

See the Profile Parameter table in the Set Up a Wi-Fi Profile from the Phone for the field values.

### Connect Your Phone to a Wireless Network with WPS

Wi-Fi Protected Setup (WPS) provides an easier way to connect your phone to a wireless network. With WPS, you don't need to
                                 enter detailed settings for the access point to connect as you do with the connection through Wi-Fi profile. You can either
                                 use the WPS button on your access point or the PIN code to connect to the network through WPS.

The WPS option is available only in the menu on the phone screen. On the phone web page, you can only configure your phone
                                 to connect to a wireless network using Wi-Fi profile.

#### Before you begin

Enable WPS on your access point.

Step 1

Press Applications .

Step 2

Select Network configuration > Wi-Fi configuration > Wi-Fi type .

Step 3

Press the navigation key to switch the Wi-Fi type to WPS .

Step 4

Press Set .

Step 5

Connect to the network using the WPS button on your access point.

Select Push-button configuration .

Press the WPS button on your access point.

The button name may vary on your access point.

Press Continue on your phone.

Step 6

Connect to the network using a PIN code.

Select PIN configuration .

Go to the web page of your access point and enter the PIN code.

The procedure of entering PIN code may vary on your access points. See the respective user guide of your access point for
                                                   more details.

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

You may experience issues related to Wi-Fi connection. You can gather information from the Wi-Fi status page to help your administrator troubleshoot.

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

the status of firmware memory when the free memory is less than 50K

the status of losing AP beacon when the phone can't receive signal from the AP

the status of no response for Wi-Fi authentication or association requests

the status of TX failure

the status of WPS connection failure

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

Cisco IP Phone 6821 Multiplatform Phones doesn't support VPN connection.

### Set Up a VPN Connection

If you want to set up the VPN connection from the phone web page, see Set Up a VPN Connection from the Phone Web Page .

Cisco IP Phone 6821 Multiplatform Phones doesn't support VPN connection.

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

Cisco IP Phone 6821 Multiplatform Phones doesn't support VPN connection.

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

## Executive Settings

Executive settings are available only on Cisco IP phone 6871 Multiplatform Phones.

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

Executive assistant settings are available only on Cisco IP phone 6871 Multiplatform Phones.

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

### Troubleshooting Executive Assistant Settings

#### Calls Fail Although Call Diversion Is On

Ensure that DND is not activated for your extension.

## Device Administration Settings

You can set some other preferences from the phone in the Device administration menu.

### Change the Time Format

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

### Change the Date Format

You can change the date format that you want to see on your phone screen.

Step 1

Press Applications .

Step 2

Select Device administration > Date/Time > Date format .

Step 3

Select a date format and press Set to apply the changes.

### Set Language

Depending upon how your phone is configured, you may be able to change the language used by your phone.

Step 1

Press Applications .

Step 2

Select Device administration > Language .

Step 3

Select a language from the list of available languages.

Step 4

Select Save .

### Set up Power Save

You can put your phone into power save mode when your phone is idle. If your phone is not idle, you can't turn power save
                                 on and you see a message on the screen.

In power save mode, your phone can't receive incoming calls.

The Cisco IP Phone 6821 Multiplatform Phones does not support power save.

When your phone is in power save mode, the screen is not lit and the Select button is lit. You press the Select button to wake up the phone.

Step 1

Press Applications .

Step 2

Select Device administration > Power save .

Step 3

Select OK .

### Set Password

#### Before you begin

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

### Set up the Profile Account

You need to enter the authentication credentials to resynchronize your phone with the provisioning profile when prompted with
                                 the Profile account setup screen.

If you missed the Profile account setup screen, you can also access it from the phone menu or the Setup softkey if available.

If the phone fails to sign in, contact your administrator.

#### Before you begin

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

### Reboot Your Phone

Step 1

Press Applications .

Step 2

Select Device administration > Restart .

Step 3

Select OK to confirm that you want to reboot your phone.

## Phone Web Page Preferences

You can customize some settings from the phone web pages.

### Assign a Ring Tone with the Phone Web Page

Step 1

On the phone web page, select User Login > Voice > Ext(n) , where (n) is the number of an extension.

Step 2

In Call Feature Settings area, choose a ringtone from the Default Ring drop-down list.

If you don't want to specify a ringtone for the phone line, choose No ring . Your phone doesn't ring when receiving an incoming call.

Step 3

Click Submit All Changes .

### Control Ringer Volume

You can control the ringer volume of an incoming call on the phone, or from the phone administration web page.

If your administrator restricts your ability to control the ringer volume, you can't perform this task from either the phone
                                 volume key or from the phone administration web page.

#### Before you begin

Your administrator must allow you to control the ringer volume.

To control the ringer volume do one of the following.

When your administrator restricts your ability to control the ringer volume, a message appears indicating that you have no
                                                            permission to change the ringer volume.

The valid value for the Ringer Volume parameter ranges from 0 to 15.

When your administrator restricts your ability to control the ringer volume, the Ringer Volume parameter doesn't appear under the Audio Volume section.

### Turn on DND from the Phone Web Page

Step 1

On the phone web page, select User Login > Voice > User .

Step 2

Under Supplementary Services , set DND Settings to Yes .

You can turn on DND on for all lines if your administrator hasn't enabled feature key sync (FKS).

Step 3

Click Submit All Changes .

### Configure the Screen Saver from the Phone Web Page

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

### Adjust the Backlight Timer from Phone Web Page

Step 1

On the phone web page, select User Login > Advanced > Voice > User .

Step 2

Under Screen , select a duration for the Back Light Timer parameter.

Step 3

In the LCD Contrast field, enter a number for the desired brightness.

### Add a Logo as a Phone Background

Step 1

On the phone web page, select User Login > Voice > User .

Step 2

In the Screen section, select Logo from the Phone Background field and in the Logo URL field enter a URL or path for the location where the logo image is saved.

Step 3

Click Submit All Changes .

After the logo is added in the phone background, if you select Default from the Phone Background list and save the changes, the logo icon on the phone screen will disappear.

### Enable Anonymous Call Blocking from the Phone Web Page

Step 1

On the phone web page, select User Login > Voice > User .

Step 2

Under Supplementary Services , set Block ANC Setting to Yes .

The setting applies to all lines, except for the ones where your administrator has enabled synchronization of Anonymous Call
                                             Rejection between the lines and the BroadSoft XSI service.

Step 3

Click Submit All Changes .

### Enable Call Waiting from the Phone Web Page

Step 1

On the phone web page, select User Login > Voice > User .

Step 2

Under Supplementary Services , set CW Setting to Yes .

The setting applies to all lines, except for the ones where your administrator has enabled synchronization of Call Waiting
                                             between the lines and the BroadSoft XSI service.

Step 3

Click Submit All Changes .

### Set Password from Phone Web Page

#### Before you begin

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

| Step 1 | Press Applications . |
|---|---|
| Step 2 | Select User preferences > Call preferences > Call forwarding to access the Call forward settings screen. |
| Step 3 | Select a call forward service. Forward all —Determines whether to forward all incoming calls to a target phone number. Forward busy —Determines whether to forward an incoming call to a target phone number when the line is busy. Forward no answer —Determines whether to forward an incoming call to a target phone number when the call isn't answered. |
| Step 4 | Enable the call forward service by pressing Select button of the Navigation cluster . |
| Step 5 | Assign a target phone number for the call forward service. (6821) Forward all —Specifies the target phone number to which you want to forward all incoming calls. (6841, 6851, and 6861) Forward all number —Specifies the target phone number to which you want to forward all incoming calls. (6821) Forward busy —Specifies the target phone number to which you want to forward the incoming call when the line is busy. (6841, 6851, and 6861) Forward busy number —Specifies the target phone number to which you want to forward the incoming call when the line is busy. (6821) Forward no answer —Specifies the target phone number to which you want to forward the coming call when the call isn't answered. (6841, 6851, and 6861) Fwd no answer number —Specifies the target phone number to which you want to forward the coming call when the call isn't answered. (all models) Fwd no answer delay —Assigns a response delay time for the no answer scenario. Note If your administrator disables the feature key synchronization (FKS) and XSI sync for call forward on your phone, you can enter the value as number of seconds after which call needs to be forwarded. If your administrator enables FKS or XSI sync for call forward on your phone, you can enter the value as number of rings after which call needs to be forwarded. The call forward settings on the phone take effect only when FKS and XSI are disabled. For more information, consult your
                                                administrator. | Note | If your administrator disables the feature key synchronization (FKS) and XSI sync for call forward on your phone, you can enter the value as number of seconds after which call needs to be forwarded. If your administrator enables FKS or XSI sync for call forward on your phone, you can enter the value as number of rings after which call needs to be forwarded. |
| Note | If your administrator disables the feature key synchronization (FKS) and XSI sync for call forward on your phone, you can enter the value as number of seconds after which call needs to be forwarded. If your administrator enables FKS or XSI sync for call forward on your phone, you can enter the value as number of rings after which call needs to be forwarded. |
| Step 6 | (Optional) Assign a target phone number by using the Contacts softkey. In the Call forward settings screen, select any of the call forward service. Select Forward all number , Forward busy number , or Fwd no answer number based on the call forward service that you selected, then press the Contacts softkey. For 6821, the service names are Forward all , Forward busy , and Forward no answer . Search for a contact. For more information, see Search for a Contact in the All Directories Screen . Press Call to assign the target phone number. You can find that the target phone number displays next to the call forward service. |
| Step 7 | Press Set to apply the settings. |
| Step 8 | Verify if the setting takes effect by looking for the call forward icon. The icon displays with a target number on the top left or middle of the phone screen. After you enable any of the call forward services, the Forward or Forward all softkey changes to the Clr fwd or Clf fwd all respectively . You can press the softkey to disable the call forward service or services, while the target phone number still remains. Clf fwd all disables only the Call Forward All service, Clf fwd disables all call forward services. If the call forward settings on the phone don't take effect, consult your administrator. |

| Note | If your administrator disables the feature key synchronization (FKS) and XSI sync for call forward on your phone, you can enter the value as number of seconds after which call needs to be forwarded. If your administrator enables FKS or XSI sync for call forward on your phone, you can enter the value as number of rings after which call needs to be forwarded. |
|---|---|

| Step 1 | Press Applications . |
|---|---|
| Step 2 | Select User preferences > Call preferences . |
| Step 3 | Enter your personal voicemail phone number in Voice mail . |
| Step 4 | Press Set . |

| Step 1 | Press Applications . |
|---|---|
| Step 2 | Select User preferences > Call preferences . |
| Step 3 | Select Block caller ID . |
| Step 4 | Press Select to toggle caller ID blocking on or off. If your administrator enables the block caller ID feature on the XSI BroadWorks server, your phone retrieves the value from
                                                the server and you see the value that your administrator sets on the server. You can then modify the value from the Block caller ID menu on the phone. |
| Step 5 | Press Set to save the change. |

| Step 1 | Press the Navigation cluster up or down to select a phone line. |
|---|---|
| Step 2 | Press Applications . |
| Step 3 | Select User preferences > Call preferences > Block anonymous call . |
| Step 4 | Select On if you want to block the call that does not have caller information, or select Off to allow the call. |
| Step 5 | Press Set to save the setting. |

| Step 1 | Select a phone line using the Navigation cluster. |
|---|---|
| Step 2 | Press Applications . |
| Step 3 | Select User preferences > Call preferences > Do not disturb . |
| Step 4 | Select On to turn on DND or select Off to turn off DND. |
| Step 5 | Press Set to save the setting. |

| Step 1 | Press Applications . |
|---|---|
| Step 2 | Select User preferences > Call preferences > Call waiting . |
| Step 3 | Press On you want the call waiting tone, or press Off if you don't want the call waiting tone. |
| Step 4 | Select Set to apply the changes. |

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

| Step 1 | Press Applications . |
|---|---|
| Step 2 | Select User preferences > Call preferences > Missed call shortcut . |
| Step 3 | Press On if you want to the shortcut, or press Off if you don't want the shortcut. |
| Step 4 | Select Set to apply the changes. |

| Step 1 | Press Applications . |
|---|---|
| Step 2 | Select User preferences > Call preferences . |
| Step 3 | Select Anywhere . |
| Step 4 | (Optional) Select a line if  BroadWorks Anywhere is configured on multiple lines. |
| Step 5 | Add contact number and name in the Locations screen. Maximum length of a name that you can enter is 25. You can also keep the Name field empty. Maximum length of a number that you can enter is 20. |
| Step 6 | Enable or disable the location. |
| Step 7 | Press Save to add the locations to the Locations list. |

| Step 1 | Press the Navigation cluster up or down to select a phone line. |
|---|---|
| Step 2 | Press Applications . |
| Step 3 | Select User preferences > Call preferences > Call waiting . |
| Step 4 | Select On to allow you to answer an incoming call that rings while on another call, or select Off to disable the function. |
| Step 5 | Press Set to save the setting. |

| Step 1 | Press Applications . |
|---|---|
| Step 2 | Select User preferences > Audio preferences > Preferred audio device . |
| Step 3 | Press Select to choose one of the options: None —Selects the last used audio device. Speaker —Selects the speakerphone as the audio device. Headset —Selects a headset as the audio device. |
| Step 4 | Press Set to save the selection. |

| Step 1 | Press Applications . |
|---|---|
| Step 2 | Select User preferences > Ringtone > Ext (n) - Ring tone , where n= extension number. |
| Step 3 | Scroll through the list of ringtones and press Play to hear a sample. |
| Step 4 | Press Select and then Set to save a selection. |

| Step 1 | Press Applications . |
|---|---|
| Step 2 | Select User preferences > Screen preferences > Screen saver . |
| Step 3 | Select On to turn on screen saver and select Off to turn it off. |
| Step 4 | Select Screen saver settings to choose the settings: Screen saver type —Choose one of the following options: Clock —Displays a rounded clock with the wallpaper in the background. Download Picture —Displays a picture pushed from the phone web page. Logo : Displays a logo as the phone screensaver. This image is added in the Logo URL field of the pone web page. Trigger interval —Enter the number of seconds that the phone remains idle before the screen saver turns on. Refresh interval —Enter the number of seconds before the screen saver should refresh (if, for example, you chose a rotation of pictures). |
| Step 5 | Press Set . |

| Step 1 | Press Applications . |
|---|---|
| Step 2 | Select User preferences > Screen preferences > Backlight timer . |
| Step 3 | Press Select to scroll through the list and select a duration for which the backlight remains on: 10 seconds 20 seconds 30 seconds Always On Off |
| Step 4 | Press Set to apply the selection. |

| Step 1 | Press Applications . |
|---|---|
| Step 2 | Select User preferences > Screen preferences , then select Contrast level or Display brightness (For 6871 only). |
| Step 3 | Press the Navigation cluster up or down to increase or decrease the contrast or brightness. |
| Step 4 | Press Save . |

| Step 1 | Press Applications . |
|---|---|
| Step 2 | Select User preferences > Screen preferences > Wallpaper . |
| Step 3 | Press Select to scroll through the list and select a wallpaper. |
| Step 4 | Press Set to apply the selection. |

| Step 1 | Press Applications . |
|---|---|
| Step 2 | Select User preferences > Attendant console preferences > Display mode . The following options are available: Name Ext Both |
| Step 3 | Choose the display mode and press Set . |

| Step 1 | Select a Wi-Fi network from the list. You see the following options: Scan —The phone scans again for available networks. Setup —Opens the Setup Wi-Fi page. Skip —You see the message If you skip this step, you will need to configure the network manually . If you confirm to skip the Connect to Wi-Fi page, the Wi-Fi Scan softkey displays. |
|---|---|
| Step 2 | Press Setup and complete the fields. |
| Step 3 | Press Connect . |

| Note | The Wi-Fi Scan softkey doesn't display if Wi-Fi type is set to WPS . |
|---|---|

| Step 1 | Press the Wi-Fi Scan softkey when it displays on the phone screen. The message Wireless scan in progress displays. After the scan completes, a list of networks is displayed. You see the following options: Scan —Scans again for available networks. Select —Opens the Setup Wi-Fi page. Cancel —Closes the network list. |
|---|---|
| Step 2 | Select a Wi-Fi network from the list. |
| Step 3 | Press Select and complete the fields. |
| Step 4 | (Optional) Press Save to save the setups as a Wi-Fi profile. You can connect to this network later with the profile. |
| Step 5 | Press Connect . |

| Step 1 | Press Applications . |
|---|---|
| Step 2 | Select Network configuration > Wi-Fi configuration > Wi-Fi . |
| Step 3 | Press the Select button, to turn the Wi-Fi on or off. |
| Step 4 | Press Set to save the changes. |

| Step 1 | On the phone web page, select User Login > Advanced > Voice > System . |
|---|---|
| Step 2 | Go to the Wi-Fi Settings section and set the Phone-wifi-on field to Yes . |
| Step 3 | Click Submit All Changes . |

| Step 1 | Press Applications . |
|---|---|
| Step 2 | Select Network configuration > Wi-Fi configuration > Wi-Fi profile . |
| Step 3 | In the Wi-Fi profile screen, do any of the actions to connect to Wi-Fi. Select any of the configured Wi-Fi profile and click Connect . Press Scan and select one wireless in the Connect to Wi-Fi screen. In the Setup Wi-Fi screen, enter values in the fields and press Connect . See the Profile Parameter table in the Set Up a Wi-Fi Profile from the Phone for the field values. |

| Step 1 | Press Applications . |
|---|---|
| Step 2 | Select Network configuration > Wi-Fi configuration > Wi-Fi type . |
| Step 3 | Press the navigation key to switch the Wi-Fi type to WPS . |
| Step 4 | Press Set . Push-button configuration and PIN configuration display under Wi-Fi type . Follow either one of the following steps to connect to the network. |
| Step 5 | Connect to the network using the WPS button on your access point. Select Push-button configuration . Press the WPS button on your access point. The button name may vary on your access point. Press Continue on your phone. |
| Step 6 | Connect to the network using a PIN code. Select PIN configuration . An 8-digit PIN code displays on your phone screen. Go to the web page of your access point and enter the PIN code. The procedure of entering PIN code may vary on your access points. See the respective user guide of your access point for
                                                   more details. |

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
| Step 5 | In the Edit profile screen, set the parameters as mentioned in the Profile Parameters table. Table 1. Profile Parameters Parameter Description Security mode Allows you to select the authentication method that is used to secure access to the Wi-Fi network. Depending on the method
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
| Step 6 | In the Setup Wi-Fi screen, set the parameters as mentioned in the Profile Parameters table. Table 2. Profile Parameters Parameter Description Security mode Allows you to select the authentication method that is used to secure access to the Wi-Fi network. Depending on the method
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
| Step 2 | Under the section HTTP Proxy Settings , set the parameters described in the following table: Table 3. HTTP Proxy Settings Parameter Description Proxy Mode Choose the proxy mode for the HTTP proxy setting. Options are: Auto Manual Off Default: Off Use Auto Discovery (WPAD) Select Yes to use the Web Proxy Auto-Discovery (WPAD) mechanism to automatically retrieve a Proxy Auto-Configuration (PAC) file. If the parameter is set to No , you must configure PAC URL . This parameter is available when you set Proxy Mode to Auto . Default: Yes PAC URL URL locating the PAC file. This parameter is available when you set Proxy Mode to Auto and Use Auto Discovery (WPAD) to No . Proxy Host Server address (hostname or IP address) of the proxy server. Do not provide the scheme ( http:// or https:// ). This parameter is available when you set Proxy Mode to Manual . Proxy Port Port number of the proxy server. This parameter is available when you set Proxy Mode to Manual . Proxy Server Requires Authentication If your proxy server requires authentication, select Yes . Otherwise, select No . The parameter configuration depends on the actual behaviour of the proxy server. This parameter is available when you set Proxy Mode to Manual . Username Enter a username of a credential user on the proxy server. This parameter is available when you set Proxy Mode to Manual and Proxy Server Requires Authentication to Yes . Password Enter a password of the specified username for the proxy authentication purpose. This parameter is available when you set Proxy Mode to Manual and Proxy Server Requires Authentication to Yes . | Parameter | Description | Proxy Mode | Choose the proxy mode for the HTTP proxy setting. Options are: Auto Manual Off Default: Off | Use Auto Discovery (WPAD) | Select Yes to use the Web Proxy Auto-Discovery (WPAD) mechanism to automatically retrieve a Proxy Auto-Configuration (PAC) file. If the parameter is set to No , you must configure PAC URL . This parameter is available when you set Proxy Mode to Auto . Default: Yes | PAC URL | URL locating the PAC file. This parameter is available when you set Proxy Mode to Auto and Use Auto Discovery (WPAD) to No . | Proxy Host | Server address (hostname or IP address) of the proxy server. Do not provide the scheme ( http:// or https:// ). This parameter is available when you set Proxy Mode to Manual . | Proxy Port | Port number of the proxy server. This parameter is available when you set Proxy Mode to Manual . | Proxy Server Requires Authentication | If your proxy server requires authentication, select Yes . Otherwise, select No . The parameter configuration depends on the actual behaviour of the proxy server. This parameter is available when you set Proxy Mode to Manual . | Username | Enter a username of a credential user on the proxy server. This parameter is available when you set Proxy Mode to Manual and Proxy Server Requires Authentication to Yes . | Password | Enter a password of the specified username for the proxy authentication purpose. This parameter is available when you set Proxy Mode to Manual and Proxy Server Requires Authentication to Yes . |
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
| Step 2 | Under the section VPN Settings , set the parameters described in the following table. Table 4. VPN Settings Parameter Description VPN Server IP address or FQDN of the VPN server. Default: Empty VPN User Name Enter a username for a credential user on the VPN server. Default: Empty VPN Password Enter a password of the specified username to access the VPN server. Default: Empty VPN Tunnel Group Enter a tunnel group assigned to the VPN user. Tunnel group is used to identify the group policy for the VPN connection. Default: Empty Connect on Bootup Choose whether your phone connects to the VPN server automatically after the phone reboots. Default: No | Parameter | Description | VPN Server | IP address or FQDN of the VPN server. Default: Empty | VPN User Name | Enter a username for a credential user on the VPN server. Default: Empty | VPN Password | Enter a password of the specified username to access the VPN server. Default: Empty | VPN Tunnel Group | Enter a tunnel group assigned to the VPN user. Tunnel group is used to identify the group policy for the VPN connection. Default: Empty | Connect on Bootup | Choose whether your phone connects to the VPN server automatically after the phone reboots. Default: No |
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
| Step 2 | Select Executive List . The Executive List screen displays a maximum of 10 executives on the phone. If your administrator configures more than one assistant on the phone, then the screen only displays the executives of the
                                             first available assistant. |

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
| Step 2 | Select Device administration > Language . |
| Step 3 | Select a language from the list of available languages. |
| Step 4 | Select Save . |

| Note | In power save mode, your phone can't receive incoming calls. The Cisco IP Phone 6821 Multiplatform Phones does not support power save. |
|---|---|

| Step 1 | Press Applications . |
|---|---|
| Step 2 | Select Device administration > Power save . |
| Step 3 | Select OK . |

| Step 1 | Press Applications . |
|---|---|
| Step 2 | Select Device administration > Set password . |
| Step 3 | Enter your current password in the Old password field. |
| Step 4 | Enter your new password in the New password  and the Reenter new password fields. |
| Step 5 | Select Save . |

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
| Step 2 | Select Device administration > Restart . |
| Step 3 | Select OK to confirm that you want to reboot your phone. |

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
| Step 3 | In the LCD Contrast field, enter a number for the desired brightness. |

| Step 1 | On the phone web page, select User Login > Voice > User . |
|---|---|
| Step 2 | In the Screen section, select Logo from the Phone Background field and in the Logo URL field enter a URL or path for the location where the logo image is saved. |
| Step 3 | Click Submit All Changes . After the logo is added in the phone background, if you select Default from the Phone Background list and save the changes, the logo icon on the phone screen will disappear. |

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

| Step 1 | On the phone web page, select Voice > System . |
|---|---|
| Step 2 | Under the section System Configuration , locate the parameter User Password , and click Change Password next to the parameter. |
| Step 3 | Enter your current password in the Old Password field. If you don't have a password, keep the field empty. |
| Step 4 | Enter your new password in the New Password field. |
| Step 5 | Click Submit . The message Password has been changed successfully. will display in the web page. |