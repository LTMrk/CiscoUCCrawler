---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cuipph-mpp-7832-firmware-11-1-1sr1-cs78-b-release-notes-for-7832mpp-110101sr-ba0e4a79ee
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cuipph/MPP/7832/firmware/11-1-1sr1/cs78_b_release_notes_for_7832mpp_110101sr1.html
retrieved_at: 2026-08-21T23:18:36.074866+00:00
---

Cisco IP Conference Phone 7832 Multiplatform Phones Release Notes for Firmware Release 11.1(1)SR1

# Cisco IP Conference Phone 7832 Multiplatform Phones Release Notes for Firmware Release 11.1(1)SR1

### Download Options

Updated: February 14, 2018

First Published:

Last Updated:

Text Part Number:

# Cisco IP Conference Phone 7832 Multiplatform Phones Release Notes for Firmware Release 11.1(1)SR1

Use these release notes with the Cisco IP Conference Phone 7832 Multiplatform Phones running SIP Firmware Release 11.1(1)SR1.

The following table describes the individual phone requirements.

Phone

Support Requirements

Cisco IP Conference Phone 7832 Multiplatform Phones

BroadSoft BroadWorks 21.0

MetaSphere CFS version 9.4

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

### Switch Sets Phone QoS

The phones let the switch set the Link Layer Discovery Protocol-Media Endpoint Devices (LLDP-MED) Quality of Service (QoS) setting. The switch overrides any manual setting on the phone. The Class of Service (CoS) is not affected.

## Installation

### Upgrade the Firmware

The Cisco IP Conference Phone 7832 Multiplatform Phones support a single image upgrade using TFTP, HTTP, or HTTPS protocols with a URL.

After the firmware upgrade completes, the phone reboots automatically.

https:/​/​software.cisco.com/​download/​navigator.html?mdfid=286311381&i=rm

Use the URL format– <protocol>://<serv_ip[:port]>/<filepath>/sipxxx.loads

You can also upgrade the third-party call control by using a URL in a web browser– <protocol>://<serv_ip[:port]>/<filepath>/sipxxx.loads

Example

https://10.74.10.225/firmware/sip7832.11-1-1MSR1-1.loads

Use the *.loads file in the URL. The *.zip file contains other files.

## Limitations and Restrictions

### Phone Behavior During Times of Network Congestion

Anything that degrades network performance can affect phone voice and video quality, and in some cases, can cause a call to drop. Sources of network degradation can include, but are not limited to, the following activities:

Administrative tasks, such as an internal port scan or security scan

Attacks that occur on your network, such as a Denial of Service attack

### Caller Identification and Other Phone Functions

Caller identification or other phone functions have not been verified with third-party applications for the visually or hearing impaired.

## Caveats

### View Caveats

You can search for caveats using the Cisco Bug Search tool.

Known caveats (bugs) are graded according to severity level, and can be either open or resolved.

To view the caveats, you need the following items:

Internet connection

Web browser

Cisco.com user ID and password

### Open Caveats

The following list contains the severity 1, 2, and 3 defects that are open for the Cisco IP Conference Phone 7832 Multiplatform Phones that use Firmware Release 11.1(1)SR1.

For more information about an individual defect, you can access the online history for the defect by accessing the Bug Search tool and entering the Identifier. You must be a registered Cisco.com user to access this defect information.

Because the defect status continually changes, the list reflects a snapshot of the defects that were open at the time this report was compiled. For an updated view of the open defects or to view specific bugs, access the Bug Search Toolkit as described in the View Caveats .

CSCvg00958 Phone doesn't send 420 Bad Extension when receives INVITE with unsupported value.

CSCvg10304 Dual Mode and IP Pref is IPv4, Phone does not fallback to IPv4 when IPv4 is up.

CSCvg59538 No record in reboot reason when the reboot is triggered by vlan change in IPv6 only mode.

CSCvg61600 Geolocation status messages show up in English words with other locale.

CSCvg63918 Phone still uses the old device after changing preferred audio device in ringback status.

CSCvg75579 Resync failed while using Digest Authentication with valid long password and username.

CSCvg83031 Call center queue states can not show "full", when queue threshold is exceeded.

CSCvg84786 Provisioning Status shows incorrect while use no <flat-profile> in resync file.

CSCvg96811 Hoteling subscribe will not retry after server unreachable or response error.

CSCvh13556 Parameter RTP Packet Size validation does not work.

CSCvh13875 Agent associating multiple call-center only shows one call-center's Queue Status.

CSCvh16152 MOS data is all zeroes in first second, phone should not send out this invalid data.

CSCvh17328 Recent call xmpp status is not updated when change xmpp presence to offline.

CSCvh19488 Generate PRT will make phone reboot when "PRT Upload Rule" can't queried by DNS in HK locale.

CSCvh23468 RFC2833 DTMF digits failing with AMR-WB mode.

CSCvh29624 Phone does not preserve the existing call when on secondary SBC and failover to primary SBC.

CSCvh52720 Ignore group paging on active call cannot work.

CSCvh52764 7832 phone Missing display: "Add from contacts" after press Option softkey during "edit speed dial"

CSCvh52884 Paging call can be answered when paging service disabled.

CSCvh66529 Phone reboots - Not handling multipart/mixed and multipart/related MIME type properly.

CSCvh66685 Softkey "back" comes up in the first softkey position instead of on the last.

CSCvh71029 Change of Hold Reminder Timer by resync will cause phone reboot.

CSCvh71043 Phone will reboot after received illegal value % for parameter.

CSCvh72506 Phone doesn't use the last DNS cached record if TTL expire and no response from DNS server.

CSCvh76496 Phone cannot get the correct content from HTTP 301 response.

CSCvh76520 Phone will always report download fail when receive 301 after reboot.

CSCvh76689 Phone cannot handle the content from HTTP 302 response.

CSCvh76791 Provisioning Status is wrong when receive 500/501/503.

CSCvh78587 Phone can't accept a long realm in 401 when upgrade.

### Resolved Caveats

The following list contains the severity 1, 2, and 3 defects that are resolved for the Cisco IP Conference Phone 7832 Multiplatform Phones that use Firmware Release 11.1(1)SR1.

For more information about an individual defect, you can access the online history for the defect by accessing the Bug Search tool and entering the Identifier. You must be a registered Cisco.com user to access this defect information.

Because the defect status continually changes, the list reflects a snapshot of the defects that were resolved at the time this report was compiled. For an updated view of the resolved defects or to view specific bugs, access the Bug Search Toolkit as described in the View Caveats .

CSCvh16689 Wrong alert message when phone get replies code 204, PRT actually uploaded successfully

CSCvh44179 When 3rd phone put the crypo which MPP can recognize after 5th, MPP SDP negotiation will fail.

CSCvh48979 Require Agent ACD state to remain in an Available State permanently

CSCvh59001 Device would reboot if it receives terminated NOTIFY with "rejected" reason

CSCvh61930 Device becomes slow and eventually freezes

CSCvh62303 Issue upgrading - missing host header on HTTP upgrade

## Cisco IP Phone
	 Firmware Support Policy

For information on the support policy for phones, see http:/​/​www.cisco.com/​c/​en/​us/​support/​docs/​collaboration-endpoints/​unified-ip-phone-7900-series/​116684-technote-ipphone-00.html .

## Documentation, Service Requests, and Additional Information

For information on obtaining documentation, submitting a service request, and gathering additional information, see the monthly What’s New in Cisco Product Documentation , which also lists all new and revised Cisco technical documentation, at:

http:/​/​www.cisco.com/​c/​en/​us/​td/​docs/​general/​whatsnew/​whatsnew.html

Subscribe to the What’s New in Cisco Product Documentation as a Really Simple Syndication (RSS) feed and set content to be delivered directly to your desktop using a reader application. The RSS feeds are a free service and Cisco currently supports RSS Version 2.0.

| Phone | Support Requirements |
|---|---|
| Cisco IP Conference Phone 7832 Multiplatform Phones | BroadSoft BroadWorks 21.0 MetaSphere CFS version 9.4 Asterisk 13.1 |

| Step 1 | Click the following URL: https:/​/​software.cisco.com/​download/​navigator.html?mdfid=286311381&i=rm |
|---|---|
| Step 2 | Select IP Phone 7800 Series with Multiplatform Firmware in the center pane. |
| Step 3 | Select IP Conference Phone 7832 with Multiplatform Firmware in the right pane. |
| Step 4 | Select the Multiplatform Firmware software type. |
| Step 5 | Under Latest , select the 11.1.1 MSR1-1 folder. |
| Step 6 | (Optional) Place your mouse pointer on the filename to display the file details and checksum values. |
| Step 7 | Download the cp-7832.11-1-1MSR1-1_REL.zip file. |
| Step 8 | Click Accept License Agreement when you accept the software license. |
| Step 9 | Unzip the firmware files. |
| Step 10 | Put the files in the TFTP, HTTP, or HTTPS download directory. |
| Step 11 | Configure the Upgrade Rule on the Provisioning tab in the web page with the valid URL. Use the URL format– <protocol>://<serv_ip[:port]>/<filepath>/sipxxx.loads You can also upgrade the third-party call control by using a URL in a web browser– <protocol>://<serv_ip[:port]>/<filepath>/sipxxx.loads Example https://10.74.10.225/firmware/sip7832.11-1-1MSR1-1.loads Note Use the *.loads file in the URL. The *.zip file contains other files. | Note | Use the *.loads file in the URL. The *.zip file contains other files. |
| Note | Use the *.loads file in the URL. The *.zip file contains other files. |

| Note | Use the *.loads file in the URL. The *.zip file contains other files. |
|---|---|

| Step 1 | Perform one of the following actions: |
|---|---|
| Step 2 | When prompted, log in with your Cisco.com user ID and password. |
| Step 3 | (Optional) To look for information about a specific problem, enter the bug ID number in the Search for field, and press Enter . |