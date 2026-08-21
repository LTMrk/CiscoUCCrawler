---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cuipph-mpp-6800-firmware-11-0-2-releasenotes-p680-b-6800-mpp-rns-110002-html-4e1068e70f
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cuipph/MPP/6800/firmware/11-0-2/releasenotes/p680_b_6800-mpp-rns-110002.html
retrieved_at: 2026-08-21T23:14:53.660738+00:00
---

Cisco IP Phone 6800 Series Multiplatform Phones Release Notes for Firmware Release 11.0(2)

# Cisco IP Phone 6800 Series Multiplatform Phones Release Notes for Firmware Release 11.0(2)

First Published: November 20, 2017

Last Updated: December 15, 2017

# Cisco IP Phone 6800 Series Multiplatform Phones Release Notes for Firmware Release 11.0(2)

These release notes support the Cisco IP Phone 6800 Series Multiplatform Phones running SIP Firmware Release 11.0(2).

The following table lists the support and protocol compatibility for the Cisco IP Phones.

Cisco IP Phone

Protocol

Support Requirements

Cisco IP Phone 6800 Series Multiplatform Phones

SIP

BroadSoft BroadWorks 21.0

Asterisk 13.1

## Cisco IP Phone 6800 Series Multiplatform Phones Introduction

The Cisco IP Phone 6800 Series Multiplatform Phones deliver easy-to-use, highly-secure voice communications.

Features

6841

6851

Screen

Greyscale, with backlight

Greyscale, with backlight

Lines

4

4

Fixed feature keys

9

9

Power over Ethernet (PoE)

Not supported

Supported

Electronic Hookswitch Headset support

Not supported

Supported

## Related
               	 Documentation

Use the following sections to obtain related information.

### Cisco IP Phone 6800 Series Documentation

See the publications that are specific to your language, phone model, and multiplatform firmware release. Navigate from the
                        following Uniform Resource Locator (URL):

https://www.cisco.com/c/en/us/support/collaboration-endpoints/ip-phone-6800-series-multiplatform-firmware/tsd-products-support-series-home.html

## Installation

### Upgrade Firmware

The Cisco IP Phone 6800 Series Multiplatform Phones supports a single image upgrade by TFTP, HTTP, or HTTPS.

After the firmware upgrade completes, the phone reboots automatically.

Step 1

Go to the following URL:

https://software.cisco.com/download/navigator.html?mdfid=286318380&i=rm

Step 2

Choose IP Phones 6800 Series with Multiplatform Firmware .

Step 3

Choose your phone model.

Step 4

Choose Multiplatform Firmware .

Step 5

In the Latest Releases folder, choose 11.0(2) .

Step 6

Download the file cmterm-68xx.11-0-2MPP-98_REL.zip .

Step 7

Unzip the files.

Step 8

Put the files on the tftp, http, or https download directory.

Step 9

Configure the Upgrade Rule on the Provisioning tab in the web page with the valid URL. The format is <schema>://<serv_ip[:port]>/<filepath>/sipxxx.loads

The third-party call control can also upgrade via a URL in the web browser <schema>://<serv_ip[:port]>/<filepath>/sipxxx.loads

Example

http://10.74.10.225/firmware/sip68xx.11-0-2MPP-98.loads

You must use the loads file in the URL. The zip file contains other files.

## Limitations and Restrictions

### Phone Behavior
                  	 During Times of Network Congestion

Administrative tasks, such as an internal port scan or security scan.

Attacks that occur on your network, such as a Denial of Service attack.

### Caller Identification and Other Phone Functions

Caller identification or other phone functions have not been verified with third-party applications for the visually or hearing
                        impaired.

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

Before you begin

#### Before you begin

To access Cisco Bug
                        		  Search, you need the following items:

Internet
                              				connection

Web browser

Cisco.com user
                              				ID and password

Step 1

To access Cisco Bug Search, go to:

https://bst.cloudapps.cisco.com/bugsearch

Step 2

Log in with your
                                 			 Cisco.com user ID and password.

Step 3

To look for
                                 			 information about a specific problem, enter the bug ID number in the Search for
                                 			 field, then press Enter .

### Open Caveats

The following list contains defects that are open for the Cisco IP Phone 6800 Series Multiplatform Phones for Firmware Release 11.0(2).

A registered cisco.com user ID is required to access this information online.

Because defect status continually changes, the list reflects a snapshot of the defects that were open at the time this report
                        was compiled. For an updated view of resolved defects, access the Bug Search tool as described in Access Cisco Bug Search .

CSCvg63336 Multiple Vulnerabilities in glibc

## Cisco IP Phone
               	 Firmware Support Policy

For information on the support policy for phones, see the Cisco IP Phone Firmware Support Policy .

## Documentation, Service Requests, and Additional Information

For information on obtaining documentation, submitting a service request, and gathering additional information, see the monthly What’s New in Cisco Product Documentation , which also lists all new and revised Cisco technical documentation, at:

http://www.cisco.com/c/en/us/td/docs/general/whatsnew/whatsnew.html

Subscribe to the What’s New in Cisco Product Documentation as a Really Simple Syndication (RSS) feed and set content to be delivered directly to your desktop using a reader application.
                  The RSS feeds are a free service and Cisco currently supports RSS Version 2.0.

| Cisco IP Phone | Protocol | Support Requirements |
|---|---|---|
| Cisco IP Phone 6800 Series Multiplatform Phones | SIP | BroadSoft BroadWorks 21.0 Asterisk 13.1 |

| Features | 6841 | 6851 |
|---|---|---|
| Screen | Greyscale, with backlight | Greyscale, with backlight |
| Lines | 4 | 4 |
| Fixed feature keys | 9 | 9 |
| Power over Ethernet (PoE) | Not supported | Supported |
| Electronic Hookswitch Headset support | Not supported | Supported |

| Step 1 | Go to the following URL: https://software.cisco.com/download/navigator.html?mdfid=286318380&i=rm |
|---|---|
| Step 2 | Choose IP Phones 6800 Series with Multiplatform Firmware . |
| Step 3 | Choose your phone model. |
| Step 4 | Choose Multiplatform Firmware . |
| Step 5 | In the Latest Releases folder, choose 11.0(2) . |
| Step 6 | Download the file cmterm-68xx.11-0-2MPP-98_REL.zip . |
| Step 7 | Unzip the files. |
| Step 8 | Put the files on the tftp, http, or https download directory. |
| Step 9 | Configure the Upgrade Rule on the Provisioning tab in the web page with the valid URL. The format is <schema>://<serv_ip[:port]>/<filepath>/sipxxx.loads The third-party call control can also upgrade via a URL in the web browser <schema>://<serv_ip[:port]>/<filepath>/sipxxx.loads Example http://10.74.10.225/firmware/sip68xx.11-0-2MPP-98.loads Note You must use the loads file in the URL. The zip file contains other files. | Note | You must use the loads file in the URL. The zip file contains other files. |
| Note | You must use the loads file in the URL. The zip file contains other files. |

| Note | You must use the loads file in the URL. The zip file contains other files. |
|---|---|

| Step 1 | To access Cisco Bug Search, go to: https://bst.cloudapps.cisco.com/bugsearch |
|---|---|
| Step 2 | Log in with your
                                 			 Cisco.com user ID and password. |
| Step 3 | To look for
                                 			 information about a specific problem, enter the bug ID number in the Search for
                                 			 field, then press Enter . |

| Note | A registered cisco.com user ID is required to access this information online. |
|---|---|