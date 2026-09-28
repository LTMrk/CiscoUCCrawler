---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cata-19x-3pcc-firmware-11-1-1-release-notes-at92-b-cisco-ata-191-and-192-htm-42b75e953b
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cata/19x/3PCC/firmware/11-1-1/release_notes/at92_b_cisco-ata-191-and-192.html
retrieved_at: 2026-08-22T01:11:56.148333+00:00
---

Cisco ATA 191 and 192 Analog Telephone Adapter Multiplatform Phones Release Notes for Firmware Release 11.1(0)

# Cisco ATA 191 and 192 Analog Telephone Adapter Multiplatform Phones Release Notes for Firmware Release 11.1(0)

### Download Options

Updated: April 3, 2018

First Published:

Last Updated:

Text Part Number:

# Introduction

These release notes support the Cisco ATA 191 and 192 Analog Telephone Adapter Multiplatform Phones running SIP Firmware Release 11.1(0).

The following table lists the support and protocol compatibility for the Cisco ATA.

Cisco IP Phone

Protocol

Support Requirements

Cisco ATA 191 and 192

SIP

BroadSoft BroadWorks 21.0

Asterisk 13.1

## Related
	 Documentation

Use the following sections to
		obtain related information.

### Cisco ATA 190 Series Documentation

Refer to publications that are specific to your language and call control system. Navigate from the following documentation URL:

https:/​/​www.cisco.com/​c/​en/​us/​products/​unified-communications/​ata-190-series-analog-telephone-adapters/​index.html

## New and Changed
	 Features

The following sections describe the features that are new or have
		changed in this release.

### Cisco ATA 191 and 192 Analogue Telephone Adapter

The Cisco ATA 191 and 192 Analog Telephone Adapter allow you to turn an analogue phone or fax communication devices into an IP phone. With these devices, you can retain your investment in your current equipment, but also benefit from an IP-based telephony network.

The ATA 191 and 192 support many of the current telephony features, including shared lines, conferencing, and voicemail. Both devices have two images or partitions in permanent storage, which allows the device to recover if the initial image is corrupted. With the dedicated Problem Report Tool button, you can quickly and easily collect troubleshooting information.

The Cisco ATA 191 and 192 both support IPv6, and SSH.

The ATA 191 and 192 easily integrate into your current network. Both devices have two RJ11 ports, each with a phone number. Both ATA devices have a RJ45 port that provides access to an Ethernet network. The Cisco ATA 192 has a RJ45 port for LAN use.

Basic network configuration can be done through an IVR system, and you use a web interface to monitor logs, view device information or do advanced configurations.

#### Where to Find More Information

Cisco ATA 191 and ATA 192 Analog Telephone Adapter Administration Guide for MultiPlatform Firmware

Cisco ATA 191 and ATA 192 Analog Telephone Adapter User Guide for MultiPlatform Firmware

## Installation

### Upgrade Firmware

The Cisco ATA 191 and 192 support dual image upgrades by TFTP, HTTP, or HTTPS.

http:/​/​software.cisco.com/​download/​navigator.html?mdfid=284883944&i=rm

<schema>://<serv_ip[:port]>/filepath/ATA19x.11-1-0MPP-23.img

Here is an example,

http://10.74.10.225/firmware/ATA19x.11-1-0MPP-23.img

The loads file is put in the file path of the above url. The zip file contains other file types also. Only the loads file is used in the above URL.

## Caveats

### View Caveat

You can search for caveats using the Cisco Bug Search.

Known caveats (bugs) are graded according to severity level, and can be either open or resolved.

To view caveats, you need the following items:

Internet connection

Web browser

Cisco.com user ID and password

Use this URL for all open caveats:

https:/​/​bst.cloudapps.cisco.com/​bugsearch/​search?kw=*&pf=prdNm&pfVal=286319456&sb=anfr&sts=open&bt=custV

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
| Cisco ATA 191 and 192 | SIP | BroadSoft BroadWorks 21.0 Asterisk 13.1 |

| Step 1 | Go to the following URL: http:/​/​software.cisco.com/​download/​navigator.html?mdfid=284883944&i=rm |
|---|---|
| Step 2 | Choose Cisco ATA 190 Series . |
| Step 3 | Choose your ATA model. |
| Step 4 | In the Latest Releases folder, choose 11.1(0) . |
| Step 5 | Download the file ATA19x.11-1-0MPP-23.zip. |
| Step 6 | Unzip the files. |
| Step 7 | Put the files on the tftp/http/https download directory. |
| Step 8 | Configure the Upgrade Rule on the Provisioning tab in the web page with the valid URL. The format is: <schema>://<serv_ip[:port]>/filepath/ATA19x.11-1-0MPP-23.img Here is an example, http://10.74.10.225/firmware/ATA19x.11-1-0MPP-23.img Note The loads file is put in the file path of the above url. The zip file contains other file types also. Only the loads file is used in the above URL. After the firmware upgrade completes, the phone reboots automatically. | Note | The loads file is put in the file path of the above url. The zip file contains other file types also. Only the loads file is used in the above URL. |
| Note | The loads file is put in the file path of the above url. The zip file contains other file types also. Only the loads file is used in the above URL. |

| Note | The loads file is put in the file path of the above url. The zip file contains other file types also. Only the loads file is used in the above URL. |
|---|---|

| Step 1 | Perform one of the following actions: Use this URL for all open caveats: https:/​/​bst.cloudapps.cisco.com/​bugsearch/​search?kw=*&pf=prdNm&pfVal=286319456&sb=anfr&sts=open&bt=custV |
|---|---|
| Step 2 | When prompted, log in with your Cisco.com user ID and password. |
| Step 3 | (Optional) Enter the bug ID number in the Search for field, then press Enter . |