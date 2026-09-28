---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cuipph-mpp-6800-firmware-11-3-1-6871-ip67-b-6871-rn-1131-html-525146bfa3
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cuipph/MPP/6800/firmware/11-3-1_6871/ip67_b_6871-rn-1131.html
retrieved_at: 2026-08-21T23:13:59.932401+00:00
---

Cisco IP Phone 6871 Multiplatform Phones Release Notes for Firmware Release 11.3(1)

# Cisco IP Phone 6871 Multiplatform Phones Release Notes for Firmware Release 11.3(1)

### Download Options

Updated: November 25, 2019

First Published: November 25, 2019

# Release Notes

Use these release notes with Cisco IP Phone 6871 Multiplatform Phones running SIP Firmware Release 11.3(1).

The following table describes the phone requirements.

Phone

Support Requirements

Cisco IP Phone 6871 Multiplatform Phones

BroadSoft BroadWorks 22.0

MetaSphere CFS version 9.5

Asterisk 11.0

## Related Documents

The following sections describe the documentation enhancement and additional documentation information.

### Cisco IP Phone 6871 Multipatform Phones Documentation

See the publications that are specific to your language, phone model, and multiplatform firmware release. Navigate from the
                        following Uniform Resource Locator (URL):

https://www.cisco.com/c/en/us/support/collaboration-endpoints/ip-phone-6800-series-multiplatform-firmware/tsd-products-support-series-home.html

## Cisco IP Phone 6871 Multiplatform Phones

The Cisco IP Phone 6871 Multiplatform Phones is a new addition to the Cisco IP Phone 6800 Series Multiplatform Phones . Here are some of the important features:

Support for six lines

480 x 272 pixel, high resolution color LCD display

Built-in 10/100/1000M switch

Supports IPv4 and IPv6

Powered by 802.3af PoE class 3 or an optional 5V DC power adapter

A USB port supporting Cisco Headset 500 Series

For detailed specifications, see the product datasheet, located here: https://www.cisco.com/c/en/us/products/collaboration-endpoints/ip-phone-6800-series-multiplatform-firmware/datasheet-listing.html

### Where to Find More Information

Cisco IP Phone 6800 Series Multiplatform Phones Administration Guide

Cisco IP Phone 6800 Series Multiplatform Phones User Guide

Cisco IP Phone 6871 Multiplatform Phones Quick Start Guide

## Upgrade the Firmware

You can upgrade the phone firmware with TFTP, HTTP, or HTTPS. After the upgrade completes, the phone reboots automatically.

Click this link:

https://software.cisco.com/download/home/286318380

On the Software Download web page that is displayed, ensure that IP Phone 6800 Series with Multiplatform Firmware is selected in the middle pane.

Select your phone model in the right pane.

On the next page that is displayed, select Multiplatform Firmware .

Under Latest Release , select 11.3.1 .

(Optional) Place your mouse pointer on the file name to see the file details and checksum values.

Download the file cmterm-68xx.11-3-1MPP-697_REL.zip .

Click Accept License Agreement .

Unzip the file and place the files in the appropriate location on your upgrade server.

The appropriate location is the TFTP, HTTP, or HTTPS download folder, depending on the protocol that you want to use for the
                                 upgrade.

Upgrade the phone firmware with one of these methods.

Upgrade the phone firmware from the phone administration web page:

On the phone administration web page, go to Admin Login > Advanced , Voice > Provisioning > Firmware Upgrade .

In the Upgrade Rule field, enter the load file URL as described below.

Load file URL format:

<upgrade protocol>://<upgrade server ip address>[:<port>]>/<path>/<file name>.loads

Examples:

https://10.73.10.223/firmware/sip68xx.11-3-1MPP-697.loads

Click Submit All Changes .

Upgrade the phone firmware directly from your web browser:

In the address bar of your web browser, enter the phone upgrade URL as described below.

Phone upgrade URL format:

Load file URL format:

<upgrade protocol>://<upgrade server ip address>[:<port>]>/<path>/<file name>.loads

Examples:

https://10.74.10.225/admin/upgrade?https://10.73.10.223/firmware/sip68xx.11-3-1MPP-697.loads

Specify the <file name>.loads file in the URL. The <file name>.zip file contains other files.

## Limitations and Restrictions

### Phone Behavior
                  	 During Times of Network Congestion

Anything that degrades network performance can affect phone audio and, in some cases, can cause a call to drop. Sources of
                        network degradation can include, but are not limited to, the following activities:

Administrative
                              				tasks, such as an internal port scan or security scan

Attacks that
                              				occur on your network, such as a Denial of Service attack

## Caveats

### View Caveats

You can search for caveats (bugs) with the Cisco Bug Search tool.

Known caveats are graded according to severity level, and are either open or resolved.

Before you begin

#### Before you begin

Click one of the following links:

To view all caveats that affect this release:

To view open caveats that affect this release:

To view resolved caveats that affect this release:

When prompted, log in with your Cisco.com user ID and password.

(Optional) For information about a specific caveat, enter the bug ID number ( CSCxxnnnnn ) in the Search for field, and press Enter .

### Open Caveats

The following list contains the severity 1, 2, and 3 defects that are open for the Cisco IP Phone 6871 Multiplatform Phones that use Firmware Release 11.3(1).

For more information about an individual defect, you can access the online history for the defect by accessing the Bug Search
                        tool and entering the Identifier ( CSCxxnnnnn ). You must be a registered Cisco.com user to access this defect information.

Because the defect status continually changes, the list reflects a snapshot of the defects that were resolved at the time
                        this report was compiled. For an updated view of the resolved defects or to view specific bugs, access the Bug Search Toolkit
                        as described in View Caveats .

CSCvo26146 Enable/Disable Vertical Service Activation Codes toggle button addition

CSCvq29352 Change audio path from headset to speaker when playing dial tone,will hear burst sound

CSCvr14202 Phone would not register after switch back from static ipv6 to DHCP ipv6

CSCvr38502 Profile account setup toast does not work with provisioning on LCD

CSCvr64226 All the lines' call logs will be deleted when select a line and press Delete All

CSCvr64429 Slight Echo is heard when calling using handset

CSCvr76623 CP-7841-3PCC-K9= Conference URI not working

CSCvr77995 Jabra Engage 75 headset does not work well if connect it via USB interface

CSCvr83686 After upgrade to new load, DDP will not auto-reconnect to 6871

CSCvr86286 Remote SDK: WebSocket Control Server URL field does not honor HTTP/1.0 Redirects

CSCvr86301 Remote SDK: WebSocket Control Server URL waits 10 seconds after HTTP 401 Challenge

CSCvr87292 Failed to answer the paging call after make paging call with headset button

CSCvr91877 Headset Status shows upgrading even if headset upgrade successfully

CSCvr91970 6871 Date is truncated if icons of headset upgrading and secured lock are displayed at the same time

CSCvr94049 Extra char is displayed at the end of cached DNS result in syslog

### Resolved Caveats

There is no resolved caveat for the Cisco IP Phone 6871 Multiplatform Phones .

## Cisco IP Phone Firmware Support Policy

For information on the support policy for phones, see https://cisco.com/go/phonefirmwaresupport .

| Phone | Support Requirements |
|---|---|
| Cisco IP Phone 6871 Multiplatform Phones | BroadSoft BroadWorks 22.0 MetaSphere CFS version 9.5 Asterisk 11.0 |

| Step 1 | Click this link: https://software.cisco.com/download/home/286318380 On the Software Download web page that is displayed, ensure that IP Phone 6800 Series with Multiplatform Firmware is selected in the middle pane. |
|---|---|
| Step 2 | Select your phone model in the right pane. |
| Step 3 | On the next page that is displayed, select Multiplatform Firmware . |
| Step 4 | Under Latest Release , select 11.3.1 . |
| Step 5 | (Optional) Place your mouse pointer on the file name to see the file details and checksum values. |
| Step 6 | Download the file cmterm-68xx.11-3-1MPP-697_REL.zip . |
| Step 7 | Click Accept License Agreement . |
| Step 8 | Unzip the file and place the files in the appropriate location on your upgrade server. The appropriate location is the TFTP, HTTP, or HTTPS download folder, depending on the protocol that you want to use for the
                                 upgrade. |
| Step 9 | Upgrade the phone firmware with one of these methods. Upgrade the phone firmware from the phone administration web page: On the phone administration web page, go to Admin Login > Advanced , Voice > Provisioning > Firmware Upgrade . In the Upgrade Rule field, enter the load file URL as described below. Load file URL format: <upgrade protocol>://<upgrade server ip address>[:<port>]>/<path>/<file name>.loads Examples: https://10.73.10.223/firmware/sip68xx.11-3-1MPP-697.loads Click Submit All Changes . Upgrade the phone firmware directly from your web browser: In the address bar of your web browser, enter the phone upgrade URL as described below. Phone upgrade URL format: <phone protocol>://<phone ip address[:port]>/admin/upgrade?<load file URL> Load file URL format: <upgrade protocol>://<upgrade server ip address>[:<port>]>/<path>/<file name>.loads Examples: https://10.74.10.225/admin/upgrade?https://10.73.10.223/firmware/sip68xx.11-3-1MPP-697.loads Note Specify the <file name>.loads file in the URL. The <file name>.zip file contains other files. | Note | Specify the <file name>.loads file in the URL. The <file name>.zip file contains other files. |
| Note | Specify the <file name>.loads file in the URL. The <file name>.zip file contains other files. |

| Note | Specify the <file name>.loads file in the URL. The <file name>.zip file contains other files. |
|---|---|

| Step 1 | Click one of the following links: To view all caveats that affect this release: https://bst.cloudapps.cisco.com/bugsearch/search?kw=*&pf=prdNm&pfVal=286318380&rls=11.3(1)&sb=anfr&bt=custV To view open caveats that affect this release: https://bst.cloudapps.cisco.com/bugsearch/search?kw=*&pf=prdNm&pfVal=286318380&rls=11.3(1)&sb=anfr&sts=open&bt=custV To view resolved caveats that affect this release: https://bst.cloudapps.cisco.com/bugsearch/search?kw=*&pf=prdNm&pfVal=286318380&rls=11.3(1)&sb=anfr&sts=fd&bt=custV |
|---|---|
| Step 2 | When prompted, log in with your Cisco.com user ID and password. |
| Step 3 | (Optional) For information about a specific caveat, enter the bug ID number ( CSCxxnnnnn ) in the Search for field, and press Enter . |