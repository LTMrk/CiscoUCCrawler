---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cuipph-7800-series-3pcc-11-0-1-english-firmware-releasenotes-pa2d-b-ip-phone-8ddadfda68
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cuipph/7800-series/3pcc/11-0-1/english/firmware/releasenotes/pa2d_b_ip-phone-7800-release-notes.html
retrieved_at: 2026-08-21T13:25:10.386117+00:00
---

Cisco IP Phone 7800 Series Multiplatform Phones Release Notes for Firmware Release 11.0(1)

# Cisco IP Phone 7800 Series Multiplatform Phones Release Notes for Firmware Release 11.0(1)

- 11.0(1)

- 11.0(0)

### Download Options

Updated: June 29, 2017

First Published:

Last Updated:

Text Part Number:

# Introduction

These release notes support the Cisco IP Phone 7800 Series Multiplatform Phones running SIP Firmware Release 11.0(1).

The following table lists the support and protocol compatibility for the
		Cisco IP Phones.

Cisco IP Phone

Protocol

Support Requirements

Cisco IP Phone 7800 Series Multiplatform Phones

SIP

BroadSoft BroadWorks 21.0

Asterisk 13.1

## Related
	 Documentation

Use the following sections to
		obtain related information.

### Cisco IP Phone 7800 Series Documentation

See the publications that are specific to your language, phone model, and multiplatform firmware release. Navigate from the following Uniform Resource Locator (URL):

https:/​/​www.cisco.com/​c/​en/​us/​products/​collaboration-endpoints/​unified-ip-phone-7800-series/​index.html

## New and Changed
	 Features

The following sections describe the features that are new or have
		changed in this release.

### Font Enhancement on Cisco IP Phone 7811

The font type for the Cisco IP Phone 7811 has been updated to improve readability.

#### Where to Find More Information

Cisco IP Phone 7800 Series Multiplatform Phones User Guide

### Conference Button with Star Code

You can add a star code that represents a conference bridge URL to the Conference button on the phone. When you enable the star code in the button, your user can combine many active calls into a single conference call by pressing the Conference button only once.

#### Where to Find More Information

Cisco IP Phone 7800 Series Multiplatform Phones User Guide

Cisco IP Phone 7800 Series Multiplatform Phones Administration Guide

### Remote Pinging and Factory Reset with Phone Web Page

If you have access to the phone admin page, you can ping a destination to identify the phone issue or perform a factory reset.

#### Where to Find More Information

Cisco IP Phone 7800 Series Multiplatform Phones User Guide

Cisco IP Phone 7800 Series Multiplatform Phones Administration Guide

### Incoming and Connected Call Display Enhancements

When the user selects a line, the phone displays the line state icon enclosed by a black box instead of a rectangular outline if the phone has two or more than two registered lines. In addition, the Cisco IP Phone 7841 phone screen displays 14 digits after the '+' in the caller id display.

#### Where to Find Information

Cisco IP Phone 7800 Series Multiplatform Phones User Guide

Cisco IP Phone 7800 Series Multiplatform Phones Administration Guide

### Customization of the New Call Window to View Line Key Details

The New Call window can be reduced to a smaller window by pressing the up key of the navigation cluster so that the user can get a quick view of the home screen. This feature facilitates a quick view to let the user use the PLK's configured with busy lamp field, speed-dial, or busy lamp field+speed-dial combos to initiate a New Call, Conference, Transfer or any other call feature which open up the New Call window.

The user can only see line keys numbered 2, 3, 4, 5, 7, 8, 9, and 10. The reduced window is restored to its original size:

If the user hits the down key on the navigation cluster.

If 5 seconds have elapsed since it has been reduced.

If the user presses any button on the device excluding the up key on Navigation cluster.

#### Where to Find More Information

Cisco IP Phone 7800 Series Multiplatform Phones User Guide

### Voice Quality Reporting

Multiplatform phones (MPP) phones provide statistics that you can use to determine the voice quality of a call. You or the phone user can receive the information about voice quality by the following means:

Configuration Utility page

Real-time Transport Protocol (RTCP) reports

SIP Publish message

#### Where to Find More Information

Cisco IP Phone 7800 Series Multiplatform Phones Administration Guide

Cisco IP Phone 7800 Series Multiplatform Phones User Guide

### Missed Call Indication

If a user is not on an active or held call and misses a call, the user needs to know about the missed call. To alert the user, configure the Handset LED Alert field on the Configuration Utility page. If you set this field to Voicemail, Missed Call , the LED on the Handset will turn on when the user has recently missed a call.

#### Where to Find More Information

Cisco IP Phone 7800 Series Multiplatform Phones Administration Guide

Cisco IP Phone 7800 Series Multiplatform Phones User Guide

### Wallpaper Download on 7800 Series Phones

You and your users can download a logo picture as wallpaper or phone background on the 7800 series phones from the phone web page. You can use the phone menu to set or delete the wallpaper. If you download a color logo, it is displayed as grayscale on the 7800 series phone screen.

#### Where to Find More Information

Cisco IP Phone 7800 Series Multiplatform Phones Administration Guide

Cisco IP Phone 7800 Series Multiplatform Phones User Guide

### G711u/G711a Enhancement

You can now enable or disable the G711u and G711a codecs on the phone web page.

#### Where to Find More Information

Cisco IP Phone 7800 Series Multiplatform Phones Administration Guide

### Speed Dial Updates

If you configure a line key to perform a speed dial without VID, the dialed call uses the line that is in focus.

If you configure one of the line keys on the key expansion module to perform a speed dial without VID, the dialed call uses the line that is in focus.

#### Where to Find More Information

Cisco IP Phone 7800 Series Multiplatform Phones User Guide

## Installation

### Upgrade Firmware

The Cisco IP Phone 7800 Series Multiplatform Phones supports a single image upgrade by TFTP, HTTP, or HTTPS.

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

### Open Caveats

The following table lists defects that are open for the Cisco IP Phone 7800 Series Multiplatform Phones for Firmware Release 11.0(1).

For more information about an individual defect, you can access the online record for the defect by accessing the Bug Search tool and entering the Identifier. You must be a registered Cisco.com user to access this online information.

Because the defect status continually changes, the table reflects a snapshot of the defects that were resolved at the time this report was compiled. For an updated view of resolved defects, access the Bug Search tool as described in Access Cisco Bug Search .

#### Open Caveats for Firmware Release 11.0(1)

No bugs currently exist.

### Resolved Caveats

The following table lists defects that are resolved for the Cisco IP Phone 7800 Series Multiplatform Phones for Firmware Release 11.0(1).

For more information about an individual defect, you can access the online record for the defect by accessing the Bug Search tool and entering the Identifier. You must be a registered Cisco.com user to access this online information.

Because the defect status continually changes, the table reflects a snapshot of the defects that were resolved at the time this report was compiled. For an updated view of resolved defects, access the Bug Search tool as described in Access Cisco Bug Search .

Identifier

Headline

CSCvd30889

HTTPS XML directory service url not working

CSCvd70640

SIP Fallback: Phone does not re-register upon DNS change of outbound proxy

CSCvd86536

phone sometimes fails to resolve the sip outbound proxy dns

CSCve06933

Provisioning Fails If cname is used for provisioning server and used on the cert

CSCvd90401

Opus Payload incorrectly has clockrate at 16000 (RFC 7587)

CSCvd23143

7811 sends SIP ACK incorrectly containing \"user=phone\"

CSCvd28937

7811/7821 unregistered after upgrade to 11.0 from 10.4

CSCvd31148

PRT generated confirmation screen showing error message even when successful

CSCvd51862

Graphic issue during incoming calls.

CSCvd70401

Intermittent re-invite errors on hold/resume

CSCvd76913

Web Time is wrong during DST

CSCvd86536

phone sometimes fails to resolve the sip outbound proxy dns

CSCvd91751

Need to press softkey twice if backlight turned off

## Cisco IP Phone
	 Firmware Support Policy

For information on the support policy for phones, see http:/​/​www.cisco.com/​c/​en/​us/​support/​docs/​collaboration-endpoints/​unified-ip-phone-7900-series/​116684-technote-ipphone-00.html .

## Documentation, Service Requests, and Additional Information

For information on obtaining documentation, submitting a service request, and gathering additional information, see the monthly What’s New in Cisco Product Documentation , which also lists all new and revised Cisco technical documentation, at:

http:/​/​www.cisco.com/​c/​en/​us/​td/​docs/​general/​whatsnew/​whatsnew.html

Subscribe to the What’s New in Cisco Product Documentation as a Really Simple Syndication (RSS) feed and set content to be delivered directly to your desktop using a reader application. The RSS feeds are a free service and Cisco currently supports RSS Version 2.0.

| Cisco IP Phone | Protocol | Support Requirements |
|---|---|---|
| Cisco IP Phone 7800 Series Multiplatform Phones | SIP | BroadSoft BroadWorks 21.0 Asterisk 13.1 |

| Step 1 | Go to the following URL: http:/​/​software.cisco.com/​download/​navigator.html?mdfid=284883944&i=rm |
|---|---|
| Step 2 | Choose Cisco IP Phones 7800 Series . |
| Step 3 | Choose your phone model. |
| Step 4 | Choose Session Initiation Protocol (SIP) Software . |
| Step 5 | In the Latest Releases folder, choose 11.0(1) . |
| Step 6 | Download the file cp-78xx.11-0-1MPP-477.zip . |
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
| CSCvd30889 | HTTPS XML directory service url not working |
| CSCvd70640 | SIP Fallback: Phone does not re-register upon DNS change of outbound proxy |
| CSCvd86536 | phone sometimes fails to resolve the sip outbound proxy dns |
| CSCve06933 | Provisioning Fails If cname is used for provisioning server and used on the cert |
| CSCvd90401 | Opus Payload incorrectly has clockrate at 16000 (RFC 7587) |
| CSCvd23143 | 7811 sends SIP ACK incorrectly containing \"user=phone\" |
| CSCvd28937 | 7811/7821 unregistered after upgrade to 11.0 from 10.4 |
| CSCvd31148 | PRT generated confirmation screen showing error message even when successful |
| CSCvd51862 | Graphic issue during incoming calls. |
| CSCvd70401 | Intermittent re-invite errors on hold/resume |
| CSCvd76913 | Web Time is wrong during DST |
| CSCvd86536 | phone sometimes fails to resolve the sip outbound proxy dns |
| CSCvd91751 | Need to press softkey twice if backlight turned off |