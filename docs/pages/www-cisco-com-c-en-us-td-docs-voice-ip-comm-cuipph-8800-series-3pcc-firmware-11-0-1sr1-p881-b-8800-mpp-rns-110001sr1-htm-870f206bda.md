---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cuipph-8800-series-3pcc-firmware-11-0-1sr1-p881-b-8800-mpp-rns-110001sr1-htm-870f206bda
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cuipph/8800-series/3pcc/firmware/11-0-1sr1/p881_b_8800-mpp-rns-110001sr1.html
retrieved_at: 2026-08-21T13:33:10.391140+00:00
---

Cisco IP Phone 8800 Series Multiplatform Phones Release Notes for Firmware Release 11.0(1)SR1

# Cisco IP Phone 8800 Series Multiplatform Phones Release Notes for Firmware Release 11.0(1)SR1

### Download Options

Updated: October 25, 2017

First Published:

Last Updated:

Text Part Number:

# Cisco IP Phone 8800 Series Multiplatform Phones Release Notes for Firmware Release 11.0(1)SR1

These release notes support the Cisco IP Phone 8800 Series Multiplatform Phones running SIP Firmware Release 11.0(1)SR1.

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

## Installation

### Install Firmware

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

The following list shows the defects that are open for the Cisco IP Phone 8800 Series Multiplatform Phones for Firmware Release 11.0(1)SR1.

For more information about an individual defect, you can access the online record for the defect by accessing the Bug Search tool and entering the Identifier. You must be a registered Cisco.com user to access this online information.

Because defect status continually changes, the list reflects a snapshot of the defects that were open at the time this report was compiled. For an updated view of resolved defects, access the Bug Search tool as described in Access Cisco Bug Search .

CSCvf77452: When provisioning a secondary config file to 8861 phone, 'Resource Exhausted' error message appeared

CSCvf77534: 88xx-3PCC: SIP Line failing to perform SIP REG FAILOVER to secondary SBC

CSCvg03527: Resumed held call does not use offhook handset, but Preferred Audio Device

CSCvg13425: 8861 shows "Network Connection Failure" and "Disconnected"

CSCvg30255: Under CPE with QMON: After any incoming/outgoing call

CSCvg30260: Wrong DNS A query sent by device

CSCvg38032: F2100 - MPP phone does not block/ignore SIP messages from unknown sources

### Resolved Caveats

The following list shows the defects that are resolved for the Cisco IP Phone 8800 Series Multiplatform Phones for Firmware Release 11.0(1)SR1.

For more information about an individual defect, you can access the online record for the defect by accessing the Bug Search tool and entering the Identifier. You must be a registered Cisco.com user to access this online information.

Because defect status continually changes, the list reflects a snapshot of the defects that were resolved at the time this report was compiled. For an updated view of resolved defects, access the Bug Search tool as described in Access Cisco Bug Search .

CSCvf06312: 3pcc-88xx: can't hear the remote party for 1-2 seconds

CSCvf77452: When provisioning a secondary config file to 8861 phone, 'Resource Exhausted' error message appeared

CSCvf82885: Lack of Connectivity :REGISTER with a Call-ID incomplete

CSCvf94005: Cannot generate encrypted file using http+openssl

CSCvf96007: SIP notify message to retrieve current device configuration

CSCvf96974: 8861 fails to obtain IP address after reboot when on VVLAN

CSCvg29271: Phone answers to unsolicited SIP messages even after setting "Restricted Access Domains"

CSCvg29326: CP-8861-3PCC-K9= Voice Quality Report not getting set

CSCvg30274: BLF led randomly not aligned (blinking orange) because device didn't

CSCvg38265: Key Reinstallation attacks against WPA protocol

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
| Step 5 | In the Latest Releases folder, choose 11.0(1)SR1 . |
| Step 6 | Download the file cp-88xx.11-0-1MSR1-1.zip. |
| Step 7 | Unzip the files. |
| Step 8 | Put the files on the tftp/http/https download directory. |
| Step 9 | Configure the Upgrade Rule on the Provisioning tab in the web page with the valid URL. The format is: <schema>://<serv_ip[:port]>/filepath/sipxxx.loads The third-party call control can also upgrade via a URL in the web browser: <schema>://<serv_ip[:port]>/filepath/sipxxx.loads Here is an example, http://10.74.10.225/firmware/sip88xx.11-0-0MPP-7dev.loads Note The loads file is put in the file path of the above url. The zip file contains other file types also. Only the loads file is used in the above URL. After the firmware upgrade completes, the phone reboots automatically. | Note | The loads file is put in the file path of the above url. The zip file contains other file types also. Only the loads file is used in the above URL. |
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