---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cuipph-3905-firmware-9-4-1-sr1-english-releasenotes-ip05-bk-304441da-00-3905-d3ebccbb4f
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cuipph/3905/firmware/9-4-1-SR1/english/releasenotes/IP05_BK_304441DA_00_3905-rn-941-sr1/IP05_BK_304441DA_00_3905-rn-941-sr1_chapter_00.html
retrieved_at: 2026-08-21T14:31:20.691803+00:00
---

Cisco Unified SIP Phone 3905 Release Notes for Firmware Release 9.4(1)SR1

# Cisco Unified SIP Phone 3905 Release Notes for Firmware Release 9.4(1)SR1

Updated: October 8, 2014

Chapter: Cisco Unified SIP Phone 3905 Release Notes for Firmware Release 9.4(1) SR1

## Chapter: Cisco Unified SIP Phone 3905 Release Notes for Firmware Release 9.4(1) SR1

# Cisco Unified SIP Phone 3905 Release Notes for Firmware Release 9.4(1) SR1

## Introduction

These release notes
		support the Cisco Unified SIP Phone 3905 running Firmware Release 9.4(1) SR1.

The following table
		lists the Cisco Unified Communications Manager release and protocol
		compatibility for the Cisco Unified SIP Phone 3905.

Cisco
					 Unified IP Phone

Protocol

Cisco
					 Unified Communications Manager

Cisco
					 Unified SIP Phone 3905

SIP

Cisco
					 Unified Communications Manager Release 7.1(5) and later.

## Related
	 Documentation

### Cisco Unified SIP Phone 3905 Documentation

Refer to publications that are specific to your language, phone model and Cisco Unified
				Communications Manager release. Navigate from the following documentation URL:

http:/​/​www.cisco.com/​c/​en/​us/​support/​collaboration-endpoints/​unified-sip-phone-3900-series/​tsd-products-support-series-home.html

### Cisco Unified
				Communications Manager Documentation

See the Cisco Unified
				Communications Manager Documentation Guide and other publications that are specific to your Cisco Unified
				Communications Manager release. Navigate from the following documentation URL:

http:/​/​www.cisco.com/​c/​en/​us/​support/​unified-communications/​unified-communications-manager-callmanager/​tsd-products-support-series-home.html

### Cisco Business Edition
				3000 Documentation

See the Cisco Business Edition
				3000 Documentation Guide and other publications that are specific to your Cisco Business Edition
				3000 release. Navigate from the following documentation URL:

http:/​/​www.cisco.com/​c/​en/​us/​support/​unified-communications/​business-edition-3000/​tsd-products-support-series-home.html

### Cisco Business Edition
				5000 Documentation

See the Cisco Business Edition
				5000 Documentation Guide and other publications that are specific to your Cisco Business Edition
				5000 release. Navigate from the following URL:

http:/​/​www.cisco.com/​c/​en/​us/​support/​unified-communications/​business-edition-5000/​tsd-products-support-series-home.html

## New and Changed Features

The following sections describe the features that are new or have changed in this release.

Failure to install the Device Package before the phone firmware upgrade may render the phones unusable.

- Features Available
	 with Firmware Release

### Features Available
	 with Firmware Release

The following sections describe the features available with the Firmware
		Release.

- Call Admission
	 Control

#### Call Admission
	 Control

The Call Admission Control feature enables the user to hear a fast busy tone and see the message Not enough bandwidth on the phone LCD when the Cisco Unified Communications Manager rejects the call because of bandwidth or policy reasons.

If users see frequent Not enough bandwidth messages, the administrator may need to change the  available bandwidth on the Cisco Unified Communications Manager.

## Installation

- Install Firmware
	 Release on Cisco Unified Communications Manager

- Install Firmware
	 Zip Files

### Install Firmware
	 Release on Cisco Unified Communications Manager

Before using the
		  Cisco Unified SIP Phone 3905 Firmware Release 9.4(1) SR1 with Cisco Unified
		  Communications Manager, you must install the latest firmware on all Cisco
		  Unified Communications Manager servers in the cluster.

http:/​/​software.cisco.com/​download/​navigator.html?mdfid=280896546&i=rm

cmterm-3905.9-4-1SR1-3.cop.sgn

If you added
				  the firmware file to the cart, click the Download Cart link when you are ready to download
				  the file.

cmterm-3905-sip-9-4-1SR1-3-readme.html

### Install Firmware
	 Zip Files

If a Cisco Unified
		  Communications Manager is not available to load the installer program, the
		  following .zip files are available to load the firmware.

cmterm-3905.9-4-1SR1-3.zip

Firmware upgrades
		  over the WLAN interface may take longer than upgrades using a wired connection.
		  Upgrade times over the WLAN interface may take more than an hour, depending on
		  the quality and bandwidth of the wireless connection.

http:/​/​software.cisco.com/​download/​navigator.html?mdfid=284883944&i=rm

## Limitations and Restrictions

### Voice VLAN and
	 IPv6 Limitation

If the PC attached to the PC port of the phone is using IPv6, we
		  recommend that the PC Voice LAN access be disabled. This ensures that the PC
		  can connect to the Voice VLAN.

### Phone Behavior During Times of Network Congestion

Anything that degrades network performance can
affect  Cisco IP Phone voice
and video quality, and in some cases, can
cause a call to drop. Sources of
network degradation can include, but are not limited to, the
following activities:

Administrative
tasks, such as an internal port scan or security scan

Attacks that
occur on your network, such as a Denial of Service
attack

To reduce or eliminate any adverse effects
to the phones, schedule administrative network tasks during a
time when the phones are not being used or exclude the phones
from testing.

## Unified
	 Communications Manager Endpoints Locale Installer

By default, Cisco
		  IP Phones are set up for the English (United States) locale. To use the Cisco
		  IP phones in other locales, you must install the locale-specific version of the
		  Unified Communications Manager Endpoints Locale Installer on every Cisco
		  Unified Communications Manager server in the cluster. The Locale Installer
		  installs the latest translated text for the phone user interface and
		  country-specific phone tones on your system so that they are available for the
		  Cisco IP Phones.

To access the
		  Locale Installer required for a release, access http:/​/​software.cisco.com/​download/​navigator.html?mdfid=286037605&flowid=46245 , navigate to your phone model, and
		  select the Unified Communications Manager Endpoints Locale Installer link.

For more
		  information, see the "Locale
			 Installer" section in the Cisco Unified
			 Communications Operating System Administration Guide .

The latest
			 Locale Installer may not be immediately available; continue to check the
			 website for updates.

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
		  problems by using the Cisco Bug Search.

To access Cisco Bug
		  Search, you need the following items:

Internet
				connection

Web browser

Cisco.com user
				ID and password

https:/​/​tools.cisco.com/​bugsearch

### Open Caveats

The following
		  table lists severity 1, 2, and 3 defects that are open for the Cisco Unified SIP Phone 3905
		  for Firmware Release 9.4(1)SR1.

For more
		  information about an individual defect, you can access the online record for
		  the defect using the Bug Toolkit. You
		  must be a registered Cisco.com user to access this online information.

Because defect
		  status continually changes, the table reflects a snapshot of the defects that
		  were open at the time this report was compiled. For an updated view of open
		  defects, access Bug Toolkit as described in Access Cisco Bug Search .

CSCug96869

Not request new address after DHCPv6 assigned address
duplicated

CSCuh02720

Take long time to bootup if DHCPv4 server shutdown

CSCuh10981

No DSCP to 802.1Q priority mapping for both IPv4 and IPv6

CSCuh15911

Phone should keep re-provision if version stamp mismatch

CSCuh51331

Phone stuck after IPv6 isic6 attack

CSCuh91119

Phone stuck during Codenomicon HTTP Server/TCP for IPv4 suite
testing

CSCui16740

Attack RTP port during active call, one-way voice occurs

CSCui21409

3905:DUT will restart and change IPv6 address when running
ISIC

CSCui57035

Phone stuck after 10 hours DHCP_option and VLAN_Flapping
stress

CSCuj73157

Not re-request config file if get TFTP "Disk full or allocation
exceed"

CSCun58512

Can't transfer after set CFwdAll and answer call in same pickup
group

### Resolved Caveats

The following
		  table lists severity 1, 2, and 3 defects that are resolved for the Cisco Unified SIP Phone 3905
		  for Firmware Release 9.4(1)SR1.

For more
		  information about an individual defect, you can access the online record for
		  the defect using the Bug Toolkit. You
		  must be a registered Cisco.com user to access this online information.

Because defect
		  status continually changes, the table reflects a snapshot of the defects that
		  were resolved at the time this report was compiled. For an updated view of open
		  defects, access Bug Toolkit as described in Access Cisco Bug Search .

CSCun72951

3905 stuck in provisioning

CSCuo28512

phone receives 403 sip error message for an outgoing call, 3905
do not give a busy tone

CSCuo52986

pick up group display issue

CSCuo99664

CP-3905 fails to transfer call after pickup

CSCup05346

3905 randomly request FAC codes

CSCup14852

3905 phone is not resolving DNS

CSCup79831

3905 phones do not increase the seconds elapsed counter in DHCP
requests

CSCup92407

CP-3905 unable to transfer call

CSCuq33263

Issue with 3905 phone facing audio issues

CSCuq51995

One-way audio for PSTN calls transferred to internal number

## Documentation Updates

The following sections contain updates to the documentation that apply to this release. The updates will be applied to the documentation when the next major firmware release occurs.

- Administration Guide

- User Guide

### Administration Guide

The following sections describe changes that apply to the Cisco Unified SIP Phone 3905 Administration Guide for Cisco Unified Communications Manager 10.0 (SIP) . The document will be updated for the next major firmware release.

- Phone Bandwidth Restrictions

#### Phone Bandwidth Restrictions

This section to be added to the "Troubleshooting" chapter, under the "General Telephone Call Problems" section.

##### Problem

Users report frequent Not  enough bandwidth messages on their phones.

##### Cause

The Cisco Unified Communications Manager  does not have adequate bandwidth to place the call or there are policy restrictions.

##### Solution

For information on changing the Cisco Unified Communications Manager  bandwidth, see the Features and Services Guide for Cisco Unified Communications Manager and the Cisco Unified Communications Manager System Guide .

### User Guide

The following sections describe changes that apply to the Cisco Unified SIP Phone 3905 User Guide for Cisco Unified Communications Manager 10.0 (SIP) . The document will be updated for the next major firmware release.

- Make Calls

#### Make Calls

The following information will be added to the "Make Calls" section of the next version of the User Guide.

When you hear a fast busy tone and see the message Not enough bandwidth on the phone LCD, the Cisco Unified Communications Manager cannot place the call because of insufficient bandwidth or policy reasons. You should retry the call in a few minutes. If you see this message frequently, contact your system administrator.

## Cisco IP Phone
	 Firmware Support Policy

For information on
		  the support policy for Cisco IP Phones, see http:/​/​www.cisco.com/​c/​en/​us/​support/​docs/​collaboration-endpoints/​unified-ip-phone-7900-series/​116684-technote-ipphone-00.html .

## Documentation, Service Requests, and Additional Information

For information on obtaining documentation, submitting a service request, and gathering additional information, see the monthly What’s New in Cisco Product Documentation , which also lists all new and revised Cisco technical documentation, at:

http:/​/​www.cisco.com/​c/​en/​us/​td/​docs/​general/​whatsnew/​whatsnew.html

Subscribe to the What’s New in Cisco Product Documentation as a Really Simple Syndication (RSS) feed and set content to be delivered directly to your desktop using a reader application. The RSS feeds are a free service and Cisco currently supports RSS Version 2.0.

| Cisco
					 Unified IP Phone | Protocol | Cisco
					 Unified Communications Manager |
|---|---|---|
| Cisco
					 Unified SIP Phone 3905 | SIP | Cisco
					 Unified Communications Manager Release 7.1(5) and later. |

| Note | Failure to install the Device Package before the phone firmware upgrade may render the phones unusable. |
|---|---|

| Step 1 | Go to the
			 following URL: http:/​/​software.cisco.com/​download/​navigator.html?mdfid=280896546&i=rm |
|---|---|
| Step 2 | Choose Cisco
				Unified SIP Phone 3900 Series . |
| Step 3 | Choose Cisco Unified SIP Phone 3905 . |
| Step 4 | Choose Session Initiation Protocol (SIP) Software . |
| Step 5 | In the Latest
			 Releases folder, choose 9.4(1)SR1 . |
| Step 6 | Select the
			 following firmware file, click the Download or Add to
				cart button, and follow the prompts: cmterm-3905.9-4-1SR1-3.cop.sgn Note If you added
				  the firmware file to the cart, click the Download Cart link when you are ready to download
				  the file. | Note | If you added
				  the firmware file to the cart, click the Download Cart link when you are ready to download
				  the file. |
| Note | If you added
				  the firmware file to the cart, click the Download Cart link when you are ready to download
				  the file. |
| Step 7 | Click the + next to the firmware file name in the Download
			 Cart section to access additional information about this file. The hyperlink
			 for the readme file is in the Additional Information section, which contains
			 installation instructions for the corresponding firmware: cmterm-3905-sip-9-4-1SR1-3-readme.html |
| Step 8 | Follow the
			 instructions in the readme file to install the firmware. |

| Note | If you added
				  the firmware file to the cart, click the Download Cart link when you are ready to download
				  the file. |
|---|---|

| Step 1 | Go to the
			 following URL: http:/​/​software.cisco.com/​download/​navigator.html?mdfid=284883944&i=rm |
|---|---|
| Step 2 | Choose Cisco
				Unified SIP Phone 3900 Series . |
| Step 3 | Choose Cisco Unified SIP Phone 3905 . |
| Step 4 | Choose Session Initiation Protocol (SIP) Software . |
| Step 5 | In the Latest
			 Releases folder, choose 9.4(1)SR1 . |
| Step 6 | Download the
			 relevant zip files. |
| Step 7 | Unzip the
			 files. |
| Step 8 | Manually copy
			 the unzipped files to the directory on the TFTP server. See Cisco
				Unified Communications Operating System Administration Guide for
			 information about how to manually copy the firmware files to the server. |

| Note | The latest
			 Locale Installer may not be immediately available; continue to check the
			 website for updates. |
|---|---|

| Step 1 | To access the
			 Cisco Bug Search, go to: https:/​/​tools.cisco.com/​bugsearch |
|---|---|
| Step 2 | Log in with your
			 Cisco.com user ID and password. |
| Step 3 | To look for
			 information about a specific problem, enter the bug ID number in the Search for
			 field, then press Enter . |

| Identifier | Headline |
|---|---|
| CSCug96869 | Not request new address after DHCPv6 assigned address
duplicated |
| CSCuh02720 | Take long time to bootup if DHCPv4 server shutdown |
| CSCuh10981 | No DSCP to 802.1Q priority mapping for both IPv4 and IPv6 |
| CSCuh15911 | Phone should keep re-provision if version stamp mismatch |
| CSCuh51331 | Phone stuck after IPv6 isic6 attack |
| CSCuh91119 | Phone stuck during Codenomicon HTTP Server/TCP for IPv4 suite
testing |
| CSCui16740 | Attack RTP port during active call, one-way voice occurs |
| CSCui21409 | 3905:DUT will restart and change IPv6 address when running
ISIC |
| CSCui57035 | Phone stuck after 10 hours DHCP_option and VLAN_Flapping
stress |
| CSCuj73157 | Not re-request config file if get TFTP "Disk full or allocation
exceed" |
| CSCun58512 | Can't transfer after set CFwdAll and answer call in same pickup
group |

| Identifier | Headline |
|---|---|
| CSCun72951 | 3905 stuck in provisioning |
| CSCuo28512 | phone receives 403 sip error message for an outgoing call, 3905
do not give a busy tone |
| CSCuo52986 | pick up group display issue |
| CSCuo99664 | CP-3905 fails to transfer call after pickup |
| CSCup05346 | 3905 randomly request FAC codes |
| CSCup14852 | 3905 phone is not resolving DNS |
| CSCup79831 | 3905 phones do not increase the seconds elapsed counter in DHCP
requests |
| CSCup92407 | CP-3905 unable to transfer call |
| CSCuq33263 | Issue with 3905 phone facing audio issues |
| CSCuq51995 | One-way audio for PSTN calls transferred to internal number |

| Note | This section to be added to the "Troubleshooting" chapter, under the "General Telephone Call Problems" section. |
|---|---|

| Note | The following information will be added to the "Make Calls" section of the next version of the User Guide. |
|---|---|