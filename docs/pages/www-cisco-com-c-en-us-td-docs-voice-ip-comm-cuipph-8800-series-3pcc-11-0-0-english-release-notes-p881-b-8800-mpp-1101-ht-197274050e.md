---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cuipph-8800-series-3pcc-11-0-0-english-release-notes-p881-b-8800-mpp-1101-ht-197274050e
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cuipph/8800-series/3pcc/11-0-0/english/release-notes/p881_b_8800-mpp-1101.html
retrieved_at: 2026-08-21T13:33:15.024716+00:00
---

Cisco IP Phone 8800 Series Multiplatform Phones Release Notes for Firmware Release 11.0(0)

# Cisco IP Phone 8800 Series Multiplatform Phones Release Notes for Firmware Release 11.0(0)

### Download Options

Updated: April 7, 2017

First Published:

Last Updated:

Text Part Number:

# Introduction

These release notes support the Cisco IP Phone 8800 Series Multiplatform Phones running SIP Firmware Release 11.0(0).

The following table lists the support and protocol compatibility for the
		Cisco IP Phones.

Cisco IP Phone

Protocol

Support Requirements

Cisco IP Phone 8800 Series Multiplatform Phones

SIP

BroadSoft BroadWorks 21.0

Asterisk 13.1

## Related
	 Documentation

Use the following sections to
		obtain related information.

### Cisco IP Phone 8800 Series Documentation

Refer to
		  publications that are specific to your language, phone model, and call control
		  system. Navigate from the following documentation URL:

https:/​/​www.cisco.com/​c/​en/​us/​products/​collaboration-endpoints/​unified-ip-phone-8800-series/​index.html

## New and Changed
	 Features

The following sections describe the features that are new or have
		changed in this release.

### Backlight Updates

You can now configure the backlight timer from the User tab of the phone Configuration Utility.

#### Where to Find More Information

Cisco IP Phone 8800 Series Multiplatform Phones User Guide

### Bluetooth Updates

You can now configure Bluetooth from the Voice tab of the phone Configuration Utility. Your mobile phone can use any of the lines on your phone. You can pair up to three Bluetooth devices. But if you try to add more than three, the phone prompts you to delete one of the existing devices.

Bluetooth configuration has also been made easier with the Scan feature that allows you to scan your surroundings for a Bluetooth device and add it.

To scan, press Applications and navigate to Bluetooth > Devices .

#### Where to Find More Information

Cisco IP Phone 8800 Series Multiplatform Phones Administration Guide

Cisco IP Phone 8800 Series Multiplatform Phones User Guide

### Busy Lamp Field List URI

The BLF List URI now overrides the extended function setting when you enable Use Line Keys For BLF List.

#### Where to Find More Information

Cisco IP Phone 8800 Series Multiplatform Phones Administration Guide

### Call Forward Updates

You can now configure call forward from the phone Configuration Utility. You can now use star codes to access call forward.

#### Where to Find More Information

Cisco IP Phone 8800 Series Multiplatform Phones User Guide

Cisco IP Phone 8800 Series Multiplatform Phones Administration Guide

### Call History Updates

The Call History softkey is now called Recents . Call history now stores 180 records. Users can add contacts from call history records.

#### Where to Find More Information

Cisco IP Phone 8800 Series Multiplatform Phones User Guide

### Call Pickup

On the Configuration Utility page, the Call Pickup Code field is now located  in the phone Configuration Utility at Admin Login > advanced > Voice > Regional .

#### Where to Find More Information

Cisco IP Phone 8800 Series Multiplatform Phones Administration Guide

### Dial Assistance

With dial assistance, a user can make calls more quickly. You need to enable the feature on the phone Configuration Utility page. After you enable the feature, as a user dials to make a call the phone displays the  phone numbers that are closely-matched to the entries in the phone directory and call history. If you do not enable the feature, the dial assistance list does not appear on the phone screen.

#### Where to Find More Information

Cisco IP Phone 8800 Series Multiplatform Phones User Guide

Cisco IP Phone 8800 Series Multiplatform Phones Administration Guide

### Do Not Disturb Updates

You can enable or disable do not disturb (DND) by dialing the respective star code that is configured for a phone. You can continue to use either the phone Configuration Utility, the phone LCD menu, or the softkey on the phone to perform the same task.

#### Where to Find More Information

Cisco IP Phone 8800 Series Multiplatform Phones User Guide

Cisco IP Phone 8800 Series Multiplatform Phones Administration Guide

### Enhanced Line Mode

The buttons on the left and right of the phone screen can be set up as line buttons, giving up to five more line keys. You can also configure up to ten calls per line.

With Enhanced Line Mode, you now use the navigation cluster to navigate between lines. Use the line key to open the call session window, and to navigate through the call window. Open the call session window to see the active calls on a line.

Enhanced line mode is enabled by default.

#### Where to Find More Information

Cisco IP Phone 8800 Series Multiplatform Phones User Guide

Cisco IP Phone 8800 Series Multiplatform Phones Administration Guide

### Feature Key Synchronization

You can enable synchronization of do not disturb (DND) and call forward to allow changes to these features on the phone or on the server.

You enable this synchronization in the Feature Key Sync field in the phone Configuration Utility at Admin Login > advanced > Voice > Ext [n] (where [n] is the extension number).

#### Where to Find More Information

Cisco IP Phone 8800 Series Multiplatform Phones Administration Guide

### Hoteling

Hoteling allows your users to sign in to a phone as a guest.

You enable this feature in the Enable Broadsoft Hosting field in the phone Configurarion Utility at Admin Login > advanced > Voice > Ext [n] . Set the amount of time (in seconds) that the user can be signed in as a guest on the phone in Hoteling Subscription Expires .

#### Where to Find More Information

Cisco IP Phone 8800 Series Multiplatform Phones User Guide

Cisco IP Phone 8800 Series Multiplatform Phones Administration Guide

### Programmable Softkeys Updates

You can use new keywords and Key Lists for the softkeys. However, some older keywords and Key Lists are no longer supported.

The following table contains the new keywords.

acd_login

lcr

acd_logout

left

astate

miss

avail

option

confLx

right

dir

starcode

em_login

unavail

em_logout

xferlx

#### Where to Find More Information

Cisco IP Phone 8800 Series Multiplatform Phones Administration Guide

### Provisioning Authority Timeout

You can specify how long a phone can be inactive before it automatically signs out from the provisioning authority.

You set this length of time in the Inactivity Timer(m) field in the phone Configuration Utility at Admin Login > Advanced > Voice > Phone . You also set the amount of time that the user has to cancel the sign-out in the Countdown Timer(s) field.

#### Where to Find More Information

Cisco IP Phone 8800 Series Multiplatform Phones Administration Guide

### PRT Upload Updates

When users submit the log files generated by the Problem Report Tool (PRT), the files are uploaded to the URL that you set in the phone Configuration Utility. Set the PRT Upload Rule field instead of the PRT Upload URL field.

#### Where to Find More Information

Cisco IP Phone 8800 Series Multiplatform Phones User Guide

Cisco IP Phone 8800 Series Multiplatform Phones Administration Guide

### Remote Customization Updates

The phone does not completely reboot after the remote customization download from the Enablement Data Orchestration System (EDOS) server. Only the voice process is restarted. So, a user would see flashing LED lights when the voice application restarts in the background.

You can view the customization state in the Customization field in the phone Configuration Utility at Admin Login > Info > Status .

Alternately, you can press Applications on the phone and navigate to Status > Product information > Customization view the customization state on the phone screen.

#### Where to Find More Information

Cisco IP Phone 8800 Series Multiplatform Phones User Guide

Cisco IP Phone 8800 Series Multiplatform Phones Administration Guide

### Screen Saver Updates

You can configure the screen saver for a phone using the User tab (instead of the Phone tab) on the phone Configuration Utility page.

Users can set up screen savers from the User preferences menu on the phone.

#### Where to Find More Information

Cisco IP Phone 8800 Series Multiplatform Phones User Guide

Cisco IP Phone 8800 Series Multiplatform Phones Administration Guide

### Single Paging (Intercom) and Server-Configured Paging

With single paging (intercom), users can automatically page a phone.

With server-configured paging, users can page specific groups of phones. The administrator configures paging groups on the server. All the phones that are part of the paged group receive the page.

#### Where to Find More Information

Cisco IP Phone 8800 Series Multiplatform Phones User Guide

Cisco IP Phone 8800 Series Multiplatform Phones Administration Guide

### Speed Dial Configuration

You can configure Speed Dials on the phone with the web interface. On the phone Configuration Utility page, select Admin Login > Voice > User and navigate to the Speed Dial section on the page.

#### Where to Find More Information

Cisco IP Phone 8800 Series Multiplatform Phones Administration Guide

### Speed Dial Updates

On the phone, users can set up speed dials. They can hold  a disabled extended line key or navigate to the Speed dials menu.

#### Where to Find More Information

Cisco IP Phone 8800 Series Multiplatform Phones User Guide

### TR-069 Protocols and Standards

You can use Technical Report 069 (TR-069) to manage your phones and call control system. With this release, the phones now support the TR-069 protocol.

You enable this feature in the Enable TR-069 field in the phone Configuration Utility at Admin Login > advanced > Voice > TR-069 .

#### Where to Find More Information

Cisco IP Phone 8800 Series Multiplatform Phones Administration Guide

### USB Headsets and Audio Path Switching

Users can easily switch the audio path while on a call.

If a USB headset is plugged in during an active call, the audio path switches to the USB headset.

When a USB headset is unplugged while in use during a call, the call audio routes to the speaker.

The USB Accessory information is shown when you press Applications and navigate to Status > Accessories in the Information and Settings screen.

Audio in/out input is not supported on the Cisco IP Phone 8861.

Swap a headset while on a call

Specify an audio device for a call

Select of an audio path for a call dynamically

#### Where to Find More Information

Cisco IP Phone 8800 Series Multiplatform Phones User Guide

### User Passwords

Users are now prompted to set a password the first time their phone boots up.

#### Where to Find More Information

Cisco IP Phone 8800 Series Multiplatform Phones User Guide

Cisco IP Phone 8800 Series Multiplatform Phones Administration Guide

### Voicemail

Users can now configure voicemail on their phones if you haven't set it up for them.

An exclamation mark (!) indicates urgent voicemail messages.

#### Where to Find More Information

Cisco IP Phone 8800 Series Multiplatform Phones User Guide

### Wallpaper Updates

You can download the wallpaper images for a phone using the User tab (instead of the Phone tab) on the phone Configuration Utility page.

Users can configure the wallpaper  from the User preferences menu on the phone.

#### Where to Find More Information

Cisco IP Phone 8800 Series Multiplatform Phones User Guide

Cisco IP Phone 8800 Series Multiplatform Phones Administration Guide

### XML Applications

You can create XML applications for your users to use on their phones.

XML applications are supported on programmable line keys and programmable softkeys. Configure XML applications from the phone Configuration Utility page, in the XML Service section of the Phone tab.

For more information, see the Cisco Unified IP Phone Services Application Development Notes located here: http:/​/​www.cisco.com/​c/​en/​us/​td/​docs/​voice_ip_comm/​cuipph/​all_models/​xsi/​9-1-1/​CUIP_​BK_​P82B3B16_​00_​phones-services-application-development-notes.html .

#### Where to Find More Information

Cisco IP Phone 8800 Series Multiplatform Phones Administration Guide

## Installation

### Upgrade Firmware

The Cisco IP Phone 8800 Series Multiplatform Phones supports a single image upgrade by TFTP, HTTP, or HTTPS.

http:/​/​software.cisco.com/​download/​navigator.html?mdfid=284883944&i=rm

<schema>://<serv_ip[:port]>/filepath/sipxxx.loads

The third-party call control can also upgrade via a URL in the web browser:

<schema>://<serv_ip[:port]>/filepath/sipxxx.loads

Here is an example,

http://10.74.10.225/firmware/sip88xx.11-0-0MPP-7dev.loads

The loads file is put in the file path of the above url. The zip file contains other file types also. Only the loads file is used in the above URL.

## Limitations and Restrictions

### Phone Behavior During Times of Network Congestion

Anything that degrades network performance can affect phone voice and video quality, and in some cases, can cause a call to drop. Sources of network degradation can include, but are not limited to, the following activities:

Administrative tasks, such as an internal port scan or security scan

Attacks that occur on your network, such as a Denial of Service attack

### Language Limitation

There is no localized Keyboard
Alphanumeric Text Entry (KATE) support for the following Asian
locales:

Chinese (China)

Chinese (Hong Kong)

Chinese (Taiwan)

Japanese (Japan)

Korean (Korea Republic)

The default English (United States) KATE is presented to the user instead.

For example, the phone screen will show text in Korean, but the 2 key on the keypad will display a b c 2 A B C .

### Caller Identification and Other Phone Functions

Caller identification or other phone functions have not been verified with third-party applications for the visually or hearing impaired.

### No Beep Sound Heard when the Mute Key is Pressed

When you press the Mute button during a call, you may not hear a beep sound. For anyone who is visually impaired, press the Mute button once to mute the phone and press the button twice to unmute the phone.

### Phone Has a Firmware Build Earlier than 11.0.0

Sometimes, a phone taken out of the box has a firmware build earlier than 11.0.0. When this happens, you must upgrade the firmware on your phone before you provision it.

## Caveats

### Access Cisco Bug
	 Search

Known problems
		  (bugs) are graded according to severity level. These release notes contain
		  descriptions of the following:

All severity
				level 1 or 2 bugs

Significant
				severity level 3 bugs

You can search for
		  problems by using Cisco Bug Search.

To access Cisco Bug
		  Search, you need the following items:

Internet
				connection

Web browser

Cisco.com user
				ID and password

https:/​/​tools.cisco.com/​bugsearch

### Open Caveats

The following table lists defects that are open for the Cisco IP Phone 8800 Series Multiplatform Phones for Firmware Release 11.0(0).

A registered cisco.com user ID is required to access this informaion online.

Because defect status continually changes, the table reflects a snapshot of the defects that were open at the time this report was compiled. For an updated view of resolved defects, access the Bug Search tool as described in Access Cisco Bug Search .

Identifier

Headline

CSCvb95192

Speaker volume bar shouldn't pop up when adjust the volume on the headset

CSCvc16010

Call gets disconnected on answering call through USB headset with BT headset connected

CSCvc51710

Join does not work for
conference call between different extensions on the
Phone

CSCvd04783

Available SSID network is not listed when trying to connect SSID with invalid password

CSCvd06737

Status message is not accurately displaying time

CSCvd52593

phone not send new dns query when A cache expires

CSCvd58195

Attendant console status tab shows different software versions for KEM units

### Resolved Caveats

The following table lists defects that are resolved for the Cisco IP Phone 8800 Series Multiplatform Phones for Firmware Release 11.0(0).

For more information about an individual defect, you can access the online record for the defect by accessing the Bug Search tool and entering the Identifier. You must be a registered Cisco.com user to access this online information.

Because defect status continually changes, the table reflects a snapshot of the defects that were resolved at the time this report was compiled. For an updated view of resolved defects, access the Bug Search tool as described in Access Cisco Bug Search .

Identifier

Headline

CSCvc61827

call history not record display name.

CSCvc93127

No audio/Ringer/Dial tone heard after switching from Ethernet to WI-FI.

CSCvd54756

WEB's current time still displays 24hr format after setting 12hr

CSCvd32276

No audio upon call pick up with secured call enabled on one end disabled on other.

CSCvd33476

Device unresponsive while IDLE

CSCvd38958

Phone not handling 2nd invite for forwarded call with same callid

CSCvd43575

Extension mobility - $MPWD macro not expanding

CSCvd43657

Wrong User Agent 88xx phones

CSCvd51053

Inconsistent behavior of missed call numbers on LCD after device restarts

## Cisco IP Phone
	 Firmware Support Policy

For information on the support policy for phones, see http:/​/​www.cisco.com/​c/​en/​us/​support/​docs/​collaboration-endpoints/​unified-ip-phone-7900-series/​116684-technote-ipphone-00.html .

## Documentation, Service Requests, and Additional Information

For information on obtaining documentation, submitting a service request, and gathering additional information, see the monthly What’s New in Cisco Product Documentation , which also lists all new and revised Cisco technical documentation, at:

http:/​/​www.cisco.com/​c/​en/​us/​td/​docs/​general/​whatsnew/​whatsnew.html

Subscribe to the What’s New in Cisco Product Documentation as a Really Simple Syndication (RSS) feed and set content to be delivered directly to your desktop using a reader application. The RSS feeds are a free service and Cisco currently supports RSS Version 2.0.

| Cisco IP Phone | Protocol | Support Requirements |
|---|---|---|
| Cisco IP Phone 8800 Series Multiplatform Phones | SIP | BroadSoft BroadWorks 21.0 Asterisk 13.1 |

| acd_login | lcr |
|---|---|
| acd_logout | left |
| astate | miss |
| avail | option |
| confLx | right |
| dir | starcode |
| em_login | unavail |
| em_logout | xferlx |

| Step 1 | Go to the
			 following URL: http:/​/​software.cisco.com/​download/​navigator.html?mdfid=284883944&i=rm |
|---|---|
| Step 2 | Choose Cisco
				IP Phones 8800 Series . |
| Step 3 | Choose your
			 phone model. |
| Step 4 | Choose Session Initiation Protocol (SIP) Software . |
| Step 5 | In the Latest
			 Releases folder, choose 11.0(0) . |
| Step 6 | Download the file cmterm-88xx.11-0-0MPP-7.zip. |
| Step 7 | Unzip the files. |
| Step 8 | Put the files on the tftp/http/https download directory. |
| Step 9 | Configure the Upgrade Rule on the Provisioning tab in the web page with the valid URL. The  format is: <schema>://<serv_ip[:port]>/filepath/sipxxx.loads The third-party call control can also upgrade via a URL in the web browser: <schema>://<serv_ip[:port]>/filepath/sipxxx.loads Here is an example, http://10.74.10.225/firmware/sip88xx.11-0-0MPP-7dev.loads Note The loads file is put in the file path of the above url. The zip file contains other file types also. Only the loads file is used in the above URL. After the firmware upgrade completes, the phone reboots automatically. | Note | The loads file is put in the file path of the above url. The zip file contains other file types also. Only the loads file is used in the above URL. |
| Note | The loads file is put in the file path of the above url. The zip file contains other file types also. Only the loads file is used in the above URL. |

| Note | The loads file is put in the file path of the above url. The zip file contains other file types also. Only the loads file is used in the above URL. |
|---|---|

| Step 1 | To access Cisco Bug Search, go to: https:/​/​tools.cisco.com/​bugsearch |
|---|---|
| Step 2 | Log in with your
			 Cisco.com user ID and password. |
| Step 3 | To look for
			 information about a specific problem, enter the bug ID number in the Search for
			 field, then press Enter . |

| Note | A registered cisco.com user ID is required to access this informaion online. |
|---|---|

| Identifier | Headline |
|---|---|
| CSCvb95192 | Speaker volume bar shouldn't pop up when adjust the volume on the headset |
| CSCvc16010 | Call gets disconnected on answering call through USB headset with BT headset connected |
| CSCvc51710 | Join does not work for
conference call between different extensions on the
Phone |
| CSCvd04783 | Available SSID network is not listed when trying to connect SSID with invalid password |
| CSCvd06737 | Status message is not accurately displaying time |
| CSCvd52593 | phone not send new dns query when A cache expires |
| CSCvd58195 | Attendant console status tab shows different software versions for KEM units |

| Identifier | Headline |
|---|---|
| CSCvc61827 | call history not record display name. |
| CSCvc93127 | No audio/Ringer/Dial tone heard after switching from Ethernet to WI-FI. |
| CSCvd54756 | WEB's current time still displays 24hr format after setting 12hr |
| CSCvd32276 | No audio upon call pick up with secured call enabled on one end disabled on other. |
| CSCvd33476 | Device unresponsive while IDLE |
| CSCvd38958 | Phone not handling 2nd invite for forwarded call with same callid |
| CSCvd43575 | Extension mobility - $MPWD macro not expanding |
| CSCvd43657 | Wrong User Agent 88xx phones |
| CSCvd51053 | Inconsistent behavior of missed call numbers on LCD after device restarts |