---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cuipph-mpp-7800-firmware-11-1-2sr1-pa2d-b-rn-11-1-2-sr1-html-ea48274066
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cuipph/MPP/7800/firmware/11-1-2sr1/pa2d_b_rn_11-1-2-sr1.html
retrieved_at: 2026-08-21T23:20:12.371027+00:00
---

Cisco IP Phone 7800 Series Multiplatform Phones Release Notes for Firmware Release 11.1(2)SR1

# Cisco IP Phone 7800 Series Multiplatform Phones Release Notes for Firmware Release 11.1(2)SR1

First Published: August 3, 2018

# Release Notes

Use these release notes with the following Cisco IP Phone 7800 Series Multiplatform Phones running SIP firmware release 11.1(2)SR1.

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

The Cisco IP Conference Phone 7832 Multiplatform Phones have a different firmware image. For more information, see the Cisco IP Conference Phone 7832 Multiplatform Phones Release Notes for firmware release 11.1(2)SR1, at this URL:

https://www.cisco.com/c/en/us/support/collaboration-endpoints/ip-phone-7800-series-multiplatform-firmware/products-release-notes-list.html

After the firmware upgrade completes, the phone reboots automatically.

Click the following URL:

https://software.cisco.com/download/navigator.html?mdfid=286311381

In the middle pane, select IP Phone 7800 Series With Multiplatform Firmware .

Select your phone model in the right pane.

On the next page that is displayed, select Multiplatform Firmware .

On the next page that is displayed, in the All Releases > MPP v11 folder, select 11.1.2 MSR1-2 .

(Optional) Place your mouse pointer on the file name in the right pane, to see the file details and checksum values.

Download the cp-78xx.11-1-2MSR1-1_REL.zip file.

Click Accept License Agreement .

Unzip the files.

Place the files in the TFTP, HTTP, or HTTPS download folder, depending on the protocol that you want to use for the upgrade.

Upgrade the phone firmware with one of these methods.

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
https://10.74.10.225/admin/upgrade?https://10.73.10.223/firmware/ sip78xx.11-1-2MSR1-1.loads
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

The following list contains the severity 1, 2, and 3 caveats that are open for the Cisco IP Phone 7800 Series Multiplatform Phones that use the firmware release 11.1(2)SR1.

This list reflects a snapshot of the caveats that were open at the time this report was compiled. The status of caveats may
                     have changed since then. For an updated view of the open caveats, or to view details or history for specific caveats, access
                     the Bug Search Toolkit as described in Access Cisco Bug Search . You must be a registered Cisco.com user to access this information.

CSCvg91741 phone can't access the webpage with http protocal

CSCvh13875 Agent associating multiple call-center only shows one call-center's Queue Status

CSCvh19503 PC port mirror does not work on 78xx with switch voice vlan configured

CSCvh59168 LDAP directory name display issue

CSCvh67018 Phone upgrade fails when it receives 302 or 303 response.

CSCvh76496 Phone cannot get the correct content from an HTTP 301 response.

CSCvh76689 Phone cannot handle the content from an HTTP 302 response.

CSCvh90129 Phone reboots when you configure BLF only without mapped line key.[7811 only]

CSCvi28353 phone reboot when have long XML User Name or password

CSCvi30920 7811/7832: String "Show detail" is truncated on English US

CSCvi40614 7861 reboot just use last line to make a call

CSCvi79573 DUT failed to resync with multiple options

CSCvi88682 re-enter Server All calls or Enterprise Directory, Cancel, then phone reboots

CSCvi90186 should limit the "TOS/DiffServ Value" on web,if not,phone will keep rebooting with max length value

## Resolved Caveats

The following list contains the severity 1, 2, and 3 caveats that are resolved for the Cisco IP Phone 7800 Series Multiplatform Phones that use Firmware Release 11.1(2)SR1.

This list reflects a snapshot of the caveats that were resolved at the time this report was compiled. The status of caveats
                     may have changed since then. For an updated view of the resolved caveats, or to view details or history for specific caveats,
                     access the Bug Search Toolkit as described in Access Cisco Bug Search . You must be a registered Cisco.com user to access this information.

CSCvj07154 CP-88xx-3PCC - Unable to hear beep from voicemail server

CSCvj59089 Phone fails to provision using TR-69

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
| Step 5 | On the next page that is displayed, in the All Releases > MPP v11 folder, select 11.1.2 MSR1-2 . |
| Step 6 | (Optional) Place your mouse pointer on the file name in the right pane, to see the file details and checksum values. |
| Step 7 | Download the cp-78xx.11-1-2MSR1-1_REL.zip file. |
| Step 8 | Click Accept License Agreement . |
| Step 9 | Unzip the files. |
| Step 10 | Place the files in the TFTP, HTTP, or HTTPS download folder, depending on the protocol that you want to use for the upgrade. |
| Step 11 | Upgrade the phone firmware with one of these methods. Upgrade the phone firmware from the phone administration web page: On the phone administration web page, go to Admin Login > Advanced > Voice > Provisioning tab, Firmware Upgrade section. In the Upgrade Rule field, enter the load file URL as described below. Load file URL format: <upgrade protocol>://<server ip address>[:<port>]>/<path>/<file name>.loads Example: https://10.73.10.223/firmware/sip78xx.11-1-2MSR1-1.loads Click Submit All Changes . Upgrade the phone firmware directly from your web browser: In the address bar of your web browser, enter the phone upgrade URL as described below. Phone upgrade URL format: <phone protocol>://<phone ip address[:port]>/admin/upgrade?<load file URL> Load file URL format: <upgrade protocol>://<server ip address>[:<port>]>/<path>/<file name>.loads Example: https://10.74.10.225/admin/upgrade?https://10.73.10.223/firmware/ sip78xx.11-1-2MSR1-1.loads Note Specify the <file name>.loads file in the URL. The <file name>.zip file contains other files. | Note | Specify the <file name>.loads file in the URL. The <file name>.zip file contains other files. |
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