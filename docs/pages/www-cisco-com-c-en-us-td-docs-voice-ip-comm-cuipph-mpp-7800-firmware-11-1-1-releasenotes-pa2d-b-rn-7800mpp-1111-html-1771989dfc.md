---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cuipph-mpp-7800-firmware-11-1-1-releasenotes-pa2d-b-rn-7800mpp-1111-html-1771989dfc
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cuipph/MPP/7800/firmware/11-1-1/releasenotes/pa2d_b_rn-7800mpp-1111.html
retrieved_at: 2026-08-21T23:20:28.928759+00:00
---

Cisco IP Phone 7800 Series Multiplatform Phones Release Notes for Firmware Release 11.1(1)

# Cisco IP Phone 7800 Series Multiplatform Phones Release Notes for Firmware Release 11.1(1)

### Download Options

Updated: October 17, 2017

First Published:

Last Updated:

Text Part Number:

# Cisco IP Phone 7800 Series Multiplatform Phones Release Notes for Firmware Release 11.1(1)

Use these release notes with the following Cisco IP Phone 7800 Series Multiplatform Phones running SIP Firmware Release 11.1(1).

Cisco IP Phone 7811 Multiplatform Phones

Cisco IP Phone 7821 Multiplatform Phones

Cisco IP Phone 7841 Multiplatform Phones

Cisco IP Phone 7861 Multiplatform Phones

The following table describes the individual phone requirements.

Phone

Support Requirements

Cisco IP Phone 7800 Series Multiplatform Phones

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

### Asian Language Support

The phones now support these languages:

Japanese

Korean

Chinese Simplified

Chinese Hong Kong

#### Where to Find More Information

Cisco IP Phone 7800 Series Multiplatform Phones Administration Guide

### Configuration Report to Provisioning Server

You can configure the phone to report its current configuration to the server. After you configure, the server issues a SIP NOTIFY message to the phone to report the configuration. You can configure this feature from the phone web page.

#### Where to Find More Information

Cisco IP Phone 7800 Series Multiplatform Phones Administration Guide

### Distinctive Ringtone

You can set a distinctive ringtone for an extension. Distinctive ringtone allows the phone to avoid playing default ringtone always and enables the receiver to identify the type of the incoming call on the extension. Distinctive ringtone depends on the SIP Alert-Info message that the server sends to the phone. When the phone receives a correct SIP Alert-INFO message, it plays the specified ringtone. Otherwise, the phone plays the default ringtone.

#### Where to Find More Information

Cisco IP Phone 7800 Series Multiplatform Phones Administration Guide

### Download Status with Phone Web Page

You can view different download status in the phone web page from Info > Download Status :

Firmware Upgrade Status: Displays the upgrade status (failed or succeeded) with reason for the same.

Provisioning Status: Displays the upgrade status (resync) of the phone.

Custom CA Status: Indicates whether provisioning using a custom CA succeeded or failed.

#### Where to Find More Information

Cisco IP Phone 7800 Series Multiplatform Phones Administration Guide

### Factory Reset Button on the Phone Web Page

You can press a button on the phone web page to perform a factory reset on an inactive phone. If the phone is not idle, you can't reset the phone.

#### Where to Find More Information

Cisco IP Phone 7800 Series Multiplatform Phones Administration Guide

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

Cisco IP Phone 7800 Series Multiplatform Phones Administration Guide

### Presence

You can set up your phones so that users can view the presence status of their contacts. You need to set up the XMPP service on the Broadsoft server, and enable access to the XMPP server in the Phone tab of the phone web page.

Users need to access Broadsoft's UC-One Communicator to set up their instant message and presence (IM&P) contact lists. After they have a list of contacts, they press Contacts and access the IM&P entry.

#### Where to Find More Information

Cisco IP Phone 7800 Series Multiplatform Phones Administration Guide

Cisco IP Phone 7800 Series Multiplatform Phones User Guide

### Phone Screen Contrast

You can adjust the phone screen brightness and contrast on the screen.

To change the brightness, press Applications and select User preferences > Screen preferences > Display contrast . You press the Navigation cluster up or down to increase or decrease the brightness.

#### Where to Find More Information

Cisco IP Phone 7800 Series Multiplatform Phones User Guide

### Secure Calls on Extensions

You can configure phones to only allow secure calls. Use the phone web page to configure the extension as secure.

When a user wants to place a call on a secure extension, they can only place calls to secure extensions. Calls to nonsecure extensions are blocked. When a call is secure, the lock icon is displayed on the phone screen.

#### Where to Find More Information

Cisco IP Phone 7800 Series Multiplatform Phones Administration Guide

Cisco IP Phone 7800 Series Multiplatform Phones User Guide

## Installation

### Upgrade Firmware

The Cisco IP Phone 7800 Series Multiplatform Phones support a single image upgrade by TFTP, HTTP, or HTTPS.

After the firmware upgrade completes, the phone reboots automatically.

http:/​/​software.cisco.com/​download/​navigator.html?mdfid=284883944&i=rm

Use the URL format– <protocol>://<serv_ip[:port]>/<filepath>/sipxxx.loads

The third-party call control can also upgrade via a URL in the web browser:

<protocol>://<serv_ip[:port]>/<filepath>/sipxxx.loads

Here is an example,

http://10.73.10.223/firmware/sip78xx.11-1-1MPP-897.loads

Use the *.loads file in the URL. The *.zip file contains other files.

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

The following list contains the severity 1, 2, and 3 defects that are open for the Cisco IP Phone 7800 Series Multiplatform Phones that use Firmware Release 11.1(1).

For more information about an individual defect, you can access the online history for the defect by accessing the Bug Search tool and entering the Identifier. You must be a registered Cisco.com user to access this defect information.

Because the defect status continually changes, the list reflects a snapshot of the defects that were open at the time this report was compiled. For an updated view of the open defects or to view specific bugs, access the Bug Search Toolkit as described in the Access Cisco Bug Search .

CSCvb50513 MPP phone having an issue upgrading to Enterprise firmware.

CSCvc85704 MPP: CFWD all De-act star code does not work.

CSCvc94798 7800-MPP: BS BLF List disappearing when receiving call.

CSCvd27675 MPP: Play ringtone failed and phone cannot answer or place a call.

CSCvd46241 MPP: Secondary DNS on a phone's web page has a nonexistent IP address.

CSCvg09851 Sometimes duplicated IPv6 address warning messages are not able to be shown on LCD GUI.

CSCvg69428 Customer is reporting random reboots.

CSCvh13270 78xx: Display is showing two calls during conference.

CSCvh19503 PC port mirror does not work on 78xx 11-1-1MPP897. Loads with switch voice VLAN configured.

### Resolved Caveats

The following list contains the severity 1, 2, and 3 defects that are resolved for the Cisco IP Phone 7800 Series Multiplatform Phones that use Firmware Release 11.1(1).

For more information about an individual defect, you can access the online history for the defect by accessing the Bug Search tool and entering the Identifier. You must be a registered Cisco.com user to access this defect information.

Because the defect status continually changes, the list reflects a snapshot of the defects that were resolved at the time this report was compiled. For an updated view of the resolved defects or to view the specific bugs, access the Bug Search Toolkit as described in the Access Cisco Bug Search .

CSCvg50696 Phone can get into a state that requires hard factory reset.

CSCva83207 EM Sign-in soft key not displayed after factory reset and EM enabled.

CSCvb55751 7861 sometimes needs reboot for pushed config to take effect.

CSCvb61321 Phones appear to ignore the 120 seconds timer in the 200 OK.

CSCvb69587 MPP-Generic-78xx: Spelling is wrong for directory in LCD Idle screen.

CSCvb71520 7811 sends SIP ACK incorrectly containing "user=phone".

CSCvb83904 MPP-78XX - phone's switch does not change CoS value after extended CoS changes.

CSCvb85886 MPP-78xx: Press BLF SD PLK three times, phone still play tone while idle.

CSCvc24856 MPP-78xx: Cisco IP Phone Menu display error: displays part of the item number.

CSCvc27600 Auth-resync not working.

CSCvc78710 MPP: Phone reboots periodically due to provision even phone config file not changed

CSCvc80575 MPP: agent not sign out from BroadSoft server after disable ACD

CSCvc97003 MPP-78xx: Changes in NTP time during a call could cause abnormal values in rtcp reports.

CSCvd09730 MPP: User can factory reset phone without password.

CSCvd15759 MPP: phone sends wrong DNS query to TFTP server.

CSCvd27898 MPP: DN not register after upgrade.

CSCvd42430 MPP: backtrace at spr_voip.

CSCvd70401 Intermittent re-invite errors on hold/resume.

CSCvd70446 Phone does not re-register upon DNS change of outbound proxy.

CSCvd90401 Opus Payload incorrectly has a clock rate at 16000 (RFC 7587)

CSCve06933 Provisioning Fails: If cname is used for provisioning server and used on the cert

CSCve89301 Phone rebooted when call came in from webex

CSCve89514 After adjusting call volume mid call, dial pad keys become unusable

CSCvf82885 Lack of Connectivity: REGISTER with a Call-ID incomplete.

CSCvf96511 ISSUE WITH "DO NOT DISTURB" AND "CALL FORWARD ALL" FEATURES.

CSCvf99303 78xx-MPP: XML Corp Directory doesn't allow you to dial out.

CSCvg22226 Evaluation of MPP-sp-dspg for Dnsmasq October 2017 vulnerabilities

CSCvg30255 Under CPE with QMON: After any incoming/outgoing call

CSCvg30274 BLF led randomly not aligned (blinking orange) because device didn't

CSCvg61103 MPP phones are now using up the bandwidth on their network

## Cisco IP Phone
	 Firmware Support Policy

For information on the support policy for phones, see http:/​/​www.cisco.com/​c/​en/​us/​support/​docs/​collaboration-endpoints/​unified-ip-phone-7900-series/​116684-technote-ipphone-00.html .

## Documentation, Service Requests, and Additional Information

For information on obtaining documentation, submitting a service request, and gathering additional information, see the monthly What’s New in Cisco Product Documentation , which also lists all new and revised Cisco technical documentation, at:

http:/​/​www.cisco.com/​c/​en/​us/​td/​docs/​general/​whatsnew/​whatsnew.html

Subscribe to the What’s New in Cisco Product Documentation as a Really Simple Syndication (RSS) feed and set content to be delivered directly to your desktop using a reader application. The RSS feeds are a free service and Cisco currently supports RSS Version 2.0.

| Phone | Support Requirements |
|---|---|
| Cisco IP Phone 7800 Series Multiplatform Phones | BroadSoft BroadWorks 21.0 Asterisk 13.1 |

| Step 1 | Click the following URL: http:/​/​software.cisco.com/​download/​navigator.html?mdfid=284883944&i=rm |
|---|---|
| Step 2 | Select the IP Phones with Multiplatform Firmware in the middle pane. |
| Step 3 | Select the IP Phones 7800 Series With Multiplatform Firmware in the right pane. |
| Step 4 | Select your phone model in the right pane. |
| Step 5 | Select Multiplatform Firmware . |
| Step 6 | In the All Releases > MPPv11 folder, select 11.1.1 . |
| Step 7 | (Optional) Place your mouse pointer on the filename to display the file details and checksum values. |
| Step 8 | Download the file cmterm-78xx.11-1-1MPP-897_REL.zip . |
| Step 9 | Click Accept License Agreement when you accept the software license. |
| Step 10 | Unzip the files. |
| Step 11 | Put the files in the TFTP, HTTP, or HTTPS download directory. |
| Step 12 | Configure the Upgrade Rule on the Provisioning tab in the web page with the valid URL. Use the URL format– <protocol>://<serv_ip[:port]>/<filepath>/sipxxx.loads The third-party call control can also upgrade via a URL in the web browser: <protocol>://<serv_ip[:port]>/<filepath>/sipxxx.loads Here is an example, http://10.73.10.223/firmware/sip78xx.11-1-1MPP-897.loads Note Use the *.loads file in the URL. The *.zip file contains other files. | Note | Use the *.loads file in the URL. The *.zip file contains other files. |
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