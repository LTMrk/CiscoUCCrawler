---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cuipph-mpp-8800-firmware-11-1-1-releasenotes-p881-b-release-notes-for-mpp-11-ebc12721dd
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cuipph/MPP/8800/firmware/11-1-1/releasenotes/p881_b_release-notes-for-mpp-1111.html
retrieved_at: 2026-08-21T13:45:26.336024+00:00
---

Cisco IP Phone 8800 Series Multiplatform Phones Release Notes for Firmware Release 11.1(1)

# Cisco IP Phone 8800 Series Multiplatform Phones Release Notes for Firmware Release 11.1(1)

### Download Options

Updated: December 20, 2017

First Published:

Last Updated:

Text Part Number:

# Cisco IP Phone 8800 Series Multiplatform Phones Release Notes for Firmware Release 11.1(1)

Use these release notes with the following Cisco IP Phone 8800 Series Multiplatform Phones running SIP Firmware Release 11.1(1).

Cisco IP Phone 8811, 8841, 8851, and 8861 Multiplatform Phones

Cisco IP Phone 8845 and 8865 Multiplatform Phones

The following table describes the individual phone requirements.

Phone

Support Requirements

Cisco IP Phone 8800 Series Multiplatform Phones

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

Cisco IP Phone 8800 Series Multiplatform Phones Administration Guide

### Cisco IP Phone 8845 and 8865 Multiplatform Phones Support

This release introduces support for the Cisco IP Phone 8845 and 8865 Multiplatform Phones. These phones support video calls with picture-in-picture (PiP). You can now make video calls and use all the standard features such as hold, mute, or transfer while on the video call. In addition, the phones support telephony feature integration with your personal mobile devices using Cisco Intelligent Proximity for Mobile Voice for hands-free and mobile Bluetooth.

The Cisco IP Phone 8845 and 8865 Multiplatform Phones also allows you to:

Adjust camera exposure to change the brightness of the transmitted video

Set up a fixed bandwidth to balance video issues

Configure a secure extension to only accept secure calls

Configure video codec

Disable or hide all video settings on the phone

Your user can close the shutter to stop video transmission, adjust camera exposure, and control video bandwidth.

#### Where to Find More Information

Cisco IP Phone 8800 Series Multiplatform Phones User Guide

Cisco IP Phone 8800 Series Multiplatform Phones Administration Guide

### Screen Brightness Adjustment Slider

You can adjust the phone screen brightness with a brightness slider on the screen.

To change the brightness, press Applications and select User preferences > Screen preferences > Display brightness . You press the Navigation cluster right or left to increase or decrease the brightness.

#### Where to Find More Information

Cisco IP Phone 8800 Series Multiplatform Phones User Guide

### Secure Calls on Extensions

You can configure phones to only allow secure calls. Use the phone web page to configure the extension as secure.

When a user wants to place a call on a secure extension, they can only place calls to secure extensions. Calls to nonsecure extensions are blocked. When a call is secure, the lock icon is displayed on the phone screen.

#### Where to Find More Information

Cisco IP Phone 8800 Series Multiplatform Phones Administration Guide

Cisco IP Phone 8800 Series Multiplatform Phones User Guide

### Factory Reset Button on the Phone Web Page

You can press a button on the phone web page to perform a factory reset on an inactive phone. If the phone is not idle, you can't reset the phone.

#### Where to Find More Information

Cisco IP Phone 8800 Series Multiplatform Phones Administration Guide

### Presence

You can set up your phones so that users can view the presence status of their contacts. You need to set up the XMPP service on the Broadsoft server, and enable access to the XMPP server in the Phone tab of the phone web page.

Users need to access Broadsoft's UC-One Communicator to set up their instant message and presence (IM&P) contact lists. After they have a list of contacts, they press Contacts and access the IM&P entry.

#### Where to Find More Information

Cisco IP Phone 8800 Series Multiplatform Phones Administration Guide

Cisco IP Phone 8800 Series Multiplatform Phones User Guide

### Asian Language Support

The phones now support these languages:

Japanese

Korean

Chinese Simplified

Chinese Hong Kong

#### Where to Find More Information

Cisco IP Phone 8800 Series Multiplatform Phones Administration Guide

### Configuration Report to Provisioning Server

You can configure the phone to report its current configuration to the server. After you configure, the server issues a SIP NOTIFY message to the phone to report the configuration. You can configure this feature from the phone web page.

#### Where to Find More Information

Cisco IP Phone 8800 Series Multiplatform Phones Administration Guide

### Distinctive Ringtone

You can set a distinctive ringtone for an extension. Distinctive ringtone allows the phone to avoid playing default ringtone always and enables the receiver to identify the type of the incoming call on the extension. Distinctive ringtone depends on the SIP Alert-Info message that the server sends to the phone. When the phone receives a correct SIP Alert-INFO message, it plays the specified ringtone. Otherwise, the phone plays the default ringtone.

#### Where to Find More Information

Cisco IP Phone 8800 Series Multiplatform Phones Administration Guide

### Download Status with Phone Web Page

You can view different download status in the phone web page from Info > Download Status :

Firmware Upgrade Status: Displays the upgrade status (failed or succeeded) with reason for the same.

Provisioning Status: Displays the upgrade status (resync) of the phone.

Custom CA Status: Indicates whether provisioning using a custom CA succeeded or failed.

#### Where to Find More Information

Cisco IP Phone 8800 Series Multiplatform Phones Administration Guide

## Installation

### Upgrade Firmware

The Cisco IP Phone 8800 Series Multiplatform Phones support a single image upgrade using TFTP, HTTP, or HTTPS.

After the firmware upgrade completes, the phone reboots automatically.

https:/​/​software.cisco.com/​download/​navigator.html?mdfid=286311381&i=rm

For the 8811, 8841, 8851, and 8861– cmterm-88xx.11-1-1MPP-897_REL.zip

For the 8845 and 8865— cp-8845_65.11-1-1MSR1-1_REL.zip

<protocol>://<serv_ip[port]>/filepath/sipxxx.loads

You can also upgrade the third-party call control by using a URL in the web browser–

<protocol>://<serv_ip[port]>/filepath/sipxxx.loads

Here is an example,

Example for 8811, 8841, 8851, and 8861

https://10.64.10.223/firmware/sip88xx.11-1-1MPP-897.loads

Example for 8845 and 8865

https://10.64.10.221/firmware/sip8845_65.11-1-1MPP-897.loads

Use the *.loads file in the URL. The *.zip file contains other files.

## Limitations and Restrictions

### Phone Behavior During Times of Network Congestion

Anything that degrades network performance can affect phone voice and video quality, and in some cases, can cause a call to drop. Sources of network degradation can include, but are not limited to, the following activities:

Administrative tasks, such as an internal port scan or security scan

Attacks that occur on your network, such as a Denial of Service attack

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

The following list contains the severity 1, 2, and 3 defects that are open for the Cisco IP Phone 8800 Series Multiplatform Phones that use Firmware Release 11.1(1).

For more information about an individual defect, you can access the online history for the defect by accessing the Bug Search tool and entering the Identifier. You must be a registered Cisco.com user to access this defect information.

Because the defect status continually changes, the list reflects a snapshot of the defects that were open at the time this report was compiled. For an updated view of the open defects or to view specific bugs, access the Bug Search Toolkit as described in the Access Cisco Bug Search .

CSCvc40180 Offhook redial input DN not work.

CSCvc96609 MPP inconsistent group membership behavior.

CSCve53325 MPP-88xx: Unable to hear audio for incoming call when specific mobile phone is paired using bluetooth.

CSCvf77008 BLF lost twice in a row.

CSCvg00958 Phone doesn't send 420 Bad Extension when it receives INVITE with an unsupported value.

CSCvg10304 Dual Mode and IP Pref is IPv4, Phone is registered to IPv6 when IPv4 is down, no reg when IPv4 is up.

CSCvg41916 NTP appears to be non-functional.

CSCvg47648 Transfer softkey is missing.

CSCvg59538 8845: IPv6 only mode, VLAN change triggers phone reboot, but there is no record in reboot reason.

CSCvg61134 Factory reset phone, add report rule, the first-time report delta has speed dial parameter.

CSCvg61600 ALL-LANG: MPP: Geolocation status messages show up in English with locale.

CSCvg63918 Phone is ringback, change preferred audio device, use PLK to call, still uses the old device.

CSCvg68176 8861 Phone: Original call dropped when the new incoming call is answered by Bluetooth headset.

CSCvg70042 88xx: Wrong LED when DUT is configured call park shared-line ext function with wrong IP as PROXY.

CSCvg73078 Call not established on dialing out an speed dial when URI dialing and outbound proxy are set.

CSCvg75733 8861 phone: The caller's ID shows "Anonymous" in a very short time before picking up the call.

CSCvg77675 Select line key fails when barge fail.

CSCvg79273 The ongoing call turn to single-pass after phone roamed to another AP by powering off current AP.

CSCvg81958 Intermittent issues with BLF (the Genband call control)

CSCvg83031 8861 Phone: Call center queue states cannot show "full", when queue threshold is exceeded.

CSCvg83857 Random UI freezes.

CSCvg84786 8861phone Provisioning Status shows incorrect while use no <flat-profile> in resync file.

CSCvg96811 Hoteling subscribe does not retry after the server is unreachable or response error.

CSCvg99367 Phone may reboot when change to a non-exist Language from web page.

CSCvh06863 Plk (BLF+CP) picks up the caller in ringback state.

CSCvh13474 MPP: Phone boots up twice after upgrading to a new firmware load.

CSCvh13556 WEB GUI parameter RTP Packet Size validation issue.

CSCvh13736 Dictionary Server Script. The modified script doesn't take effect when only modify the "d1".

CSCvh14975 MPP device does not send LDAP query.

CSCvh15538 Video path is not available on DUTA when DUTB exits the early conference before DUTC answers.

CSCvh15653 Missed call LED does not light red when phone is in the call.

CSCvh16152 Phone sends all zeroes in MOS report.

CSCvh16689 88xx-MPP: PRT failing to upload into server which is using 'Content-Type: application/x-gzip'.

CSCvh16923 When making an AMR-WB call, coding mode cannot be changed for AMR-WB codec.

CSCvh17018 The second busy line can't forward when active call forward busy by pressing *90 (star code).

CSCvh17328 Recent call xmpp status is not updated when you change xmpp presence to offline.

CSCvh17346 xmpp, The login is invisible, does not work when users logs in.

CSCvh19110 Save "display brightness" in LCD GUI is wrong value after submitting it in web GUI.

### Resolved Caveats

The following list contains the severity 1, 2, and 3 defects that are resolved for the Cisco IP Phone 8800 Series Multiplatform Phones that use Firmware Release 11.1(1).

For more information about an individual defect, you can access the online history for the defect by accessing the Bug Search tool and entering the Identifier. You must be a registered Cisco.com user to access this defect information.

Because the defect status continually changes, the table reflects a snapshot of the defects that were resolved at the time this report was compiled. For an updated view of the resolved defects, access the Bug Search tool as described in the Access Cisco Bug Search .

CSCuw69731 MPP-8841 After upgrade CFWD All icon is getting Enable automatically.

CSCux03048 All Languages-MPP-88xx: Pressing the Back physical button deletes wallpaper.

CSCuz13922 MPP-88xx: Auto-Provisioning fails when SSLVerifyClient required.

CSCvb20017 NTP setting not cleared on a factory reset.

CSCvb65980 Nav hard key can't move cursor in the Search Enterprise folder.

CSCvb70815 Press BLF SD PLK several times phone still plays tone while idle.

CSCvb76405 Restart the phone using LCD UI and get crash log.

CSCvb77919 Set DNS Server order to Manual using web user interface does not work.

CSCvb84547 Phone resets after change of PC port status.

CSCvb86426 After dialing only two digits, phone goes onhook.

CSCvb86521 F1474: MPP - Prevent upgrade to Enterprise firmware.

CSCvb93247 NAT Keep Alive message always sends SIP Notify message.

CSCvb95670 Programmable Soft Keys do not work correctly during the middle of a call.

CSCvc06146 MPP-78xx/88xx MPP phone crashes after pressing Add List soft key of fnc=mp3.

CSCvc20880 MPP-88xx/78xx: Post CiscoIPPhoneText to phone get 500 internal server error.

CSCvc27587 MPP-User_Agent $VERSION does not work.

CSCvc27602 MPP-BLF subscribe, illegal CSEQ numbers from CP-7861.

CSCvc27606 MPP: Slow user.

CSCvc27608 MPP: Call fails when called phone places the call on hold.

CSCvc29353 Cisco IP Phone 8800 Series SIP Denial of Service vulnerability.

CSCvc30728 MPP-88xx: phone does not register when Auto VLAN is selected.

CSCvc30743 MPP-88xx: IT NAT keep alive not working in MPP.

CSCvc33150 MPP-78xx/88xx: Offhook, redials, and then edit call does not work.

CSCvc41857 After provision park PLK BLF list on the KEM disappears.

CSCvc51277 Call pickup is not successful when person enables a secure call.

CSCvc62590 Cisco IP Phone 8800 Series Denial of Service vulnerability.

CSCvc65877 BLF+SD setting makes status.xml unaccessible and Call status messes up.

CSCvc80462 MPP: Setting ringtone using provisioning is not working properly.

CSCvc87203 MPP: VID not working with BLF.

CSCvc89845 BLF notify updates missed.

CSCvc90927 Incorrect translation for German.

CSCvc94312 8800-MPP: PSK definition with '"' substitution failing to display name.

CSCvc96190 BLFs blink off, then periodically blinks back on.

CSCvc96607 MPP: Call transfer fails.

CSCvc96639 MPP: Call waiting notification tone.

CSCvc97835 Authenticated SIP Notify for Prov Refresh failing.

CSCvd48936 MPP: Screen fluctuations seen when call received on a shared line number.

CSCvd53399 ALL-LANG: MPP-88xx: Strings in Accessories show up localized when English is set as language.

CSCvd54756 MPP-88XX: WEB's current time still displays 24-hour format after setting to a 12-hour format.

CSCvd56997 MPP: Edit dial window returns to All call window before edit dial completes.

CSCve05725 un-SUBSCRIBE is not sent before un-REGISTER is sent to the server.

CSCve06274 MPP-78xx/88xx: Inactive prompt is not displayed in EM login phone when screen saver is enabled.

CSCve78758 88xx-MPP: Device is continuously ringing after call parked.

CSCvf04597 Device id is not set in CDP.

CSCvf06312 DUT phone can't hear the remote party for 1-2 seconds.

CSCvf62629 Phone parse error when receives SIP message with big Record-Route entries.

CSCvf77452 When provisioning a secondary config file to 8861 phone, 'Resource Exhausted' error message displays.

CSCvf77534 88xx-MPP: SIP Line failing to perform SIP REG FAILOVER to secondary SBC.

CSCvf86343 88xx-MPP: Line ID Mapping not working for incoming calls.

CSCvf96271 Phone continuously reboots after adding more than 100 contacts using provisioning.

CSCvf96764 BLF unsubscribed at 1800 secs after receiving blank dialog NOTIFY.

CSCvf96974 8861 fails to obtain IP address after reboot when on VVLAN.

CSCvg03527 Resumed held call does not use offhook handset, but Preferred Audio Device.

CSCvg15839 BXfer On Speed Dial incorrectly initiating a new call during midcall when to own extension.

CSCvg18498 Maximum length of Speed-dial button is too short.

CSCvg22225 Evaluation of MPP 8800 Audio-only IP Phones for Dnsmasq October 2017 vulnerabilities.

CSCvg29271 Phone answers to unsolicited SIP messages even after setting "Restricted Access Domains".

CSCvg29326 Voice Quality Report not getting set.

CSCvg38566 MPP-88xx:Phone reboots upon call pickup.

CSCvg40114 88xx-MPP: Emergency Call is failing to block hold/endCall user actions

CSCvg41339 88xx-MPP: Inconsistent handling of InfoSec trusted CA.

CSCvg42488 BLF incorrectly shows available when monitored line is in use.

CSCvg57045 User=Phone tag missing value causing XFER/Conf issues.

CSCvg62431 Manual PRT not following file definition.

CSCvg67251 NWay Conference Reject not handled gracefully.

CSCvg77605 QMON: Phone sends an unwanted PUBLISH right after an outgoing to PSTN is established.

CSCvg87084 Calls from MPP phone to VoLTE registered devices fail.

CSCvg91416 Local Directory Name is not displayed for incoming call.

CSCvh06566 88xx-MPP: No toast error screen for Blind XFER fail.

CSCvh12027 Dual Register feature, INVITE doesn't fail over to the Alternate Proxy when Proxy is down.

CSCvh13838 Delete "Dictionary Server Script", all the characters go away after quitting the screen saver.

CSCvh16184 Under Certain Circumstances, phone does not accept configuration of TIME_FORMAT.

CSCvh17106 7832/8811: The packet capture by phone have fcs error when the switch port have voice VLAN configured.

CSCvh19142 Locale Problem: 'No Service' in the call status doesn't translate.

CSCvh19322 Locale Problem: 'DNS Resolution' in Provisioning status doesn't translate.

CSCvg66758 XML configuration for phone background is not backward compatible.

CSCvg74520 IOT: More than 10 devices can be added successfully to a network conference.

CSCvg75487 Video phone parses dictionary server error.

CSCvh12025 Login xmpp with no password, no "authentication failures" message displays.

## Cisco IP Phone
	 Firmware Support Policy

For information on the support policy for phones, see http:/​/​www.cisco.com/​c/​en/​us/​support/​docs/​collaboration-endpoints/​unified-ip-phone-7900-series/​116684-technote-ipphone-00.html .

## Documentation, Service Requests, and Additional Information

For information on obtaining documentation, submitting a service request, and gathering additional information, see the monthly What’s New in Cisco Product Documentation , which also lists all new and revised Cisco technical documentation, at:

http:/​/​www.cisco.com/​c/​en/​us/​td/​docs/​general/​whatsnew/​whatsnew.html

Subscribe to the What’s New in Cisco Product Documentation as a Really Simple Syndication (RSS) feed and set content to be delivered directly to your desktop using a reader application. The RSS feeds are a free service and Cisco currently supports RSS Version 2.0.

| Phone | Support Requirements |
|---|---|
| Cisco IP Phone 8800 Series Multiplatform Phones | BroadSoft BroadWorks 21.0 Asterisk 13.1 |

| Step 1 | Click the following URL: https:/​/​software.cisco.com/​download/​navigator.html?mdfid=286311381&i=rm |
|---|---|
| Step 2 | Select IP Phone 8800 Series with Multiplatform Firmware in the middle pane. |
| Step 3 | Select your phone model (with Multiplatform Firmware) in the right pane. |
| Step 4 | Select the Multiplatform Firmware software type. |
| Step 5 | Navigate to All Releases > MPP v11 , select the 11.1.1 folder. |
| Step 6 | (Optional) Place your mouse pointer on the filename to display the file details and checksum values. |
| Step 7 | Download one of these files: For the 8811, 8841, 8851, and 8861– cmterm-88xx.11-1-1MPP-897_REL.zip For the 8845 and 8865— cp-8845_65.11-1-1MSR1-1_REL.zip |
| Step 8 | Click Accept License Agreement when you accept the software license. |
| Step 9 | Unzip the files. |
| Step 10 | Put the files in the TFTP, HTTP, or HTTPS download directory. |
| Step 11 | Configure the Upgrade Rule on the Provisioning tab in the web page with the valid URL. <protocol>://<serv_ip[port]>/filepath/sipxxx.loads You can also upgrade the third-party call control by using a URL in the web browser– <protocol>://<serv_ip[port]>/filepath/sipxxx.loads Here is an example, Example for 8811, 8841, 8851, and 8861 https://10.64.10.223/firmware/sip88xx.11-1-1MPP-897.loads Example for 8845 and 8865 https://10.64.10.221/firmware/sip8845_65.11-1-1MPP-897.loads Note Use the *.loads file in the URL. The *.zip file contains other files. | Note | Use the *.loads file in the URL. The *.zip file contains other files. |
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