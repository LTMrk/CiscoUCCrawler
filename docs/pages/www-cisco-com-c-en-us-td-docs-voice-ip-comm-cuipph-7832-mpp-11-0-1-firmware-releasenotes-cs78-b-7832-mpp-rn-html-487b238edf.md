---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cuipph-7832-mpp-11-0-1-firmware-releasenotes-cs78-b-7832-mpp-rn-html-487b238edf
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cuipph/7832-mpp/11-0-1/firmware/releasenotes/cs78_b_7832-mpp-rn.html
retrieved_at: 2026-08-21T13:22:59.982112+00:00
---

Cisco IP Conference Phone 7832 Multiplatform Phones Release Notes for Firmware Release 11.0(1)

# Cisco IP Conference Phone 7832 Multiplatform Phones Release Notes for Firmware Release 11.0(1)

### Download Options

Updated: August 14, 2017

First Published:

Last Updated:

Text Part Number:

# Introduction

These release notes support the Cisco IP Phone 7800 Series Multiplatform Phones running SIP Firmware Release 11.0(1).

The following table lists the support and protocol compatibility for the Cisco IP Phones.

Cisco IP Phone

Protocol

Support Requirements

Cisco IP Phone 7800 Series Multiplatform Phones

SIP

BroadSoft BroadWorks 21.0

Asterisk 13.1

## Related
	 Documentation

Use the following sections to
		obtain related information.

### Cisco IP Conference Phone 7832 Documentation

Refer to publications that are specific to your language and call control system. Navigate from the following documentation URL:

https:/​/​www.cisco.com/​c/​en/​us/​products/​collaboration-endpoints/​unified-ip-phone-7800-series/​index.html

## Cisco IP Conference Phone 7832 Multiplatform Phones

The Cisco IP Conference Phone 7832 Multiplatform Phones is an entry-level, cost-effective conference endpoint that provides superior HD audio performance for executive offices and small meeting rooms with up to six participants. It combines superior high-definition (HD) audio performance and 360-degree microphone coverage in a very sleek, approachable, and compact form to deliver easy-to-use audio conferencing.

The phone has four sensitive microphones with 360-degree coverage that allow users to speak in a normal voice and be heard clearly from up to 7 feet (2.1 m) away. The phone also features technology that resists interference from mobile phones and other wireless devices, assuring delivery of clear communications without distractions.

The key features of this conference phone are:

Encrypted voice communications for unparalleled security

Compact footprint design with 360-degree room coverage and no less than 7-ft (2.1-m) microphone pickup

3.4-inch (8.6-cm), 384x128-pixel monochrome LCD with backlit LED and antiglare bezel

Single line with multiple calls per line

Large mute button for easy access from all sides of the device

IEEE 802.3af Power over Ethernet (PoE) Class 2 for low power consumption

Codec supported include G.711(u/A), G.729a, G.729ab, iLBC, G.722, and OPUS

Secure Hash Algorithm (SHA)-256 enabled for advanced security features

### Where to Find Information

Cisco IP Conference Phone 7832 Multiplatform Phones User Guide

Cisco IP Conference Phone 7832 Multiplatform Phones Administration Guide

## Installation

### Upgrade Firmware

The Cisco IP Conference Phone 7832 Multiplatform Phones supports a single image upgrade by TFTP, HTTP, or HTTPS.

http:/​/​software.cisco.com/​download/​navigator.html?mdfid=284883944&i=rm

<schema>://<serv_ip[:port]>/filepath/sipxxx.loads

The third-party call control can also upgrade via a URL in the web browser:

<schema>://<serv_ip[:port]>/filepath/sipxxx.loads

Here is an example,

http://10.74.10.225/firmware/sip7832.11-0-0MPP-7dev.loads

The loads file is put in the file path of the above url. The zip file contains other file types also. Only the loads file is used in the above URL.

## Limitations and Restrictions

### Phone Behavior During Times of Network Congestion

Anything that degrades network performance can affect phone voice and video quality, and in some cases, can cause a call to drop. Sources of network degradation can include, but are not limited to, the following activities:

Administrative tasks, such as an internal port scan or security scan

Attacks that occur on your network, such as a Denial of Service attack

### Caller Identification and Other Phone Functions

Caller identification or other phone functions have not been verified with third-party applications for the visually or hearing impaired.

## Cisco IP Phone
	 Firmware Support Policy

For information on the support policy for phones, see http:/​/​www.cisco.com/​c/​en/​us/​support/​docs/​collaboration-endpoints/​unified-ip-phone-7900-series/​116684-technote-ipphone-00.html .

## Documentation, Service Requests, and Additional Information

For information on obtaining documentation, submitting a service request, and gathering additional information, see the monthly What’s New in Cisco Product Documentation , which also lists all new and revised Cisco technical documentation, at:

http:/​/​www.cisco.com/​c/​en/​us/​td/​docs/​general/​whatsnew/​whatsnew.html

Subscribe to the What’s New in Cisco Product Documentation as a Really Simple Syndication (RSS) feed and set content to be delivered directly to your desktop using a reader application. The RSS feeds are a free service and Cisco currently supports RSS Version 2.0.

| Cisco IP Phone | Protocol | Support Requirements |
|---|---|---|
| Cisco IP Phone 7800 Series Multiplatform Phones | SIP | BroadSoft BroadWorks 21.0 Asterisk 13.1 |

| Step 1 | Go to the following URL: http:/​/​software.cisco.com/​download/​navigator.html?mdfid=284883944&i=rm |
|---|---|
| Step 2 | Choose Cisco IP Phones 7800 Series . |
| Step 3 | Choose your phone model. |
| Step 4 | Choose Session Initiation Protocol (SIP) Software . |
| Step 5 | In the Latest Releases folder, choose 11.0(1) . |
| Step 6 | Download the file cmterm-7832.11-0-1MPP-473_REL.zip . |
| Step 7 | Unzip the files. |
| Step 8 | Put the files on the tftp/http/https download directory. |
| Step 9 | Configure the Upgrade Rule on the Provisioning tab in the web page with the valid URL. The format is: <schema>://<serv_ip[:port]>/filepath/sipxxx.loads The third-party call control can also upgrade via a URL in the web browser: <schema>://<serv_ip[:port]>/filepath/sipxxx.loads Here is an example, http://10.74.10.225/firmware/sip7832.11-0-0MPP-7dev.loads Note The loads file is put in the file path of the above url. The zip file contains other file types also. Only the loads file is used in the above URL. After the firmware upgrade completes, the phone reboots automatically. | Note | The loads file is put in the file path of the above url. The zip file contains other file types also. Only the loads file is used in the above URL. |
| Note | The loads file is put in the file path of the above url. The zip file contains other file types also. Only the loads file is used in the above URL. |

| Note | The loads file is put in the file path of the above url. The zip file contains other file types also. Only the loads file is used in the above URL. |
|---|---|