---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cuipph-8800-series-3pcc-11-0-1-english-firmware-releasenotes-p881-b-ip-phone-c27f4f3dcb
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cuipph/8800-series/3pcc/11-0-1/english/firmware/releasenotes/p881_b_ip-phone-8800-release-notes.html
retrieved_at: 2026-08-21T13:33:06.523457+00:00
---

Cisco IP Phone 8800 Series Multiplatform Phones Release Notes for Firmware Release 11.0(1)

# Cisco IP Phone 8800 Series Multiplatform Phones Release Notes for Firmware Release 11.0(1)

### Download Options

Updated: June 29, 2017

First Published:

Last Updated:

Text Part Number:

# Introduction

These release notes support the Cisco IP Phone 8800 Series Multiplatform Phones running SIP Firmware Release 11.0(1).

The following table lists the support and protocol compatibility for the Cisco IP Phones.

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

### Auto Detection of Key Expansion Modules

A key expansion module is enabled automatically after it is attached to the phone.

#### Where to Find More Information

Cisco IP Phone 8800 Series Multiplatform Phones User Guide

Cisco IP Phone 8800 Series Multiplatform Phones Administration Guide

### Conference Button with Star Code

You can add a star code that represents a conference bridge URL to the Conference button on the phone. When you enable the star code in the button, your user can combine many active calls into a single conference call by pressing the Conference button only once.

#### Where to Find More Information

Cisco IP Phone 8800 Series Multiplatform Phones User Guide

Cisco IP Phone 8800 Series Multiplatform Phones Administration Guide

### Remote Pinging and Factory Reset with Phone Web Page

If you have access to the phone admin page, you can ping a destination to identify the phone issue or perform a factory reset.

#### Where to Find More Information

Cisco IP Phone 8800 Series Multiplatform Phones User Guide

Cisco IP Phone 8800 Series Multiplatform Phones Administration Guide

### Wallpaper Enhancement in Cisco IP Phone 8800 Series

The Cisco IP Phone 8800 series phone has a clear and bright status bar appearance. White overlay of the wallpaper is removed. The darker wallpaper has bright color font for the line and status bar. When the phone starts for the first time and has no wallpaper added, it displays monocolor background.

#### Where to Find More Information

Cisco IP Phone 8800 Series Multiplatform Phones User Guide

Cisco IP Phone 8800 Series Multiplatform Phones Administration Guide

### Customization of the New Call Window to View Line Key Details

The New Call window can be reduced to a smaller window by pressing the up key of the navigation cluster so that the user can get a quick view of the home screen. This feature facilitates a quick view to let the user use the PLK's configured with busy lamp field, speed-dial, or busy lamp field+speed-dial combos to initiate a New Call, Conference, Transfer or any other call feature which open up the New Call window.

The user can only see line keys numbered 2, 3, 4, 5, 7, 8, 9, and 10. The reduced window is restored to its original size:

If the user hits the down key on the navigation cluster.

If 5 seconds have elapsed since it has been reduced.

If the user presses any button on the device excluding the up key on Navigation cluster.

#### Where to Find More Information

Cisco IP Phone 8800 Series Multiplatform Phones User Guide

### Voice Quality Reporting

Multiplatform phones (MPP) phones provide statistics that you can use to determine the voice quality of a call. You or the phone user can receive the information about voice quality by the following means:

Configuration Utility page

Real-time Transport Protocol (RTCP) reports

SIP Publish message

#### Where to Find More Information

Cisco IP Phone 8800 Series Multiplatform Phones Administration Guide

Cisco IP Phone 8800 Series Multiplatform Phones User Guide

### Missed Call Indication

If a user is not on an active or held call and misses a call, the user needs to know about the missed call. To alert the user, configure the Handset LED Alert field on the Configuration Utility page. If you set this field to Voicemail, Missed Call , the LED on the Handset will turn on when the user has recently missed a call.

#### Where to Find More Information

Cisco IP Phone 8800 Series Multiplatform Phones Administration Guide

Cisco IP Phone 8800 Series Multiplatform Phones User Guide

### Colored Box Highlight Around the Line State Icon

When the user selects a line, the phone displays the current selected line by enclosing only the line's icon with a colored box instead of having a big rectangular outline around the whole line.

#### Where to Find More Information

Cisco IP Phone 8800 Series Multiplatform Phones User Guide

### G711u/G711a Enhancement

You can now enable or disable the G711u and G711a codecs on the phone web page.

#### Where to Find More Information

Cisco IP Phone 8800 Series Multiplatform Phones Administration Guide

### Speed Dial Updates

If you configure a line key to perform a speed dial without VID, the dialed call uses the line that is in focus.

If you configure one of the line keys on the key expansion module to perform a speed dial without VID, the dialed call uses the line that is in focus.

#### Where to Find More Information

Cisco IP Phone 8800 Series Multiplatform Phones User Guide

## Installation

### Upgrade Firmware

The Cisco IP Phone 8800 Series Multiplatform Phones supports a single image upgrade by TFTP, HTTP, or HTTPS.

http:/​/​software.cisco.com/​download/​navigator.html?mdfid=284883944&i=rm

<schema>://<serv_ip[:port]>/filepath/sipxxx.loads

The third-party call control can also upgrade via a URL in the web browser:

<schema>://<serv_ip[:port]>/filepath/sipxxx.loads

Here is an example:

http://10.74.10.225/firmware/sip78xx.11-0-1MPP-7dev.loads

The loads file is put in the file path of the above url. The zip file contains other file types also. Only the loads file is used in the above URL.

## Limitations and Restrictions

### Phone Behavior During Times of Network Congestion

Anything that degrades network performance can affect phone voice and video quality, and in some cases, can cause a call to drop. Sources of network degradation can include, but are not limited to, the following activities:

Administrative tasks, such as an internal port scan or security scan

Attacks that occur on your network, such as a Denial of Service attack

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

#### Open Caveats

The following table lists defects that are open for the Cisco IP Phone 8800 Series Multiplatform Phones for Firmware Release 11.0(1).

For more information about an individual defect, you can access the online record for the defect by accessing the Bug Search tool and entering the Identifier. You must be a registered Cisco.com user to access this online information.

Because defect status continually changes, the table reflects a snapshot of the defects that were resolved at the time this report was compiled. For an updated view of resolved defects, access the Bug Search tool as described in Access Cisco Bug Search .

##### Open Caveats for Firmware Release 11.0(1)

No bugs currently exist.

#### Resolved Caveats

The following table lists defects that are resolved for the Cisco IP Phone 8800 Series Multiplatform Phones for Firmware Release 11.0(1).

For more information about an individual defect, you can access the online record for the defect by accessing the Bug Search tool and entering the Identifier. You must be a registered Cisco.com user to access this online information.

Because the defect status continually changes, the table reflects a snapshot of the defects that were resolved at the time this report was compiled. For an updated view of resolved defects, access the Bug Search tool as described in Access Cisco Bug Search .

Identifier

Headline

CSCvc97835

Authenticated SIP Notify for Prov Refresh failing

CSCvd47529

HTTPS provisioning using a Comodo root CA is failing to provision

CSCvd18179

MPP Display Info header Issue during an Incoming Call

CSCvd30961

8861 failed to upgrade from 10.4

CSCvd38958

Phone not handling 2nd invite for forwarded call with same callid

CSCvd41747

Resync reboot loop caused by "Language Selection" field

CSCvd44012

EM login/logout renders black screen

CSCvd46037

$SWVER not expanding correctly

CSCvd72680

Subscribe failover failed, wrong behavior if change DNS record before sub retry

CSCvd90353

Hungarian translation for BLF state "Alerting" not appropriate for the context

CSCve05718

Phones are not consistent on sending un-REG when failover and fallback

CSCve28571

Device sending INVITE with port=0 in the m-line during network conference

CSCve40739

156 characters limit upgrade rule parameter

CSCve05725

un-SUBSCRIBE is not sent before un-REGISTER is sent to the server

CSCvd02954

LDAP DNS lookup not working

CSCvd02993

Call Park blind transfer - gap versus Cisco SPA

CSCvd03001

Call Pick up - gap versus Cisco SPA

CSCvd34732

Phone does not reboot with Notify check-sync

CSCvd90443

BLF intermittently and incorrectly changes to orange

CSCve05830

EM logout even if user was on an active call

CSCvc97880

8800-3PCC: MACRO handling of firmware failing

CSCvd14992

xml configuration for the GMT time zones is different between 10.4 and 11.0

CSCvd15002

Device not downloading wallpaper via https url

CSCvd17734

MPP The user-agent in the SIP REGISTER and the http GET is not the same.

CSCvd27068

IP being sent instead of hostname in HTTP request

CSCvd30979

Upon upgrade from 10.4 to 11.0 phone prompts for user password

CSCvd37087

Devices send wrong A and AAAA queries

CSCvd37438

Typo in call history web page showing \"Recieved\" instead of \"Received\"

CSCvd39075

Issue w/ DND on/off from phone and sync (as-feature-event) is enabled

CSCvd41747

Resync reboot loop caused by \"Language Selection\" field.

CSCvd43569

Missing of \"Exit\" softkey in phone menus except \"Bluetooth\".

CSCvd43657

Wrong User Agent 88xx phones

CSCvd49065

phone doesn't respect the record-route provided by the server

CSCvd51859

Wrong translation during a change of configuration via the Configuration Utility page

CSCvd56841

Wrong name displayed on received calls menu.

CSCvd63455

SIP Reg User Agent changes not taking effect without reboot

CSCve12673

User set brightness is not being preserved

CSCve36260

88xx-3PCC: CID is not update after call to BS VP

CSCve78758

88xx-3PCC: Device is continuously ringing after callprk

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

| Step 1 | Go to the following URL: http:/​/​software.cisco.com/​download/​navigator.html?mdfid=284883944&i=rm |
|---|---|
| Step 2 | Choose Cisco IP Phones 8800 Series . |
| Step 3 | Choose your phone model. |
| Step 4 | Choose Session Initiation Protocol (SIP) Software . |
| Step 5 | In the Latest Releases folder, choose 11.0(1) . |
| Step 6 | Download the file cp-88xx.11-0-1MPP-477.zip . |
| Step 7 | Unzip the files. |
| Step 8 | Put the files on the tftp/http/https download directory. |
| Step 9 | Configure the Upgrade Rule on the Provisioning tab in the web page with the valid URL. The format is: <schema>://<serv_ip[:port]>/filepath/sipxxx.loads The third-party call control can also upgrade via a URL in the web browser: <schema>://<serv_ip[:port]>/filepath/sipxxx.loads Here is an example: http://10.74.10.225/firmware/sip78xx.11-0-1MPP-7dev.loads Note The loads file is put in the file path of the above url. The zip file contains other file types also. Only the loads file is used in the above URL. After the firmware upgrade completes, the phone reboots automatically. | Note | The loads file is put in the file path of the above url. The zip file contains other file types also. Only the loads file is used in the above URL. |
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

| Identifier | Headline |
|---|---|
| CSCvc97835 | Authenticated SIP Notify for Prov Refresh failing |
| CSCvd47529 | HTTPS provisioning using a Comodo root CA is failing to provision |
| CSCvd18179 | MPP Display Info header Issue during an Incoming Call |
| CSCvd30961 | 8861 failed to upgrade from 10.4 |
| CSCvd38958 | Phone not handling 2nd invite for forwarded call with same callid |
| CSCvd41747 | Resync reboot loop caused by "Language Selection" field |
| CSCvd44012 | EM login/logout renders black screen |
| CSCvd46037 | $SWVER not expanding correctly |
| CSCvd72680 | Subscribe failover failed, wrong behavior if change DNS record before sub retry |
| CSCvd90353 | Hungarian translation for BLF state "Alerting" not appropriate for the context |
| CSCve05718 | Phones are not consistent on sending un-REG when failover and fallback |
| CSCve28571 | Device sending INVITE with port=0 in the m-line during network conference |
| CSCve40739 | 156 characters limit upgrade rule parameter |
| CSCve05725 | un-SUBSCRIBE is not sent before un-REGISTER is sent to the server |
| CSCvd02954 | LDAP DNS lookup not working |
| CSCvd02993 | Call Park blind transfer - gap versus Cisco SPA |
| CSCvd03001 | Call Pick up - gap versus Cisco SPA |
| CSCvd34732 | Phone does not reboot with Notify check-sync |
| CSCvd90443 | BLF intermittently and incorrectly changes to orange |
| CSCve05830 | EM logout even if user was on an active call |
| CSCvc97880 | 8800-3PCC: MACRO handling of firmware failing |
| CSCvd14992 | xml configuration for the GMT time zones is different between 10.4 and 11.0 |
| CSCvd15002 | Device not downloading wallpaper via https url |
| CSCvd17734 | MPP The user-agent in the SIP REGISTER and the http GET is not the same. |
| CSCvd27068 | IP being sent instead of hostname in HTTP request |
| CSCvd30979 | Upon upgrade from 10.4 to 11.0 phone prompts for user password |
| CSCvd37087 | Devices send wrong A and AAAA queries |
| CSCvd37438 | Typo in call history web page showing \"Recieved\" instead of \"Received\" |
| CSCvd39075 | Issue w/ DND on/off from phone and sync (as-feature-event) is enabled |
| CSCvd41747 | Resync reboot loop caused by \"Language Selection\" field. |
| CSCvd43569 | Missing of \"Exit\" softkey in phone menus except \"Bluetooth\". |
| CSCvd43657 | Wrong User Agent 88xx phones |
| CSCvd49065 | phone doesn't respect the record-route provided by the server |
| CSCvd51859 | Wrong translation during a change of configuration via the Configuration Utility page |
| CSCvd56841 | Wrong name displayed on received calls menu. |
| CSCvd63455 | SIP Reg User Agent changes not taking effect without reboot |
| CSCve12673 | User set brightness is not being preserved |
| CSCve36260 | 88xx-3PCC: CID is not update after call to BS VP |
| CSCve78758 | 88xx-3PCC: Device is continuously ringing after callprk |