---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cuipph-mpp-8800-firmware-11-1-1sr1-p881-b-release-notes2-8800mpp-110101sr1-h-5ea442075e
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cuipph/MPP/8800/firmware/11-1-1sr1/p881_b_release_notes2_8800mpp_110101sr1.html
retrieved_at: 2026-08-21T13:45:21.472260+00:00
---

Cisco IP Phone 8800 Series Multiplatform Phones Release Notes for Firmware Release 11.1(1)SR1

# Cisco IP Phone 8800 Series Multiplatform Phones Release Notes for Firmware Release 11.1(1)SR1

### Download Options

Updated: February 14, 2018

First Published:

Last Updated:

Text Part Number:

# Cisco IP Phone 8800 Series Multiplatform Phones Release Notes for Firmware Release 11.1(1)SR1

Use these release notes with the following Cisco IP Phone 8800 Series Multiplatform Phones running SIP Firmware Release 11.1(1)SR1.

Cisco IP Phone 8811, 8841, 8851, and 8861 Multiplatform Phones

Cisco IP Phone 8845 and 8865 Multiplatform Phones

The following table describes the individual phone requirements.

Phone

Support Requirements

Cisco IP Phone 8800 Series Multiplatform Phones

BroadSoft BroadWorks 21.0

MetaSphere CFS version 9.4

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

## New and Changed Features

The following sections describe the features that are new or have changed during this release.

### Switch Sets Phone QoS

The phones let the switch set the Link Layer Discovery Protocol-Media Endpoint Devices (LLDP-MED) Quality of Service (QoS) setting. The switch overrides any manual setting on the phone. The Class of Service (CoS) is not affected.

## Installation

### Upgrade the Firmware

The Cisco IP Phone 8800 Series Multiplatform Phones support a single image upgrade using TFTP, HTTP, or HTTPS.

After the firmware upgrade completes, the phone reboots automatically.

https:/​/​software.cisco.com/​download/​navigator.html?mdfid=286311381&i=rm

For the 8811, 8841, 8851, and 8861– cp-88xx.11-1-1MSR1-1_REL.zip

For the 8845 and 8865– cp-8845_65.11-1-1MSR1-1_REL.zip

Use the URL format– <protocol>://<serv_ip[:port]>/<filepath>/sipxxx.loads

You can also upgrade the third-party call control by using a URL in the web browser– <protocol>://<serv_ip[:port]>/<filepath>/sipxxx.loads

Example for 8811, 8841, 8851, and 8861

https://10.13.10.222/firmware/sip88xx.11-1-1MSR1-1.loads

Example for 8845 and 8865

https://10.42.10.223/firmware/sip8845_65.11-1-1MSR1-1.loads

Use the *.loads file in the URL. The *.zip file contains other files.

## Limitations and Restrictions

### Phone Behavior During Times of Network Congestion

Anything that degrades network performance can affect phone voice and video quality, and in some cases, can cause a call to drop. Sources of network degradation can include, but are not limited to, the following activities:

Administrative tasks, such as an internal port scan or security scan

Attacks that occur on your network, such as a Denial of Service attack

## Caveats

### View Caveats

You can search for caveats using the Cisco Bug Search tool.

Known caveats (bugs) are graded according to severity level, and can be either open or resolved.

To view the caveats, you need the following items:

Internet connection

Web browser

Cisco.com user ID and password

### Open Caveats

The following list contains the severity 1, 2, and 3 defects that are open for the Cisco IP Phone 8800 Series Multiplatform Phones that use Firmware Release 11.1(1)SR1.

For more information about an individual defect, you can access the online history for the defect by accessing the Bug Search tool and entering the Identifier. You must be a registered Cisco.com user to access this defect information.

Because the defect status continually changes, the list reflects a snapshot of the defects that were open at the time this report was compiled. For an updated view of the open defects or to view specific bugs, access the Bug Search Toolkit as described in the View Caveats .

Seven caveats apply only to the Cisco IP 8845 and 8865 Multiplatform Phones. The list annotates these caveats as [8845 and 8865 only] .

CSCvg00958 Phone doesn't send 420 Bad Extension when receives INVITE with unsupported value.

CSCvg10304 Dual Mode and IP Pref is IPv4, Phone does not fall back to IPv4 address when IPv4 is up.

CSCvg59538 No record in reboot reason when the reboot is triggered by a VLAN change in IPv6-only mode.

CSCvg61134 Report delta has a speed dial parameter in the first time after factory reset.

CSCvg61600 Geolocation status messages show up in English words with other locale.

CSCvg63918 Phone still uses the old device after changing preferred audio device in ringback status.

CSCvg70042 Wrong LED when DUT is configured call park shared-line ext function with wrong IP as PROXY.

CSCvg73078 Call cannot be established on dialing out a speed dial when URI dialing and outbound proxy are set.

CSCvg75579 Resync failed while using Digest Authentication with valid long password and username.

CSCvg75733 The caller's ID shows "Anonymous" in a short time before picking up the call.

CSCvg77675 Select line key fails when barge fails.

CSCvg79273 The on-going call turn to single-pass after phone roamed to another AP by powering off current AP.

CSCvg83031 Call center queue states cannot show "full", when queue threshold is exceeded.

CSCvg84786 Provisioning Status shows incorrect while use no <flat-profile> in resync file.

CSCvg96811 Hoteling subscribe will not retry after server unreachable or response error.

CSCvg99367 Phone may reboot when changing to a non-exist language from web page.

CSCvh06863 PLK (blf+cp) will pick up the caller in ringback state.

CSCvh13270 Display is showing two calls during conference.

CSCvh13556 Parameter RTP Packet Size validation does not work.

CSCvh13736 Phone can't choose the language when just modifying the "d1".

CSCvh15538 Video path is not available on DUTA when DUTB exits the early conference before DUTC answers. [8845 and 8865 only]

CSCvh16152 MOS data is all zeroes in first second, phone should not send out this invalid data.

CSCvh16923 When making an AMR-WB call, coding mode cannot be changed for AMR-WB codec. [8845 and 8865 only]

CSCvh17018 The second busy line can't forward when active call forward busy by pressing *90 (star code).

CSCvh17328 Recent call xmpp status is not updated when change xmpp presence to offline.

CSCvh17346 Configuration, "Login Invisible" does not work when user login.

CSCvh19110 Save "display brightness" in LCD GUI will be wrong value after submitting it in web GUI.

CSCvh19488 Generate PRT will make phone reboot when "PRT Upload Rule" can't queried by DNS in HK locale.

CSCvh23468 RFC2833 DTMF digits failing with AMR-WB mode.

CSCvh29624 Phone does not preserve the existing call when on secondary SBC and failover to primary SBC.

CSCvh52720 Ignore group paging on active call cannot work.

CSCvh52884 Paging call can be answered when paging service disabled.

CSCvh65657 The headset items are not aligned with the other items on the headset info UI.

CSCvh66529 Phone reboots - Not handling multipart-mixed and multipart-related MIME type properly.

CSCvh71029 Change of Hold Reminder Timer by resync causes phone to reboot.

CSCvh71043 Phone reboots after received illegal value % for parameter.

CSCvh67243 Speaker LED will not light when picking up a call.

CSCvh72506 Phone doesn't use the last DNS cached record if TTL expires and no response from DNS server.

CSCvh73357 Video does not always present. [8845 and 8865 only]

CSCvh76496 Phone cannot get the correct content from HTTP 301 response.

CSCvh76520 Phone always reports download fail when receive 301 after reboot.

CSCvh76689 Phone cannot handle the content from HTTP 302 response.

CSCvh76791 Provisioning status is wrong when receiving 500/501/503 response.

CSCvh77161 Call center Disposition code sent to BS server mismatch the DispostionCode set.

CSCvh78587 Phone can't accept a long realm in 401 when upgrade.

CSCvh78730 Callee side has no video after pressing hold/resume with Asterisk call server. [8845 and 8865 only]

CSCvh78875 The first frame of video is black screen after hold/resume one call with Asterisk call server. [8845 and 8865 only]

CSCvh80117 Upgrade rule with macro conditional expression $SWVER does not equal distinguish phone model.

CSCvh80256 Call UI only has hold and End call softkey after video disabled. [8845 and 8865 only]

CSCvh86427 Phone reboots occasionally when switching the phone between power-adapter and POE. [8845 and 8865 only]

CSCvh87790 Dual-mode phone should try IPv4 to upload PRT if no IPv6 address defined.

### Resolved Caveats

The following list contains the severity 1, 2, and 3 defects that are resolved for the Cisco IP Phone 8800 Series Multiplatform Phones that use Firmware Release 11.1(1)SR1.

For more information about an individual defect, you can access the online history for the defect by accessing the Bug Search tool and entering the Identifier. Register at Cisco.com to access this defect information.

Because the defect status continually changes, the list reflects a snapshot of the defects that were resolved at the time this report was compiled. For an updated view of the resolved defects or to view specific bugs, access the Bug Search Toolkit as described in the View Caveats .

CSCvh16689 Wrong alert message when the phone gets reply code 204, PRT uploaded successfully.

CSCvh44179 When third phone puts the crypto which MPP can recognize after fifth, MPP SDP negotiation fails.

CSCvh48979 Require Agent ACD state to remain in an Available state permanently.

CSCvh59001 Phone reboots if it receives terminated NOTIFY with "rejected" reason.

CSCvh61930 Phone becomes slow and eventually freezes.

CSCvh62303 Issue upgrading - missing host header in HTTP upgrade.

## Cisco IP Phone
	 Firmware Support Policy

For information on the support policy for phones, see http:/​/​www.cisco.com/​c/​en/​us/​support/​docs/​collaboration-endpoints/​unified-ip-phone-7900-series/​116684-technote-ipphone-00.html .

## Documentation, Service Requests, and Additional Information

For information on obtaining documentation, submitting a service request, and gathering additional information, see the monthly What’s New in Cisco Product Documentation , which also lists all new and revised Cisco technical documentation, at:

http:/​/​www.cisco.com/​c/​en/​us/​td/​docs/​general/​whatsnew/​whatsnew.html

Subscribe to the What’s New in Cisco Product Documentation as a Really Simple Syndication (RSS) feed and set content to be delivered directly to your desktop using a reader application. The RSS feeds are a free service and Cisco currently supports RSS Version 2.0.

| Phone | Support Requirements |
|---|---|
| Cisco IP Phone 8800 Series Multiplatform Phones | BroadSoft BroadWorks 21.0 MetaSphere CFS version 9.4 Asterisk 13.1 |

| Step 1 | Click the following URL: https:/​/​software.cisco.com/​download/​navigator.html?mdfid=286311381&i=rm |
|---|---|
| Step 2 | Select IP Phone 8800 Series with Multiplatform Firmware in the middle pane. |
| Step 3 | Select your phone model (with Multiplatform Firmware) in the right pane. |
| Step 4 | Select the Multiplatform Firmware software type. |
| Step 5 | Navigate to the Latest > 11.1.1 MSR1-1 folder. |
| Step 6 | (Optional) Place your mouse pointer on the filename to display the file details and checksum values. |
| Step 7 | Download one of these files: For the 8811, 8841, 8851, and 8861– cp-88xx.11-1-1MSR1-1_REL.zip For the 8845 and 8865– cp-8845_65.11-1-1MSR1-1_REL.zip |
| Step 8 | Click Accept License Agreement when you accept the software license. |
| Step 9 | Unzip the firmware files. |
| Step 10 | Put the files in the TFTP, HTTP, or HTTPS download directory. |
| Step 11 | Configure the Upgrade Rule on the Provisioning tab in the web page with the valid URL. Use the URL format– <protocol>://<serv_ip[:port]>/<filepath>/sipxxx.loads You can also upgrade the third-party call control by using a URL in the web browser– <protocol>://<serv_ip[:port]>/<filepath>/sipxxx.loads Example for 8811, 8841, 8851, and 8861 https://10.13.10.222/firmware/sip88xx.11-1-1MSR1-1.loads Example for 8845 and 8865 https://10.42.10.223/firmware/sip8845_65.11-1-1MSR1-1.loads Note Use the *.loads file in the URL. The *.zip file contains other files. | Note | Use the *.loads file in the URL. The *.zip file contains other files. |
| Note | Use the *.loads file in the URL. The *.zip file contains other files. |

| Note | Use the *.loads file in the URL. The *.zip file contains other files. |
|---|---|

| Step 1 | Perform one of the following actions: |
|---|---|
| Step 2 | When prompted, log in with your Cisco.com user ID and password. |
| Step 3 | (Optional) To look for information about a specific problem, enter the bug ID number in the Search for field, and press Enter . |

| Note | Seven caveats apply only to the Cisco IP 8845 and 8865 Multiplatform Phones. The list annotates these caveats as [8845 and 8865 only] . |
|---|---|