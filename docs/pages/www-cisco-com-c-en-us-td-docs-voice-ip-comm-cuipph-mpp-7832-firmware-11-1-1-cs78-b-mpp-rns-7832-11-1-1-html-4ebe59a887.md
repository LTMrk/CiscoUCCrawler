---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cuipph-mpp-7832-firmware-11-1-1-cs78-b-mpp-rns-7832-11-1-1-html-4ebe59a887
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cuipph/MPP/7832/firmware/11-1-1/cs78_b_mpp-rns-7832-11_1_1.html
retrieved_at: 2026-08-21T23:18:40.479904+00:00
---

Cisco IP Conference Phone 7832 Multiplatform Phones Release Notes for Firmware Release 11.1(1)

# Cisco IP Conference Phone 7832 Multiplatform Phones Release Notes for Firmware Release 11.1(1)

### Download Options

Updated: January 19, 2018

First Published:

Last Updated:

Text Part Number:

# Cisco IP Conference Phone 7832 Multiplatform Phones Release Notes for Firmware Release 11.1(1)

Use these release notes with the Cisco IP Conference Phone 7832 Multiplatform Phones running SIP Firmware Release 11.1(1).

The following table describes the individual phone requirements.

Phone

Support Requirements

Cisco IP Conference Phone 7832 Multiplatform Phones

BroadSoft BroadWorks 21.0

Asterisk 13.1

## Related
	 Documentation

Use the following sections to
		obtain related information.

### Cisco IP Conference Phone 7832 Documentation

Refer to publications that are specific to your language and call control system. Navigate from the following documentation URL:

https:/​/​www.cisco.com/​c/​en/​us/​products/​collaboration-endpoints/​unified-ip-phone-7800-series/​index.html

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

Cisco IP Conference Phone 7832 Multiplatform Phones Administration Guide

### Call Center Support

You can set up phones in a call center configuration. First, set up the server for the call center feature and set up call center users. Second, access each phone web page and set the Automatic Call Distribution (ACD) parameters for the phone extension.

Additionally, you also need to enable the programmable softkeys (PSK) and add the ACD softkeys to the softkey list for the Cisco IP Conference Phone 7832 Multiplatform Phones . See the Configuring Programmable Softkeys section in the Administration Guide.

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

Cisco IP Conference Phone 7832 Multiplatform Phones Administration Guide

Cisco IP Conference Phone 7832 Multiplatform Phones User Guide

### Configuration Report to Provisioning Server

You can configure the phone to report its current configuration to the server. After you configure, the server issues a SIP NOTIFY message to the phone to report the configuration. You can configure this feature from the phone web page.

#### Where to Find More Information

Cisco IP Conference Phone 7832 Multiplatform Phones Administration Guide

### Distinctive Ringtone

You can set a distinctive ringtone for an extension. Distinctive ringtone allows the phone to avoid playing default ringtone always and enables the receiver to identify the type of the incoming call on the extension. Distinctive ringtone depends on the SIP Alert-Info message that the server sends to the phone. When the phone receives a correct SIP Alert-INFO message, it plays the specified ringtone. Otherwise, the phone plays the default ringtone.

#### Where to Find More Information

Cisco IP Conference Phone 7832 Multiplatform Phones Administration Guide

### Download Status with Phone Web Page

You can view different download status in the phone web page from Info > Download Status :

Firmware Upgrade Status: Displays the upgrade status (failed or succeeded) with reason for the same.

Provisioning Status: Displays the upgrade status (resync) of the phone.

Custom CA Status: Indicates whether provisioning using a custom CA succeeded or failed.

#### Where to Find More Information

Cisco IP Conference Phone 7832 Multiplatform Phones Administration Guide

### Factory Reset Button on the Phone Web Page

You can press a button on the phone web page to perform a factory reset on an inactive phone. If the phone is not idle, you can't reset the phone.

#### Where to Find More Information

Cisco IP Conference Phone 7832 Multiplatform Phones Administration Guide

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

Cisco IP Conference Phone 7832 Multiplatform Phones Administration Guide

### Presence

You can set up your phones so that users can view the presence status of their contacts. You need to set up the XMPP service on the Broadsoft server, and enable access to the XMPP server in the Phone tab of the phone web page.

Users need to access Broadsoft's UC-One Communicator to set up their instant message and presence (IM&P) contact lists. After they have a list of contacts, they press Contacts and access the IM&P entry.

#### Where to Find More Information

Cisco IP Conference Phone 7832 Multiplatform Phones Administration Guide

Cisco IP Conference Phone 7832 Multiplatform Phones User Guide

### Phone Screen Contrast

You can adjust the phone screen brightness and contrast on the screen.

To change the brightness, press Settings and select User preferences > Screen preferences > Display contrast . You press the Navigation bar up or down to increase or decrease the brightness.

#### Where to Find More Information

Cisco IP Conference Phone 7832 Multiplatform Phones User Guide

### Secure Calls on Extensions

You can configure phones to only allow secure calls. Use the phone web page to configure the extension as secure.

When a user wants to place a call on a secure extension, they can only place calls to secure extensions. Calls to nonsecure extensions are blocked. When a call is secure, the lock icon is displayed on the phone screen.

#### Where to Find More Information

Cisco IP Conference Phone 7832 Multiplatform Phones Administration Guide

Cisco IP Conference Phone 7832 Multiplatform Phones User Guide

## Installation

### Upgrade the Firmware

The Cisco IP Conference Phone 7832 Multiplatform Phones support a single image upgrade using TFTP, HTTP, or HTTPS protocols with a URL.

After the firmware upgrade completes, the phone reboots automatically.

https:/​/​software.cisco.com/​download/​navigator.html?mdfid=286311381&i=rm

Use the URL format– <protocol>://<serv_ip[:port]>/<filepath>/sipxxx.loads

You can also upgrade the third-party call control by using a URL in a web browser– <protocol>://<serv_ip[:port]>/<filepath>/sipxxx.loads

Example

http://10.64.10.223/firmware/sip7832.11-1-1MPP-897dev.loads

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

The following list contains the severity 1, 2, and 3 defects that are open for the Cisco IP Conference Phone 7832 Multiplatform Phones that use Firmware Release 11.1(1).

For more information about an individual defect, you can access the online history for the defect by accessing the Bug Search tool and entering the Identifier. You must be a registered Cisco.com user to access this defect information.

Because the defect status continually changes, the list reflects a snapshot of the defects that were open at the time this report was compiled. For an updated view of the open defects or to view the specific bugs, access the Bug Search Toolkit as described in the Access Cisco Bug Search .

CSCvh13875 7832 phone: Agent-associated multiple call center only shows one call center's Queue Status.

### Resolved Caveats

The following list contains the severity 1, 2, and 3 defects that are resolved for the Cisco IP Conference Phone 7832 Multiplatform Phones that use Firmware Release 11.1(1).

For more information about an individual defect, you can access the online history for the defect by accessing the Bug Search tool and entering the Identifier. You must be a registered Cisco.com user to access this defect information.

Because the defect status continually changes, the list reflects a snapshot of the defects that were resolved at the time this report was compiled. For an updated view of the resolved defects or to view specific bugs, access the Bug Search Toolkit as described in the Access Cisco Bug Search .

CSCvg50696 Phone can get into a state that requires hard factory reset.

## Cisco IP Phone
	 Firmware Support Policy

For information on the support policy for phones, see http:/​/​www.cisco.com/​c/​en/​us/​support/​docs/​collaboration-endpoints/​unified-ip-phone-7900-series/​116684-technote-ipphone-00.html .

## Documentation, Service Requests, and Additional Information

For information on obtaining documentation, submitting a service request, and gathering additional information, see the monthly What’s New in Cisco Product Documentation , which also lists all new and revised Cisco technical documentation, at:

http:/​/​www.cisco.com/​c/​en/​us/​td/​docs/​general/​whatsnew/​whatsnew.html

Subscribe to the What’s New in Cisco Product Documentation as a Really Simple Syndication (RSS) feed and set content to be delivered directly to your desktop using a reader application. The RSS feeds are a free service and Cisco currently supports RSS Version 2.0.

| Phone | Support Requirements |
|---|---|
| Cisco IP Conference Phone 7832 Multiplatform Phones | BroadSoft BroadWorks 21.0 Asterisk 13.1 |

| Note | Additionally, you also need to enable the programmable softkeys (PSK) and add the ACD softkeys to the softkey list for the Cisco IP Conference Phone 7832 Multiplatform Phones . See the Configuring Programmable Softkeys section in the Administration Guide. |
|---|---|

| Step 1 | Click the following URL: https:/​/​software.cisco.com/​download/​navigator.html?mdfid=286311381&i=rm |
|---|---|
| Step 2 | Select IP Phone 7800 Series with Multiplatform Firmware in the center pane. |
| Step 3 | Select IP Conference Phone 7832 with Multiplatform Firmware in the right pane. |
| Step 4 | Select Multiplatform Firmware software type. |
| Step 5 | Under All Releases > MPP v11 , select the 11.1.1 folder. |
| Step 6 | (Optional) Place your mouse pointer on the filename to display the file details and checksum values. |
| Step 7 | Download the cmterm-7832.11-1-1MPP-897_REL.zip file. |
| Step 8 | Click Accept License Agreement when you accept the software license. |
| Step 9 | Unzip the firmware files. |
| Step 10 | Put the files in the TFTP, HTTP, or HTTPS download directory. |
| Step 11 | Configure the Upgrade Rule on the Provisioning tab in the web page with the valid URL. Use the URL format– <protocol>://<serv_ip[:port]>/<filepath>/sipxxx.loads You can also upgrade the third-party call control by using a URL in a web browser– <protocol>://<serv_ip[:port]>/<filepath>/sipxxx.loads Example http://10.64.10.223/firmware/sip7832.11-1-1MPP-897dev.loads Note Use the *.loads file in the URL. The *.zip file contains other files. | Note | Use the *.loads file in the URL. The *.zip file contains other files. |
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