---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cuipph-mpp-6800-firmware-11-2-4-ip66-b-release-notes-6861mpp-1124-html-f79394e20b
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cuipph/MPP/6800/firmware/11-2-4/ip66_b_release-notes-6861mpp-1124.html
retrieved_at: 2026-08-21T23:14:08.321787+00:00
---

Cisco IP Phone 6861 Multiplatform Phones Release Notes for Firmware Release 11.2(4)

# Cisco IP Phone 6861 Multiplatform Phones Release Notes for Firmware Release 11.2(4)

### Download Options

Updated: August 1, 2019

First Published: August 1, 2019

# Release Notes

Use these release notes with Cisco IP Phone 6861 Multiplatform Phones running SIP Firmware Release 11.2(4).

The following table describes the individual phone requirements.

Phone

Support Requirements

Cisco IP Phone 6861 Multiplatform Phones

BroadSoft BroadWorks 22.0

MetaSphere CFS version 9.4

Asterisk 13.21

## Cisco IP Phone 6861 Multiplatform Phones

The Cisco IP Phone 6861 Multiplatform Phones is a new addition to the Cisco IP Phone 6800 Series Multiplatform Phones . Here are some of the important features:

Supports for four lines

320 x 120 pixel, grayscale LCD display

Built-in 10/100M switch

Built-in WiFi module

Supports IPv4 and IPv6

Powered by 5V DC power adapter

For detailed specifications, see the product datasheet, located here: https://www.cisco.com/c/en/us/products/collaboration-endpoints/ip-phone-6800-series-multiplatform-firmware/datasheet-listing.html

### Where to Find More Information

Cisco IP Phone 6800 Series Multiplatform Phones Administration Guide

Cisco IP Phone 6800 Series Multiplatform Phones User Guide

Cisco IP Phone 6800 Series Multiplatform Phones Provisioning Guide

Cisco IP Phone 6861 Multiplatform Phones Quick Start Guide

## Cisco IP Phone 6861 Multiplatform Phones Documentation

See the publications that are specific to your language, phone model, and multiplatform firmware release. Navigate from the
                     following Uniform Resource Locator (URL):

https://www.cisco.com/c/en/us/support/collaboration-endpoints/ip-phone-6800-series-multiplatform-firmware/tsd-products-support-series-home.html

## Upgrade the Firmware

The Cisco IP Phone 6861 Multiplatform Phones support a single image upgrade using the TFTP, HTTP, or HTTPS protocols with a URL.

After the firmware upgrade completes, the phone reboots automatically.

Click the following URL:

https://software.cisco.com/download/navigator.html?mdfid=286318380&i=rm

Choose IP Phone 6800 Series with Multiplatform Firmware in the middle pane.

Choose IP Phone 6861 with Multiplatform Firmware .

Choose the Multiplatform Firmware software type.

In the All Releases > MPPv11 folder, select 11.2.4 .

(Optional) Place your mouse pointer on the file name to display the file details and checksum values.

Download the cmterm-6861.11-2-4MPP-395_REL.zip file.

Click Accept License Agreement when you accept the software license.

Unzip the firmware files.

Put the files in the TFTP, HTTP, or HTTPS download directory.

You can upgrade the phone firmware using either of the following methods:

Configure the Upgrade Rule on the Provisioning tab in the phone web page with the upgrade URL.

URL Format: <upgrade_protocol>://<serv_ip[:port]>/<filepath>/sipMMxx.RR-nnn.loads

Where the user input values are:

<upgrade_protocol> –HTTP, TFTP, or HTTPS.

<serv_ip[:port]> –Server IP address and optional port number.

<filepath> –File folder on the server that contains the firmware upgrade *.loads file.

MMxx –Cisco IP Phone MM Series with Multiplatform Firmware (for example, 68xx, 78xx, or 88xx)

or

MMxx –Cisco specific phone model (for example, 6861)

RR –Major and minor release numbers (for example, 11-2-4MPP)

nnn –Build number (for example, 395)

Example using the Upgrade Rule for .

tftp://10.73.10.192/firmware/sip6861.11-2-4MPP-395.loads

Provide a URL in a web browser that directs the call server to download the firmware to the phone.

URL Format: <phone_protocol>://<phone_ip[:port]>/admin/upgrade?

<upgrade_protocol>://<serv_ip[:port]>/<filepath>/sipMMxx.RR-nnn.loads

Where the user input values are:

<phone_protocol> –HTTP or HTTPS only.

<phone_ip[:port] –Phone IP address and optional port number.

<upgrade_protocol> –HTTP, TFTP, or HTTPS.

<serv_ip[:port]> –Server IP address and optional port number.

<filepath> –File folder on the server that contains the firmware upgrade *.loads file.

MMxx –Cisco IP Phone MM Series with Multiplatform Firmware (for example, 68xx, 78xx, or 88xx)

or

MMxx –Cisco specific phone model (for example, 6861)

RR –Major and minor release numbers (for example, 11-2-4MPP)

nnn –Build number (for example, 395)

Example using the web browser URL for .

https://10.74.10.225/admin/upgrade?http//10.73.10.192/firmware/sip6861.11-2-4MPP-395.loads

Use the *.loads file in the URL. The *.zip file contains other files.

## Limitations and Restrictions

### Phone Behavior
                  	 During Times of Network Congestion

Administrative
                              				tasks, such as an internal port scan or security scan

Attacks that
                              				occur on your network, such as a Denial of Service attack

### Caller Identification and Other Phone Functions

Caller identification or other phone functions have not been verified with third-party applications for the visually or hearing
                        impaired.

## Caveats

### View Caveats

You can search for caveats using the Cisco Bug Search tool.

Known caveats (bugs) are graded according to severity level, and can be either open or resolved.

Before you begin

#### Before you begin

To view the caveats, you need the following items:

Internet connection

Web browser

Cisco.com user ID and password

Perform one of the following actions:

To find all of the caveats for the 11.2.4 release, use this URL: https://bst.cloudapps.cisco.com/bugsearch/search?kw=*&pf=prdNm&rls=11.2.4&sb=anfr&bt=custV

To find all open caveats for the 11.2.4 release, use this URL: https://bst.cloudapps.cisco.com/bugsearch/search?kw=*&pf=prdNm&rls=11.2.4&sb=anfr&sts=open&bt=custV

To find all resolved caveats for the 11.2.4 release, use this URL: https://bst.cloudapps.cisco.com/bugsearch/search?kw=*&pf=prdNm&rls=11.2.4&sb=anfr&sts=fd&bt=custV

When prompted, log in with your Cisco.com user ID and password.

(Optional) To look for information about a specific problem, enter the bug ID number ( CSCxxnnnnn ) in the Search for field, and press Enter .

### Open Caveats

The following list contains the severity 1, 2, and 3 defects that are open for the Cisco IP Phone 6861 Multiplatform Phones that use Firmware Release 11.2(4).

For more information about an individual defect, you can access the online history for the defect by accessing the Bug Search
                        tool and entering the Identifier ( CSCxxnnnnn ). You must be a registered Cisco.com user to access this defect information.

Because the defect status continually changes, the list reflects a snapshot of the defects that were resolved at the time
                        this report was compiled. For an updated view of the resolved defects or to view specific bugs, access the Bug Search Toolkit
                        as described in the View Caveats .

CSCvp33011 Adjust ringer quickly while phone is in Wi-Fi scan, the ringer screen will not go away

CSCvp62448 uri dialing ending with # on "off hook" mode, the behavior is different with "on hook" mode

CSCvp64527 After connected to wifi successfully, XSI DND or CFWD takes about 3 minutes to be available.

CSCvp64719 DST end time rule won't take effect if new rule is very close to the enter criteria.

CSCvp78722 [asterisk v11] intermittently DUT fails to make local conf call on tls+<Secure Call Setting>= Yes

CSCvp81010 Phone ignores any other incoming paging calls when it is in an active paging call

CSCvq20186 Toast of call recording is of full lcd sized.

CSCvq22023 Phone warm reboot repeatedly when gets dhcp timeoff in wired connection and switches to wireless.

CSCvq23643 The countdown timer alerting of EM is not center-alignment

CSCvp94578 Do not disturb is not displayed in the exact center of top line

CSCvq51961 One phone was found no audio for 3 minutes when the connected AP swapping to radar channel.

### Resolved Caveats

There is no resolved caveat for Cisco IP Phone 6861 Multiplatform Phones with Firmware Release 11.2(4).

## Cisco IP Phone
               	 Firmware Support Policy

For information on the support policy for phones, see https://cisco.com/go/phonefirmwaresupport .

| Phone | Support Requirements |
|---|---|
| Cisco IP Phone 6861 Multiplatform Phones | BroadSoft BroadWorks 22.0 MetaSphere CFS version 9.4 Asterisk 13.21 |

| Step 1 | Click the following URL: https://software.cisco.com/download/navigator.html?mdfid=286318380&i=rm |
|---|---|
| Step 2 | Choose IP Phone 6800 Series with Multiplatform Firmware in the middle pane. |
| Step 3 | Choose IP Phone 6861 with Multiplatform Firmware . |
| Step 4 | Choose the Multiplatform Firmware software type. |
| Step 5 | In the All Releases > MPPv11 folder, select 11.2.4 . |
| Step 6 | (Optional) Place your mouse pointer on the file name to display the file details and checksum values. |
| Step 7 | Download the cmterm-6861.11-2-4MPP-395_REL.zip file. |
| Step 8 | Click Accept License Agreement when you accept the software license. |
| Step 9 | Unzip the firmware files. |
| Step 10 | Put the files in the TFTP, HTTP, or HTTPS download directory. |
| Step 11 | You can upgrade the phone firmware using either of the following methods: Configure the Upgrade Rule on the Provisioning tab in the phone web page with the upgrade URL. URL Format: <upgrade_protocol>://<serv_ip[:port]>/<filepath>/sipMMxx.RR-nnn.loads Where the user input values are: <upgrade_protocol> –HTTP, TFTP, or HTTPS. <serv_ip[:port]> –Server IP address and optional port number. <filepath> –File folder on the server that contains the firmware upgrade *.loads file. MMxx –Cisco IP Phone MM Series with Multiplatform Firmware (for example, 68xx, 78xx, or 88xx) or MMxx –Cisco specific phone model (for example, 6861) RR –Major and minor release numbers (for example, 11-2-4MPP) nnn –Build number (for example, 395) Example using the Upgrade Rule for . tftp://10.73.10.192/firmware/sip6861.11-2-4MPP-395.loads Provide a URL in a web browser that directs the call server to download the firmware to the phone. URL Format: <phone_protocol>://<phone_ip[:port]>/admin/upgrade? <upgrade_protocol>://<serv_ip[:port]>/<filepath>/sipMMxx.RR-nnn.loads Where the user input values are: <phone_protocol> –HTTP or HTTPS only. <phone_ip[:port] –Phone IP address and optional port number. <upgrade_protocol> –HTTP, TFTP, or HTTPS. <serv_ip[:port]> –Server IP address and optional port number. <filepath> –File folder on the server that contains the firmware upgrade *.loads file. MMxx –Cisco IP Phone MM Series with Multiplatform Firmware (for example, 68xx, 78xx, or 88xx) or MMxx –Cisco specific phone model (for example, 6861) RR –Major and minor release numbers (for example, 11-2-4MPP) nnn –Build number (for example, 395) Example using the web browser URL for . https://10.74.10.225/admin/upgrade?http//10.73.10.192/firmware/sip6861.11-2-4MPP-395.loads Note Use the *.loads file in the URL. The *.zip file contains other files. | Note | Use the *.loads file in the URL. The *.zip file contains other files. |
| Note | Use the *.loads file in the URL. The *.zip file contains other files. |

| Note | Use the *.loads file in the URL. The *.zip file contains other files. |
|---|---|

| Step 1 | Perform one of the following actions: To find all of the caveats for the 11.2.4 release, use this URL: https://bst.cloudapps.cisco.com/bugsearch/search?kw=*&pf=prdNm&rls=11.2.4&sb=anfr&bt=custV To find all open caveats for the 11.2.4 release, use this URL: https://bst.cloudapps.cisco.com/bugsearch/search?kw=*&pf=prdNm&rls=11.2.4&sb=anfr&sts=open&bt=custV To find all resolved caveats for the 11.2.4 release, use this URL: https://bst.cloudapps.cisco.com/bugsearch/search?kw=*&pf=prdNm&rls=11.2.4&sb=anfr&sts=fd&bt=custV |
|---|---|
| Step 2 | When prompted, log in with your Cisco.com user ID and password. |
| Step 3 | (Optional) To look for information about a specific problem, enter the bug ID number ( CSCxxnnnnn ) in the Search for field, and press Enter . |