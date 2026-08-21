---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-jabber-android-9-1-jaba-bk-j0ae313a-00-jabber-voice-android-faq-9-1-4-html-bbdc187b67
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/jabber/Android/9_1/JABA_BK_J0AE313A_00_jabber-voice-android-faq-9-1-4.html
retrieved_at: 2026-08-21T12:36:12.595557+00:00
---

Frequently Asked Questions: Cisco Jabber Voice 9.1(4) for Android

# Frequently Asked Questions: Cisco Jabber Voice 9.1(4) for Android

### Download Options

Updated: October 8, 2013

Frequently Asked Questions

# FAQs

Cisco Jabber Voice for Android lets you manage your work calls using either the Internet or your mobile voice network.

In this release, Cisco Jabber for Android is renamed to Cisco Jabber Voice for Android.

Cisco Jabber Voice is a separate product from the upcoming Cisco Jabber for Android application that will offer chat, presence, audio and video calling, voicemail, and conference escalations.

When you are in the office, you connect to the corporate Wi-Fi network directly. When you are away from the office, you typically need a VPN connection to your corporate network. You must set up this VPN connection before you use Cisco Jabber Voice. You can use the VPN with Wi-Fi or mobile data networks. Contact your system administrator if you need assistance.

For a list of supported devices, see the Release Notes .

Although not officially supported, Cisco Jabber Voice for Android runs on many Android Version 2.3, 4.0, and 4.1 devices with various limitations depending on the device. For information about running Cisco Jabber Voice for Android on unsupported devices, see the Cisco Support Forums .

## Setup

- Install

- Set Up

- Upgrade

### Install

Q.

I want to install Cisco Jabber Voice for Android . Where do I find it?

A.

Obtain the application from Google Play (formerly known as Google Android Market).

Q.

How do I install Cisco Jabber Voice for Android ?

A.

Install Cisco Jabber Voice for Android the same way that you normally install any application from Google Play on your Android device. If you need help, consult the user manual for your device, or contact your system administrator.

### Set Up

Q.

I'm signing in for the first time. What do I need to do?

A.

Complete the following steps:

If you cannot set up Cisco Jabber Voice for Android , see the tips in the troubleshooting section.

- If you are outside your corporate network, you must set up a VPN connection to connect to the corporate network before you set up Cisco Jabber Voice for Android . Contact your system administrator if you need assistance.

- Obtain your setup information (such as server addresses and credentials) from your system administrator.

- On the Installation screen, tap Open .

(For new Android users) Swipe the screen to the left or right to navigate through your applications.

- Read the licensing agreement and then tap Accept .

Depending on how your system administrator set up your account, the setup wizard may not display all the screens that are documented in this procedure. If you do not see a screen for a particular feature, skip to the next step.

- In the Device ID field, enter the device ID.

- In the Server Address field, enter the TFTP server address.

- Check the Use mobile data network check box.

- Click Continue to verify the change.

- Check the Use noncorporate Wi-Fi check box.

- Click Continue to verify the change.

- If desired, uncheck the Auto Start check box to prevent Cisco Jabber Voice from automatically starting each time your phone restarts.

- Tap Verify .

- If prompted, enter your SIP Digest Authentication username and password. SIP Digest Authentication is a security measure that your corporate calling system uses to authenticate your device.

- In the Username field, if the username is not already entered, enter your username.

- In the Password field, enter your password.

- Tap Done to hide the keyboard.

- Tap Verify .

If you do not want to set up your voicemail, tap Skip . You can also set up voicemail after installation.

If you do not want to set up your corporate directory, tap Skip . You can also set up the corporate directory after installation.

- Tap Save .

### Upgrade

Q.

How do I upgrade from Cisco Jabber for Android Release 9.x to Cisco Jabber Voice for Android Release 9.1(4)?

A.

To upgrade from Cisco Jabber for Android Release 9.x to Cisco Jabber Voice for Android Release 9.1(4), download the latest release from Google Play and overwrite the previous version of the product on your device.

## Basics

Q.

How do I access the Cisco Jabber Voice for Android settings?

A.

To access the Cisco Jabber Voice for Android settings, open Cisco Jabber Voice for Android , and then tap Menu > Settings .

Q.

Why do I need to stop other Internet calling applications before using Cisco Jabber Voice for Android ?

A.

If you run multiple Internet calling applications on your Android device, they can conflict with each other and cause unpredictable behavior. To prevent these conflicts, run one application at a time.

To stop an application, complete the following steps:

Android OS 4.1:

- Tap the Android Settings application.

- Depending on your OS, tap either Apps or Application manager .

- Tap the name of the application you want to stop.

- Tap Force stop .

Android OS 2.3:

- On the Android home screen, tap Menu > Settings > Applications > Manage applications .

- Tap the application name, and then tap Force stop .

Q.

What do the icons in the status bar mean?

A.

The icons indicate your connection status. Swipe down the status bar to view details.

Cisco Jabber Voice for Android is connected to your corporate calling system and the Phone Services features are available.

Cisco Jabber Voice for Android is not connected to your corporate calling system and the Phone Services features are unavailable.

To resolve connection issues, try one of the following:

- Check whether you were on a call using your mobile phone number (instead of your work phone number). When you are on a call using your mobile phone number, Cisco Jabber Voice for Android automatically disconnects until you end the call.

- Verify that you entered your account settings properly. In Cisco Jabber Voice for Android , tap Menu > Settings . Under Accounts , tap Phone Services .

- If you are inside your corporate network, check your Wi-Fi settings. If your status bar indicates that you are connected to a Wi-Fi network, verify that you are connected to the correct Wi-Fi network (that is, your corporate Wi-Fi network). To verify, open a browser and try to connect to an internal website.

- If you are outside of your corporate network, check your native Wi-Fi or mobile network settings. If you are using mobile data network, verify that you have a strong mobile network signal. If your network settings are correct, check whether your VPN is connected.

- Contact your system administrator for additional assistance.

Cisco Jabber Voice for Android has an active call.

Cisco Jabber Voice for Android has a call on hold.

Cisco Jabber Voice for Android has an error. Swipe down the status bar to view details about the error. For some error messages, you can tap the notification message to go to an associated screen or popup window to try to resolve the error.

Cisco Jabber Voice for Android lost the connection to the voicemail server. Swipe down the status bar to view details about the error. For some error messages, you can tap the notification message to go to an associated screen or popup window to try to resolve the error.

Q.

How do I view details about features that do not connect properly?

A.

If features do not connect properly, check the connection status. To view the connection status, complete the following steps:

- In Cisco Jabber Voice for Android , tap Menu > Settings .

- Under Accounts , check the connection status for the related feature.

- Connected: Feature is set up and connected properly.

- Connecting: Feature is currently making a connection attempt.

- Disconnected: Feature is set up but is not currently connected. For example, you see this connection status if the corporate network is not properly connected or the server is down.

- Error: Feature is not currently set up or connected. For example, you see an error if you enter an incorrect password.

Q.

How do I view my account settings?

A.

To view your account settings, complete the following steps:

- In Cisco Jabber Voice for Android , tap Menu > Settings .

- Phone Services: Settings for your corporate phone system.

- Directory: Settings for your corporate directory or Lightweight Directory Access Protocol (LDAP) server. If your system administrator did not set up your account for directory search, the application does not display the directory account.

- Voicemail: Settings for your corporate visual voicemail server. You see this setting only if your system administrator set up your account for visual voicemail. You do not see this setting if your system administrator set up your account for basic voicemail.

Q.

How do I set my Jabber calling options?

A.

If your administrator enabled the Dial via Office (DVO) feature, you can view and select different Jabber calling options.

Use these calling options to select whether Jabber places calls with your work number over the Internet or your mobile voice network.

Set Jabber calling options as follows:

- Tap Settings .

- In the Phone Services section, tap Jabber Calling Options .

- Always use Internet: Cisco Jabber Voice functions as an Internet phone, using Wi-Fi or your mobile data plan to make calls over the Internet with your work number.

- Always use DVO: Cisco Jabber Voice initiates calls with your work number, but uses the voice plan for your device for all calls.

- Automatically select: (Default) Cisco Jabber Voice automatically selects to use either the Internet or DVO, based on your network connection. The app functions as an Internet phone when on Wi-Fi, but uses the voice plan for your device when on mobile data networks.

- If the DVO Callback Number is not already specified, enter a phone number. When you use DVO, the corporate calling system calls you back to start all calls. The DVO callback number is usually your mobile phone number.

Q.

Why does Cisco Jabber Voice for Android start automatically?

A.

When you first set up Cisco Jabber Voice for Android , you can choose whether to allow it to start automatically each time your device restarts. To change this setting, complete the following steps:

- In Cisco Jabber Voice for Android , tap Menu > Settings .

- Under General , turn off Auto Start to prevent Cisco Jabber Voice for Android from starting automatically.

Q.

How do I exit Cisco Jabber Voice for Android ?

A.

To exit Cisco Jabber Voice for Android , go to the Cisco Jabber Voice for Android home screen and tap Menu > Exit .

After you exit Cisco Jabber Voice for Android , it stops running in the background, disconnects from the server, and prevents you from making or receiving your work calls.

Cisco Jabber Voice for Android does not display the Exit menu on all screens. If you do not see the Exit menu, go back to the Cisco Jabber Voice for Android home screen.

If you turned on Auto Start , Cisco Jabber Voice for Android automatically starts after you boot your device.

## Connectivity

Q.

How do I use Cisco Jabber Voice when I’m not physically on-site at my office?

A.

To use Cisco Jabber Voice , you must connect to your corporate network. When you are in the office, you probably connect to the corporate network directly. When you are away from the office, you typically must have a VPN connection to your office network. You must set up this VPN connection before you use Cisco Jabber Voice . You can use the VPN with Wi-Fi or mobile data networks. If your administrator sets up DVO, the corporate calling system initiates the DVO calls over Wi-Fi or mobile data networks, and then places the calls over the mobile voice network. Contact your system administrator if you need assistance.

Q.

My administrator told me to install Cisco AnyConnect Secure Mobility Client so I can use Cisco Jabber Voice for Android outside my corporate Wi-Fi network. How do I do that?

A.

For information about how to install and use Cisco AnyConnect Secure Mobility Client on your Android device, see the latest Android end user guide for Cisco AnyConnect Secure Mobility Client in the user guide list .

Q.

I want to use Cisco Jabber Voice for Android with mobile data networks, but not with noncorporate Wi-Fi networks. Can I do that?

A.

If DVO is not enabled:

Yes. To prevent Cisco Jabber Voice for Android from connecting to the corporate calling system with noncorporate Wi-Fi networks over VPN, complete the following steps:

- In Cisco Jabber Voice for Android , tap Menu > Settings .

- Under General, turn on Use mobile data network .

- Under General, turn off Use noncorporate Wi-Fi .

If DVO is enabled:

No. Both Wi-Fi networks and mobile data networks are always turned on when DVO is enabled. Cisco Jabber Voice does not display options to turn noncorporate Wi-Fi and mobile data networks on or off individually.

Q.

I want to use Cisco Jabber Voice for Android with noncorporate Wi-Fi networks, but not with mobile data networks. Can I do that?

A.

If DVO is not enabled:

Yes. To prevent Cisco Jabber Voice for Android from connecting to the corporate calling system with mobile data networks over VPN, complete the following steps:

- In Cisco Jabber Voice for Android , tap Menu > Settings .

- Under General, turn off Use mobile data network .

- Under General, turn on Use noncorporate Wi-Fi .

If DVO is enabled:

No. Both Wi-Fi networks and mobile data networks are always turned on when DVO is enabled. Cisco Jabber Voice does not display options to turn noncorporate Wi-Fi and mobile data networks on or off individually.

Q.

What is low bandwidth mode?

A.

Cisco Jabber Voice for Android uses low bandwidth mode to optimize the audio for low bandwidth networks, which may improve call quality for Internet calls.

To use low bandwidth mode, one of the following must be true:

- Your system is set up to handle calls between devices that use different codecs

- Both your device and the device of the person you are calling support the same low bandwidth codec (G.729a or G.729b).

If you call a device that does not support the same low bandwidth codec, and the system is not set up to handle a codec mismatch, you may experience one of the following problems:

- You cannot hear audio

- The call is immediately disconnected

If you have questions about your system setup, contact your system administrator.

Q.

How do I turn on low bandwidth mode?

A.

To turn on low bandwidth mode, complete the following steps.

- In Cisco Jabber Voice for Android , tap Menu > Settings .

- Under Phone Services , turn on Use low bandwidth mode .

## Calls

Q.

What is the difference between making calls with my native phone application and Cisco Jabber Voice for Android ?

A.

When you make a phone call with your native phone application, the application uses your mobile phone number and your mobile service provider's voice network. The application uses your mobile voice plan to make the call, and displays the mobile voice number to the person you call.

When you make a phone call with Cisco Jabber Voice for Android , the application uses your work phone number and displays that work number to the person you call. Cisco Jabber Voice can use different networks to make these calls with your work number, depending on whether your administrator enables the DVO feature.

- Without DVO, Cisco Jabber Voice places calls with your work number using Wi-Fi or mobile data networks. In this case, Cisco Jabber Voice functions as an Internet phone.

- With DVO, Cisco Jabber Voice places calls over your mobile voice network, which uses your mobile voice plan. These calls are initiated either over Wi-Fi or your mobile data network, which uses your mobile data plan.

Q.

What calling features does Cisco Jabber Voice for Android support?

A.

Cisco Jabber Voice for Android supports the following calling features for Internet calls, which you might already be familiar with from using your Cisco Unified IP Phone:

- Conference: Allows you to talk simultaneously with multiple callers

- Transfer: Allows you to redirect a connected call from your phone to another number

- Hold: Allows you to put an active call into a held state

- Two calls: Supports two simultaneous calls, and lets you toggle between them

- VoIP over mobile voice network: Allows you to use your mobile voice network for VoIP calls if you leave a Wi-Fi network

Cisco Jabber Voice also supports the Dial via Office feature, which allows you to place calls with your work number using the voice plan for your device.

Q.

How do I make a call?

A.

Before you make a call, make sure your Android device is connected to your corporate network.

Cisco Jabber Voice for Android integrates with the standard Android Phone application. You can make calls from either the Android Phone application or the Cisco Jabber Voice for Android application. To make a call, complete the following steps:

From the Android Phone application:

- Tap the Phone icon on the Android home screen.

- Dial a number.

- Tap Jabber Voice to place your call using Cisco Jabber Voice for Android .

- Swipe the Phone icon to accept the call.

- If prompted, press any number on the keypad.

From the Cisco Jabber Voice for Android application:

- Tap the Phone tab on the Cisco Jabber Voice for Android home screen.

- Dial a number.

- If prompted, tap Jabber Voice to place your call using Cisco Jabber Voice for Android .

- Swipe the Phone icon to accept the call.

- If prompted, press any number on the keypad.

Q.

Can I set Cisco Jabber Voice for Android to use either my mobile number or my work number to make calls?

A.

Yes. Cisco Jabber Voice for Android integrates with the Android Phone application and allows you to choose whether you want to place calls with your native mobile phone number or your work number. To change this setting, complete the following steps:

- In Cisco Jabber Voice for Android , tap Menu > Settings .

- Tap Dial Options .

- Call using Cisco Jabber: (Default) Cisco Jabber Voice for Android to make all calls with your work number over your corporate network.

- Ask for every call: Allows you to choose which number to use to make each call.

- Call using my mobile phone: Uses the Android Phone application to make all calls with your mobile number over your mobile network.

Q.

How do I answer a call?

A.

You can answer calls using Cisco Jabber Voice for Android if you are connected to your corporate network.

When your device rings, do one of the following:

- If you are not already on a call when you receive the new incoming call, tap Accept .

- If you are already on a work call in the Cisco Jabber Voice application when you receive a new incoming work call, you can just decline the new call or accept it. If you accept the call, the new call is connected and the original call is placed on hold. If you decline the call, the device displays it as a received call in the standard call log on your Android device and the original call remains connected.

- If you are already on a work call in the native phone application when you receive a new incoming work call, you can ignore the new call or end your first call before you accept the new call.

Q.

How many calls does Cisco Jabber Voice for Android support at the same time?

A.

Cisco Jabber Voice supports one or two calls, depending on whether your administrator enabled the DVO feature.

If DVO is not enabled:

Cisco Jabber Voice acts like a two-line phone. If you are already connected to a call, you can receive or make another one. Only one call is active at a time; the other is automatically placed on hold. Tap Swap to toggle between the two calls.

If DVO is enabled:

Incoming work calls open in the native phone application. In these cases, Cisco Jabber Voice like a one-line phone.

Q.

How do I make a work call from the call log on my Android device?

A.

Before you make a work call, make sure your Android device is connected to your corporate network.

Cisco Jabber Voice for Android integrates with the standard call log on your Android device. You can access the call log from either the Android Phone application or the Cisco Jabber Voice for Android application.

To make a call from the call log, complete the following steps:

From the Android Phone application:

- On the Android home screen, tap the Phone icon.

- Tap the Logs tab.

- Tap the phone number that you want to call.

- Tap the Phone icon.

- If prompted, tap Jabber Voice to place your call using Cisco Jabber Voice for Android .

- Swipe the Phone icon to accept the call.

- If prompted, press any number on the keypad.

From the Cisco Jabber Voice for Android application:

- On the Cisco Jabber Voice for Android home screen, tap the Phone tab.

- Tap the Recents button ( ).

- Tap the phone number that you want to call.

- Tap the Phone icon.

- If prompted, tap Jabber Voice to place your call using Cisco Jabber Voice for Android .

- Swipe the Phone icon to accept the call.

- If prompted, press any number on the keypad.

After you save a contact, you can also call using an alternate method. Tap the contact's picture in the call log item, and then tap the Phone icon on the slider that appears.

Q.

How do I make a work call from Favorites?

A.

Before you make a work call, make sure your Android device is connected to your corporate network.

Cisco Jabber Voice for Android integrates with the native Favorites on your Android device. The procedure for making a work call from Favorites varies depending on your Android operating system.

To make a work call from Favorites, complete the following steps:

Android OS 4.0:

- On the Android home screen, tap the People icon or the Contacts icon (depending on your device).

- Tap the phone number that you want to call.

- If prompted, tap Jabber Voice to place your call using Cisco Jabber Voice for Android .

- Swipe the Phone icon to accept the call.

- If prompted, press any number on the keypad.

Android OS 2.3:

- On the Android home screen, tap the Phone icon.

- Tap the Favorites tab.

- Tap the name of the Favorite that you want to call.

- Tap the green Phone icon.

- If prompted, tap Jabber Voice to place your call using Cisco Jabber Voice for Android .

- Swipe the Phone icon to accept the call.

- If prompted, press any number on the keypad.

You can also tap the picture in the Favorites list, and then tap the Phone icon on the slider that appears.

Q.

How do I make a work call from Contacts?

A.

Before you make a work call, make sure your Android device is connected to your corporate network.

Cisco Jabber Voice for Android integrates with the standard Contacts on your Android device. To make a work call from Contacts, complete the following steps:

- Tap the Contacts icon on the Android home screen (or the Contacts tab if you are already in the Phone application).

- Tap a contact in the list.

- Tap the green Phone icon.

- If prompted, tap Jabber Voice to place your call using Cisco Jabber Voice for Android .

- Swipe the Phone icon to accept the call.

- If prompted, press any number on the keypad.

Q.

How do I make a second call from within the Cisco Jabber Voice for Android application?

A.

To make a second Internet call while on a Cisco Jabber Voice for Android Internet call, complete the following steps:

- While on a call, tap the Show more menu button and select Add Call .

- Tap Add Call .

- Make the new call. Cisco Jabber Voice for Android automatically places your first call on hold and displays the status of both calls.

- Tap Swap to toggle between connected calls.

Q.

How do I make a conference call from within the Cisco Jabber Voice for Android application?

A.

To make a conference call, complete the following steps:

- While on a call, tap More .

- Tap Add Call .

- Make the new call and wait for it to connect.

- Tap Merge .

Repeat the steps to add more people to the call.

Q.

How do I transfer a call from within the Cisco Jabber Voice for Android application?

A.

To transfer an Internet call, complete the following steps:

- While on a call, tap the Show more menu button and select Transfer .

- Dial the number to which you want to transfer the call, and then tap Complete Transfer either before or after the call is answered.

After you complete the transfer, the system automatically disconnects you from the original call.

Q.

How do I answer an incoming work call to Cisco Jabber Voice for Android while I am already on a call in the app?

A.

If you are already on an Internet call when a new call arrives to Cisco Jabber Voice for Android , the caller ID information for the new call appears on the screen. Tap Accept to answer the call and choose whether to put your current call on hold or end it.

If you are already on an Internet call when a new call arrives to Cisco Jabber Voice for Android , the caller ID information for the new call appears on the screen. Tap Accept to answer the call. The new call is connected, and the original call is placed on hold.

If you do not want to accept the call, tap Decline , and the system transfers the caller to your available voicemail system.

Q.

How do I toggle between two calls from within the Cisco Jabber Voice for Android application?

A.

When you are connected to two Internet calls, only one call is active at a time; the other is automatically placed on hold. Tap Swap to toggle between the two calls.

Q.

How do I end a call from within the Cisco Jabber Voice for Android application?

A.

Tap End .

Q.

How do I place a call on hold from within the Cisco Jabber Voice for Android application?

A.

While on an Internet call, tap Hold . To resume the call, tap Resume .

Q.

How do I put a call on hold when I have two Internet calls at the same time?

A.

When you are connected to two Internet calls, only one call is active at a time. Tap the call that is currently on hold, and the application automatically places the other call on hold.

Q.

Can I move my current Internet call from Cisco Jabber Voice for Android to my Cisco IP Phone?

A.

Yes, you can move your Internet call if your Cisco Jabber Voice for Android device and your Cisco IP Phone share the same directory number. To move your Internet call to your Cisco IP Phone, complete the following steps:

- While you are on a Cisco Jabber Voice for Android Internet call, place the call on hold.

If you do not resume the call on your Cisco IP Phone, you can resume the call on Cisco Jabber Voice for Android .

Q.

If I'm about to leave my corporate Wi-Fi network, can I move my current Cisco Jabber Voice for Android Internet call to my mobile network?

A.

Yes. This action moves the Internet call from Cisco Jabber Voice for Android to the Android Phone application.

This option is not available if you are connected to your corporate network using VPN over either your mobile data network or a noncorporate Wi-Fi network.

Before you move your call, make sure your mobile network signal is strong enough to receive calls. To move your call to your mobile network, complete the following steps:

- While on a call using Cisco Jabber Voice for Android , tap the Show more menu button.

- Tap Use mobile network . The system calls your device over the mobile voice network.

- Accept the incoming call. Cisco Jabber Voice for Android moves the call to the mobile voice network and the call continues within the standard Android Phone application.

- After you finish your conversation, tap End to end the call. After you end the call, the person that you were talking to hears music for a few seconds before the call disconnects.

Q.

Can I accept work calls while on a mobile voice call?

A.

If you are not using Cisco Jabber Voice for Android when you accept a mobile voice call, Cisco Jabber Voice for Android automatically disconnects while you are on the mobile voice call. Phone services are unavailable while you are on the active mobile voice call. After you end the mobile voice call, Cisco Jabber Voice for Android automatically reconnects.

However, if you set up Mobile Connect for your work number, the system passes work calls to you using your mobile network number. You can then handle those calls as you would any other mobile voice call.

Q.

What do I do if I get an incoming mobile voice call while on a Cisco Jabber Voice for Android Internet call?

A.

If you are on a Cisco Jabber Voice for Android Internet call and you receive an incoming mobile voice call, the call screen displays the incoming caller ID and you hear a call waiting tone. You can accept or decline the call:

If the Cisco Jabber Voice for Android call does not automatically appear, open Cisco Jabber Voice for Android to access the call again.

- Decline: Ignores the incoming mobile voice call (sends the call to the associated mobile number voicemail, if set up) and returns you to the Cisco Jabber Voice for Android Internet call.

## Contacts and Directory Search

Q.

When I used the Cisco Jabber Voice for Android setup wizard, I skipped the Directory screen. Can I still set up the application to search my directory?

A.

Yes. If you did not previously set up your corporate directory using the setup wizard, complete the following steps:

- In Cisco Jabber Voice for Android , tap Menu > Settings .

- Under Accounts , tap Directory .

- In the Username field, enter your username.

- In the Password field, enter your password.

- Tap Connect .

Q.

How do I search my corporate directory?

A.

To search the corporate directory, complete the following steps:

- In Cisco Jabber Voice for Android , tap the Directory tab, and then enter a name in the text box.

- In the search results, tap a name to see the contact details.

Q.

Why isn't directory search available?

A.

Cisco Jabber Voice displays your directory as disconnected until you make your first search.

If you have already completed a search, the directory search displays as not available if either the directory server is not available if either the directory server disconnected your device, or if the directory server is not reachable. If the problem persists, contact your system administrator.

Q.

How do I create a contact?

A.

To create a contact, complete the following steps:

- Search your corporate directory using Cisco Jabber Voice for Android .

- In the search results, tap a name to see the contact details.

- Tap Add to Contacts .

- Make any changes and then tap Save . The contact appears in the standard Android Contacts list.

Q.

Why did the directory search not show the person I looked for?

A.

Cisco Jabber Voice for Android limits the directory search results to 20 items. If your search is too broad, the application might not include your target in the results. Narrow your search by including more characters in your entry.

Q.

Why do the pictures of my corporate directory contacts not appear?

A.

Cisco Jabber Voice for Android does not currently support downloading images from corporate directory search results. However, you can edit the contact information to add a photo locally.

## Voicemail

- Basic Voicemail

- Visual Voicemail

### Basic Voicemail

Q.

How do I know if I have a voice message?

A.

After you receive a new voice message, the Voicemail icon appears in the status bar. Swipe down the status bar to see the number of new Cisco Jabber Voice for Android voice messages.

In addition, a new voice message notification appears on the Voicemail tab on the Cisco Jabber Voice for Android home screen.

Q.

How do I listen to my voice messages?

A.

Swipe down the status bar and tap the voice message notification, or tap the Voicemail tab in Cisco Jabber Voice for Android . Tap the Call Voicemail button to call your voicemail server and listen to your voice messages. After you listen to all your messages, Cisco Jabber Voice for Android removes the notification from both the status bar and the Voicemail tab.

### Visual Voicemail

Q.

What's the difference between basic voicemail and visual voicemail?

A.

The visual voicemail feature is an alternative to the basic voicemail service. With a basic voicemail service, you dial in to your voice mailbox and then respond to audio prompts. With visual voicemail, you use the screen on your device to work with your messages, rather than respond to audio prompts. You can see a list of your messages without having to dial in to your voice mailbox.

If your system administrator sets up visual voicemail, you can:

- Play or pause your messages

- If available, see a transcription of your messages

- Delete and restore messages

- Call back the contact who sent the message

Q.

How do I set up visual voicemail?

A.

If you did not already set up visual voicemail using the setup wizard, complete the following steps:

- In Cisco Jabber Voice for Android , tap Menu > Settings .

If your system administrator did not enable the visual voicemail feature, you do not see the Voicemail menu.

- In the Server Address field, if the address is not already entered, enter the voicemail server address. If you do not already have this information, contact your system administrator.

- (Optional) In the Port field, enter the voicemail server port.

- In the Username field, if the username is not already entered, enter your voicemail username.

- In the Password field, enter your voicemail password.

- Tap Verify .

Q.

How do I know if I have a visual voice message?

A.

After you receive a new visual voice message, the Voicemail icon appears in the status bar. Swipe down the status bar to see the number of new Cisco Jabber Voice for Android visual voice messages.

A new visual voice message notification also appears on the Voicemail tab on the Cisco Jabber Voice for Android home screen.

Q.

How do I listen to my visual voice messages?

A.

Complete the following steps:

- Swipe down the status bar and tap the visual voice message notification.

- Tap the Voicemail tab on the Cisco Jabber Voice for Android home screen.

- Tap the Play button to play the message in the list view.

- Tap anywhere else to play the message in the detail view.

- If prompted, tap Call voicemail to call the voicemail system.

Q.

Can I listen to my visual voice messages even if I'm not connected to my corporate network?

A.

Cisco Jabber Voice must be connected to your corporate network (either directly or remotely using VPN ) to receive new visual voice messages.

You can listen to your other saved visual voice messages even if you are not connected to your corporate network.

Q.

Can I call the voicemail system directly?

A.

Yes. In some cases, you may want to call the voicemail system directly instead of using the visual voicemail screens (for example, if a data network is not available and you want to use a traditional telephone user interface to check messages). To call the voicemail system directly, go to the Voicemail tab, and then tap Menu > Call Voicemail .

Q.

What is a secure visual voice message?

A.

Secure visual voice messages are encrypted on your device. Your system administrator can set the voicemail system to secure all corporate visual voice messages. If your visual voice messages are secured, you cannot distribute them outside your corporate voicemail system. Also, your system administrator can specify whether Cisco Jabber Voice for Android can download the messages.

Q.

What do the icons in the Voice Messages and Voice Message Details screens mean?

A.

The icons indicate the type of voice message.

Urgent message

Secure message

Q.

What do the buttons on the Voice Messages or Deleted Voice Messages screens do?

A.

The buttons function as follows:

Play: Tap this button to play the message.

Pause: Tap this button to pause the message.

Call back: Tap this button to call back the person who left the message.

Speaker: Tap this button to use speakerphone.

Delete: Tap this button to send the message to the Deleted Messages folder.

Undelete: Tap this button to move a deleted message from the Deleted Messages folder back to your inbox.

Read message: This button indicates that you have read the message. If you tap this button, the status of the message changes to unread.

Unread message: This button indicates that you have not read the message. If you tap this button, the status of the message changes to read.

Q.

How do I delete a visual voice message?

A.

To delete a visual voice message, complete the following steps:

- In Cisco Jabber Voice for Android , from either the Voice Messages or Voice Message Details screen, tap Delete to send the messages to the Deleted Messages folder.

- To view the contents of the Deleted Messages folder, tap Menu > Deleted Messages .

- To permanently delete the messages in the Deleted Messages folder, tap Menu > Empty Deleted Messages .

- Tap OK .

Q.

I accidentally deleted a visual voice message. Can I restore it?

A.

Yes. To restore a deleted message, complete the following steps:

- In the Cisco Jabber Voice for Android Voicemail tab, on the Voice Messages screen, tap Menu .

- Tap Deleted Messages .

- Tap and hold the message that you want to restore.

- Tap Undelete .

Q.

What ways can I communicate with my contacts from the Voice Messages screen?

A.

You can communicate with contacts using any method that is set up in the native Android Contacts application (for example, email or instant messaging).

Tap the contact's picture to view the communication options for that contact.

Q.

I see the voicemail connection error icon ( ) in the status bar. How do I resolve the error?

A.

Swipe down the status bar to view details about the error. For some error messages, you can tap the notification message to go to an associated screen or popup window to try to resolve the error. If you cannot resolve the error, contact your system administrator.

## Recents

Q.

How do I view my recents for calls that I made using Cisco Jabber Voice for Android ?

A.

The recents for all calls you made using Cisco Jabber Voice for Android appear in the standard call log on your Android device. To view your recents, complete the following steps:

- On the Android home screen, tap the Phone icon.

The native Android call log does not store Caller ID information that is obtained from a remote location. Therefore, you can see the Caller ID information during a Cisco Jabber Voice call, but only the number is stored in the native Android call log after the call ends.

You can add the contact to the native Android Contacts application to resolve the caller ID information.

Q.

How do I know if I missed a call?

A.

The device displays missed-call notifications in the status bar. Your Android device briefly displays the name and number of the caller. The Missed Call icon remains in the status bar until you open the standard call log on your Android device. To view details of a missed call, complete the following steps:

- Swipe down the status bar to view details about the missed call.

- Tap the missed-call notification to open the call log.

## Feedback and Troubleshooting

Q.

I'm trying to set up Cisco Jabber Voice for Android for the first time, but I can't get past the "Phone Services Settings" screen in the setup wizard. What can I do?

A.

If you cannot get past the "Phone Services Settings" screen in the setup wizard, try the following troubleshooting tips:

- Verify that you are using a supported device. For information about supported devices, see the Release Notes for your release.

- Verify that you are using the correct release of Cisco Jabber Voice for Android . You can download latest release of Cisco Jabber Voice for Android from the Google Play Store . If your administrator requested that you use a previous release of Cisco Jabber Voice for Android , contact your administrator for instructions for obtaining the Cisco Jabber Voice for Android software.

- On the Phone Services Settings screen, verify that the name in Device ID field starts with "BOT" . If the Device ID does not start with "BOT" , contact your administrator to correct the Device ID.

- On the Phone Services Settings screen, in Server Address field, verify that you entered the Fully Qualified Domain Name (FQDN) of your TFTP server instead of the hostname. If the issue is not resolved after you verify your Device ID and enter the FQDN of your TFTP server, check whether there is a TFTP or network issue that prevents your device from accessing TFTP server to download the TFTP file. If you need help, contact your administrator.

- Open your Internet browser.

- Try to access the administration pages for your corporate calling system by entering the following URL: http:// <your company's Cisco Unified Communication Manager server address> . For example, http://209.165.200.224. Contact your administrator if you do not have the address for your company's Cisco Unified Communication Manager server.

- If you cannot access the administration pages for your corporate calling system, try again from different access point. If you still cannot access the administration pages for your corporate calling system, then there may be a network issue. Contact your system administrator for assistance.

- Check if your VPN is connected (if VPN is required). If not, contact your system administrator.

- Tap the Android Settings application.

- Depending on your OS, tap either Apps or Application manager .

- Tap Jabber Voice .

- Tap Force stop .

- Tap Clear data .

- On the Android home screen, tap Menu > Settings > Applications > Manage applications .

- Tap Jabber Voice .

- Tap Force stop .

- Tap Clear data .

- If you still cannot set up Cisco Jabber Voice for Android , send a problem report to your administrator. See the procedure that follows.

Q.

My system administrator requested that I send a problem report by email. How do I do that?

A.

To send a problem report by email, complete the following steps.

The steps to send a problem report vary, depending on whether you completed the setup wizard for Cisco Jabber Voice for Android .

If you did not complete the setup wizard:

On Begin Setup screen, tap Menu > Help > Troubleshooting > Send Logs .

If you already completed the setup wizard:

- In Cisco Jabber Voice for Android , tap Menu > Settings . Cisco recommends that you set up the Email application on the Android device.

- Under Help , tap Send Logs .

- Check the Audio Engine Logs check box.

- Check the Configuration Files check box.

- Tap Send Logs . Your Email application launches with a new message that contains a repopulated subject line and attached log files.

- Enter a description of the problem in the body of the email message and send it to your system administrator.

If you can reproduce your problem, enable Detailed Logging by tapping Menu > Settings . Then, under Help , tap Troubleshooting . Check the Detailed Logging check box and reproduce your issue before you send the problem report.

In addition, include the timestamp when the problem occurred.

Q.

How do I send general feedback about Cisco Jabber Voice for Android ?

A.

To send general feedback about Cisco Jabber Voice for Android , complete the following steps:

- On the Cisco Jabber Voice for Android home screen, tap Menu > Feedback .

- Complete the feedback form.

Q.

Cisco Jabber Voice for Android stopped working and I see a red Cisco Jabber Voice icon ( ) in the status bar. What could be wrong?

A.

If Cisco Jabber Voice suddenly stops working, try the following troubleshooting tips:

- Check your Wi-Fi settings. If your status bar indicates that you are connected to a Wi-Fi network, verify that you are connected to the correct Wi-Fi network (that is, your corporate Wi-Fi network).

- Verify that you are connected to your corporate network by opening a browser and trying to connect to an internal website.

- If Cisco Jabber Voice still does not connect, verify your Wi-Fi settings.

- Open Cisco Jabber Voice for Android and tap Menu > Settings . Tap Corporate Wi-Fi Networks > Preset Wi-Fi Networks and verify that your network SSID is listed.

- If your network SSID is not listed in the Preset Wi-Fi Networks list, tap Menu > Settings . Tap Corporate Wi-Fi Networks > Custom Wi-Fi Networks . Locate the network SSID that you are connected to, and ensure that the check box is checked. If it is unchecked, check it and then exit Cisco Jabber Voice for Android and relaunch the application.

- Check if your VPN is connected (if VPN is required). If not, contact your system administrator.

- Check for the Cisco Jabber Voice for Android error icon ( ) in the status bar. If there is an error, swipe down the status bar to view details about the error. For some error messages, you can tap the notification message to go to an associated screen or popup window to try to resolve the error. If you have an error such as SIP digest authentication failure, a server error, or no network connectivity, contact your administrator for assistance.

- Check your account settings. In Cisco Jabber Voice for Android , tap Menu > Settings . Under Accounts, check whether any of your accounts have errors or are not connected. If so, contact your administrator for assistance.

- If you have more than one mobile device, check whether you are logged in twice on different mobile devices using the same "BOT" device ID. To test whether you are logged in twice, disable one device and contact your administrator to see if the corporate calling system shows that your device registered. If the device is registered, then you may have another Cisco Jabber Voice device that is registering with your account, which prevents your second device from functioning properly.

Q.

I'm on company premises and I'm connected to the Wi-Fi network, but I cannot get Cisco Jabber Voice for Android to work. What could be wrong?

A.

Check your Wi-Fi settings. If your status bar indicates that you are connected to a Wi-Fi network, verify that you are connected to the correct Wi-Fi network (that is, your corporate Wi-Fi network). To verify that you are connected to your corporate Wi-Fi network, open a browser and try to connect to an internal website.

If you are properly connected, Cisco Jabber Voice for Android should automatically connect.

If Cisco Jabber Voice still does not connect, verify your Wi-Fi settings using the following steps:

- In Cisco Jabber Voice for Android , tap Menu > Settings . Tap Corporate Wi-Fi Networks > Custom Wi-Fi Networks .

- Verify that the access point that you are connected to has a green check mark beside it. If not, tap the check box to add the green check mark.

Q.

I'm using Android OS 4.0 and Cisco Jabber Voice for Android won't connect to my calling system? Why not?

A.

Due to a limitation with some versions of Android OS 4.0, Cisco Jabber Voice cannot register to Cisco Unified Communications Manager on some devices. Cisco is working with select device manufacturers to resolve this issue at the Android OS level.

Q.

I see the Cisco Jabber Voice for Android icon ( ) in the status bar. How do I resolve the error?

A.

Swipe down the status bar to view details about the error. For some error messages, you can tap the notification message to go to an associated screen or popup window to try to resolve the error.

Q.

I can't see my Cisco Jabber Voice icon in the status bar when I'm connected. What could be wrong?

A.

Due to a limitation of Android OS, this problem can occur if you use Cisco Jabber Voice for Android with the Samsung Galaxy Nexus with Android OS 4.0.

To check your connection status, complete the following steps:

- In Cisco Jabber Voice for Android , tap Menu > Settings .

- Under Accounts , check the connection status for the related feature.

- Connected: Feature is set up and connected properly.

- Connecting: Feature is currently making a connection attempt.

- Disconnected: Feature is set up but is not currently connected. For example, you see this connection status if the corporate network is not properly connected or the server is down.

- Error: Feature is not currently set up or connected. For example, you see an error if you enter an incorrect password.

Q.

When I move outside of my corporate Wi-Fi network, it takes a long time for Cisco Jabber Voice for Android to register to the corporate calling system. What's wrong?

A.

Due to VPN limitations, Cisco Jabber Voice for Android can take over 2 minutes to register to the Cisco Unified Communications server after you transition from the corporate Wi-Fi network to the VPN.

Q.

Cisco Jabber Voice for Android does not ring when I have an incoming call, and the option to make a call using Cisco Jabber Voice is disabled or unavailable. What's wrong?

A.

Cisco Jabber Voice for Android must be registered to the server and running on your Android device to receive incoming calls. Verify the following:

- The device is connected to your corporate network. Verify your Wi-Fi settings to make sure you are still connected to your corporate network.

- The device is connected to a preferred Wi-Fi network. Verify your Custom Wi-Fi Networks settings to make sure you enable the Wi-Fi network to which you want to connect. On the Cisco Jabber Voice for Android home screen, tap Menu > Settings . Tap Corporate Wi-Fi Networks > Custom Wi-Fi Networks . Ensure that you check the desired Wi-Fi network check box to enable Cisco Jabber Voice for Android to register to the network.

Q.

When I received an incoming call to my mobile phone number, I noticed that the audible ringtone automatically changed to silent mode. What's wrong?

A.

This problem can occur if you use a Samsung Galaxy S II SGH-I777 (AT&T) with Android OS 2.3.6 while Cisco Jabber Voice for Android runs in the background, and you receive an incoming call to your mobile phone number. To resolve this issue, do the following:

- From the native Android settings, uncheck the silent mode check box.

- Exit and relaunch Cisco Jabber Voice for Android .

Q.

When I received an incoming work call on the Cisco Jabber Voice for Android application, I could not press Accept to answer the call. What is wrong?

A.

This problem can occur due to operating system limitations. To resolve this issue, lock the screen and then unlock it.

Q.

After I received an incoming mobile voice call when I was already on a Cisco Jabber Voice for Android call, Cisco Jabber Voice disconnected from the corporate calling system. What could be wrong?

A.

If your mobile voice service provider does not support simultaneous voice and data connections on your device, you may experience the following issues if you are already on a Cisco Jabber Voice for Android call and you receive a new incoming mobile voice call to your device:

- Cisco Jabber Voice for Android disconnects from the corporate calling server.

- You temporarily lose audio.

Q.

After I received an incoming mobile voice call when I was already on a Cisco Jabber Voice for Android call, I lost my audio connection. What could be wrong?

A.

If your mobile voice service provider does not support simultaneous voice and data connections on your device, you may experience the following issues if you are already on a Cisco Jabber Voice for Android call and you receive a new incoming mobile voice call to your device:

- Cisco Jabber Voice for Android disconnects from the corporate calling server.

- You temporarily lose audio.

Q.

Cisco Jabber Voice for Android shut down unexpectedly. What do I do?

A.

Restart the Cisco Jabber Voice for Android application. You do not need to enter your setup information again. If the problem persists, contact your system administrator.

Q.

I was already on a Cisco Jabber Voice for Android Internet call when I accepted a mobile voice call. After I ended the mobile voice call, I received a "Call failed" error for my Cisco Jabber Voice for Android Internet call. Why?

A.

Due to a limitation on certain mobile carriers, while Cisco Jabber Voice for Android is connected to a VPN, you may not be able to resume a Cisco Jabber Voice for Android Internet call after you accept an incoming mobile voice call and then end it quickly.

Q.

During an Internet call, I received a message that the call failed. After I tap OK on the message, the call log appears. Can I continue my call?

A.

Calls sometimes drop if:

- The device disconnects from the Wi-Fi. Look for the black Cisco Jabber Voice icon ( ) in the status bar to verify that Cisco Jabber Voice for Android is registered and available. Then, tap the call in the standard call log on your Android device to redial.

- The application must preregister. If your system administrator makes changes to your setup, the application preregisters twice (once, and again 30 seconds later). Look for the black Cisco Jabber Voice icon ( ) in the status bar to verify that Cisco Jabber Voice for Android is registered and available. Then, tap the call in the standard call log on your Android device to redial.

- You make a call to, or receive a call from a device that does not support the low bandwidth codec (G.729a or G.729b). In both cases, the call is immediately disconnected.

- You initiate a conference call with low bandwidth mode turned on, but the device of another person on the conference call does not support the same low bandwidth codec (G.729a or G.729b). You or the other person may be immediately disconnected from the conference call.

Q.

I turned on low bandwidth mode, but now I can't hear any audio on my Internet calls. Why not?

A.

To use low bandwidth mode, one of the following must be true:

- Your system is set up to handle calls between devices that use different codecs

- Both your device and the device of the person you are calling support the same low bandwidth codec (G.729a or G.729b)

If these conditions are not met, you may not be able to hear audio. To verify your system setup, contact your system administrator.

Q.

I was on an Internet call and the person I called could not hear my audio for a few seconds. What could be wrong?

A.

This problem can occur when you are roaming between access points within your corporate Wi-Fi network. Audio should return to normal within a few seconds.

Q.

I tried to move my Cisco Jabber Voice for Android Internet call to my mobile voice network, but the "Use mobile network" option was not available. Why not?

A.

The option to move your Cisco Jabber Voice for Android Internet call to your mobile voice network is not available if you are connected to your corporate network using VPN over either your mobile data network or a noncorporate Wi-Fi network.

Q.

When I received a Cisco Jabber Voice for Android call, I saw the person's caller ID, but now I can't see the caller ID in my recents list. Why not?

A.

The native Android call log does not store Caller ID information that is obtained from a remote location. Therefore, you can see the Caller ID information during a call, but only the number is stored in the native Android call log after the call ends.

You can add the contact to the native Android Contacts application to resolve the caller ID information.

Q.

Can I install Cisco Jabber Voice for Android on the SD card of my device?

A.

Cisco does not support the installation of Cisco Jabber Voice for Android on a Secure Digital (SD) card. Cisco Jabber Voice for Android must always run in the background to work properly. The Android OS terminates applications that you installed on the SD card when the SD card is mounted as a disk drive.

Q.

I'm trying to upgrade from Cisco Jabber for Android Release 8.6.x to Cisco Jabber Voice for Android Release 9.1.4, but the app won't install. Why not?

A.

To upgrade from Cisco Jabber for Android Release 8.6.x to Cisco Jabber Voice for Android Release 9.1.4, you must first uninstall the previous version of the product from your device.

Q.

With my previous version of Cisco Jabber Voice for Android , I used secure connect to connect to my corporate network from a remote location, but now I can't see that feature. Can I still use Cisco Jabber Voice for Android from a remote location?

A.

Yes, you can still use Cisco Jabber Voice for Android when you are away from your corporate Wi-Fi network if your administrator set up your system to use VPN. For more information, contact your administrator.

Q.

With my previous version of Cisco Jabber Voice for Android , I used secure connect to connect to my corporate network from a remote location, but now my administrator asked me to use a VPN client. Does Cisco Jabber Voice for Android work differently with a VPN client than it did with secure connect?

A.

Both secure connect and VPN allow you use Cisco Jabber Voice for Android to place work calls over the Internet when you are outside of your corporate network. However, VPN clients differ from secure connect as follows:

- VPN clients secure your whole device as opposed to the Cisco Jabber Voice for Android application only.

- VPN clients do not maintain active calls if you transition between your mobile data network and your corporate Wi-Fi network. Instead, you must either end your call or transfer it to your mobile voice network before you transition between networks.

- VPN clients re-register more frequently when you transition between networks.

Q.

I'm using a noncorporate Wi-Fi network, but I can't get Cisco Jabber Voice for Android to connect to my corporate network. What could be wrong?

A.

To resolve your connection issue, try one of the following:

- Check whether you are connected through VPN. When you are away from the office, you can use a Wi-Fi or mobile data network, but you also must use a VPN connection to your corporate network. You must set up this VPN connection before you use Cisco Jabber Voice for Android . Contact your system administrator if you need assistance.

- If DVO is not enabled, verify that you turned on the Use noncorporate Wi-Fi setting. In Cisco Jabber Voice for Android , tap Menu > Settings . Under General, verify that you turned on Use noncorporate Wi-Fi to enable your VPN to automatically connect to your corporate network when you are connected to a noncorporate Wi-Fi network.

Q.

My battery seems to drain faster when I use Cisco Jabber Voice for Android . What could cause this?

A.

Like other Android applications, Cisco Jabber Voice for Android consumes more power when used with a mobile data network.

In addition, some settings can cause high battery drain while Cisco Jabber Voice for Android is idle. To reduce battery drain, update your selected Custom Wi-Fi Networks. When Cisco Jabber Voice for Android is running in the background, it maintains a connection to the server. If this connection is lost, it continually tries to reconnect, which uses more power. To prevent this power drain, you can set Cisco Jabber Voice for Android to reconnect only when your device is connected to specific Wi-Fi networks (other than the networks that your system administrator presets, which you cannot change). Open Cisco Jabber Voice for Android and tap Menu > Settings . Tap Corporate Wi-Fi Networks > Custom Wi-Fi Networks .

Q.

When I use Cisco Jabber Voice for Android with Internet calling to participate in a Cisco WebEx conference, I have a hard time hearing participants and they have a hard time hearing me. What do I do?

A.

Tap Hold , and then tap Resume .

Q.

When I'm using VPN and Internet calling and my phone rings, the phone stops ringing before I can answer it. What can I do?

A.

Contact your system administrator to verify that the SIP dual-mode alert timer is set to the recommended value. Your administrator can set the SIP dual-mode alert timer value to extend the length of time that the systems rings the Cisco Jabber Voice for Android application.

Q.

I'm using VPN to connect to my corporate network and I answer an Cisco Jabber Voice for Android Internet call, but I can't hear audio and the caller gets sent to my voicemail. What could be the problem?

A.

If you answer an incoming Internet call when you use VPN to connect to your corporate network, the Accept signal sometimes cannot reach the corporate calling system because of network delays. As a result, the corporate calling system sends the call to voicemail. This problem occurs if the network does not communicate the acceptance to the calling server on time. For best results, connect to a better quality Wi-Fi or mobile data network.

Q.

During setup, Cisco Jabber Voice for Android prompted me for SIP Digest Authentication credentials, but my system administrator didn't give me that information. I entered some text and the application accepted it. Is my device authenticated properly?

A.

No. Contact your system administrator to verify that SIP Digest Authentication is set up properly on the system.

Q.

I can't download my voice messages using visual voicemail. Can I call the voicemail system directly?

A.

Yes. From the Voice Messages screen, tap Menu > Call Voicemail .

Q.

I see a notification that my voicemail credentials are not valid but I entered the correct username and password. What could cause this?

A.

You may see this message if your voicemail account is locked. Your voicemail account may be locked for either of the following reasons:

- Your voicemail administrator locks your account.

- The voicemail system locks your account after too many failed login attempts.

To resolve a locked voicemail account, contact your voicemail administrator.

Q.

I see a notification that I lost the connection to my voicemail server because of expired or invalid credentials, but I can't change my password. What can I do?

A.

You cannot change your voicemail password in Cisco Jabber Voice for Android . To resolve this issue, go to the Cisco Personal Communications Assistant (PCA) to change your password. To access your Cisco PCA, go to http:// <Cisco Unity Connection server> /ciscopca.

Q.

I was on the Deleted Voice Messages screen and after I declined an incoming call I did not see any more incoming calls. Why not?

A.

This is a known issue. To resolve this issue, tap the Search tab or place a Cisco Jabber Voice for Android call.

Q.

When I make an Internet call to certain numbers, the calls immediately drop. What could be wrong?

A.

Check your settings to see if low bandwidth mode is turned on. Calls sometimes drop if the system is not set up to handle codec mismatches and the device used by the person you called does not support the same low bandwidth codec (G.729a or G.729b). To resolve this issue, turn off low bandwidth mode and then retry.

To turn off low bandwidth mode, complete the following steps:

- In Cisco Jabber Voice for Android , tap Menu > Settings .

- Turn off Use low bandwidth mode .

Q.

Sometimes my directory search is slow or it doesn't work at all. What could be the problem?

A.

If you use a 3G mobile data network to remotely connect to your corporate network, network delays can cause issues with directory searches. For best results, you must connect to a better quality Wi-Fi or mobile data network.

Q.

When I check my call log, calls that I received in Cisco Jabber Voice for Android don't display correctly. What could be wrong?

A.

If you receive a call from someone who is not already in your contact list, the Android operating system uses a default format to display the call log entry. After the operating system applies the default format to the Cisco Jabber Voice for Android phone numbers, some phone numbers do not display correctly in the call logs. For example, the call log displays a call received from John Doe at 8-555-1234 as an Unknown caller at 855-512-34.

To resolve this issue, you can add new contacts to your contact list with the correct formatting. The call log recognizes phone numbers in your contact list and displays them using the formatting that you apply to the contact list entry.

Q.

I can't use silent mode or vibrate for my incoming Cisco Jabber Voice for Android calls. Why not?

A.

You cannot use silent mode or vibrate for incoming Cisco Jabber Voice for Android calls if your administrator set a minimum volume for the ringtone.

Q.

I can't change my ringtone for my Cisco Jabber Voice for Android calls. Why not?

A.

You cannot change the ringtone if your administrator set your device to always use the Cisco Jabber Voice ringtone for Cisco Jabber Voice for Android calls. When an administrator sets the app to use the Cisco Jabber Voice ringtone, only the calls on your native Android Phone application use the native Android ringtones.

Q.

I added a contact and entered some information in the Organization field, but I can't see the "Organization" title in the contact's information. What could be wrong?

A.

Due to device limitations, when using Samsung Galaxy S II SC-02C with Android OS 2.3.3, the device does not display the "Organization" title after you add a new contact and enter information for the contact's organization.

Q.

I'm having problems when I use my headset with Cisco Jabber Voice for Android . What could be wrong?

A.

- Called party hears poor audio quality

- Audio path is missing in one direction

- Audio is intermittently sent to the wrong audio channel

- Audio for a second call goes to handset instead of wired headset

If you use the official model of headset and you experience problems, contact your administrator for support.

Q.

When I use my earbuds with Cisco Jabber Voice for Android , the audio goes to my handset instead of the earbuds. What could be wrong?

A.

Verify that you check the checkbox to enable the earbuds as follows.

- Tap the Android Settings application.

- Tap Accessory .

- Check the Audio applications check box.

Q.

Why don't I see the Jabber calling options in my settings menu?

A.

Your administrator must enable the DVO feature before you can see the Jabber calling options in your settings menu. For more information, contact your administrator.

Q.

If I set my calling option to Always use DVO and try to make a DVO call, the call doesn’t connect. What could be wrong?

A.

This problem can occur if your administrator enabled the DVO feature on an unsupported version of the corporate calling server. Contact your system administrator to resolve this issue.

Q.

If I set my calling option to Automatically select and try to make a DVO call, the call doesn’t connect. What could be wrong?

A.

This problem can occur if you try to make a call from outside your corporate Wi-Fi network and your administrator enabled the DVO feature on an unsupported version of the corporate calling server. Contact your system administrator to resolve this issue.

Q.

Cisco Jabber Voice is prompting me for a DVO callback number. What is that?

A.

A DVO callback number is the phone number that the DVO feature uses to start calls. DVO allows you to place calls with your work number using the voice plan for your device. If your administrator enabled the DVO feature, the default setting is "Automatically select," which enables DVO when you are not on a Wi-Fi network. Cisco Jabber Voice checks to see if you or your administrator specified a callback number before making a DVO call. If a callback number is not already specified, the application prompts you to provide one. The DVO Callback number is usually your mobile phone number.

To use DVO, perform the following steps:

- In the DVO Callback Number field, enter the DVO callback number. This is usually your mobile phone number.

- Tap Save .

If you do not want to use DVO, perform the following steps:

- Tap Settings .

- Tap Jabber Calling Options .

- Select Always use Internet . With this option, Cisco Jabber Voice functions as an Internet phone, using Wi-Fi or your mobile data plan to make calls over the Internet with your work number.

Q.

My DVO Callback Number is prefilled, and the number is different than my mobile phone number. Can I change it?

A.

Yes. Cisco Jabber Voice for Android prefills your DVO Callback Number if your administrator entered a phone number in your Mobility Identity on the corporate calling system. To change this number, enter your mobile phone number in the DVO Callback Number field.

Q.

I tried to make a DVO call, but the person I called received a call from my voicemail system or a different number. What's wrong?

A.

When you place a DVO call, the person you call can receive a call from your voicemail system or a different number in the following cases:

- Your mobile voice network connection is weak. To prevent this issue, verify that you have a strong mobile voice network connection before you place a DVO call.

- You set up your DVO Callback Number with a phone number that is different than your mobile phone number. To prevent this issue, change your DVO Callback Number to your mobile phone number in the Cisco Jabber Voice settings. Select Settings > Jabber Calling Options , and then enter the new DVO Callback Number.

- You do not answer your callback in time and your device is set up with voicemail.

Q.

I tried to make a DVO call, but after I pressed any number on my keypad to connect the call, the call ended. What's wrong?

A.

Due to a limitation of the corporate calling system, calls end without notification if:

- You place a DVO call that requires you to enter a number before the system connects the call

- The person you call has a busy line and that person did not set up voicemail for the deskphone

If you encounter this issue, try calling the contact again at a later time. If the problem persists, contact your system administrator.

Q.

After I placed a DVO call, I heard several seconds of silence and then the call was dropped. What could be wrong?

A.

Due to a limitation of the corporate calling system, in some situations there is no audio message after you place a DVO call to an invalid phone number. To troubleshoot the problem, verify whether the phone number that you dialed is a valid phone number.

Q.

After I upgraded Cisco Jabber Voice for Android , the application registers to noncorporate Wi-Fi and mobile data networks even though I turned these settings off in the previous release. Why does this happen?

A.

If you upgrade Cisco Jabber Voice for Android and your administrator enabled the DVO feature, the application has different settings than previous releases.

Cisco Jabber Voice does not display options to turn noncorporate Wi-Fi and mobile data networks on or off individually. Instead, the application automatically turns on both noncorporate Wi-Fi networks and mobile data networks.

Q.

My administrator disabled the Dial via Office feature, and now my Corporate Wi-Fi Network setting is not displaying properly. What's wrong?

A.

If your administrator sets the Dial via Office feature from enabled to disabled on the device page for a user, you may see the wrong text or no text under the Corporate Wi-Fi Network field on the Settings screen. To resolve this issue, navigate away from the Settings menu and then navigate back to the Settings menu.

THE SPECIFICATIONS AND INFORMATION REGARDING THE PRODUCTS IN THIS MANUAL ARE SUBJECT TO CHANGE WITHOUT NOTICE. ALL STATEMENTS, INFORMATION, AND RECOMMENDATIONS IN THIS MANUAL ARE BELIEVED TO BE ACCURATE BUT ARE PRESENTED WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED. USERS MUST TAKE FULL RESPONSIBILITY FOR THEIR APPLICATION OF ANY PRODUCTS.

THE SOFTWARE LICENSE AND LIMITED WARRANTY FOR THE ACCOMPANYING PRODUCT ARE SET FORTH IN THE INFORMATION PACKET THAT SHIPPED WITH THE PRODUCT AND ARE INCORPORATED HEREIN BY THIS REFERENCE. IF YOU ARE UNABLE TO LOCATE THE SOFTWARE LICENSE OR LIMITED WARRANTY, CONTACT YOUR CISCO REPRESENTATIVE FOR A COPY.

The Cisco implementation of TCP header compression is an adaptation of a program developed by the University of California, Berkeley (UCB) as part of UCB's public domain version of the UNIX operating system. All rights reserved. Copyright © 1981, Regents of the University of California.

NOTWITHSTANDING ANY OTHER WARRANTY HEREIN, ALL DOCUMENT FILES AND SOFTWARE OF THESE SUPPLIERS ARE PROVIDED “AS IS" WITH ALL FAULTS. CISCO AND THE ABOVE-NAMED SUPPLIERS DISCLAIM ALL WARRANTIES, EXPRESSED OR IMPLIED, INCLUDING, WITHOUT LIMITATION, THOSE OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT OR ARISING FROM A COURSE OF DEALING, USAGE, OR TRADE PRACTICE.

IN NO EVENT SHALL CISCO OR ITS SUPPLIERS BE LIABLE FOR ANY INDIRECT, SPECIAL, CONSEQUENTIAL, OR INCIDENTAL DAMAGES, INCLUDING, WITHOUT LIMITATION, LOST PROFITS OR LOSS OR DAMAGE TO DATA ARISING OUT OF THE USE OR INABILITY TO USE THIS MANUAL, EVEN IF CISCO OR ITS SUPPLIERS HAVE BEEN ADVISED OF THE POSSIBILITY OF SUCH DAMAGES.

Any Internet Protocol (IP) addresses and phone numbers used in this document are not intended to be actual addresses and phone numbers. Any examples, command display output, network topology diagrams, and other figures included in the document are shown for illustrative purposes only. Any use of actual IP addresses or phone numbers in illustrative content is unintentional and coincidental.

Cisco and the Cisco logo are trademarks or registered trademarks of Cisco and/or its affiliates in the U.S. and other countries. To view a list of Cisco trademarks, go to this URL: http:/​/​www.cisco.com/​go/​trademarks . Third-party trademarks mentioned are the property of their respective owners. The use of the word partner does not imply a partnership relationship between Cisco and any other company. (1110R)

### This Document Applies to These Products

- Jabber for Android

| Q. | I want to install Cisco Jabber Voice for Android . Where do I find it? |
|---|---|

| A. | Obtain the application from Google Play (formerly known as Google Android Market). |
|---|---|

| Q. | How do I install Cisco Jabber Voice for Android ? |
|---|---|

| A. | Install Cisco Jabber Voice for Android the same way that you normally install any application from Google Play on your Android device. If you need help, consult the user manual for your device, or contact your system administrator. |
|---|---|

| Q. | I'm signing in for the first time. What do I need to do? |
|---|---|

| A. | Complete the following steps: Tip If you cannot set up Cisco Jabber Voice for Android , see the tips in the troubleshooting section. If you are outside your corporate network, you must set up a VPN connection to connect to the corporate network before you set up Cisco Jabber Voice for Android . Contact your system administrator if you need assistance. Obtain your setup information (such as server addresses and credentials) from your system administrator. Open Cisco Jabber Voice for Android using one of the following methods: On the Installation screen, tap Open . On the Android home screen, tap the Applications icon. Locate and tap the Cisco Jabber Voice icon. Tip (For new Android users) Swipe the screen to the left or right to navigate through your applications. Read the licensing agreement and then tap Accept . Tap Begin Setup . Important: Depending on how your system administrator set up your account, the setup wizard may not display all the screens that are documented in this procedure. If you do not see a screen for a particular feature, skip to the next step. On the Phone Services Settings screen: In the Device ID field, enter the device ID. In the Server Address field, enter the TFTP server address. If you want to allow Cisco Jabber Voice for Android to connect to the corporate calling system from your mobile data network over VPN, do the following: Check the Use mobile data network check box. Click Continue to verify the change. If you want to allow Cisco Jabber Voice for Android to connect to the corporate calling system from noncorporate Wi-Fi networks over VPN, do the following: Check the Use noncorporate Wi-Fi check box. Click Continue to verify the change. If desired, uncheck the Auto Start check box to prevent Cisco Jabber Voice from automatically starting each time your phone restarts. Tap Verify . If prompted, enter your SIP Digest Authentication username and password. SIP Digest Authentication is a security measure that your corporate calling system uses to authenticate your device. (Optional) If you see the Voicemail Settings screen: In the Username field, if the username is not already entered, enter your username. In the Password field, enter your password. Tap Done to hide the keyboard. Tap Verify . Note If you do not want to set up your voicemail, tap Skip . You can also set up voicemail after installation. (Optional) If you see the Directory Settings screen, enter your username and password. Note If you do not want to set up your corporate directory, tap Skip . You can also set up the corporate directory after installation. Tap Save . | Tip | If you cannot set up Cisco Jabber Voice for Android , see the tips in the troubleshooting section. | Tip | (For new Android users) Swipe the screen to the left or right to navigate through your applications. | Note | If you do not want to set up your voicemail, tap Skip . You can also set up voicemail after installation. | Note | If you do not want to set up your corporate directory, tap Skip . You can also set up the corporate directory after installation. |
|---|---|---|---|---|---|---|---|---|---|
| Tip | If you cannot set up Cisco Jabber Voice for Android , see the tips in the troubleshooting section. |
| Tip | (For new Android users) Swipe the screen to the left or right to navigate through your applications. |
| Note | If you do not want to set up your voicemail, tap Skip . You can also set up voicemail after installation. |
| Note | If you do not want to set up your corporate directory, tap Skip . You can also set up the corporate directory after installation. |

| Tip | If you cannot set up Cisco Jabber Voice for Android , see the tips in the troubleshooting section. |
|---|---|

| Tip | (For new Android users) Swipe the screen to the left or right to navigate through your applications. |
|---|---|

| Note | If you do not want to set up your voicemail, tap Skip . You can also set up voicemail after installation. |
|---|---|

| Note | If you do not want to set up your corporate directory, tap Skip . You can also set up the corporate directory after installation. |
|---|---|

| Q. | How do I upgrade from Cisco Jabber for Android Release 9.x to Cisco Jabber Voice for Android Release 9.1(4)? |
|---|---|

| A. | To upgrade from Cisco Jabber for Android Release 9.x to Cisco Jabber Voice for Android Release 9.1(4), download the latest release from Google Play and overwrite the previous version of the product on your device. Note To upgrade from Cisco Jabber for Android Release 8.6.x to Cisco Jabber Voice for Android Release 9.1(4), you must first uninstall the previous version of the product from your device. | Note | To upgrade from Cisco Jabber for Android Release 8.6.x to Cisco Jabber Voice for Android Release 9.1(4), you must first uninstall the previous version of the product from your device. |
|---|---|---|---|
| Note | To upgrade from Cisco Jabber for Android Release 8.6.x to Cisco Jabber Voice for Android Release 9.1(4), you must first uninstall the previous version of the product from your device. |

| Note | To upgrade from Cisco Jabber for Android Release 8.6.x to Cisco Jabber Voice for Android Release 9.1(4), you must first uninstall the previous version of the product from your device. |
|---|---|

| Q. | How do I access the Cisco Jabber Voice for Android settings? |
|---|---|

| A. | To access the Cisco Jabber Voice for Android settings, open Cisco Jabber Voice for Android , and then tap Menu > Settings . |
|---|---|

| Q. | Why do I need to stop other Internet calling applications before using Cisco Jabber Voice for Android ? |
|---|---|

| A. | If you run multiple Internet calling applications on your Android device, they can conflict with each other and cause unpredictable behavior. To prevent these conflicts, run one application at a time. To stop an application, complete the following steps: Android OS 4.1: Tap the Android Settings application. Depending on your OS, tap either Apps or Application manager . Tap the name of the application you want to stop. Tap Force stop . Android OS 2.3: On the Android home screen, tap Menu > Settings > Applications > Manage applications . Tap the application name, and then tap Force stop . |
|---|---|

| Q. | What do the icons in the status bar mean? |
|---|---|

| A. | The icons indicate your connection status. Swipe down the status bar to view details. Icon Description Cisco Jabber Voice for Android is connected to your corporate calling system and the Phone Services features are available. Cisco Jabber Voice for Android is not connected to your corporate calling system and the Phone Services features are unavailable. To resolve connection issues, try one of the following: Check whether you were on a call using your mobile phone number (instead of your work phone number). When you are on a call using your mobile phone number, Cisco Jabber Voice for Android automatically disconnects until you end the call. Verify that you entered your account settings properly. In Cisco Jabber Voice for Android , tap Menu > Settings . Under Accounts , tap Phone Services . Check your network settings. If you are inside your corporate network, check your Wi-Fi settings. If your status bar indicates that you are connected to a Wi-Fi network, verify that you are connected to the correct Wi-Fi network (that is, your corporate Wi-Fi network). To verify, open a browser and try to connect to an internal website. If you are outside of your corporate network, check your native Wi-Fi or mobile network settings. If you are using mobile data network, verify that you have a strong mobile network signal. If your network settings are correct, check whether your VPN is connected. Contact your system administrator for additional assistance. Cisco Jabber Voice for Android has an active call. Cisco Jabber Voice for Android has a call on hold. Cisco Jabber Voice for Android has an error. Swipe down the status bar to view details about the error. For some error messages, you can tap the notification message to go to an associated screen or popup window to try to resolve the error. Cisco Jabber Voice for Android lost the connection to the voicemail server. Swipe down the status bar to view details about the error. For some error messages, you can tap the notification message to go to an associated screen or popup window to try to resolve the error. | Icon | Description |  | Cisco Jabber Voice for Android is connected to your corporate calling system and the Phone Services features are available. |  | Cisco Jabber Voice for Android is not connected to your corporate calling system and the Phone Services features are unavailable. To resolve connection issues, try one of the following: Check whether you were on a call using your mobile phone number (instead of your work phone number). When you are on a call using your mobile phone number, Cisco Jabber Voice for Android automatically disconnects until you end the call. Verify that you entered your account settings properly. In Cisco Jabber Voice for Android , tap Menu > Settings . Under Accounts , tap Phone Services . Check your network settings. If you are inside your corporate network, check your Wi-Fi settings. If your status bar indicates that you are connected to a Wi-Fi network, verify that you are connected to the correct Wi-Fi network (that is, your corporate Wi-Fi network). To verify, open a browser and try to connect to an internal website. If you are outside of your corporate network, check your native Wi-Fi or mobile network settings. If you are using mobile data network, verify that you have a strong mobile network signal. If your network settings are correct, check whether your VPN is connected. Contact your system administrator for additional assistance. |  | Cisco Jabber Voice for Android has an active call. |  | Cisco Jabber Voice for Android has a call on hold. |  | Cisco Jabber Voice for Android has an error. Swipe down the status bar to view details about the error. For some error messages, you can tap the notification message to go to an associated screen or popup window to try to resolve the error. |  | Cisco Jabber Voice for Android lost the connection to the voicemail server. Swipe down the status bar to view details about the error. For some error messages, you can tap the notification message to go to an associated screen or popup window to try to resolve the error. |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Icon | Description |
|  | Cisco Jabber Voice for Android is connected to your corporate calling system and the Phone Services features are available. |
|  | Cisco Jabber Voice for Android is not connected to your corporate calling system and the Phone Services features are unavailable. To resolve connection issues, try one of the following: Check whether you were on a call using your mobile phone number (instead of your work phone number). When you are on a call using your mobile phone number, Cisco Jabber Voice for Android automatically disconnects until you end the call. Verify that you entered your account settings properly. In Cisco Jabber Voice for Android , tap Menu > Settings . Under Accounts , tap Phone Services . Check your network settings. If you are inside your corporate network, check your Wi-Fi settings. If your status bar indicates that you are connected to a Wi-Fi network, verify that you are connected to the correct Wi-Fi network (that is, your corporate Wi-Fi network). To verify, open a browser and try to connect to an internal website. If you are outside of your corporate network, check your native Wi-Fi or mobile network settings. If you are using mobile data network, verify that you have a strong mobile network signal. If your network settings are correct, check whether your VPN is connected. Contact your system administrator for additional assistance. |
|  | Cisco Jabber Voice for Android has an active call. |
|  | Cisco Jabber Voice for Android has a call on hold. |
|  | Cisco Jabber Voice for Android has an error. Swipe down the status bar to view details about the error. For some error messages, you can tap the notification message to go to an associated screen or popup window to try to resolve the error. |
|  | Cisco Jabber Voice for Android lost the connection to the voicemail server. Swipe down the status bar to view details about the error. For some error messages, you can tap the notification message to go to an associated screen or popup window to try to resolve the error. |

| Icon | Description |
|---|---|
|  | Cisco Jabber Voice for Android is connected to your corporate calling system and the Phone Services features are available. |
|  | Cisco Jabber Voice for Android is not connected to your corporate calling system and the Phone Services features are unavailable. To resolve connection issues, try one of the following: Check whether you were on a call using your mobile phone number (instead of your work phone number). When you are on a call using your mobile phone number, Cisco Jabber Voice for Android automatically disconnects until you end the call. Verify that you entered your account settings properly. In Cisco Jabber Voice for Android , tap Menu > Settings . Under Accounts , tap Phone Services . Check your network settings. If you are inside your corporate network, check your Wi-Fi settings. If your status bar indicates that you are connected to a Wi-Fi network, verify that you are connected to the correct Wi-Fi network (that is, your corporate Wi-Fi network). To verify, open a browser and try to connect to an internal website. If you are outside of your corporate network, check your native Wi-Fi or mobile network settings. If you are using mobile data network, verify that you have a strong mobile network signal. If your network settings are correct, check whether your VPN is connected. Contact your system administrator for additional assistance. |
|  | Cisco Jabber Voice for Android has an active call. |
|  | Cisco Jabber Voice for Android has a call on hold. |
|  | Cisco Jabber Voice for Android has an error. Swipe down the status bar to view details about the error. For some error messages, you can tap the notification message to go to an associated screen or popup window to try to resolve the error. |
|  | Cisco Jabber Voice for Android lost the connection to the voicemail server. Swipe down the status bar to view details about the error. For some error messages, you can tap the notification message to go to an associated screen or popup window to try to resolve the error. |

| Q. | How do I view details about features that do not connect properly? |
|---|---|

| A. | If features do not connect properly, check the connection status. To view the connection status, complete the following steps: In Cisco Jabber Voice for Android , tap Menu > Settings . Under Accounts , check the connection status for the related feature. Connected: Feature is set up and connected properly. Connecting: Feature is currently making a connection attempt. Disconnected: Feature is set up but is not currently connected. For example, you see this connection status if the corporate network is not properly connected or the server is down. Error: Feature is not currently set up or connected. For example, you see an error if you enter an incorrect password. |
|---|---|

| Q. | How do I view my account settings? |
|---|---|

| A. | To view your account settings, complete the following steps: In Cisco Jabber Voice for Android , tap Menu > Settings . Under Accounts , tap one of the accounts to view the settings: Phone Services: Settings for your corporate phone system. Directory: Settings for your corporate directory or Lightweight Directory Access Protocol (LDAP) server. If your system administrator did not set up your account for directory search, the application does not display the directory account. Voicemail: Settings for your corporate visual voicemail server. You see this setting only if your system administrator set up your account for visual voicemail. You do not see this setting if your system administrator set up your account for basic voicemail. |
|---|---|

| Q. | How do I set my Jabber calling options? |
|---|---|

| A. | If your administrator enabled the Dial via Office (DVO) feature, you can view and select different Jabber calling options. Use these calling options to select whether Jabber places calls with your work number over the Internet or your mobile voice network. Set Jabber calling options as follows: Tap Settings . In the Phone Services section, tap Jabber Calling Options . Select one of the following calling options: Always use Internet: Cisco Jabber Voice functions as an Internet phone, using Wi-Fi or your mobile data plan to make calls over the Internet with your work number. Always use DVO: Cisco Jabber Voice initiates calls with your work number, but uses the voice plan for your device for all calls. Automatically select: (Default) Cisco Jabber Voice automatically selects to use either the Internet or DVO, based on your network connection. The app functions as an Internet phone when on Wi-Fi, but uses the voice plan for your device when on mobile data networks. If the DVO Callback Number is not already specified, enter a phone number. When you use DVO, the corporate calling system calls you back to start all calls. The DVO callback number is usually your mobile phone number. |
|---|---|

| Q. | Why does Cisco Jabber Voice for Android start automatically? |
|---|---|

| A. | When you first set up Cisco Jabber Voice for Android , you can choose whether to allow it to start automatically each time your device restarts. To change this setting, complete the following steps: In Cisco Jabber Voice for Android , tap Menu > Settings . Under General , turn off Auto Start to prevent Cisco Jabber Voice for Android from starting automatically. |
|---|---|

| Q. | How do I exit Cisco Jabber Voice for Android ? |
|---|---|

| A. | To exit Cisco Jabber Voice for Android , go to the Cisco Jabber Voice for Android home screen and tap Menu > Exit . After you exit Cisco Jabber Voice for Android , it stops running in the background, disconnects from the server, and prevents you from making or receiving your work calls. Tip Cisco Jabber Voice for Android does not display the Exit menu on all screens. If you do not see the Exit menu, go back to the Cisco Jabber Voice for Android home screen. Note If you turned on Auto Start , Cisco Jabber Voice for Android automatically starts after you boot your device. | Tip | Cisco Jabber Voice for Android does not display the Exit menu on all screens. If you do not see the Exit menu, go back to the Cisco Jabber Voice for Android home screen. | Note | If you turned on Auto Start , Cisco Jabber Voice for Android automatically starts after you boot your device. |
|---|---|---|---|---|---|
| Tip | Cisco Jabber Voice for Android does not display the Exit menu on all screens. If you do not see the Exit menu, go back to the Cisco Jabber Voice for Android home screen. |
| Note | If you turned on Auto Start , Cisco Jabber Voice for Android automatically starts after you boot your device. |

| Tip | Cisco Jabber Voice for Android does not display the Exit menu on all screens. If you do not see the Exit menu, go back to the Cisco Jabber Voice for Android home screen. |
|---|---|

| Note | If you turned on Auto Start , Cisco Jabber Voice for Android automatically starts after you boot your device. |
|---|---|

| Q. | How do I use Cisco Jabber Voice when I’m not physically on-site at my office? |
|---|---|

| A. | To use Cisco Jabber Voice , you must connect to your corporate network. When you are in the office, you probably connect to the corporate network directly. When you are away from the office, you typically must have a VPN connection to your office network. You must set up this VPN connection before you use Cisco Jabber Voice . You can use the VPN with Wi-Fi or mobile data networks. If your administrator sets up DVO, the corporate calling system initiates the DVO calls over Wi-Fi or mobile data networks, and then places the calls over the mobile voice network. Contact your system administrator if you need assistance. |
|---|---|

| Q. | My administrator told me to install Cisco AnyConnect Secure Mobility Client so I can use Cisco Jabber Voice for Android outside my corporate Wi-Fi network. How do I do that? |
|---|---|

| A. | For information about how to install and use Cisco AnyConnect Secure Mobility Client on your Android device, see the latest Android end user guide for Cisco AnyConnect Secure Mobility Client in the user guide list . |
|---|---|

| Q. | I want to use Cisco Jabber Voice for Android with mobile data networks, but not with noncorporate Wi-Fi networks. Can I do that? |
|---|---|

| A. | If DVO is not enabled: Yes. To prevent Cisco Jabber Voice for Android from connecting to the corporate calling system with noncorporate Wi-Fi networks over VPN, complete the following steps: In Cisco Jabber Voice for Android , tap Menu > Settings . Under General, turn on Use mobile data network . Under General, turn off Use noncorporate Wi-Fi . If DVO is enabled: No. Both Wi-Fi networks and mobile data networks are always turned on when DVO is enabled. Cisco Jabber Voice does not display options to turn noncorporate Wi-Fi and mobile data networks on or off individually. |
|---|---|

| Q. | I want to use Cisco Jabber Voice for Android with noncorporate Wi-Fi networks, but not with mobile data networks. Can I do that? |
|---|---|

| A. | If DVO is not enabled: Yes. To prevent Cisco Jabber Voice for Android from connecting to the corporate calling system with mobile data networks over VPN, complete the following steps: In Cisco Jabber Voice for Android , tap Menu > Settings . Under General, turn off Use mobile data network . Under General, turn on Use noncorporate Wi-Fi . If DVO is enabled: No. Both Wi-Fi networks and mobile data networks are always turned on when DVO is enabled. Cisco Jabber Voice does not display options to turn noncorporate Wi-Fi and mobile data networks on or off individually. |
|---|---|

| Q. | What is low bandwidth mode? |
|---|---|

| A. | Cisco Jabber Voice for Android uses low bandwidth mode to optimize the audio for low bandwidth networks, which may improve call quality for Internet calls. To use low bandwidth mode, one of the following must be true: Your system is set up to handle calls between devices that use different codecs Both your device and the device of the person you are calling support the same low bandwidth codec (G.729a or G.729b). Note If you call a device that does not support the same low bandwidth codec, and the system is not set up to handle a codec mismatch, you may experience one of the following problems: You cannot hear audio The call is immediately disconnected If you have questions about your system setup, contact your system administrator. | Note | If you call a device that does not support the same low bandwidth codec, and the system is not set up to handle a codec mismatch, you may experience one of the following problems: You cannot hear audio The call is immediately disconnected |
|---|---|---|---|
| Note | If you call a device that does not support the same low bandwidth codec, and the system is not set up to handle a codec mismatch, you may experience one of the following problems: You cannot hear audio The call is immediately disconnected |

| Note | If you call a device that does not support the same low bandwidth codec, and the system is not set up to handle a codec mismatch, you may experience one of the following problems: You cannot hear audio The call is immediately disconnected |
|---|---|

| Q. | How do I turn on low bandwidth mode? |
|---|---|

| A. | To turn on low bandwidth mode, complete the following steps. In Cisco Jabber Voice for Android , tap Menu > Settings . Under Phone Services , turn on Use low bandwidth mode . |
|---|---|

| Q. | What is the difference between making calls with my native phone application and Cisco Jabber Voice for Android ? |
|---|---|

| A. | When you make a phone call with your native phone application, the application uses your mobile phone number and your mobile service provider's voice network. The application uses your mobile voice plan to make the call, and displays the mobile voice number to the person you call. When you make a phone call with Cisco Jabber Voice for Android , the application uses your work phone number and displays that work number to the person you call. Cisco Jabber Voice can use different networks to make these calls with your work number, depending on whether your administrator enables the DVO feature. Without DVO, Cisco Jabber Voice places calls with your work number using Wi-Fi or mobile data networks. In this case, Cisco Jabber Voice functions as an Internet phone. With DVO, Cisco Jabber Voice places calls over your mobile voice network, which uses your mobile voice plan. These calls are initiated either over Wi-Fi or your mobile data network, which uses your mobile data plan. |
|---|---|

| Q. | What calling features does Cisco Jabber Voice for Android support? |
|---|---|

| A. | Cisco Jabber Voice for Android supports the following calling features for Internet calls, which you might already be familiar with from using your Cisco Unified IP Phone: Conference: Allows you to talk simultaneously with multiple callers Transfer: Allows you to redirect a connected call from your phone to another number Hold: Allows you to put an active call into a held state Two calls: Supports two simultaneous calls, and lets you toggle between them VoIP over mobile voice network: Allows you to use your mobile voice network for VoIP calls if you leave a Wi-Fi network Cisco Jabber Voice also supports the Dial via Office feature, which allows you to place calls with your work number using the voice plan for your device. |
|---|---|

| Q. | How do I make a call? |
|---|---|

| A. | Before you make a call, make sure your Android device is connected to your corporate network. Cisco Jabber Voice for Android integrates with the standard Android Phone application. You can make calls from either the Android Phone application or the Cisco Jabber Voice for Android application. To make a call, complete the following steps: From the Android Phone application: Tap the Phone icon on the Android home screen. Dial a number. Tap Jabber Voice to place your call using Cisco Jabber Voice for Android . If using DVO, the corporate calling system calls you back on your native Android Phone application. Swipe the Phone icon to accept the call. If prompted, press any number on the keypad. After you accept the call, the corporate calling system calls the number you dialed. From the Cisco Jabber Voice for Android application: Tap the Phone tab on the Cisco Jabber Voice for Android home screen. Dial a number. If prompted, tap Jabber Voice to place your call using Cisco Jabber Voice for Android . If using DVO, the corporate calling system calls you back on your native Android Phone application. Swipe the Phone icon to accept the call. If prompted, press any number on the keypad. After you accept the call, the corporate calling system calls the number you dialed. |
|---|---|

| Q. | Can I set Cisco Jabber Voice for Android to use either my mobile number or my work number to make calls? |
|---|---|

| A. | Yes. Cisco Jabber Voice for Android integrates with the Android Phone application and allows you to choose whether you want to place calls with your native mobile phone number or your work number. To change this setting, complete the following steps: In Cisco Jabber Voice for Android , tap Menu > Settings . Tap Dial Options . Tap one of the options: Call using Cisco Jabber: (Default) Cisco Jabber Voice for Android to make all calls with your work number over your corporate network. Ask for every call: Allows you to choose which number to use to make each call. Call using my mobile phone: Uses the Android Phone application to make all calls with your mobile number over your mobile network. |
|---|---|

| Q. | How do I answer a call? |
|---|---|

| A. | You can answer calls using Cisco Jabber Voice for Android if you are connected to your corporate network. When your device rings, do one of the following: If you are not already on a call when you receive the new incoming call, tap Accept . If you are already on a work call in the Cisco Jabber Voice application when you receive a new incoming work call, you can just decline the new call or accept it. If you accept the call, the new call is connected and the original call is placed on hold. If you decline the call, the device displays it as a received call in the standard call log on your Android device and the original call remains connected. If you are already on a work call in the native phone application when you receive a new incoming work call, you can ignore the new call or end your first call before you accept the new call. |
|---|---|

| Q. | How many calls does Cisco Jabber Voice for Android support at the same time? |
|---|---|

| A. | Cisco Jabber Voice supports one or two calls, depending on whether your administrator enabled the DVO feature. If DVO is not enabled: Cisco Jabber Voice acts like a two-line phone. If you are already connected to a call, you can receive or make another one. Only one call is active at a time; the other is automatically placed on hold. Tap Swap to toggle between the two calls. If DVO is enabled: Incoming work calls open in the native phone application. In these cases, Cisco Jabber Voice like a one-line phone. |
|---|---|

| Q. | How do I make a work call from the call log on my Android device? |
|---|---|

| A. | Before you make a work call, make sure your Android device is connected to your corporate network. Cisco Jabber Voice for Android integrates with the standard call log on your Android device. You can access the call log from either the Android Phone application or the Cisco Jabber Voice for Android application. To make a call from the call log, complete the following steps: From the Android Phone application: On the Android home screen, tap the Phone icon. Tap the Logs tab. Tap the phone number that you want to call. Tap the Phone icon. If prompted, tap Jabber Voice to place your call using Cisco Jabber Voice for Android . If using DVO, the corporate calling system calls you back on your native Android Phone application. Swipe the Phone icon to accept the call. If prompted, press any number on the keypad. After you accept the call, the corporate calling system calls the number you dialed. From the Cisco Jabber Voice for Android application: On the Cisco Jabber Voice for Android home screen, tap the Phone tab. Tap the Recents button ( ). Tap the phone number that you want to call. Tap the Phone icon. If prompted, tap Jabber Voice to place your call using Cisco Jabber Voice for Android . If using DVO, the corporate calling system calls you back on your native Android Phone application. Swipe the Phone icon to accept the call. If prompted, press any number on the keypad. After you accept the call, the corporate calling system calls the number you dialed. Note After you save a contact, you can also call using an alternate method. Tap the contact's picture in the call log item, and then tap the Phone icon on the slider that appears. | Note | After you save a contact, you can also call using an alternate method. Tap the contact's picture in the call log item, and then tap the Phone icon on the slider that appears. |
|---|---|---|---|
| Note | After you save a contact, you can also call using an alternate method. Tap the contact's picture in the call log item, and then tap the Phone icon on the slider that appears. |

| Note | After you save a contact, you can also call using an alternate method. Tap the contact's picture in the call log item, and then tap the Phone icon on the slider that appears. |
|---|---|

| Q. | How do I make a work call from Favorites? |
|---|---|

| A. | Before you make a work call, make sure your Android device is connected to your corporate network. Cisco Jabber Voice for Android integrates with the native Favorites on your Android device. The procedure for making a work call from Favorites varies depending on your Android operating system. To make a work call from Favorites, complete the following steps: Android OS 4.0: On the Android home screen, tap the People icon or the Contacts icon (depending on your device). Tap the phone number that you want to call. If prompted, tap Jabber Voice to place your call using Cisco Jabber Voice for Android . If using DVO, the corporate calling system calls you back on your native Android Phone application. Swipe the Phone icon to accept the call. If prompted, press any number on the keypad. After you accept the call, the corporate calling system calls the number you dialed. Android OS 2.3: On the Android home screen, tap the Phone icon. Tap the Favorites tab. Tap the name of the Favorite that you want to call. Tap the green Phone icon. If prompted, tap Jabber Voice to place your call using Cisco Jabber Voice for Android . If using DVO, the corporate calling system calls you back on your native Android Phone application. Swipe the Phone icon to accept the call. If prompted, press any number on the keypad. After you accept the call, the corporate calling system calls the number you dialed. Note You can also tap the picture in the Favorites list, and then tap the Phone icon on the slider that appears. | Note | You can also tap the picture in the Favorites list, and then tap the Phone icon on the slider that appears. |
|---|---|---|---|
| Note | You can also tap the picture in the Favorites list, and then tap the Phone icon on the slider that appears. |

| Note | You can also tap the picture in the Favorites list, and then tap the Phone icon on the slider that appears. |
|---|---|

| Q. | How do I make a work call from Contacts? |
|---|---|

| A. | Before you make a work call, make sure your Android device is connected to your corporate network. Cisco Jabber Voice for Android integrates with the standard Contacts on your Android device. To make a work call from Contacts, complete the following steps: Tap the Contacts icon on the Android home screen (or the Contacts tab if you are already in the Phone application). Tap a contact in the list. Tap the green Phone icon. If prompted, tap Jabber Voice to place your call using Cisco Jabber Voice for Android . If using DVO, the corporate calling system calls you back on your native Android Phone application. Swipe the Phone icon to accept the call. If prompted, press any number on the keypad. After you accept the call, the corporate calling system calls the number you dialed. |
|---|---|

| Q. | How do I make a second call from within the Cisco Jabber Voice for Android application? |
|---|---|

| A. | To make a second Internet call while on a Cisco Jabber Voice for Android Internet call, complete the following steps: While on a call, tap the Show more menu button and select Add Call . Tap Add Call . Make the new call. Cisco Jabber Voice for Android automatically places your first call on hold and displays the status of both calls. Tap Swap to toggle between connected calls. |
|---|---|

| Q. | How do I make a conference call from within the Cisco Jabber Voice for Android application? |
|---|---|

| A. | To make a conference call, complete the following steps: While on a call, tap More . Tap Add Call . Make the new call and wait for it to connect. Tap Merge . Repeat the steps to add more people to the call. |
|---|---|

| Q. | How do I transfer a call from within the Cisco Jabber Voice for Android application? |
|---|---|

| A. | To transfer an Internet call, complete the following steps: While on a call, tap the Show more menu button and select Transfer . Dial the number to which you want to transfer the call, and then tap Complete Transfer either before or after the call is answered. After you complete the transfer, the system automatically disconnects you from the original call. |
|---|---|

| Q. | How do I answer an incoming work call to Cisco Jabber Voice for Android while I am already on a call in the app? |
|---|---|

| A. | If you are already on an Internet call when a new call arrives to Cisco Jabber Voice for Android , the caller ID information for the new call appears on the screen. Tap Accept to answer the call and choose whether to put your current call on hold or end it. If you are already on an Internet call when a new call arrives to Cisco Jabber Voice for Android , the caller ID information for the new call appears on the screen. Tap Accept to answer the call. The new call is connected, and the original call is placed on hold. If you do not want to accept the call, tap Decline , and the system transfers the caller to your available voicemail system. If you decline the call, it appears as a received call in the standard call log on your Android device. |
|---|---|

| Q. | How do I toggle between two calls from within the Cisco Jabber Voice for Android application? |
|---|---|

| A. | When you are connected to two Internet calls, only one call is active at a time; the other is automatically placed on hold. Tap Swap to toggle between the two calls. |
|---|---|

| Q. | How do I end a call from within the Cisco Jabber Voice for Android application? |
|---|---|

| A. | Tap End . |
|---|---|

| Q. | How do I place a call on hold from within the Cisco Jabber Voice for Android application? |
|---|---|

| A. | While on an Internet call, tap Hold . To resume the call, tap Resume . |
|---|---|

| Q. | How do I put a call on hold when I have two Internet calls at the same time? |
|---|---|

| A. | When you are connected to two Internet calls, only one call is active at a time. Tap the call that is currently on hold, and the application automatically places the other call on hold. |
|---|---|

| Q. | Can I move my current Internet call from Cisco Jabber Voice for Android to my Cisco IP Phone? |
|---|---|

| A. | Yes, you can move your Internet call if your Cisco Jabber Voice for Android device and your Cisco IP Phone share the same directory number. To move your Internet call to your Cisco IP Phone, complete the following steps: While you are on a Cisco Jabber Voice for Android Internet call, place the call on hold. Use the resume function on your Cisco IP Phone to continue the call. After you resume the call on your Cisco IP Phone, Cisco Jabber Voice for Android closes the call screen and displays the call log, which shows the call as ended. Note If you do not resume the call on your Cisco IP Phone, you can resume the call on Cisco Jabber Voice for Android . | Note | If you do not resume the call on your Cisco IP Phone, you can resume the call on Cisco Jabber Voice for Android . |
|---|---|---|---|
| Note | If you do not resume the call on your Cisco IP Phone, you can resume the call on Cisco Jabber Voice for Android . |

| Note | If you do not resume the call on your Cisco IP Phone, you can resume the call on Cisco Jabber Voice for Android . |
|---|---|

| Q. | If I'm about to leave my corporate Wi-Fi network, can I move my current Cisco Jabber Voice for Android Internet call to my mobile network? |
|---|---|

| A. | Yes. This action moves the Internet call from Cisco Jabber Voice for Android to the Android Phone application. Note This option is not available if you are connected to your corporate network using VPN over either your mobile data network or a noncorporate Wi-Fi network. Before you move your call, make sure your mobile network signal is strong enough to receive calls. To move your call to your mobile network, complete the following steps: While on a call using Cisco Jabber Voice for Android , tap the Show more menu button. Tap Use mobile network . The system calls your device over the mobile voice network. Accept the incoming call. Cisco Jabber Voice for Android moves the call to the mobile voice network and the call continues within the standard Android Phone application. After you finish your conversation, tap End to end the call. After you end the call, the person that you were talking to hears music for a few seconds before the call disconnects. | Note | This option is not available if you are connected to your corporate network using VPN over either your mobile data network or a noncorporate Wi-Fi network. |
|---|---|---|---|
| Note | This option is not available if you are connected to your corporate network using VPN over either your mobile data network or a noncorporate Wi-Fi network. |

| Note | This option is not available if you are connected to your corporate network using VPN over either your mobile data network or a noncorporate Wi-Fi network. |
|---|---|

| Q. | Can I accept work calls while on a mobile voice call? |
|---|---|

| A. | If you are not using Cisco Jabber Voice for Android when you accept a mobile voice call, Cisco Jabber Voice for Android automatically disconnects while you are on the mobile voice call. Phone services are unavailable while you are on the active mobile voice call. After you end the mobile voice call, Cisco Jabber Voice for Android automatically reconnects. However, if you set up Mobile Connect for your work number, the system passes work calls to you using your mobile network number. You can then handle those calls as you would any other mobile voice call. |
|---|---|

| Q. | What do I do if I get an incoming mobile voice call while on a Cisco Jabber Voice for Android Internet call? |
|---|---|

| A. | If you are on a Cisco Jabber Voice for Android Internet call and you receive an incoming mobile voice call, the call screen displays the incoming caller ID and you hear a call waiting tone. You can accept or decline the call: Accept: Puts your active Cisco Jabber Voice for Android Internet call on hold. If you have a Cisco Jabber Voice for Android Internet call on hold and you are on a second Cisco Jabber Voice for Android Internet call when you accept the mobile voice call, the held call drops. You cannot toggle between the mobile voice call and the Cisco Jabber Voice for Android Internet call. You must end the mobile voice call before you can resume the Cisco Jabber Voice for Android call. After you disconnect the mobile voice call, your device displays your Cisco Jabber Voice for Android call again. Tap Resume to continue the call. Cisco Jabber Voice for Android does not disconnect during the mobile voice call, so it can hold the Cisco Jabber Voice for Android call and allow you to return to it after you end the mobile voice call. Tip If the Cisco Jabber Voice for Android call does not automatically appear, open Cisco Jabber Voice for Android to access the call again. Decline: Ignores the incoming mobile voice call (sends the call to the associated mobile number voicemail, if set up) and returns you to the Cisco Jabber Voice for Android Internet call. | Tip | If the Cisco Jabber Voice for Android call does not automatically appear, open Cisco Jabber Voice for Android to access the call again. |
|---|---|---|---|
| Tip | If the Cisco Jabber Voice for Android call does not automatically appear, open Cisco Jabber Voice for Android to access the call again. |

| Tip | If the Cisco Jabber Voice for Android call does not automatically appear, open Cisco Jabber Voice for Android to access the call again. |
|---|---|

| Q. | When I used the Cisco Jabber Voice for Android setup wizard, I skipped the Directory screen. Can I still set up the application to search my directory? |
|---|---|

| A. | Yes. If you did not previously set up your corporate directory using the setup wizard, complete the following steps: In Cisco Jabber Voice for Android , tap Menu > Settings . Under Accounts , tap Directory . In the Username field, enter your username. In the Password field, enter your password. Tap Connect . |
|---|---|

| Q. | How do I search my corporate directory? |
|---|---|

| A. | To search the corporate directory, complete the following steps: In Cisco Jabber Voice for Android , tap the Directory tab, and then enter a name in the text box. In the search results, tap a name to see the contact details. |
|---|---|

| Q. | Why isn't directory search available? |
|---|---|

| A. | Cisco Jabber Voice displays your directory as disconnected until you make your first search. If you have already completed a search, the directory search displays as not available if either the directory server is not available if either the directory server disconnected your device, or if the directory server is not reachable. If the problem persists, contact your system administrator. |
|---|---|

| Q. | How do I create a contact? |
|---|---|

| A. | To create a contact, complete the following steps: Search your corporate directory using Cisco Jabber Voice for Android . In the search results, tap a name to see the contact details. Tap Add to Contacts . Make any changes and then tap Save . The contact appears in the standard Android Contacts list. |
|---|---|

| Q. | Why did the directory search not show the person I looked for? |
|---|---|

| A. | Cisco Jabber Voice for Android limits the directory search results to 20 items. If your search is too broad, the application might not include your target in the results. Narrow your search by including more characters in your entry. |
|---|---|

| Q. | Why do the pictures of my corporate directory contacts not appear? |
|---|---|

| A. | Cisco Jabber Voice for Android does not currently support downloading images from corporate directory search results. However, you can edit the contact information to add a photo locally. |
|---|---|

| Q. | How do I know if I have a voice message? |
|---|---|

| A. | After you receive a new voice message, the Voicemail icon appears in the status bar. Swipe down the status bar to see the number of new Cisco Jabber Voice for Android voice messages. In addition, a new voice message notification appears on the Voicemail tab on the Cisco Jabber Voice for Android home screen. |
|---|---|

| Q. | How do I listen to my voice messages? |
|---|---|

| A. | Swipe down the status bar and tap the voice message notification, or tap the Voicemail tab in Cisco Jabber Voice for Android . Tap the Call Voicemail button to call your voicemail server and listen to your voice messages. After you listen to all your messages, Cisco Jabber Voice for Android removes the notification from both the status bar and the Voicemail tab. |
|---|---|

| Q. | What's the difference between basic voicemail and visual voicemail? |
|---|---|

| A. | The visual voicemail feature is an alternative to the basic voicemail service. With a basic voicemail service, you dial in to your voice mailbox and then respond to audio prompts. With visual voicemail, you use the screen on your device to work with your messages, rather than respond to audio prompts. You can see a list of your messages without having to dial in to your voice mailbox. If your system administrator sets up visual voicemail, you can: Play or pause your messages If available, see a transcription of your messages Delete and restore messages Call back the contact who sent the message |
|---|---|

| Q. | How do I set up visual voicemail? |
|---|---|

| A. | If you did not already set up visual voicemail using the setup wizard, complete the following steps: In Cisco Jabber Voice for Android , tap Menu > Settings . Under Accounts , tap Voicemail . Note If your system administrator did not enable the visual voicemail feature, you do not see the Voicemail menu. In the Server Address field, if the address is not already entered, enter the voicemail server address. If you do not already have this information, contact your system administrator. (Optional) In the Port field, enter the voicemail server port. In the Username field, if the username is not already entered, enter your voicemail username. In the Password field, enter your voicemail password. Tap Verify . | Note | If your system administrator did not enable the visual voicemail feature, you do not see the Voicemail menu. |
|---|---|---|---|
| Note | If your system administrator did not enable the visual voicemail feature, you do not see the Voicemail menu. |

| Note | If your system administrator did not enable the visual voicemail feature, you do not see the Voicemail menu. |
|---|---|

| Q. | How do I know if I have a visual voice message? |
|---|---|

| A. | After you receive a new visual voice message, the Voicemail icon appears in the status bar. Swipe down the status bar to see the number of new Cisco Jabber Voice for Android visual voice messages. A new visual voice message notification also appears on the Voicemail tab on the Cisco Jabber Voice for Android home screen. |
|---|---|

| Q. | How do I listen to my visual voice messages? |
|---|---|

| A. | Complete the following steps: Do one of the following: Swipe down the status bar and tap the visual voice message notification. Tap the Voicemail tab on the Cisco Jabber Voice for Android home screen. On the Voice Messages screen, Cisco Jabber Voice for Android displays the most recent messages at the top of the list. Cisco Jabber Voice for Android indicates unread messages with a green bar on the left side of the messages. Within the message, do one of the following: Tap the Play button to play the message in the list view. Tap anywhere else to play the message in the detail view. If prompted, tap Call voicemail to call the voicemail system. |
|---|---|

| Q. | Can I listen to my visual voice messages even if I'm not connected to my corporate network? |
|---|---|

| A. | Cisco Jabber Voice must be connected to your corporate network (either directly or remotely using VPN ) to receive new visual voice messages. You can listen to your other saved visual voice messages even if you are not connected to your corporate network. |
|---|---|

| Q. | Can I call the voicemail system directly? |
|---|---|

| A. | Yes. In some cases, you may want to call the voicemail system directly instead of using the visual voicemail screens (for example, if a data network is not available and you want to use a traditional telephone user interface to check messages). To call the voicemail system directly, go to the Voicemail tab, and then tap Menu > Call Voicemail . |
|---|---|

| Q. | What is a secure visual voice message? |
|---|---|

| A. | Secure visual voice messages are encrypted on your device. Your system administrator can set the voicemail system to secure all corporate visual voice messages. If your visual voice messages are secured, you cannot distribute them outside your corporate voicemail system. Also, your system administrator can specify whether Cisco Jabber Voice for Android can download the messages. |
|---|---|

| Q. | What do the icons in the Voice Messages and Voice Message Details screens mean? |
|---|---|

| A. | The icons indicate the type of voice message. Icon Description Urgent message Secure message | Icon | Description |  | Urgent message |  | Secure message |
|---|---|---|---|---|---|---|---|
| Icon | Description |
|  | Urgent message |
|  | Secure message |

| Icon | Description |
|---|---|
|  | Urgent message |
|  | Secure message |

| Q. | What do the buttons on the Voice Messages or Deleted Voice Messages screens do? |
|---|---|

| A. | The buttons function as follows: Button Description Play: Tap this button to play the message. Pause: Tap this button to pause the message. Call back: Tap this button to call back the person who left the message. Speaker: Tap this button to use speakerphone. Delete: Tap this button to send the message to the Deleted Messages folder. Undelete: Tap this button to move a deleted message from the Deleted Messages folder back to your inbox. Read message: This button indicates that you have read the message. If you tap this button, the status of the message changes to unread. Unread message: This button indicates that you have not read the message. If you tap this button, the status of the message changes to read. | Button | Description |  | Play: Tap this button to play the message. |  | Pause: Tap this button to pause the message. |  | Call back: Tap this button to call back the person who left the message. |  | Speaker: Tap this button to use speakerphone. |  | Delete: Tap this button to send the message to the Deleted Messages folder. |  | Undelete: Tap this button to move a deleted message from the Deleted Messages folder back to your inbox. |  | Read message: This button indicates that you have read the message. If you tap this button, the status of the message changes to unread. |  | Unread message: This button indicates that you have not read the message. If you tap this button, the status of the message changes to read. |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Button | Description |
|  | Play: Tap this button to play the message. |
|  | Pause: Tap this button to pause the message. |
|  | Call back: Tap this button to call back the person who left the message. |
|  | Speaker: Tap this button to use speakerphone. |
|  | Delete: Tap this button to send the message to the Deleted Messages folder. |
|  | Undelete: Tap this button to move a deleted message from the Deleted Messages folder back to your inbox. |
|  | Read message: This button indicates that you have read the message. If you tap this button, the status of the message changes to unread. |
|  | Unread message: This button indicates that you have not read the message. If you tap this button, the status of the message changes to read. |

| Button | Description |
|---|---|
|  | Play: Tap this button to play the message. |
|  | Pause: Tap this button to pause the message. |
|  | Call back: Tap this button to call back the person who left the message. |
|  | Speaker: Tap this button to use speakerphone. |
|  | Delete: Tap this button to send the message to the Deleted Messages folder. |
|  | Undelete: Tap this button to move a deleted message from the Deleted Messages folder back to your inbox. |
|  | Read message: This button indicates that you have read the message. If you tap this button, the status of the message changes to unread. |
|  | Unread message: This button indicates that you have not read the message. If you tap this button, the status of the message changes to read. |

| Q. | How do I delete a visual voice message? |
|---|---|

| A. | To delete a visual voice message, complete the following steps: In Cisco Jabber Voice for Android , from either the Voice Messages or Voice Message Details screen, tap Delete to send the messages to the Deleted Messages folder. To view the contents of the Deleted Messages folder, tap Menu > Deleted Messages . To permanently delete the messages in the Deleted Messages folder, tap Menu > Empty Deleted Messages . Tap OK . |
|---|---|

| Q. | I accidentally deleted a visual voice message. Can I restore it? |
|---|---|

| A. | Yes. To restore a deleted message, complete the following steps: In the Cisco Jabber Voice for Android Voicemail tab, on the Voice Messages screen, tap Menu . Tap Deleted Messages . Tap and hold the message that you want to restore. Tap Undelete . |
|---|---|

| Q. | What ways can I communicate with my contacts from the Voice Messages screen? |
|---|---|

| A. | You can communicate with contacts using any method that is set up in the native Android Contacts application (for example, email or instant messaging). Tap the contact's picture to view the communication options for that contact. |
|---|---|

| Q. | I see the voicemail connection error icon ( ) in the status bar. How do I resolve the error? |
|---|---|

| A. | Swipe down the status bar to view details about the error. For some error messages, you can tap the notification message to go to an associated screen or popup window to try to resolve the error. If you cannot resolve the error, contact your system administrator. |
|---|---|

| Q. | How do I view my recents for calls that I made using Cisco Jabber Voice for Android ? |
|---|---|

| A. | The recents for all calls you made using Cisco Jabber Voice for Android appear in the standard call log on your Android device. To view your recents, complete the following steps: On the Android home screen, tap the Phone icon. Tap the Logs tab. Note The native Android call log does not store Caller ID information that is obtained from a remote location. Therefore, you can see the Caller ID information during a Cisco Jabber Voice call, but only the number is stored in the native Android call log after the call ends. You can add the contact to the native Android Contacts application to resolve the caller ID information. | Note | The native Android call log does not store Caller ID information that is obtained from a remote location. Therefore, you can see the Caller ID information during a Cisco Jabber Voice call, but only the number is stored in the native Android call log after the call ends. You can add the contact to the native Android Contacts application to resolve the caller ID information. |
|---|---|---|---|
| Note | The native Android call log does not store Caller ID information that is obtained from a remote location. Therefore, you can see the Caller ID information during a Cisco Jabber Voice call, but only the number is stored in the native Android call log after the call ends. You can add the contact to the native Android Contacts application to resolve the caller ID information. |

| Note | The native Android call log does not store Caller ID information that is obtained from a remote location. Therefore, you can see the Caller ID information during a Cisco Jabber Voice call, but only the number is stored in the native Android call log after the call ends. You can add the contact to the native Android Contacts application to resolve the caller ID information. |
|---|---|

| Q. | How do I know if I missed a call? |
|---|---|

| A. | The device displays missed-call notifications in the status bar. Your Android device briefly displays the name and number of the caller. The Missed Call icon remains in the status bar until you open the standard call log on your Android device. To view details of a missed call, complete the following steps: Swipe down the status bar to view details about the missed call. Tap the missed-call notification to open the call log. |
|---|---|

| Q. | I'm trying to set up Cisco Jabber Voice for Android for the first time, but I can't get past the "Phone Services Settings" screen in the setup wizard. What can I do? |
|---|---|

| A. | If you cannot get past the "Phone Services Settings" screen in the setup wizard, try the following troubleshooting tips: Verify that you are using a supported device. For information about supported devices, see the Release Notes for your release. Verify that you are using the correct release of Cisco Jabber Voice for Android . You can download latest release of Cisco Jabber Voice for Android from the Google Play Store . If your administrator requested that you use a previous release of Cisco Jabber Voice for Android , contact your administrator for instructions for obtaining the Cisco Jabber Voice for Android software. Verify the following settings on the Cisco Jabber Voice for Android setup wizard: On the Phone Services Settings screen, verify that the name in Device ID field starts with "BOT" . If the Device ID does not start with "BOT" , contact your administrator to correct the Device ID. On the Phone Services Settings screen, in Server Address field, verify that you entered the Fully Qualified Domain Name (FQDN) of your TFTP server instead of the hostname. If the issue is not resolved after you verify your Device ID and enter the FQDN of your TFTP server, check whether there is a TFTP or network issue that prevents your device from accessing TFTP server to download the TFTP file. If you need help, contact your administrator. Verify the network connection between your device and the corporate network as follows: Open your Internet browser. Try to access the administration pages for your corporate calling system by entering the following URL: http:// <your company's Cisco Unified Communication Manager server address> . For example, http://209.165.200.224. Contact your administrator if you do not have the address for your company's Cisco Unified Communication Manager server. If you cannot access the administration pages for your corporate calling system, try again from different access point. If you still cannot access the administration pages for your corporate calling system, then there may be a network issue. Contact your system administrator for assistance. Check if your VPN is connected (if VPN is required). If not, contact your system administrator. If you already tried to provision once or twice unsuccessfully, clear your data and then try to provision again. To clear your application data, complete the following steps: Android OS 4.1: Tap the Android Settings application. Depending on your OS, tap either Apps or Application manager . Tap Jabber Voice . Tap Force stop . Tap Clear data . Android OS 2.3: On the Android home screen, tap Menu > Settings > Applications > Manage applications . Tap Jabber Voice . Tap Force stop . Tap Clear data . If you still cannot set up Cisco Jabber Voice for Android , send a problem report to your administrator. See the procedure that follows. |
|---|---|

| Q. | My system administrator requested that I send a problem report by email. How do I do that? |
|---|---|

| A. | To send a problem report by email, complete the following steps. Note The steps to send a problem report vary, depending on whether you completed the setup wizard for Cisco Jabber Voice for Android . If you did not complete the setup wizard: On Begin Setup screen, tap Menu > Help > Troubleshooting > Send Logs . If you already completed the setup wizard: In Cisco Jabber Voice for Android , tap Menu > Settings . Cisco recommends that you set up the Email application on the Android device. Under Help , tap Send Logs . Check the Audio Engine Logs check box. Check the Configuration Files check box. Tap Send Logs . Your Email application launches with a new message that contains a repopulated subject line and attached log files. Enter a description of the problem in the body of the email message and send it to your system administrator. Tip If you can reproduce your problem, enable Detailed Logging by tapping Menu > Settings . Then, under Help , tap Troubleshooting . Check the Detailed Logging check box and reproduce your issue before you send the problem report. In addition, include the timestamp when the problem occurred. | Note | The steps to send a problem report vary, depending on whether you completed the setup wizard for Cisco Jabber Voice for Android . | Tip | If you can reproduce your problem, enable Detailed Logging by tapping Menu > Settings . Then, under Help , tap Troubleshooting . Check the Detailed Logging check box and reproduce your issue before you send the problem report. In addition, include the timestamp when the problem occurred. |
|---|---|---|---|---|---|
| Note | The steps to send a problem report vary, depending on whether you completed the setup wizard for Cisco Jabber Voice for Android . |
| Tip | If you can reproduce your problem, enable Detailed Logging by tapping Menu > Settings . Then, under Help , tap Troubleshooting . Check the Detailed Logging check box and reproduce your issue before you send the problem report. In addition, include the timestamp when the problem occurred. |

| Note | The steps to send a problem report vary, depending on whether you completed the setup wizard for Cisco Jabber Voice for Android . |
|---|---|

| Tip | If you can reproduce your problem, enable Detailed Logging by tapping Menu > Settings . Then, under Help , tap Troubleshooting . Check the Detailed Logging check box and reproduce your issue before you send the problem report. In addition, include the timestamp when the problem occurred. |
|---|---|

| Q. | How do I send general feedback about Cisco Jabber Voice for Android ? |
|---|---|

| A. | To send general feedback about Cisco Jabber Voice for Android , complete the following steps: On the Cisco Jabber Voice for Android home screen, tap Menu > Feedback . Complete the feedback form. |
|---|---|

| Q. | Cisco Jabber Voice for Android stopped working and I see a red Cisco Jabber Voice icon ( ) in the status bar. What could be wrong? |
|---|---|

| A. | If Cisco Jabber Voice suddenly stops working, try the following troubleshooting tips: Check your connectivity to your corporate network. Check your Wi-Fi settings. If your status bar indicates that you are connected to a Wi-Fi network, verify that you are connected to the correct Wi-Fi network (that is, your corporate Wi-Fi network). Verify that you are connected to your corporate network by opening a browser and trying to connect to an internal website. If Cisco Jabber Voice still does not connect, verify your Wi-Fi settings. Verify that your network is properly set up in Cisco Jabber Voice for Android as follows: Open Cisco Jabber Voice for Android and tap Menu > Settings . Tap Corporate Wi-Fi Networks > Preset Wi-Fi Networks and verify that your network SSID is listed. If your network SSID is not listed in the Preset Wi-Fi Networks list, tap Menu > Settings . Tap Corporate Wi-Fi Networks > Custom Wi-Fi Networks . Locate the network SSID that you are connected to, and ensure that the check box is checked. If it is unchecked, check it and then exit Cisco Jabber Voice for Android and relaunch the application. Check if your VPN is connected (if VPN is required). If not, contact your system administrator. Check for the Cisco Jabber Voice for Android error icon ( ) in the status bar. If there is an error, swipe down the status bar to view details about the error. For some error messages, you can tap the notification message to go to an associated screen or popup window to try to resolve the error. If you have an error such as SIP digest authentication failure, a server error, or no network connectivity, contact your administrator for assistance. Check your account settings. In Cisco Jabber Voice for Android , tap Menu > Settings . Under Accounts, check whether any of your accounts have errors or are not connected. If so, contact your administrator for assistance. If you have more than one mobile device, check whether you are logged in twice on different mobile devices using the same "BOT" device ID. To test whether you are logged in twice, disable one device and contact your administrator to see if the corporate calling system shows that your device registered. If the device is registered, then you may have another Cisco Jabber Voice device that is registering with your account, which prevents your second device from functioning properly. |
|---|---|

| Q. | I'm on company premises and I'm connected to the Wi-Fi network, but I cannot get Cisco Jabber Voice for Android to work. What could be wrong? |
|---|---|

| A. | Check your Wi-Fi settings. If your status bar indicates that you are connected to a Wi-Fi network, verify that you are connected to the correct Wi-Fi network (that is, your corporate Wi-Fi network). To verify that you are connected to your corporate Wi-Fi network, open a browser and try to connect to an internal website. If you are properly connected, Cisco Jabber Voice for Android should automatically connect. If Cisco Jabber Voice still does not connect, verify your Wi-Fi settings using the following steps: In Cisco Jabber Voice for Android , tap Menu > Settings . Tap Corporate Wi-Fi Networks > Custom Wi-Fi Networks . Verify that the access point that you are connected to has a green check mark beside it. If not, tap the check box to add the green check mark. |
|---|---|

| Q. | I'm using Android OS 4.0 and Cisco Jabber Voice for Android won't connect to my calling system? Why not? |
|---|---|

| A. | Due to a limitation with some versions of Android OS 4.0, Cisco Jabber Voice cannot register to Cisco Unified Communications Manager on some devices. Cisco is working with select device manufacturers to resolve this issue at the Android OS level. |
|---|---|

| Q. | I see the Cisco Jabber Voice for Android icon ( ) in the status bar. How do I resolve the error? |
|---|---|

| A. | Swipe down the status bar to view details about the error. For some error messages, you can tap the notification message to go to an associated screen or popup window to try to resolve the error. |
|---|---|

| Q. | I can't see my Cisco Jabber Voice icon in the status bar when I'm connected. What could be wrong? |
|---|---|

| A. | Due to a limitation of Android OS, this problem can occur if you use Cisco Jabber Voice for Android with the Samsung Galaxy Nexus with Android OS 4.0. To check your connection status, complete the following steps: In Cisco Jabber Voice for Android , tap Menu > Settings . Under Accounts , check the connection status for the related feature. Connected: Feature is set up and connected properly. Connecting: Feature is currently making a connection attempt. Disconnected: Feature is set up but is not currently connected. For example, you see this connection status if the corporate network is not properly connected or the server is down. Error: Feature is not currently set up or connected. For example, you see an error if you enter an incorrect password. |
|---|---|

| Q. | When I move outside of my corporate Wi-Fi network, it takes a long time for Cisco Jabber Voice for Android to register to the corporate calling system. What's wrong? |
|---|---|

| A. | Due to VPN limitations, Cisco Jabber Voice for Android can take over 2 minutes to register to the Cisco Unified Communications server after you transition from the corporate Wi-Fi network to the VPN. |
|---|---|

| Q. | Cisco Jabber Voice for Android does not ring when I have an incoming call, and the option to make a call using Cisco Jabber Voice is disabled or unavailable. What's wrong? |
|---|---|

| A. | Cisco Jabber Voice for Android must be registered to the server and running on your Android device to receive incoming calls. Verify the following: The device is connected to your corporate network. Verify your Wi-Fi settings to make sure you are still connected to your corporate network. The device is connected to a preferred Wi-Fi network. Verify your Custom Wi-Fi Networks settings to make sure you enable the Wi-Fi network to which you want to connect. On the Cisco Jabber Voice for Android home screen, tap Menu > Settings . Tap Corporate Wi-Fi Networks > Custom Wi-Fi Networks . Ensure that you check the desired Wi-Fi network check box to enable Cisco Jabber Voice for Android to register to the network. |
|---|---|

| Q. | When I received an incoming call to my mobile phone number, I noticed that the audible ringtone automatically changed to silent mode. What's wrong? |
|---|---|

| A. | This problem can occur if you use a Samsung Galaxy S II SGH-I777 (AT&T) with Android OS 2.3.6 while Cisco Jabber Voice for Android runs in the background, and you receive an incoming call to your mobile phone number. To resolve this issue, do the following: From the native Android settings, uncheck the silent mode check box. Exit and relaunch Cisco Jabber Voice for Android . |
|---|---|

| Q. | When I received an incoming work call on the Cisco Jabber Voice for Android application, I could not press Accept to answer the call. What is wrong? |
|---|---|

| A. | This problem can occur due to operating system limitations. To resolve this issue, lock the screen and then unlock it. |
|---|---|

| Q. | After I received an incoming mobile voice call when I was already on a Cisco Jabber Voice for Android call, Cisco Jabber Voice disconnected from the corporate calling system. What could be wrong? |
|---|---|

| A. | If your mobile voice service provider does not support simultaneous voice and data connections on your device, you may experience the following issues if you are already on a Cisco Jabber Voice for Android call and you receive a new incoming mobile voice call to your device: Cisco Jabber Voice for Android disconnects from the corporate calling server. You temporarily lose audio. |
|---|---|

| Q. | After I received an incoming mobile voice call when I was already on a Cisco Jabber Voice for Android call, I lost my audio connection. What could be wrong? |
|---|---|

| A. | If your mobile voice service provider does not support simultaneous voice and data connections on your device, you may experience the following issues if you are already on a Cisco Jabber Voice for Android call and you receive a new incoming mobile voice call to your device: Cisco Jabber Voice for Android disconnects from the corporate calling server. You temporarily lose audio. |
|---|---|

| Q. | Cisco Jabber Voice for Android shut down unexpectedly. What do I do? |
|---|---|

| A. | Restart the Cisco Jabber Voice for Android application. You do not need to enter your setup information again. If the problem persists, contact your system administrator. |
|---|---|

| Q. | I was already on a Cisco Jabber Voice for Android Internet call when I accepted a mobile voice call. After I ended the mobile voice call, I received a "Call failed" error for my Cisco Jabber Voice for Android Internet call. Why? |
|---|---|

| A. | Due to a limitation on certain mobile carriers, while Cisco Jabber Voice for Android is connected to a VPN, you may not be able to resume a Cisco Jabber Voice for Android Internet call after you accept an incoming mobile voice call and then end it quickly. |
|---|---|

| Q. | During an Internet call, I received a message that the call failed. After I tap OK on the message, the call log appears. Can I continue my call? |
|---|---|

| A. | Calls sometimes drop if: The device disconnects from the Wi-Fi. Look for the black Cisco Jabber Voice icon ( ) in the status bar to verify that Cisco Jabber Voice for Android is registered and available. Then, tap the call in the standard call log on your Android device to redial. The application must preregister. If your system administrator makes changes to your setup, the application preregisters twice (once, and again 30 seconds later). Look for the black Cisco Jabber Voice icon ( ) in the status bar to verify that Cisco Jabber Voice for Android is registered and available. Then, tap the call in the standard call log on your Android device to redial. There is a codec mismatch. Codec mismatches occur if your system does not already handle codec mismatches, and some but not all the devices in a call use low bandwidth mode. For example: You make a call to, or receive a call from a device that does not support the low bandwidth codec (G.729a or G.729b). In both cases, the call is immediately disconnected. You initiate a conference call with low bandwidth mode turned on, but the device of another person on the conference call does not support the same low bandwidth codec (G.729a or G.729b). You or the other person may be immediately disconnected from the conference call. To resolve these issues, turn off low bandwidth mode and then retry. In Cisco Jabber Voice for Android , tap Menu > Settings . Turn off Use low bandwidth mode . |
|---|---|

| Q. | I turned on low bandwidth mode, but now I can't hear any audio on my Internet calls. Why not? |
|---|---|

| A. | To use low bandwidth mode, one of the following must be true: Your system is set up to handle calls between devices that use different codecs Both your device and the device of the person you are calling support the same low bandwidth codec (G.729a or G.729b) If these conditions are not met, you may not be able to hear audio. To verify your system setup, contact your system administrator. |
|---|---|

| Q. | I was on an Internet call and the person I called could not hear my audio for a few seconds. What could be wrong? |
|---|---|

| A. | This problem can occur when you are roaming between access points within your corporate Wi-Fi network. Audio should return to normal within a few seconds. |
|---|---|

| Q. | I tried to move my Cisco Jabber Voice for Android Internet call to my mobile voice network, but the "Use mobile network" option was not available. Why not? |
|---|---|

| A. | The option to move your Cisco Jabber Voice for Android Internet call to your mobile voice network is not available if you are connected to your corporate network using VPN over either your mobile data network or a noncorporate Wi-Fi network. |
|---|---|

| Q. | When I received a Cisco Jabber Voice for Android call, I saw the person's caller ID, but now I can't see the caller ID in my recents list. Why not? |
|---|---|

| A. | The native Android call log does not store Caller ID information that is obtained from a remote location. Therefore, you can see the Caller ID information during a call, but only the number is stored in the native Android call log after the call ends. Tip You can add the contact to the native Android Contacts application to resolve the caller ID information. | Tip | You can add the contact to the native Android Contacts application to resolve the caller ID information. |
|---|---|---|---|
| Tip | You can add the contact to the native Android Contacts application to resolve the caller ID information. |

| Tip | You can add the contact to the native Android Contacts application to resolve the caller ID information. |
|---|---|

| Q. | Can I install Cisco Jabber Voice for Android on the SD card of my device? |
|---|---|

| A. | Cisco does not support the installation of Cisco Jabber Voice for Android on a Secure Digital (SD) card. Cisco Jabber Voice for Android must always run in the background to work properly. The Android OS terminates applications that you installed on the SD card when the SD card is mounted as a disk drive. |
|---|---|

| Q. | I'm trying to upgrade from Cisco Jabber for Android Release 8.6.x to Cisco Jabber Voice for Android Release 9.1.4, but the app won't install. Why not? |
|---|---|

| A. | To upgrade from Cisco Jabber for Android Release 8.6.x to Cisco Jabber Voice for Android Release 9.1.4, you must first uninstall the previous version of the product from your device. |
|---|---|

| Q. | With my previous version of Cisco Jabber Voice for Android , I used secure connect to connect to my corporate network from a remote location, but now I can't see that feature. Can I still use Cisco Jabber Voice for Android from a remote location? |
|---|---|

| A. | Yes, you can still use Cisco Jabber Voice for Android when you are away from your corporate Wi-Fi network if your administrator set up your system to use VPN. For more information, contact your administrator. |
|---|---|

| Q. | With my previous version of Cisco Jabber Voice for Android , I used secure connect to connect to my corporate network from a remote location, but now my administrator asked me to use a VPN client. Does Cisco Jabber Voice for Android work differently with a VPN client than it did with secure connect? |
|---|---|

| A. | Both secure connect and VPN allow you use Cisco Jabber Voice for Android to place work calls over the Internet when you are outside of your corporate network. However, VPN clients differ from secure connect as follows: VPN clients secure your whole device as opposed to the Cisco Jabber Voice for Android application only. VPN clients do not maintain active calls if you transition between your mobile data network and your corporate Wi-Fi network. Instead, you must either end your call or transfer it to your mobile voice network before you transition between networks. VPN clients re-register more frequently when you transition between networks. |
|---|---|

| Q. | I'm using a noncorporate Wi-Fi network, but I can't get Cisco Jabber Voice for Android to connect to my corporate network. What could be wrong? |
|---|---|

| A. | To resolve your connection issue, try one of the following: Check whether you are connected through VPN. When you are away from the office, you can use a Wi-Fi or mobile data network, but you also must use a VPN connection to your corporate network. You must set up this VPN connection before you use Cisco Jabber Voice for Android . Contact your system administrator if you need assistance. If DVO is not enabled, verify that you turned on the Use noncorporate Wi-Fi setting. In Cisco Jabber Voice for Android , tap Menu > Settings . Under General, verify that you turned on Use noncorporate Wi-Fi to enable your VPN to automatically connect to your corporate network when you are connected to a noncorporate Wi-Fi network. |
|---|---|

| Q. | My battery seems to drain faster when I use Cisco Jabber Voice for Android . What could cause this? |
|---|---|

| A. | Like other Android applications, Cisco Jabber Voice for Android consumes more power when used with a mobile data network. In addition, some settings can cause high battery drain while Cisco Jabber Voice for Android is idle. To reduce battery drain, update your selected Custom Wi-Fi Networks. When Cisco Jabber Voice for Android is running in the background, it maintains a connection to the server. If this connection is lost, it continually tries to reconnect, which uses more power. To prevent this power drain, you can set Cisco Jabber Voice for Android to reconnect only when your device is connected to specific Wi-Fi networks (other than the networks that your system administrator presets, which you cannot change). Open Cisco Jabber Voice for Android and tap Menu > Settings . Tap Corporate Wi-Fi Networks > Custom Wi-Fi Networks . |
|---|---|

| Q. | When I use Cisco Jabber Voice for Android with Internet calling to participate in a Cisco WebEx conference, I have a hard time hearing participants and they have a hard time hearing me. What do I do? |
|---|---|

| A. | Tap Hold , and then tap Resume . |
|---|---|

| Q. | When I'm using VPN and Internet calling and my phone rings, the phone stops ringing before I can answer it. What can I do? |
|---|---|

| A. | Contact your system administrator to verify that the SIP dual-mode alert timer is set to the recommended value. Your administrator can set the SIP dual-mode alert timer value to extend the length of time that the systems rings the Cisco Jabber Voice for Android application. |
|---|---|

| Q. | I'm using VPN to connect to my corporate network and I answer an Cisco Jabber Voice for Android Internet call, but I can't hear audio and the caller gets sent to my voicemail. What could be the problem? |
|---|---|

| A. | If you answer an incoming Internet call when you use VPN to connect to your corporate network, the Accept signal sometimes cannot reach the corporate calling system because of network delays. As a result, the corporate calling system sends the call to voicemail. This problem occurs if the network does not communicate the acceptance to the calling server on time. For best results, connect to a better quality Wi-Fi or mobile data network. |
|---|---|

| Q. | During setup, Cisco Jabber Voice for Android prompted me for SIP Digest Authentication credentials, but my system administrator didn't give me that information. I entered some text and the application accepted it. Is my device authenticated properly? |
|---|---|

| A. | No. Contact your system administrator to verify that SIP Digest Authentication is set up properly on the system. |
|---|---|

| Q. | I can't download my voice messages using visual voicemail. Can I call the voicemail system directly? |
|---|---|

| A. | Yes. From the Voice Messages screen, tap Menu > Call Voicemail . |
|---|---|

| Q. | I see a notification that my voicemail credentials are not valid but I entered the correct username and password. What could cause this? |
|---|---|

| A. | You may see this message if your voicemail account is locked. Your voicemail account may be locked for either of the following reasons: Your voicemail administrator locks your account. The voicemail system locks your account after too many failed login attempts. To resolve a locked voicemail account, contact your voicemail administrator. |
|---|---|

| Q. | I see a notification that I lost the connection to my voicemail server because of expired or invalid credentials, but I can't change my password. What can I do? |
|---|---|

| A. | You cannot change your voicemail password in Cisco Jabber Voice for Android . To resolve this issue, go to the Cisco Personal Communications Assistant (PCA) to change your password. To access your Cisco PCA, go to http:// <Cisco Unity Connection server> /ciscopca. |
|---|---|

| Q. | I was on the Deleted Voice Messages screen and after I declined an incoming call I did not see any more incoming calls. Why not? |
|---|---|

| A. | This is a known issue. To resolve this issue, tap the Search tab or place a Cisco Jabber Voice for Android call. |
|---|---|

| Q. | When I make an Internet call to certain numbers, the calls immediately drop. What could be wrong? |
|---|---|

| A. | Check your settings to see if low bandwidth mode is turned on. Calls sometimes drop if the system is not set up to handle codec mismatches and the device used by the person you called does not support the same low bandwidth codec (G.729a or G.729b). To resolve this issue, turn off low bandwidth mode and then retry. To turn off low bandwidth mode, complete the following steps: In Cisco Jabber Voice for Android , tap Menu > Settings . Turn off Use low bandwidth mode . |
|---|---|

| Q. | Sometimes my directory search is slow or it doesn't work at all. What could be the problem? |
|---|---|

| A. | If you use a 3G mobile data network to remotely connect to your corporate network, network delays can cause issues with directory searches. For best results, you must connect to a better quality Wi-Fi or mobile data network. |
|---|---|

| Q. | When I check my call log, calls that I received in Cisco Jabber Voice for Android don't display correctly. What could be wrong? |
|---|---|

| A. | If you receive a call from someone who is not already in your contact list, the Android operating system uses a default format to display the call log entry. After the operating system applies the default format to the Cisco Jabber Voice for Android phone numbers, some phone numbers do not display correctly in the call logs. For example, the call log displays a call received from John Doe at 8-555-1234 as an Unknown caller at 855-512-34. To resolve this issue, you can add new contacts to your contact list with the correct formatting. The call log recognizes phone numbers in your contact list and displays them using the formatting that you apply to the contact list entry. |
|---|---|

| Q. | I can't use silent mode or vibrate for my incoming Cisco Jabber Voice for Android calls. Why not? |
|---|---|

| A. | You cannot use silent mode or vibrate for incoming Cisco Jabber Voice for Android calls if your administrator set a minimum volume for the ringtone. |
|---|---|

| Q. | I can't change my ringtone for my Cisco Jabber Voice for Android calls. Why not? |
|---|---|

| A. | You cannot change the ringtone if your administrator set your device to always use the Cisco Jabber Voice ringtone for Cisco Jabber Voice for Android calls. When an administrator sets the app to use the Cisco Jabber Voice ringtone, only the calls on your native Android Phone application use the native Android ringtones. |
|---|---|

| Q. | I added a contact and entered some information in the Organization field, but I can't see the "Organization" title in the contact's information. What could be wrong? |
|---|---|

| A. | Due to device limitations, when using Samsung Galaxy S II SC-02C with Android OS 2.3.3, the device does not display the "Organization" title after you add a new contact and enter information for the contact's organization. |
|---|---|

| Q. | I'm having problems when I use my headset with Cisco Jabber Voice for Android . What could be wrong? |
|---|---|

| A. | Verify that you are using the official headset for your Android device. Cisco supports only the official headset for your device. If you use another model of headset, you may experience the following issues: Called party hears poor audio quality Audio path is missing in one direction Audio is intermittently sent to the wrong audio channel Audio for a second call goes to handset instead of wired headset If you use the official model of headset and you experience problems, contact your administrator for support. |
|---|---|

| Q. | When I use my earbuds with Cisco Jabber Voice for Android , the audio goes to my handset instead of the earbuds. What could be wrong? |
|---|---|

| A. | Verify that you check the checkbox to enable the earbuds as follows. Tap the Android Settings application. Tap Accessory . Check the Audio applications check box. |
|---|---|

| Q. | Why don't I see the Jabber calling options in my settings menu? |
|---|---|

| A. | Your administrator must enable the DVO feature before you can see the Jabber calling options in your settings menu. For more information, contact your administrator. |
|---|---|

| Q. | If I set my calling option to Always use DVO and try to make a DVO call, the call doesn’t connect. What could be wrong? |
|---|---|

| A. | This problem can occur if your administrator enabled the DVO feature on an unsupported version of the corporate calling server. Contact your system administrator to resolve this issue. |
|---|---|

| Q. | If I set my calling option to Automatically select and try to make a DVO call, the call doesn’t connect. What could be wrong? |
|---|---|

| A. | This problem can occur if you try to make a call from outside your corporate Wi-Fi network and your administrator enabled the DVO feature on an unsupported version of the corporate calling server. Contact your system administrator to resolve this issue. |
|---|---|

| Q. | Cisco Jabber Voice is prompting me for a DVO callback number. What is that? |
|---|---|

| A. | A DVO callback number is the phone number that the DVO feature uses to start calls. DVO allows you to place calls with your work number using the voice plan for your device. If your administrator enabled the DVO feature, the default setting is "Automatically select," which enables DVO when you are not on a Wi-Fi network. Cisco Jabber Voice checks to see if you or your administrator specified a callback number before making a DVO call. If a callback number is not already specified, the application prompts you to provide one. The DVO Callback number is usually your mobile phone number. To use DVO, perform the following steps: In the DVO Callback Number field, enter the DVO callback number. This is usually your mobile phone number. Tap Save . If you do not want to use DVO, perform the following steps: Tap Settings . Tap Jabber Calling Options . Select Always use Internet . With this option, Cisco Jabber Voice functions as an Internet phone, using Wi-Fi or your mobile data plan to make calls over the Internet with your work number. |
|---|---|

| Q. | My DVO Callback Number is prefilled, and the number is different than my mobile phone number. Can I change it? |
|---|---|

| A. | Yes. Cisco Jabber Voice for Android prefills your DVO Callback Number if your administrator entered a phone number in your Mobility Identity on the corporate calling system. To change this number, enter your mobile phone number in the DVO Callback Number field. |
|---|---|

| Q. | I tried to make a DVO call, but the person I called received a call from my voicemail system or a different number. What's wrong? |
|---|---|

| A. | When you place a DVO call, the person you call can receive a call from your voicemail system or a different number in the following cases: Your mobile voice network connection is weak. To prevent this issue, verify that you have a strong mobile voice network connection before you place a DVO call. You set up your DVO Callback Number with a phone number that is different than your mobile phone number. To prevent this issue, change your DVO Callback Number to your mobile phone number in the Cisco Jabber Voice settings. Select Settings > Jabber Calling Options , and then enter the new DVO Callback Number. You do not answer your callback in time and your device is set up with voicemail. |
|---|---|

| Q. | I tried to make a DVO call, but after I pressed any number on my keypad to connect the call, the call ended. What's wrong? |
|---|---|

| A. | Due to a limitation of the corporate calling system, calls end without notification if: You place a DVO call that requires you to enter a number before the system connects the call The person you call has a busy line and that person did not set up voicemail for the deskphone If you encounter this issue, try calling the contact again at a later time. If the problem persists, contact your system administrator. |
|---|---|

| Q. | After I placed a DVO call, I heard several seconds of silence and then the call was dropped. What could be wrong? |
|---|---|

| A. | Due to a limitation of the corporate calling system, in some situations there is no audio message after you place a DVO call to an invalid phone number. To troubleshoot the problem, verify whether the phone number that you dialed is a valid phone number. |
|---|---|

| Q. | After I upgraded Cisco Jabber Voice for Android , the application registers to noncorporate Wi-Fi and mobile data networks even though I turned these settings off in the previous release. Why does this happen? |
|---|---|

| A. | If you upgrade Cisco Jabber Voice for Android and your administrator enabled the DVO feature, the application has different settings than previous releases. Cisco Jabber Voice does not display options to turn noncorporate Wi-Fi and mobile data networks on or off individually. Instead, the application automatically turns on both noncorporate Wi-Fi networks and mobile data networks. |
|---|---|

| Q. | My administrator disabled the Dial via Office feature, and now my Corporate Wi-Fi Network setting is not displaying properly. What's wrong? |
|---|---|

| A. | If your administrator sets the Dial via Office feature from enabled to disabled on the device page for a user, you may see the wrong text or no text under the Corporate Wi-Fi Network field on the Settings screen. To resolve this issue, navigate away from the Settings menu and then navigate back to the Settings menu. |
|---|---|