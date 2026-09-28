---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cuipph-mpp-7800-firmware-11-1-1sr2-pa2d-b-rn-11-1-1-sr2-html-20f50bbacf
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cuipph/MPP/7800/firmware/11-1-1sr2/pa2d_b_rn_11-1-1-sr2.html
retrieved_at: 2026-08-21T23:20:20.396242+00:00
---

Cisco IP Phone 7800 Series Multiplatform Phones Release Notes for Firmware Release 11.1(1)SR2

# Cisco IP Phone 7800 Series Multiplatform Phones Release Notes for Firmware Release 11.1(1)SR2

### Download Options

Updated: August 3, 2018

First Published: August 3, 2018

# Release Notes

Use these release notes with the following Cisco IP Phone 7800 Series Multiplatform Phones running SIP firmware release 11.1(1)SR2.

Cisco IP Phone 7811 Multiplatform Phones

Cisco IP Phone 7821 Multiplatform Phones

Cisco IP Phone 7841 Multiplatform Phones

Cisco IP Phone 7861 Multiplatform Phones

The following table describes the individual phone requirements.

Phone

Support Server

Cisco IP Phone 7800 Series Multiplatform Phones

BroadSoft BroadWorks 22.0

MetaSphere CFS version 9.4

Asterisk 11.0

## Related
               	 Documentation

Use the following sections to obtain related information.

### Cisco IP Phone
                  	 7800 Series Documentation

See the
                        		  publications that are specific to your language, phone model, and multiplatform
                        		  firmware release. Navigate from the following Uniform Resource Locator (URL):

https://www.cisco.com/c/en/us/products/collaboration-endpoints/ip-phone-7800-series-multiplatform-firmware/index.html

New and Changed Features

## New Domain Support while Provisioning

When a phone connects to a network for the first time or after a factory reset, if there are no DHCP options setup, it contacts
                     a device activation server for zero touch provisioning. Starting with this firmware release, phones will use activate.cisco.com instead of webapps.cisco.com for provisioning. Phones with older versions of the firmware will continue to use webapps.cisco.com . Cisco recommends that you allow both the domain names through your firewall.

### Where to Find More Information

Cisco IP Phone 7800 Series and Cisco IP Conference Phone 7832 Multiplatform Phones Provisioning Guide

## Upgrade the Firmware

Use the information in this section to upgrade Cisco IP Phone 7811, 7821, 7841, and 7861 Multiplatform Phones.

The Cisco IP Conference Phone 7832 Multiplatform Phones have a different firmware image. For more information, see the Cisco IP Conference Phone 7832 Multiplatform Phones Release Notes for firmware release 11.1(1)SR2, at this URL:

https://www.cisco.com/c/en/us/support/collaboration-endpoints/ip-phone-7800-series-multiplatform-firmware/products-release-notes-list.html

After the firmware upgrade completes, the phone reboots automatically.

Click the following URL:

https://software.cisco.com/download/navigator.html?mdfid=286311381

In the middle pane, select IP Phone 7800 Series With Multiplatform Firmware .

Select your phone model in the right pane.

On the next page that is displayed, select Multiplatform Firmware .

On the next page that is displayed, in the All Releases > MPP v11 folder, select 11.1.1 MSR2-1 .

(Optional) Place your mouse pointer on the file name in the right pane, to see the file details and checksum values.

Download the cp-78xx.11-1-1MSR2-1_REL.zip file.

Click Accept License Agreement .

Unzip the files.

Place the files in the TFTP, HTTP, or HTTPS download folder, depending on the protocol that you want to use for the upgrade.

You can upgrade the phone firmware using either of the following methods.

Upgrade the phone firmware from the phone administration web page:

On the phone administration web page, go to Admin Login > Advanced > Voice > Provisioning tab, Firmware Upgrade section. In the Upgrade Rule field, enter the load file URL as described below.

Load file URL format:

<upgrade protocol>://<server ip address>[:<port>]>/<path>/<file name>.loads

Example:

Click Submit All Changes .

Upgrade the phone firmware directly from your web browser:

In the address bar of your web browser, enter the phone upgrade URL as described below.

Phone upgrade URL format:

Load file URL format:

<upgrade protocol>://<server ip address>[:<port>]>/<path>/<file name>.loads

Example:

```
https://10.74.10.225/admin/upgrade?https://10.73.10.223/firmware/ sip78xx.11-1-1MSR2-1.loads
```

Specify the <file name>.loads file in the URL. The <file name>.zip file contains other files.

## Limitations and Restrictions

### Phone Behavior
                  	 During Times of Network Congestion

Anything that degrades network performance can affect phone voice and video quality, and in some cases, can cause a call
                        to drop. Sources of network degradation can include, but are not limited to, the following activities:

Administrative
                              				tasks, such as an internal port scan or security scan

Attacks that
                              				occur on your network, such as a Denial of Service attack

### Caller Identification and Other Phone Functions

Caller identification or other phone functions have not been verified with third-party applications for the visually or hearing
                        impaired.

### No Beep Sound Heard when the Mute Key is Pressed

When you press the Mute button during a call, you may not hear a beep sound. For anyone who is visually impaired, press the Mute button once to mute the phone and press the button twice to unmute the phone.

### Phone Has a Firmware Build Earlier than 11.0.0

Sometimes, a phone taken out of the box has a firmware build earlier than 11.0.0. When this happens, you must upgrade the
                        firmware on your phone to 11.0.0. Then you must update to 11.1.1 or later before you provision it.

Caveats

## Access Cisco Bug
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

Before you begin

### Before you begin

To access Cisco Bug
                     		  Search, you need the following items:

Internet
                           				connection

Web browser

Cisco.com user
                           				ID and password

To access Cisco Bug Search, go to:

https://tools.cisco.com/bugsearch

Log in with your
                              			 Cisco.com user ID and password.

To look for
                              			 information about a specific problem, enter the bug ID number in the Search for
                              			 field, then press Enter .

## Open Caveats

The following list contains the severity 1, 2, and 3 caveats that are open for the Cisco IP Phone 7800 Series Multiplatform Phones that use the firmware release 11.1(1)SR2.

This list reflects a snapshot of the caveats that were open at the time this report was compiled. The status of caveats may
                     have changed since then. For an updated view of the open caveats, or to view details or history for specific caveats, access
                     the Bug Search Toolkit as described in Access Cisco Bug Search . You must be a registered Cisco.com user to access this information.

CSCvg00958 Phone doesn't send 420 Bad Extension when receives INVITE with unsupported value

CSCvg10304 Dual Mode and IP Pref is IPv4, Phone does not fallback to IPv4 when IPv4 is up

CSCvg42260 Sometimes packet capture may not be terminated

CSCvg59538 No record in reboot reason when the reboot is triggered by vlan change in IPv6 only mode

CSCvg61600 Geolocation status messages show up in English words with other locale

CSCvg63918 Phone still uses the old device after changing preferred audio device in ringback status

CSCvg70042 Wrong LED when DUT is configured call park shared-line ext function with wrong IP as PROXY

CSCvg75579 Re-ync failed while using Digest Authentication with valid long password and username

CSCvg77675 Select line key fail when barge fail.

CSCvg83031 Call center queue states can not show "full", when queue threshold is exceeded.

CSCvg84786 Provisioning Status shows incorrect while use no <flat-profile> in resync file.

CSCvg96811 Hoteling subscribe does not retry after the server is unreachable or response error.

CSCvh02982 Initiate Paging call during upgrade, and the upgrade fails after the call is terminated.

CSCvh13270 Display is showing two calls during conference.

CSCvh13556 Parameter RTP Packet Size validation does not work.

CSCvh13875 Agent associating multiple call-center only shows one call-center's Queue Status.

CSCvh16152 MOS data is all zeroes in first second, phone should not send out this invalid data.

CSCvh17328 Recent call XMPP status is not updated when change XMPP presence to offline.

CSCvh17346 Configuration, "Login Invisible" does not work when user logs in.

CSCvh19488 Generate PRT will make phone reboot when "PRT Upload Rule" can't queried by DNS in HK locale.

CSCvh19503 PC port mirror does not work on 78xx with switch voice vlan configured.

CSCvh23468 RFC2833 DTMF digits failing with AMR-WB mode

CSCvh29624 Phone does not preserve the existing call when on secondary SBC and failover to primary SBC

CSCvh52720 Ignore group paging on active call cannot work.

CSCvh52884 Paging call can be answered when paging service disabled.

CSCvh66529 Phone reboots - Not handling multipart/mixed and multipart/related MIME type properly

CSCvh66685 Softkey "back" comes up in the first softkey position instead of on the last

CSCvh71029 Change of Hold Reminder Timer by resync will cause phone reboot

CSCvh71043 Phone will reboot after received illegal value % for parameter

CSCvh72506 Phone doesn't use the last DNS cached record if TTL expire and no response from DNS server

CSCvh73377 7861 Key System scenarios suffers serious delays with Broadworks call control

CSCvh76496 Phone cannot get the correct content from HTTP 301 response

CSCvh76520 Phone will always report download fail when receive 301 after reboot

CSCvh76689 Phone cannot handle the content from HTTP 302 response

CSCvh76791 Provisioning Status is wrong when receive 500/501/503

CSCvh78587 Phone can't accept a long realm in 401 when upgrade

CSCvh92118 Phone UI freezes, but on the next call inbound it starts working

## Resolved Caveats

The following list contains the severity 1, 2, and 3 caveats that are resolved for the Cisco IP Phone 7800 Series Multiplatform Phones that use Firmware Release 11.1(1)SR2.

This list reflects a snapshot of the caveats that were resolved at the time this report was compiled. The status of caveats
                     may have changed since then. For an updated view of the resolved caveats, or to view details or history for specific caveats,
                     access the Bug Search Toolkit as described in Access Cisco Bug Search . You must be a registered Cisco.com user to access this information.

CSCvh16689 PRT failing to upload into server since reply code 204 handled as failure

CSCvh98841 7861 Key System scenarios STILL suffers serious issue (keys in stuck state, phone resets)

CSCvh73377 7861 Key System scenarios suffers serious delays with Broadworks call control

CSCvi47436 CP-8861-3PCC - Daylight Savings Time did not take effect after DST started

CSCvi60903 Search in NAB: wrong character(rectangle) displayed at the end of directory result

CSCvi20334 No Call Wait tone in secured call

CSCvi18914 88xx-3PCC: 8851 losing audio with BroadCloud

CSCvj84294 Can not open phone's web page with Chrome

## Cisco IP Phone
               	 Firmware Support Policy

For information on the support policy for phones, see https://cisco.com/go/phonefirmwaresupport .

| Phone | Support Server |
|---|---|
| Cisco IP Phone 7800 Series Multiplatform Phones | BroadSoft BroadWorks 22.0 MetaSphere CFS version 9.4 Asterisk 11.0 |

| Step 1 | Click the following URL: https://software.cisco.com/download/navigator.html?mdfid=286311381 |
|---|---|
| Step 2 | In the middle pane, select IP Phone 7800 Series With Multiplatform Firmware . |
| Step 3 | Select your phone model in the right pane. |
| Step 4 | On the next page that is displayed, select Multiplatform Firmware . |
| Step 5 | On the next page that is displayed, in the All Releases > MPP v11 folder, select 11.1.1 MSR2-1 . |
| Step 6 | (Optional) Place your mouse pointer on the file name in the right pane, to see the file details and checksum values. |
| Step 7 | Download the cp-78xx.11-1-1MSR2-1_REL.zip file. |
| Step 8 | Click Accept License Agreement . |
| Step 9 | Unzip the files. |
| Step 10 | Place the files in the TFTP, HTTP, or HTTPS download folder, depending on the protocol that you want to use for the upgrade. |
| Step 11 | You can upgrade the phone firmware using either of the following methods. Upgrade the phone firmware from the phone administration web page: On the phone administration web page, go to Admin Login > Advanced > Voice > Provisioning tab, Firmware Upgrade section. In the Upgrade Rule field, enter the load file URL as described below. Load file URL format: <upgrade protocol>://<server ip address>[:<port>]>/<path>/<file name>.loads Example: https://10.73.10.223/firmware/sip78xx.11-1-1MSR2-1.loads Click Submit All Changes . Upgrade the phone firmware directly from your web browser: In the address bar of your web browser, enter the phone upgrade URL as described below. Phone upgrade URL format: <phone protocol>://<phone ip address[:port]>/admin/upgrade?<load file URL> Load file URL format: <upgrade protocol>://<server ip address>[:<port>]>/<path>/<file name>.loads Example: https://10.74.10.225/admin/upgrade?https://10.73.10.223/firmware/ sip78xx.11-1-1MSR2-1.loads Note Specify the <file name>.loads file in the URL. The <file name>.zip file contains other files. | Note | Specify the <file name>.loads file in the URL. The <file name>.zip file contains other files. |
| Note | Specify the <file name>.loads file in the URL. The <file name>.zip file contains other files. |

| Note | Specify the <file name>.loads file in the URL. The <file name>.zip file contains other files. |
|---|---|

| Step 1 | To access Cisco Bug Search, go to: https://tools.cisco.com/bugsearch |
|---|---|
| Step 2 | Log in with your
                              			 Cisco.com user ID and password. |
| Step 3 | To look for
                              			 information about a specific problem, enter the bug ID number in the Search for
                              			 field, then press Enter . |