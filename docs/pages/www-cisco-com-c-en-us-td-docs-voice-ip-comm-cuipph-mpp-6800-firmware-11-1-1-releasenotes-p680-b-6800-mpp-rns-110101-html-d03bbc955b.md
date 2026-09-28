---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cuipph-mpp-6800-firmware-11-1-1-releasenotes-p680-b-6800-mpp-rns-110101-html-d03bbc955b
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cuipph/MPP/6800/firmware/11-1-1/releasenotes/p680_b_6800-mpp-rns-110101.html
retrieved_at: 2026-08-21T23:14:50.360064+00:00
---

Cisco IP Phone 6800 Series Multiplatform Phones Release Notes for Firmware Release 11.1(1)

# Cisco IP Phone 6800 Series Multiplatform Phones Release Notes for Firmware Release 11.1(1)

### Download Options

Updated: December 20, 2017

First Published:

Last Updated:

Text Part Number:

# Cisco IP Phone 6800 Multiplatform Phones Release Notes for Firmware Release 11.1(1)

Use these release notes with the following Cisco IP Phone 6800 Series Multiplatform Phones running SIP Firmware Release 11.1(1).

Cisco IP Phone 6841 and 6851 Multiplatform Phones

The following table describes the individual phone requirements.

Phone

Support Requirements

Cisco IP Phone 6800 Series Multiplatform Phones

BroadSoft BroadWorks 21.0

Asterisk 13.1

## Related
	 Documentation

Use the following sections to
		obtain related information.

### Cisco IP Phone 6800 Series Documentation

See the publications that are specific to your language, phone model, and multiplatform firmware release. Navigate from the following Uniform Resource Locator (URL):

https:/​/​www.cisco.com/​c/​en/​us/​products/​collaboration-endpoints/​ip-phone-6800-series/​index.html

## New and Changed
	 Features

The following sections describe the features that are new or have
		changed in this release.

### Asian Language Support

The phones now support these languages:

Japanese

Korean

Chinese Simplified

Chinese Hong Kong

#### Where to Find More Information

Cisco IP Phone 6800 Multiplatform Phones Administration Guide

### Call Center Support

You can set up phones in a call center configuration. First, set up the server for the call center feature and set up call center users. Second, access each phone web page and set the Automatic Call Distribution (ACD) parameters for the phone extension.

You press AgtSignIn on the phone to sign in as a call center agent.

The call center features supported are:

Basic features

Agent sign in and sign out

Agent presence status (available, unavailable, wrap-up)

Advanced features

Call information

Hold reminder

Disposition code

Trace

Emergency escalation

Queue status notification

Hoteling event

#### Where to Find More Information

Cisco IP Phone 6800 Series Multiplatform Phones Administration Guide

Cisco IP Phone 6800 Series Multiplatform Phones User Guide

### Configuration Report to Provisioning Server

You can configure the phone to report its current configuration to the server. After you configure, the server issues a SIP NOTIFY message to the phone to report the configuration. You can configure this feature from the phone web page.

#### Where to Find More Information

Cisco IP Phone 6800 Series Multiplatform Phones Administration Guide

### Distinctive Ringtone

You can set a distinctive ringtone for an extension. Distinctive ringtone allows the phone to avoid playing default ringtone always and enables the receiver to identify the type of the incoming call on the extension. Distinctive ringtone depends on the SIP Alert-Info message that the server sends to the phone. When the phone receives a correct SIP Alert-INFO message, it plays the specified ringtone. Otherwise, the phone plays the default ringtone.

#### Where to Find More Information

Cisco IP Phone 6800 Series Multiplatform Phones Administration Guide

### Download Status with Phone Web Page

You can view different download status in the phone web page from Info > Download Status :

Firmware Upgrade Status: Displays the upgrade status (failed or succeeded) with reason for the same.

Provisioning Status: Displays the upgrade status (resync) of the phone.

Custom CA Status: Indicates whether provisioning using a custom CA succeeded or failed.

#### Where to Find More Information

Cisco IP Phone 6800 Series Multiplatform Phones Administration Guide

### Factory Reset Button on the Phone Web Page

You can press a button on the phone web page to perform a factory reset on an inactive phone. If the phone is not idle, you can't reset the phone.

#### Where to Find More Information

Cisco IP Phone 6800 Series Multiplatform Phones Administration Guide

### Gigabit Ethernet Support

You can set the phones to use 1000 Base-T for the PC port and SW port.

#### Where to Find More Information

Cisco IP Phone 6800 Multiplatform Phones Administration Guide

### IPv6 Support

The Cisco IP Phones support IPv6 addressing. A valid IPv6 address is 128 bits in length that includes the subnet prefix. The subnet prefix length is a decimal value from 1-128. IPv6 has support for NTP and SIP. IPv6 addresses must be in one of the following formats:

Eight sets of four hexadecimal digits separated by colons, where the left-most digits represent the highest-order bits. Any leading or trailing zeros in each group may be omitted. An example of an IPv6 address is 2009:10:74:10:6969:ad71:93c5:2fca.

Compressed format to collapse a single run of consecutive zero groups into a single group represented by a double colon. Note that this can only be done once in an address. An example of compressed format IPv6 address is fe80::21b:54ff:feb0:4f91.

Phone features that do not support IPv6 are:

Group Paging

TR069

LDAP

STUN

#### Where to Find More Information

Cisco IP Phone 6800 Multiplatform Phones Administration Guide

### Power Save Support

The Cisco IP Phone 6800 Multiplatform Phones support power save. When the phone is in power save, the phone screen is dark and the Select button is lit white.

#### Where to Find More Information

Cisco IP Phone 6800 Multiplatform Phones Administration Guide

Cisco IP Phone 6800 Multiplatform Phones User Guide

### Presence

You can set up your phones so that users can view the presence status of their contacts. You need to set up the XMPP service on the Broadsoft server, and enable access to the XMPP server in the Phone tab of the phone web page.

Users need to access Broadsoft's UC-One Communicator to set up their instant message and presence (IM&P) contact lists. After they have a list of contacts, they press Contacts and access the IM&P entry.

#### Where to Find More Information

Cisco IP Phone 6800 Series Multiplatform Phones Administration Guide

Cisco IP Phone 6800 Series Multiplatform Phones User Guide

### Record a Call

You can enable phones to record calls. You can set up the phones to always record calls or to let the user deteremine when a call needs to be recorded.

Users press a button on the phone to record the call.

#### Where to Find More Information

Cisco IP Phone 6800 Series Multiplatform Phones Administration Guide

Cisco IP Phone 6800 Series Multiplatform Phones User Guide

### Phone Screen Contrast

You can adjust the phone screen brightness and contrast on the screen.

To change the brightness, press Applications and select User preferences > Screen preferences > Display contrast . You press the Navigation cluster up or down to increase or decrease the brightness.

#### Where to Find More Information

Cisco IP Phone 6800 Series Multiplatform Phones User Guide

### Secure Calls on Extensions

You can configure phones to only allow secure calls. Use the phone web page to configure the extension as secure.

When a user wants to place a call on a secure extension, they can only place calls to secure extensions. Calls to nonsecure extensions are blocked. When a call is secure, the lock icon is displayed on the phone screen.

Where to Find More Information

#### Where to Find More Information

### Wideband Handset Support

The Cisco IP Phone 6800 Series Multiplatform Phones now support a wideband handset. The wideband handset is an orderable accessory for the phone.

The user unplugs the standard narrowband handset, plugs in the wideband handset, and enables wideband support in the phone web page.

## Installation

### Install the Firmware

The Cisco IP Phone 6800 Series Multiplatform Phones supports a single image upgrade by TFTP, HTTP, or HTTPS with a URL.

After the firmware upgrade completes, the phone reboots automatically.

https:/​/​software.cisco.com/​download/​navigator.html?mdfid=286318380&i=rm

Use the URL format: <protocol>://<serv_ip[:port]>/<filepath>/sipxxx.loads .

You can also upgrade the third-party call control by using a URL in the web browser:

<protocol>://<serv_ip[:port]>/<filepath>/sipxxx.loads

Example

http://10.80.10.115/firmware/sip68xx.11-1-1MPP-897.loads

Use the *.loads file in the URL. The *.zip file contains other files.

## Limitations and Restrictions

### Phone Behavior During Times of Network Congestion

Anything that degrades network performance can affect phone voice and video quality, and in some cases, can cause a call to drop. Sources of network degradation can include, but are not limited to, the following activities:

Administrative tasks, such as an internal port scan or security scan

Attacks that occur on your network, such as a Denial of Service attack

### Caller Identification and Other Phone Functions

Caller identification or other phone functions have not been verified with third-party applications for the visually or hearing impaired.

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

The following list contains the severity 1, 2, and 3 defects that are open for the Cisco IP Phone 6800 Series Multiplatform Phones that use Firmware Release 11.1(1).

For more information about an individual defect, you can access the online history for the defect by accessing the Bug Search tool and entering the Identifier. You must be a registered Cisco.com user to access this defect information.

Because the defect status continually changes, the list reflects a snapshot of the defects that were open at the time this report was compiled. For an updated view of the open defects or to view specific bugs, access the Bug Search Toolkit as described in the Access Cisco Bug Search .

CSCvg42260 Sometimes packet capture may not be terminated.

CSCvh02982 68/78xx: Initiate a Paging call during upgrade, and the upgrade will fail after the call is terminated.

CSCvh10338 68/78xx: If NOTIFY content length is large, phone responds slowly when you enabled share line and line status.

### Resolved Caveats

The following list contains the severity 1, 2, and 3 defects that are resolved for the Cisco IP Phone 6800 Series Multiplatform Phones that use Firmware Release 11.1(1).

For more information about an individual defect, you can access the online history for the defect by accessing the Bug Search tool and entering the Identifier. You must be a registered Cisco.com user to access this defect information.

Because a defect status continually changes, the list reflects a snapshot of the defects that were resolved at the time this report was compiled. For an updated view of the resolved defects or to view specific bugs, access the Bug Search Toolkit as described in the Access Cisco Bug Search .

CSCvf64140 68xx: Firmware upgrade can't continue after plug out or in network cable while DUT firmware upgrade is in progress.

CSCvf68983 68xx The DUT backlight doesn't work.

CSCvf82957 68xx: Hardcode PC Port, the switch/port port config doesn't have the "1000M full" option.

CSCvf90731 68xx: Wrong upgrade status displayed in the phone web page.

CSCvf92265 68xx: WEB GUI current Time is 1 hour earlier if manual setting time on DUT LCD-GUI.

CSCvf99407 68xx: HTTP authentication fail after changing user id.

CSCvg04781 68xx [IOT]Phone can't upgrade to new firmware with BS IOP1 server.

CSCvg14787 [68xx]The DUT can register when network cable pulls in the PC port.

CSCvg32215 The speaker volume will get bigger after audio path switch.

CSCvg35997 Can configure a minimum rtp-port bigger than maximum rpt-port in web GUI.

## Cisco IP Phone
	 Firmware Support Policy

For information on the support policy for phones, see http:/​/​www.cisco.com/​c/​en/​us/​support/​docs/​collaboration-endpoints/​unified-ip-phone-7900-series/​116684-technote-ipphone-00.html .

## Documentation, Service Requests, and Additional Information

For information on obtaining documentation, submitting a service request, and gathering additional information, see the monthly What’s New in Cisco Product Documentation , which also lists all new and revised Cisco technical documentation, at:

http:/​/​www.cisco.com/​c/​en/​us/​td/​docs/​general/​whatsnew/​whatsnew.html

Subscribe to the What’s New in Cisco Product Documentation as a Really Simple Syndication (RSS) feed and set content to be delivered directly to your desktop using a reader application. The RSS feeds are a free service and Cisco currently supports RSS Version 2.0.

| Phone | Support Requirements |
|---|---|
| Cisco IP Phone 6800 Series Multiplatform Phones | BroadSoft BroadWorks 21.0 Asterisk 13.1 |

| Step 1 | Click the following URL: https:/​/​software.cisco.com/​download/​navigator.html?mdfid=286318380&i=rm |
|---|---|
| Step 2 | Select IP Phones 6800 Series with Multiplatform Firmware in the middle pane. |
| Step 3 | Select your phone model in the right pane. |
| Step 4 | Select Multiplatform Firmware . |
| Step 5 | Under All Releases > MPPv11 , select the 11.1.1 folder. |
| Step 6 | (Optional) Place your mouse pointer on the filename to display the file details and checksum values. |
| Step 7 | Download the file cmterm-68xx.11-1-1MPP-897_REL.zip . |
| Step 8 | Click Accept License Agreement to accept the software license. |
| Step 9 | Unzip the files. |
| Step 10 | Put the files in the TFTP, HTTP, or HTTPS download folder. |
| Step 11 | Configure the Upgrade Rule on the Provisioning tab in the web page with the valid URL. Use the URL format: <protocol>://<serv_ip[:port]>/<filepath>/sipxxx.loads . You can also upgrade the third-party call control by using a URL in the web browser: <protocol>://<serv_ip[:port]>/<filepath>/sipxxx.loads Example http://10.80.10.115/firmware/sip68xx.11-1-1MPP-897.loads Note Use the *.loads file in the URL. The *.zip file contains other files. | Note | Use the *.loads file in the URL. The *.zip file contains other files. |
| Note | Use the *.loads file in the URL. The *.zip file contains other files. |

| Note | Use the *.loads file in the URL. The *.zip file contains other files. |
|---|---|

| Step 1 | To access Cisco Bug Search, go to: https:/​/​tools.cisco.com/​bugsearch |
|---|---|
| Step 2 | Log in with your
			 Cisco.com user ID and password. |
| Step 3 | To look for
			 information about a specific problem, enter the bug ID number in the Search for
			 field, then press Enter . |